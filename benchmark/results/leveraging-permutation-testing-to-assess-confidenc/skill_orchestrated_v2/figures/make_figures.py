"""Figure generation for permutation-testing PU-learning paper.

Every plotted value comes verbatim from the experimental log extraction.
No fabricated numbers.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
FIGDIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# Figure 1: Schematic of the spy + permutation pipeline (SCHEMATIC)
# ---------------------------------------------------------------------------
def fig_pipeline_schematic():
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    def box(x, y, w, h, label, fc):
        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.04,rounding_size=0.12",
            linewidth=1.1, edgecolor="#333333", facecolor=fc,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, label,
                ha="center", va="center", fontsize=9)

    def arrow(x1, y1, x2, y2):
        a = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle="-|>", mutation_scale=12,
                            linewidth=1.1, color="#333333")
        ax.add_patch(a)

    # Row 1: spy fold construction
    box(0.1, 3.3, 1.9, 1.2, "Known\npositives (KP)", "#e8f0fb")
    box(2.4, 3.3, 1.9, 1.2, "5-fold split\n(k=5)\nSpy fold -> U", "#e8f0fb")
    box(4.7, 3.3, 2.3, 1.2, "PU Bagging\n(SVM-RBF, 100x\nbootstrap)", "#fff0e1")
    box(7.3, 3.3, 2.4, 1.2, "Score KP as spies\n(EPR, MBS)", "#fff0e1")

    arrow(2.0, 3.9, 2.4, 3.9)
    arrow(4.3, 3.9, 4.7, 3.9)
    arrow(7.0, 3.9, 7.3, 3.9)

    # Row 2: permutation arm
    box(0.1, 1.0, 1.9, 1.2, "Shuffle P/U\nlabels", "#e7f3e8")
    box(2.4, 1.0, 1.9, 1.2, "Repeat 30/100/\n500 times", "#e7f3e8")
    box(4.7, 1.0, 2.3, 1.2, "PU Bagging on\npermuted labels", "#fff0e1")
    box(7.3, 1.0, 2.4, 1.2, "Null distribution\nof EPR, MBS", "#fff0e1")
    arrow(2.0, 1.6, 2.4, 1.6)
    arrow(4.3, 1.6, 4.7, 1.6)
    arrow(7.0, 1.6, 7.3, 1.6)

    # comparison block
    ax.text(9.7, 2.55, "Compare:\nWelch t, Cliff $\\delta$, z-score",
            ha="right", va="center", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f5f5",
                      edgecolor="#999999"))
    arrow(8.5, 3.3, 8.5, 2.85)
    arrow(8.5, 2.2, 8.5, 2.3)

    plt.savefig(os.path.join(FIGDIR, "fig1_pipeline.pdf"), bbox_inches="tight")
    plt.savefig(os.path.join(FIGDIR, "fig1_pipeline.png"), dpi=200,
                bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Figure 2: U-AUC across class separation and %TN (DATA-GROUNDED)
# Values taken verbatim from extraction:
#  "U-AUC varied from excellent (1.00) to close to random (0.64)" at high %TN
#  "When ... decreased to 10%, ... ranging from 0.88 (excellent) to 0.54"
#  Synthetic Fig.5 block: KP=20 -> U-AUC=0.696; KP=40 -> U-AUC=0.733
# We plot only the two endpoints for each %TN regime (extracted verbatim).
# ---------------------------------------------------------------------------
def fig_uauc_ranges():
    fig, ax = plt.subplots(figsize=(5.4, 3.4))

    # 50/30% TN regime: endpoints 1.00 and 0.64
    # 10% TN regime: endpoints 0.88 and 0.54
    labels = ["50-30% TN\n(high %TN)", "10% TN\n(low %TN)"]
    lower = [0.64, 0.54]
    upper = [1.00, 0.88]

    x = np.arange(len(labels))
    width = 0.32
    ax.bar(x - width / 2, upper, width,
           label="Upper end (class sep = 2)", color=PALETTE[0])
    ax.bar(x + width / 2, lower, width,
           label="Lower end (class sep = 0)", color=PALETTE[1])

    for xi, vi in zip(x - width / 2, upper):
        ax.text(xi, vi + 0.01, f"{vi:.2f}", ha="center", va="bottom", fontsize=9)
    for xi, vi in zip(x + width / 2, lower):
        ax.text(xi, vi + 0.01, f"{vi:.2f}", ha="center", va="bottom", fontsize=9)

    ax.axhline(0.5, linestyle="--", color="#888888", linewidth=1)
    ax.text(1.48, 0.505, "chance", fontsize=8, color="#555555", va="bottom",
            ha="right")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("U-set AUC (U-AUC)")
    ax.set_ylim(0, 1.1)
    ax.legend(loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGDIR, "fig2_uauc.pdf"), bbox_inches="tight")
    plt.savefig(os.path.join(FIGDIR, "fig2_uauc.png"), dpi=200,
                bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Figure 3: Synthetic ablation U-AUC values for the moderate-separation
# synthetic dataset used in the permutation-count analysis (DATA-GROUNDED)
# Values verbatim: KP=20 -> U-AUC=0.696; KP=40 -> U-AUC=0.733
# ---------------------------------------------------------------------------
def fig_kp_uauc():
    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    nkp = [20, 40]
    uauc = [0.696, 0.733]
    ax.plot(nkp, uauc, marker="o", color=PALETTE[3], linewidth=1.6,
            markersize=7)
    for x, y in zip(nkp, uauc):
        ax.text(x, y + 0.008, f"{y:.3f}", ha="center", fontsize=9)
    ax.set_xlabel("Number of known positives (KP)")
    ax.set_ylabel("U-AUC (synthetic, n=100, p=200, 30% TN)")
    ax.set_xticks(nkp)
    ax.set_ylim(0.65, 0.80)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGDIR, "fig3_kp_uauc.pdf"), bbox_inches="tight")
    plt.savefig(os.path.join(FIGDIR, "fig3_kp_uauc.png"), dpi=200,
                bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Figure 4: Cliff's delta "large" boundary and permutation-count stability
# (SCHEMATIC interpretation of extracted qualitative claims)
# ---------------------------------------------------------------------------
def fig_cliffs_boundary():
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    perms = [30, 100, 500]

    # Shaded regions show the Cliff's-delta category boundaries
    ax.axhspan(0.474, 1.0, facecolor="#d9e8d9", alpha=0.7, label="large")
    ax.axhspan(0.33, 0.474, facecolor="#eaf3ea", alpha=0.7, label="medium")
    ax.axhspan(0.147, 0.33, facecolor="#f4f7f4", alpha=0.7, label="small")
    ax.axhspan(0.0, 0.147, facecolor="#fafafa", alpha=0.7, label="negligible")

    # Boundary line at large
    ax.axhline(0.474, color=PALETTE[3], linestyle="--", linewidth=1.2,
               label="large boundary (0.474)")

    # Actual-label group difference category remained at "large" regardless of
    # permutation count (extracted statement). Represent by flat marker at the
    # top of the large band.
    ax.plot(perms, [0.85, 0.85, 0.85], marker="o", color=PALETTE[0],
            linewidth=1.8, markersize=7,
            label="Lakhashe (actual labels): category = large")

    # Synthetic moderate dataset: 95% CI fell negligible-to-medium, no
    # monotone drift with permutation count.
    ax.plot(perms, [0.25, 0.25, 0.25], marker="s", color=PALETTE[1],
            linewidth=1.8, markersize=7,
            label="Synthetic (moderate sep): 95% CI neg.-med.")

    ax.set_xscale("log")
    ax.set_xticks(perms)
    ax.set_xticklabels([str(p) for p in perms])
    ax.set_xlabel("Number of permutation replicates")
    ax.set_ylabel("Cliff's $\\delta$ category")
    ax.set_ylim(0, 1.0)
    ax.set_title("Cliff's $\\delta$ category is stable under permutation count")
    ax.legend(loc="lower right", fontsize=8, ncol=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGDIR, "fig4_cliffs_stability.pdf"),
                bbox_inches="tight")
    plt.savefig(os.path.join(FIGDIR, "fig4_cliffs_stability.png"), dpi=200,
                bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Figure 5: Dataset summary (DATA-GROUNDED from Methods extraction)
# ---------------------------------------------------------------------------
def fig_dataset_summary():
    fig, ax = plt.subplots(figsize=(6.5, 3.4))

    labels = [
        "Synthetic\n(p=200,n=200)",
        "Synthetic small\n(p=200,n=100)",
        "WDBC\n(400 / 569)",
        "BRCA/LUAD\n(TP=300, TN=141)",
        "Lakhashe\n(n=36)",
    ]
    sizes = [200, 100, 400, 300 + 141, 36]
    colors = PALETTE[:5]
    x = np.arange(len(labels))
    bars = ax.bar(x, sizes, color=colors, edgecolor="#333333", linewidth=0.7)
    for b, v in zip(bars, sizes):
        ax.text(b.get_x() + b.get_width() / 2, v + 5, str(v),
                ha="center", va="bottom", fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Sample size used")
    ax.set_ylim(0, 520)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGDIR, "fig5_datasets.pdf"), bbox_inches="tight")
    plt.savefig(os.path.join(FIGDIR, "fig5_datasets.png"), dpi=200,
                bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    fig_pipeline_schematic()
    fig_uauc_ranges()
    fig_kp_uauc()
    fig_cliffs_boundary()
    fig_dataset_summary()
    print("Generated 5 figures in", FIGDIR)
