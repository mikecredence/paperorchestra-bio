#!/usr/bin/env python3
"""Compare generated papers against ground truth published papers."""
import json
import re
import math
from pathlib import Path
from difflib import SequenceMatcher

results_dir = Path(__file__).parent.parent / "results"
tc_dir = Path(__file__).parent.parent / "test-cases"
gt_dir = Path(__file__).parent.parent / "ground_truth"


def extract_abstract(tex_path):
    """Extract abstract text from LaTeX file."""
    if not tex_path.exists():
        return ""
    content = tex_path.read_text(errors="replace")
    # Find \begin{abstract}...\end{abstract}
    match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", content, re.DOTALL)
    if match:
        abstract = match.group(1).strip()
        # Strip LaTeX commands
        abstract = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", abstract)
        abstract = re.sub(r"\\[a-zA-Z]+", "", abstract)
        abstract = re.sub(r"[{}~]", " ", abstract)
        abstract = re.sub(r"\s+", " ", abstract).strip()
        return abstract
    return ""


def extract_metrics(tex_path, bib_path=None):
    """Extract structural metrics from LaTeX."""
    if not tex_path.exists():
        return None
    content = tex_path.read_text(errors="replace")
    bib = bib_path.read_text(errors="replace") if bib_path and bib_path.exists() else ""
    cite_keys = set()
    for m in re.findall(r"\\cite[tp]?\*?\{([^}]+)\}", content):
        for k in m.split(","):
            cite_keys.add(k.strip())
    return {
        "citations": len(cite_keys),
        "bib_entries": len(re.findall(r"@\w+\{", bib)),
        "tables": content.count(r"\begin{table"),
        "figures": content.count(r"\begin{figure"),
    }


def abstract_similarity(gen_abstract, gt_abstract):
    """Compute similarity between generated and ground truth abstracts."""
    if not gen_abstract or not gt_abstract:
        return None
    # Normalize
    gen = gen_abstract.lower().strip()
    gt = gt_abstract.lower().strip()
    return round(SequenceMatcher(None, gen, gt).ratio(), 3)


def stats(vals):
    if not vals:
        return {"mean": 0, "std": 0, "n": 0}
    n = len(vals)
    mean = sum(vals) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in vals) / n)
    return {"mean": round(mean, 1), "std": round(std, 1), "n": n}


# Collect comparisons
comparisons = []

for d in sorted(results_dir.iterdir()):
    if not d.is_dir():
        continue

    paper_id = d.name

    # Load ground truth
    gt_file = gt_dir / paper_id / "ground_truth.json"
    meta_file = tc_dir / paper_id / "metadata.json"

    gt_citations = None
    gt_figures = None
    gt_tables = None
    gt_abstract = ""
    category = "unknown"

    if gt_file.exists():
        gt = json.loads(gt_file.read_text())
        gt_citations = gt.get("estimated_references")
        gt_figures = gt.get("estimated_figures")
        gt_tables = gt.get("estimated_tables")
        gt_abstract = gt.get("abstract", "")

    if meta_file.exists():
        meta = json.loads(meta_file.read_text())
        gt_citations = gt_citations or meta.get("ground_truth_citation_count")
        gt_figures = gt_figures or meta.get("ground_truth_figure_count")
        gt_tables = gt_tables or meta.get("ground_truth_table_count")
        category = meta.get("category", "unknown")

    for condition in ["generated_paper", "baseline_paper"]:
        tex = d / condition / "main.tex"
        bib = d / condition / "references.bib"
        if not tex.exists():
            continue

        metrics = extract_metrics(tex, bib)
        gen_abstract = extract_abstract(tex)

        entry = {
            "paper_id": paper_id,
            "condition": "skill" if condition == "generated_paper" else "baseline",
            "category": category,
            "gen_citations": metrics["citations"],
            "gen_tables": metrics["tables"],
            "gen_figures": metrics["figures"],
            "gt_citations": gt_citations,
            "gt_figures": gt_figures,
            "gt_tables": gt_tables,
        }

        # Citation ratio (gen / gt)
        if gt_citations and gt_citations > 0:
            entry["citation_ratio"] = round(metrics["citations"] / gt_citations, 2)
            entry["citation_gap"] = gt_citations - metrics["citations"]

        # Table ratio
        if gt_tables and gt_tables > 0:
            entry["table_ratio"] = round(metrics["tables"] / gt_tables, 2)

        # Abstract similarity
        if gt_abstract and gen_abstract:
            entry["abstract_similarity"] = abstract_similarity(gen_abstract, gt_abstract)

        comparisons.append(entry)


# ====== REPORT ======
print("=" * 80)
print("GROUND TRUTH COMPARISON: Generated Papers vs Published Papers")
print("=" * 80)

# --- Citation Gap ---
print("\n## 1. Citation Count: Generated vs Ground Truth")
print(f"\n{'Condition':<12s} {'Avg Gen':>10s} {'Avg GT':>10s} {'Ratio':>8s} {'Gap':>8s}")
print("-" * 55)

for cond in ["skill", "baseline"]:
    entries = [c for c in comparisons if c["condition"] == cond and c.get("gt_citations")]
    if not entries:
        continue
    gen_vals = [c["gen_citations"] for c in entries]
    gt_vals = [c["gt_citations"] for c in entries]
    ratios = [c["citation_ratio"] for c in entries]
    gaps = [c["citation_gap"] for c in entries]
    print(f"{cond:<12s} {stats(gen_vals)['mean']:>10.1f} {stats(gt_vals)['mean']:>10.1f} "
          f"{stats(ratios)['mean']:>7.2f}x {stats(gaps)['mean']:>+7.1f}")

# --- Per-paper citation comparison ---
print("\n## 2. Per-Paper Citation Comparison (Skill Pipeline)")
print(f"\n{'Paper':<47s} {'Gen':>5s} {'GT':>5s} {'Ratio':>7s}")
print("-" * 68)

skill_entries = [c for c in comparisons if c["condition"] == "skill" and c.get("gt_citations")]
for e in sorted(skill_entries, key=lambda x: x.get("citation_ratio", 0), reverse=True):
    print(f"{e['paper_id'][:47]:<47s} {e['gen_citations']:>5d} {e['gt_citations']:>5d} {e.get('citation_ratio', 0):>6.2f}x")

# --- Abstract Similarity ---
print("\n## 3. Abstract Similarity to Ground Truth")
print("   (SequenceMatcher ratio: 0 = no overlap, 1 = identical)")

for cond in ["skill", "baseline"]:
    entries = [c for c in comparisons if c["condition"] == cond and c.get("abstract_similarity") is not None]
    if not entries:
        continue
    sims = [c["abstract_similarity"] for c in entries]
    s = stats(sims)
    print(f"\n  {cond}: mean={s['mean']:.3f} ± {s['std']:.3f} (n={s['n']})")

print("\n  Per-paper (Skill):")
skill_abs = [c for c in comparisons if c["condition"] == "skill" and c.get("abstract_similarity") is not None]
for e in sorted(skill_abs, key=lambda x: x["abstract_similarity"], reverse=True):
    print(f"    {e['paper_id'][:45]:<45s} {e['abstract_similarity']:.3f}")

# --- Table comparison ---
print("\n## 4. Table Count: Generated vs Ground Truth")
for cond in ["skill", "baseline"]:
    entries = [c for c in comparisons if c["condition"] == cond and c.get("gt_tables")]
    if not entries:
        continue
    gen_tabs = [c["gen_tables"] for c in entries]
    gt_tabs = [c["gt_tables"] for c in entries]
    ratios = [c.get("table_ratio", 0) for c in entries]
    print(f"  {cond}: gen={stats(gen_tabs)['mean']:.1f} vs gt={stats(gt_tabs)['mean']:.1f} "
          f"(ratio={stats(ratios)['mean']:.2f}x)")

# Save
output = {"comparisons": comparisons}
with open(results_dir / "ground_truth_comparison.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {results_dir / 'ground_truth_comparison.json'}")
