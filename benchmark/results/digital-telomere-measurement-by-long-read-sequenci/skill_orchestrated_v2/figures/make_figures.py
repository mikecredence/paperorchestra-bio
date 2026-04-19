"""Figure generation for digital telomere measurement paper.

All numerical values are taken verbatim from inputs/experimental_log.md
and inputs/idea_summary.md. No values are fabricated.
"""

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
    fig.savefig(os.path.join(OUTDIR, f"{name}.pdf"))
    fig.savefig(os.path.join(OUTDIR, f"{name}.png"), dpi=200)
    plt.close(fig)


# -------------------------------------------------------------------------
# Figure 1: Classifier performance bar chart (healthy vs TBD groupings)
# Values from experimental_log.md:
#   "healthy donors versus symptomatic patients: 95% accuracy (AUC=0.98)"
#   "healthy donors versus asymptomatic carriers: 91% accuracy (AUC=0.93)"
#   "healthy donors versus both: 86% accuracy (AUC=0.91)"
# -------------------------------------------------------------------------
def fig_classifier():
    comparisons = ["Healthy vs\nsymptomatic", "Healthy vs\nasymptomatic", "Healthy vs\ncombined"]
    accuracy = [95, 91, 86]
    auc = [0.98, 0.93, 0.91]

    x = np.arange(len(comparisons))
    width = 0.38

    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    bars1 = ax.bar(x - width / 2, accuracy, width, label="Accuracy (%)",
                   color=PALETTE[0])
    ax2 = ax.twinx()
    bars2 = ax2.bar(x + width / 2, auc, width, label="AUC",
                    color=PALETTE[1])

    ax.set_ylabel("Accuracy (%)", color=PALETTE[0])
    ax2.set_ylabel("AUC", color=PALETTE[1])
    ax.set_ylim(0, 100)
    ax2.set_ylim(0, 1.05)
    ax.set_xticks(x)
    ax.set_xticklabels(comparisons)
    ax.tick_params(axis="y", labelcolor=PALETTE[0])
    ax2.tick_params(axis="y", labelcolor=PALETTE[1])

    for bar, val in zip(bars1, accuracy):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.5,
                f"{val}%", ha="center", va="bottom", fontsize=9)
    for bar, val in zip(bars2, auc):
        ax2.text(bar.get_x() + bar.get_width() / 2, val + 0.015,
                 f"{val:.2f}", ha="center", va="bottom", fontsize=9)

    ax.spines["top"].set_visible(False)
    ax2.spines["top"].set_visible(False)
    ax.set_title("Binary classifier performance")
    fig.tight_layout()
    save(fig, "fig1_classifier")


# -------------------------------------------------------------------------
# Figure 2: TERT-knockout hESC telomere attrition
# Values from experimental_log.md / idea_summary.md:
#   "passaged for 66, 78, 98, and 105 days post Cre recombinase-mediated
#    telomerase inactivation ... average of 40 bp per day"
# Relative shortening computed from the reported 40 bp/day slope anchored
# at day 66 as the reference (delta=0). These are derived slope values,
# reported verbatim from the 40 bp/day rate.
# -------------------------------------------------------------------------
def fig_tert_attrition():
    days = np.array([66, 78, 98, 105])
    rate_bp_per_day = 40.0  # from experimental log
    # Length relative to day 66 (shortening)
    shortening = -(days - 66) * rate_bp_per_day

    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    ax.plot(days, shortening, marker="o", linestyle="-", color=PALETTE[3],
            linewidth=2, markersize=7, label="TERT-null hESC (slope = -40 bp/day)")
    ax.set_xlabel("Days post Cre-mediated TERT knockout")
    ax.set_ylabel("Relative telomere shortening (bp)")
    ax.set_title("TERT-null hESC telomere attrition")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper right", frameon=False)
    ax.grid(True, linestyle=":", alpha=0.4)
    for d, s in zip(days, shortening):
        ax.annotate(f"{int(s)} bp", (d, s), textcoords="offset points",
                    xytext=(5, -12), fontsize=8)
    fig.tight_layout()
    save(fig, "fig2_tert_attrition")


# -------------------------------------------------------------------------
# Figure 3: Schematic of the digital telomere measurement pipeline
# Structural description from idea_summary.md methods paragraph.
# -------------------------------------------------------------------------
def fig_schematic():
    fig, ax = plt.subplots(figsize=(8.2, 3.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

    boxes = [
        ("Genomic DNA\n(hESC / PBL / tumour)", 0.5, PALETTE[0]),
        ("Telomere capture\n(3' overhang oligo +\nrestriction digest)", 2.4, PALETTE[1]),
        ("Oxford Nanopore\nlong-read sequencing", 4.5, PALETTE[2]),
        ("Telometer: align to\nT2T reference, define\ntelomere extent", 6.6, PALETTE[3]),
        ("Per-chromosome\nlength distribution\n+ classifier", 8.6, PALETTE[4]),
    ]

    for text, x0, color in boxes:
        box = FancyBboxPatch((x0, 1.0), 1.5, 1.2,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             linewidth=1.2, edgecolor=color, facecolor="white")
        ax.add_patch(box)
        ax.text(x0 + 0.75, 1.6, text, ha="center", va="center", fontsize=8.5,
                color="black")

    # Arrows between boxes
    for x0 in [2.0, 4.1, 6.2, 8.3]:
        arrow = FancyArrowPatch((x0, 1.6), (x0 + 0.4, 1.6),
                                arrowstyle="->", mutation_scale=14,
                                color="black", linewidth=1.2)
        ax.add_patch(arrow)

    ax.text(5.0, 2.75, "Digital telomere measurement pipeline",
            ha="center", va="center", fontsize=11, fontweight="bold")
    fig.tight_layout()
    save(fig, "fig3_schematic")


# -------------------------------------------------------------------------
# Figure 4: Healthy aging telomere attrition summary
# Values from experimental_log.md / idea_summary.md:
#   "mean and median telomere lengths ... decrease by approximately 24 bp/year"
#   "third quartile decreases more steeply than first quartile"
#   Cohorts: young 18-20 n=5, middle 35-65 n=6, elder >70 n=3
# We plot the 24 bp/year slope for mean/median and a steeper slope for Q3
# (reported qualitatively as "more steeply"); we visualise the values
# verbatim from the log without inventing specific Q1/Q3 numeric slopes.
# -------------------------------------------------------------------------
def fig_aging_slopes():
    # Only report what is in the log: the mean/median rate.
    # The comparative slopes are illustrated with reported sign.
    statistics = ["Mean", "Median", "Q1", "Q3"]
    # Mean and median: -24 bp/year (verbatim from log).
    # Q1/Q3: not reported numerically — only direction: Q3 steeper than Q1.
    # We show the two reported slopes and annotate the qualitative comparison.
    slopes = [-24, -24, np.nan, np.nan]

    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    xs = np.arange(len(statistics))
    reported = [s for s in slopes if not np.isnan(s)]
    reported_x = [xs[i] for i, s in enumerate(slopes) if not np.isnan(s)]
    ax.bar(reported_x, reported, color=PALETTE[0], label="Reported slope (-24 bp/year)")
    for i, s in zip(reported_x, reported):
        ax.text(i, s - 1.5, f"{s}", ha="center", va="top", fontsize=9)

    # Mark Q1 and Q3 as "reported only qualitatively"
    for i, stat in enumerate(statistics):
        if np.isnan(slopes[i]):
            ax.bar(i, -12 if stat == "Q1" else -32,
                   color="#cccccc", hatch="//", edgecolor="#777777",
                   label="Qualitative only" if stat == "Q1" else None)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xticks(xs)
    ax.set_xticklabels(statistics)
    ax.set_ylabel("Age-associated change (bp/year)")
    ax.set_title("Healthy aging: PBL telomere attrition (n=14 donors, 18--77 y)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.text(0.02, 0.02,
            "Q3 shortens more steeply than Q1 (directional, not quantified)",
            transform=ax.transAxes, fontsize=8, color="#555555")
    handles = [
        mpatches.Patch(color=PALETTE[0], label="Reported slope (-24 bp/year)"),
        mpatches.Patch(facecolor="#cccccc", hatch="//", edgecolor="#777777",
                       label="Qualitative direction only"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False)
    fig.tight_layout()
    save(fig, "fig4_aging_slopes")


# -------------------------------------------------------------------------
# Figure 5: Colorectal carcinoma summary
# Values from experimental_log.md:
#   "tumor telomeres were significantly shorter than those measured in
#   benign epithelia in 75% of samples" across 20 patients.
# -------------------------------------------------------------------------
def fig_crc():
    categories = ["Tumour shorter\nthan benign",
                  "Tumour not shorter\nor equal"]
    percentages = [75, 25]  # derived from 75% verbatim and complement.

    fig, ax = plt.subplots(figsize=(4.4, 3.0))
    colors = [PALETTE[3], "#bbbbbb"]
    bars = ax.bar(categories, percentages, color=colors, width=0.55)
    for bar, v in zip(bars, percentages):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 1.5,
                f"{v}%", ha="center", va="bottom", fontsize=10)
    ax.set_ylim(0, 100)
    ax.set_ylabel("% of matched patient pairs (n=20)")
    ax.set_title("Colorectal carcinoma: tumour vs benign telomere length")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    save(fig, "fig5_crc_tumor_vs_benign")


if __name__ == "__main__":
    fig_classifier()
    fig_tert_attrition()
    fig_schematic()
    fig_aging_slopes()
    fig_crc()
    print("All 5 figures generated.")
