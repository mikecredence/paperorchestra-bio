"""
Generate publication-quality figures for the AI-accelerated virtual screening paper.
All plotted values come verbatim from the experimental log.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

# Academic figure standards
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Output directory
OUTDIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------
# Figure 1: CASF-2016 Screening Power EF1% (bar chart, data-grounded)
# Source: "EF1%=16.72 ... second-best method (EF1%=11.9)"
# ---------------------------------------------------------------
def fig_casf_ef1():
    methods = ["RosettaGenFF-VS", "Second-best\nmethod"]
    ef1 = [16.72, 11.9]

    fig, ax = plt.subplots(figsize=(4.0, 3.2))
    bars = ax.bar(methods, ef1, color=[PALETTE[0], PALETTE[1]], width=0.55, edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Top 1% Enrichment Factor (EF$_{1\\%}$)")
    ax.set_title("CASF-2016 Screening Power")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 20)

    # Value labels on bars
    for bar, val in zip(bars, ef1):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.4,
                f"{val}", ha="center", va="bottom", fontsize=10, fontweight="bold")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "fig_casf_ef1.pdf"))
    plt.savefig(os.path.join(OUTDIR, "fig_casf_ef1.png"), dpi=200)
    plt.close()
    print("  [OK] fig_casf_ef1")


# ---------------------------------------------------------------
# Figure 2: Active-learning binding affinity improvement (bar chart, data-grounded)
# KLHDC2: -6.81 (iter 1) -> -12.43 (iter 10)
# NaV1.7: -10.8 (iter 1) -> -18.2 (final iter)
# ---------------------------------------------------------------
def fig_active_learning():
    campaigns = ["KLHDC2", "NaV1.7"]
    iter1 = [-6.81, -10.8]
    final = [-12.43, -18.2]

    x = np.arange(len(campaigns))
    width = 0.32

    fig, ax = plt.subplots(figsize=(4.5, 3.2))
    bars1 = ax.bar(x - width / 2, iter1, width, label="Iteration 1",
                   color=PALETTE[0], edgecolor="black", linewidth=0.5)
    bars2 = ax.bar(x + width / 2, final, width, label="Final iteration",
                   color=PALETTE[1], edgecolor="black", linewidth=0.5)

    ax.set_ylabel("Predicted binding affinity (kcal/mol)")
    ax.set_title("Active-Learning Convergence")
    ax.set_xticks(x)
    ax.set_xticklabels(campaigns)
    ax.legend(loc="lower left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(-22, 0)

    # Value labels
    for bar, val in zip(list(bars1) + list(bars2), iter1 + final):
        ax.text(bar.get_x() + bar.get_width() / 2, val - 0.6,
                f"{val}", ha="center", va="top", fontsize=8, fontweight="bold")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "fig_active_learning.pdf"))
    plt.savefig(os.path.join(OUTDIR, "fig_active_learning.png"), dpi=200)
    plt.close()
    print("  [OK] fig_active_learning")


# ---------------------------------------------------------------
# Figure 3: Campaign hit rates (grouped bar chart, data-grounded)
# KLHDC2: ~5.5B library, 6M docked (0.11%), 7 hits, 14% hit rate
# NaV1.7: ~4.1B library, 4.5M docked (0.11%), 4 hits, 44.4% hit rate
# ---------------------------------------------------------------
def fig_hit_rates():
    campaigns = ["KLHDC2", "NaV1.7"]
    hit_rates = [14.0, 44.4]
    n_hits = [7, 4]

    fig, ax = plt.subplots(figsize=(4.0, 3.2))
    bars = ax.bar(campaigns, hit_rates, color=[PALETTE[2], PALETTE[3]],
                  width=0.5, edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Hit rate (%)")
    ax.set_title("Virtual Screening Hit Rates")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 55)

    for bar, rate, n in zip(bars, hit_rates, n_hits):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.0,
                f"{rate}%\n({n} hits)", ha="center", va="bottom", fontsize=9, fontweight="bold")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "fig_hit_rates.pdf"))
    plt.savefig(os.path.join(OUTDIR, "fig_hit_rates.png"), dpi=200)
    plt.close()
    print("  [OK] fig_hit_rates")


# ---------------------------------------------------------------
# Figure 4: NaV1.7 IC50 values with confidence intervals (data-grounded)
# Z8739902234 inactivated: 1.32 (1.14-1.55)
# Z8739902234 resting: 13.1 (12.78-13.45)
# Z8739902234 NaV1.5: 5.14 (4.74-5.55)
# Z8739902234 hERG: 6.27 (5.27-7.37)
# Z8739905023 inactivated: 2.23 (2.14-2.46)
# ---------------------------------------------------------------
def fig_nav17_ic50():
    labels = [
        "Z...234\nNaV1.7\n(inact.)",
        "Z...234\nNaV1.7\n(rest.)",
        "Z...234\nNaV1.5",
        "Z...234\nhERG",
        "Z...023\nNaV1.7\n(inact.)",
    ]
    ic50 = [1.32, 13.1, 5.14, 6.27, 2.23]
    ci_lo = [1.14, 12.78, 4.74, 5.27, 2.14]
    ci_hi = [1.55, 13.45, 5.55, 7.37, 2.46]

    errors_lo = [v - lo for v, lo in zip(ic50, ci_lo)]
    errors_hi = [hi - v for v, hi in zip(ic50, ci_hi)]

    colors = [PALETTE[0], PALETTE[0], PALETTE[1], PALETTE[4], PALETTE[3]]

    fig, ax = plt.subplots(figsize=(6.0, 3.5))
    x = np.arange(len(labels))
    bars = ax.bar(x, ic50, color=colors, width=0.55, edgecolor="black", linewidth=0.5,
                  yerr=[errors_lo, errors_hi], capsize=4, error_kw={"linewidth": 1.2})

    ax.set_ylabel("IC$_{50}$ ($\\mu$M)")
    ax.set_title("NaV1.7 Lead Compound Potency and Selectivity")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 17)

    for xi, val, hi in zip(x, ic50, ci_hi):
        ax.text(xi, hi + 0.4, f"{val}", ha="center", va="bottom", fontsize=8, fontweight="bold")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "fig_nav17_ic50.pdf"))
    plt.savefig(os.path.join(OUTDIR, "fig_nav17_ic50.png"), dpi=200)
    plt.close()
    print("  [OK] fig_nav17_ic50")


# ---------------------------------------------------------------
# Figure 5: OpenVS pipeline schematic (schematic)
# Based on: "OpenVS platform uses active-learning surrogate training"
# VSX -> surrogate -> VSH -> filter/cluster -> synthesis -> assay
# ---------------------------------------------------------------
def fig_pipeline_schematic():
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

    fig, ax = plt.subplots(figsize=(7.0, 2.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2.5)
    ax.axis("off")

    boxes = [
        (0.2, 0.8, "Ultra-large\nlibrary\n(billions)"),
        (1.8, 0.8, "Active-learning\nsurrogate\n(NN triage)"),
        (3.4, 0.8, "VSX\n(fast dock)"),
        (5.0, 0.8, "VSH\n(flexible\nreceptor)"),
        (6.6, 0.8, "Filter &\ncluster"),
        (8.2, 0.8, "Synthesis\n& assay"),
    ]

    box_w = 1.3
    box_h = 1.0
    colors = [PALETTE[0], PALETTE[1], PALETTE[2], PALETTE[3], PALETTE[4], "#888888"]

    for (bx, by, txt), c in zip(boxes, colors):
        patch = FancyBboxPatch((bx, by), box_w, box_h, boxstyle="round,pad=0.05",
                               facecolor=c, edgecolor="black", linewidth=1.0, alpha=0.25)
        ax.add_patch(patch)
        ax.text(bx + box_w / 2, by + box_h / 2, txt, ha="center", va="center",
                fontsize=7.5, fontweight="bold")

    # Arrows
    for i in range(len(boxes) - 1):
        x_start = boxes[i][0] + box_w
        x_end = boxes[i + 1][0]
        y_mid = boxes[i][1] + box_h / 2
        ax.annotate("", xy=(x_end, y_mid), xytext=(x_start, y_mid),
                     arrowprops=dict(arrowstyle="->", color="black", lw=1.5))

    ax.set_title("OpenVS Platform Pipeline", fontsize=11, fontweight="bold", pad=8)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "fig_pipeline.pdf"))
    plt.savefig(os.path.join(OUTDIR, "fig_pipeline.png"), dpi=200)
    plt.close()
    print("  [OK] fig_pipeline (schematic)")


# ---------------------------------------------------------------
# Run all
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("Generating figures...")
    fig_casf_ef1()
    fig_active_learning()
    fig_hit_rates()
    fig_nav17_ic50()
    fig_pipeline_schematic()
    print(f"Done. All figures saved to {OUTDIR}")
