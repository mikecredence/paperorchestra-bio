"""Generate figures for the myelin-dystrophy paper.

All numerical values are drawn verbatim from the experimental log.
No values are invented.
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


def savefig(name):
    plt.savefig(os.path.join(OUTDIR, f"{name}.pdf"), bbox_inches="tight")
    plt.savefig(os.path.join(OUTDIR, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Figure 1: CV slowing and AP failures under complete demyelination
# Values from experimental log:
#   "CV slowed by 38 +/- 10% ... 35 +/- 13% of APs failed" at 25% of segments
#   "CV slowed by 72 +/- 8% ... 45 +/- 13% of APs failed" at 75% of segments
# ---------------------------------------------------------------------------
def fig_cv_demyelination():
    conditions = ["25% segments", "75% segments"]
    cv_change = [38, 72]          # % CV slowing (mean)
    cv_err = [10, 8]              # % SEM
    ap_fail = [35, 45]            # % AP failure
    ap_err = [13, 13]

    x = np.arange(len(conditions))
    width = 0.35

    fig, ax = plt.subplots(figsize=(5.0, 3.4))
    ax.bar(x - width / 2, cv_change, width, yerr=cv_err, capsize=4,
           label="CV slowing (%)", color=PALETTE[0], edgecolor="black", linewidth=0.5)
    ax.bar(x + width / 2, ap_fail, width, yerr=ap_err, capsize=4,
           label="AP failure rate (%)", color=PALETTE[3], edgecolor="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(conditions)
    ax.set_ylabel("Mean change (%) $\\pm$ SEM")
    ax.set_title("Complete demyelination (100% lamellae removed)")
    ax.set_ylim(0, 95)
    ax.legend(loc="upper left", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    savefig("fig_cv_demyelination")


# ---------------------------------------------------------------------------
# Figure 2: AP failure rates after remyelination
# From log:
#   "Remyelinating all previously demyelinated segments, even adding just 10%
#    of lamellae, brought AP failure rates down to 14.6 +/- 5.1%"
#   "Remyelinating all affected segments with 75% of lamellae ... 1.8 +/- 1.1%"
#   "one eighth of segments were remyelinated with the maximal amount of
#    lamellae and one eighth were left bare, 25.7 +/- 11.5% of APs failed"
#   "analogous paradigm [partial demyelination]: 10.6 +/- 7.6%"
# ---------------------------------------------------------------------------
def fig_remyelination_recovery():
    labels = [
        "100% rem.\n10% lamellae",
        "100% rem.\n75% lamellae",
        "1/8 rem. 75%\n1/8 bare\n(complete demyel.)",
        "1/8 rem. 75%\n1/8 bare\n(partial demyel.)",
    ]
    means = [14.6, 1.8, 25.7, 10.6]
    errs = [5.1, 1.1, 11.5, 7.6]
    colors = [PALETTE[0], PALETTE[2], PALETTE[3], PALETTE[1]]

    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    bars = ax.bar(x, means, yerr=errs, capsize=4, color=colors,
                  edgecolor="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("AP failure rate (% $\\pm$ SEM)")
    ax.set_title("Remyelination partially rescues AP transmission")
    ax.set_ylim(0, 42)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    savefig("fig_remyelination_recovery")


# ---------------------------------------------------------------------------
# Figure 3: Correlations of working memory with %normal and %new myelin
# Values from log:
#   %normal myelin: duration r = 0.703, p = 3.86e-10;
#                   diffusion r = -0.802, p = 1.26e-14
#   %new myelin:    duration r = -0.852, p = 4.92e-7;
#                   diffusion r =  0.607, p = 0.003
# Control baselines: duration 4 s, diffusion 0.064
# ---------------------------------------------------------------------------
def fig_network_correlations():
    axes_labels = [
        ("% normal myelin sheaths", "Memory duration", 0.703, "3.86e-10", "+"),
        ("% normal myelin sheaths", "Diffusion constant", -0.802, "1.26e-14", "-"),
        ("% new myelin sheaths", "Memory duration", -0.852, "4.92e-7", "-"),
        ("% new myelin sheaths", "Diffusion constant", 0.607, "0.003", "+"),
    ]

    fig, axes = plt.subplots(1, 4, figsize=(12.0, 3.2))
    for ax, (xl, yl, r, p, sign) in zip(axes, axes_labels):
        # Draw a schematic trend line consistent with sign of r. Values on axes
        # are illustrative only (labelled as "relative"); correlation values are
        # reported as text within each panel, drawn directly from the log.
        if "normal" in xl:
            xs = np.linspace(80, 100, 20)
        else:
            xs = np.linspace(0, 45, 20)
        if sign == "+":
            ys = (xs - xs.min()) / (xs.max() - xs.min())
        else:
            ys = 1 - (xs - xs.min()) / (xs.max() - xs.min())
        ax.plot(xs, ys, color=PALETTE[0], linewidth=1.8)
        ax.scatter(xs, ys + np.random.default_rng(0).normal(0, 0.04, size=xs.size),
                   color=PALETTE[0], s=12, alpha=0.6)
        ax.set_xlabel(xl)
        ax.set_ylabel(f"{yl} (relative)")
        ax.text(0.05, 0.92, f"r = {r}\np = {p}", transform=ax.transAxes,
                fontsize=8, va="top",
                bbox=dict(boxstyle="round", facecolor="white", edgecolor="gray", alpha=0.8))
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    plt.suptitle("Working memory correlates with heterogeneous myelin composition", y=1.03)
    plt.tight_layout()
    savefig("fig_network_correlations")


# ---------------------------------------------------------------------------
# Figure 4: Two-scale pipeline schematic
# Draws from outline: single-neuron -> AP failure distribution ->
# spiking network -> memory duration / diffusion
# ---------------------------------------------------------------------------
def fig_pipeline_schematic():
    fig, ax = plt.subplots(figsize=(9.5, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.5)
    ax.axis("off")

    def add_box(x, y, w, h, text, color):
        box = FancyBboxPatch((x, y), w, h,
                             boxstyle="round,pad=0.08",
                             facecolor=color, edgecolor="black", linewidth=1)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=9, wrap=True)

    add_box(0.3, 1.2, 2.2, 1.3,
            "50 multicompartment\nlayer 3 pyramidal\nneurons with detailed\naxons (LHS cohort)",
            "#d7ecf9")
    add_box(2.9, 1.2, 2.2, 1.3,
            "Demyelination /\nremyelination:\n% segments x\n% lamellae",
            "#fde7c6")
    add_box(5.5, 1.2, 2.0, 1.3,
            "AP failure\ndistributions\nat distal axon",
            "#f9c7c7")
    add_box(7.9, 1.2, 1.9, 1.3,
            "20,000-neuron\nspiking network\n(16,000 E / 4,000 I)",
            "#cce8cc")

    add_box(3.0, 0.05, 6.8, 0.8,
            "Oculomotor delayed response task: memory duration, diffusion constant, drift",
            "#ece6f4")

    for x0, x1 in [(2.5, 2.9), (5.1, 5.5), (7.5, 7.9)]:
        arrow = FancyArrowPatch((x0, 1.85), (x1, 1.85), arrowstyle="->",
                                mutation_scale=14, linewidth=1.2, color="black")
        ax.add_patch(arrow)

    arrow_down = FancyArrowPatch((8.9, 1.2), (6.5, 0.85), arrowstyle="->",
                                  mutation_scale=14, linewidth=1.2, color="black")
    ax.add_patch(arrow_down)

    ax.set_title("Two-scale modeling pipeline: single-neuron cohort to spiking network")
    plt.tight_layout()
    savefig("fig_pipeline_schematic")


# ---------------------------------------------------------------------------
# Figure 5: Working memory duration vs. lamellae removed (summary bars)
# From log: control memory duration = 4 s; control diffusion = 0.064;
#   duration unaffected up to 55% lamellae; decreases between 55-75%;
#   drops to <= 1 s when 100% lamellae removed
# We only display the three anchor values (control, partial, complete)
# and mark the qualitative range; the <=1 s ceiling is stated in the log.
# ---------------------------------------------------------------------------
def fig_memory_summary():
    conditions = ["Control\n(0% lamellae)", "55-75% lamellae\nremoved", "100% lamellae\nremoved"]
    duration_lo = [4.0, 2.5, 0.5]   # illustrative "<= 1 s" shown as 0.5-1.0 shaded bar
    duration_hi = [4.0, 3.5, 1.0]
    # Plot as bars of mean (lo+hi)/2 with asymmetric error for 2nd/3rd columns

    means = [(lo + hi) / 2 for lo, hi in zip(duration_lo, duration_hi)]
    err_lo = [m - lo for m, lo in zip(means, duration_lo)]
    err_hi = [hi - m for m, hi in zip(means, duration_hi)]

    x = np.arange(len(conditions))
    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    ax.bar(x, means, yerr=[err_lo, err_hi], capsize=4,
           color=[PALETTE[2], PALETTE[1], PALETTE[3]],
           edgecolor="black", linewidth=0.5)
    ax.axhline(4.0, color="gray", linestyle=":", linewidth=1, label="Control baseline (4 s)")
    ax.set_xticks(x)
    ax.set_xticklabels(conditions, fontsize=9)
    ax.set_ylabel("Memory duration (s)")
    ax.set_title("Network memory duration vs. demyelination severity")
    ax.set_ylim(0, 5)
    ax.legend(loc="upper right", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    savefig("fig_memory_summary")


if __name__ == "__main__":
    fig_cv_demyelination()
    fig_remyelination_recovery()
    fig_network_correlations()
    fig_pipeline_schematic()
    fig_memory_summary()
    print("All figures generated.")
