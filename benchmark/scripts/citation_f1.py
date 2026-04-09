"""
citation_f1.py — Citation F1 evaluation for BiomedWritingBench.

Computes precision, recall, and F1 for generated citations compared against
a ground truth reference list. Uses fuzzy title matching (SequenceMatcher)
to account for minor formatting differences between generated and reference
citation titles.

Usage:
    python citation_f1.py --generated-bib path/to/generated.bib \
                          --ground-truth path/to/ground_truth.json

    python citation_f1.py --generated-bib path/to/generated.bib \
                          --ground-truth path/to/ground_truth.json --json
"""

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path


# ---------------------------------------------------------------------------
# BibTeX parsing
# ---------------------------------------------------------------------------

def extract_titles_from_bib(bib_path: str) -> list[str]:
    """Extract all title fields from a BibTeX file using regex.

    Handles both brace-delimited and quote-delimited title values,
    including multi-line values. Returns a list of cleaned title strings.
    """
    text = Path(bib_path).read_text(encoding="utf-8")

    # Match title = {…} or title = "…", allowing multiline content.
    # We first try brace-delimited (most common), then quote-delimited.
    brace_pattern = re.compile(
        r"title\s*=\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}",
        re.IGNORECASE | re.DOTALL,
    )
    quote_pattern = re.compile(
        r'title\s*=\s*"([^"]*)"',
        re.IGNORECASE | re.DOTALL,
    )

    titles: list[str] = []
    for match in brace_pattern.finditer(text):
        titles.append(_clean_title(match.group(1)))
    for match in quote_pattern.finditer(text):
        titles.append(_clean_title(match.group(1)))

    return titles


def _clean_title(raw: str) -> str:
    """Normalize a raw title string extracted from BibTeX."""
    # Remove LaTeX commands like \textit{}, \emph{}, etc.
    cleaned = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", raw)
    # Remove stray braces used for capitalization protection
    cleaned = cleaned.replace("{", "").replace("}", "")
    # Collapse whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


# ---------------------------------------------------------------------------
# Ground truth loading
# ---------------------------------------------------------------------------

def load_ground_truth(gt_path: str) -> list[str]:
    """Load ground truth citation titles from a JSON file.

    Expected format — either a plain list of strings:
        ["Title one", "Title two", ...]

    Or an object with a "titles" key:
        {"titles": ["Title one", "Title two", ...]}
    """
    data = json.loads(Path(gt_path).read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [str(t).strip() for t in data]
    if isinstance(data, dict) and "titles" in data:
        return [str(t).strip() for t in data["titles"]]
    raise ValueError(
        "Ground truth JSON must be a list of strings or an object with a 'titles' key."
    )


# ---------------------------------------------------------------------------
# Fuzzy matching
# ---------------------------------------------------------------------------

def fuzzy_match(
    generated_titles: list[str],
    gt_titles: list[str],
    threshold: float = 0.75,
) -> dict:
    """Match generated citation titles against ground truth using SequenceMatcher.

    Returns a dict with:
        true_positives  — list of (generated_title, matched_gt_title, score)
        false_positives — list of generated titles with no match
        false_negatives — list of ground truth titles not matched
    """
    # Track which GT titles have been claimed by a match.
    gt_matched: set[int] = set()
    true_positives: list[tuple[str, str, float]] = []
    false_positives: list[str] = []

    for gen_title in generated_titles:
        best_score = 0.0
        best_idx = -1
        gen_lower = gen_title.lower()

        for idx, gt_title in enumerate(gt_titles):
            if idx in gt_matched:
                continue
            score = SequenceMatcher(None, gen_lower, gt_title.lower()).ratio()
            if score > best_score:
                best_score = score
                best_idx = idx

        if best_score >= threshold and best_idx >= 0:
            true_positives.append((gen_title, gt_titles[best_idx], best_score))
            gt_matched.add(best_idx)
        else:
            false_positives.append(gen_title)

    false_negatives = [
        gt_titles[i] for i in range(len(gt_titles)) if i not in gt_matched
    ]

    return {
        "true_positives": true_positives,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
    }


# ---------------------------------------------------------------------------
# Metric computation
# ---------------------------------------------------------------------------

def compute_f1(match_result: dict) -> dict:
    """Compute precision, recall, and F1 from a match result dict."""
    tp = len(match_result["true_positives"])
    fp = len(match_result["false_positives"])
    fn = len(match_result["false_negatives"])

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp_count": tp,
        "fp_count": fp,
        "fn_count": fn,
    }


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_human_readable(metrics: dict, match_result: dict) -> str:
    """Return a human-readable report string."""
    lines: list[str] = []
    lines.append("=" * 60)
    lines.append("Citation F1 Evaluation — BiomedWritingBench")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"  Precision : {metrics['precision']:.4f}")
    lines.append(f"  Recall    : {metrics['recall']:.4f}")
    lines.append(f"  F1        : {metrics['f1']:.4f}")
    lines.append("")
    lines.append(
        f"  True Positives  : {metrics['tp_count']}  |  "
        f"False Positives : {metrics['fp_count']}  |  "
        f"False Negatives : {metrics['fn_count']}"
    )

    if match_result["true_positives"]:
        lines.append("")
        lines.append("--- True Positives (generated -> ground truth) ---")
        for gen, gt, score in match_result["true_positives"]:
            lines.append(f"  [{score:.2f}]  {gen}")
            lines.append(f"       -> {gt}")

    if match_result["false_positives"]:
        lines.append("")
        lines.append("--- False Positives (generated, no match in ground truth) ---")
        for title in match_result["false_positives"]:
            lines.append(f"  - {title}")

    if match_result["false_negatives"]:
        lines.append("")
        lines.append("--- False Negatives (ground truth, not found in generated) ---")
        for title in match_result["false_negatives"]:
            lines.append(f"  - {title}")

    lines.append("")
    return "\n".join(lines)


def format_json(metrics: dict, match_result: dict) -> str:
    """Return a JSON-formatted report string."""
    output = {
        "precision": round(metrics["precision"], 4),
        "recall": round(metrics["recall"], 4),
        "f1": round(metrics["f1"], 4),
        "tp_count": metrics["tp_count"],
        "fp_count": metrics["fp_count"],
        "fn_count": metrics["fn_count"],
        "true_positives": [
            {"generated": gen, "ground_truth": gt, "similarity": round(score, 4)}
            for gen, gt, score in match_result["true_positives"]
        ],
        "false_positives": match_result["false_positives"],
        "false_negatives": match_result["false_negatives"],
    }
    return json.dumps(output, indent=2)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Citation F1 Evaluation for BiomedWritingBench. "
            "Compares generated BibTeX citations against a ground truth "
            "reference list using fuzzy title matching."
        ),
    )
    parser.add_argument(
        "--generated-bib",
        required=True,
        help="Path to the generated .bib (BibTeX) file.",
    )
    parser.add_argument(
        "--ground-truth",
        required=True,
        help=(
            "Path to ground truth JSON file containing a list of citation "
            "titles (either a plain list or an object with a 'titles' key)."
        ),
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.75,
        help="Fuzzy matching threshold (0-1). Default: 0.75.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as machine-readable JSON.",
    )
    return parser


def main() -> None:
    """Entry point for citation_f1 evaluation."""
    parser = build_parser()
    args = parser.parse_args()

    # Validate paths
    if not Path(args.generated_bib).is_file():
        print(f"Error: Generated .bib file not found: {args.generated_bib}", file=sys.stderr)
        sys.exit(1)
    if not Path(args.ground_truth).is_file():
        print(f"Error: Ground truth JSON file not found: {args.ground_truth}", file=sys.stderr)
        sys.exit(1)

    # Extract and load
    generated_titles = extract_titles_from_bib(args.generated_bib)
    gt_titles = load_ground_truth(args.ground_truth)

    if not generated_titles:
        print("Warning: No titles found in the generated .bib file.", file=sys.stderr)
    if not gt_titles:
        print("Warning: No titles found in the ground truth file.", file=sys.stderr)

    # Match and score
    match_result = fuzzy_match(generated_titles, gt_titles, threshold=args.threshold)
    metrics = compute_f1(match_result)

    # Output
    if args.json_output:
        print(format_json(metrics, match_result))
    else:
        print(format_human_readable(metrics, match_result))


if __name__ == "__main__":
    main()
