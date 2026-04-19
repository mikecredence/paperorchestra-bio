"""Generate figures for the DNA foundation model benchmark paper.

All values are taken verbatim from inputs/experimental_log.md. No values are
fabricated. Missing values are rendered as placeholder/empty bars.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

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

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
MODELS = ["DNABERT-2", "NT-v2", "HyenaDNA", "Caduceus-Ph", "GROVER"]


def save(fig, stem):
    fig.tight_layout()
    fig.savefig(f"figures/{stem}.pdf")
    fig.savefig(f"figures/{stem}.png", dpi=200)
    plt.close(fig)


# ------------------------------------------------------------------
# Figure 1: Average AUC gain from summary-token -> mean-token pooling
# Experimental log Experiment 1.
# ------------------------------------------------------------------
gain = [4.0, 6.8, 8.7, 5.9, 1.4]               # percent, verbatim
iqr_lo = [2.0, 3.7, 4.6, 2.8, 0.7]
iqr_hi = [5.5, 9.6, 12.9, 9.1, 1.9]
err_lo = [g - lo for g, lo in zip(gain, iqr_lo)]
err_hi = [hi - g for g, hi in zip(gain, iqr_hi)]

fig, ax = plt.subplots(figsize=(5.0, 3.3))
x = np.arange(len(MODELS))
bars = ax.bar(x, gain, yerr=[err_lo, err_hi], capsize=4,
              color=PALETTE, edgecolor="black", linewidth=0.5)
ax.set_xticks(x)
ax.set_xticklabels(MODELS, rotation=15)
ax.set_ylabel("Average AUC gain (\u0025)\n(summary-token \u2192 mean token)")
ax.set_title("Mean token pooling improves zero-shot classification")
ax.set_ylim(0, 14)
for xi, g in zip(x, gain):
    ax.text(xi, g + 0.25, f"{g:.1f}%", ha="center", va="bottom", fontsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.grid(True, alpha=0.3)
save(fig, "fig1_pooling_gain")


# ------------------------------------------------------------------
# Figure 2: Datasets (out of 52) where mean pooling is significantly better
# Experimental log Experiment 1.
# ------------------------------------------------------------------
vs_summary = [41, 42, 35, 37, 41]
vs_max = [41, 42, 35, 37, 41]
x = np.arange(len(MODELS))
width = 0.4

fig, ax = plt.subplots(figsize=(5.4, 3.3))
ax.bar(x - width / 2, vs_summary, width, label="Mean > summary-token",
       color=PALETTE[0], edgecolor="black", linewidth=0.5)
ax.bar(x + width / 2, vs_max, width, label="Mean > max pooling",
       color=PALETTE[1], edgecolor="black", linewidth=0.5)
ax.axhline(52, linestyle="--", color="gray", linewidth=0.8)
ax.text(len(MODELS) - 0.5, 52.5, "52 datasets total", fontsize=8, color="gray",
        ha="right")
ax.set_xticks(x)
ax.set_xticklabels(MODELS, rotation=15)
ax.set_ylabel("Datasets with $p<0.01$ (DeLong)")
ax.set_ylim(0, 56)
ax.set_title("Mean pooling superior across a majority of binary tasks")
ax.legend(loc="lower right", frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "fig2_pooling_counts")


# ------------------------------------------------------------------
# Figure 3: Pathogenic SNP identification and QTL AUC
# Experimental log Experiments 7 and 8.
# ------------------------------------------------------------------
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(8.8, 3.5))

# Left: pathogenic SNP AUC + Cohen's d
snp_models = ["NT-v2", "Caduceus-Ph", "Enformer*", "Caduceus-Ph (long)"]
snp_auc = [0.73, 0.70, 0.69, 0.62]
snp_d = [0.88, np.nan, 0.73, np.nan]
xs = np.arange(len(snp_models))
bars = ax_left.bar(xs, snp_auc, color=[PALETTE[1], PALETTE[3], "#888888",
                                       PALETTE[3]], edgecolor="black",
                   linewidth=0.5)
for xi, d in zip(xs, snp_d):
    if not np.isnan(d):
        ax_left.text(xi, snp_auc[xi] + 0.01, f"d={d:.2f}",
                     ha="center", va="bottom", fontsize=8)
ax_left.axhline(0.5, linestyle="--", color="gray", linewidth=0.6)
ax_left.set_xticks(xs)
ax_left.set_xticklabels(snp_models, rotation=20, ha="right")
ax_left.set_ylim(0.45, 0.95)
ax_left.set_ylabel("Average test AUC")
ax_left.set_title("Pathogenic vs. common SNP identification")
ax_left.spines["top"].set_visible(False)
ax_left.spines["right"].set_visible(False)

# Right: QTL AUC
qtl_labels = ["eQTL", "sQTL", "ipaQTL", "paQTL"]
alpha_genome = [np.nan, 0.80, 0.86, np.nan]
enformer = [0.77, np.nan, np.nan, np.nan]
sei_hidden = [np.nan, 0.65, np.nan, np.nan]
sei_output = [np.nan, 0.63, np.nan, np.nan]
caduceus = [0.65, np.nan, np.nan, np.nan]

xq = np.arange(len(qtl_labels))
w = 0.17
groups = [
    ("AlphaGenome*", alpha_genome, "#2ca02c"),
    ("Enformer*", enformer, "#888888"),
    ("Sei* (hidden)", sei_hidden, "#555555"),
    ("Sei* (output)", sei_output, "#bbbbbb"),
    ("Caduceus-Ph", caduceus, PALETTE[3]),
]
for i, (lab, vals, col) in enumerate(groups):
    mask = ~np.isnan(vals)
    ax_right.bar(xq[mask] + (i - 2) * w, np.array(vals)[mask], w,
                 label=lab, color=col, edgecolor="black", linewidth=0.5)
ax_right.axhline(0.5, linestyle="--", color="gray", linewidth=0.6)
ax_right.set_xticks(xq)
ax_right.set_xticklabels(qtl_labels)
ax_right.set_ylim(0.45, 0.95)
ax_right.set_ylabel("AUC")
ax_right.set_title("QTL variant effect prediction")
ax_right.legend(loc="lower right", frameon=False, fontsize=7)
ax_right.spines["top"].set_visible(False)
ax_right.spines["right"].set_visible(False)

save(fig, "fig3_variants")


# ------------------------------------------------------------------
# Figure 4: Multi-species pre-training improves HyenaDNA on specific tasks
# Experimental log Experiment 9.
# ------------------------------------------------------------------
labels = ["Human 5mC", "Human vs. Worm"]
orig = [0.707, 0.968]
multi = [0.749, 0.984]

xs = np.arange(len(labels))
w = 0.35

fig, ax = plt.subplots(figsize=(4.8, 3.3))
ax.bar(xs - w / 2, orig, w, label="Original (human only)",
       color=PALETTE[0], edgecolor="black", linewidth=0.5)
ax.bar(xs + w / 2, multi, w, label="Multi-species (135 species)",
       color=PALETTE[2], edgecolor="black", linewidth=0.5)
for xi in xs:
    ax.text(xi - w / 2, orig[xi] + 0.005, f"{orig[xi]:.3f}",
            ha="center", va="bottom", fontsize=8)
    ax.text(xi + w / 2, multi[xi] + 0.005, f"{multi[xi]:.3f}",
            ha="center", va="bottom", fontsize=8)
ax.set_xticks(xs)
ax.set_xticklabels(labels)
ax.set_ylabel("AUC")
ax.set_ylim(0.6, 1.02)
ax.set_title("Multi-species pre-training improves HyenaDNA (14/49 datasets)")
ax.legend(loc="lower right", frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "fig4_pretraining")


# ------------------------------------------------------------------
# Figure 5 (schematic): zero-shot benchmark pipeline
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.0, 2.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

boxes = [
    (0.2, "DNA sequence\n(41 bp - 196 kb)"),
    (2.2, "Frozen foundation\nmodel (5 models)"),
    (4.4, "Token embeddings\n(last layer)"),
    (6.6, "Pooling\n(sum / mean / max)"),
    (8.7, "Random forest\nclassifier"),
]
for x, label in boxes:
    patch = FancyBboxPatch((x, 1.0), 1.6, 1.1, boxstyle="round,pad=0.06",
                           linewidth=0.8, edgecolor="black",
                           facecolor="#e8f0ff")
    ax.add_patch(patch)
    ax.text(x + 0.8, 1.55, label, ha="center", va="center", fontsize=9)

for x in [1.8, 4.0, 6.2, 8.3]:
    ax.annotate("", xy=(x + 0.3, 1.55), xytext=(x - 0.1, 1.55),
                arrowprops=dict(arrowstyle="->", lw=1.2))

ax.text(5.0, 2.8, "Zero-shot embedding benchmark pipeline",
        ha="center", fontsize=11, fontweight="bold")
ax.text(5.0, 0.55,
        "Evaluation: 57 classification datasets; gene expression (GTEx v8);\n"
        "variant effect (22,222/17,374 SNPs; 1,896 eQTLs, 540 sQTLs,\n"
        "116 ipaQTLs, 142 paQTLs); TAD attention analysis",
        ha="center", fontsize=8, color="#444444")
save(fig, "fig5_pipeline")


print("Done: 5 figures generated.")
