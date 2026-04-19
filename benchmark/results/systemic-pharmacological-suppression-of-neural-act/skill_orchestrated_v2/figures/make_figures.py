"""Figure generation for systemic pharmacological suppression paper.

All plotted numerical quantities are p-values or stimulus parameters that
appear verbatim in the experimental log. No means/SEMs are fabricated;
because raw means are not numerically tabulated in the extraction, the
data-grounded figures visualise the extracted p-value comparisons, and
the remaining figures are schematic/protocol diagrams grounded in the
extraction text.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "figure.dpi": 200,
})

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PALETTE = {"WT": "#333333", "KO": "#d62728", "rescue": "#2ca02c",
           "neutral": "#1f77b4", "accent": "#9467bd"}


def neg_log10(p):
    return -np.log10(max(p, 1e-10))


def significance_bar_panel(ax, labels, pvals, title, threshold=0.05, rotation=0,
                           ylabel=r"$-\log_{10}(p)$"):
    """Draw -log10(p) bars for extracted p-values, with alpha line at 0.05."""
    x = np.arange(len(labels))
    nlp = [neg_log10(p) for p in pvals]
    colors = [PALETTE["rescue"] if p < threshold else PALETTE["KO"] for p in pvals]
    bars = ax.bar(x, nlp, color=colors, edgecolor="black", linewidth=0.6)
    ax.axhline(neg_log10(threshold), color="gray", linestyle="--", linewidth=0.8,
               label=r"$\alpha=0.05$")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=rotation, ha="right" if rotation else "center")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    for xi, pv in zip(x, pvals):
        ax.text(xi, neg_log10(pv) + 0.1, f"p={pv:g}", ha="center", fontsize=7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=7)


# ------------------------------------------------------------------ Figure 1
# Selective VOR-increase impairment: key p-values from Fig. 1
fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.2))
# Panel A: WT and KO VOR-increase 0 vs 30 min + KO vs WT
sig_labels_A = ["WT 0 vs 30\n(VOR-inc)", "KO 0 vs 30\n(VOR-inc)", "KO vs WT\n(30 min)"]
sig_pvals_A = [7.37e-4, 0.97, 3.47e-5]
significance_bar_panel(axes[0], sig_labels_A, sig_pvals_A,
                       "VOR-increase learning (1 Hz)")
# Panel B: VOR-decrease control
sig_labels_B = ["WT 0 vs 30\n(VOR-dec)", "KO 0 vs 30\n(VOR-dec)", "KO vs WT\n(30 min)"]
sig_pvals_B = [0.001, 1.10e-5, 0.091]
significance_bar_panel(axes[1], sig_labels_B, sig_pvals_B,
                       "VOR-decrease learning (1 Hz)")
fig.suptitle("Fig. 1. Selective VOR-increase learning impairment in L7-Fmr1 KO mice",
             y=1.02, fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "fig1_selective_impairment.pdf"),
            bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "fig1_selective_impairment.png"),
            bbox_inches="tight")
plt.close()


# ------------------------------------------------------------------ Figure 2
# Behavioral pre-training rescue (Fig. 2 p-values)
fig, ax = plt.subplots(figsize=(7.5, 3.2))
labels = [
    "No pre-training\nKO 0 vs 30",
    "VOR-dec pre-train\nKO 0 vs 30",
    "Vest-only pre-train\nKO vs WT 30",
    "KO pre vs no-pre\n(paired t-test)",
    "Subsampled: KO vs WT\n(VOR-dec pre)",
    "Subsampled: KO vs WT\n(Vest-only pre)",
]
pvals = [0.99, 0.001, 0.84, 0.01, 0.74, 0.40]
significance_bar_panel(ax, labels, pvals,
                       "Fig. 2. Behavioural pre-training rescues VOR-increase learning in L7-Fmr1 KO",
                       rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "fig2_behavioral_pretraining.pdf"),
            bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "fig2_behavioral_pretraining.png"),
            bbox_inches="tight")
plt.close()


# ------------------------------------------------------------------ Figure 3
# Diazepam rescue: Fig. 3 p-values
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.2))
labels_L = [
    "KO 1-day post-diaz\nvs WT (30 min)",
    "KO no-drug\n0 vs 30",
    "KO 1 week post-diaz\n0 vs 30",
    "WT no-drug vs\n1-day post-diaz",
]
pvals_L = [0.86, 0.99, 0.12, 0.55]
significance_bar_panel(axes[0], labels_L, pvals_L,
                       "VOR-increase: diazepam rescue (0.5 mg/kg IP)",
                       rotation=30)

labels_R = [
    "WT VOR-dec\n1d post vs ctrl",
    "KO VOR-dec\n1d post vs ctrl",
    "KO vs WT\n1d post VOR-dec",
    "KO baseline VOR\nPre vs 2h post",
    "KO baseline VOR\nPre vs 18-24h post",
]
pvals_R = [0.91, 0.37, 0.11, 0.72, 0.77]
significance_bar_panel(axes[1], labels_R, pvals_R,
                       "Specificity: VOR-decrease and baseline unchanged",
                       rotation=30)
fig.suptitle("Fig. 3. Diazepam pre-treatment rescues VOR-increase learning specifically",
             y=1.04, fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "fig3_diazepam_rescue.pdf"),
            bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "fig3_diazepam_rescue.png"),
            bbox_inches="tight")
plt.close()


# ------------------------------------------------------------------ Figure 4
# Low-frequency 0.5 Hz results: not rescued
fig, ax = plt.subplots(figsize=(7.5, 3.2))
labels = [
    "KO vs WT\n0.5 Hz, no pre-train",
    "KO VOR-dec pre vs\nno pre (paired)",
    "KO Vest-only pre vs\nno pre (paired)",
    "KO saline vs\ndiazepam (paired)",
]
pvals = [0.06, 0.47, 0.35, 0.66]
significance_bar_panel(ax, labels, pvals,
                       "Fig. 4. Low-frequency (0.5 Hz) VOR-increase impairment is NOT rescued",
                       rotation=20)
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "fig4_low_freq_no_rescue.pdf"),
            bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "fig4_low_freq_no_rescue.png"),
            bbox_inches="tight")
plt.close()


# ------------------------------------------------------------------ Figure 5
# OKR adaptation: rescue exceeds WT
fig, ax = plt.subplots(figsize=(7.5, 3.2))
labels = [
    "WT 0 vs 60 min\n(saline)",
    "KO vs WT, 60 min\n(saline)",
    "KO 0 vs 60 min\n(saline)",
    "KO saline vs\ndiazepam (60 min)",
    "KO vs WT, 60 min\n(post-diazepam)",
    "Baseline OKR\nKO vs WT (Pre)",
]
pvals = [0.001, 1.27e-4, 0.87, 0.0001, 0.02, 0.69]
significance_bar_panel(ax, labels, pvals,
                       "Fig. 5. Diazepam rescues OKR adaptation; KO exceeds WT post-drug",
                       rotation=20)
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "fig5_okr_rescue.pdf"),
            bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "fig5_okr_rescue.png"),
            bbox_inches="tight")
plt.close()


# ------------------------------------------------------------------ Figure 6
# Schematic: metaplasticity hypothesis
fig, ax = plt.subplots(figsize=(7.5, 4.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis("off")

# Top row: WT
ax.add_patch(FancyBboxPatch((0.3, 4.5), 2.4, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor="black", facecolor="#eeeeee"))
ax.text(1.5, 5.8, "Naive WT\nnormal LTD threshold", ha="center", fontsize=9)
ax.text(1.5, 4.9, "spont. activity fails\nto induce LTD", ha="center", fontsize=8,
        style="italic")

ax.add_patch(FancyBboxPatch((3.5, 4.5), 2.4, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor="black", facecolor="#cfe8d3"))
ax.text(4.7, 5.8, "Training induces\nLTD at needed\nsynapses", ha="center", fontsize=9)

ax.add_patch(FancyBboxPatch((6.7, 4.5), 2.9, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor="black", facecolor="#cfe8d3"))
ax.text(8.15, 5.8, "Normal learning", ha="center", fontsize=10, weight="bold")

# Arrows top row
ax.add_patch(FancyArrowPatch((2.75, 5.4), (3.45, 5.4),
                             arrowstyle="->", mutation_scale=15))
ax.add_patch(FancyArrowPatch((5.95, 5.4), (6.65, 5.4),
                             arrowstyle="->", mutation_scale=15))

# Bottom row: Enhanced LTD
ax.add_patch(FancyBboxPatch((0.3, 1.0), 2.4, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor="black", facecolor="#fbd5d5"))
ax.text(1.5, 2.3, "Enhanced LTD\n(L7-Fmr1 KO /\nMHCI KbDb-/-)", ha="center", fontsize=9)
ax.text(1.5, 1.4, "spont. activity\naberrantly induces\nLTD, raises threshold",
        ha="center", fontsize=7, style="italic")

ax.add_patch(FancyBboxPatch((3.5, 1.0), 2.4, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor="black", facecolor="#fbd5d5"))
ax.text(4.7, 2.3, "Training FAILS\nto induce LTD\nwhere needed", ha="center", fontsize=9)

ax.add_patch(FancyBboxPatch((6.7, 1.0), 2.9, 1.8,
                            boxstyle="round,pad=0.1",
                            edgecolor="black", facecolor="#fbd5d5"))
ax.text(8.15, 2.3, "Impaired learning", ha="center", fontsize=10, weight="bold")

ax.add_patch(FancyArrowPatch((2.75, 1.9), (3.45, 1.9),
                             arrowstyle="->", mutation_scale=15))
ax.add_patch(FancyArrowPatch((5.95, 1.9), (6.65, 1.9),
                             arrowstyle="->", mutation_scale=15))

# Vertical intervention arrow: pre-training / diazepam resets
ax.add_patch(FancyArrowPatch((1.5, 2.85), (1.5, 4.45),
                             arrowstyle="->", mutation_scale=18,
                             color=PALETTE["rescue"], linewidth=1.8))
ax.text(1.5, 3.65, "Pre-training\nor diazepam\n(activity suppression)",
        ha="center", fontsize=8, color=PALETTE["rescue"],
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                  edgecolor=PALETTE["rescue"]))

ax.set_title("Fig. 6. Threshold metaplasticity hypothesis", fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "fig6_metaplasticity_schematic.pdf"),
            bbox_inches="tight")
plt.savefig(os.path.join(OUTDIR, "fig6_metaplasticity_schematic.png"),
            bbox_inches="tight")
plt.close()

print("Generated 6 figures: fig1..fig5 (data-grounded p-value plots) + fig6 (schematic).")
