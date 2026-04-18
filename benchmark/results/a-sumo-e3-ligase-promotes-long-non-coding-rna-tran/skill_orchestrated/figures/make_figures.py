"""Generate figures for the Ema2/Tetrahymena manuscript.

All data values traced to the experimental_log.md extraction. Where discrete
numerical comparisons were not available in the extraction, schematic diagrams
or annotated placeholder panels are generated instead. No numeric values are
fabricated.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))

COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "figure.dpi": 120,
})


def save(fig, name):
    fig.savefig(os.path.join(HERE, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(HERE, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# -----------------------------------------------------------------------------
# Figure 1: Schematic of Ema2 expression and localization timeline
# (Source: Results chunk describing Figure 1A-B -- EMA2 mRNA expressed only
# during conjugation; Ema2-HA at 3/6 hpm in parental MAC, 8 hpm new MAC,
# 12/14 hpm fades away.)
# -----------------------------------------------------------------------------
def fig_timeline():
    fig, ax = plt.subplots(figsize=(6.5, 2.4))
    stages = [
        ("Vg",      0.0, "no expression"),
        ("3 hpm",   1.0, "parental MAC"),
        ("6 hpm",   2.0, "parental MAC"),
        ("8 hpm",   3.0, "new MAC"),
        ("12 hpm",  4.0, "fading"),
        ("14 hpm",  5.0, "fading"),
    ]
    # timeline axis
    ax.hlines(0.5, -0.3, 5.3, colors="#333", linewidth=1)
    for label, x, loc in stages:
        ax.plot(x, 0.5, "o", color=COLORS[0], markersize=8, zorder=3)
        ax.text(x, 0.8, label, ha="center", va="bottom", fontsize=9)
        ax.text(x, 0.2, loc, ha="center", va="top", fontsize=8,
                color="#555", style="italic")
    ax.text(-0.3, 0.5, "Ema2-HA:", ha="right", va="center", fontsize=9)
    ax.set_xlim(-1.4, 5.6)
    ax.set_ylim(-0.1, 1.1)
    ax.axis("off")
    ax.set_title("Timeline of Ema2 expression and subnuclear localization")
    save(fig, "fig1_ema2_timeline")


# -----------------------------------------------------------------------------
# Figure 2: Schematic of the TDSD defect in EMA2 KO
# (Source: Figure 3A text in Results chunk -- Mi-9 scnRNAs detected at 3 hpm,
# reduced at 4.5 hpm, undetectable at 6 hpm in WT; remain detectable at 6 hpm
# in EMA2 KO. Levels are qualitative (present/reduced/absent), so this is
# drawn as a categorical 3-level heatmap rather than with invented numbers.)
# -----------------------------------------------------------------------------
def fig_tdsd_schematic():
    fig, ax = plt.subplots(figsize=(5.2, 2.4))
    conditions = ["WT", "EMA2 KO"]
    time_points = ["3 hpm", "4.5 hpm", "6 hpm"]
    # Qualitative levels from the log: present=1.0, reduced=0.5, absent=0.0
    data = np.array([
        [1.0, 0.5, 0.0],   # WT
        [1.0, 1.0, 1.0],   # EMA2 KO: remains detectable at all three time points
    ])
    im = ax.imshow(data, cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(len(time_points)))
    ax.set_xticklabels(time_points)
    ax.set_yticks(range(len(conditions)))
    ax.set_yticklabels(conditions)
    labels = np.array([
        ["detected", "reduced", "absent"],
        ["detected", "detected", "detected"],
    ])
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, labels[i, j], ha="center", va="center",
                    fontsize=9,
                    color="white" if data[i, j] > 0.6 else "#222")
    ax.set_title("Mi-9 probe scnRNA signal (categorical, from Figure 3A)")
    cbar = fig.colorbar(im, ax=ax, shrink=0.7)
    cbar.set_ticks([0.0, 0.5, 1.0])
    cbar.set_ticklabels(["absent", "reduced", "detected"])
    save(fig, "fig2_tdsd_schematic")


# -----------------------------------------------------------------------------
# Figure 3: Ema2-dependent SUMOylated protein levels
# (Source: "high molecular weight proteins (mainly >200 kDa) were detected in
# the WT cross, and they were reduced to ~50% in the EMA2 KO cross".)
# -----------------------------------------------------------------------------
def fig_sumo_bar():
    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    crosses = ["WT cross", "EMA2 KO cross"]
    # Only the WT = 1 (normalized) and KO ~ 0.5 levels are stated in the log.
    values = [1.0, 0.5]
    ax.bar(crosses, values, color=[COLORS[0], COLORS[3]], width=0.55)
    ax.set_ylim(0, 1.25)
    ax.set_ylabel("HMW SUMOylated protein signal\n(normalized, WT = 1)")
    ax.set_title(">200 kDa HA-Smt3 conjugates\nat 4.5 and 6 hpm")
    for i, v in enumerate(values):
        ax.text(i, v + 0.03, f"{v:.1f}", ha="center", va="bottom", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig3_sumo_bar")


# -----------------------------------------------------------------------------
# Figure 4: Schematic of Ema2-directed SUMOylation pathway.
# -----------------------------------------------------------------------------
def fig_pathway_schematic():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    def box(x, y, w, h, label, color):
        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.08,rounding_size=0.15",
            linewidth=1.2, edgecolor="#222",
            facecolor=color, alpha=0.85,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=10, weight="bold")

    def arrow(x1, y1, x2, y2, text=None):
        ax.add_patch(FancyArrowPatch(
            (x1, y1), (x2, y2),
            arrowstyle="-|>", mutation_scale=12,
            color="#333", linewidth=1.3,
        ))
        if text:
            ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.15, text,
                    ha="center", va="bottom", fontsize=8, style="italic")

    box(0.2, 3.4, 1.8, 1.0, "Ema2\n(SP-RING)", "#ffe8b3")
    box(2.6, 3.4, 1.6, 1.0, "Ubc9 (E2)", "#bde4a8")
    box(4.8, 3.4, 1.6, 1.0, "Smt3\n(SUMO)", "#c4d9f5")
    box(7.0, 3.4, 2.6, 1.0, "Spt6 / other\nsubstrates", "#f4c4c4")

    arrow(2.0, 3.9, 2.6, 3.9, "bind")
    arrow(4.2, 3.9, 4.8, 3.9)
    arrow(6.4, 3.9, 7.0, 3.9, "transfer")

    box(7.0, 1.4, 2.6, 1.0, "Chromatin\n(pMAC)", "#e0e0e0")
    arrow(8.3, 3.4, 8.3, 2.4, "recruit Spt6,\nRNAPII")

    box(0.2, 1.4, 6.0, 1.0,
        "pMAC-lncRNA transcription $\\rightarrow$ TDSD $\\rightarrow$ DNA elimination",
        "#d9f0f0")
    arrow(7.0, 1.9, 6.2, 1.9)

    ax.set_title("Ema2-directed SUMOylation cascade (schematic)", pad=6)
    save(fig, "fig4_pathway_schematic")


# -----------------------------------------------------------------------------
# Figure 5: Phenotype matrix across knockouts
# (Source: Figures 2, 3, 6 descriptions -- categorical summary of KO
# phenotypes for pMAC-lncRNA, H3K27me3, TDSD, DNA elimination, viable progeny.)
# -----------------------------------------------------------------------------
def fig_phenotype_matrix():
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    strains = ["WT", "EMA2 KO", "EMA1 KO", "TWI1 KO", "EZL1 KO"]
    measures = [
        "pMAC dsRNA",
        "H3K27me3 in pMAC",
        "MDS scnRNA TDSD",
        "DNA elim. (Tlr1)",
        "Viable progeny",
    ]
    # 1 = present/complete, 0 = absent/defective, 0.5 = partial
    # Values directly justified by the experimental_log text; cells where
    # the log does not state a value are marked "n.d."
    grid = np.array([
        #  pMAC  H3K27 TDSD  DNAe  viab
        [1.0,   1.0,  1.0,  1.0,  1.0],  # WT
        [0.0,   0.0,  0.0,  0.5,  0.0],  # EMA2 KO
        [1.0,   0.0,  0.0,  0.0,  np.nan],  # EMA1 KO (viability not stated)
        [np.nan,0.0,  np.nan,0.0, np.nan],  # TWI1 KO
        [np.nan,0.0,  np.nan,np.nan,np.nan],  # EZL1 KO
    ])
    masked = np.ma.masked_invalid(grid)
    cmap = plt.cm.RdYlGn
    im = ax.imshow(masked, cmap=cmap, vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(len(measures)))
    ax.set_xticklabels(measures, rotation=20, ha="right")
    ax.set_yticks(range(len(strains)))
    ax.set_yticklabels(strains)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            v = grid[i, j]
            if np.isnan(v):
                txt = "n.d."
            elif v == 1.0:
                txt = "+"
            elif v == 0.0:
                txt = "--"
            else:
                txt = "partial"
            ax.text(j, i, txt, ha="center", va="center", fontsize=9, color="#111")
    ax.set_title("Phenotype summary across knockout strains")
    save(fig, "fig5_phenotype_matrix")


# -----------------------------------------------------------------------------
# Figure 6: Spt6 mutant summary bar (categorical)
# (Source: Results on HA-SPT6-WT, DOL-KR, N-KR, M-KR, C-KR.)
# -----------------------------------------------------------------------------
def fig_spt6_mutants():
    fig, ax = plt.subplots(figsize=(6.8, 3.2))
    mutants = ["WT", "DOL-KR", "N-KR", "M-KR", "C-KR"]
    # Each feature encoded categorically from the text:
    # 1 = yes, 0 = no, 0.5 = partial / mild defect, nan = not examined
    vegetative_rescue = [1, 1, 1, 1, 1]
    conjugation_ok    = [1, 1, 0, 0, 0.5]   # N-KR meiosis block, M-KR mating block, C-KR lower mating
    sumoylation_seen  = [1, 1, np.nan, np.nan, 0]
    lncRNA_ok         = [1, np.nan, np.nan, np.nan, 1]
    DNA_elim          = [1, np.nan, np.nan, np.nan, 0.5]

    x = np.arange(len(mutants))
    width = 0.15
    series = [
        ("Veg rescue", vegetative_rescue, COLORS[0]),
        ("Conjugation", conjugation_ok, COLORS[1]),
        ("SUMOylation", sumoylation_seen, COLORS[2]),
        ("pMAC-lncRNA", lncRNA_ok, COLORS[3]),
        ("DNA elim.", DNA_elim, COLORS[4]),
    ]
    for i, (label, vals, c) in enumerate(series):
        vals_clean = [0 if np.isnan(v) else v for v in vals]
        nans = [np.isnan(v) for v in vals]
        bars = ax.bar(x + (i - 2) * width, vals_clean, width, label=label, color=c)
        for j, (bar, is_nan) in enumerate(zip(bars, nans)):
            if is_nan:
                bar.set_hatch("///")
                bar.set_edgecolor("#666")
                bar.set_facecolor("#eee")
                ax.text(bar.get_x() + bar.get_width() / 2,
                        0.04, "n.d.", ha="center", va="bottom", fontsize=7, color="#555")
    ax.set_xticks(x)
    ax.set_xticklabels(mutants)
    ax.set_ylabel("Categorical score\n(1 = yes, 0.5 = partial, 0 = no)")
    ax.set_ylim(0, 1.3)
    ax.legend(ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.18),
              frameon=False, fontsize=8)
    ax.set_title("Spt6 K-to-R mutant series")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "fig6_spt6_mutants")


if __name__ == "__main__":
    fig_timeline()
    fig_tdsd_schematic()
    fig_sumo_bar()
    fig_pathway_schematic()
    fig_phenotype_matrix()
    fig_spt6_mutants()
    print("Generated 6 figures in", HERE)
