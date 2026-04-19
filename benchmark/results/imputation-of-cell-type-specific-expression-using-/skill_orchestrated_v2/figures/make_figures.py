"""Generate figures for the penalised-regression imputation paper.

Every numeric value in this script is taken verbatim from inputs/experimental_log.md.
No fabricated values are introduced.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 10,
        "axes.titlesize": 11,
        "legend.fontsize": 9,
        "savefig.bbox": "tight",
    }
)

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

OUT = Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / f"{name}.pdf")
    fig.savefig(OUT / f"{name}.png", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1: Schematic of the multi-response LASSO/ridge pipeline
# ---------------------------------------------------------------------------
def fig_schematic():
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    def box(x, y, w, h, text, color):
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.08",
            linewidth=1.2,
            edgecolor="black",
            facecolor=color,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9)

    def arrow(x0, y0, x1, y1):
        ax.add_patch(
            FancyArrowPatch(
                (x0, y0),
                (x1, y1),
                arrowstyle="->",
                mutation_scale=14,
                linewidth=1.0,
                color="black",
            )
        )

    box(0.2, 2.4, 2.0, 1.0, "PBMC\nRNA-seq\n(N=158)", "#deebf7")
    box(0.2, 0.6, 2.0, 1.0, "Sorted CD4/CD8\nCD14/CD19\n(80 training)", "#deebf7")

    box(3.0, 1.5, 2.2, 1.0, "Hierarchical\ngene chunking\n($<$ 500 genes)", "#fdd0a2")

    box(5.8, 1.5, 2.2, 1.0, "Multi-response\nglmnet\n($\\alpha=0$ or $1$)", "#c7e9c0")

    box(8.5, 1.5, 1.3, 1.0, "Imputed\ncell-type\nexpression", "#fbb4ae")

    arrow(2.2, 2.9, 3.0, 2.1)
    arrow(2.2, 1.1, 3.0, 1.9)
    arrow(5.2, 2.0, 5.8, 2.0)
    arrow(8.0, 2.0, 8.5, 2.0)

    ax.text(5.0, 3.6, "Training: paired bulk + sorted", ha="center", fontsize=10)
    save(fig, "fig_schematic")


# ---------------------------------------------------------------------------
# Figure 2: Attenuation of log2 fold changes (slope ranges from S7C)
# ---------------------------------------------------------------------------
def fig_slopes():
    methods = [
        "CIBX-inbuilt",
        "CIBX-custom",
        "bMIND",
        "swCAM",
        "LASSO",
        "ridge",
    ]
    # Ranges (min, max) from experimental log S7C sentence.
    ranges = [
        (0.60, 0.70),
        (0.64, 0.76),
        (0.66, 0.85),
        (0.55, 0.90),
        (0.69, 0.76),
        (0.68, 0.76),
    ]

    mins = [r[0] for r in ranges]
    maxs = [r[1] for r in ranges]
    mids = [(lo + hi) / 2 for lo, hi in ranges]
    err_lo = [m - lo for m, lo in zip(mids, mins)]
    err_hi = [hi - m for m, hi in zip(mids, maxs)]

    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    x = np.arange(len(methods))
    ax.errorbar(
        x,
        mids,
        yerr=[err_lo, err_hi],
        fmt="o",
        capsize=5,
        color=PALETTE[0],
        ecolor="black",
        markersize=7,
    )
    ax.axhline(1.0, linestyle="--", color="gray", linewidth=0.8, label="Unattenuated ($\\beta=1$)")
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=20, ha="right")
    ax.set_ylabel("Slope of imputed vs.\\ observed $\\log_{2}$FC")
    ax.set_ylim(0.4, 1.05)
    ax.set_title("Attenuation of differential-expression effect sizes")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="lower right", frameon=False)
    save(fig, "fig_slopes")


# ---------------------------------------------------------------------------
# Figure 3: Common gene counts by cell type (S3 Fig)
# ---------------------------------------------------------------------------
def fig_common_genes():
    cell_types = ["CD4", "CD8", "CD14", "CD19"]
    counts = [3837, 6274, 5185, 2689]

    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    bars = ax.bar(cell_types, counts, color=PALETTE[:4], edgecolor="black", linewidth=0.6)
    for b, c in zip(bars, counts):
        ax.text(b.get_x() + b.get_width() / 2, c + 100, f"{c:,}", ha="center", fontsize=9)
    ax.set_ylabel("Genes predicted by all methods")
    ax.set_title("Common gene sets across approaches")
    ax.set_ylim(0, max(counts) + 1000)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig_common_genes")


# ---------------------------------------------------------------------------
# Figure 4: Computational cost vs. CIBERSORTx (S2/S3 Table + Discussion)
# ---------------------------------------------------------------------------
def fig_compute():
    methods = ["CIBX", "bMIND", "swCAM", "LASSO", "ridge"]
    # CPU relative to CIBERSORTx = 1.0; from experimental log Discussion.
    cpu = [1.0, 2.7, 385.0, 192.3, 658.1]
    # Memory relative to CIBERSORTx; bMIND 33%, swCAM 54%, LASSO up to 3x, ridge up to 11x.
    mem = [1.0, 0.33, 0.54, 3.0, 11.0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.4, 3.2))
    bars1 = ax1.bar(methods, cpu, color=PALETTE[: len(methods)], edgecolor="black", linewidth=0.5)
    ax1.set_yscale("log")
    ax1.set_ylabel("CPU time (\\texttimes\\ CIBERSORTx)")
    ax1.set_title("CPU cost")
    for b, v in zip(bars1, cpu):
        ax1.text(b.get_x() + b.get_width() / 2, v * 1.2, f"{v:g}", ha="center", fontsize=8)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    bars2 = ax2.bar(methods, mem, color=PALETTE[: len(methods)], edgecolor="black", linewidth=0.5)
    ax2.set_ylabel("Memory (\\texttimes\\ CIBERSORTx)")
    ax2.set_title("Peak memory")
    ax2.axhline(1.0, linestyle="--", color="gray", linewidth=0.7)
    for b, v in zip(bars2, mem):
        ax2.text(b.get_x() + b.get_width() / 2, v + 0.2, f"{v}", ha="center", fontsize=8)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    save(fig, "fig_compute")


# ---------------------------------------------------------------------------
# Figure 5: eQTLgen pseudobulk cell-type fractions used for simulation
# ---------------------------------------------------------------------------
def fig_eqtlgen_fractions():
    cells = ["CD4", "CD8", "CD14", "CD19"]
    means = [42.74, 28.12, 26.29, 2.85]
    sds = [4.30, 2.40, 6.21, 0.36]

    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    x = np.arange(len(cells))
    ax.bar(x, means, yerr=sds, capsize=5, color=PALETTE[:4], edgecolor="black", linewidth=0.6)
    for xi, m, s in zip(x, means, sds):
        ax.text(xi, m + s + 1.5, f"{m:.2f}\\%", ha="center", fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels(cells)
    ax.set_ylabel("Cell-type fraction (\\%)")
    ax.set_title("eQTLgen pseudobulk composition")
    ax.set_ylim(0, 55)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig_eqtlgen_fractions")


def main():
    plt.rcParams["text.usetex"] = False  # keep rendering local-portable
    fig_schematic()
    fig_slopes()
    fig_common_genes()
    fig_compute()
    fig_eqtlgen_fractions()
    print("Wrote 5 figures to", OUT)


if __name__ == "__main__":
    main()
