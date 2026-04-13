#!/usr/bin/env python3
"""
V3 extraction pipeline: two-phase lossless preservation of quantitative content.

Key change from v2: the LLM's job is to ORGANIZE extracted data, not to summarize.
All numeric values, statistical reports, and methodology parameters are extracted
deterministically in Phase 1 and handed to the LLM verbatim in Phase 2.

Phase 1 (deterministic, regex + XML):
- Full table content (no char-cell truncation, no row limit)
- Full figure captions (no truncation)
- Statistical sentences (F, t, chi-squared, p, r, %, n=, mean+/-SD, 95% CI)
- Methodology parameters (coordinates, volumes, titers, doses, durations)

Phase 2 (LLM, narrative organization only):
- Structures the extracted data into idea_summary_v3.md and experimental_log_v3.md
- Preserves every numeric value verbatim
- Never paraphrases statistical reports

Usage:
    # Single paper
    python llm_extract.py --paper dna-foundation-models --prompt-only

    # All papers with JATS ground truth
    python llm_extract.py --all --prompt-only --output-dir benchmark/extraction_prompts_v3/
"""

import sys
import json
import re
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).parent))
from config import BENCHMARK_DIR, TEST_CASES_DIR, GROUND_TRUTH_DIR, slugify


# ============================================================
# Phase 1: Deterministic extraction patterns
# ============================================================

# Statistical reporting patterns — preserve sentences containing ANY of these
STAT_PATTERNS = [
    r"F\s*\(\s*\d+\s*,\s*\d+\s*\)\s*=\s*-?\d+\.?\d*",        # F(4,68)=6.344
    r"F\s*=\s*-?\d+\.?\d*",                                    # F=6.344
    r"t\s*\(\s*\d+\s*\)\s*=\s*-?\d+\.?\d*",                  # t(24)=2.5
    r"\bt\s*=\s*-?\d+\.?\d*",                                  # t=2.5
    r"(?:χ²|[Cc]hi-?squared?|chi\s*squared?)\s*[=()]\s*\d+\.?\d*",
    r"[Uu]\s*=\s*\d+\.?\d*",                                   # U=5234 (Mann-Whitney)
    r"\bp\s*[<=>≤≥]\s*\d*\.?\d+(?:\s*[eE][-+]?\d+)?",         # p<0.05, p=0.003, p<1e-4
    r"\bP\s*[<=>≤≥]\s*\d*\.?\d+(?:\s*[eE][-+]?\d+)?",
    r"\br\s*=\s*-?\d*\.?\d+",                                  # r=0.937
    r"R\s*=\s*-?\d*\.?\d+",                                    # R=0.8
    r"R\s*\^?\s*2\s*=\s*-?\d*\.?\d+",                          # R^2=0.5
    r"-?\d+\.?\d*\s*±\s*-?\d+\.?\d*",                          # 83.2 ± 1.4
    r"-?\d+\.?\d*\s*\\pm\s*-?\d+\.?\d*",                       # LaTeX version
    r"\d+\.?\d*\s*%",                                           # 47.3%
    r"\bn\s*=\s*\d+",                                          # n=18
    r"\bN\s*=\s*\d+",                                          # N=18
    r"95\s*%\s*CI",                                            # 95% CI
    r"confidence\s+interval",
    r"Cohen'?s?\s*d\s*=\s*-?\d+\.?\d*",                        # Cohen's d=0.8
    r"η²|eta-?squared|eta\s*squared",
    r"[Oo]dds\s+ratio",
    r"fold[- ]change",
    r"-?\d+\.?\d*\s*[-–]\s*-?\d+\.?\d*\s*%",                   # range like 18-24%
]

# Methodology parameter patterns (units and measurements)
METHOD_PATTERNS = [
    r"[AM][PL]\s*-?\d+\.?\d*\s*(?:mm|μm|um)",                 # AP -1.3 mm, ML 1.0 mm
    r"DV\s*-?\d+\.?\d*(?:\s*[/,]\s*-?\d+\.?\d*)?\s*mm",       # DV -5.0/-4.3 mm
    r"\d+\.?\d*\s*(?:nl|µl|ul|ml|μl)",                         # 500 nl
    r"\d+\.?\d*\s*mg(?:\s*/\s*(?:kg|g|ml))?",                  # 0.13 mg/g
    r"\d+\.?\d*\s*(?:Hz|kHz|MHz)",                             # 75 Hz
    r"\d+\s*(?:ms|sec|min|hr|days?|weeks?|months?|years?)\b",
    r"\d+\.?\d*\s*(?:cm|mm|μm|um|nm)\b",                       # 360 cm
    r"\d+\s*×\s*\d+",                                          # 2 × 500
    r"\d+\.?\d*[eE][-+]?\d+\s*(?:vg/ml|TU|pfu)",               # 1e13 vg/ml
    r"titer\s+[\w.]+\s*[\d.eE+-]+",
    r"n\s*=\s*\d+\s+(?:mice|rats|animals|subjects|participants|cells|neurons)",
]


def get_text(elem):
    """Extract text from XML element, preserving spaces."""
    if elem is None:
        return ""
    return "".join(elem.itertext()).strip()


def split_sentences(text):
    """Simple sentence splitter that handles common abbreviations."""
    # Protect abbreviations
    text = re.sub(r"\b(Dr|Mr|Mrs|Ms|Prof|Fig|fig|Eq|eq|e\.g|i\.e|vs|et al|ref)\.", r"\1<DOT>", text)
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
    return [s.replace("<DOT>", ".").strip() for s in sentences if s.strip()]


def extract_statistical_sentences(text):
    """Return sentences that contain any statistical pattern, verbatim."""
    stat_re = re.compile("|".join(f"({p})" for p in STAT_PATTERNS), re.IGNORECASE)
    sentences = split_sentences(text)
    hits = [s for s in sentences if stat_re.search(s)]
    # Dedupe while preserving order
    seen = set()
    out = []
    for s in hits:
        key = s[:100]
        if key not in seen:
            seen.add(key)
            out.append(s)
    return out


def extract_methods_sentences(text):
    """Return sentences containing methodology parameters (coordinates, doses, etc.)."""
    method_re = re.compile("|".join(f"({p})" for p in METHOD_PATTERNS), re.IGNORECASE)
    sentences = split_sentences(text)
    hits = [s for s in sentences if method_re.search(s)]
    seen = set()
    out = []
    for s in hits:
        key = s[:100]
        if key not in seen:
            seen.add(key)
            out.append(s)
    return out


def extract_jats_sections(xml_text):
    """Parse JATS XML into structured paper content — LOSSLESS version (no truncation)."""
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

    # Full body sections (no truncation)
    body = root.find(".//body")
    if body is not None:
        for sec in body.findall("sec"):
            title = get_text(sec.find("title"))
            text = get_text(sec)
            if text and len(text) > 50:
                result["sections"].append({"title": title, "text": text})

    # Full figure captions (no truncation)
    for fig in root.findall(".//fig"):
        label = get_text(fig.find("label"))
        caption = get_text(fig.find("caption"))
        if caption:
            result["figure_captions"].append(f"{label}: {caption}")

    # Full table content (no cell truncation, no row limit)
    for tab in root.findall(".//table-wrap"):
        label = get_text(tab.find("label"))
        caption = get_text(tab.find("caption"))
        if caption:
            result["table_captions"].append(f"{label}: {caption}")

        table_elem = tab.find(".//table")
        if table_elem is not None:
            rows = []
            for tr in table_elem.findall(".//tr"):
                cells = [get_text(c) for c in tr.findall("*")]  # NO truncation
                if cells:
                    rows.append(cells)
            if rows:
                result["table_data"].append({"label": label, "caption": caption, "rows": rows})

    # Full references
    ref_list = root.find(".//ref-list")
    if ref_list is not None:
        for ref in ref_list.findall(".//ref"):
            title = get_text(ref.find(".//article-title"))
            year = get_text(ref.find(".//year"))
            if title:
                result["references"].append({"title": title, "year": year})

    return result


def extract_quantitative_content(parsed):
    """Run Phase 1 regex extraction over all parsed text."""
    full_text = parsed["abstract"] + "\n"
    for sec in parsed["sections"]:
        full_text += sec["text"] + "\n"
    for cap in parsed["figure_captions"]:
        full_text += cap + "\n"
    for cap in parsed["table_captions"]:
        full_text += cap + "\n"

    return {
        "statistical_sentences": extract_statistical_sentences(full_text),
        "methods_sentences": extract_methods_sentences(full_text),
    }


def render_markdown_table(label, caption, rows):
    """Render extracted table rows as a proper markdown table."""
    if not rows:
        return ""
    out = f"### {label}\n"
    if caption:
        out += f"*{caption}*\n\n"
    # Header row
    header = rows[0]
    ncols = len(header)
    out += "| " + " | ".join(cell or "" for cell in header) + " |\n"
    out += "| " + " | ".join(["---"] * ncols) + " |\n"
    # Data rows
    for row in rows[1:]:
        row_padded = row + [""] * (ncols - len(row))
        out += "| " + " | ".join(cell or "" for cell in row_padded[:ncols]) + " |\n"
    out += "\n"
    return out


# ============================================================
# Phase 2: LLM extraction prompt
# ============================================================

def build_extraction_prompt(parsed, quant, venue):
    """Build the LLM prompt with Phase 1 extracted content as ground truth."""

    # Full sections (no truncation — LLM gets all content)
    sections_text = ""
    for sec in parsed["sections"]:
        sections_text += f"\n### {sec['title']}\n{sec['text']}\n"

    figures_text = "\n".join(parsed["figure_captions"])
    tables_caption_text = "\n".join(parsed["table_captions"])

    # Rendered markdown tables from Phase 1 (verbatim table data)
    tables_md = ""
    for td in parsed["table_data"]:
        tables_md += render_markdown_table(td["label"], td.get("caption", ""), td["rows"])

    # Statistical reports extracted verbatim
    stat_block = "\n".join(f"- {s}" for s in quant["statistical_sentences"])
    methods_block = "\n".join(f"- {s}" for s in quant["methods_sentences"])

    ref_count = len(parsed["references"])

    prompt = f"""You are extracting research content from a published paper into pre-writing materials. Your job is to ORGANIZE the extracted data, NOT to summarize or paraphrase it.

PAPER TITLE: {parsed['title']}
TARGET VENUE: {venue}

ABSTRACT:
{parsed['abstract']}

FULL PAPER SECTIONS:
{sections_text}

FIGURE CAPTIONS (full text):
{figures_text}

TABLE CAPTIONS:
{tables_caption_text}

---
EXTRACTED TABLES (use these verbatim — do not modify cell values):
{tables_md}

---
EXTRACTED STATISTICAL REPORTS (preserve these verbatim in your output):
{stat_block}

---
EXTRACTED METHODS PARAMETERS (preserve verbatim in methods tables):
{methods_block}

REFERENCE COUNT: {ref_count}

---

Produce exactly TWO documents separated by the marker "---EXPERIMENTAL_LOG---":

DOCUMENT 1: IDEA SUMMARY
Structure as research notes that would exist BEFORE the paper was written:

## Working title
## Core question
(One focused research question)
## Motivation / gap
(3-5 bullet points — what prior work lacks and why this matters)
## Core contribution (bullet form)
(4-6 contributions, each with SPECIFIC NUMBERS from the extracted statistical reports)
## Method in brief
(2-3 paragraphs describing the approach. Include key equations and exact methodology parameters from the extracted block.)
## Target venue
{venue}

DOCUMENT 2: EXPERIMENTAL LOG (after the ---EXPERIMENTAL_LOG--- marker)
Structure as a lab notebook, organizing the extracted quantitative content:

- Use markdown tables with | delimiters for all structured data
- Copy the EXTRACTED TABLES above verbatim (preserve every cell value)
- Group related findings into sections (Training, Imaging, Experiment 1, etc.)
- Include the EXTRACTED STATISTICAL REPORTS organized by experiment. Every p-value, F-statistic, r, %, n=, and ± value must appear in your output exactly as in the extracted block.
- Include figure observations with their key statistics
- Include a Methods Parameters table with coordinates, volumes, titers, doses verbatim from the EXTRACTED METHODS block
- Include a Statistics section naming every statistical test used (e.g., "repeated-measures ANOVA with Greenhouse-Geisser correction", "Mann-Whitney U test")

CRITICAL RULES:
1. **Preserve every numeric value verbatim.** Do not round, paraphrase, or replace with qualitative words.
2. **Every cell in a results/comparison table must be numeric, N/A, or a categorical label** (e.g., a method name). NEVER use "Higher", "Lower", "Enriched", "Improved", "Better", "Worse", "Larger", "Smaller", "Stronger", "Weaker", "Comparable", "Competitive", "Significant" (alone without p-value), "Detected", "Increased", "Decreased", "Above chance", "Near 1:1", "Yes"/"No" (in results tables).
3. **Name every statistical test explicitly.** Not "appropriate test" — name it (Mann-Whitney U, chi-squared, t-test, ANOVA, etc.).
4. Do NOT include author names, affiliations, or acknowledgments.
5. Do NOT fabricate numbers. If a value was not reported, write "not reported" or omit it.
6. The experimental log should be comprehensive — organize ALL extracted content, do not skip sections.
"""
    return prompt


# ============================================================
# Orchestration
# ============================================================

def process_paper_for_extraction(paper_id):
    """Load JATS content, run Phase 1 extraction, build Phase 2 prompt."""
    gt_file = GROUND_TRUTH_DIR / paper_id / "full_text_ground_truth.json"
    if not gt_file.exists():
        return None

    gt = json.loads(gt_file.read_text(encoding="utf-8"))
    biorxiv_doi = gt.get("biorxiv_doi", "")

    if not biorxiv_doi:
        meta_file = TEST_CASES_DIR / paper_id / "metadata.json"
        if meta_file.exists():
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
            biorxiv_doi = meta.get("biorxiv_doi", "")

    if not biorxiv_doi:
        return None

    # Fetch JATS XML
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

    # Phase 1: lossless extraction
    parsed = extract_jats_sections(xml_text)
    quant = extract_quantitative_content(parsed)

    # Get venue
    meta_file = TEST_CASES_DIR / paper_id / "metadata.json"
    venue = ""
    if meta_file.exists():
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
        venue = meta.get("published_venue", "") or ""

    # Phase 2: build LLM prompt
    prompt = build_extraction_prompt(parsed, quant, venue)

    return {
        "paper_id": paper_id,
        "title": parsed["title"],
        "venue": venue,
        "prompt": prompt,
        "prompt_length": len(prompt),
        "sections": len(parsed["sections"]),
        "figures": len(parsed["figure_captions"]),
        "tables": len(parsed["table_data"]),
        "references": len(parsed["references"]),
        "stat_sentences": len(quant["statistical_sentences"]),
        "method_sentences": len(quant["methods_sentences"]),
        # Also save the Phase 1 extracted content for validation/inspection
        "extracted": {
            "statistical_sentences": quant["statistical_sentences"],
            "methods_sentences": quant["methods_sentences"],
            "table_count": len(parsed["table_data"]),
        },
    }


def main():
    parser = argparse.ArgumentParser(description="V3 two-phase extraction")
    parser.add_argument("--paper", type=str, help="Single paper ID")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--prompt-only", action="store_true",
                        help="Just generate prompts, don't call LLM")
    parser.add_argument("--output-dir", type=Path,
                        default=BENCHMARK_DIR / "extraction_prompts_v3")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

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

        # Also save Phase 1 extracted content as JSON for inspection/validation
        extracted_file = args.output_dir / f"{paper_id}.extracted.json"
        extracted_file.write_text(json.dumps(result["extracted"], indent=2), encoding="utf-8")

        print(f"  Prompt: {result['prompt_length']} chars, {result['sections']} sections, "
              f"{result['tables']} tables, {result['stat_sentences']} stat sentences, "
              f"{result['method_sentences']} method sentences, {result['references']} refs",
              file=sys.stderr)
        processed += 1

    print(f"\nGenerated {processed} v3 extraction prompts in {args.output_dir}", file=sys.stderr)


if __name__ == "__main__":
    main()
