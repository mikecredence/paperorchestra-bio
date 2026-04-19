"""
Figure generator for the chronic negative-engram paper.

All numerical values used here come directly from the experimental log.
No raw means/SEMs for individual conditions were provided in the
extraction, so behavioral and glial panels are summarized as:
  - significance-level plots (p-values and F-statistics from the
    two-way ANOVA and Tukey/Sidak post-hocs that ARE in the extraction),
  - schematic diagrams of the experimental design, and
  - placeholder panels for raw microscopy.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


def save(fig, name):
    fig.savefig(f"{name}.pdf", bbox_inches="tight")
    fig.savefig(f"{name}.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ----------------------------------------------------------------------
# Figure 1: Experimental design schematic (TRAP2 tagging + chronic DCZ).
# ----------------------------------------------------------------------
def fig_schematic():
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

    # Timeline arrow
    ax.annotate("", xy=(9.8, 0.6), xytext=(0.2, 0.6),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.4))
    ax.text(5.0, 0.25, "time (months)", ha="center", va="top", fontsize=9)

    stages = [
        (0.2, "AAV-DIO-\nhM3Dq-mCherry\n(or mCherry)\nvCA1, bilateral"),
        (2.2, "CFC + 4-OHT\n(tag negative\nengram)"),
        (4.4, "DCZ in H$_2$O\n3 $\\mu$g/kg/day\n(3 months)"),
        (7.2, "Behavioral battery\nOF, ZM, Y-maze,\nrecall, extinction,\ngeneralization"),
        (9.3, "Histology\nIba1, GFAP, NeuN"),
    ]
    for x, label in stages:
        box = FancyBboxPatch((x, 1.0), 1.7, 1.6,
                             boxstyle="round,pad=0.05",
                             linewidth=1.2,
                             edgecolor=PALETTE[0], facecolor="#eaf2fb")
        ax.add_patch(box)
        ax.text(x + 0.85, 1.8, label, ha="center", va="center", fontsize=8.5)
        ax.plot(x + 0.85, 0.6, "ko", markersize=4)

    # Cohorts
    ax.text(0.2, 2.85, "Young cohort: 3 mo $\\rightarrow$ 6 mo at endpoint   |   "
                      "Aged cohort: 11 mo $\\rightarrow$ 14 mo at endpoint",
            fontsize=9, color="black")

    return fig


# ----------------------------------------------------------------------
# Figure 2: Behavioral summary - group ANOVA F and p values.
# All numbers below come verbatim from the experimental log statistical_sentences.
# ----------------------------------------------------------------------
def fig_behavior_summary():
    # (assay, F-stat, p-value (Group effect), label-short)
    rows = [
        ("Open field\n(center time)",    29.56, 0.00005),  # p<0.0001 reported
        ("Zero maze\n(open-arm time)",   40.22, 0.00005),  # p<0.0001 reported
        ("Y-maze\n(% spont. alt.)",       7.517, 0.0091),
        ("Generalization\n(Ctx B freezing)", 26.53, 0.00005),
        ("Extinction 6MO\n(freezing)",    5.494, 0.0315),
        ("Remote recall 6MO\n(freezing)", 6.588, 0.0200),
    ]
    labels = [r[0] for r in rows]
    fvals = np.array([r[1] for r in rows])
    pvals = np.array([r[2] for r in rows])
    neglogp = -np.log10(pvals)

    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    bars = ax.barh(labels, neglogp,
                   color=[PALETTE[0] if p <= 0.05 else "#aaaaaa" for p in pvals],
                   edgecolor="black", linewidth=0.5)
    # annotate with F and p
    for bar, f, p in zip(bars, fvals, pvals):
        xt = bar.get_width()
        txt = f"F={f:g},  p={'<0.0001' if p < 0.0001 else f'{p:.4f}'}"
        ax.text(xt + 0.1, bar.get_y() + bar.get_height() / 2,
                txt, va="center", fontsize=8.5)

    ax.axvline(-np.log10(0.05), color="red", linestyle="--", linewidth=1,
               label=r"$p=0.05$")
    ax.set_xlabel(r"$-\log_{10}(p)$ for Group effect")
    ax.set_title("Effect of chronic negative-engram activation (Group: hM3Dq vs mCherry)")
    ax.legend(loc="lower right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.invert_yaxis()
    plt.tight_layout()
    return fig


# ----------------------------------------------------------------------
# Figure 3: Glial cell count and morphology - Group ANOVA summary.
# All F/p values from the experimental log.
# ----------------------------------------------------------------------
def fig_glia_summary():
    # (cell, measure, F(1,8), p, age-specific significance note)
    rows = [
        ("Iba1+ count",            13.42,  0.0064),
        ("Iba1 ramification",      15.11,  0.0046),
        ("Iba1 territory vol.",    16.45,  0.0037),
        ("Iba1 min branch len.",    7.470, 0.0257),
        ("Iba1 max branch len.",    8.964, 0.0172),
        ("GFAP+ count",            26.95,  0.0008),
        ("GFAP avg branch len.",   32.75,  0.0004),
        ("GFAP max branch len.",   41.82,  0.0002),
        ("GFAP min branch len.",   16.26,  0.0038),
    ]
    labels = [r[0] for r in rows]
    fvals  = np.array([r[1] for r in rows])
    pvals  = np.array([r[2] for r in rows])
    neglogp = -np.log10(pvals)

    colors = [PALETTE[2] if "GFAP" in lab else PALETTE[3] for lab in labels]

    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    bars = ax.barh(labels, neglogp, color=colors,
                   edgecolor="black", linewidth=0.5)
    for bar, f, p in zip(bars, fvals, pvals):
        ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height() / 2,
                f"F={f:g},  p={p:.4f}", va="center", fontsize=8.5)
    ax.axvline(-np.log10(0.05), color="red", linestyle="--", linewidth=1,
               label=r"$p=0.05$")
    ax.set_xlabel(r"$-\log_{10}(p)$ for Group effect (hM3Dq vs mCherry)")
    ax.set_title("Glial remodeling in hippocampus after 3 mo of engram activation")
    # legend with cell-type color
    handles = [mpatches.Patch(color=PALETTE[3], label="Microglia (Iba1+)"),
               mpatches.Patch(color=PALETTE[2], label="Astrocytes (GFAP+)"),
               mpatches.Patch(color="red", label=r"$p=0.05$ threshold")]
    ax.legend(handles=handles, loc="lower right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.invert_yaxis()
    plt.tight_layout()
    return fig


# ----------------------------------------------------------------------
# Figure 4: Age-by-group interaction summary (per-age Tukey p-values).
# All Tukey p-values from the experimental log.
# ----------------------------------------------------------------------
def fig_age_by_group():
    # Each row is a measure; columns are 6MO and 14MO mCherry-vs-hM3Dq Tukey p.
    rows = [
        ("Open field (center time)",      0.0049, 0.0016),
        ("Zero maze (open-arm time)",     0.0002, 0.0007),
        ("Y-maze (% alternation)",        0.9634, 0.0045),
        ("Generalization (Ctx B freeze)", 0.0053, 0.0026),
        ("Iba1+ cell count",              0.9906, 0.0113),
        ("GFAP+ cell count",              0.0328, 0.0208),
        ("Iba1 ramification index",       0.3513, 0.0324),
        ("GFAP avg branch length",        0.0228, 0.0109),
    ]

    labels   = [r[0] for r in rows]
    p6       = np.array([r[1] for r in rows])
    p14      = np.array([r[2] for r in rows])
    y        = np.arange(len(labels))
    width    = 0.4

    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    b1 = ax.barh(y - width/2, -np.log10(p6),  height=width,
                 color=PALETTE[0], edgecolor="black", linewidth=0.5,
                 label="6MO (mCherry vs hM3Dq)")
    b2 = ax.barh(y + width/2, -np.log10(p14), height=width,
                 color=PALETTE[1], edgecolor="black", linewidth=0.5,
                 label="14MO (mCherry vs hM3Dq)")

    for bars, ps in [(b1, p6), (b2, p14)]:
        for bar, p in zip(bars, ps):
            ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                    f"p={p:.4f}", va="center", fontsize=8)

    ax.axvline(-np.log10(0.05), color="red", linestyle="--", linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel(r"$-\log_{10}(p)$  (Tukey post-hoc, mCherry vs hM3Dq)")
    ax.set_title("Age-dependence of chronic negative-engram activation effects")
    ax.legend(loc="lower right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.invert_yaxis()
    plt.tight_layout()
    return fig


# ----------------------------------------------------------------------
# Figure 5: Neuronal-count safety placeholder (report all ns from log).
# ----------------------------------------------------------------------
def fig_neun_ns():
    regions = ["Subiculum", "Ventral DG", "Ventral CA1"]
    groupF  = [0.00721, 0.0524, 2.947]   # Group F-stats from log
    groupP  = [0.9344,  0.8246, 0.1244]  # Group p-vals from log

    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.2))

    ax = axes[0]
    ax.bar(regions, groupF, color=PALETTE[4], edgecolor="black", linewidth=0.5)
    for r, f in zip(regions, groupF):
        ax.text(r, f + 0.08, f"F={f:.3g}", ha="center", fontsize=8.5)
    ax.set_ylabel("Group F(1,8)")
    ax.set_title("NeuN+ two-way ANOVA: Group F")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax = axes[1]
    ax.bar(regions, -np.log10(groupP), color=PALETTE[4],
           edgecolor="black", linewidth=0.5)
    for r, p in zip(regions, groupP):
        ax.text(r, -np.log10(p) + 0.03, f"p={p:.4f}", ha="center", fontsize=8.5)
    ax.axhline(-np.log10(0.05), color="red", linestyle="--", linewidth=1,
               label=r"$p=0.05$")
    ax.set_ylabel(r"$-\log_{10}(p)$")
    ax.set_title("NeuN+ Group p-value (all ns)")
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    return fig


# ----------------------------------------------------------------------
# Figure 6: Microscopy placeholder (data not in extraction).
# ----------------------------------------------------------------------
def fig_microscopy_placeholder():
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 4.6))
    panels = [
        "6MO mCherry\nIba1 / GFAP imaging",
        "6MO hM3Dq\nIba1 / GFAP imaging",
        "14MO mCherry\nIba1 / GFAP imaging",
        "14MO hM3Dq\nIba1 / GFAP imaging",
    ]
    for ax, lab in zip(axes.flat, panels):
        ax.text(0.5, 0.5,
                f"[Figure placeholder]\n{lab}\nRaw microscopy not in extraction",
                ha="center", va="center", fontsize=9.5, color="gray",
                bbox=dict(boxstyle="round", facecolor="#f0f0f0", edgecolor="gray"))
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    save(fig_schematic(),              "fig1_design_schematic")
    save(fig_behavior_summary(),       "fig2_behavior_summary")
    save(fig_age_by_group(),           "fig3_age_by_group_tukey")
    save(fig_glia_summary(),           "fig4_glia_summary")
    save(fig_neun_ns(),                "fig5_neun_safety")
    save(fig_microscopy_placeholder(), "fig6_microscopy_placeholder")
    print("All figures generated.")
