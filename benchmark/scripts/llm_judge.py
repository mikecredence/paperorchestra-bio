"""
llm_judge.py — LLM-as-judge evaluation for BiomedWritingBench.

Compares a generated paper section against a ground truth section using
Claude as a side-by-side judge. Supports evaluation on individual axes
(clarity, rigor, completeness, writing, presentation, citations) or all
axes at once via --batch mode.

Usage:
    python llm_judge.py --generated section_gen.tex \
                        --ground-truth section_gt.tex \
                        --axis clarity

    python llm_judge.py --generated section_gen.tex \
                        --ground-truth section_gt.tex \
                        --batch

    python llm_judge.py --generated section_gen.tex \
                        --ground-truth section_gt.tex \
                        --axis rigor --dry-run
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MODEL = "claude-sonnet-4-20250514"

AXES = [
    "clarity",
    "rigor",
    "completeness",
    "writing",
    "presentation",
    "citations",
    "overall",
]

AXIS_DESCRIPTIONS: dict[str, str] = {
    "clarity": (
        "Clarity — How clear, readable, and easy to follow is the text? "
        "Consider logical flow, sentence structure, and whether the main "
        "points are communicated effectively."
    ),
    "rigor": (
        "Scientific Rigor — How accurate, precise, and methodologically "
        "sound is the content? Consider correctness of claims, appropriate "
        "use of evidence, and avoidance of unsupported assertions."
    ),
    "completeness": (
        "Completeness — How thoroughly does the section cover the expected "
        "content? Consider whether key concepts, methods, results, or "
        "arguments are present and sufficiently detailed."
    ),
    "writing": (
        "Writing Quality — How polished is the prose? Consider grammar, "
        "word choice, conciseness, and overall stylistic quality appropriate "
        "for a biomedical research paper."
    ),
    "presentation": (
        "Presentation — How well is the information organized and formatted? "
        "Consider use of structure (paragraphs, sub-headings), figures/tables "
        "references, and overall document layout."
    ),
    "citations": (
        "Citation Quality — How appropriate and complete are the citations? "
        "Consider whether key claims are supported by references, whether "
        "the cited works are relevant, and whether important references are "
        "missing."
    ),
    "overall": (
        "Overall Quality — Holistic assessment of the section considering "
        "all dimensions: clarity, rigor, completeness, writing quality, "
        "presentation, and citations."
    ),
}


# ---------------------------------------------------------------------------
# LaTeX stripping
# ---------------------------------------------------------------------------

def strip_latex(text: str) -> str:
    """Strip common LaTeX commands to produce approximate plain text.

    This is intentionally simple — it handles the most common constructs
    found in biomedical paper sections without requiring a full LaTeX parser.
    """
    # Remove comments (lines starting with %)
    text = re.sub(r"(?m)^%.*$", "", text)
    text = re.sub(r"(?<!\\)%.*$", "", text, flags=re.MULTILINE)

    # Remove \begin{...} and \end{...}
    text = re.sub(r"\\(begin|end)\{[^}]*\}", "", text)

    # Remove \label{...}, \ref{...}, \cite{...}, \eqref{...}
    text = re.sub(r"\\(label|ref|cite|citep|citet|eqref|autoref)\{[^}]*\}", "", text)

    # Remove \command{content} but keep content for formatting commands
    text = re.sub(
        r"\\(textbf|textit|emph|underline|textrm|textsc|textsf|texttt|"
        r"section|subsection|subsubsection|paragraph|caption)\*?\{([^}]*)\}",
        r"\2",
        text,
    )

    # Remove remaining \command{...} patterns (drop content)
    text = re.sub(r"\\[a-zA-Z]+\*?\{[^}]*\}", "", text)

    # Remove \command without braces (e.g., \noindent, \newline)
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)

    # Remove remaining braces
    text = text.replace("{", "").replace("}", "")

    # Remove math delimiters
    text = re.sub(r"\$\$?", "", text)

    # Collapse whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

def build_judge_prompt(
    text_a: str,
    text_b: str,
    axis: str,
) -> str:
    """Construct the judge prompt for a single evaluation axis.

    Section A is always the generated text and Section B is the ground truth,
    but the prompt does not reveal which is which to avoid bias.
    """
    axis_desc = AXIS_DESCRIPTIONS[axis]

    prompt = f"""\
You are an expert biomedical research reviewer acting as a judge in a \
side-by-side evaluation. You will be given two versions of a paper section \
(Section A and Section B). Evaluate both on the following axis:

{axis_desc}

Instructions:
1. Read both sections carefully.
2. Score each section from 0 to 100 on the axis described above.
3. Determine a winner: "A", "B", or "tie" (if scores are within 3 points).
4. Provide a brief rationale (2-4 sentences) explaining your judgment.

You MUST respond with valid JSON in exactly this format (no other text):
{{
  "axis": "{axis}",
  "score_a": <int 0-100>,
  "score_b": <int 0-100>,
  "winner": "<A|B|tie>",
  "rationale": "<brief explanation>"
}}

--- SECTION A ---
{text_a}

--- SECTION B ---
{text_b}

Respond with the JSON evaluation only."""

    return prompt


def build_absolute_prompt(text: str, axis: str) -> str:
    """Construct a prompt for absolute scoring of a single paper (no comparison).

    Used when ground truth full text is unavailable.
    """
    axis_desc = AXIS_DESCRIPTIONS[axis]

    prompt = f"""\
You are an expert biomedical research reviewer. You will be given a generated \
research paper (or section). Score it on the following axis:

{axis_desc}

Instructions:
1. Read the paper carefully.
2. Score the paper from 0 to 100 on the axis described above.
3. Provide a brief rationale (2-4 sentences) explaining your judgment.
4. List 1-3 specific suggestions for improvement.

Scoring guide:
  90-100: Publication-ready, excellent quality
  75-89:  Good quality, minor issues
  60-74:  Acceptable, noticeable weaknesses
  40-59:  Below average, significant issues
  0-39:   Poor, major problems

You MUST respond with valid JSON in exactly this format (no other text):
{{
  "axis": "{axis}",
  "score": <int 0-100>,
  "rationale": "<brief explanation>",
  "suggestions": ["<suggestion 1>", "<suggestion 2>"]
}}

--- PAPER ---
{text}

Respond with the JSON evaluation only."""

    return prompt


# ---------------------------------------------------------------------------
# API interaction
# ---------------------------------------------------------------------------

def call_judge(prompt: str) -> dict:
    """Call the Anthropic API with the judge prompt and parse the response.

    Returns the parsed JSON evaluation dict.
    Raises RuntimeError on API or parsing failures.
    """
    try:
        import anthropic
    except ImportError:
        print(
            "Error: The 'anthropic' package is not installed.\n"
            "Install it by running:  uv add anthropic\n"
            "Then try again.",
            file=sys.stderr,
        )
        sys.exit(1)

    client = anthropic.Anthropic()

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract text from the response
    raw_text = response.content[0].text.strip()

    # Try to parse JSON from the response. The model should return pure JSON,
    # but sometimes wraps it in markdown code fences.
    json_match = re.search(r"\{.*\}", raw_text, re.DOTALL)
    if not json_match:
        raise RuntimeError(f"Could not extract JSON from model response:\n{raw_text}")

    try:
        result = json.loads(json_match.group())
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Failed to parse JSON from model response:\n{raw_text}"
        ) from exc

    # Validate expected keys
    for key in ("score_a", "score_b", "winner", "rationale"):
        if key not in result:
            raise RuntimeError(f"Missing key '{key}' in model response: {result}")

    return result


# ---------------------------------------------------------------------------
# Evaluation orchestration
# ---------------------------------------------------------------------------

def evaluate_axis(
    generated_text: str,
    gt_text: str | None,
    axis: str,
    dry_run: bool = False,
    absolute: bool = False,
) -> dict:
    """Evaluate a single axis. Returns the evaluation dict or the prompt (dry run)."""
    if absolute or gt_text is None:
        prompt = build_absolute_prompt(generated_text, axis)
    else:
        prompt = build_judge_prompt(generated_text, gt_text, axis)

    if dry_run:
        return {"axis": axis, "prompt": prompt}

    result = call_judge(prompt)
    result["axis"] = axis
    result["mode"] = "absolute" if (absolute or gt_text is None) else "side_by_side"
    return result


def evaluate_batch(
    generated_text: str,
    gt_text: str | None,
    dry_run: bool = False,
    absolute: bool = False,
) -> list[dict]:
    """Evaluate all non-overall axes plus the overall axis."""
    axes_to_run = [a for a in AXES if a != "overall"] + ["overall"]
    results: list[dict] = []

    for axis in axes_to_run:
        result = evaluate_axis(generated_text, gt_text, axis,
                               dry_run=dry_run, absolute=absolute)
        results.append(result)
        if not dry_run:
            print(f"  Evaluated: {axis}", file=sys.stderr)

    return results


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_output(results: list[dict], dry_run: bool = False) -> str:
    """Format evaluation results as JSON."""
    if dry_run:
        # In dry-run mode, show the prompts that would be sent
        output = {
            "mode": "dry_run",
            "evaluations": results,
        }
    elif len(results) == 1:
        output = results[0]
    else:
        # Batch mode: include individual results and a summary
        output = {
            "mode": "batch",
            "model": MODEL,
            "evaluations": results,
            "summary": _build_summary(results),
        }
    return json.dumps(output, indent=2)


def _build_summary(results: list[dict]) -> dict:
    """Build a summary across multiple axis evaluations."""
    valid = [r for r in results if "score_a" in r and "score_b" in r]
    if not valid:
        return {}

    avg_a = sum(r["score_a"] for r in valid) / len(valid)
    avg_b = sum(r["score_b"] for r in valid) / len(valid)

    a_wins = sum(1 for r in valid if r.get("winner") == "A")
    b_wins = sum(1 for r in valid if r.get("winner") == "B")
    ties = sum(1 for r in valid if r.get("winner") == "tie")

    return {
        "avg_score_a": round(avg_a, 1),
        "avg_score_b": round(avg_b, 1),
        "a_wins": a_wins,
        "b_wins": b_wins,
        "ties": ties,
        "overall_winner": (
            "A" if avg_a > avg_b + 2
            else "B" if avg_b > avg_a + 2
            else "tie"
        ),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "LLM-as-Judge Evaluation for BiomedWritingBench. "
            "Uses Claude to compare a generated paper section against a "
            "ground truth section on one or more evaluation axes."
        ),
    )
    parser.add_argument(
        "--generated",
        required=True,
        help="Path to the generated LaTeX section file.",
    )
    parser.add_argument(
        "--ground-truth",
        default=None,
        help="Path to the ground truth LaTeX section file. "
             "Not required when using --absolute mode.",
    )
    parser.add_argument(
        "--absolute",
        action="store_true",
        help="Score a single paper without side-by-side comparison. "
             "Use when ground truth full text is unavailable.",
    )

    axis_group = parser.add_mutually_exclusive_group(required=True)
    axis_group.add_argument(
        "--axis",
        choices=AXES,
        help=(
            "Evaluation axis. One of: "
            + ", ".join(AXES)
            + "."
        ),
    )
    axis_group.add_argument(
        "--batch",
        action="store_true",
        help="Evaluate all axes (clarity, rigor, completeness, writing, "
             "presentation, citations, overall).",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the judge prompt(s) without calling the API.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help=f"Override the default model. Default: {MODEL}.",
    )
    return parser


def main() -> None:
    """Entry point for llm_judge evaluation."""
    global MODEL

    parser = build_parser()
    args = parser.parse_args()

    if args.model:
        MODEL = args.model

    # Validate paths
    if not Path(args.generated).is_file():
        print(f"Error: Generated file not found: {args.generated}", file=sys.stderr)
        sys.exit(1)

    if not args.absolute and args.ground_truth and not Path(args.ground_truth).is_file():
        print(f"Error: Ground truth file not found: {args.ground_truth}", file=sys.stderr)
        sys.exit(1)

    if not args.absolute and not args.ground_truth:
        print("Error: --ground-truth is required unless using --absolute mode.", file=sys.stderr)
        sys.exit(1)

    # Read and strip LaTeX
    generated_raw = Path(args.generated).read_text(encoding="utf-8")
    generated_text = strip_latex(generated_raw)

    gt_text = None
    if args.ground_truth and not args.absolute:
        gt_raw = Path(args.ground_truth).read_text(encoding="utf-8")
        gt_text = strip_latex(gt_raw)

    if not generated_text.strip():
        print("Warning: Generated file produced empty text after LaTeX stripping.", file=sys.stderr)
    if gt_text is not None and not gt_text.strip():
        print("Warning: Ground truth file produced empty text after LaTeX stripping.", file=sys.stderr)

    # Evaluate
    if args.batch:
        results = evaluate_batch(generated_text, gt_text,
                                 dry_run=args.dry_run, absolute=args.absolute)
    else:
        result = evaluate_axis(generated_text, gt_text, args.axis,
                               dry_run=args.dry_run, absolute=args.absolute)
        results = [result]

    # Output
    print(format_output(results, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
