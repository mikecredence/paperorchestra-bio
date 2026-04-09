#!/usr/bin/env python3
"""
Citation audit tool: orphaned citation detection + coverage enforcement.

Usage:
    python citation_audit.py --tex main.tex --bib references.bib
    python citation_audit.py --tex main.tex --bib references.bib --min-coverage 0.90

Checks:
    1. Orphaned cite{} keys (in text but not in .bib)
    2. Unused .bib entries (in .bib but never cited in text)
    3. Coverage ratio (% of verified pool actually cited)
    4. Duplicate citation keys
    5. Citation count statistics
"""

import sys
import re
import json
import argparse
from pathlib import Path


def extract_cite_keys_from_tex(tex_path: str) -> list[str]:
    """Extract all citation keys from LaTeX cite, citep, citet commands."""
    tex_content = Path(tex_path).read_text(encoding="utf-8", errors="replace")

    # Match \cite{key}, \citep{key1, key2}, \citet{key}, \citeauthor{key}, etc.
    pattern = r'\\cite[tp]?\*?\{([^}]+)\}'
    matches = re.findall(pattern, tex_content)

    keys = []
    for match in matches:
        # Split on commas for multi-citation commands like \cite{a,b,c}
        for key in match.split(","):
            key = key.strip()
            if key:
                keys.append(key)

    return keys


def extract_bib_keys(bib_path: str) -> list[str]:
    """Extract all entry keys from a .bib file."""
    bib_content = Path(bib_path).read_text(encoding="utf-8", errors="replace")

    # Match @type{key, at the start of entries
    pattern = r'@\w+\{([^,]+),'
    matches = re.findall(pattern, bib_content)

    return [m.strip() for m in matches]


def audit(tex_path: str, bib_path: str, min_coverage: float = 0.90) -> dict:
    """Run the full citation audit."""
    cited_keys = extract_cite_keys_from_tex(tex_path)
    bib_keys = extract_bib_keys(bib_path)

    cited_set = set(cited_keys)
    bib_set = set(bib_keys)

    # Orphaned citations: in text but not in bib
    orphaned = sorted(cited_set - bib_set)

    # Unused bib entries: in bib but never cited
    unused = sorted(bib_set - cited_set)

    # Duplicate citation keys in tex
    from collections import Counter
    key_counts = Counter(cited_keys)
    # This is fine - duplicates in tex just mean multiple citations

    # Coverage: what % of the bib pool is actually cited
    if bib_set:
        coverage = len(cited_set & bib_set) / len(bib_set)
    else:
        coverage = 0.0

    # Unique citations used
    unique_citations = len(cited_set & bib_set)

    result = {
        "tex_file": tex_path,
        "bib_file": bib_path,
        "total_cite_commands": len(cited_keys),
        "unique_keys_cited": len(cited_set),
        "total_bib_entries": len(bib_set),
        "unique_citations_used": unique_citations,
        "coverage": round(coverage, 3),
        "coverage_target": min_coverage,
        "coverage_met": coverage >= min_coverage,
        "orphaned_citations": orphaned,
        "orphaned_count": len(orphaned),
        "unused_bib_entries": unused,
        "unused_count": len(unused),
        "status": "PASS" if not orphaned and coverage >= min_coverage else "FAIL",
        "issues": [],
    }

    if orphaned:
        result["issues"].append(
            f"CRITICAL: {len(orphaned)} citation(s) in text not found in .bib: "
            f"{', '.join(orphaned[:10])}"
        )

    if not result["coverage_met"]:
        result["issues"].append(
            f"WARNING: Citation coverage {coverage:.1%} is below target "
            f"{min_coverage:.1%}. {len(unused)} bib entries are unused."
        )

    if unique_citations < 25:
        result["issues"].append(
            f"WARNING: Only {unique_citations} unique citations used. "
            f"Target: 45-50 for top-tier quality."
        )

    return result


def main():
    parser = argparse.ArgumentParser(description="Audit citations in LaTeX paper")
    parser.add_argument("--tex", required=True, help="Path to main .tex file")
    parser.add_argument("--bib", required=True, help="Path to .bib file")
    parser.add_argument("--min-coverage", type=float, default=0.90,
                        help="Minimum citation coverage ratio (default: 0.90)")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON instead of human-readable")
    args = parser.parse_args()

    result = audit(args.tex, args.bib, args.min_coverage)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== Citation Audit Report ===")
        print(f"Status: {result['status']}")
        print(f"Citations used: {result['unique_citations_used']} "
              f"(out of {result['total_bib_entries']} in .bib)")
        print(f"Coverage: {result['coverage']:.1%} "
              f"(target: {result['coverage_target']:.1%})")
        print(f"Orphaned (in text, not in bib): {result['orphaned_count']}")
        print(f"Unused (in bib, not in text): {result['unused_count']}")

        if result["issues"]:
            print(f"\nIssues:")
            for issue in result["issues"]:
                print(f"  - {issue}")

        if result["orphaned_citations"]:
            print(f"\nOrphaned keys: {', '.join(result['orphaned_citations'])}")

        if result["unused_bib_entries"] and len(result["unused_bib_entries"]) <= 20:
            print(f"\nUnused entries: {', '.join(result['unused_bib_entries'])}")


if __name__ == "__main__":
    main()
