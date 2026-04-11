#!/usr/bin/env python3
"""
LLM-powered extraction pipeline matching PaperOrchestra quality.

Uses Claude subagents (via the Agent tool in Claude Code) or writes
extraction prompts for manual/batch processing.

For each paper's JATS XML content, produces:
1. Sparse idea summary (high-level, no math)
2. Dense idea summary (with equations, formal definitions)
3. Structured experimental log (every table as markdown, figure observations)
4. Anonymized (no author names, no specific citations)

Usage:
    # Generate extraction prompts for a single paper
    python llm_extract.py --paper dna-foundation-models --prompt-only

    # Generate prompts for all papers with JATS content
    python llm_extract.py --all --prompt-only --output-dir benchmark/extraction_prompts/
"""

import sys
import json
import re
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).parent))
from config import BENCHMARK_DIR, TEST_CASES_DIR, GROUND_TRUTH_DIR, slugify


def get_text(elem):
    return "".join(elem.itertext()).strip() if elem is not None else ""


def extract_jats_sections(xml_text: str) -> dict:
    """Parse JATS XML into structured sections for LLM processing."""
    root = ET.fromstring(xml_text)

    result = {
        "title": get_text(root.find(".//article-title")),
        "abstract": get_text(root.find(".//abstract")),
        "sections": [],
        "figure_captions": [],
        "table_captions": [],
        "table_data": [],
        "references": [],
    }

    # Body sections with text
    body = root.find(".//body")
    if body is not None:
        for sec in body.findall("sec"):
            title = get_text(sec.find("title"))
            text = get_text(sec)
            if text and len(text) > 50:
                result["sections"].append({
                    "title": title,
                    "text": text[:5000],  # Cap per section
                })

    # Figure captions
    for fig in root.findall(".//fig"):
        label = get_text(fig.find("label"))
        caption = get_text(fig.find("caption"))
        if caption:
            result["figure_captions"].append(f"{label}: {caption[:500]}")

    # Table captions and any extractable data
    for tab in root.findall(".//table-wrap"):
        label = get_text(tab.find("label"))
        caption = get_text(tab.find("caption"))
        if caption:
            result["table_captions"].append(f"{label}: {caption[:500]}")

        # Try to get table rows
        table_elem = tab.find(".//table")
        if table_elem is not None:
            rows = []
            for tr in table_elem.findall(".//tr"):
                cells = [get_text(c)[:50] for c in tr.findall("*")]
                if cells:
                    rows.append(cells)
            if rows:
                result["table_data"].append({
                    "label": label,
                    "rows": rows[:20],
                })

    # References
    ref_list = root.find(".//ref-list")
    if ref_list is not None:
        for ref in ref_list.findall(".//ref"):
            title = get_text(ref.find(".//article-title"))
            if title:
                result["references"].append(title[:150])

    return result


def build_extraction_prompt(parsed: dict, venue: str) -> str:
    """Build the prompt for Claude to produce PaperOrchestra-quality extraction."""

    # Truncate sections to fit context
    sections_text = ""
    for sec in parsed["sections"][:10]:
        sections_text += f"\n### {sec['title']}\n{sec['text'][:3000]}\n"

    figures_text = "\n".join(parsed["figure_captions"][:10])
    tables_text = "\n".join(parsed["table_captions"][:10])

    # Include raw table data if available
    table_data_text = ""
    for td in parsed.get("table_data", [])[:5]:
        table_data_text += f"\n{td['label']}:\n"
        for row in td["rows"][:10]:
            table_data_text += "| " + " | ".join(row) + " |\n"

    prompt = f"""You are reverse-engineering a published research paper into pre-writing materials for a benchmark. Given the paper's content below, produce TWO documents that simulate what a researcher would have BEFORE writing the paper.

PAPER TITLE: {parsed['title']}
TARGET VENUE: {venue}

ABSTRACT:
{parsed['abstract']}

PAPER SECTIONS:
{sections_text}

FIGURE DESCRIPTIONS:
{figures_text}

TABLE DESCRIPTIONS:
{tables_text}

RAW TABLE DATA (if available):
{table_data_text}

REFERENCE COUNT: {len(parsed['references'])}

---

Produce exactly TWO documents separated by the marker "---EXPERIMENTAL_LOG---":

DOCUMENT 1: IDEA SUMMARY
Write as informal research notes BEFORE the paper was written. Include:
## Working title
## Core question
(What specific question does this paper answer?)
## Motivation / gap
(Bullet points: what's missing in prior work, why this matters)
## Core contribution (bullet form)
(4-6 specific, verifiable contributions with key numbers from the results)
## Method in brief
(2-3 paragraphs describing the approach, including any key equations or algorithms mentioned)
## Target venue
{venue}

DOCUMENT 2: EXPERIMENTAL LOG (after the ---EXPERIMENTAL_LOG--- marker)
Write as a raw lab notebook / data log. Include:
- Every comparison table as a MARKDOWN TABLE with | delimiters
- Extract ALL numeric results from the sections above into tables
- Group results by experiment type
- Include figure observations as factual statements (e.g., "Fig 2 shows X increases with Y")
- List all datasets, baselines, and metrics used
- Include statistical test results where mentioned

CRITICAL RULES:
- Do NOT include author names, affiliations, or acknowledgments
- Do NOT copy sentences verbatim — paraphrase as research notes
- ALL tables must use markdown format with | delimiters and header separators
- Include at least 3 data tables with numeric values
- The experimental log should be the LONGER document (aim for 3000+ words)
"""
    return prompt


def process_paper_for_extraction(paper_id: str) -> dict | None:
    """Load JATS content and build extraction prompt for a paper."""
    # Check for existing full-text ground truth (has the JATS data reference)
    gt_file = GROUND_TRUTH_DIR / paper_id / "full_text_ground_truth.json"
    if not gt_file.exists():
        return None

    gt = json.loads(gt_file.read_text(encoding="utf-8"))
    biorxiv_doi = gt.get("biorxiv_doi", "")

    # Also check metadata.json for DOI if not in ground truth
    if not biorxiv_doi:
        meta_file = TEST_CASES_DIR / paper_id / "metadata.json"
        if meta_file.exists():
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            biorxiv_doi = meta.get("biorxiv_doi", "")

    if not biorxiv_doi:
        return None

    # We need the JATS XML — fetch it
    import requests
    from config import biorxiv_limiter, BIORXIV_API

    biorxiv_limiter.wait()
    url = f"{BIORXIV_API}/details/biorxiv/{biorxiv_doi}"
    try:
        resp = requests.get(url, timeout=15)
        collection = resp.json().get("collection", [])
        if not collection:
            return None
        jats_url = collection[-1].get("jatsxml", "")
        if not jats_url:
            return None

        biorxiv_limiter.wait()
        xml_text = requests.get(jats_url, timeout=30).text
    except Exception as e:
        print(f"  Error fetching JATS for {paper_id}: {e}", file=sys.stderr)
        return None

    # Parse and build prompt
    parsed = extract_jats_sections(xml_text)

    # Get venue from metadata
    meta_file = TEST_CASES_DIR / paper_id / "metadata.json"
    venue = ""
    if meta_file.exists():
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
        venue = meta.get("published_venue", "") or ""

    prompt = build_extraction_prompt(parsed, venue)

    return {
        "paper_id": paper_id,
        "title": parsed["title"],
        "venue": venue,
        "prompt": prompt,
        "prompt_length": len(prompt),
        "sections": len(parsed["sections"]),
        "figures": len(parsed["figure_captions"]),
        "tables": len(parsed["table_captions"]),
        "references": len(parsed["references"]),
    }


def main():
    parser = argparse.ArgumentParser(description="LLM-powered paper extraction")
    parser.add_argument("--paper", type=str, help="Single paper ID")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--prompt-only", action="store_true",
                        help="Just generate prompts, don't call LLM")
    parser.add_argument("--output-dir", type=Path,
                        default=BENCHMARK_DIR / "extraction_prompts")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Get paper IDs
    if args.paper:
        paper_ids = [args.paper]
    elif args.all:
        paper_ids = sorted(d.name for d in GROUND_TRUTH_DIR.iterdir()
                           if d.is_dir() and (d / "full_text_ground_truth.json").exists())
        paper_ids = paper_ids[:args.limit]
    else:
        print("Specify --paper or --all", file=sys.stderr)
        sys.exit(1)

    processed = 0
    for paper_id in paper_ids:
        print(f"Processing: {paper_id[:50]}...", file=sys.stderr)
        result = process_paper_for_extraction(paper_id)
        if not result:
            print(f"  Skipped (no JATS data)", file=sys.stderr)
            continue

        # Save prompt
        prompt_file = args.output_dir / f"{paper_id}.txt"
        prompt_file.write_text(result["prompt"], encoding="utf-8")

        print(f"  Prompt: {result['prompt_length']} chars, "
              f"{result['sections']} sections, {result['references']} refs",
              file=sys.stderr)
        processed += 1

    print(f"\nGenerated {processed} extraction prompts in {args.output_dir}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
