#!/usr/bin/env python3
"""Compare skill_v2_paper (original) vs skill_v2_improved (A/B test)."""
import json
import math
from pathlib import Path

RES = Path(__file__).parent.parent / "results"
AXES = ["clarity", "rigor", "completeness", "writing", "presentation", "citations", "overall"]


def load(path):
    if not path.exists():
        return None
    return json.loads(path.read_text()).get("scores", {})


def stats(vals):
    if not vals:
        return {"mean": 0, "std": 0, "n": 0}
    n = len(vals)
    mean = sum(vals) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in vals) / n)
    return {"mean": round(mean, 2), "std": round(std, 2), "n": n}


def paired_wilcoxon(a, b):
    diffs = [x - y for x, y in zip(a, b) if x != y]
    if not diffs:
        return {"p": 1.0, "n": 0}
    n = len(diffs)
    sorted_diffs = sorted(enumerate(diffs), key=lambda x: abs(x[1]))
    ranks = list(range(1, n + 1))
    w_plus = sum(r for (_, d), r in zip(sorted_diffs, ranks) if d > 0)
    w_minus = sum(r for (_, d), r in zip(sorted_diffs, ranks) if d < 0)
    w = min(w_plus, w_minus)
    if n >= 6:
        mean_w = n * (n + 1) / 4
        std_w = math.sqrt(n * (n + 1) * (2 * n + 1) / 24)
        z = (w - mean_w) / std_w if std_w > 0 else 0
        p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    else:
        p = None
    return {"W": w, "n": n, "p": p, "w_plus": w_plus, "w_minus": w_minus}


def sig(p):
    if p is None:
        return ""
    if p < 0.001: return "***"
    if p < 0.01: return "**"
    if p < 0.05: return "*"
    return ""


# Find all papers with both conditions
paired = []
for d in sorted(RES.iterdir()):
    if not d.is_dir():
        continue
    orig = load(d / "skill_v2_paper" / "llm_judge.json")
    imp = load(d / "skill_v2_improved" / "llm_judge.json")
    if orig and imp:
        paired.append({"id": d.name, "orig": orig, "imp": imp})

print("=" * 88)
print("A/B TEST: skill_v2_paper (v1) vs skill_v2_improved (v2 pipeline)")
print("=" * 88)
print(f"\nN = {len(paired)} paired papers\n")

# Per-paper comparison
print(f"{'Paper':<52s} {'v1':>5s} {'v2':>5s} {'d':>5s}")
print("-" * 72)
improvements = []
for p in sorted(paired, key=lambda x: x["orig"].get("overall", 0)):
    o = p["orig"].get("overall", 0)
    i = p["imp"].get("overall", 0)
    d = i - o
    improvements.append(d)
    marker = "+" if d > 0 else ("-" if d < 0 else "=")
    print(f"{p['id'][:50]:<52s} {o:>5d} {i:>5d} {d:>+5d} {marker}")

# Per-axis comparison
print("\n## Per-axis Comparison\n")
print(f"{'Axis':<15s} {'v1 mean':>10s} {'v2 mean':>10s} {'Delta':>8s} {'p-value':>10s}  Wins(v2/v1/tie)")
print("-" * 80)
for axis in AXES:
    v1_vals = [p["orig"].get(axis, 0) for p in paired]
    v2_vals = [p["imp"].get(axis, 0) for p in paired]
    s1 = stats(v1_vals)
    s2 = stats(v2_vals)
    delta = s2["mean"] - s1["mean"]
    wt = paired_wilcoxon(v2_vals, v1_vals)
    p_str = f"p={wt['p']:.4f}" if wt.get("p") is not None else "n<6"
    stars = sig(wt.get("p"))
    v2_wins = sum(1 for a, b in zip(v2_vals, v1_vals) if a > b)
    v1_wins = sum(1 for a, b in zip(v2_vals, v1_vals) if a < b)
    ties = len(paired) - v2_wins - v1_wins
    print(f"{axis:<15s} {s1['mean']:>6.1f}\u00b1{s1['std']:<3.1f} {s2['mean']:>6.1f}\u00b1{s2['std']:<3.1f} {delta:>+6.1f}  {p_str}{stars}   {v2_wins}/{v1_wins}/{ties}")

# Bottom vs median split
print("\n## Split Analysis")

# Identify bottom 10 (lowest original overall)
sorted_by_orig = sorted(paired, key=lambda x: x["orig"].get("overall", 0))
bottom10 = sorted_by_orig[:10]
median10 = sorted_by_orig[10:]

for label, group in [("Bottom 10 (originally 77-79)", bottom10), ("Median 10 (originally 81-82)", median10)]:
    print(f"\n### {label}")
    for axis in AXES:
        v1 = [p["orig"].get(axis, 0) for p in group]
        v2 = [p["imp"].get(axis, 0) for p in group]
        s1 = stats(v1)
        s2 = stats(v2)
        delta = s2["mean"] - s1["mean"]
        print(f"  {axis:<15s} v1={s1['mean']:>5.1f}  v2={s2['mean']:>5.1f}  d={delta:>+5.1f}")

print(f"\n{'=' * 88}")
print(f"SUMMARY")
print(f"{'=' * 88}")
v2_wins = sum(1 for d in improvements if d > 0)
v1_wins = sum(1 for d in improvements if d < 0)
ties = len(improvements) - v2_wins - v1_wins
avg_delta = sum(improvements) / len(improvements)
print(f"Overall delta: {avg_delta:+.1f} points (v2 improved pipeline vs v1 original)")
print(f"v2 wins: {v2_wins}, v1 wins: {v1_wins}, ties: {ties} (n={len(paired)})")
