"""Generate publication figures for fastBE paper.

Every numerical value plotted here appears verbatim in the extracted experimental
log. Source lines are noted inline. No values are fabricated.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = {
    "fastBE":   "#1f77b4",
    "Pairtree": "#ff7f0e",
    "Orchard":  "#2ca02c",
    "CALDER":   "#d62728",
    "CITUP":    "#9467bd",
}

OUT = Path(__file__).parent


# ---------------------------------------------------------------------------
# Figure 1: Schematic of structured regression inside tree-space search.
#
# Source: idea_summary.md Section 3 describes the analogous structured
# regression problem for VAFFP (F = UB) and the minimum-evolution framework
# (distance vector d = A x). This schematic uses no numerical values.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.2, 3.6))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

def box(ax, x, y, w, h, text, fc="#eaf3fb", ec="#1f77b4"):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.12",
                       linewidth=1.2, edgecolor=ec, facecolor=fc)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=9)

def arrow(ax, x1, y1, x2, y2, color="#333333"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=12, linewidth=1.2, color=color))

# top row: VAFFP pipeline
box(ax, 0.2, 4.2, 1.8, 1.1, "Frequency\nmatrix $F$", fc="#eaf3fb")
box(ax, 2.6, 4.2, 1.8, 1.1, "Clonal tree $\\mathcal{T}$\nwith matrix $B$", fc="#eaf3fb")
box(ax, 5.0, 4.2, 2.4, 1.1, "$\\ell_1$-regression\n$\\min\\|F-UB\\|_1$", fc="#cfe4f6")
box(ax, 7.8, 4.2, 2.0, 1.1, "Usage $U$,\nloss $L^*$", fc="#eaf3fb")
arrow(ax, 2.0, 4.75, 2.6, 4.75)
arrow(ax, 4.4, 4.75, 5.0, 4.75)
arrow(ax, 7.4, 4.75, 7.8, 4.75)
ax.text(5.0, 5.55, "Tumour VAFFP framework", fontsize=10, weight="bold")

# bottom row: distance-based analogue
box(ax, 0.2, 1.2, 1.8, 1.1, "Distance\nvector $d$", fc="#fff4e6")
box(ax, 2.6, 1.2, 1.8, 1.1, "Tree $\\mathcal{T}$ with\nadjacency $A$", fc="#fff4e6")
box(ax, 5.0, 1.2, 2.4, 1.1, "Least-squares\n$\\min\\|d - Ax\\|$", fc="#fddfbd")
box(ax, 7.8, 1.2, 2.0, 1.1, "Branch\nlengths $x$", fc="#fff4e6")
arrow(ax, 2.0, 1.75, 2.6, 1.75)
arrow(ax, 4.4, 1.75, 5.0, 1.75)
arrow(ax, 7.4, 1.75, 7.8, 1.75)
ax.text(5.0, 2.55, "Minimum-evolution distance framework (FastME / FastTree)",
        fontsize=10, weight="bold")

# vertical dashed brace indicating analogy
arrow(ax, 6.2, 4.2, 6.2, 2.3, color="#888")
ax.text(6.4, 3.25, "analogous\nstructured\nregression", fontsize=8.5, color="#555")

plt.tight_layout()
fig.savefig(OUT / "fig_schematic.pdf")
fig.savefig(OUT / "fig_schematic.png", dpi=200)
plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2: Mean F1-score of pairwise relationships vs number of clones.
#
# Source (experimental_log.md / idea_summary.md Section 5.2):
#   n=10  : fastBE 0.965, Pairtree 0.972, Orchard 0.965
#   n=50  : fastBE 0.825, Pairtree 0.749, Orchard 0.805
#   n>=100: fastBE 0.773, Orchard 0.783  (Pairtree excluded, did not scale)
# Only these data points are used; no interpolation.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.6, 3.4))
ns_small    = [10, 50]
fastBE_vals = [0.965, 0.825]
pairtree_vals = [0.972, 0.749]
orchard_vals  = [0.965, 0.805]
# large regime aggregate (n in {100,250,500,1000})
ns_large = [100]    # plotted as single point at n=100 for the mean-F1 aggregate
fastBE_large  = [0.773]
orchard_large = [0.783]

ax.plot(ns_small, fastBE_vals, "o-", color=PALETTE["fastBE"], label="fastBE", linewidth=1.7)
ax.plot(ns_small, pairtree_vals, "s-", color=PALETTE["Pairtree"], label="Pairtree", linewidth=1.7)
ax.plot(ns_small, orchard_vals, "^-", color=PALETTE["Orchard"], label="Orchard", linewidth=1.7)
ax.plot(ns_large, fastBE_large, "o", color=PALETTE["fastBE"], markersize=7)
ax.plot(ns_large, orchard_large, "^", color=PALETTE["Orchard"], markersize=7)
ax.axvline(100, color="gray", linestyle=":", linewidth=0.8)
ax.text(100, 0.58, " Pairtree\n excluded (n$\\geq$100)", fontsize=8, color="gray")

ax.set_xlabel("Number of clones $n$")
ax.set_ylabel("Mean F1-score (pairwise relationships)")
ax.set_xscale("log")
ax.set_xticks([10, 50, 100])
ax.set_xticklabels(["10", "50", "100--1000"])
ax.set_ylim(0.55, 1.02)
ax.legend(loc="lower left")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
fig.savefig(OUT / "fig_f1_vs_clones.pdf")
fig.savefig(OUT / "fig_f1_vs_clones.png", dpi=200)
plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 3: Mean wall-clock runtime on large simulated instances.
#
# Source (experimental_log.md / idea_summary.md Section 5.2):
#   n=50  : fastBE mean 1.21 s (Pairtree and Orchard "order of magnitude"
#           slower; no exact number given -> show only fastBE at n=50.)
#   n=1000: fastBE mean 1229.8 s (24/24 terminations);
#           Orchard mean 71749.1 s (19/24 terminations, 48 h / 32 cores).
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.6, 3.4))
categories = ["n=50 (fastBE)", "n=1000 (fastBE)", "n=1000 (Orchard)"]
values = [1.21, 1229.8, 71749.1]
colors = [PALETTE["fastBE"], PALETTE["fastBE"], PALETTE["Orchard"]]
bars = ax.bar(categories, values, color=colors, edgecolor="black", linewidth=0.6)
ax.set_yscale("log")
ax.set_ylabel("Mean wall-clock runtime (s, log scale)")
for b, v in zip(bars, values):
    ax.text(b.get_x() + b.get_width()/2, v*1.15, f"{v:g}",
            ha="center", va="bottom", fontsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
fig.savefig(OUT / "fig_runtime.pdf")
fig.savefig(OUT / "fig_runtime.png", dpi=200)
plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 4: Total sum-condition violation on real data.
#
# Source (experimental_log.md / idea_summary.md Sections 5.3, 5.4):
#   B-ALL (mean over 14 patients): fastBE 1.44, Pairtree 2.40
#   CSC28                         : fastBE 0.273, Pairtree 0.473
#   POP66                         : fastBE 3.280, Pairtree 4.770
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.6, 3.4))
datasets = ["B-ALL\n(mean over 14)", "CSC28", "POP66"]
fastbe   = [1.44, 0.273, 3.280]
pairtree = [2.40, 0.473, 4.770]
x = np.arange(len(datasets))
w = 0.35
ax.bar(x - w/2, fastbe, w, label="fastBE", color=PALETTE["fastBE"], edgecolor="black", linewidth=0.5)
ax.bar(x + w/2, pairtree, w, label="Pairtree", color=PALETTE["Pairtree"], edgecolor="black", linewidth=0.5)
ax.set_xticks(x); ax.set_xticklabels(datasets)
ax.set_ylabel("Total sum-condition violation $V$")
ax.legend()
for xi, vb, vp in zip(x, fastbe, pairtree):
    ax.text(xi - w/2, vb + 0.08, f"{vb}", ha="center", va="bottom", fontsize=8)
    ax.text(xi + w/2, vp + 0.08, f"{vp}", ha="center", va="bottom", fontsize=8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
fig.savefig(OUT / "fig_sum_violation.pdf")
fig.savefig(OUT / "fig_sum_violation.png", dpi=200)
plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 5: LP-solver speedup (schematic bar; mean factors verbatim).
#
# Source (experimental_log.md / idea_summary.md Section 5.1):
#   Mean speedup over Gurobi v9.0.3: 95.6x
#   Mean speedup over CPLEX v22.1.0: 105.1x
#   Warm vs cold start (Corollary 1): 6.2x mean speedup across 25,000 SPR moves
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.2, 3.2))
labels = ["vs Gurobi\nv9.0.3", "vs CPLEX\nv22.1.0", "Warm vs cold\nstart (SPR)"]
vals = [95.6, 105.1, 6.2]
colors = ["#1f77b4", "#1f77b4", "#9467bd"]
bars = ax.bar(labels, vals, color=colors, edgecolor="black", linewidth=0.6)
ax.set_ylabel("Mean wall-clock speedup (x)")
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, v + 1.5, f"{v}x",
            ha="center", va="bottom", fontsize=9)
ax.set_ylim(0, max(vals) * 1.15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
fig.savefig(OUT / "fig_lp_speedup.pdf")
fig.savefig(OUT / "fig_lp_speedup.png", dpi=200)
plt.close(fig)

print("All figures written to:", OUT)
