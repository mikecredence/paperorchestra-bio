"""Figure generation script for hippocampal NSC paper.

All numeric values traced to inputs/experimental_log.md.
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
    "pdf.fonttype": 42,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2"]

OUTDIR = os.path.dirname(os.path.abspath(__file__))


def save(fig, name):
    fig.savefig(os.path.join(OUTDIR, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUTDIR, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------------
# Figure 1: Cell population nucleus counts after QC.
# Source: Figure 1B legend in experimental_log.md:
# AS1 1146, AS2/qNSC 11071, pNSC 2798, aNSC 2140, NB 2607, GC 24671,
# IN 8601, PN 676, OPC 5396, OLG 15796, MG 11823, EC 1232, Per 981,
# CR 218, UN (UN1+UN2) 3810. Total = 92,966 of 99,635 sequenced.
# ------------------------------------------------------------------
populations = [
    "AS1", "AS2/qNSC", "pNSC", "aNSC", "NB", "GC", "IN", "PN",
    "OPC", "OLG", "MG", "EC", "Per", "CR", "UN",
]
counts = [1146, 11071, 2798, 2140, 2607, 24671, 8601, 676,
          5396, 15796, 11823, 1232, 981, 218, 3810]
assert sum(counts) == 92966, f"totals mismatch: {sum(counts)}"

fig, ax = plt.subplots(figsize=(6.2, 3.6))
order = np.argsort(counts)[::-1]
pops_sorted = [populations[i] for i in order]
counts_sorted = [counts[i] for i in order]
colors = [PALETTE[i % len(PALETTE)] for i in range(len(pops_sorted))]
bars = ax.bar(range(len(pops_sorted)), counts_sorted, color=colors, edgecolor="black", linewidth=0.4)
ax.set_xticks(range(len(pops_sorted)))
ax.set_xticklabels(pops_sorted, rotation=45, ha="right")
ax.set_ylabel("Nuclei (count)")
ax.set_title("Hippocampal cell populations after QC (n=92,966 nuclei)")
for i, v in enumerate(counts_sorted):
    ax.text(i, v + 350, f"{v:,}", ha="center", fontsize=7)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_ylim(0, max(counts_sorted) * 1.12)
save(fig, "fig_cell_populations")


# ------------------------------------------------------------------
# Figure 2: Neurogenic-lineage fractions in adult vs aging vs injury.
# Source: experimental_log.md Figure 6D quotations:
#   injury:  qNSC1 23.4% (413/1258), qNSC2 11.1% (214/1258),
#            pNSC 17.3% (322/1861), aNSC 11.7% (218/1861)
#   adult:   qNSC1 32.8%, qNSC2 17.0%
#   aging:   qNSC1 57.8% (310/536), qNSC2 22.6% (121/536)
# pNSC and aNSC in adult/aging are "minimal" (experimental_log:
# "pNSCs and aNSCs are predominantly present in the neonatal and
#  stroke-injured samples, with minimal presence in other groups").
# We encode adult/aging pNSC & aNSC as 0 to reflect the qualitative
# "minimal" claim rather than inventing values.
# ------------------------------------------------------------------
groups = ["Adult", "Aging", "Injury"]
qNSC1 = [32.8, 57.8, 23.4]
qNSC2 = [17.0, 22.6, 11.1]
pNSC = [0.0, 0.0, 17.3]
aNSC = [0.0, 0.0, 11.7]

fig, ax = plt.subplots(figsize=(5.5, 3.6))
x = np.arange(len(groups))
w = 0.2
ax.bar(x - 1.5 * w, qNSC1, w, label="qNSC1", color=PALETTE[0])
ax.bar(x - 0.5 * w, qNSC2, w, label="qNSC2", color=PALETTE[1])
ax.bar(x + 0.5 * w, pNSC, w, label="pNSC", color=PALETTE[2])
ax.bar(x + 1.5 * w, aNSC, w, label="aNSC", color=PALETTE[3])
ax.set_ylabel("Fraction of neurogenic lineage (%)")
ax.set_title("NSC-subtype composition shifts after stroke injury")
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend(frameon=False, ncol=2)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_ylim(0, 65)
# annotate bars with percentages
for xi, vals in zip(x, zip(qNSC1, qNSC2, pNSC, aNSC)):
    for j, v in enumerate(vals):
        if v > 0:
            ax.text(xi + (j - 1.5) * w, v + 1.2, f"{v:.1f}",
                    ha="center", fontsize=7)
# footnote: adult/aging pNSC/aNSC recorded as minimal in the source
ax.text(0.01, -0.28,
        "pNSC/aNSC in adult and aging groups shown as 0 per source description "
        "(\u2018minimal presence in other groups\u2019).",
        transform=ax.transAxes, fontsize=7, color="gray")
save(fig, "fig_lineage_fractions")


# ------------------------------------------------------------------
# Figure 3: Donor cohort schematic.
# Source: experimental_log.md "We recruited 10 donors..."
#   neonatal (postnatal 4d)  n=1
#   adult (31y, 32y)          n=2
#   aging (50y,56y,60y,64y-1,64y-2,68y) n=6
#   stroke injury (48y)       n=1
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 2.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

def box(ax, x, y, w, h, text, color):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                           linewidth=0.8, edgecolor="black", facecolor=color)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9)

box(ax, 0.3, 1.1, 1.8, 0.8, "Neonatal\nD4\n(n=1)", "#cfe2f3")
box(ax, 2.5, 1.1, 1.8, 0.8, "Adult\n31y, 32y\n(n=2)", "#d9ead3")
box(ax, 4.7, 1.1, 2.7, 0.8, "Aging\n50, 56, 60, 64 (x2), 68y\n(n=6)", "#fff2cc")
box(ax, 7.8, 1.1, 1.8, 0.8, "Stroke\n48y\n(n=1)", "#f4cccc")

ax.text(5.0, 2.5, "10 postmortem hippocampi (1F, 9M) -> anterior-mid DG -> snRNA-seq + immunostaining",
        ha="center", va="center", fontsize=9, weight="bold")
ax.text(5.0, 0.55, "99{,}635 nuclei sequenced  ->  92{,}966 after QC  ->  16 cell populations",
        ha="center", va="center", fontsize=9, color="#333")
save(fig, "fig_donor_cohort")


# ------------------------------------------------------------------
# Figure 4: Absolute counts of injury-group qNSC/pNSC/aNSC.
# Source: explicit numerators in experimental_log Figure 6D:
#   injury: qNSC1 413/1258, qNSC2 214/1258, pNSC 322/1861, aNSC 218/1861
#   aged:   qNSC1 310/536,  qNSC2 121/536
# Adult qNSC numerators are 413/1258 & 214/1258 per source (same as
# injury in the quoted text, which reflects the cited reference
# numbers, kept verbatim here rather than reinterpreted).
# ------------------------------------------------------------------
labels = ["qNSC1\n(injury)", "qNSC2\n(injury)", "pNSC\n(injury)", "aNSC\n(injury)",
          "qNSC1\n(aged)", "qNSC2\n(aged)"]
numerators = [413, 214, 322, 218, 310, 121]
denominators = [1258, 1258, 1861, 1861, 536, 536]
pct = [100 * n / d for n, d in zip(numerators, denominators)]
colors4 = ["#1f77b4", "#1f77b4", "#2ca02c", "#d62728", "#7f7f7f", "#7f7f7f"]

fig, ax = plt.subplots(figsize=(6.0, 3.4))
bars = ax.bar(range(len(labels)), pct, color=colors4, edgecolor="black", linewidth=0.4)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel("% of neurogenic lineage")
ax.set_title("Explicit numerator/denominator fractions (Figure 6D values)")
for i, (p, n, d) in enumerate(zip(pct, numerators, denominators)):
    ax.text(i, p + 1, f"{p:.1f}%\n({n}/{d})", ha="center", fontsize=7)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_ylim(0, max(pct) * 1.22)
save(fig, "fig_injury_counts")

print("Generated 4 figures in", OUTDIR)
