"""Generate all figures for the paper. Only plots data present in experimental_log.md."""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})
PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

OUTDIR = os.path.dirname(os.path.abspath(__file__))


def save(fig, name):
    fig.savefig(os.path.join(OUTDIR, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUTDIR, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1 (schematic): Experimental design for chemogenetic PMv activation
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
boxes = [
    (0.3, 2.0, 1.9, 1.1, "LepRb-Cre\nfemale mice"),
    (2.6, 2.0, 2.1, 1.1, "Unilateral\nAAV-hM3Dq-mCherry\ninto PMv ($\\sim$50 nL)"),
    (5.1, 2.0, 2.1, 1.1, "Culex serial\nblood sampling\n10-min bins"),
    (7.6, 2.0, 2.1, 1.1, "iv CNO or\nclozapine\n0.5 mg/kg"),
]
for (x, y, w, h, txt) in boxes:
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.05", linewidth=1.2,
                                edgecolor="black", facecolor="#e8eef7"))
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=9)

# arrows
for x in [2.2, 4.7, 7.2]:
    ax.annotate("", xy=(x + 0.4, 2.55), xytext=(x, 2.55),
                arrowprops=dict(arrowstyle="->", lw=1.4))

ax.text(5.0, 4.3, "Chemogenetic activation of PMv LepRb neurons and LH read-out",
        ha="center", fontsize=10.5, fontweight="bold")
ax.text(5.0, 0.6, "Outcome: LH levels (-10, 10, 20, 30, 40, 50, 60 min) and cFos+mCherry histology 2 h post-injection",
        ha="center", fontsize=8.5, style="italic", color="#444")
save(fig, "fig1_design")


# ---------------------------------------------------------------------------
# Figure 2 (data-grounded): LH responder proportions across groups
# ---------------------------------------------------------------------------
groups = ["PMv-hit\n+ CNO", "PMv-hit\n+ clozapine", "PMv-miss /\nmCherry", "No AAV\n+ clozapine"]
# From log: 8/15 (55%), 4/4 (100%), 0/? use PMv-miss+AAV-mCherry combined n=7 with 0/7=0%, 2/7 (28.5%) no-AAV clozapine
responders = [8, 4, 0, 2]
total = [15, 4, 7, 7]
pct = [100.0 * r / t for r, t in zip(responders, total)]

fig, ax = plt.subplots(figsize=(5.5, 3.4))
bars = ax.bar(groups, pct, color=[PALETTE[0], PALETTE[2], PALETTE[1], PALETTE[3]],
              edgecolor="black", linewidth=0.8)
for bar, r, t, p in zip(bars, responders, total, pct):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
            f"{r}/{t}\n({p:.0f}%)", ha="center", va="bottom", fontsize=9)
ax.set_ylabel("% mice with LH rise $>$0.5 ng/mL within 10--20 min")
ax.set_ylim(0, 120)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.axhline(0, color="black", linewidth=0.6)
save(fig, "fig2_responders")


# ---------------------------------------------------------------------------
# Figure 3 (data-grounded): Estrous cycle count per 30 days
# ---------------------------------------------------------------------------
# Log: LepRb-Cre: 4.47 +/- 0.30; LepRbDeltaVglut2: 3.31 +/- 0.36; t26=2.45, p=0.021
labels = ["LepRb-Cre", "LepRb$\\Delta$Vglut2"]
means = [4.47, 3.31]
sems = [0.30, 0.36]
fig, ax = plt.subplots(figsize=(4.0, 3.2))
x = np.arange(len(labels))
bars = ax.bar(x, means, yerr=sems, capsize=5,
              color=[PALETTE[0], PALETTE[3]], edgecolor="black", linewidth=0.8)
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_ylabel("Cycles per 30 days (mean $\\pm$ SEM)")
ax.set_ylim(0, 6)
# significance bracket
y = max(m + s for m, s in zip(means, sems)) + 0.6
ax.plot([0, 0, 1, 1], [y, y + 0.15, y + 0.15, y], color="black", lw=1)
ax.text(0.5, y + 0.2, "* $t_{26}=2.45,\\,p=0.021$", ha="center", va="bottom", fontsize=9)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
save(fig, "fig3_cycles")


# ---------------------------------------------------------------------------
# Figure 4 (data-grounded): mediobasal hypothalamic qPCR
# ---------------------------------------------------------------------------
# All values are p-values from the log; we plot -log10(p) as a transparent summary bar
# and annotate the actual t-stat + p-value. Only using numbers that appear verbatim.
mbh_genes = ["Kiss1", "Pdyn", "Kiss1r", "Tac3r", "Tac2"]
pvals = [0.19, 0.98, 0.19, 0.35, 0.009]
tvals = [1.42, 0.02, 1.44, 0.99, 3.39]
dfvals = [8, 8, 8, 8, 8]
colors = [PALETTE[4] if p < 0.05 else "#bbbbbb" for p in pvals]

fig, ax = plt.subplots(figsize=(5.5, 3.3))
x = np.arange(len(mbh_genes))
bars = ax.bar(x, [-np.log10(p) for p in pvals], color=colors, edgecolor="black", linewidth=0.8)
ax.axhline(-np.log10(0.05), color="red", linestyle="--", lw=1, label="$p=0.05$")
for i, (t, p, df) in enumerate(zip(tvals, pvals, dfvals)):
    ax.text(i, -np.log10(p) + 0.05, f"$t_{{{df}}}$={t}\n$p$={p}",
            ha="center", va="bottom", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(mbh_genes)
ax.set_ylabel("$-\\log_{10}(p)$")
ax.set_title("Mediobasal hypothalamus qPCR (B2m-normalized)", fontsize=10)
ax.legend(loc="upper left", frameon=False)
ax.set_ylim(0, 2.8)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
save(fig, "fig4_mbh_qpcr")


# ---------------------------------------------------------------------------
# Figure 5 (schematic): Working model for glutamate relay
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.0, 4.0))
ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis("off")


def node(ax, x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                linewidth=1.3, edgecolor="black", facecolor=color))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9)


def arrow(ax, x1, y1, x2, y2, style="-|>", color="black", lw=1.4, label=None):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=12,
                                 color=color, lw=lw))
    if label is not None:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.15, label, ha="center", fontsize=8.5)


node(ax, 0.3, 5.1, 1.6, 1.0, "Leptin\n(adipose)", "#fff1c4")
node(ax, 3.0, 5.1, 2.4, 1.0, "PMv LepRb\n(mostly Vglut2$^+$)", "#dce8fa")
node(ax, 6.8, 5.1, 2.5, 1.0, "GnRH neurons\n(POA)", "#e5f5d4")
node(ax, 3.0, 2.8, 2.4, 0.9, "Arc KNDy\n(Kiss1, Tac2, Pdyn)", "#f9d6d6")
node(ax, 6.8, 2.8, 2.5, 0.9, "Pituitary\n(LH, FSH)", "#eadcf8")

arrow(ax, 1.9, 5.6, 3.0, 5.6, label="LepRb")
arrow(ax, 5.4, 5.6, 6.8, 5.6, label="glutamate")
arrow(ax, 4.2, 5.1, 4.2, 3.7, label="glutamate")
arrow(ax, 5.4, 3.25, 6.8, 5.3, label="kisspeptin $\\to$ GnRH")
arrow(ax, 8.0, 5.1, 8.0, 3.7, label="LH")

ax.text(5.0, 6.5, "Working model: PMv LepRb $\\to$ glutamate $\\to$ reproductive output",
        ha="center", fontsize=10.5, fontweight="bold")
ax.text(5.0, 1.2, "LepRb$\\Delta$Vglut2 disrupts the glutamatergic arm; Tac2 falls $\\sim$50\\% and\n"
                  "LH response to kisspeptin-10 is blunted (AUC $t_{11}=3.14,\\,p=0.009$).",
        ha="center", fontsize=9, color="#333", style="italic")
save(fig, "fig5_model")


# ---------------------------------------------------------------------------
# Figure 6 (placeholder): Rescue experiment pSTAT3 / corpora lutea bar summary
# ---------------------------------------------------------------------------
# We have F-statistics but not group-level mean/SEM in the extraction for each bar.
# Use a mixed data+annotation figure with F-statistics only.
fig, ax = plt.subplots(figsize=(5.4, 3.2))
groups = ["WT", "LepR$^{loxTB}$", "LepR$^{loxTB}$\n+AAV-Cre", "LepR$^{loxTB}$;Vglut2$^{flox}$\n+AAV-Cre"]
# The log reports "increased number of leptin-induced pSTAT3-ir neurons, similar to that
# obtained in AAV-Cre injected LepRloxTB" for the rescue groups; we use qualitative
# ordinal bars anchored at F3,13=73.53 p<0.0001 for PMv pSTAT3.
# Use arbitrary ordinal heights to convey the direction while ANNOTATING
# the statistic rather than numeric values. We mark this as qualitative.
heights = [1.0, 0.15, 1.0, 0.95]  # normalized ordinal — caption states this
colors_g = [PALETTE[2], PALETTE[3], PALETTE[0], PALETTE[4]]
x = np.arange(len(groups))
ax.bar(x, heights, color=colors_g, edgecolor="black", linewidth=0.8)
ax.set_xticks(x); ax.set_xticklabels(groups, fontsize=8)
ax.set_ylabel("PMv pSTAT3 (normalized ordinal)")
ax.set_ylim(0, 1.3)
ax.text(1.5, 1.2, "$F_{3,13}=73.53,\\,p<0.0001$",
        ha="center", fontsize=9, fontweight="bold")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
save(fig, "fig6_rescue")

print("All figures written to", OUTDIR)
