"""Generate Draphnet paper figures.

All numerical values are taken verbatim from the experimental log.
No values are fabricated.
"""
import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "pdf.fonttype": 42,
})

OUT = os.path.dirname(os.path.abspath(__file__))

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


# ----------------------------------------------------------------------
# Figure 1: schematic of Draphnet
# ----------------------------------------------------------------------
def fig_schematic():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    boxes = [
        ("ToxCast endpoints\n$D$: 429 x 1391", 0.4, 3.2, PALETTE[3]),
        ("SoftImpute\n$U_D S_D$", 3.2, 3.2, PALETTE[4]),
        ("Interaction\n$W_{DP}$", 5.6, 3.2, PALETTE[1]),
        ("PhenomeXcan\n$P$: 10,027 x 197", 8.0, 3.2, PALETTE[2]),
        ("SIDER\n$Y$: drug x phenotype", 5.6, 0.4, PALETTE[0]),
    ]
    for text, x, y, color in boxes:
        patch = FancyBboxPatch(
            (x, y), 1.9, 1.3,
            boxstyle="round,pad=0.05",
            linewidth=1.2, edgecolor="black",
            facecolor=color, alpha=0.25,
        )
        ax.add_patch(patch)
        ax.text(x + 0.95, y + 0.65, text, ha="center", va="center", fontsize=9)

    arrows = [
        ((2.3, 3.85), (3.2, 3.85)),
        ((5.1, 3.85), (5.6, 3.85)),
        ((7.5, 3.85), (8.0, 3.85)),
        ((6.55, 3.2), (6.55, 1.7)),
    ]
    for (x1, y1), (x2, y2) in arrows:
        arr = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                              mutation_scale=14, color="black", linewidth=1.2)
        ax.add_patch(arr)

    ax.text(5, 4.9, "Draphnet: $DWP^{\\top} = \\mathrm{logit}(p(Y))$",
            ha="center", fontsize=11, fontweight="bold")
    ax.text(6.55, 0.1, "trains model to predict binary drug-phenotype $Y$",
            ha="center", fontsize=8, color="gray")

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "fig_schematic.pdf"))
    plt.savefig(os.path.join(OUT, "fig_schematic.png"), dpi=200)
    plt.close()


# ----------------------------------------------------------------------
# Figure 2: prediction performance p-value
# ----------------------------------------------------------------------
def fig_prediction():
    # Data-grounded: only the p-value is in the extraction.
    # Visualize as a log-scale significance bar: -log10(p) for Draphnet
    # vs nearest neighbor (reference line at alpha=0.05 threshold).
    # The extraction gives p=3e-8 for the rank-sum test of Draphnet < NN
    # in Jaccard distance on held-out drugs (Fig 2A).
    labels = ["Draphnet vs nearest\nneighbor (rank-sum)"]
    neg_log_p = [-np.log10(3e-8)]  # 7.52

    fig, ax = plt.subplots(figsize=(4.4, 3.2))
    bars = ax.bar(labels, neg_log_p, color=PALETTE[0], width=0.45,
                  edgecolor="black", linewidth=0.8)
    ax.axhline(-np.log10(0.05), color="gray", linestyle="--", linewidth=0.9,
               label=r"$\alpha=0.05$")
    ax.set_ylabel(r"$-\log_{10}(p)$")
    ax.set_title("Held-out side-effect prediction\n(Draphnet lower Jaccard distance)")
    ax.set_ylim(0, 9)
    for bar, val in zip(bars, neg_log_p):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.15,
                f"$p=3\\times10^{{-8}}$", ha="center", fontsize=9)
    ax.legend(loc="upper right", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "fig_prediction.pdf"))
    plt.savefig(os.path.join(OUT, "fig_prediction.png"), dpi=200)
    plt.close()


# ----------------------------------------------------------------------
# Figure 3: enrichment summary (targets with significant disease-gene
# associations)
# ----------------------------------------------------------------------
def fig_enrichment():
    # Data grounded: 28 of 132 DrugBank targets have >=1 disease gene
    # at adjusted p<0.01. Median = 7 disease genes per drug.
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    sig = 28
    rest = 132 - 28  # 104
    ax.bar(["Significantly\nenriched\n(adj. $p<0.01$)", "Not\nenriched"],
           [sig, rest],
           color=[PALETTE[2], "lightgray"],
           edgecolor="black", linewidth=0.8)
    ax.set_ylabel("Number of DrugBank targets")
    ax.set_title("Target-level disease-gene enrichment\n(132 targets shared by $\\geq 3$ drugs)")
    for i, v in enumerate([sig, rest]):
        ax.text(i, v + 2, str(v), ha="center", fontsize=10)
    ax.set_ylim(0, 140)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "fig_enrichment.pdf"))
    plt.savefig(os.path.join(OUT, "fig_enrichment.png"), dpi=200)
    plt.close()


# ----------------------------------------------------------------------
# Figure 4: placeholder for drug-gene associations (detailed matrix
# not in extraction)
# ----------------------------------------------------------------------
def fig_associations_placeholder():
    fig, ax = plt.subplots(figsize=(5.4, 3.4))
    ax.text(0.5, 0.55,
            "Selected drug-disease-gene associations\n"
            "(e.g., PPM1M / HTR2C-targeting neuroleptics,\n"
            "CETP / fenofibrate + PPAR$\\alpha$-targeting drugs)",
            ha="center", va="center", fontsize=10,
            bbox=dict(boxstyle="round", facecolor="#f0f0f0",
                      edgecolor="gray"))
    ax.text(0.5, 0.18,
            "Full per-drug, per-gene significance values: Supplementary Table S2.",
            ha="center", va="center", fontsize=9, color="gray")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "fig_associations.pdf"))
    plt.savefig(os.path.join(OUT, "fig_associations.png"), dpi=200)
    plt.close()


if __name__ == "__main__":
    fig_schematic()
    fig_prediction()
    fig_enrichment()
    fig_associations_placeholder()
    print("Generated 4 figures in", OUT)
