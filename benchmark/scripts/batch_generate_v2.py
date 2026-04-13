#!/usr/bin/env python3
"""Generate prompt files and manifest for batch v2 paper generation."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
RI_DIR = ROOT / "benchmark" / "rich_inputs"
TC_DIR = ROOT / "benchmark" / "test-cases"
RES_DIR = ROOT / "benchmark" / "results"
BATCH_DIR = ROOT / "benchmark" / "batch_v2"

def get_untested_papers():
    """Return sorted list of papers with v2 inputs but no results."""
    has_results = set(d.name for d in RES_DIR.iterdir() if d.is_dir() and d.name != "figures")
    untested = []
    for d in sorted(RI_DIR.iterdir()):
        if not d.is_dir():
            continue
        if d.name in has_results:
            continue
        idea = d / "idea_summary_v2.md"
        exp = d / "experimental_log_v2.md"
        meta = TC_DIR / d.name / "metadata.json"
        if idea.exists() and exp.exists() and meta.exists():
            untested.append(d.name)
    return untested


def get_venue(paper_id):
    meta = TC_DIR / paper_id / "metadata.json"
    data = json.loads(meta.read_text(encoding="utf-8"))
    return data.get("published_venue", "Nature Communications")


def main():
    papers = get_untested_papers()
    print(f"Found {len(papers)} untested papers with v2 inputs")

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []

    for paper_id in papers:
        idea = (RI_DIR / paper_id / "idea_summary_v2.md").read_text(errors="replace")
        exp = (RI_DIR / paper_id / "experimental_log_v2.md").read_text(errors="replace")
        venue = get_venue(paper_id)

        out_dir = BATCH_DIR / paper_id
        out_dir.mkdir(parents=True, exist_ok=True)

        # Baseline prompt
        baseline_prompt = f"""Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: {venue}

## Idea Summary

{idea}

## Experimental Log

{exp}
"""
        (out_dir / "baseline_prompt.md").write_text(baseline_prompt)

        # Skill prompt
        skill_prompt = f"""Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: {venue}

## Idea Summary

{idea}

## Experimental Log

{exp}
"""
        (out_dir / "skill_prompt.md").write_text(skill_prompt)

        manifest.append({
            "id": paper_id,
            "venue": venue,
            "idea_size": len(idea),
            "exp_size": len(exp),
        })

    manifest_path = BATCH_DIR / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Generated prompts for {len(manifest)} papers in {BATCH_DIR}")
    print(f"Manifest: {manifest_path}")

    # Print batch assignments (10 per batch for baseline, 5 for skill)
    for batch_size, label in [(10, "baseline"), (5, "skill")]:
        n_batches = (len(papers) + batch_size - 1) // batch_size
        print(f"\n{label} batches ({batch_size}/batch, {n_batches} batches):")
        for i in range(n_batches):
            batch = papers[i * batch_size : (i + 1) * batch_size]
            print(f"  Batch {i+1}: {len(batch)} papers")


if __name__ == "__main__":
    main()
