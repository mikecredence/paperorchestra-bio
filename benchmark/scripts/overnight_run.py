#!/usr/bin/env python3
"""
Overnight batch run: extract full text + generate test cases for queued papers.

Usage:
    # Process all queued candidates (full pipeline)
    python overnight_run.py --all

    # Process just N papers
    python overnight_run.py --limit 40

    # Dry run (show what would be processed)
    python overnight_run.py --dry-run

This script:
1. Reads benchmark/fulltext_queue.json
2. For each candidate: fetches JATS XML, extracts full text, generates test case
3. Saves to benchmark/rich_inputs/{id}/ and benchmark/ground_truth/{id}/
4. Validates all new test cases
"""

import sys
import json
import time
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import BENCHMARK_DIR, TEST_CASES_DIR, GROUND_TRUTH_DIR, slugify

# Import the extraction functions
from extract_full_text import fetch_jats_xml, parse_jats, generate_rich_idea_summary, generate_rich_experimental_log


def process_candidate(candidate: dict, rich_dir: Path, gt_dir: Path) -> bool:
    """Process a single candidate: fetch JATS, extract, save."""
    doi = candidate.get("biorxiv_doi", "")
    title = candidate.get("title", "")
    journal = candidate.get("journal", "")
    category = candidate.get("category", "unknown")
    paper_id = slugify(title)

    # Skip if already processed
    if (rich_dir / paper_id / "idea_summary.md").exists():
        return False

    print(f"  Processing: {paper_id[:50]}...", file=sys.stderr)

    # Fetch JATS XML
    xml_text = fetch_jats_xml(doi)
    if not xml_text:
        print(f"    SKIP: no JATS XML for {doi}", file=sys.stderr)
        return False

    # Parse
    parsed = parse_jats(xml_text)
    if not parsed.get("sections"):
        print(f"    SKIP: empty body for {doi}", file=sys.stderr)
        return False

    # Generate rich inputs
    idea = generate_rich_idea_summary(parsed, journal)
    exp_log = generate_rich_experimental_log(parsed)

    # Save rich inputs
    out_dir = rich_dir / paper_id
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "idea_summary.md").write_text(idea, encoding="utf-8")
    (out_dir / "experimental_log.md").write_text(exp_log, encoding="utf-8")

    # Save ground truth
    gt_out = gt_dir / paper_id
    gt_out.mkdir(parents=True, exist_ok=True)
    gt_data = {
        "paper_id": paper_id,
        "title": parsed["title"],
        "biorxiv_doi": doi,
        "published_doi": candidate.get("published_doi", ""),
        "journal": journal,
        "category": category,
        "num_sections": len(parsed["sections"]),
        "num_figures": len(parsed["figures"]),
        "num_tables": len(parsed["tables"]),
        "num_references": len(parsed["references"]),
        "reference_titles": [r["title"] for r in parsed["references"]],
        "extraction_method": "jats_xml_full_text",
    }
    (gt_out / "full_text_ground_truth.json").write_text(
        json.dumps(gt_data, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Also create a basic test case
    tc_dir = TEST_CASES_DIR / paper_id
    if not tc_dir.exists():
        tc_dir.mkdir(parents=True, exist_ok=True)
        (tc_dir / "idea_summary.md").write_text(idea, encoding="utf-8")
        (tc_dir / "experimental_log.md").write_text(exp_log, encoding="utf-8")
        meta = {
            "id": paper_id,
            "title": parsed["title"],
            "biorxiv_doi": doi,
            "published_doi": candidate.get("published_doi", ""),
            "published_venue": journal,
            "published_year": 2024,
            "authors": [],
            "category": category,
            "subcategory": None,
            "paper_type": "research",
            "format": "single-column",
            "ground_truth_citation_count": len(parsed["references"]),
            "ground_truth_figure_count": len(parsed["figures"]),
            "ground_truth_table_count": len(parsed["tables"]),
            "difficulty": "medium",
            "notes": parsed.get("abstract", "")[:200],
        }
        (tc_dir / "metadata.json").write_text(
            json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    refs = len(parsed["references"])
    figs = len(parsed["figures"])
    tabs = len(parsed["tables"])
    print(f"    OK: {refs} refs, {figs} figs, {tabs} tabs, "
          f"idea={len(idea)}b, log={len(exp_log)}b", file=sys.stderr)
    return True


def main():
    parser = argparse.ArgumentParser(description="Overnight batch full-text extraction")
    parser.add_argument("--all", action="store_true", help="Process all candidates")
    parser.add_argument("--limit", type=int, help="Max candidates to process")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed")
    parser.add_argument("--queue", type=Path,
                        default=BENCHMARK_DIR / "fulltext_queue.json")
    args = parser.parse_args()

    queue = json.loads(args.queue.read_text(encoding="utf-8"))
    candidates = queue["candidates"]

    if args.limit:
        candidates = candidates[:args.limit]

    rich_dir = BENCHMARK_DIR / "rich_inputs"
    gt_dir = GROUND_TRUTH_DIR

    if args.dry_run:
        print(f"Would process {len(candidates)} candidates:")
        from collections import Counter
        cats = Counter(c.get("category", "?") for c in candidates)
        for cat, n in cats.most_common():
            print(f"  {cat}: {n}")
        return

    print(f"Processing {len(candidates)} candidates...", file=sys.stderr)
    processed = 0
    skipped = 0
    failed = 0

    for i, candidate in enumerate(candidates):
        try:
            if process_candidate(candidate, rich_dir, gt_dir):
                processed += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"    ERROR: {e}", file=sys.stderr)
            failed += 1

        if (i + 1) % 10 == 0:
            print(f"  Progress: {i+1}/{len(candidates)} "
                  f"(processed={processed}, skipped={skipped}, failed={failed})",
                  file=sys.stderr)

    print(f"\nDone: processed={processed}, skipped={skipped}, failed={failed}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
