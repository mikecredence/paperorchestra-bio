"""Generate figures for TEMPy-REFF paper.

All numeric values are copied verbatim from the experimental log
(inputs/experimental_log.md). Nothing in this script fabricates data."""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))


def savefig(fig, name: str) -> None:
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), bbox_inches="tight", dpi=220)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1: CERES benchmark delta CCC summary
# Values from experimental log Results/Benchmarking structure refinement:
#   - Average improvement vs deposited EMDB models: 0.197 (p=0.0006)
#   - Average improvement vs CERES re-refined models: 0.150 (p=0.003)
#   - 366 complexes
# ---------------------------------------------------------------------------
def fig_ccc_delta():
    labels = ["vs deposited\n(EMDB)", "vs CERES\nre-refinement"]
    deltas = [0.197, 0.150]
    pvals = [0.0006, 0.003]

    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    colours = ["#1f77b4", "#2ca02c"]
    bars = ax.bar(labels, deltas, color=colours, edgecolor="black", width=0.55)
    for bar, delta, p in zip(bars, deltas, pvals):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.004,
                f"$\\Delta$CCC = {delta:.3f}\n$p$ = {p}",
                ha="center", va="bottom", fontsize=9)
    ax.set_ylabel("Mean improvement in CCC (ensemble)")
    ax.set_title("TEMPy-REFF ensemble CCC gains across 366 CERES+ complexes")
    ax.set_ylim(0, max(deltas) * 1.45)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    savefig(fig, "fig_ccc_delta")


# ---------------------------------------------------------------------------
# Figure 2: RNA polymerase III case study fit quality
# Values from experimental log Case study I:
#   CCC deposited = 0.82
#   CCC prepared (H added) = 0.82
#   CCC TEMPy-REFF single = 0.83
#   CCC TEMPy-REFF ensemble = 0.94
# ---------------------------------------------------------------------------
def fig_rnapol_iii_ccc():
    labels = ["Deposited", "Prepared\n(+H)", "TEMPy-REFF\nsingle", "TEMPy-REFF\nensemble"]
    cccs = [0.82, 0.82, 0.83, 0.94]
    colours = ["#6baed6", "#9ecae1", "#fd8d3c", "#e6550d"]

    fig, ax = plt.subplots(figsize=(5.6, 3.8))
    bars = ax.bar(labels, cccs, color=colours, edgecolor="black", width=0.6)
    for bar, value in zip(bars, cccs):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.005,
                f"{value:.2f}", ha="center", va="bottom", fontsize=10)
    ax.set_ylim(0.7, 1.0)
    ax.set_ylabel("Model-to-map CCC")
    ax.set_title("Yeast RNA polymerase III (PDB 5FJ8, EMD-3178, 3.9\u00c5)")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    savefig(fig, "fig_rnapol_iii_ccc")


# ---------------------------------------------------------------------------
# Figure 3: Per-chain LoQFit (A) before vs after refinement
# Values from experimental log Case study I:
#   Before: chain A=5.4, chain B=5.6, chain M=7.4, chain N=7.0, chain O=7.3
#   After : chain M=6.0, chain N=5.7, chain O=5.9 (A, B not reported post)
#   Global average LoQFit: before 10.1 -> after 9.0 (reported)
# ---------------------------------------------------------------------------
def fig_loqfit_chains():
    chains = ["A", "B", "M", "N", "O"]
    before = [5.4, 5.6, 7.4, 7.0, 7.3]
    # For A and B, after-values are not reported; show only the before bars for those.
    after = [np.nan, np.nan, 6.0, 5.7, 5.9]

    x = np.arange(len(chains))
    width = 0.35
    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    ax.bar(x - width / 2, before, width, label="Deposited", color="#1f77b4", edgecolor="black")
    after_masked = [v if not np.isnan(v) else 0 for v in after]
    after_missing = [np.isnan(v) for v in after]
    ax.bar(x + width / 2, after_masked, width, label="TEMPy-REFF", color="#ff7f0e", edgecolor="black")

    for i, missing in enumerate(after_missing):
        if missing:
            ax.text(x[i] + width / 2, 0.1, "n/r", ha="center", va="bottom", fontsize=9, color="grey")

    for i, (b, a) in enumerate(zip(before, after)):
        ax.text(x[i] - width / 2, b + 0.1, f"{b:.1f}", ha="center", va="bottom", fontsize=9)
        if not np.isnan(a):
            ax.text(x[i] + width / 2, a + 0.1, f"{a:.1f}", ha="center", va="bottom", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(chains)
    ax.set_ylabel("Average LoQFit (\u00c5)")
    ax.set_xlabel("Chain")
    ax.set_title("LoQFit per chain, RNA pol III before vs after TEMPy-REFF")
    ax.set_ylim(0, 9)
    ax.legend(loc="upper left")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    savefig(fig, "fig_loqfit_chains")


# ---------------------------------------------------------------------------
# Figure 4: TEMPy-REFF schematic (pipeline diagram)
# No numeric data plotted; schematic description of Fig. 1 from the paper.
# ---------------------------------------------------------------------------
def fig_pipeline_schematic():
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    def box(x, y, w, h, label, face):
        patch = FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.05,rounding_size=0.1",
                                linewidth=1.2,
                                facecolor=face, edgecolor="black")
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=10)

    box(0.2, 2.1, 2.0, 1.0, "Cryo-EM map\n+ atomic model", "#deebf7")
    box(2.6, 2.1, 2.0, 1.0, "Per-atom Gaussian\nmixture (EM)", "#c6dbef")
    box(5.0, 2.1, 2.0, 1.0, "Update x, B,\nbackground k_bg", "#9ecae1")
    box(7.4, 2.1, 2.4, 1.0, "Ensemble + LoQFit\nsegmentation / composite", "#fdd0a2")

    def arrow(x1, y1, x2, y2):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                                      arrowstyle="-|>", mutation_scale=14,
                                      color="black", linewidth=1.2))

    arrow(2.2, 2.6, 2.6, 2.6)
    arrow(4.6, 2.6, 5.0, 2.6)
    arrow(7.0, 2.6, 7.4, 2.6)

    # Loop back arrow for EM iterations
    ax.annotate("", xy=(2.9, 1.9), xytext=(6.5, 1.9),
                arrowprops=dict(arrowstyle="->", linewidth=1.1,
                                connectionstyle="arc3,rad=0.4", color="grey"))
    ax.text(4.8, 1.0, "EM iterations (responsibility-weighted updates)",
            ha="center", fontsize=9, color="grey")

    ax.text(5.0, 4.4, "TEMPy-REFF refinement pipeline",
            ha="center", fontsize=12, weight="bold")
    savefig(fig, "fig_pipeline_schematic")


def main():
    fig_ccc_delta()
    fig_rnapol_iii_ccc()
    fig_loqfit_chains()
    fig_pipeline_schematic()
    print("All figures written to", OUT)


if __name__ == "__main__":
    main()
