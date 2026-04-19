"""Generate figures for the translational AxCaliber paper.

All numbers used here are taken verbatim from inputs/experimental_log.md.
No values are fabricated; where a figure requires raw pixel/image data that
was not present in the extraction (e.g., TBSS brain slices, tractography
renderings, microscopy images), a placeholder panel is produced.
"""
from __future__ import annotations

import os
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

HERE = Path(__file__).resolve().parent
os.chdir(HERE.parent)  # so relative paths land inside the workspace

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})
PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


def save(fig, stem: str) -> None:
    fig.tight_layout()
    fig.savefig(f"figures/{stem}.pdf")
    fig.savefig(f"figures/{stem}.png", dpi=220)
    plt.close(fig)


# ----------------------------------------------------------------------------
# Figure 1 -- Schematic of the translational pipeline (SCHEMATIC)
# Values used verbatim from experimental_log.md
# ----------------------------------------------------------------------------
def fig_pipeline_schematic() -> None:
    fig, ax = plt.subplots(figsize=(7.0, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.2)
    ax.axis("off")

    def box(x, y, w, h, text, color):
        p = mpatches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.04",
            linewidth=1.1, edgecolor="black", facecolor=color)
        ax.add_patch(p)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=9, wrap=True)

    def arrow(x0, y0, x1, y1):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", lw=1.1, color="black"))

    # Preclinical row
    box(0.1, 2.6, 2.2, 1.1,
        "Rat model\nn=9, ibotenic acid\n2.5 ug/ul, 1 ul\nbregma -3.8 mm",
        "#e8f1fa")
    box(2.6, 2.6, 2.2, 1.1,
        "7T Bruker BioSpect\n31 dirs\nb=2000/4000\n$\\Delta$=15/25/40/60 ms",
        "#e8f1fa")
    box(5.1, 2.6, 2.2, 1.1,
        "AxCaliber\n(crossing-fiber)\nfimbria diameter",
        "#e8f1fa")
    box(7.6, 2.6, 2.2, 1.1,
        "Histology\nNeuN / NF / MBP\nICY quantification",
        "#e8f1fa")

    # Clinical row
    box(0.1, 0.6, 2.2, 1.1,
        "MS cohort\n10 RRMS (7F)\n6 controls (3F)\nage p=0.093 (MWU)",
        "#fdecd7")
    box(2.6, 0.6, 2.2, 1.1,
        "3T Connectom\n91 dirs, 300 mT/m\n$b$=2000/4000\n$\\Delta$=17/35/61 ms",
        "#fdecd7")
    box(5.1, 0.6, 2.2, 1.1,
        "Whole-brain\nAxCaliber\n+ lesion masks",
        "#fdecd7")
    box(7.6, 0.6, 2.2, 1.1,
        "TBSS + GLM\nNAWM & lesion\n(T1 iso / hypo)",
        "#fdecd7")

    arrow(2.3, 3.15, 2.6, 3.15)
    arrow(4.8, 3.15, 5.1, 3.15)
    arrow(7.3, 3.15, 7.6, 3.15)
    arrow(2.3, 1.15, 2.6, 1.15)
    arrow(4.8, 1.15, 5.1, 1.15)
    arrow(7.3, 1.15, 7.6, 1.15)

    # translation arrow
    arrow(6.2, 2.58, 6.2, 1.72)
    ax.text(6.35, 2.15, "translation", fontsize=8.5, style="italic")

    ax.text(0.1, 3.85, "Preclinical validation", fontsize=10.5, weight="bold")
    ax.text(0.1, 1.85, "Clinical application", fontsize=10.5, weight="bold")

    save(fig, "fig1_pipeline")


# ----------------------------------------------------------------------------
# Figure 2 -- Rat preclinical ANOVA statistics (DATA-GROUNDED)
# Source lines:
#  "F1,7=19.5, p=0.003"  injection main effect
#  "F98,686=219.5, p<0.001"  position main effect (rescaled for log axis)
#  "F98,686=11.2, p=0.012"  interaction
#  paired t p=0.003 (fimbria diameter), p=0.026 (NeuN), p=0.047 (NF)
#  correlation r=0.54, p=0.029
# ----------------------------------------------------------------------------
def fig_rat_stats() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.2))

    # Left: ANOVA F-statistics on log scale
    effects = ["Injection\n(F1,7)", "Position\n(F98,686)", "Inj x Pos\n(F98,686)"]
    F = [19.5, 219.5, 11.2]
    bars = ax1.bar(effects, F, color=[PALETTE[0], PALETTE[1], PALETTE[2]],
                   edgecolor="black", linewidth=0.6)
    ax1.set_yscale("log")
    ax1.set_ylabel("F statistic (log scale)")
    ax1.set_title("RM-ANOVA on fimbria axonal diameter")
    for b, f, p in zip(bars, F, ["p=0.003", "p<0.001", "p=0.012"]):
        ax1.text(b.get_x() + b.get_width() / 2, f * 1.15, f"{p}",
                 ha="center", va="bottom", fontsize=8.5)
    ax1.set_ylim(top=700)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.grid(axis="y", which="major", ls=":", lw=0.6, alpha=0.5)

    # Right: paired t-test p-values (plot -log10 p so shorter bars are ns)
    tests = ["Fimbria\ndiameter", "NeuN\n(hippo)", "NF-M\n(fimbria)", "MRI vs NF\ncorr"]
    pvals = [0.003, 0.026, 0.047, 0.029]
    neglog = [-np.log10(p) for p in pvals]
    colors = [PALETTE[0], PALETTE[3], PALETTE[2], PALETTE[4]]
    bars2 = ax2.bar(tests, neglog, color=colors, edgecolor="black", linewidth=0.6)
    ax2.axhline(-np.log10(0.05), color="black", ls="--", lw=0.8, label="p=0.05")
    ax2.set_ylabel("-log10(p)")
    ax2.set_title("Preclinical validation tests")
    for b, p in zip(bars2, pvals):
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.05,
                 f"p={p}", ha="center", va="bottom", fontsize=8.5)
    ax2.legend(loc="upper right", frameon=False)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    save(fig, "fig2_rat_stats")


# ----------------------------------------------------------------------------
# Figure 3 -- MS clinical GLM (DATA-GROUNDED)
#  group effect F1,235=25.7, p<0.001
#  group x lesion-type F1,235=40.1, p=0.03
#  post-hoc hypointense p<0.01; isointense n.s.
#  NIA one-sample t p<0.001
# ----------------------------------------------------------------------------
def fig_ms_glm() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.3))

    # Left: GLM F-statistics
    effects = ["Group\n(F1,235)", "Group x lesion\ntype (F1,235)"]
    F = [25.7, 40.1]
    bars = ax1.bar(effects, F, color=[PALETTE[0], PALETTE[3]],
                   edgecolor="black", linewidth=0.6)
    ax1.set_ylabel("F statistic")
    ax1.set_title("Lesion GLM (MS vs healthy cohort)")
    for b, f, p in zip(bars, F, ["p<0.001", "p=0.03"]):
        ax1.text(b.get_x() + b.get_width() / 2, f + 1.0, p,
                 ha="center", va="bottom", fontsize=9)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_ylim(0, max(F) * 1.2)

    # Right: post-hoc pattern across lesion types (categorical)
    lesion_types = ["T1 isointense", "T1 hypointense"]
    # The log encodes: hypo p<0.01 with significantly higher axon diameter in lesion
    # vs matched healthy region; iso n.s. We plot as a relative "lesion minus
    # healthy-cohort" effect using only the sign+significance reported, not any
    # fabricated magnitude: represented on an ordinal axis.
    sig_level = [0, 1]  # 0 = n.s., 1 = p<0.01
    bars2 = ax2.bar(lesion_types, sig_level, color=[PALETTE[1], PALETTE[3]],
                    edgecolor="black", linewidth=0.6)
    ax2.set_yticks([0, 1])
    ax2.set_yticklabels(["n.s.", "p<0.01"])
    ax2.set_ylabel("Post-hoc significance\n(lesion > healthy cohort)")
    ax2.set_title("Lesion-type-selective effect")
    for b, lab in zip(bars2, ["n.s.", "p<0.01"]):
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.03,
                 lab, ha="center", va="bottom", fontsize=9, weight="bold")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_ylim(0, 1.35)

    save(fig, "fig3_ms_glm")


# ----------------------------------------------------------------------------
# Figure 4 -- MRI-histology correlation: schematic depiction
# We only have: r=0.54, p=0.029. We do NOT fabricate individual points.
# Show an annotated summary panel.
# ----------------------------------------------------------------------------
def fig_mri_histology_correlation() -> None:
    fig, ax = plt.subplots(figsize=(4.5, 3.3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Axes skeleton
    ax_in = fig.add_axes([0.18, 0.18, 0.72, 0.68])
    ax_in.set_xlabel("Neurofilament fluorescence intensity (a.u.)")
    ax_in.set_ylabel("AxCaliber axon diameter (a.u.)")
    ax_in.set_title("MRI vs histology (n=9 rats, both hemispheres)")
    ax_in.set_xticks([])
    ax_in.set_yticks([])
    ax_in.spines["top"].set_visible(False)
    ax_in.spines["right"].set_visible(False)

    # Draw a conceptual positive trend line (no data points fabricated)
    xs = np.linspace(0.05, 0.95, 100)
    ys = 0.15 + 0.7 * xs
    ax_in.plot(xs, ys, color=PALETTE[0], lw=1.6)
    ax_in.fill_between(xs, ys - 0.12, ys + 0.12, color=PALETTE[0], alpha=0.15)
    ax_in.set_xlim(0, 1)
    ax_in.set_ylim(0, 1)
    ax_in.text(0.04, 0.92, "r = 0.54\np = 0.029",
               fontsize=11, weight="bold",
               bbox=dict(boxstyle="round", facecolor="white",
                         edgecolor="black", lw=0.6))
    ax_in.text(0.98, 0.04,
               "Schematic; exact point cloud not provided in extraction",
               fontsize=7, style="italic", ha="right", color="gray")

    save(fig, "fig4_mri_histology")


# ----------------------------------------------------------------------------
# Figure 5 -- TBSS / brain maps PLACEHOLDER
# We do not have the raw TBSS statistic maps; mark clearly as placeholder.
# ----------------------------------------------------------------------------
def fig_tbss_placeholder() -> None:
    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    ax.axis("off")
    ax.text(0.5, 0.5,
            "[Placeholder]\n\n"
            "TBSS voxelwise map of increased axonal diameter\n"
            "in MS NAWM vs controls (p<0.05, corrected).\n"
            "Symmetric effects across CC, internal capsule,\n"
            "corona radiata, thalamic radiation, ILF, cingulum,\n"
            "fornix, SLF, IFOF, uncinate, tapetum.\n\n"
            "Raw statistic volumes were not present in the extraction.",
            ha="center", va="center", fontsize=9.5, color="#333333",
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#f2f2f2",
                      edgecolor="gray", lw=0.8))
    save(fig, "fig5_tbss_placeholder")


if __name__ == "__main__":
    Path("figures").mkdir(exist_ok=True)
    fig_pipeline_schematic()
    fig_rat_stats()
    fig_ms_glm()
    fig_mri_histology_correlation()
    fig_tbss_placeholder()
    print("Generated 5 figures in figures/")
