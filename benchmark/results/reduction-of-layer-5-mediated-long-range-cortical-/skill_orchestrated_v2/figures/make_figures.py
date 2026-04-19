"""Generate figures for L5 IT antipsychotic decorrelation paper.

All numerical values below are taken verbatim from the experimental log
(inputs/experimental_log.md). Only counts of ROI pairs, mouse counts, and
correction parameters that appear explicitly in the log are used.
"""

import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 10,
        "axes.titlesize": 11,
        "legend.fontsize": 9,
        "figure.dpi": 120,
    }
)

COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
HERE = os.path.dirname(os.path.abspath(__file__))


# -----------------------------------------------------------------------------
# Figure 1: Schematic of experimental approach
# -----------------------------------------------------------------------------
def make_fig_schematic():
    fig, ax = plt.subplots(figsize=(6.2, 3.4))

    def add_box(x, y, w, h, text, facecolor="#eaf2fb", edgecolor="#1f77b4"):
        box = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02",
            linewidth=1.2,
            edgecolor=edgecolor,
            facecolor=facecolor,
        )
        ax.add_patch(box)
        ax.text(
            x + w / 2,
            y + h / 2,
            text,
            ha="center",
            va="center",
            fontsize=9,
            wrap=True,
        )

    # Left column: mouse lines
    add_box(0.02, 0.70, 0.28, 0.18, "C57BL/6\n+ AAV-PHP.eB\n(pan-neuronal,\n6 mice)")
    add_box(0.02, 0.40, 0.28, 0.18, "Tlx3-Cre x Ai148\n(L5 IT neurons,\n14 mice)")
    add_box(0.02, 0.10, 0.28, 0.18, "Cux2-CreERT2 x Ai148\n(L2/3 neurons,\n3 mice)")

    # Middle: widefield macroscope
    add_box(
        0.36,
        0.38,
        0.28,
        0.30,
        "Widefield\nmacroscope\n(470 nm LED, 100 Hz)\n12 ROIs,\ndorsal cortex",
        facecolor="#fff2e0",
        edgecolor="#ff7f0e",
    )

    # Right: drug conditions
    add_box(
        0.70,
        0.70,
        0.28,
        0.18,
        "Clozapine\n(0.2-10 $\\mu$g/g)",
        facecolor="#e8f5e9",
        edgecolor="#2ca02c",
    )
    add_box(
        0.70,
        0.48,
        0.28,
        0.16,
        "Aripiprazole (0.2 $\\mu$g/g)\nHaloperidol (0.1 $\\mu$g/g)",
        facecolor="#e8f5e9",
        edgecolor="#2ca02c",
    )
    add_box(
        0.70,
        0.26,
        0.28,
        0.16,
        "Amphetamine\n(4 $\\mu$g/g)",
        facecolor="#fdecea",
        edgecolor="#d62728",
    )
    add_box(
        0.70,
        0.04,
        0.28,
        0.16,
        "Saline (0.9\\% NaCl)",
        facecolor="#f0f0f0",
        edgecolor="gray",
    )

    # Arrows
    for y_src in (0.79, 0.49, 0.19):
        arrow = FancyArrowPatch(
            (0.30, y_src), (0.36, 0.53), arrowstyle="->", mutation_scale=12, color="#333"
        )
        ax.add_patch(arrow)
    for y_tgt in (0.79, 0.56, 0.34, 0.12):
        arrow = FancyArrowPatch(
            (0.64, 0.53), (0.70, y_tgt), arrowstyle="->", mutation_scale=12, color="#333"
        )
        ax.add_patch(arrow)

    ax.text(
        0.50,
        0.95,
        "Cell-type-specific widefield imaging before/after i.p. drug injection",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    plt.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_schematic.pdf"))
    fig.savefig(os.path.join(HERE, "fig_schematic.png"), dpi=200)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Figure 2: ROI pair counts across the main correlation comparisons
# -----------------------------------------------------------------------------
def make_fig_pair_counts():
    # Values directly from statistical_sentences of experimental_log
    comparisons = [
        "C57BL/6\n+ clozapine",
        "Tlx3 x Ai148\n+ clozapine",
        "Tlx3 x Ai148\n+ haloperidol/\naripiprazole",
        "Cux2 x Ai148\n+ clozapine",
    ]
    short_range = [204, 182, 114, 137]
    long_range = [192, 148, 84, 127]

    x = np.arange(len(comparisons))
    width = 0.38

    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    ax.bar(x - width / 2, short_range, width, color=COLORS[0], label="Short-range pairs")
    ax.bar(x + width / 2, long_range, width, color=COLORS[1], label="Long-range pairs")
    for i, (s, l) in enumerate(zip(short_range, long_range)):
        ax.text(i - width / 2, s + 3, str(s), ha="center", va="bottom", fontsize=8)
        ax.text(i + width / 2, l + 3, str(l), ha="center", va="bottom", fontsize=8)

    ax.set_ylabel("Number of ROI pairs")
    ax.set_title("Pair counts per genotype $\\times$ drug comparison")
    ax.set_xticks(x)
    ax.set_xticklabels(comparisons, fontsize=8.5)
    ax.set_ylim(0, 230)
    ax.legend(loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_pair_counts.pdf"))
    fig.savefig(os.path.join(HERE, "fig_pair_counts.png"), dpi=200)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Figure 3: Mouse cohort sizes (reported in log for onset-response analyses)
# -----------------------------------------------------------------------------
def make_fig_mouse_counts():
    lines = [
        "C57BL/6",
        "Emx1-Cre",
        "Scnn1a-Cre",
        "Tlx3-Cre",
        "Ntsr1-Cre",
        "PV-Cre",
        "VIP-Cre",
        "Sst-Cre",
        "Cux2-CreERT2",
    ]
    counts = [6, 4, 7, 14, 3, 2, 6, 6, 3]

    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    bars = ax.bar(lines, counts, color=COLORS[0])
    bars[3].set_color(COLORS[1])  # Highlight Tlx3
    bars[8].set_color(COLORS[2])  # Highlight Cux2
    for bar, c in zip(bars, counts):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.25,
            str(c),
            ha="center",
            va="bottom",
            fontsize=9,
        )
    ax.set_ylabel("N mice (onset-response analyses)")
    ax.set_title("Mouse cohort sizes across genotypes")
    ax.set_ylim(0, 17)
    ax.set_xticklabels(lines, rotation=30, ha="right", fontsize=8.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legend
    handles = [
        mpatches.Patch(color=COLORS[0], label="Other / control"),
        mpatches.Patch(color=COLORS[1], label="Tlx3-Cre (L5 IT)"),
        mpatches.Patch(color=COLORS[2], label="Cux2-CreERT2 (L2/3)"),
    ]
    ax.legend(handles=handles, loc="upper right", fontsize=8)

    plt.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_mouse_counts.pdf"))
    fig.savefig(os.path.join(HERE, "fig_mouse_counts.png"), dpi=200)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Figure 4: Statistical significance summary (p-values reported in log)
# -----------------------------------------------------------------------------
def make_fig_pvalues():
    """Plot -log10(p) for the cross-genotype comparisons from the log.

    Reported p-value bounds (from experimental_log statistical_sentences):
      C57BL/6 vs Tlx3-Cre x Ai148 short-range: p < 0.05        -> -log10(p) > 1.3
      C57BL/6 vs Tlx3-Cre x Ai148 long-range:  p < 1e-5        -> -log10(p) > 5.0
      Cux2-CreERT2 vs Tlx3-Cre x Ai148 short:  p < 0.005       -> -log10(p) > 2.3
      Cux2-CreERT2 vs Tlx3-Cre x Ai148 long:   p < 1e-8        -> -log10(p) > 8.0

    We plot the reported *bounds* as conservative lower limits -- no
    fabricated exact values are introduced.
    """

    comparisons = ["C57BL/6 vs Tlx3", "Cux2 vs Tlx3"]
    short_bound = [-np.log10(0.05), -np.log10(0.005)]
    long_bound = [-np.log10(1e-5), -np.log10(1e-8)]

    x = np.arange(len(comparisons))
    width = 0.38

    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    ax.bar(x - width / 2, short_bound, width, color=COLORS[0], label="Short-range")
    ax.bar(x + width / 2, long_bound, width, color=COLORS[1], label="Long-range")

    for i, (s, l) in enumerate(zip(short_bound, long_bound)):
        ax.text(i - width / 2, s + 0.15, f"$<$10$^{{-{s:.1f}}}$", ha="center", fontsize=8)
        ax.text(i + width / 2, l + 0.15, f"$<$10$^{{-{l:.1f}}}$", ha="center", fontsize=8)

    ax.axhline(-np.log10(0.05), color="gray", linestyle="--", linewidth=0.7, label="$\\alpha = 0.05$")

    ax.set_ylabel("$-\\log_{10}(p)$ bound (rank-sum)")
    ax.set_title("Cross-genotype correlation comparisons (clozapine)")
    ax.set_xticks(x)
    ax.set_xticklabels(comparisons)
    ax.legend(loc="upper left", fontsize=8.5)
    ax.set_ylim(0, 10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_pvalues.pdf"))
    fig.savefig(os.path.join(HERE, "fig_pvalues.png"), dpi=200)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Figure 5: Session exclusion placeholder summary (0.26% excluded)
# -----------------------------------------------------------------------------
def make_fig_exclusion():
    kept = 3801 - 10
    excluded = 10
    sizes = [kept, excluded]
    labels = [f"Kept\n({kept} / 3801)", f"Excluded\n({excluded} / 3801; 0.26%)"]
    colors = [COLORS[0], COLORS[3]]

    fig, ax = plt.subplots(figsize=(4.0, 3.4))
    wedges, _ = ax.pie(
        sizes,
        labels=None,
        colors=colors,
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5},
    )
    ax.legend(wedges, labels, loc="lower center", bbox_to_anchor=(0.5, -0.15), fontsize=8.5, ncol=1)
    ax.set_title("Session inclusion\n($>$30\\% $\\Delta$F/F for $>$10 s excluded)")

    plt.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_exclusion.pdf"))
    fig.savefig(os.path.join(HERE, "fig_exclusion.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    make_fig_schematic()
    make_fig_pair_counts()
    make_fig_mouse_counts()
    make_fig_pvalues()
    make_fig_exclusion()
    print("All figures generated in", HERE)
