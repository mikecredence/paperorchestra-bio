"""Generate figures for the brain-bone SNS atlas paper.

All numeric values come verbatim from experimental_log.md:
  hypothalamus:       1177.25 +/- 62.75
  midbrain and pons:  1065    +/- 22.39
  hindbrain medulla:  495.25  +/- 33.49
  forebrain:          237.5   +/- 15.08
  cerebral cortex:    104.75  +/- 4.64
  thalamus:           65.25   +/- 7.78

Number of PRV152-positive nuclei/regions per division:
  hypothalamus: 25; midbrain and pons: 18; medulla: 23;
  forebrain: 15; cerebral cortex: 3; thalamus: 3.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

FIG_DIR = Path(__file__).parent
FIG_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]


def fig_counts():
    divisions = [
        "Hypothalamus",
        "Midbrain\n& pons",
        "Hindbrain\nmedulla",
        "Forebrain",
        "Cerebral\ncortex",
        "Thalamus",
    ]
    means = [1177.25, 1065.0, 495.25, 237.5, 104.75, 65.25]
    sems = [62.75, 22.39, 33.49, 15.08, 4.64, 7.78]

    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    x = np.arange(len(divisions))
    bars = ax.bar(x, means, yerr=sems, capsize=4, color=PALETTE, edgecolor="black", linewidth=0.6)
    ax.set_ylabel("PRV152-labeled neurons (mean $\\pm$ SEM)")
    ax.set_xticks(x)
    ax.set_xticklabels(divisions)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bar, m, s in zip(bars, means, sems):
        ax.text(bar.get_x() + bar.get_width() / 2, m + s + 30,
                f"{m:g}", ha="center", va="bottom", fontsize=8)
    ax.set_ylim(0, max(means) * 1.18)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig_counts.pdf")
    plt.savefig(FIG_DIR / "fig_counts.png", dpi=220)
    plt.close()


def fig_subnuclei():
    divisions = [
        "Hypothalamus", "Midbrain\n& pons", "Medulla",
        "Forebrain", "Cerebral\ncortex", "Thalamus",
    ]
    counts = [25, 18, 23, 15, 3, 3]

    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    x = np.arange(len(divisions))
    bars = ax.bar(x, counts, color=PALETTE, edgecolor="black", linewidth=0.6)
    ax.set_ylabel("Number of PRV152-positive\nnuclei / sub-nuclei / regions")
    ax.set_xticks(x)
    ax.set_xticklabels(divisions)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bar, c in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, c + 0.4,
                str(c), ha="center", va="bottom", fontsize=9)
    ax.set_ylim(0, max(counts) + 4)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig_subnuclei.pdf")
    plt.savefig(FIG_DIR / "fig_subnuclei.png", dpi=220)
    plt.close()


def _box(ax, xy, w, h, label, face="#e7f0fa", edge="#1f77b4"):
    fb = FancyBboxPatch(xy, w, h,
                        boxstyle="round,pad=0.02,rounding_size=0.05",
                        facecolor=face, edgecolor=edge, linewidth=1.2)
    ax.add_patch(fb)
    cx = xy[0] + w / 2.0
    cy = xy[1] + h / 2.0
    ax.text(cx, cy, label, ha="center", va="center", fontsize=9)


def _arrow(ax, p1, p2, color="#444444"):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=12,
                        color=color, linewidth=1.0, shrinkA=2, shrinkB=2)
    ax.add_patch(a)


def fig_circuit():
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    _box(ax, (0.2, 4.6), 1.8, 0.8, "PVH\n(hypothalamus)", face="#fff1e0", edge="#ff7f0e")
    _box(ax, (0.2, 3.2), 1.8, 0.8, "LH / DM\n(hypothalamus)", face="#fff1e0", edge="#ff7f0e")
    _box(ax, (2.8, 4.0), 1.8, 0.8, "PAG / LPAG\n(midbrain)", face="#e7f0fa", edge="#1f77b4")
    _box(ax, (5.2, 4.0), 1.8, 0.8, "RMg / RPa\n(medulla)", face="#eaf7e8", edge="#2ca02c")
    _box(ax, (7.8, 4.0), 1.9, 0.8, "IML\n(T13--L2)", face="#f5e0e0", edge="#d62728")
    _box(ax, (7.8, 2.2), 1.9, 0.8, "Paravertebral\nganglia", face="#f5e0e0", edge="#d62728")
    _box(ax, (5.0, 0.8), 2.4, 0.9, "Femur\n(periosteum, metaphysis)", face="#ece3f4", edge="#9467bd")
    _box(ax, (2.3, 2.4), 2.2, 0.8, "Dorsal horn\n(enkephalin / SP)", face="#fff6df", edge="#b58900")

    _arrow(ax, (2.0, 5.0), (2.8, 4.6))
    _arrow(ax, (2.0, 3.6), (2.8, 4.2))
    _arrow(ax, (4.6, 4.4), (5.2, 4.4))
    _arrow(ax, (5.2, 4.2), (4.6, 4.0), color="#888888")
    _arrow(ax, (7.0, 4.4), (7.8, 4.4))
    _arrow(ax, (8.7, 4.0), (8.7, 3.05))
    _arrow(ax, (8.5, 2.2), (7.0, 1.3))
    _arrow(ax, (4.5, 2.8), (3.5, 3.2))
    _arrow(ax, (6.0, 1.3), (4.5, 2.4), color="#888888")

    ax.text(5, 5.7, "Brain--bone SNS neuroaxis (retrograde PRV152 tracing)",
            ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(8.8, 3.55, "preganglionic",
            ha="center", va="center", fontsize=8, color="#555555", rotation=90)
    ax.text(5.2, 1.9, "postganglionic SNS\nto bone",
            ha="center", va="center", fontsize=8, color="#555555")

    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig_circuit.pdf")
    plt.savefig(FIG_DIR / "fig_circuit.png", dpi=220)
    plt.close()


def fig_validation_placeholder():
    """Placeholder micrograph panel for validation figure (raw images unavailable)."""
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.8))
    for ax, title in zip(axs, ["PRV152 on bone surface\n(no EGFP in PVH, RPa)",
                               "PRV152 into metaphysis\n(EGFP in PVH; IML T13--L2)"]):
        ax.text(0.5, 0.5, "[Representative micrograph\nplaceholder]",
                ha="center", va="center", fontsize=9, color="gray",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#f0f0f0", edgecolor="gray"))
        ax.set_title(title, fontsize=9)
        ax.set_xticks([]); ax.set_yticks([])
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig_validation.pdf")
    plt.savefig(FIG_DIR / "fig_validation.png", dpi=220)
    plt.close()


if __name__ == "__main__":
    fig_counts()
    fig_subnuclei()
    fig_circuit()
    fig_validation_placeholder()
    print("Wrote 4 figures to", FIG_DIR)
