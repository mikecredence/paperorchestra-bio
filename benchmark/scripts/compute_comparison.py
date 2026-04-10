#!/usr/bin/env python3
"""Compute skill vs baseline comparison metrics for the benchmark run."""
import re
import json
import math
from pathlib import Path
from collections import defaultdict

results_dir = Path(__file__).parent.parent / "results"
tc_dir = Path(__file__).parent.parent / "test-cases"


def extract_metrics(tex_path, bib_path=None):
    """Extract structural metrics from a LaTeX paper."""
    content = tex_path.read_text(errors="replace")
    bib_content = bib_path.read_text(errors="replace") if bib_path and bib_path.exists() else ""

    sections = content.count(r"\section{")
    subsections = content.count(r"\subsection{")
    tables = content.count(r"\begin{table")
    figures = content.count(r"\begin{figure")

    cite_keys = set()
    for match in re.findall(r"\\cite[tp]?\*?\{([^}]+)\}", content):
        for key in match.split(","):
            cite_keys.add(key.strip())

    bib_entries = len(re.findall(r"@\w+\{", bib_content))
    word_count = len(re.sub(r"\\[a-zA-Z]+\{[^}]*\}", "", content).split())
    kb = len(content) / 1024

    return {
        "sections": sections,
        "subsections": subsections,
        "tables": tables,
        "figures": figures,
        "unique_citations": len(cite_keys),
        "bib_entries": bib_entries,
        "word_count": word_count,
        "size_kb": round(kb, 1),
    }


def stats(values):
    """Compute mean, std, min, max."""
    if not values:
        return {"mean": 0, "std": 0, "min": 0, "max": 0, "n": 0}
    n = len(values)
    mean = sum(values) / n
    var = sum((x - mean) ** 2 for x in values) / n
    return {
        "mean": round(mean, 1),
        "std": round(math.sqrt(var), 1),
        "min": min(values),
        "max": max(values),
        "n": n,
    }


# Collect metrics for both conditions
skill_metrics = []
baseline_metrics = []
paired = []  # Papers with both conditions

for d in sorted(results_dir.iterdir()):
    if not d.is_dir():
        continue

    skill_tex = d / "generated_paper" / "main.tex"
    baseline_tex = d / "baseline_paper" / "main.tex"
    skill_bib = d / "generated_paper" / "references.bib"
    baseline_bib = d / "baseline_paper" / "references.bib"

    # Get category from metadata
    meta_path = tc_dir / d.name / "metadata.json"
    category = "unknown"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())
        category = meta.get("category", "unknown")

    has_skill = skill_tex.exists()
    has_baseline = baseline_tex.exists()

    if has_skill:
        sm = extract_metrics(skill_tex, skill_bib)
        sm["paper_id"] = d.name
        sm["category"] = category
        skill_metrics.append(sm)

    if has_baseline:
        bm = extract_metrics(baseline_tex, baseline_bib)
        bm["paper_id"] = d.name
        bm["category"] = category
        baseline_metrics.append(bm)

    if has_skill and has_baseline:
        paired.append({
            "paper_id": d.name,
            "category": category,
            "skill": extract_metrics(skill_tex, skill_bib),
            "baseline": extract_metrics(baseline_tex, baseline_bib),
        })


# === MAIN COMPARISON TABLE ===
print("=" * 70)
print("BiomedWritingBench: Skill Pipeline vs Single-Agent Baseline")
print("=" * 70)
print()

metrics_to_compare = [
    ("unique_citations", "Unique Citations"),
    ("bib_entries", "BibTeX Entries"),
    ("tables", "Tables"),
    ("figures", "Figures"),
    ("subsections", "Subsections"),
    ("size_kb", "Paper Size (KB)"),
    ("word_count", "Word Count"),
]

print(f"{'Metric':<25s} {'Skill (n={len(skill_metrics)})':>20s} {'Baseline (n={len(baseline_metrics)})':>20s} {'Delta':>10s} {'% Improv':>10s}")
print("-" * 90)

for key, label in metrics_to_compare:
    skill_vals = [m[key] for m in skill_metrics]
    base_vals = [m[key] for m in baseline_metrics]
    s_stats = stats(skill_vals)
    b_stats = stats(base_vals)
    delta = s_stats["mean"] - b_stats["mean"]
    pct = (delta / b_stats["mean"] * 100) if b_stats["mean"] > 0 else 0
    print(f"{label:<25s} {s_stats['mean']:>7.1f} +/- {s_stats['std']:<7.1f} {b_stats['mean']:>7.1f} +/- {b_stats['std']:<7.1f} {delta:>+8.1f} {pct:>+8.1f}%")

# === PAIRED COMPARISON (papers with both conditions) ===
print(f"\n{'='*70}")
print(f"Paired Comparison ({len(paired)} papers with both conditions)")
print(f"{'='*70}")
print()

print(f"{'Paper':<47s} {'Skill Cites':>12s} {'Base Cites':>12s} {'Delta':>8s}")
print("-" * 82)
skill_wins = 0
for p in paired:
    sc = p["skill"]["unique_citations"]
    bc = p["baseline"]["unique_citations"]
    delta = sc - bc
    if sc > bc:
        skill_wins += 1
    print(f"{p['paper_id'][:47]:<47s} {sc:12d} {bc:12d} {delta:>+8d}")
print("-" * 82)
print(f"Skill wins: {skill_wins}/{len(paired)} ({skill_wins/len(paired)*100:.0f}%)")

# === PER-CATEGORY BREAKDOWN ===
print(f"\n{'='*70}")
print("Per-Subfield Breakdown (Skill Pipeline)")
print(f"{'='*70}")
print()

by_cat = defaultdict(list)
for m in skill_metrics:
    by_cat[m["category"]].append(m)

print(f"{'Category':<25s} {'N':>3s} {'Avg Cites':>10s} {'Avg Tables':>11s} {'Avg KB':>8s}")
print("-" * 60)
for cat in sorted(by_cat.keys()):
    papers = by_cat[cat]
    n = len(papers)
    avg_cites = sum(p["unique_citations"] for p in papers) / n
    avg_tables = sum(p["tables"] for p in papers) / n
    avg_kb = sum(p["size_kb"] for p in papers) / n
    print(f"{cat:<25s} {n:3d} {avg_cites:10.1f} {avg_tables:11.1f} {avg_kb:8.1f}")

# Save full results as JSON
output = {
    "skill_papers": len(skill_metrics),
    "baseline_papers": len(baseline_metrics),
    "paired_papers": len(paired),
    "comparison": {},
    "paired_results": paired,
}

for key, label in metrics_to_compare:
    skill_vals = [m[key] for m in skill_metrics]
    base_vals = [m[key] for m in baseline_metrics]
    output["comparison"][key] = {
        "skill": stats(skill_vals),
        "baseline": stats(base_vals),
    }

with open(results_dir / "comparison_results.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"\nFull results saved to {results_dir / 'comparison_results.json'}")
