#!/usr/bin/env python3
"""
Generate test cases (idea_summary.md + experimental_log.md) from ground truth.

Without ANTHROPIC_API_KEY: generates template-based test cases from abstracts.
With ANTHROPIC_API_KEY: uses Claude for richer reverse-engineering.

Usage:
    python generate_test_case.py
    python generate_test_case.py --single genomics_001
    python generate_test_case.py --skip-existing
"""

import sys
import json
import re
import os
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import (
    BENCHMARK_DIR, TEST_CASES_DIR, GROUND_TRUTH_DIR,
    CANDIDATES_PATH, CLAUDE_MODEL, slugify, venue_sections,
)

HAS_ANTHROPIC = bool(os.environ.get("ANTHROPIC_API_KEY"))


def generate_idea_summary_heuristic(gt: dict) -> str:
    """Generate idea_summary.md from ground truth using templates."""
    title = gt.get("title", "Untitled")
    abstract = gt.get("abstract", "")
    venue = gt.get("published_venue", "")
    methods = gt.get("key_methods", [])
    results = gt.get("key_results", [])
    tags = gt.get("difficulty_tags", [])

    # Extract first sentence as core question proxy
    sentences = re.split(r'(?<=[.!?])\s+', abstract)
    motivation = sentences[0] if sentences else "Research question not available."
    approach = sentences[1] if len(sentences) > 1 else ""

    # Build contributions from results
    contributions = []
    for r in results[:5]:
        contributions.append(f"- {r[:150]}")
    if not contributions:
        contributions.append("- [Contributions to be extracted from full paper]")

    methods_str = ", ".join(methods[:5]) if methods else "[Methods to be extracted]"

    return f"""# Idea Summary: {title}

## Working title
{title}

## Core question
{motivation}

## Motivation / gap
{approach}

## Core contribution (bullet form)
{chr(10).join(contributions)}

## Method in brief
{methods_str}

## Target venue
{venue or 'Not specified'}
"""


def generate_experimental_log_heuristic(gt: dict) -> str:
    """Generate experimental_log.md from ground truth using templates."""
    title = gt.get("title", "")
    abstract = gt.get("abstract", "")
    methods = gt.get("key_methods", [])
    results = gt.get("key_results", [])
    datasets = gt.get("key_datasets", [])
    confidence = gt.get("generation_confidence", "low")

    # Extract numbers from abstract
    numbers = re.findall(r'(\d+\.?\d*%?)', abstract)

    methods_table = "| Method | Description |\n|--------|-------------|\n"
    for m in methods[:10]:
        methods_table += f"| {m} | [Details from paper] |\n"

    results_section = ""
    for r in results[:5]:
        results_section += f"- {r}\n"

    datasets_section = ""
    for d in datasets[:5]:
        datasets_section += f"- {d}\n"

    return f"""# Experimental Log: {title}

> Generation confidence: {confidence}
> Extracted from abstract only — enrich with full paper data when available.

## Methods / Tools
{methods_table}

## Datasets
{datasets_section if datasets_section else '- [Datasets to be extracted from full paper]'}

## Key Results
{results_section if results_section else '- [Results to be extracted from full paper]'}

## Quantitative Values Found in Abstract
{', '.join(numbers[:20]) if numbers else 'No numeric values extracted.'}

## Ground Truth Reference
- bioRxiv DOI: {gt.get('biorxiv_doi', 'N/A')}
- Published DOI: {gt.get('published_doi', 'N/A')}
- Venue: {gt.get('published_venue', 'N/A')}
"""


def generate_with_claude(gt: dict) -> tuple[str, str]:
    """Use Claude to generate richer test case content."""
    import anthropic

    client = anthropic.Anthropic()
    abstract = gt.get("abstract", "")
    title = gt.get("title", "")
    venue = gt.get("published_venue", "")
    methods = gt.get("key_methods", [])
    results = gt.get("key_results", [])

    prompt = f"""You are reverse-engineering a published paper into pre-writing research materials.
Given this paper's abstract and metadata, generate TWO documents:

1. **idea_summary.md** — Written as if the researcher is describing their idea BEFORE writing the paper.
   Use informal research-notes style, bullet points, forward-looking language.
   Sections: ## Working title, ## Core question, ## Motivation / gap, ## Core contribution (bullet form), ## Method in brief, ## Target venue

2. **experimental_log.md** — Written as raw lab-notebook data.
   Include any quantitative values from the abstract as if they were experimental results.
   Use markdown tables where possible. Sections should include models/tools used, datasets, key results with numbers.

Paper: {title}
Venue: {venue}
Abstract: {abstract}
Key methods: {', '.join(methods)}
Key results: {'; '.join(results)}

Output format:
---IDEA_SUMMARY---
(content)
---EXPERIMENTAL_LOG---
(content)
"""

    try:
        response = client.messages.create(
            model=CLAUDE_MODEL, max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text

        # Parse the two sections
        if "---IDEA_SUMMARY---" in text and "---EXPERIMENTAL_LOG---" in text:
            parts = text.split("---EXPERIMENTAL_LOG---")
            idea = parts[0].replace("---IDEA_SUMMARY---", "").strip()
            exp_log = parts[1].strip()
            return idea, exp_log

    except Exception as e:
        print(f"  Claude API error: {e}", file=sys.stderr)

    return "", ""


def generate_metadata(gt: dict, paper_id: str) -> dict:
    """Generate metadata.json from ground truth."""
    return {
        "id": paper_id,
        "title": gt.get("title", ""),
        "biorxiv_doi": gt.get("biorxiv_doi"),
        "published_doi": gt.get("published_doi"),
        "published_venue": gt.get("published_venue"),
        "published_year": gt.get("published_year"),
        "authors": [],
        "category": gt.get("subfield", "bioinformatics") if "subfield" in gt else "bioinformatics",
        "subcategory": None,
        "paper_type": gt.get("paper_type", "research"),
        "format": "single-column",
        "ground_truth_citation_count": gt.get("estimated_references"),
        "ground_truth_figure_count": gt.get("estimated_figures"),
        "ground_truth_table_count": gt.get("estimated_tables"),
        "difficulty": "medium",
        "notes": gt.get("abstract", "")[:200],
    }


def process_ground_truth(gt_dir: Path, output_dir: Path, skip_existing: bool) -> bool:
    """Generate a test case from a ground truth directory."""
    gt_file = gt_dir / "ground_truth.json"
    if not gt_file.exists():
        return False

    gt = json.loads(gt_file.read_text(encoding="utf-8"))
    paper_id = gt.get("paper_id", gt_dir.name)
    case_dir = output_dir / paper_id

    if skip_existing and case_dir.exists() and (case_dir / "idea_summary.md").exists():
        print(f"  Skipping {paper_id} (exists)", file=sys.stderr)
        return False

    print(f"Generating: {paper_id} — {gt.get('title', '')[:50]}...", file=sys.stderr)

    # Generate content
    if HAS_ANTHROPIC and gt.get("abstract", ""):
        idea, exp_log = generate_with_claude(gt)
        if not idea:
            idea = generate_idea_summary_heuristic(gt)
            exp_log = generate_experimental_log_heuristic(gt)
    else:
        idea = generate_idea_summary_heuristic(gt)
        exp_log = generate_experimental_log_heuristic(gt)

    # Generate metadata
    metadata = generate_metadata(gt, paper_id)

    # Write files
    case_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / "idea_summary.md").write_text(idea, encoding="utf-8")
    (case_dir / "experimental_log.md").write_text(exp_log, encoding="utf-8")
    (case_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    conf = gt.get("generation_confidence", "low")
    print(f"  Created {paper_id} (confidence: {conf})", file=sys.stderr)
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate test cases from ground truth")
    parser.add_argument("--ground-truth-dir", type=Path, default=GROUND_TRUTH_DIR)
    parser.add_argument("--output-dir", type=Path, default=TEST_CASES_DIR)
    parser.add_argument("--single", type=str, help="Generate for a single paper ID")
    parser.add_argument("--skip-existing", action="store_true", default=True,
                        help="Skip test cases that already exist")
    args = parser.parse_args()

    if not args.ground_truth_dir.exists():
        print(f"No ground truth directory at {args.ground_truth_dir}", file=sys.stderr)
        sys.exit(1)

    if HAS_ANTHROPIC:
        print("Claude API available — using LLM-assisted generation", file=sys.stderr)
    else:
        print("No ANTHROPIC_API_KEY — using heuristic generation", file=sys.stderr)

    gt_dirs = sorted(args.ground_truth_dir.iterdir())
    if args.single:
        gt_dirs = [d for d in gt_dirs if d.name == args.single]

    generated = 0
    for gt_dir in gt_dirs:
        if not gt_dir.is_dir():
            continue
        if process_ground_truth(gt_dir, args.output_dir, args.skip_existing):
            generated += 1

    print(f"\nGenerated {generated} test cases", file=sys.stderr)


if __name__ == "__main__":
    main()
