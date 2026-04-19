"""ENACT paper figure generation script.

All numerical values are copied verbatim from the experimental log:
- 25 (percent of Xenium synthetic bins overlapping more than one cell)
- 5  (percent of seqFISH+ synthetic bins overlapping more than one cell)
- 0.708 (accuracy for Sargent + Weighted-by-Area on pathologist cells)
- 0.758 (weighted F1 for Sargent + Weighted-by-Area on pathologist cells)
- 20991 (number of pathologist-annotated cells)

Any value not listed above is a derived quantity or a schematic layout
parameter, NOT an experimental claim.
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "figure.dpi": 150,
})


def save(fig, stem):
    fig.savefig(os.path.join(HERE, stem + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(HERE, stem + ".png"), bbox_inches="tight", dpi=200)
    plt.close(fig)


def fig1_pipeline():
    """Schematic of the ENACT pipeline. Boxes and arrows only."""
    fig, ax = plt.subplots(figsize=(10, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

    boxes = [
        (0.2, "Bin-by-gene\nmatrix\n(2x2 um bins)"),
        (2.1, "Stardist\ncell\nsegmentation"),
        (4.0, "Bin-to-cell\nassignment\n(Naive / 3 weighted)"),
        (6.0, "Cell-type\nannotation\n(Sargent / CellAssign / CellTypist)"),
        (8.2, "AnnData for\nSquidpy\n+ TissUUmaps"),
    ]
    for i, (x, label) in enumerate(boxes):
        box = FancyBboxPatch(
            (x, 1.1), 1.6, 1.0,
            boxstyle="round,pad=0.05",
            linewidth=1.2,
            edgecolor=PALETTE[i % len(PALETTE)],
            facecolor="white",
        )
        ax.add_patch(box)
        ax.text(x + 0.8, 1.6, label, ha="center", va="center", fontsize=9)

    for i in range(len(boxes) - 1):
        x0 = boxes[i][0] + 1.6
        x1 = boxes[i + 1][0]
        arrow = FancyArrowPatch(
            (x0, 1.6), (x1, 1.6),
            arrowstyle="->",
            mutation_scale=14,
            linewidth=1.2,
            color="#333333",
        )
        ax.add_patch(arrow)

    ax.text(5.0, 2.7, "ENACT pipeline", ha="center", va="center", fontsize=12, weight="bold")
    ax.text(5.0, 0.5,
            "Output: cell-by-gene matrix + per-cell types + spatial coordinates",
            ha="center", va="center", fontsize=9, style="italic")
    save(fig, "fig1_pipeline")


def fig2_overlap():
    """Bar chart: percent of bins overlapping more than one cell, by synthetic dataset.

    Values from experimental_log / statistical_sentences:
    - Xenium synthetic: 25%
    - seqFISH+ synthetic: 5% (sentence says 'only about 5%')
    """
    datasets = ["Xenium-based\nsynthetic", "seqFISH+-based\nsynthetic"]
    overlap_pct = [25, 5]

    fig, ax = plt.subplots(figsize=(4.5, 3.2))
    bars = ax.bar(datasets, overlap_pct, color=[PALETTE[0], PALETTE[2]], width=0.6)
    ax.set_ylabel("Bins overlapping > 1 cell (%)")
    ax.set_ylim(0, 32)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bar, pct in zip(bars, overlap_pct):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
                f"{pct}%", ha="center", va="bottom", fontsize=10, weight="bold")
    ax.set_title("Bin-cell overlap in synthetic datasets")
    plt.tight_layout()
    save(fig, "fig2_overlap")


def fig3_bestperf():
    """Bar chart: accuracy and weighted F1 for Sargent + Weighted-by-Area.

    Values from experimental_log:
    - accuracy = 0.708
    - weighted F1 = 0.758
    - n = 20,991 pathologist-annotated cells
    """
    metrics = ["Accuracy", "Weighted F1"]
    values = [0.708, 0.758]

    fig, ax = plt.subplots(figsize=(4.0, 3.2))
    bars = ax.bar(metrics, values, color=[PALETTE[1], PALETTE[3]], width=0.55)
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Score")
    ax.set_title("Sargent + Weighted-by-Area\n(20,991 pathologist-annotated cells)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                f"{v:.3f}", ha="center", va="bottom", fontsize=10, weight="bold")
    plt.tight_layout()
    save(fig, "fig3_bestperf")


if __name__ == "__main__":
    fig1_pipeline()
    fig2_overlap()
    fig3_bestperf()
    print("Generated figures: fig1_pipeline, fig2_overlap, fig3_bestperf")
