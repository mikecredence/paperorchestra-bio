"""Generate figures for the Biome biodiversity-monitoring manuscript.

Every numeric value is taken verbatim from the experimental log
(inputs/experimental_log.md).  No values are fabricated.
"""
from __future__ import annotations

import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

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


def save(fig: plt.Figure, name: str) -> None:
    pdf_path = os.path.join(HERE, f"{name}.pdf")
    png_path = os.path.join(HERE, f"{name}.png")
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1: training records required to reach Boyce Index > 0.9
#
# Source (experimental_log.md):
#   "BI ... exceeds 0.9 with 294 +/- 471 records (mean +/- SD across all
#    species) in the Biome+Traditional data, whereas the Traditional survey
#    data requires 2,129 +/- 4,157 records to achieve the same accuracy."
#   "2,336 +/- 3,718 Traditional survey records were required to exceed 0.9
#    of BI, only 338 +/- 571 were required for Biome+Traditional data."
# ---------------------------------------------------------------------------
def figure_records_to_bi09() -> None:
    categories = ["All species (n=132)", "Endangered species"]
    traditional_mean = [2129.0, 2336.0]
    traditional_sd = [4157.0, 3718.0]
    blended_mean = [294.0, 338.0]
    blended_sd = [471.0, 571.0]

    x = np.arange(len(categories))
    width = 0.38

    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    bars_t = ax.bar(
        x - width / 2,
        traditional_mean,
        width,
        yerr=traditional_sd,
        label="Traditional",
        color=PALETTE[0],
        capsize=3,
        edgecolor="black",
        linewidth=0.5,
    )
    bars_b = ax.bar(
        x + width / 2,
        blended_mean,
        width,
        yerr=blended_sd,
        label="Biome + Traditional (50% Biome)",
        color=PALETTE[2],
        capsize=3,
        edgecolor="black",
        linewidth=0.5,
    )

    # annotate with the exact mean values
    for bars, values in ((bars_t, traditional_mean), (bars_b, blended_mean)):
        for rect, val in zip(bars, values):
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                rect.get_height(),
                f"{int(val):,}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    ax.set_ylabel("Training records required (mean $\\pm$ SD)")
    ax.set_title("Records needed to reach Boyce Index $>$ 0.9")
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, max(traditional_mean) + max(traditional_sd) + 500)
    ax.legend(loc="upper right", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.set_axisbelow(True)
    plt.tight_layout()
    save(fig, "fig_records_to_bi09")


# ---------------------------------------------------------------------------
# Figure 2: best per-species Boyce Index by dataset
#
# Source: "BIs of Biome+Traditional data: 0.81 +/- 0.20; Traditional survey
# data: 0.83 +/- 0.20."
# ---------------------------------------------------------------------------
def figure_best_bi() -> None:
    labels = ["Traditional", "Biome + Traditional"]
    means = [0.83, 0.81]
    sds = [0.20, 0.20]
    colors = [PALETTE[0], PALETTE[2]]

    fig, ax = plt.subplots(figsize=(4.2, 3.3))
    bars = ax.bar(
        labels,
        means,
        yerr=sds,
        color=colors,
        capsize=4,
        edgecolor="black",
        linewidth=0.5,
        width=0.55,
    )
    for rect, val in zip(bars, means):
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            rect.get_height() + 0.02,
            f"{val:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_ylabel("Best per-species Boyce Index (mean $\\pm$ SD)")
    ax.set_ylim(0, 1.05)
    ax.axhline(0.9, color="gray", linestyle="--", linewidth=0.8)
    ax.text(1.45, 0.91, "BI = 0.9", color="gray", fontsize=8, va="bottom")
    ax.set_title("Best model performance per species")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.set_axisbelow(True)
    plt.tight_layout()
    save(fig, "fig_best_bi")


# ---------------------------------------------------------------------------
# Figure 3: taxonomic composition of Biome records
#
# Source: "The majority of records are attributed to insects (31.2%) and to
# seed plants (41.8%)."  The remaining 27.0% is reported only as an aggregate
# across the residual taxa ("other"), so we plot it as a single "other taxa"
# wedge rather than inventing a breakdown.
# ---------------------------------------------------------------------------
def figure_taxa_composition() -> None:
    labels = ["Seed plants", "Insects", "Other taxa"]
    values = [41.8, 31.2, 100.0 - 41.8 - 31.2]  # = 27.0
    colors = [PALETTE[2], PALETTE[1], PALETTE[4]]

    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    bars = ax.barh(labels, values, color=colors, edgecolor="black", linewidth=0.5)
    for rect, val in zip(bars, values):
        ax.text(
            rect.get_width() + 0.6,
            rect.get_y() + rect.get_height() / 2,
            f"{val:.1f}%",
            va="center",
            fontsize=9,
        )

    ax.set_xlabel("Share of Biome records (%)")
    ax.set_xlim(0, 55)
    ax.set_title("Taxonomic composition of Biome records (N = 5,275,457)")
    ax.invert_yaxis()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.xaxis.grid(True, linestyle=":", alpha=0.5)
    ax.set_axisbelow(True)
    plt.tight_layout()
    save(fig, "fig_taxa_composition")


# ---------------------------------------------------------------------------
# Figure 4: schematic of the Biome submission and filtering pipeline
#
# Structural elements traced to the extracted Methods section:
#   - image upload, AI identification, "ask Biomers" social ID, filtering
#     (non-wild / private / cultural centres), certified-user gating, final
#     SDM training set.
# ---------------------------------------------------------------------------
def figure_workflow_schematic() -> None:
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    def box(x, y, w, h, text, color):
        patch = mpatches.FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            linewidth=1.0,
            edgecolor="black",
            facecolor=color,
        )
        ax.add_patch(patch)
        ax.text(
            x + w / 2,
            y + h / 2,
            text,
            ha="center",
            va="center",
            fontsize=9,
            wrap=True,
        )

    def arrow(x1, y1, x2, y2):
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="->", lw=1.1, color="black"),
        )

    # Row of stages
    box(0.2, 1.4, 1.7, 1.2, "User photo\n+ EXIF", "#eaf2fb")
    box(2.2, 1.4, 1.7, 1.2, "CNN +\ngeospatial\nprior", "#eaf2fb")
    box(4.2, 1.4, 1.7, 1.2, "AI candidate\nlist / \"Ask\nBiomers\"", "#eaf2fb")
    box(6.2, 1.4, 1.7, 1.2, "Automatic\nfiltering\n(45.0% pass)", "#fdecd9")
    box(8.2, 1.4, 1.7, 1.2, "SDM\ntraining set", "#e3f2e0")

    for x1 in (1.9, 3.9, 5.9, 7.9):
        arrow(x1, 2.0, x1 + 0.3, 2.0)

    # Side boxes describing filtering rules
    box(
        2.2,
        0.1,
        5.5,
        0.95,
        "Filters: non-wild labels, private records, cultural-centre\nand pet-store locations, certified-user gating "
        "(<15% misID, <0.5% inappropriate, >20 public records)",
        "#fff3e6",
    )
    arrow(7.0, 1.05, 7.0, 1.38)

    ax.set_title("Biome data pipeline: from photograph to SDM-ready records", fontsize=11)
    plt.tight_layout()
    save(fig, "fig_workflow")


def main() -> None:
    os.makedirs(HERE, exist_ok=True)
    figure_records_to_bi09()
    figure_best_bi()
    figure_taxa_composition()
    figure_workflow_schematic()


if __name__ == "__main__":
    main()
