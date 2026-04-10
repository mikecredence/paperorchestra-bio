#!/usr/bin/env python3
"""
Extract structured ground truth from published papers using bioRxiv API.

When an Anthropic API key is available (ANTHROPIC_API_KEY env var), uses Claude
for richer extraction. Otherwise falls back to heuristic extraction from abstracts.

Usage:
    python extract_ground_truth.py --candidates benchmark/corpus_candidates.json
    python extract_ground_truth.py --single bioinfo_001
    python extract_ground_truth.py --backfill-metadata
"""

import sys
import json
import re
import argparse
import os
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from config import (
    BENCHMARK_DIR, TEST_CASES_DIR, GROUND_TRUTH_DIR,
    CANDIDATES_PATH, CLAUDE_MODEL,
    BIORXIV_API, biorxiv_limiter, slugify,
    venue_sections,
)

HAS_ANTHROPIC = bool(os.environ.get("ANTHROPIC_API_KEY"))


def fetch_biorxiv_details(doi: str) -> dict | None:
    """Fetch preprint details from bioRxiv API by DOI."""
    # API needs the full DOI including 10.1101/ prefix
    if not doi.startswith("10.1101/"):
        doi = f"10.1101/{doi}"
    url = f"{BIORXIV_API}/details/biorxiv/{doi}"

    biorxiv_limiter.wait()
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        collection = data.get("collection", [])
        if collection:
            return collection[-1]
    except requests.RequestException as e:
        print(f"  bioRxiv API error for {doi}: {e}", file=sys.stderr)
    return None


def extract_numbers_from_text(text: str) -> list[str]:
    """Extract numeric values from text (percentages, decimals, integers)."""
    return re.findall(r'\d+\.?\d*%?', text)


def estimate_from_abstract(title: str, abstract: str, venue: str,
                           year: int, category: str, paper_type: str) -> dict:
    """Heuristic ground truth extraction from abstract metadata only."""
    numbers = extract_numbers_from_text(abstract)
    words = abstract.split()

    # Estimate figures based on paper type and venue
    fig_estimates = {
        "benchmark": 6, "methods": 5, "clinical": 4,
        "clinical_validation": 4, "atlas": 7, "dataset": 4, "research": 5,
    }
    estimated_figures = fig_estimates.get(paper_type, 5)

    # Estimate tables — benchmark papers have more
    tab_estimates = {
        "benchmark": 4, "methods": 2, "clinical": 3,
        "clinical_validation": 3, "atlas": 2, "dataset": 3, "research": 2,
    }
    estimated_tables = tab_estimates.get(paper_type, 2)

    # Estimate references based on venue
    ref_estimates = {
        "Nature Communications": 50, "Nature Methods": 45,
        "Nature Biotechnology": 55, "Nature Genetics": 50,
        "eLife": 60, "Genome Biology": 55,
        "PLOS Computational Biology": 50, "Nucleic Acids Research": 45,
    }
    estimated_refs = 50
    if venue:
        for v, count in ref_estimates.items():
            if v.lower() in venue.lower():
                estimated_refs = count
                break

    # Extract key methods from abstract (look for method-like phrases)
    method_patterns = [
        r'(?:using|with|via|by)\s+(\w[\w\s]{2,30}?)(?:\.|,|\s+to\s)',
        r'(?:method|algorithm|model|framework|pipeline|tool)\s+(?:called\s+)?(\w+)',
    ]
    key_methods = []
    for pattern in method_patterns:
        matches = re.findall(pattern, abstract, re.IGNORECASE)
        key_methods.extend(m.strip() for m in matches[:5])

    # Extract key results (sentences with numbers)
    sentences = re.split(r'[.!?]+', abstract)
    key_results = []
    for sent in sentences:
        if any(c.isdigit() for c in sent) and len(sent.strip()) > 20:
            key_results.append(sent.strip()[:200])

    # Determine quantitative density for confidence
    num_count = len(numbers)
    if num_count >= 10:
        confidence = "high"
    elif num_count >= 4:
        confidence = "medium"
    else:
        confidence = "low"

    # Difficulty tags
    difficulty_tags = []
    abstract_lower = abstract.lower()
    if any(w in abstract_lower for w in ["benchmark", "comparison", "evaluate", "compare"]):
        difficulty_tags.append("multi-model-comparison")
    if any(w in abstract_lower for w in ["table", "dataset", "datasets"]):
        difficulty_tags.append("dense-tables")
    if any(w in abstract_lower for w in ["clinical", "patient", "cohort"]):
        difficulty_tags.append("clinical-validation")
    if any(w in abstract_lower for w in ["negative", "fail", "does not", "cannot"]):
        difficulty_tags.append("negative-result")
    if num_count >= 10:
        difficulty_tags.append("quantitative-rich")
    if len(words) > 250:
        difficulty_tags.append("complex-methods")

    return {
        "estimated_figures": estimated_figures,
        "estimated_tables": estimated_tables,
        "estimated_references": estimated_refs,
        "key_methods": key_methods[:10],
        "key_results": key_results[:5],
        "key_datasets": [],  # Hard to extract without full text
        "expected_citation_titles": [],  # Needs Claude or manual curation
        "difficulty_tags": difficulty_tags,
        "generation_confidence": confidence,
    }


def extract_with_claude(title: str, abstract: str, venue: str, year: int,
                        authors: str, category: str) -> dict:
    """Use Claude API with tool_use to extract structured ground truth."""
    import anthropic

    client = anthropic.Anthropic()
    tool_schema = {
        "name": "extract_ground_truth",
        "description": "Extract structured ground truth metadata from a biomedical paper.",
        "input_schema": {
            "type": "object",
            "required": ["estimated_figures", "estimated_tables", "estimated_references",
                         "key_methods", "key_results", "key_datasets",
                         "expected_citation_titles", "difficulty_tags",
                         "generation_confidence"],
            "properties": {
                "estimated_figures": {"type": "integer"},
                "estimated_tables": {"type": "integer"},
                "estimated_references": {"type": "integer"},
                "key_methods": {"type": "array", "items": {"type": "string"}},
                "key_results": {"type": "array", "items": {"type": "string"}},
                "key_datasets": {"type": "array", "items": {"type": "string"}},
                "expected_citation_titles": {
                    "type": "array", "items": {"type": "string"},
                    "description": "Titles of papers that SHOULD be cited based on methods and baselines described"
                },
                "difficulty_tags": {"type": "array", "items": {"type": "string"}},
                "generation_confidence": {"type": "string", "enum": ["high", "medium", "low"]},
            }
        }
    }

    prompt = f"""Analyze this biomedical paper and extract structured metadata.

Title: {title}
Venue: {venue} ({year})
Authors: {authors}
Category: {category}

Abstract:
{abstract}

Extract ground truth metadata using the provided tool. Be thorough with expected_citation_titles."""

    try:
        response = client.messages.create(
            model=CLAUDE_MODEL, max_tokens=4096,
            tools=[tool_schema],
            messages=[{"role": "user", "content": prompt}],
        )
        for block in response.content:
            if block.type == "tool_use" and block.name == "extract_ground_truth":
                return block.input
    except Exception as e:
        print(f"  Claude API error: {e}", file=sys.stderr)

    return {}


def process_candidate(candidate: dict) -> dict | None:
    """Process a single candidate paper and extract ground truth."""
    paper_id = candidate.get("id", slugify(candidate.get("title", "unknown")))
    title = candidate.get("title", "")
    biorxiv_doi = candidate.get("biorxiv_doi")
    published_venue = candidate.get("published_venue", "")
    published_year = candidate.get("published_year", 2024)
    paper_type = candidate.get("paper_type", "research")
    note = candidate.get("note", "")

    print(f"Processing: {paper_id} — {title[:60]}...", file=sys.stderr)

    # Fetch abstract from bioRxiv
    abstract = ""
    authors = ""
    category = ""

    if biorxiv_doi:
        details = fetch_biorxiv_details(biorxiv_doi)
        if details:
            abstract = details.get("abstract", "")
            authors = details.get("authors", "")
            category = details.get("category", "")
            print(f"  Got abstract ({len(abstract)} chars) from bioRxiv", file=sys.stderr)

    if not abstract:
        print(f"  No abstract from bioRxiv, using note", file=sys.stderr)
        abstract = note or f"Paper titled '{title}' published in {published_venue} ({published_year})."

    # Extract ground truth
    if HAS_ANTHROPIC:
        print(f"  Using Claude API for extraction", file=sys.stderr)
        gt = extract_with_claude(title, abstract, published_venue, published_year, authors, category)
    else:
        print(f"  Using heuristic extraction (no ANTHROPIC_API_KEY)", file=sys.stderr)
        gt = estimate_from_abstract(title, abstract, published_venue, published_year, category, paper_type)

    if not gt:
        print(f"  Failed to extract ground truth for {paper_id}", file=sys.stderr)
        return None

    ground_truth = {
        "paper_id": paper_id,
        "title": title,
        "biorxiv_doi": biorxiv_doi,
        "published_doi": candidate.get("published_doi"),
        "published_venue": published_venue,
        "published_year": published_year,
        "abstract": abstract[:1000],
        "authors": authors[:500] if isinstance(authors, str) else "",
        "section_structure": venue_sections(published_venue),
        "extraction_method": "claude" if HAS_ANTHROPIC else "heuristic",
        **gt,
    }

    return ground_truth


def backfill_metadata(ground_truth_dir: Path, test_cases_dir: Path):
    """Update existing metadata.json files with ground truth data."""
    for gt_file in ground_truth_dir.glob("*/ground_truth.json"):
        paper_id = gt_file.parent.name
        meta_path = test_cases_dir / paper_id / "metadata.json"

        if not meta_path.exists():
            continue

        gt = json.loads(gt_file.read_text(encoding="utf-8"))
        meta = json.loads(meta_path.read_text(encoding="utf-8"))

        updated = False
        field_map = {
            "ground_truth_citation_count": "estimated_references",
            "ground_truth_figure_count": "estimated_figures",
            "ground_truth_table_count": "estimated_tables",
        }
        for meta_field, gt_field in field_map.items():
            if meta.get(meta_field) is None and gt.get(gt_field):
                meta[meta_field] = gt[gt_field]
                updated = True

        if updated:
            meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"  Updated metadata for {paper_id}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Extract ground truth from published papers")
    parser.add_argument("--candidates", type=Path, default=CANDIDATES_PATH)
    parser.add_argument("--output-dir", type=Path, default=GROUND_TRUTH_DIR)
    parser.add_argument("--single", type=str, help="Process a single paper by ID")
    parser.add_argument("--backfill-metadata", action="store_true")
    parser.add_argument("--limit", type=int, help="Max candidates to process")
    parser.add_argument("--skip-existing", action="store_true", default=True)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    if HAS_ANTHROPIC:
        print("Claude API available — using LLM-assisted extraction", file=sys.stderr)
    else:
        print("No ANTHROPIC_API_KEY — using heuristic extraction", file=sys.stderr)

    with open(args.candidates, encoding="utf-8") as f:
        corpus = json.load(f)

    all_candidates = []
    for subfield in corpus.get("subfields", []):
        for candidate in subfield.get("candidates", []):
            all_candidates.append(candidate)
    for tc in corpus.get("additional_test_cases_identified", []):
        all_candidates.append(tc)

    if args.single:
        all_candidates = [c for c in all_candidates if c.get("id") == args.single]
        if not all_candidates:
            print(f"No candidate with id '{args.single}'", file=sys.stderr)
            sys.exit(1)

    if args.limit:
        all_candidates = all_candidates[:args.limit]

    processed = skipped = failed = 0

    for candidate in all_candidates:
        paper_id = candidate.get("id", slugify(candidate.get("title", "unknown")))
        gt_dir = args.output_dir / paper_id
        gt_file = gt_dir / "ground_truth.json"

        if args.skip_existing and gt_file.exists():
            print(f"  Skipping {paper_id} (exists)", file=sys.stderr)
            skipped += 1
            continue

        gt = process_candidate(candidate)
        if gt:
            gt_dir.mkdir(parents=True, exist_ok=True)
            gt_file.write_text(json.dumps(gt, indent=2, ensure_ascii=False), encoding="utf-8")
            processed += 1
        else:
            failed += 1

    print(f"\nProcessed: {processed}, Skipped: {skipped}, Failed: {failed}", file=sys.stderr)

    if args.backfill_metadata:
        print("\nBackfilling metadata...", file=sys.stderr)
        backfill_metadata(args.output_dir, TEST_CASES_DIR)

    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
