#!/usr/bin/env python3
"""
Discover new benchmark candidates via bioRxiv publisher API.

Finds bioRxiv preprints that have been published in peer-reviewed journals,
filters for quantitative/benchmark papers, and merges with existing candidates.

Usage:
    python discover_candidates.py --target-count 30
    python discover_candidates.py --target-count 50 --date-range 2024-01-01:2025-06-30
"""

import sys
import json
import re
import argparse
import time
from pathlib import Path
from datetime import datetime, timedelta

import requests

sys.path.insert(0, str(Path(__file__).parent))
from config import (
    CANDIDATES_PATH, BIORXIV_API, biorxiv_limiter,
    BIORXIV_CATEGORY_MAP, SUBFIELD_CATEGORIES, slugify,
)

# Journals we want papers from (high-impact biomedical)
TARGET_JOURNALS = [
    "nature communications", "nature methods", "nature biotechnology",
    "nature genetics", "nature medicine", "nature neuroscience",
    "nature immunology", "nature cell biology", "nature chemical biology",
    "genome biology", "genome research", "elife",
    "nucleic acids research", "bioinformatics",
    "plos computational biology", "plos genetics", "plos biology",
    "cell systems", "cell reports", "cell reports methods",
    "bmc genomics", "bmc bioinformatics", "bmc genomic data",
    "scientific data", "gigascience",
    "briefings in bioinformatics",
    "journal of chemical information and modeling",
    "lancet digital health",
]

# Keywords that signal quantitative/benchmark papers
QUANT_KEYWORDS = [
    "benchmark", "comparison", "evaluate", "evaluation", "systematic",
    "accuracy", "auc", "f1", "precision", "recall", "performance",
    "outperform", "state-of-the-art", "baseline", "dataset",
    "pipeline", "framework", "tool", "method", "algorithm",
    "deep learning", "machine learning", "neural network",
    "classification", "prediction", "detection",
]


def fetch_published_preprints(start_date: str, end_date: str,
                              cursor: int = 0) -> tuple[list[dict], int]:
    """Fetch bioRxiv preprints that have been published in journals.
    Returns (collection, total_count)."""
    url = f"{BIORXIV_API}/pubs/biorxiv/{start_date}/{end_date}/{cursor}"
    biorxiv_limiter.wait()

    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        messages = data.get("messages", [{}])
        total = int(messages[0].get("total", 0)) if messages else 0
        return data.get("collection", []), total
    except requests.RequestException as e:
        print(f"  API error: {e}", file=sys.stderr)
        return [], 0


def is_target_journal(preprint_data: dict) -> str | None:
    """Check if the paper was published in a target journal. Returns journal name or None."""
    published_journal = preprint_data.get("published_journal", "")
    if not published_journal:
        return None

    journal_lower = published_journal.lower()
    for journal in TARGET_JOURNALS:
        if journal in journal_lower:
            return published_journal
    return None


def has_quantitative_abstract(abstract: str) -> bool:
    """Check if abstract suggests a quantitative/benchmark paper."""
    if not abstract:
        return False
    abstract_lower = abstract.lower()
    keyword_hits = sum(1 for kw in QUANT_KEYWORDS if kw in abstract_lower)
    number_count = len(re.findall(r'\d+\.?\d*', abstract))
    return keyword_hits >= 3 or number_count >= 5


def classify_subfield(category: str, abstract: str) -> str:
    """Classify paper into our subfield taxonomy."""
    # First try bioRxiv category mapping
    if category:
        mapped = BIORXIV_CATEGORY_MAP.get(category.lower())
        if mapped:
            return mapped

    # Fallback: keyword-based classification
    abstract_lower = (abstract or "").lower()
    keyword_map = {
        "genomics": ["genome", "sequencing", "single-cell", "rna-seq", "chip-seq", "atac-seq"],
        "bioinformatics": ["algorithm", "software", "pipeline", "tool", "benchmark", "computational"],
        "drug_discovery": ["drug", "compound", "target", "therapeutic", "pharmacol", "docking"],
        "neuroscience": ["brain", "neural", "neuron", "cortex", "fmri", "eeg", "connectome"],
        "immunology": ["immune", "antibody", "t cell", "b cell", "vaccine", "cytokine"],
        "cancer_biology": ["cancer", "tumor", "oncolog", "metasta", "carcinoma"],
        "structural_biology": ["protein structure", "cryo-em", "crystal", "molecular dynamics", "folding"],
        "clinical": ["clinical trial", "patient", "cohort", "diagnostic", "prognos"],
        "cell_biology": ["cell", "proteomic", "metabolomic", "organoid", "stem cell"],
        "epidemiology": ["epidemiol", "surveillance", "outbreak", "public health", "pandemic"],
        "methods": ["method", "assay", "protocol", "platform", "technique"],
    }
    best_field = "bioinformatics"
    best_score = 0
    for field, keywords in keyword_map.items():
        score = sum(1 for kw in keywords if kw in abstract_lower)
        if score > best_score:
            best_score = score
            best_field = field
    return best_field


def classify_paper_type(abstract: str) -> str:
    """Classify paper type from abstract."""
    abstract_lower = (abstract or "").lower()
    if any(w in abstract_lower for w in ["benchmark", "systematic comparison", "evaluate", "compared"]):
        return "benchmark"
    if any(w in abstract_lower for w in ["clinical trial", "patient cohort", "enrolled"]):
        return "clinical"
    if any(w in abstract_lower for w in ["atlas", "catalog", "compendium", "resource"]):
        return "atlas"
    if any(w in abstract_lower for w in ["dataset", "data resource", "collection"]):
        return "dataset"
    if any(w in abstract_lower for w in ["novel method", "new tool", "we developed", "we present a"]):
        return "methods"
    return "research"


def load_existing_dois(candidates_path: Path) -> set[str]:
    """Load DOIs from existing candidates to avoid duplicates."""
    dois = set()
    if candidates_path.exists():
        with open(candidates_path, encoding="utf-8") as f:
            corpus = json.load(f)
        for subfield in corpus.get("subfields", []):
            for c in subfield.get("candidates", []):
                if c.get("biorxiv_doi"):
                    dois.add(c["biorxiv_doi"])
                if c.get("published_doi"):
                    dois.add(c["published_doi"])
        for tc in corpus.get("additional_test_cases_identified", []):
            if tc.get("biorxiv_doi"):
                dois.add(tc["biorxiv_doi"])
    return dois


def discover(start_date: str, end_date: str, target_count: int,
             existing_dois: set[str]) -> list[dict]:
    """Discover new candidates from bioRxiv publisher API."""
    candidates = []
    cursor = 0
    pages_fetched = 0
    max_pages = 50  # Safety limit

    print(f"Searching bioRxiv published preprints {start_date} to {end_date}...", file=sys.stderr)

    while len(candidates) < target_count and pages_fetched < max_pages:
        collection, total = fetch_published_preprints(start_date, end_date, cursor)
        if not collection:
            break

        pages_fetched += 1
        print(f"  Page {pages_fetched}: {len(collection)} preprints (total: {total}), "
              f"{len(candidates)} candidates so far", file=sys.stderr)

        for item in collection:
            biorxiv_doi = item.get("preprint_doi", "")
            published_doi = item.get("published_doi", "")

            # Normalize DOI format
            if biorxiv_doi and not biorxiv_doi.startswith("10.1101/"):
                biorxiv_doi = f"10.1101/{biorxiv_doi}"

            # Skip duplicates
            if biorxiv_doi in existing_dois or published_doi in existing_dois:
                continue

            # Check if published in target journal
            journal = is_target_journal(item)
            if not journal:
                continue

            # Check abstract quality
            abstract = item.get("preprint_abstract", "")
            if not has_quantitative_abstract(abstract):
                continue

            # Classify
            category = item.get("preprint_category", "")
            subfield = classify_subfield(category, abstract)
            paper_type = classify_paper_type(abstract)
            title = item.get("preprint_title", "")

            candidate = {
                "id": slugify(title),
                "title": title,
                "biorxiv_doi": biorxiv_doi,
                "published_doi": published_doi,
                "published_venue": journal,
                "published_year": int(item.get("published_date", "2024")[:4]) if item.get("published_date") else 2024,
                "paper_type": paper_type,
                "subfield": subfield,
                "note": abstract[:200] if abstract else "",
            }

            candidates.append(candidate)
            existing_dois.add(biorxiv_doi)
            existing_dois.add(published_doi)

            if len(candidates) >= target_count:
                break

        # Move cursor forward (API returns 100 per page)
        cursor += len(collection)

    return candidates


def merge_candidates(existing_path: Path, new_candidates: list[dict]) -> dict:
    """Merge new candidates into existing corpus structure."""
    with open(existing_path, encoding="utf-8") as f:
        corpus = json.load(f)

    # Group new candidates by subfield
    by_subfield = {}
    for c in new_candidates:
        sf = c.pop("subfield", "bioinformatics")
        by_subfield.setdefault(sf, []).append(c)

    # Find or create subfield entries
    existing_names = {s["name"].lower(): i for i, s in enumerate(corpus["subfields"])}

    for sf, candidates in by_subfield.items():
        # Try to find matching subfield
        matched = False
        for existing_sf in corpus["subfields"]:
            if sf.lower() in existing_sf["name"].lower() or existing_sf["name"].lower().startswith(sf):
                existing_sf["candidates"].extend(candidates)
                matched = True
                break

        if not matched:
            corpus["subfields"].append({
                "name": sf.replace("_", " ").title(),
                "target_count": 10,
                "candidates": candidates,
            })

    # Update counts
    total = sum(len(s["candidates"]) for s in corpus["subfields"])
    total += len(corpus.get("additional_test_cases_identified", []))
    corpus["current_candidates"] = total

    return corpus


def main():
    parser = argparse.ArgumentParser(description="Discover biomedical benchmark candidates")
    parser.add_argument("--target-count", type=int, default=30,
                        help="Number of new candidates to find (default: 30)")
    parser.add_argument("--date-range", type=str, default="2024-01-01:2025-12-31",
                        help="Date range as start:end (YYYY-MM-DD)")
    parser.add_argument("--existing", type=Path, default=CANDIDATES_PATH)
    parser.add_argument("--output", type=Path, help="Output path (default: update existing)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print candidates without saving")
    args = parser.parse_args()

    start_date, end_date = args.date_range.split(":")
    existing_dois = load_existing_dois(args.existing)
    print(f"Existing DOIs: {len(existing_dois)}", file=sys.stderr)

    new_candidates = discover(start_date, end_date, args.target_count, existing_dois)

    print(f"\nDiscovered {len(new_candidates)} new candidates", file=sys.stderr)

    # Show subfield distribution
    sf_counts = {}
    for c in new_candidates:
        sf = c.get("subfield", "unknown")
        sf_counts[sf] = sf_counts.get(sf, 0) + 1
    print(f"Subfield distribution:", file=sys.stderr)
    for sf, count in sorted(sf_counts.items()):
        print(f"  {sf}: {count}", file=sys.stderr)

    if args.dry_run:
        for c in new_candidates[:10]:
            print(f"  [{c.get('subfield', '?')}] {c['title'][:70]}", file=sys.stderr)
            print(f"    DOI: {c['biorxiv_doi']}", file=sys.stderr)
            print(f"    Venue: {c['published_venue']}", file=sys.stderr)
        return

    # Merge and save
    output_path = args.output or args.existing
    corpus = merge_candidates(args.existing, new_candidates)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)

    print(f"Saved to {output_path} (total: {corpus['current_candidates']} candidates)", file=sys.stderr)


if __name__ == "__main__":
    main()
