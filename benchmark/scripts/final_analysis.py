#!/usr/bin/env python3
"""Final benchmark analysis: structural + compilation + LLM judge + stats."""
import json
import math
import re
from pathlib import Path
from collections import defaultdict

results_dir = Path(__file__).parent.parent / "results"
tc_dir = Path(__file__).parent.parent / "test-cases"


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


def paired_wilcoxon(skill_vals, base_vals):
    """Simple Wilcoxon signed-rank test approximation."""
    diffs = [s - b for s, b in zip(skill_vals, base_vals) if s != b]
    if not diffs:
        return {"p_approx": 1.0, "n_nonzero": 0}
    n = len(diffs)
    abs_diffs = sorted(enumerate(diffs), key=lambda x: abs(x[1]))
    ranks = list(range(1, n + 1))
    w_plus = sum(r for (i, d), r in zip(abs_diffs, ranks) if d > 0)
    w_minus = sum(r for (i, d), r in zip(abs_diffs, ranks) if d < 0)
    w = min(w_plus, w_minus)
    # Normal approximation for n >= 10
    if n >= 10:
        mean_w = n * (n + 1) / 4
        std_w = math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
        z = (w - mean_w) / std_w if std_w > 0 else 0
        # Two-tailed p-value approximation
        p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    else:
        p = None  # Too few samples for normal approximation
    return {"W": w, "W+": w_plus, "W-": w_minus, "n": n, "p_approx": p}


def stats(vals):
    if not vals:
        return {"mean": 0, "std": 0, "n": 0}
    n = len(vals)
    mean = sum(vals) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in vals) / n)
    return {"mean": round(mean, 1), "std": round(std, 1), "n": n}


# Collect all data
papers = []
for d in sorted(results_dir.iterdir()):
    if not d.is_dir() or d.name in ("figures",):
        continue

    skill_tex = d / "generated_paper" / "main.tex"
    base_tex = d / "baseline_paper" / "main.tex"

    if not skill_tex.exists() and not base_tex.exists():
        continue

    meta_path = tc_dir / d.name / "metadata.json"
    category = "unknown"
    if meta_path.exists():
        category = json.loads(meta_path.read_text()).get("category", "unknown")

    entry = {"id": d.name, "category": category}

    if skill_tex.exists():
        entry["skill_struct"] = extract_tex_metrics(skill_tex, d / "generated_paper" / "references.bib")
        entry["skill_judge"] = load_judge(d / "generated_paper" / "llm_judge.json")
    if base_tex.exists():
        entry["base_struct"] = extract_tex_metrics(base_tex, d / "baseline_paper" / "references.bib")
        entry["base_judge"] = load_judge(d / "baseline_paper" / "llm_judge.json")

    papers.append(entry)


# Load compilation results
comp_results = {}
comp_path = results_dir / "compilation_results.json"
if comp_path.exists():
    comp_results = json.loads(comp_path.read_text())


# ====== PRINT REPORT ======
print("=" * 80)
print("BiomedWritingBench: FULL EVALUATION REPORT")
print("=" * 80)

# --- Structural Metrics ---
print("\n## 1. Structural Metrics (Skill vs Baseline)")
print(f"\n{'Metric':<25s} {'Skill':>15s} {'Baseline':>15s} {'Delta':>10s}")
print("-" * 70)

paired = [p for p in papers if "skill_struct" in p and "base_struct" in p]
for metric, label in [
    ("citations", "Unique Citations"),
    ("bib_entries", "BibTeX Entries"),
    ("tables", "Tables"),
    ("word_count", "Word Count"),
    ("size_kb", "Paper Size (KB)"),
]:
    s_vals = [p["skill_struct"][metric] for p in paired]
    b_vals = [p["base_struct"][metric] for p in paired]
    s = stats(s_vals)
    b = stats(b_vals)
    delta = s["mean"] - b["mean"]
    pct = (delta / b["mean"] * 100) if b["mean"] else 0
    # Wilcoxon test
    wt = paired_wilcoxon(s_vals, b_vals)
    p_str = f"p={wt['p_approx']:.4f}" if wt.get("p_approx") is not None else "n/a"
    sig = "*" if wt.get("p_approx") and wt["p_approx"] < 0.05 else ""
    print(f"{label:<25s} {s['mean']:>6.1f}±{s['std']:<5.1f} {b['mean']:>6.1f}±{b['std']:<5.1f} {delta:>+7.1f} ({pct:>+.0f}%) {p_str}{sig}")

# --- Compilation ---
print("\n## 2. LaTeX Compilation Rates")
for cond, label in [("generated_paper", "Skill"), ("baseline_paper", "Baseline")]:
    relevant = {k: v for k, v in comp_results.items() if cond in k}
    ok = sum(1 for v in relevant.values() if v.get("success"))
    n = len(relevant)
    avg_pages = sum(v["pages"] for v in relevant.values() if v.get("success")) / max(ok, 1)
    print(f"  {label:12s}: {ok}/{n} ({ok/n*100:.0f}%), avg {avg_pages:.1f} pages")

# --- LLM Judge Scores ---
print("\n## 3. LLM-as-Judge Quality Scores (0-100)")
axes = ["clarity", "rigor", "completeness", "writing", "presentation", "citations", "overall"]

print(f"\n{'Axis':<18s} {'Skill':>15s} {'Baseline':>15s} {'Delta':>10s} {'Stat':>15s}")
print("-" * 78)

judge_paired = [p for p in papers if p.get("skill_judge") and p.get("base_judge")]
for axis in axes:
    s_vals = [p["skill_judge"].get(axis, 0) for p in judge_paired]
    b_vals = [p["base_judge"].get(axis, 0) for p in judge_paired]
    s = stats(s_vals)
    b = stats(b_vals)
    delta = s["mean"] - b["mean"]
    wt = paired_wilcoxon(s_vals, b_vals)
    p_str = f"p={wt['p_approx']:.4f}" if wt.get("p_approx") is not None else "n/a"
    sig = "**" if wt.get("p_approx") and wt["p_approx"] < 0.01 else ("*" if wt.get("p_approx") and wt["p_approx"] < 0.05 else "")
    print(f"{axis:<18s} {s['mean']:>6.1f}±{s['std']:<5.1f} {b['mean']:>6.1f}±{b['std']:<5.1f} {delta:>+7.1f}  {p_str}{sig}")

# --- Skill wins on overall ---
skill_wins = sum(1 for p in judge_paired if p["skill_judge"].get("overall", 0) > p["base_judge"].get("overall", 0))
base_wins = sum(1 for p in judge_paired if p["base_judge"].get("overall", 0) > p["skill_judge"].get("overall", 0))
ties = len(judge_paired) - skill_wins - base_wins
print(f"\nOverall quality winner: Skill {skill_wins}, Baseline {base_wins}, Tie {ties} (n={len(judge_paired)})")

# --- Per-subfield ---
print("\n## 4. Per-Subfield Scores (Skill Pipeline)")
by_cat = defaultdict(list)
for p in papers:
    if p.get("skill_judge"):
        by_cat[p["category"]].append(p["skill_judge"].get("overall", 0))

print(f"{'Subfield':<25s} {'N':>3s} {'Overall':>10s}")
print("-" * 42)
for cat in sorted(by_cat.keys()):
    vals = by_cat[cat]
    s = stats(vals)
    print(f"{cat:<25s} {s['n']:3d} {s['mean']:>6.1f}±{s['std']:.1f}")

# --- Save full results ---
full_output = {
    "n_papers": len(paired),
    "n_judge_paired": len(judge_paired),
    "structural_comparison": {},
    "judge_comparison": {},
    "compilation": {
        "skill_rate": sum(1 for k, v in comp_results.items() if "generated" in k and v.get("success")) / max(sum(1 for k in comp_results if "generated" in k), 1),
        "baseline_rate": sum(1 for k, v in comp_results.items() if "baseline" in k and v.get("success")) / max(sum(1 for k in comp_results if "baseline" in k), 1),
    },
}

for metric in ["citations", "bib_entries", "tables", "word_count", "size_kb"]:
    s_vals = [p["skill_struct"][metric] for p in paired]
    b_vals = [p["base_struct"][metric] for p in paired]
    full_output["structural_comparison"][metric] = {
        "skill": stats(s_vals), "baseline": stats(b_vals),
        "wilcoxon": paired_wilcoxon(s_vals, b_vals),
    }

for axis in axes:
    s_vals = [p["skill_judge"].get(axis, 0) for p in judge_paired]
    b_vals = [p["base_judge"].get(axis, 0) for p in judge_paired]
    full_output["judge_comparison"][axis] = {
        "skill": stats(s_vals), "baseline": stats(b_vals),
        "wilcoxon": paired_wilcoxon(s_vals, b_vals),
    }

with open(results_dir / "final_analysis.json", "w") as f:
    json.dump(full_output, f, indent=2)

print(f"\nFull analysis saved to {results_dir / 'final_analysis.json'}")
