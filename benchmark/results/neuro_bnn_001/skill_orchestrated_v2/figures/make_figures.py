"""Generate figures for the FlyWire network-statistics manuscript.

All numerical values used below are extracted verbatim from the experimental
log (inputs/experimental_log.md). No values are fabricated or inferred.
"""
from __future__ import annotations

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
    "figure.dpi": 120,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
OUT = os.path.dirname(os.path.abspath(__file__))


def _save(fig, stem):
    fig.savefig(os.path.join(OUT, f"{stem}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, f"{stem}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# -------------------------------------------------------------------
# Figure 1. Whole-brain connectivity: giant component fractions and
# rich-club regime on the total-degree axis.
# Values from experimental log:
#  - Giant SCC contains 93.3% of neurons.
#  - Giant WCC contains 98.8% of neurons.
#  - Rich-club regime: total-degree 37 to 93 (Phi_norm > 1.01).
# -------------------------------------------------------------------
def figure_global_connectivity():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.1))

    # Panel a: giant component fractions
    ax = axes[0]
    labels = ["Giant SCC", "Giant WCC"]
    fractions = [93.3, 98.8]  # percent
    bars = ax.bar(labels, fractions, color=[PALETTE[0], PALETTE[1]], width=0.55)
    ax.set_ylim(0, 105)
    ax.set_ylabel("Neurons in component (\%)")
    ax.set_title("Giant connected components")
    for bar, f in zip(bars, fractions):
        ax.text(bar.get_x() + bar.get_width() / 2, f + 1.2, f"{f:.1f}\%",
                ha="center", va="bottom", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Panel b: rich-club regime band on total-degree axis
    ax = axes[1]
    k_min, k_max = 37, 93
    ax.axvspan(k_min, k_max, color=PALETTE[2], alpha=0.25, label="Rich-club regime")
    ax.axvline(k_min, color=PALETTE[2], linestyle="--", linewidth=1.2)
    ax.axvline(k_max, color=PALETTE[2], linestyle="--", linewidth=1.2)
    ax.set_xlim(0, 150)
    ax.set_ylim(0.8, 1.4)
    ax.axhline(1.0, color="gray", linewidth=0.8)
    ax.axhline(1.01, color=PALETTE[3], linewidth=0.8, linestyle=":",
               label=r"$\Phi_{\mathrm{norm}} = 1.01$ threshold")
    ax.set_xlabel("Total degree $k$")
    ax.set_ylabel(r"$\Phi_{\mathrm{norm}}(k)$ (schematic)")
    ax.set_title("Rich-club regime")
    ax.annotate(f"k = {k_min}", xy=(k_min, 1.25), xytext=(k_min - 25, 1.32),
                fontsize=8, arrowprops=dict(arrowstyle="->", color="gray"))
    ax.annotate(f"k = {k_max}", xy=(k_max, 1.25), xytext=(k_max + 8, 1.32),
                fontsize=8, arrowprops=dict(arrowstyle="->", color="gray"))
    ax.legend(loc="lower right", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.suptitle("Whole-brain connectivity and rich-club regime", y=1.02)
    fig.tight_layout()
    _save(fig, "fig1_global")


# -------------------------------------------------------------------
# Figure 2. Rich-club sub-populations and their cholinergic fractions.
# Values from experimental log:
#  - 40,218 rich-club neurons; 676 broadcasters; 638 integrators;
#    37,093 balanced.
#  - Broadcasters 75% cholinergic; integrators 49% cholinergic.
#  - Bilateral inputs: rich club 18%, broadcasters 16%, integrators 23%.
#  - All neurons: 11% bilateral inputs.
# -------------------------------------------------------------------
def figure_populations():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2))

    # Panel a: population counts (log scale)
    ax = axes[0]
    pops = ["Rich club", "Balanced", "Broadcasters", "Integrators", "NSRNs"]
    counts = [40218, 37093, 676, 638, 1863]
    colors = [PALETTE[0], PALETTE[4], PALETTE[1], PALETTE[2], PALETTE[3]]
    bars = ax.barh(pops, counts, color=colors)
    ax.set_xscale("log")
    ax.set_xlabel("Number of neurons (log scale)")
    ax.set_title("Rich-club sub-populations")
    for bar, c in zip(bars, counts):
        ax.text(bar.get_width() * 1.06, bar.get_y() + bar.get_height() / 2,
                f"{c:,}", va="center", fontsize=8)
    ax.invert_yaxis()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Panel b: cholinergic fraction and bilateral-input fraction by population
    ax = axes[1]
    groups = ["All neurons", "Rich club", "Broadcasters", "Integrators"]
    ach = [np.nan, np.nan, 75, 49]  # only reported for broadcasters/integrators
    bilat = [11, 18, 16, 23]
    x = np.arange(len(groups))
    width = 0.38
    ach_vals = [v if not np.isnan(v) else 0 for v in ach]
    mask = [not np.isnan(v) for v in ach]
    ax.bar(x - width / 2, ach_vals, width, color=PALETTE[1],
           label="\% cholinergic", alpha=[1.0 if m else 0.0 for m in mask][0])
    # Draw cholinergic only where reported
    for xi, val, m in zip(x, ach_vals, mask):
        if m:
            ax.bar(xi - width / 2, val, width, color=PALETTE[1])
            ax.text(xi - width / 2, val + 1.5, f"{val}\%", ha="center", fontsize=8)
    ax.bar(x + width / 2, bilat, width, color=PALETTE[0],
           label="\% bilateral inputs")
    for xi, val in zip(x, bilat):
        ax.text(xi + width / 2, val + 1.5, f"{val}\%", ha="center", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(groups, rotation=15, ha="right")
    ax.set_ylabel("Percent of neurons")
    ax.set_ylim(0, 90)
    ax.set_title("Composition of populations")
    ax.legend(frameon=False, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    _save(fig, "fig2_populations")


# -------------------------------------------------------------------
# Figure 3. Reciprocity and clustering coefficient in the fly brain vs.
# Erdos-Renyi null model.
# Values from experimental log / Table 2:
#  - Fly: reciprocity 0.138, clustering 0.0463.
#  - ER clustering 0.0003 (explicitly reported).
#  - Small-world comparison: fly path 3.91 vs. ER 3.57.
# -------------------------------------------------------------------
def figure_reciprocity_clustering():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.1))

    # Panel a: reciprocity vs. baseline (ER reciprocity equals density = 0.000161
    # for a directed ER with matched density; we display only verified numbers).
    ax = axes[0]
    labels = ["Fly brain", "Connection prob."]
    values = [0.138, 0.000161]
    bars = ax.bar(labels, values, color=[PALETTE[0], "#888888"])
    ax.set_yscale("log")
    ax.set_ylabel("Probability (log scale)")
    ax.set_title("Reciprocity vs. random expectation")
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v * 1.3, f"{v:g}",
                ha="center", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Panel b: clustering coefficient
    ax = axes[1]
    labels = ["Fly brain", "ER null"]
    values = [0.0463, 0.0003]
    bars = ax.bar(labels, values, color=[PALETTE[0], "#888888"])
    ax.set_ylabel("Clustering coefficient")
    ax.set_title("Clustering coefficient")
    ax.set_ylim(0, 0.06)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.002, f"{v:g}",
                ha="center", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    _save(fig, "fig3_recip_clustering")


# -------------------------------------------------------------------
# Figure 4. Mean percentile rank of rich-club populations relative to the
# set of all sensory inputs.
# Values from experimental log:
#  - Rich club mean percentile rank 44%.
#  - Integrators 43%.
#  - Broadcasters 53%.
# -------------------------------------------------------------------
def figure_sensory_rank():
    fig, ax = plt.subplots(figsize=(4.6, 3.1))
    labels = ["Rich club", "Integrators", "Broadcasters"]
    values = [44, 43, 53]
    colors = [PALETTE[0], PALETTE[2], PALETTE[1]]
    bars = ax.bar(labels, values, color=colors, width=0.55)
    ax.axhline(50, color="gray", linewidth=0.8, linestyle="--",
               label="Brain-wide mean (50\%)")
    ax.set_ylim(0, 70)
    ax.set_ylabel("Mean percentile rank (\%)")
    ax.set_title("Proximity to sensory inputs")
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 1.2, f"{v}\%",
                ha="center", fontsize=9)
    ax.legend(frameon=False, loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    _save(fig, "fig4_sensory_rank")


def main():
    plt.rcParams["text.usetex"] = False
    figure_global_connectivity()
    figure_populations()
    figure_reciprocity_clustering()
    figure_sensory_rank()
    print("Wrote 4 figures (PDF + PNG each) to", OUT)


if __name__ == "__main__":
    main()
