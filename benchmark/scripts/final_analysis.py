#!/usr/bin/env python3
"""Final benchmark analysis: 3×2 factorial design with all 6 conditions.

Pipeline (2 levels): baseline vs skill
Input (3 levels): abstract vs XML-fulltext vs v2-LLM-structured

Conditions:
  abstract:  baseline_paper       vs  generated_paper
  XML:       baseline_rich_paper  vs  rich_paper
  v2-LLM:   baseline_v2_paper    vs  skill_v2_paper
"""
import json
import math
import re
from pathlib import Path
from collections import defaultdict

results_dir = Path(__file__).parent.parent / "results"
tc_dir = Path(__file__).parent.parent / "test-cases"

# 3×2 condition mapping: (input_type, pipeline) -> directory name
CONDITIONS = {
    ("abstract", "baseline"): "baseline_paper",
    ("abstract", "skill"): "generated_paper",
    ("xml", "baseline"): "baseline_rich_paper",
    ("xml", "skill"): "rich_paper",
    ("v2", "baseline"): "baseline_v2_paper",
    ("v2", "skill"): "skill_v2_paper",
}

INPUT_LABELS = {"abstract": "Abstract", "xml": "XML Full-Text", "v2": "v2 LLM-Structured"}
PIPELINE_LABELS = {"baseline": "Single Agent", "skill": "Skill Pipeline"}
AXES = ["clarity", "rigor", "completeness", "writing", "presentation", "citations", "overall"]


def load_judge(path):
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return data.get("scores", {})


def extract_tex_metrics(tex_path, bib_path=None):
    if not tex_path.exists():
        return None
    content = tex_path.read_text(errors="replace")
    bib = bib_path.read_text(errors="replace") if bib_path and bib_path.exists() else ""
    cite_keys = set()
    for m in re.findall(r"\\cite[tp]?\*?\{([^}]+)\}", content):
        for k in m.split(","):
            cite_keys.add(k.strip())
    return {
        "sections": content.count(r"\section{"),
        "tables": content.count(r"\begin{table"),
        "figures": content.count(r"\begin{figure"),
        "citations": len(cite_keys),
        "bib_entries": len(re.findall(r"@\w+\{", bib)),
        "word_count": len(re.sub(r"\\[a-zA-Z]+\{[^}]*\}", "", content).split()),
        "size_kb": round(len(content) / 1024, 1),
    }


def paired_wilcoxon(a_vals, b_vals):
    """Wilcoxon signed-rank test (normal approx for n>=10)."""
    diffs = [a - b for a, b in zip(a_vals, b_vals) if a != b]
    if not diffs:
        return {"p_approx": 1.0, "n_nonzero": 0}
    n = len(diffs)
    abs_diffs = sorted(enumerate(diffs), key=lambda x: abs(x[1]))
    ranks = list(range(1, n + 1))
    w_plus = sum(r for (i, d), r in zip(abs_diffs, ranks) if d > 0)
    w_minus = sum(r for (i, d), r in zip(abs_diffs, ranks) if d < 0)
    w = min(w_plus, w_minus)
    if n >= 10:
        mean_w = n * (n + 1) / 4
        std_w = math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
        z = (w - mean_w) / std_w if std_w > 0 else 0
        p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    else:
        p = None
    return {"W": w, "W+": w_plus, "W-": w_minus, "n": n, "p_approx": p, "z": z if n >= 10 else None}


def stats(vals):
    if not vals:
        return {"mean": 0, "std": 0, "n": 0}
    n = len(vals)
    mean = sum(vals) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in vals) / n)
    return {"mean": round(mean, 2), "std": round(std, 2), "n": n}


def sig_stars(p):
    if p is None:
        return ""
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return ""


# ============================================================
# Collect all data across 6 conditions
# ============================================================
all_data = defaultdict(dict)  # paper_id -> {(input, pipeline) -> {struct, judge}}

for d in sorted(results_dir.iterdir()):
    if not d.is_dir() or d.name in ("figures",):
        continue
    paper_id = d.name

    for (inp, pipe), cond_dir in CONDITIONS.items():
        tex_path = d / cond_dir / "main.tex"
        if not tex_path.exists():
            continue
        bib_path = d / cond_dir / "references.bib"
        judge_path = d / cond_dir / "llm_judge.json"

        entry = {
            "struct": extract_tex_metrics(tex_path, bib_path),
            "judge": load_judge(judge_path),
        }
        all_data[paper_id][(inp, pipe)] = entry

# Get categories
categories = {}
for paper_id in all_data:
    meta_path = tc_dir / paper_id / "metadata.json"
    if meta_path.exists():
        categories[paper_id] = json.loads(meta_path.read_text()).get("category", "unknown")
    else:
        categories[paper_id] = "unknown"


# ============================================================
# PRINT REPORT
# ============================================================
print("=" * 90)
print("BiomedWritingBench: 3×2 FACTORIAL EVALUATION REPORT")
print("=" * 90)

# --- Coverage ---
print("\n## 0. Coverage")
print(f"\n{'Condition':<30s} {'Papers':>8s} {'Judged':>8s}")
print("-" * 50)
for (inp, pipe), cond_dir in sorted(CONDITIONS.items()):
    n_papers = sum(1 for p in all_data.values() if (inp, pipe) in p)
    n_judged = sum(1 for p in all_data.values() if (inp, pipe) in p and p[(inp, pipe)]["judge"])
    print(f"{cond_dir:<30s} {n_papers:>8d} {n_judged:>8d}")


# --- Structural Metrics per Condition ---
print("\n## 1. Structural Metrics by Condition")
print(f"\n{'Condition':<30s} {'Citations':>12s} {'Tables':>10s} {'Words':>12s} {'Size KB':>10s}")
print("-" * 78)

for (inp, pipe), cond_dir in sorted(CONDITIONS.items()):
    entries = [p[(inp, pipe)]["struct"] for p in all_data.values() if (inp, pipe) in p and p[(inp, pipe)]["struct"]]
    if not entries:
        continue
    cites = stats([e["citations"] for e in entries])
    tables = stats([e["tables"] for e in entries])
    words = stats([e["word_count"] for e in entries])
    size = stats([e["size_kb"] for e in entries])
    print(f"{cond_dir:<30s} {cites['mean']:>5.1f}±{cites['std']:<4.1f} {tables['mean']:>4.1f}±{tables['std']:<3.1f} {words['mean']:>6.0f}±{words['std']:<4.0f} {size['mean']:>5.1f}±{size['std']:<3.1f}")


# --- LLM Judge: Full 6-condition comparison ---
print("\n## 2. LLM-as-Judge Quality Scores by Condition (0-100)")
print(f"\n{'Condition':<30s}", end="")
for axis in AXES:
    print(f" {axis[:7]:>8s}", end="")
print()
print("-" * 90)

condition_scores = {}
for (inp, pipe), cond_dir in sorted(CONDITIONS.items()):
    entries = [p[(inp, pipe)]["judge"] for p in all_data.values() if (inp, pipe) in p and p[(inp, pipe)]["judge"]]
    if not entries:
        print(f"{cond_dir:<30s}  (no judge data)")
        continue
    row_stats = {}
    print(f"{cond_dir:<30s}", end="")
    for axis in AXES:
        vals = [e.get(axis, 0) for e in entries]
        s = stats(vals)
        row_stats[axis] = s
        print(f" {s['mean']:>5.1f}±{s['std']:<2.0f}", end="")
    print(f"  (n={len(entries)})")
    condition_scores[(inp, pipe)] = row_stats


# --- Paired comparisons: Skill vs Baseline within each input type ---
print("\n## 3. Paired Skill vs Baseline Comparisons (Wilcoxon signed-rank)")

for inp in ["abstract", "xml", "v2"]:
    print(f"\n### Input: {INPUT_LABELS[inp]}")
    skill_cond = (inp, "skill")
    base_cond = (inp, "baseline")

    # Find papers that have BOTH conditions judged
    paired_ids = [pid for pid, data in all_data.items()
                  if skill_cond in data and base_cond in data
                  and data[skill_cond]["judge"] and data[base_cond]["judge"]]

    if not paired_ids:
        print("  No paired papers with judge scores.")
        continue

    print(f"  n = {len(paired_ids)} paired papers")
    print(f"  {'Axis':<18s} {'Skill':>12s} {'Baseline':>12s} {'Delta':>8s} {'p':>10s}")
    print(f"  {'-'*64}")

    for axis in AXES:
        s_vals = [all_data[pid][skill_cond]["judge"].get(axis, 0) for pid in paired_ids]
        b_vals = [all_data[pid][base_cond]["judge"].get(axis, 0) for pid in paired_ids]
        s = stats(s_vals)
        b = stats(b_vals)
        delta = s["mean"] - b["mean"]
        wt = paired_wilcoxon(s_vals, b_vals)
        p_str = f"p={wt['p_approx']:.4f}" if wt.get("p_approx") is not None else "n<10"
        stars = sig_stars(wt.get("p_approx"))
        print(f"  {axis:<18s} {s['mean']:>5.1f}±{s['std']:<4.1f} {b['mean']:>5.1f}±{b['std']:<4.1f} {delta:>+6.1f}  {p_str}{stars}")

    # Win/loss/tie on overall
    skill_wins = sum(1 for pid in paired_ids
                     if all_data[pid][skill_cond]["judge"].get("overall", 0) > all_data[pid][base_cond]["judge"].get("overall", 0))
    base_wins = sum(1 for pid in paired_ids
                    if all_data[pid][base_cond]["judge"].get("overall", 0) > all_data[pid][skill_cond]["judge"].get("overall", 0))
    ties = len(paired_ids) - skill_wins - base_wins
    print(f"  Overall winner: Skill {skill_wins}, Baseline {base_wins}, Tie {ties}")

    # Structural comparison
    s_struct_ids = [pid for pid in paired_ids
                    if all_data[pid][skill_cond].get("struct") and all_data[pid][base_cond].get("struct")]
    if s_struct_ids:
        print(f"\n  Structural (n={len(s_struct_ids)} paired):")
        for metric, label in [("citations", "Citations"), ("tables", "Tables"), ("word_count", "Words")]:
            sv = [all_data[pid][skill_cond]["struct"][metric] for pid in s_struct_ids]
            bv = [all_data[pid][base_cond]["struct"][metric] for pid in s_struct_ids]
            ss = stats(sv)
            bs = stats(bv)
            d = ss["mean"] - bs["mean"]
            wt = paired_wilcoxon(sv, bv)
            p_str = f"p={wt['p_approx']:.4f}" if wt.get("p_approx") is not None else "n<10"
            stars = sig_stars(wt.get("p_approx"))
            print(f"    {label:<15s} Skill {ss['mean']:>6.1f} vs Base {bs['mean']:>6.1f}  d={d:>+6.1f}  {p_str}{stars}")


# --- Cross-input comparisons (skill pipeline only) ---
print("\n## 4. Input Quality Comparison (Skill Pipeline Only)")
print("  Comparing overall quality across input types\n")

for inp_a, inp_b in [("abstract", "xml"), ("abstract", "v2"), ("xml", "v2")]:
    cond_a = (inp_a, "skill")
    cond_b = (inp_b, "skill")
    paired_ids = [pid for pid, data in all_data.items()
                  if cond_a in data and cond_b in data
                  and data[cond_a]["judge"] and data[cond_b]["judge"]]
    if not paired_ids:
        print(f"  {INPUT_LABELS[inp_a]} vs {INPUT_LABELS[inp_b]}: no paired papers")
        continue
    a_vals = [all_data[pid][cond_a]["judge"].get("overall", 0) for pid in paired_ids]
    b_vals = [all_data[pid][cond_b]["judge"].get("overall", 0) for pid in paired_ids]
    sa = stats(a_vals)
    sb = stats(b_vals)
    delta = sb["mean"] - sa["mean"]
    wt = paired_wilcoxon(b_vals, a_vals)
    p_str = f"p={wt['p_approx']:.4f}" if wt.get("p_approx") is not None else "n<10"
    stars = sig_stars(wt.get("p_approx"))
    print(f"  {INPUT_LABELS[inp_a]:>20s} ({sa['mean']:.1f}) vs {INPUT_LABELS[inp_b]:>20s} ({sb['mean']:.1f})  d={delta:>+5.1f}  {p_str}{stars}  (n={len(paired_ids)})")


# --- Per-subfield breakdown ---
print("\n## 5. Per-Subfield Overall Scores (Skill Pipeline)")
print(f"\n{'Subfield':<25s}", end="")
for inp in ["abstract", "xml", "v2"]:
    print(f" {INPUT_LABELS[inp]:>18s}", end="")
print()
print("-" * 80)

subfield_data = defaultdict(lambda: defaultdict(list))
for pid, data in all_data.items():
    cat = categories.get(pid, "unknown")
    for inp in ["abstract", "xml", "v2"]:
        cond = (inp, "skill")
        if cond in data and data[cond]["judge"]:
            subfield_data[cat][inp].append(data[cond]["judge"].get("overall", 0))

for cat in sorted(subfield_data.keys()):
    print(f"{cat:<25s}", end="")
    for inp in ["abstract", "xml", "v2"]:
        vals = subfield_data[cat][inp]
        if vals:
            s = stats(vals)
            print(f" {s['mean']:>6.1f}±{s['std']:<3.1f} (n={s['n']})", end="")
        else:
            print(f" {'---':>18s}", end="")
    print()


# --- Interaction analysis (2×2 for papers with abstract + one other input) ---
print("\n## 6. Interaction Analysis")
for inp in ["xml", "v2"]:
    paired_ids = [pid for pid, data in all_data.items()
                  if all(c in data and data[c]["judge"] for c in
                         [("abstract", "baseline"), ("abstract", "skill"), (inp, "baseline"), (inp, "skill")])]
    if not paired_ids:
        print(f"\n  Abstract × {INPUT_LABELS[inp]}: no papers with all 4 conditions")
        continue

    print(f"\n  2×2: Abstract vs {INPUT_LABELS[inp]} × Baseline vs Skill (n={len(paired_ids)})")
    ab = stats([all_data[pid][("abstract", "baseline")]["judge"]["overall"] for pid in paired_ids])
    ask = stats([all_data[pid][("abstract", "skill")]["judge"]["overall"] for pid in paired_ids])
    rb = stats([all_data[pid][(inp, "baseline")]["judge"]["overall"] for pid in paired_ids])
    rsk = stats([all_data[pid][(inp, "skill")]["judge"]["overall"] for pid in paired_ids])

    pipeline_effect = ((ask["mean"] - ab["mean"]) + (rsk["mean"] - rb["mean"])) / 2
    input_effect = ((rb["mean"] - ab["mean"]) + (rsk["mean"] - ask["mean"])) / 2
    interaction = (rsk["mean"] - rb["mean"]) - (ask["mean"] - ab["mean"])

    print(f"    Abstract+Baseline:  {ab['mean']:.1f}")
    print(f"    Abstract+Skill:     {ask['mean']:.1f}")
    print(f"    {INPUT_LABELS[inp]}+Baseline: {rb['mean']:.1f}")
    print(f"    {INPUT_LABELS[inp]}+Skill:    {rsk['mean']:.1f}")
    print(f"    Pipeline effect:    {pipeline_effect:+.1f}")
    print(f"    Input effect:       {input_effect:+.1f}")
    print(f"    Interaction:        {interaction:+.1f} ({'synergistic' if interaction > 0 else 'antagonistic' if interaction < 0 else 'none'})")


# ============================================================
# Save full results as JSON
# ============================================================
full_output = {
    "design": "3x2 factorial: Pipeline(baseline,skill) x Input(abstract,xml,v2)",
    "coverage": {},
    "condition_scores": {},
    "paired_comparisons": {},
    "structural_metrics": {},
}

for (inp, pipe), cond_dir in CONDITIONS.items():
    entries_j = [p[(inp, pipe)]["judge"] for p in all_data.values() if (inp, pipe) in p and p[(inp, pipe)]["judge"]]
    entries_s = [p[(inp, pipe)]["struct"] for p in all_data.values() if (inp, pipe) in p and p[(inp, pipe)]["struct"]]
    full_output["coverage"][cond_dir] = {
        "n_papers": sum(1 for p in all_data.values() if (inp, pipe) in p),
        "n_judged": len(entries_j),
    }
    if entries_j:
        full_output["condition_scores"][cond_dir] = {
            axis: stats([e.get(axis, 0) for e in entries_j]) for axis in AXES
        }
    if entries_s:
        full_output["structural_metrics"][cond_dir] = {
            metric: stats([e[metric] for e in entries_s])
            for metric in ["citations", "tables", "word_count", "size_kb"]
        }

# Save paired comparison stats
for inp in ["abstract", "xml", "v2"]:
    skill_cond = (inp, "skill")
    base_cond = (inp, "baseline")
    paired_ids = [pid for pid, data in all_data.items()
                  if skill_cond in data and base_cond in data
                  and data[skill_cond]["judge"] and data[base_cond]["judge"]]
    if paired_ids:
        comp = {}
        for axis in AXES:
            sv = [all_data[pid][skill_cond]["judge"].get(axis, 0) for pid in paired_ids]
            bv = [all_data[pid][base_cond]["judge"].get(axis, 0) for pid in paired_ids]
            comp[axis] = {
                "skill": stats(sv), "baseline": stats(bv),
                "delta": round(stats(sv)["mean"] - stats(bv)["mean"], 2),
                "wilcoxon": paired_wilcoxon(sv, bv),
            }
        full_output["paired_comparisons"][inp] = {"n_paired": len(paired_ids), "axes": comp}

out_path = results_dir / "factorial_analysis_3x2.json"
with open(out_path, "w") as f:
    json.dump(full_output, f, indent=2)
print(f"\nFull 3×2 analysis saved to {out_path}")
