"""Generate figures for the 5'UTR mRNA editing paper.

All values traced to experimental_log.md (statistical_sentences block).
No fabricated numbers.
"""

import os
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

HERE = Path(__file__).resolve().parent
os.chdir(HERE)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "pdf.fonttype": 42,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]


def save(fig, stem):
    fig.savefig(f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(f"{stem}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 1: cross-cell-line MRL correlations (r^2)
# Data (verbatim from experimental_log.md):
#   HEK293T vs T cells: 0.837-0.870
#   HEK293T vs HepG2:   0.847-0.871
#   HEK293T replicates: 0.938
#   T cell replicates:  0.814
#   Optimus held-out HEK293T: 0.937
#   Optimus on T cells:  0.841
#   Optimus on HepG2:    0.840
labels = [
    "HEK293T\nreplicates",
    "T-cell\nreplicates",
    "HEK293T vs\nT cells",
    "HEK293T vs\nHepG2",
    "Model vs\nHEK293T",
    "Model vs\nT cells",
    "Model vs\nHepG2",
]
# For ranges we use the midpoint and draw an error bar to the extremes.
values = [0.938, 0.814, (0.837 + 0.870) / 2, (0.847 + 0.871) / 2,
          0.937, 0.841, 0.840]
lows = [0.938, 0.814, 0.837, 0.847, 0.937, 0.841, 0.840]
highs = [0.938, 0.814, 0.870, 0.871, 0.937, 0.841, 0.840]
err_low = [v - l for v, l in zip(values, lows)]
err_high = [h - v for v, h in zip(values, highs)]
colors = [PALETTE[0]] * 2 + [PALETTE[1]] * 2 + [PALETTE[2]] * 3

fig, ax = plt.subplots(figsize=(6.4, 3.4))
xs = np.arange(len(labels))
bars = ax.bar(xs, values, color=colors, edgecolor="black", linewidth=0.6)
ax.errorbar(xs, values, yerr=[err_low, err_high], fmt="none",
            ecolor="black", capsize=3, lw=0.8)
ax.set_ylim(0.75, 1.0)
ax.set_ylabel(r"Coefficient of determination $r^2$")
ax.set_xticks(xs)
ax.set_xticklabels(labels, fontsize=8)
# Legend
legend_handles = [
    mpatches.Patch(color=PALETTE[0], label="Replicate"),
    mpatches.Patch(color=PALETTE[1], label="Between cell lines"),
    mpatches.Patch(color=PALETTE[2], label="Optimus 5-Prime prediction"),
]
ax.legend(handles=legend_handles, loc="lower left", frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("MRL correlations across cell types and against model predictions")
plt.tight_layout()
save(fig, "fig1_cross_cell_r2")


# ----------------------------------------------------------------------
# Figure 2: model performance on random-end 25nt MPRA
# Data (verbatim):
#   Inter-replicate top-20k: r^2 = 0.692; top-2k: r^2 = 0.844
#   Previous fixed-end 50nt library replicate r^2 = 0.938 (for reference)
#   Optimus 5-Prime (50nt) on 25nt data: r^2 = 0.564
#   Optimus 5-Prime(25-100nt): r^2 = 0.600
#   Optimus 5-Prime(25): r^2 = 0.806 on held-out set (Figure 3E)
models = ["Optimus 5-Prime\n(50 nt)", "Optimus 5-Prime\n(25-100 nt)",
          "Optimus 5-Prime(25)\n(this work)"]
r2s = [0.564, 0.600, 0.806]
colors2 = [PALETTE[3], PALETTE[4], PALETTE[2]]

fig, ax = plt.subplots(figsize=(5.4, 3.4))
xs = np.arange(len(models))
ax.bar(xs, r2s, color=colors2, edgecolor="black", linewidth=0.6)
for i, v in enumerate(r2s):
    ax.text(i, v + 0.01, f"{v:.3f}", ha="center", fontsize=9)
# Reference line: inter-replicate ceiling at 0.844 (top-2k) for the 25nt library
ax.axhline(0.844, color="gray", linestyle="--", lw=0.9)
ax.text(len(models) - 1.05, 0.852,
        r"Inter-replicate ceiling $r^2 = 0.844$ (top-2000)", fontsize=8,
        ha="right", color="gray")
ax.set_ylim(0.0, 1.0)
ax.set_ylabel(r"Prediction $r^2$ on random-end 25-nt MPRA")
ax.set_xticks(xs)
ax.set_xticklabels(models, fontsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("Transfer of Optimus models to fully-variable 25 nt 5'UTRs")
plt.tight_layout()
save(fig, "fig2_model_r2_25nt")


# ----------------------------------------------------------------------
# Figure 3: megaTAL editing at 2 pmol mRNA for TGFBR2 and PDCD1
# Data (verbatim):
#   TGFBR2, DEN-designed best: 55.6% absolute
#   (LAMA5 was the prior best; DEN-designed is 18-33% higher than LAMA5)
#   PDCD1, same DEN-designed: 80.8% absolute (as good as Strong Kozak)
#   PDCD1, VAT1 control: 91.4% absolute (best for PDCD1)
#   Text also states editing exceeded 40% for TGFBR2 and 80% for PDCD1
#   Additionally "one design resulted in a TGFBR2 editing efficiency up to
#   50% higher than all controls"
# LAMA5 can be derived from DEN/(1+0.33) to DEN/(1+0.18) = [41.8, 47.1]%
lama5_low = 55.6 / 1.33
lama5_high = 55.6 / 1.18
lama5_mid = (lama5_low + lama5_high) / 2
# Use midpoint with an error bar to reflect the 18-33% improvement range.
conditions = ["DEN-designed\nbest (this work)", "LAMA5\n(prior best)"]
tgfbr2 = [55.6, lama5_mid]
tgfbr2_err = [[0, lama5_mid - lama5_low], [0, lama5_high - lama5_mid]]

# For PDCD1, we have the DEN-designed and VAT1 values explicitly.
pdcd1 = [80.8, 91.4]
pdcd1_labels = ["DEN-designed\n(TGFBR2 best)", "VAT1 control\n(PDCD1 best)"]

fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.6))

ax = axes[0]
xs = np.arange(len(conditions))
bars = ax.bar(xs, tgfbr2, color=[PALETTE[2], PALETTE[0]],
              edgecolor="black", linewidth=0.6)
ax.errorbar(xs, tgfbr2, yerr=tgfbr2_err, fmt="none", ecolor="black",
            capsize=3, lw=0.8)
for i, v in enumerate(tgfbr2):
    ax.text(i, v + 1.5, f"{v:.1f}%", ha="center", fontsize=9)
ax.set_xticks(xs)
ax.set_xticklabels(conditions, fontsize=9)
ax.set_ylabel("Absolute editing efficiency at 2 pmol mRNA (%)")
ax.set_ylim(0, 80)
ax.set_title(r"$TGFBR2$ megaTAL in K562")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax = axes[1]
xs = np.arange(len(pdcd1))
ax.bar(xs, pdcd1, color=[PALETTE[2], PALETTE[1]],
       edgecolor="black", linewidth=0.6)
for i, v in enumerate(pdcd1):
    ax.text(i, v + 1.5, f"{v:.1f}%", ha="center", fontsize=9)
ax.set_xticks(xs)
ax.set_xticklabels(pdcd1_labels, fontsize=9)
ax.set_ylabel("Absolute editing efficiency at 2 pmol mRNA (%)")
ax.set_ylim(0, 100)
ax.set_title(r"$PDCD1$ megaTAL in K562")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
save(fig, "fig3_editing_efficiency")


# ----------------------------------------------------------------------
# Figure 4: schematic of Optimus 5-Prime + DEN design pipeline
# Structural description comes verbatim from experimental_log.md:
#   DEN generator takes 100-d latent vector -> 50x4 or 25x4 logits
#   Optimus 5-Prime(CNN) predicts MRL from sequence
#   Fitness = predicted MRL; diversity = pairwise similarity penalty
fig, ax = plt.subplots(figsize=(7.5, 3.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis("off")


def box(x, y, w, h, text, color):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       fc=color, ec="black", lw=0.9)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=9)


def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                                 arrowstyle="->", mutation_scale=15,
                                 lw=1.2, color="black"))


box(0.1, 2.5, 1.9, 0.9, "100-d\nlatent vector\n$z\\sim\\mathcal{N}(0,I)$",
    "#e8f0fb")
box(2.4, 2.3, 1.8, 1.3,
    "DEN generator\n$G_\\theta(z)$\n($\\rightarrow$ 50$\\times$4 or 25$\\times$4 logits)",
    "#fde8d4")
box(4.8, 2.3, 1.8, 1.3,
    "One-hot\n5'UTR sequence\n(softmax/sampling)", "#e6f4ea")
box(7.2, 2.3, 2.6, 1.3,
    "Optimus 5-Prime (CNN)\npredicts MRL",
    "#f4e2f4")

arrow(2.0, 2.95, 2.4, 2.95)
arrow(4.2, 2.95, 4.8, 2.95)
arrow(6.6, 2.95, 7.2, 2.95)

# Feedback arrow: diversity + MRL loss
box(3.0, 0.3, 5.0, 1.1,
    r"Loss: $-\,\mathrm{MRL}(\mathrm{seq})$"
    r"$+\lambda_{\mathrm{div}}\cdot\mathrm{sim}(\mathrm{seq}_i,\mathrm{seq}_j)"
    r"+\lambda_{\mathrm{VAE}}\cdot\mathrm{KL}$",
    "#fff7d1")
ax.add_patch(FancyArrowPatch((8.4, 2.3), (7.0, 1.4), arrowstyle="->",
                             mutation_scale=14, lw=1.0, color="black",
                             connectionstyle="arc3,rad=-0.2"))
ax.add_patch(FancyArrowPatch((4.0, 1.4), (3.3, 2.3), arrowstyle="->",
                             mutation_scale=14, lw=1.0, color="black",
                             connectionstyle="arc3,rad=-0.2"))
ax.text(5.5, 3.7, "Deep Exploration Network (DEN) for 5'UTR design",
        ha="center", fontsize=11, fontweight="bold")

plt.tight_layout()
save(fig, "fig4_den_schematic")

print("Done: generated 4 figures.")
