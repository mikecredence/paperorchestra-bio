"""Generate figures for the BELA paper using only values from the experimental log."""
import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Consistent academic styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "figure.dpi": 150,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

OUTDIR = os.path.dirname(os.path.abspath(__file__))


def save(fig, name):
    fig.savefig(os.path.join(OUTDIR, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUTDIR, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1: BELA pipeline schematic
# ---------------------------------------------------------------------------
def fig_pipeline():
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.2)
    ax.axis("off")

    boxes = [
        (0.1, 1.1, "Day-5 time-lapse\n(96-112 hpi)"),
        (2.1, 1.1, "VGG16\n(512-d features)"),
        (4.1, 1.1, "Multitask BiLSTM\nBS/ICM/TE/Exp"),
        (6.3, 1.1, "Model-derived\nBS (MDBS)"),
        (8.3, 1.1, "Logistic reg.\n+ maternal age"),
    ]
    width, height = 1.75, 1.1
    for (x, y, txt) in boxes:
        box = FancyBboxPatch(
            (x, y), width, height,
            boxstyle="round,pad=0.04",
            linewidth=1.1, edgecolor="#333333", facecolor="#e8eef7",
        )
        ax.add_patch(box)
        ax.text(x + width / 2, y + height / 2, txt,
                ha="center", va="center", fontsize=9)

    # arrows between boxes
    for i in range(len(boxes) - 1):
        x_start = boxes[i][0] + width
        x_end = boxes[i + 1][0]
        arrow = FancyArrowPatch(
            (x_start, boxes[i][1] + height / 2),
            (x_end, boxes[i + 1][1] + height / 2),
            arrowstyle="->", mutation_scale=14, color="#555555",
        )
        ax.add_patch(arrow)

    ax.text(5.0, 2.8, "BELA: two-step automated ploidy prediction pipeline",
            ha="center", va="center", fontsize=10.5, weight="bold")
    ax.text(5.0, 0.3,
            "Output: P(EUP), P(ANU or CxA), intermediate quality scores",
            ha="center", va="center", fontsize=9, style="italic")

    save(fig, "fig_pipeline")


# ---------------------------------------------------------------------------
# Figure 2: AUC on WCM-Embryoscope test set (with / without maternal age)
# ---------------------------------------------------------------------------
def fig_auc_wcm():
    # Values from experimental_log.md:
    # EUP vs ANU: 0.66 +/- 0.008 without age; 0.76 +/- 0.002 with age
    # EUP vs CxA: 0.708 +/- 0.004 without age; 0.826 +/- 0.004 with age
    tasks = ["EUP vs ANU", "EUP vs CxA"]
    auc_no_age = [0.66, 0.708]
    err_no_age = [0.008, 0.004]
    auc_age = [0.76, 0.826]
    err_age = [0.002, 0.004]

    x = np.arange(len(tasks))
    width = 0.35

    fig, ax = plt.subplots(figsize=(5.0, 3.4))
    bars1 = ax.bar(x - width / 2, auc_no_age, width, yerr=err_no_age,
                   capsize=4, label="BELA (no age)", color=PALETTE[0])
    bars2 = ax.bar(x + width / 2, auc_age, width, yerr=err_age,
                   capsize=4, label="BELA + maternal age", color=PALETTE[1])

    for bars, values in [(bars1, auc_no_age), (bars2, auc_age)]:
        for b, v in zip(bars, values):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.015,
                    f"{v:.3f}", ha="center", va="bottom", fontsize=9)

    ax.set_ylabel("AUC on WCM-Embryoscope test set")
    ax.set_xticks(x)
    ax.set_xticklabels(tasks)
    ax.set_ylim(0.5, 0.95)
    ax.legend(loc="upper left", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    plt.tight_layout()
    save(fig, "fig_auc_wcm")


# ---------------------------------------------------------------------------
# Figure 3: Dataset sizes and ploidy class distributions
# ---------------------------------------------------------------------------
def fig_datasets():
    # From Materials & Methods in the experimental log.
    datasets = ["WCM-\nEmbryoscope", "WCM-\nEmbryoscope+", "Spain\n(IVI Valencia)", "Florida\n(IVF Florida)"]
    eup = [916, 410, 234, 445]
    sa  = [494, 170, 0, 202]       # Spain has no SA/CxA split
    cxa = [588, 261, 0, 222]
    anu_only = [0, 0, 309, 0]      # Spain reports ANU in aggregate

    x = np.arange(len(datasets))
    width = 0.18

    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.bar(x - 1.5 * width, eup, width, label="EUP", color=PALETTE[2])
    ax.bar(x - 0.5 * width, sa, width, label="SA", color=PALETTE[0])
    ax.bar(x + 0.5 * width, cxa, width, label="CxA", color=PALETTE[3])
    ax.bar(x + 1.5 * width, anu_only, width, label="ANU (aggregate)", color=PALETTE[4])

    totals = [a + b + c + d for a, b, c, d in zip(eup, sa, cxa, anu_only)]
    for i, t in enumerate(totals):
        ax.text(i, max(eup[i], sa[i], cxa[i], anu_only[i]) + 30,
                f"n={t}", ha="center", va="bottom", fontsize=9, weight="bold")

    ax.set_ylabel("Number of embryos")
    ax.set_xticks(x)
    ax.set_xticklabels(datasets, fontsize=9)
    ax.legend(loc="upper right", frameon=False, ncol=2)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 1100)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    plt.tight_layout()
    save(fig, "fig_datasets")


# ---------------------------------------------------------------------------
# Figure 4: Multitask vs non-multitask MAE and Florida MAE comparison
# ---------------------------------------------------------------------------
def fig_mae_comparisons():
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2))

    # Left: multitask vs non-multitask on WCM-Embryoscope
    # Non-multitask MAE = 1.877 +/- 0.027; Multitask MAE = 1.855 +/- 0.03
    labels_l = ["Non-multitask\nBELA", "Multitask\nBELA"]
    mae_vals = [1.877, 1.855]
    mae_err = [0.027, 0.03]
    bars = axes[0].bar(labels_l, mae_vals, yerr=mae_err, capsize=5,
                       color=[PALETTE[0], PALETTE[1]])
    for b, v in zip(bars, mae_vals):
        axes[0].text(b.get_x() + b.get_width() / 2, v + 0.008,
                     f"{v:.3f}", ha="center", va="bottom", fontsize=9)
    axes[0].set_ylabel("MAE of predicted BS vs ground truth")
    axes[0].set_title("WCM-Embryoscope test")
    axes[0].set_ylim(1.75, 1.95)
    axes[0].spines["top"].set_visible(False)
    axes[0].spines["right"].set_visible(False)
    axes[0].grid(axis="y", linestyle=":", alpha=0.4)

    # Right: Florida re-grading MAE comparison
    # MDBS vs WCM re-graded BS = 4.16; MDBS vs Florida BS = 5.02
    labels_r = ["MDBS vs\nWCM re-graded", "MDBS vs\nFlorida BS"]
    vals_r = [4.16, 5.02]
    bars = axes[1].bar(labels_r, vals_r, color=[PALETTE[2], PALETTE[3]])
    for b, v in zip(bars, vals_r):
        axes[1].text(b.get_x() + b.get_width() / 2, v + 0.08,
                     f"{v:.2f}", ha="center", va="bottom", fontsize=9)
    axes[1].set_ylabel("MAE")
    axes[1].set_title("Florida re-grading (n=50)")
    axes[1].set_ylim(0, 6.2)
    axes[1].spines["top"].set_visible(False)
    axes[1].spines["right"].set_visible(False)
    axes[1].grid(axis="y", linestyle=":", alpha=0.4)

    plt.tight_layout()
    save(fig, "fig_mae_comparisons")


# ---------------------------------------------------------------------------
# Figure 5: Feature-space PCA placeholder (structure described but raw values
# not available).
# ---------------------------------------------------------------------------
def fig_pca_placeholder():
    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    ax.text(
        0.5, 0.5,
        "[Figure placeholder]\nPCA of VGG16 feature encodings\nper embryo "
        "(WCM, Spain, Florida).\nRaw coordinates not in extraction.",
        ha="center", va="center", fontsize=9.5, color="#555555",
        bbox=dict(boxstyle="round,pad=0.7",
                  facecolor="#f3f3f3", edgecolor="#888888"),
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    plt.tight_layout()
    save(fig, "fig_pca_placeholder")


if __name__ == "__main__":
    fig_pipeline()
    fig_auc_wcm()
    fig_datasets()
    fig_mae_comparisons()
    fig_pca_placeholder()
    print("Generated figures in", OUTDIR)
