"""Generate figures for RNAseqCovarImpute paper.

All plotted numerical values are taken verbatim from inputs/idea_summary.md
statistical_sentences (the experimental log). No fabricated data.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

FIG_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# Figure 1: Schematic of RNAseqCovarImpute workflow
# ---------------------------------------------------------------------------
def fig1_schematic():
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    boxes = [
        (0.3, 4.8, 2.6, 1.4, "A. Count matrix\n(e.g. 10,000 genes\nx 500 samples)", "#d1e7ff"),
        (3.3, 4.8, 2.6, 1.4, "B. Bin genes\n(default ~1 gene\nper 10 samples)", "#cfe9cc"),
        (6.3, 4.8, 2.6, 1.4, "C. MI within each bin\n(mice; outcome genes\nin predictor matrix)", "#ffe9c7"),
        (9.3, 4.8, 2.6, 1.4, "D. voom + lmFit\nper bin per imp.", "#f5cfe0"),
        (0.3, 1.2, 2.6, 1.4, "E. Un-bin and stack\nM tables of gene\nresults", "#e6d7f2"),
        (3.3, 1.2, 2.6, 1.4, "F. squeezeVar\n(empirical Bayes)\nper imputation", "#d5f0f2"),
        (6.3, 1.2, 2.6, 1.4, "G. Pool with\nRubin's rules\n(coef, SE, df)", "#ffd6d6"),
        (9.3, 1.2, 2.6, 1.4, "H. FDR-adjusted\nDEG table", "#e0e0e0"),
    ]
    for x, y, w, h, text, color in boxes:
        ax.add_patch(mpatches.FancyBboxPatch((x, y), w, h,
                                             boxstyle="round,pad=0.04,rounding_size=0.12",
                                             linewidth=1.0, facecolor=color, edgecolor="black"))
        ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=9)

    # Arrows
    arrow_pairs = [
        (2.9, 5.5, 3.3, 5.5),
        (5.9, 5.5, 6.3, 5.5),
        (8.9, 5.5, 9.3, 5.5),
        (10.6, 4.8, 1.6, 2.6),  # wrap-around to E
        (2.9, 1.9, 3.3, 1.9),
        (5.9, 1.9, 6.3, 1.9),
        (8.9, 1.9, 9.3, 1.9),
    ]
    for x1, y1, x2, y2 in arrow_pairs:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.2,
                                     connectionstyle="arc3,rad=0.0" if not (x1 > x2) else "arc3,rad=-0.2"))

    ax.set_title("RNAseqCovarImpute workflow for multiple imputation in limma-voom analyses",
                 fontsize=11)
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG_DIR, f"fig1.{ext}"), bbox_inches="tight", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Helper for paired bar plots showing range (min, max)
# ---------------------------------------------------------------------------
def range_bar(ax, methods, ranges, colors, title, ylabel, ymax=100):
    n = len(methods)
    x = np.arange(n)
    mids = [(lo + hi) / 2 for (lo, hi) in ranges]
    errs_lo = [mids[i] - ranges[i][0] for i in range(n)]
    errs_hi = [ranges[i][1] - mids[i] for i in range(n)]
    ax.bar(x, mids, yerr=[errs_lo, errs_hi], capsize=6, color=colors,
           edgecolor="black")
    for i, (lo, hi) in enumerate(ranges):
        ax.text(x[i], hi + 1.5, f"{lo:.1f}-{hi:.1f}%", ha="center", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_ylim(0, ymax)
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontsize=10)


# ---------------------------------------------------------------------------
# Figure 2: Simulation 1 true DEG recovery and FDR, MCAR + MAR
# Values from experimental log:
#   MCAR true DEGs: MI 95.6-98.5, SI 56.6-90.7 (CC not specified numerically; leave CC range as implied)
#   MCAR FDR: MI 2.9-13.8, SI 1.9-14.8, CC 5.3-12.8
#   MAR true DEGs: MI 90.3-97.4, SI 55.7-77.6 (CC implicit in figure)
#   MAR FDR: MI 2.0-8.0, SI 1.4-12.2, CC 11.4-18.5
# CC true DEG numbers are not given in the extracted log so we omit CC bars for true-DEG.
# ---------------------------------------------------------------------------
def fig2_sim1():
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.2))

    # MCAR true DEG
    range_bar(
        axes[0, 0],
        ["RNAseqCovarImpute", "SI"],
        [(95.6, 98.5), (56.6, 90.7)],
        ["#2c7fb8", "#7fcdbb"],
        "Sim 1 MCAR: percent of 2,453 true DEGs",
        "True DEGs recovered (%)",
    )

    # MCAR FDR
    range_bar(
        axes[0, 1],
        ["RNAseqCovarImpute", "SI", "CC"],
        [(2.9, 13.8), (1.9, 14.8), (5.3, 12.8)],
        ["#2c7fb8", "#7fcdbb", "#d95f0e"],
        "Sim 1 MCAR: FDR",
        "FDR (%)",
        ymax=25,
    )

    # MAR true DEG
    range_bar(
        axes[1, 0],
        ["RNAseqCovarImpute", "SI"],
        [(90.3, 97.4), (55.7, 77.6)],
        ["#2c7fb8", "#7fcdbb"],
        "Sim 1 MAR: percent of 2,453 true DEGs",
        "True DEGs recovered (%)",
    )

    # MAR FDR
    range_bar(
        axes[1, 1],
        ["RNAseqCovarImpute", "SI", "CC"],
        [(2.0, 8.0), (1.4, 12.2), (11.4, 18.5)],
        ["#2c7fb8", "#7fcdbb", "#d95f0e"],
        "Sim 1 MAR: FDR",
        "FDR (%)",
        ymax=25,
    )

    fig.suptitle("Simulation 1: real covariates and real RNA-seq counts (N=1,044)",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG_DIR, f"fig2.{ext}"), bbox_inches="tight", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 3: Simulation 2 true DEG recovery and FDR at 82.5% null-gene rate
# Values from experimental log:
#   MCAR true DEGs: MI 96.8-99.1, SI 78.9-95.9, CC 58.2-92.9
#   MCAR FDR: MI 1.4-6.1, SI 1.4-7.6, CC 3.0-8.0
#   MAR true DEGs: MI 94.0-98.2, SI 77.6-89.6, CC 61.1-93.2
#   MAR FDR: MI 0.9-3.9, SI 1.2-7.7, CC 6.0-10.9
# ---------------------------------------------------------------------------
def fig3_sim2():
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.2))
    methods = ["RNAseqCovarImpute", "SI", "CC"]
    colors = ["#2c7fb8", "#7fcdbb", "#d95f0e"]

    range_bar(axes[0, 0], methods,
              [(96.8, 99.1), (78.9, 95.9), (58.2, 92.9)], colors,
              "Sim 2 MCAR: true DEGs", "True DEGs recovered (%)")
    range_bar(axes[0, 1], methods,
              [(1.4, 6.1), (1.4, 7.6), (3.0, 8.0)], colors,
              "Sim 2 MCAR: FDR", "FDR (%)", ymax=15)
    range_bar(axes[1, 0], methods,
              [(94.0, 98.2), (77.6, 89.6), (61.1, 93.2)], colors,
              "Sim 2 MAR: true DEGs", "True DEGs recovered (%)")
    range_bar(axes[1, 1], methods,
              [(0.9, 3.9), (1.2, 7.7), (6.0, 10.9)], colors,
              "Sim 2 MAR: FDR", "FDR (%)", ymax=15)

    fig.suptitle("Simulation 2: real covariates, synthetic counts at 82.5% null rate (N=1,044)",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG_DIR, f"fig3.{ext}"), bbox_inches="tight", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 4: placental-transcriptome DEGs across methods
# Values: CC 575, SI 214, MI 382. CC captured 368 (96%) of MI DEGs; SI captured 214 (56%) of MI; 30 MI-exclusive.
# ---------------------------------------------------------------------------
def fig4_application():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

    methods = ["CC", "SI", "MI (RNAseqCovarImpute)"]
    counts = [575, 214, 382]
    colors = ["#d95f0e", "#7fcdbb", "#2c7fb8"]
    axes[0].bar(methods, counts, color=colors, edgecolor="black")
    for i, v in enumerate(counts):
        axes[0].text(i, v + 8, str(v), ha="center")
    axes[0].set_ylabel("Significant maternal-age DEGs")
    axes[0].set_title("DEG counts across methods\n(N=1,045, FDR<0.05)")
    axes[0].set_ylim(0, max(counts) + 60)

    mi_total = 382
    overlap_cc = 368  # 96% of MI
    overlap_si = 214  # 56% of MI
    mi_exclusive = 30
    labels = ["Shared with CC", "Shared with SI", "MI exclusive"]
    values = [overlap_cc, overlap_si, mi_exclusive]
    axes[1].bar(labels, values, color=["#d95f0e", "#7fcdbb", "#2c7fb8"], edgecolor="black")
    for i, v in enumerate(values):
        axes[1].text(i, v + 5, str(v), ha="center")
    axes[1].set_ylabel("DEGs")
    axes[1].set_title("MI-identified DEG breakdown\n(MI identified 382 total)")
    axes[1].set_ylim(0, max(values) + 60)

    fig.suptitle("Application: maternal age and placental transcriptome", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG_DIR, f"fig4.{ext}"), bbox_inches="tight", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig1_schematic()
    fig2_sim1()
    fig3_sim2()
    fig4_application()
    print("Generated fig1-fig4 in", FIG_DIR)
