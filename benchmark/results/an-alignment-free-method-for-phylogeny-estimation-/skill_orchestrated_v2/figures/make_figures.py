"""Generate figures for the Peafowl paper.

All numeric values are taken verbatim from inputs/experimental_log.md.
No values are fabricated. Datasets and nRF values sourced from the
experimental log table 'Peafowl nRF results on the seven datasets'.
"""

import os
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

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def savefig(fig, name):
    fig.savefig(os.path.join(OUT_DIR, name + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT_DIR, name + ".png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

# -----------------------------------------------------------------------------
# Figure 1: Pipeline schematic (schematic)
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.0, 2.3))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

stages = [
    ("Input\nDNA sequences", 0.8),
    ("Jellyfish\n$k$-mer counting\n($k\\in\\{9,11,\\ldots,31\\}$)", 3.0),
    ("Binary matrix\n($X_{ij}\\in\\{0,1\\}$)", 5.4),
    ("Select $k_\\mathrm{entropy}$\nby cumulative entropy\n($p=5000$ rows)", 7.5),
    ("RAxML\nBINGAMMA ML tree", 9.6),
]

box_colors = ["#e8e8e8", PALETTE[0], PALETTE[1], PALETTE[2], PALETTE[3]]
for (text, x), color in zip(stages, box_colors):
    ax.add_patch(FancyBboxPatch((x-0.95, 1.0), 1.9, 1.0,
                                 boxstyle="round,pad=0.05",
                                 facecolor=color, edgecolor="black",
                                 alpha=0.35 if color == "#e8e8e8" else 0.6,
                                 linewidth=1.0))
    ax.text(x, 1.5, text, ha="center", va="center", fontsize=8.5)

for i in range(len(stages) - 1):
    x_from = stages[i][1] + 0.95
    x_to = stages[i+1][1] - 0.95
    ax.annotate("", xy=(x_to, 1.5), xytext=(x_from, 1.5),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.0))

ax.text(5.0, 2.65, "Peafowl pipeline", ha="center", va="center",
        fontsize=11, fontweight="bold")
savefig(fig, "fig1_pipeline")

# -----------------------------------------------------------------------------
# Figure 2: Peafowl nRF across the seven real datasets (data-grounded)
# -----------------------------------------------------------------------------
# From experimental_log.md, 'Peafowl nRF results on the seven datasets':
#   7 Primates: 0
#   29 E.coli/Shigella (assembled): 0.23
#   25 Labroidei fish (mt): 0.05
#   14 plants: 0.36
#   27 E.coli/Shigella (full): 0.17
#   8 Yersinia (canonical): 1
#   8 Yersinia (non-canonical): 0
# Drosophila: not reported as a single numeric value in extraction, omitted from bar chart.

datasets = [
    "7 Primates\n(mt)",
    "25 Fish\n(mt)",
    "27 E.coli/\nShigella",
    "29 E.coli/\nShigella",
    "14 Plants",
    "8 Yersinia\n(canonical)",
    "8 Yersinia\n(non-canonical)",
]
nrf = [0.0, 0.05, 0.17, 0.23, 0.36, 1.00, 0.0]

fig, ax = plt.subplots(figsize=(7.0, 3.4))
x = np.arange(len(datasets))
bar_colors = [PALETTE[2] if v <= 0.1 else (PALETTE[0] if v < 0.5 else PALETTE[3]) for v in nrf]
bars = ax.bar(x, nrf, color=bar_colors, edgecolor="black", linewidth=0.7)
ax.axhline(0.1, color="gray", linewidth=0.6, linestyle=":", alpha=0.7)
ax.set_xticks(x)
ax.set_xticklabels(datasets, fontsize=8.5)
ax.set_ylabel("Normalized Robinson-Foulds distance (nRF)")
ax.set_ylim(0, 1.12)
ax.set_title("Peafowl nRF across seven benchmark datasets")
for bar, val in zip(bars, nrf):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f"{val:.2f}" if val > 0 else "0", ha="center", va="bottom", fontsize=8.5)

# legend via patches
good = mpatches.Patch(color=PALETTE[2], label="nRF $\\leq$ 0.1 (tied best)")
mid = mpatches.Patch(color=PALETTE[0], label="0.1 $<$ nRF $<$ 0.5")
bad = mpatches.Patch(color=PALETTE[3], label="nRF $\\geq$ 0.5")
ax.legend(handles=[good, mid, bad], loc="upper left", frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
savefig(fig, "fig2_nrf_bar")

# -----------------------------------------------------------------------------
# Figure 3: Canonical vs non-canonical on Yersinia (data-grounded)
# -----------------------------------------------------------------------------
# From experimental_log.md: 8 Yersinia canonical nRF = 1; non-canonical = 0.
modes = ["Canonical\ncounting", "Non-canonical\ncounting"]
vals = [1.0, 0.0]
fig, ax = plt.subplots(figsize=(4.2, 3.2))
bars = ax.bar(modes, vals, color=[PALETTE[3], PALETTE[2]], edgecolor="black", linewidth=0.7)
ax.set_ylim(0, 1.12)
ax.set_ylabel("nRF on 8 Yersinia dataset")
ax.set_title("Inversion signal recovery on Yersinia")
for bar, val in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f"{val:.0f}", ha="center", va="bottom", fontsize=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
savefig(fig, "fig3_yersinia_canonical")

print("Generated fig1_pipeline, fig2_nrf_bar, fig3_yersinia_canonical (pdf+png)")
