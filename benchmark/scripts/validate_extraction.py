#!/usr/bin/env python3
"""
Validate extraction quality: count numeric values, statistical reports,
and banned qualitative table cells.

Usage:
    # Compare v2 and v3 for a paper
    python validate_extraction.py --paper a-hippocampus-accumbens-code-guides-goal-directed-

    # Validate all rich_inputs
    python validate_extraction.py --all
"""
import sys
import re
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import BENCHMARK_DIR

RICH_INPUTS = BENCHMARK_DIR / "rich_inputs"

# Banned qualitative words (within table rows only — these are flagged when
# they appear as standalone cell values in markdown tables).
BANNED_CELL_WORDS = {
    "Higher", "Lower", "High", "Low", "Enriched", "Improved", "Better", "Worse",
    "Enhanced", "Moderate", "Strong", "Weak", "Larger", "Smaller", "Stronger",
    "Weaker", "Comparable", "Competitive", "Detected", "Increased", "Decreased",
    "Above chance", "Near 1:1", "Significant",
}

# Numeric value pattern (broad)
NUM_PATTERN = re.compile(r"\b-?\d+\.?\d*(?:[eE][-+]?\d+)?\b")

# Statistical report signatures
STAT_SIGNATURES = [
    r"F\s*\(",                              # F(df)
    r"\bt\s*=",
    r"\bU\s*=",
    r"χ²|[Cc]hi-?squared",
    r"\bp\s*[<=>≤≥]\s*\d",
    r"\br\s*=\s*-?\d",
    r"-?\d+\.?\d*\s*±",
    r"\bn\s*=\s*\d",
    r"95\s*%\s*CI",
    r"Cohen'?s?\s*d",
]
STAT_RE = re.compile("|".join(STAT_SIGNATURES), re.IGNORECASE)


def count_numbers(text):
    """Count numeric values in text."""
    return len(NUM_PATTERN.findall(text))


def count_stat_reports(text):
    """Count sentences containing statistical signatures."""
    sentences = re.split(r"(?<=[.!?])\s+|\n", text)
    return sum(1 for s in sentences if STAT_RE.search(s))


def find_banned_cells(text):
    """Find markdown table rows where any cell is a banned qualitative word."""
    hits = []
    for line in text.split("\n"):
        if not line.startswith("|"):
            continue
        # Skip separator rows like | --- | --- |
        if re.fullmatch(r"\|[\s\-:|]+\|?", line.strip()):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        for c in cells:
            # Strip markdown emphasis and simple annotations
            bare = re.sub(r"[*_`]", "", c).strip()
            # Remove trailing parenthetical like "(baseline)"
            bare_core = re.sub(r"\s*\([^)]*\)\s*$", "", bare).strip()
            if bare_core in BANNED_CELL_WORDS:
                hits.append((line.strip(), bare_core))
    return hits


def count_table_rows(text):
    """Count data rows across all markdown tables (excluding separators/headers)."""
    data_rows = 0
    in_table = False
    header_seen = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("|"):
            if re.fullmatch(r"\|[\s\-:|]+\|?", stripped):
                header_seen = True
                in_table = True
                continue
            if in_table and header_seen:
                data_rows += 1
        else:
            if in_table:
                in_table = False
                header_seen = False
    return data_rows


def count_numeric_table_cells(text):
    """Count table cells whose content includes at least one number."""
    count = 0
    for line in text.split("\n"):
        if not line.startswith("|"):
            continue
        if re.fullmatch(r"\|[\s\-:|]+\|?", line.strip()):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        for c in cells:
            if NUM_PATTERN.search(c):
                count += 1
    return count


def validate(paper_id, version="v2"):
    """Validate one paper's extraction. Returns a dict of metrics."""
    suffix = "_v2" if version == "v2" else "_v3" if version == "v3" else ""
    rich_dir = RICH_INPUTS / paper_id
    idea_path = rich_dir / f"idea_summary{suffix}.md"
    exp_path = rich_dir / f"experimental_log{suffix}.md"

    # Fallbacks for plain filenames
    if not idea_path.exists() and not suffix:
        idea_path = rich_dir / "idea_summary.md"
    if not exp_path.exists() and not suffix:
        exp_path = rich_dir / "experimental_log.md"

    if not exp_path.exists():
        return None

    exp_text = exp_path.read_text(encoding="utf-8", errors="replace")
    idea_text = idea_path.read_text(encoding="utf-8", errors="replace") if idea_path.exists() else ""

    banned = find_banned_cells(exp_text)

    return {
        "paper_id": paper_id,
        "version": version,
        "files_found": {"idea": idea_path.exists(), "exp": exp_path.exists()},
        "numbers_in_exp": count_numbers(exp_text),
        "numbers_in_idea": count_numbers(idea_text),
        "stat_reports": count_stat_reports(exp_text),
        "table_rows": count_table_rows(exp_text),
        "numeric_cells": count_numeric_table_cells(exp_text),
        "banned_cells": len(banned),
        "banned_examples": banned[:5],
        "word_count": len(exp_text.split()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", type=str)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--compare", action="store_true",
                        help="Compare v2 and v3 side by side")
    parser.add_argument("--version", default="v2", choices=["v2", "v3", "plain"])
    args = parser.parse_args()

    if args.paper:
        paper_ids = [args.paper]
    elif args.all:
        paper_ids = sorted(d.name for d in RICH_INPUTS.iterdir() if d.is_dir())
    else:
        print("Specify --paper or --all", file=sys.stderr)
        sys.exit(1)

    if args.compare:
        # Side-by-side comparison
        print(f"{'Paper':<55s} {'v2 nums':>8s} {'v3 nums':>8s} {'v2 stats':>9s} {'v3 stats':>9s} {'v2 banned':>10s} {'v3 banned':>10s}")
        print("-" * 115)
        totals = {"v2_nums": 0, "v3_nums": 0, "v2_stats": 0, "v3_stats": 0, "v2_banned": 0, "v3_banned": 0, "n": 0}
        for pid in paper_ids:
            v2 = validate(pid, "v2")
            v3 = validate(pid, "v3")
            if v2 is None and v3 is None:
                continue
            v2n = v2["numbers_in_exp"] if v2 else 0
            v3n = v3["numbers_in_exp"] if v3 else 0
            v2s = v2["stat_reports"] if v2 else 0
            v3s = v3["stat_reports"] if v3 else 0
            v2b = v2["banned_cells"] if v2 else 0
            v3b = v3["banned_cells"] if v3 else 0
            print(f"{pid[:53]:<55s} {v2n:>8d} {v3n:>8d} {v2s:>9d} {v3s:>9d} {v2b:>10d} {v3b:>10d}")
            if v2 and v3:
                totals["v2_nums"] += v2n; totals["v3_nums"] += v3n
                totals["v2_stats"] += v2s; totals["v3_stats"] += v3s
                totals["v2_banned"] += v2b; totals["v3_banned"] += v3b
                totals["n"] += 1
        if totals["n"] > 0:
            print("-" * 115)
            print(f"{'TOTAL (n=' + str(totals['n']) + ')':<55s} {totals['v2_nums']:>8d} {totals['v3_nums']:>8d} {totals['v2_stats']:>9d} {totals['v3_stats']:>9d} {totals['v2_banned']:>10d} {totals['v3_banned']:>10d}")
            improvement = (totals["v3_nums"] - totals["v2_nums"]) / max(totals["v2_nums"], 1) * 100
            print(f"\nNumeric density improvement: {improvement:+.1f}%")
    else:
        for pid in paper_ids:
            result = validate(pid, args.version)
            if result is None:
                print(f"{pid}: NOT FOUND", file=sys.stderr)
                continue
            print(f"\n=== {pid} ({args.version}) ===")
            print(f"  Numbers in log:     {result['numbers_in_exp']}")
            print(f"  Numbers in idea:    {result['numbers_in_idea']}")
            print(f"  Statistical reports: {result['stat_reports']}")
            print(f"  Table data rows:     {result['table_rows']}")
            print(f"  Numeric cells:       {result['numeric_cells']}")
            print(f"  Banned cells:        {result['banned_cells']}")
            if result["banned_examples"]:
                for line, word in result["banned_examples"]:
                    print(f"    - '{word}' in: {line[:80]}")
            print(f"  Word count:          {result['word_count']}")


if __name__ == "__main__":
    main()
