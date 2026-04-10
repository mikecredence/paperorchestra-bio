#!/usr/bin/env python3
"""
Extract full paper content from bioRxiv JATS XML and re-engineer rich test cases.

This produces PaperOrchestra-quality inputs:
- Dense idea summary with methodology details
- Full experimental log with every table and figure description
- Complete reference list for Citation F1 ground truth

Usage:
    python extract_full_text.py --paper dna-foundation-models
    python extract_full_text.py --all --limit 20
"""

import sys
import json
import re
import time
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET

import requests

sys.path.insert(0, str(Path(__file__).parent))
from config import BENCHMARK_DIR, TEST_CASES_DIR, GROUND_TRUTH_DIR, biorxiv_limiter


def fetch_jats_xml(biorxiv_doi: str) -> str | None:
    """Fetch JATS XML full text from bioRxiv."""
    if not biorxiv_doi:
        return None

    # Get paper details to find JATS URL
    biorxiv_limiter.wait()
    url = f"https://api.biorxiv.org/details/biorxiv/{biorxiv_doi}"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        collection = data.get("collection", [])
        if not collection:
            return None

        paper = collection[-1]  # Latest version
        jats_url = paper.get("jatsxml", "")
        if not jats_url:
            return None

        biorxiv_limiter.wait()
        jats_resp = requests.get(jats_url, timeout=30)
        jats_resp.raise_for_status()
        return jats_resp.text

    except requests.RequestException as e:
        print(f"  Error fetching JATS: {e}", file=sys.stderr)
        return None


def get_text(elem):
    """Extract all text from an XML element and children."""
    if elem is None:
        return ""
    return "".join(elem.itertext()).strip()


def parse_jats(xml_text: str) -> dict:
    """Parse JATS XML into structured paper content."""
    root = ET.fromstring(xml_text)

    result = {
        "title": "",
        "abstract": "",
        "sections": [],
        "figures": [],
        "tables": [],
        "references": [],
        "methods_text": "",
        "results_text": "",
        "introduction_text": "",
    }

    # Title
    title_elem = root.find(".//article-title")
    result["title"] = get_text(title_elem)

    # Abstract
    abstract_elem = root.find(".//abstract")
    result["abstract"] = get_text(abstract_elem)

    # Body sections
    body = root.find(".//body")
    if body is not None:
        for sec in body.findall("sec"):
            title_elem = sec.find("title")
            title = get_text(title_elem) if title_elem is not None else ""
            text = get_text(sec)

            section = {"title": title, "text": text, "length": len(text)}
            result["sections"].append(section)

            # Categorize
            title_lower = title.lower()
            if "introduction" in title_lower:
                result["introduction_text"] = text
            elif "method" in title_lower or "materials" in title_lower:
                result["methods_text"] += text + "\n"
            elif "result" in title_lower:
                result["results_text"] += text + "\n"

    # Figures
    for fig in root.findall(".//fig"):
        label = get_text(fig.find("label"))
        caption = get_text(fig.find("caption"))
        result["figures"].append({"label": label, "caption": caption[:500]})

    # Tables
    for tab in root.findall(".//table-wrap"):
        label = get_text(tab.find("label"))
        caption = get_text(tab.find("caption"))

        # Try to extract table data
        table_data = []
        table_elem = tab.find(".//table")
        if table_elem is not None:
            for row in table_elem.findall(".//tr"):
                cells = [get_text(cell) for cell in row.findall("*")]  # th or td
                if cells:
                    table_data.append(cells)

        result["tables"].append({
            "label": label,
            "caption": caption[:500],
            "data": table_data[:30],  # Limit rows
        })

    # References
    ref_list = root.find(".//ref-list")
    if ref_list is not None:
        for ref in ref_list.findall(".//ref"):
            article_title = get_text(ref.find(".//article-title"))
            year = get_text(ref.find(".//year"))
            source = get_text(ref.find(".//source"))
            authors = []
            for name in ref.findall(".//name"):
                surname = get_text(name.find("surname"))
                given = get_text(name.find("given-names"))
                if surname:
                    authors.append(f"{surname}, {given}" if given else surname)

            if article_title:
                result["references"].append({
                    "title": article_title,
                    "authors": authors[:3],
                    "year": year,
                    "source": source,
                })

    return result


def generate_rich_idea_summary(parsed: dict, venue: str) -> str:
    """Generate a rich idea summary from parsed full-text content."""
    intro = parsed.get("introduction_text", "")[:3000]
    methods = parsed.get("methods_text", "")[:2000]
    abstract = parsed.get("abstract", "")

    # Extract key sentences from introduction for motivation
    intro_sentences = re.split(r'(?<=[.!?])\s+', intro)
    motivation = "\n".join(f"- {s[:200]}" for s in intro_sentences[:5] if len(s) > 30)

    # Extract method descriptions
    methods_brief = methods[:1500] if methods else "Methods not available from XML."

    return f"""# Idea Summary: {parsed['title']}

## Working title
{parsed['title']}

## Core question
{abstract[:500]}

## Motivation / gap
{motivation}

## Core contribution (bullet form)
Extracted from abstract:
{abstract}

## Method in brief
{methods_brief}

## Target venue
{venue}
"""


def generate_rich_experimental_log(parsed: dict) -> str:
    """Generate a rich experimental log from parsed full-text content."""
    lines = [f"# Experimental Log: {parsed['title']}\n"]
    lines.append("> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)\n")

    # Results text
    results = parsed.get("results_text", "")
    if results:
        lines.append("## Key Results\n")
        # Extract sentences with numbers
        sentences = re.split(r'(?<=[.!?])\s+', results)
        for s in sentences:
            if any(c.isdigit() for c in s) and len(s) > 30:
                lines.append(f"- {s[:300]}")
        lines.append("")

    # Tables
    if parsed["tables"]:
        lines.append("## Tables\n")
        for tab in parsed["tables"]:
            lines.append(f"### {tab['label']}")
            if tab["caption"]:
                lines.append(f"> {tab['caption'][:200]}\n")
            if tab["data"]:
                # Convert to markdown table
                for i, row in enumerate(tab["data"][:15]):
                    line = "| " + " | ".join(str(c)[:50] for c in row) + " |"
                    lines.append(line)
                    if i == 0:
                        lines.append("|" + "|".join("---" for _ in row) + "|")
            lines.append("")

    # Figures (descriptions only)
    if parsed["figures"]:
        lines.append("## Figure Descriptions\n")
        for fig in parsed["figures"]:
            lines.append(f"### {fig['label']}")
            lines.append(f"{fig['caption'][:300]}\n")

    # Reference count
    lines.append(f"## References")
    lines.append(f"Total references in published paper: {len(parsed['references'])}\n")

    # List key references
    if parsed["references"]:
        lines.append("### Key References (from published paper)")
        for ref in parsed["references"][:30]:
            authors = ", ".join(ref["authors"][:2])
            if len(ref["authors"]) > 2:
                authors += " et al."
            lines.append(f"- {ref['title'][:100]} ({authors}, {ref['year']})")

    lines.append(f"\n## Ground Truth Reference")
    lines.append(f"- Figures: {len(parsed['figures'])}")
    lines.append(f"- Tables: {len(parsed['tables'])}")
    lines.append(f"- References: {len(parsed['references'])}")

    return "\n".join(lines)


def process_paper(paper_id: str, meta: dict) -> bool:
    """Process a single paper: fetch JATS XML, extract, generate rich inputs."""
    biorxiv_doi = meta.get("biorxiv_doi")
    if not biorxiv_doi:
        print(f"  {paper_id}: no bioRxiv DOI, skipping", file=sys.stderr)
        return False

    print(f"  {paper_id}: fetching JATS XML...", file=sys.stderr)
    xml_text = fetch_jats_xml(biorxiv_doi)
    if not xml_text:
        print(f"  {paper_id}: JATS XML not available", file=sys.stderr)
        return False

    print(f"  {paper_id}: parsing ({len(xml_text)} chars)...", file=sys.stderr)
    parsed = parse_jats(xml_text)

    # Generate rich inputs
    venue = meta.get("published_venue", "")
    idea = generate_rich_idea_summary(parsed, venue)
    exp_log = generate_rich_experimental_log(parsed)

    # Save to rich_inputs subdirectory (don't overwrite existing test cases)
    rich_dir = BENCHMARK_DIR / "rich_inputs" / paper_id
    rich_dir.mkdir(parents=True, exist_ok=True)
    (rich_dir / "idea_summary.md").write_text(idea, encoding="utf-8")
    (rich_dir / "experimental_log.md").write_text(exp_log, encoding="utf-8")

    # Save parsed content for ground truth
    gt_dir = GROUND_TRUTH_DIR / paper_id
    gt_dir.mkdir(parents=True, exist_ok=True)
    gt_file = gt_dir / "full_text_ground_truth.json"
    gt_data = {
        "paper_id": paper_id,
        "title": parsed["title"],
        "num_sections": len(parsed["sections"]),
        "num_figures": len(parsed["figures"]),
        "num_tables": len(parsed["tables"]),
        "num_references": len(parsed["references"]),
        "reference_titles": [r["title"] for r in parsed["references"]],
        "extraction_method": "jats_xml_full_text",
    }
    gt_file.write_text(json.dumps(gt_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # Also update metadata with real counts
    meta_path = TEST_CASES_DIR / paper_id / "metadata.json"
    if meta_path.exists():
        meta_data = json.loads(meta_path.read_text())
        meta_data["ground_truth_citation_count"] = len(parsed["references"])
        meta_data["ground_truth_figure_count"] = len(parsed["figures"])
        meta_data["ground_truth_table_count"] = len(parsed["tables"])
        meta_path.write_text(json.dumps(meta_data, indent=2), encoding="utf-8")

    print(f"  {paper_id}: {len(parsed['sections'])} sections, "
          f"{len(parsed['references'])} refs, "
          f"{len(parsed['figures'])} figs, "
          f"{len(parsed['tables'])} tables, "
          f"idea={len(idea)} chars, log={len(exp_log)} chars",
          file=sys.stderr)

    return True


def main():
    parser = argparse.ArgumentParser(description="Extract full text from bioRxiv JATS XML")
    parser.add_argument("--paper", type=str, help="Single paper ID to process")
    parser.add_argument("--all", action="store_true", help="Process all benchmark papers")
    parser.add_argument("--limit", type=int, help="Max papers to process")
    args = parser.parse_args()

    # Load benchmark run papers
    run_file = BENCHMARK_DIR / "benchmark_run_20.json"
    if run_file.exists():
        paper_ids = json.loads(run_file.read_text())["papers"]
    else:
        paper_ids = [d.name for d in TEST_CASES_DIR.iterdir() if d.is_dir()]

    if args.paper:
        paper_ids = [args.paper]

    if args.limit:
        paper_ids = paper_ids[:args.limit]

    processed = 0
    skipped = 0
    for paper_id in paper_ids:
        meta_path = TEST_CASES_DIR / paper_id / "metadata.json"
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text())

        if process_paper(paper_id, meta):
            processed += 1
        else:
            skipped += 1

    print(f"\nProcessed: {processed}, Skipped: {skipped}", file=sys.stderr)


if __name__ == "__main__":
    main()
