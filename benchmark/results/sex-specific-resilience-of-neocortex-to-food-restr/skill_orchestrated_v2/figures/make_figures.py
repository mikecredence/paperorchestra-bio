"""Generate figures for Sex-specific resilience of neocortex to food restriction.
All numerical values are verbatim from experimental_log.md.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

FIG_DIR = os.path.dirname(os.path.abspath(__file__))
MALE_COLOR = "#2ca02c"   # green per Suppl Fig 3 description
FEMALE_COLOR = "#9467bd" # purple per Suppl Fig 3 description
CTR_COLOR = "#7f7f7f"
FR_COLOR = "#d62728"


def _star(p):
    if p < 0.0001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "n.s."


def savefig(fig, name):
    fig.savefig(os.path.join(FIG_DIR, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(FIG_DIR, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig1_weight_leptin_ampk():
    """Bodyweight, leptin, AMPK Thr172, PPARalpha across sex and diet."""
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.2))

    # Panel A: Bodyweight at baseline male vs female (only 2 values reported)
    ax = axes[0]
    vals = [27.82, 23.21]
    ci_lo = [26.84, 22.35]
    ci_hi = [28.79, 24.07]
    labels = ["Male", "Female"]
    yerr = [[v - l for v, l in zip(vals, ci_lo)], [h - v for v, h in zip(vals, ci_hi)]]
    ax.bar(labels, vals, yerr=yerr, color=[MALE_COLOR, FEMALE_COLOR], capsize=5,
           edgecolor="black", linewidth=0.6)
    ax.set_ylabel("Bodyweight (g)")
    ax.set_title("Baseline weight")
    ax.text(0.5, max(ci_hi) * 1.05, "***", ha="center")
    ax.set_ylim(0, 33)

    # Panel B: Serum leptin
    ax = axes[1]
    x = np.arange(2)
    w = 0.35
    ctr_m, fr_m = 6.45, 1.84
    ctr_f, fr_f = 3.94, 2.83
    ctr_m_err = [[ctr_m - 4.47], [8.43 - ctr_m]]
    fr_m_err = [[fr_m - 0.90], [2.79 - fr_m]]
    ctr_f_err = [[ctr_f - 2.53], [5.35 - ctr_f]]
    fr_f_err = [[fr_f - 1.20], [4.47 - fr_f]]
    ax.bar([0 - w/2], [ctr_m], w, yerr=ctr_m_err, color=CTR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, label="CTR", capsize=4)
    ax.bar([0 + w/2], [fr_m], w, yerr=fr_m_err, color=FR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, label="FR", capsize=4)
    ax.bar([1 - w/2], [ctr_f], w, yerr=ctr_f_err, color=CTR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([1 + w/2], [fr_f], w, yerr=fr_f_err, color=FR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.set_xticks(x)
    ax.set_xticklabels(["Male", "Female"])
    ax.set_ylabel("Serum leptin (ng/mL)")
    ax.set_title("Leptin")
    ax.text(0, 9.0, "***\np<0.0001", ha="center", fontsize=8)
    ax.text(1, 6.0, "n.s.\np=0.32", ha="center", fontsize=8)
    ax.legend(fontsize=8, loc="upper right")
    ax.set_ylim(0, 10)

    # Panel C: AMPK Thr172
    ax = axes[2]
    ctr_m, fr_m = 13.19, 38.21
    ctr_f, fr_f = 20.94, 29.52
    ctr_m_err = [[ctr_m - 7.68], [18.71 - ctr_m]]
    fr_m_err = [[fr_m - 16.50], [59.93 - fr_m]]
    ctr_f_err = [[ctr_f - 9.42], [32.46 - ctr_f]]
    fr_f_err = [[fr_f - 8.52], [50.53 - fr_f]]
    ax.bar([0 - w/2], [ctr_m], w, yerr=ctr_m_err, color=CTR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([0 + w/2], [fr_m], w, yerr=fr_m_err, color=FR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([1 - w/2], [ctr_f], w, yerr=ctr_f_err, color=CTR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([1 + w/2], [fr_f], w, yerr=fr_f_err, color=FR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.set_xticks(x)
    ax.set_xticklabels(["Male", "Female"])
    ax.set_ylabel("pAMPK(Thr172) (AU/\u03bcg)")
    ax.set_title("V1 AMPK")
    ax.text(0, 66, "*\np=0.022", ha="center", fontsize=8)
    ax.text(1, 55, "n.s.\np=0.11", ha="center", fontsize=8)
    ax.set_ylim(0, 70)

    # Panel D: PPARalpha (from Figure 1E right; numeric values not fully given;
    # show only male vs female p's as schematic using t statistics as magnitude)
    ax = axes[3]
    # Only the statistics are reported for PPARalpha (no mean/CI given). Present
    # as stat results text bar graph mimicking the reported t values (which are
    # NOT means; we indicate this clearly in caption).
    # Per extraction: male t=4.81 p=0.013; female t=0.0016 p=0.99.
    cats = ["Male", "Female"]
    tvals = [4.81, 0.0016]
    bars = ax.bar(cats, tvals, color=[MALE_COLOR, FEMALE_COLOR],
                  edgecolor="black", linewidth=0.6)
    ax.set_ylabel("Two-way ANOVA t statistic")
    ax.set_title("V1 PPAR\u03b1 activity (CTR vs FR)")
    ax.text(0, 5.2, "*\np=0.013", ha="center", fontsize=8)
    ax.text(1, 0.3, "n.s.\np=0.99", ha="center", fontsize=8)
    ax.set_ylim(0, 6)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.tight_layout()
    savefig(fig, "fig1_weight_leptin_ampk")


def fig2_rnaseq():
    """DE gene counts, GSEA counts, and pathway t-statistics."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.4))

    # Panel A: DE gene counts (Venn-like bar)
    ax = axes[0]
    male_only = 657 - 125
    female_only = 585 - 125
    shared = 125
    ax.bar(["Male only", "Shared", "Female only"],
           [male_only, shared, female_only],
           color=[MALE_COLOR, "#bcbd22", FEMALE_COLOR], edgecolor="black", linewidth=0.6)
    ax.set_ylabel("# DE genes (p-adj < 0.1)")
    ax.set_title(f"DESeq2: {657} M, {585} F, {125} shared")
    for i, v in enumerate([male_only, shared, female_only]):
        ax.text(i, v + 8, str(v), ha="center", fontsize=9)

    # Panel B: GSEA Hallmark sets
    ax = axes[1]
    m, f, sh = 34, 14, 13
    ax.bar(["Male only", "Shared", "Female only"], [m - sh, sh, f - sh],
           color=[MALE_COLOR, "#bcbd22", FEMALE_COLOR], edgecolor="black", linewidth=0.6)
    ax.set_ylabel("# Hallmark gene sets (p-adj < 0.05)")
    ax.set_title(f"GSEA: {m} M, {f} F, {sh} shared")
    for i, v in enumerate([m - sh, sh, f - sh]):
        ax.text(i, v + 0.4, str(v), ha="center", fontsize=9)

    # Panel C: pathway t-statistics (male vs female) for four gene sets
    ax = axes[2]
    pathways = ["Ox phos", "mTORC1", "Fatty acid\nmetab.", "PI3K/AKT/mTOR"]
    male_t = [0.48, 0.46, 0.43, 0.34]
    female_t = [-0.17, -0.18, 0.20, 0.17]
    male_p = [1e-5, 1e-5, 1e-5, 0.027]
    female_p = [0.96, 0.98, 0.88, 0.98]
    x = np.arange(len(pathways))
    w = 0.38
    ax.bar(x - w/2, male_t, w, color=MALE_COLOR, edgecolor="black", linewidth=0.5, label="Male")
    ax.bar(x + w/2, female_t, w, color=FEMALE_COLOR, edgecolor="black", linewidth=0.5, label="Female")
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(pathways, fontsize=9)
    ax.set_ylabel("Enrichment score (t)")
    ax.set_title("GSEA t-statistic")
    for i, (mt, mp) in enumerate(zip(male_t, male_p)):
        s = _star(mp)
        ax.text(i - w/2, mt + 0.03, s, ha="center", fontsize=9)
    for i, (ft, fp) in enumerate(zip(female_t, female_p)):
        s = _star(fp)
        ax.text(i + w/2, ft + (0.04 if ft >= 0 else -0.09), s, ha="center", fontsize=9)
    ax.legend()
    ax.set_ylim(-0.25, 0.62)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.tight_layout()
    savefig(fig, "fig2_rnaseq")


def fig3_atp_osi():
    """ATP half-time and OSI by sex/diet."""
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.4))

    # Panel A: ATP half-time of FRET decay
    ax = axes[0]
    ctr_m, fr_m = 8.48, 10.51
    ctr_f, fr_f = 8.66, 9.66
    ctr_m_err = [[ctr_m - 7.59], [9.37 - ctr_m]]
    fr_m_err = [[fr_m - 9.08], [11.93 - fr_m]]
    ctr_f_err = [[ctr_f - 7.49], [9.84 - ctr_f]]
    fr_f_err = [[fr_f - 8.92], [10.39 - fr_f]]
    w = 0.35
    x = np.arange(2)
    ax.bar([0 - w/2], [ctr_m], w, yerr=ctr_m_err, color=CTR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, label="CTR", capsize=4)
    ax.bar([0 + w/2], [fr_m], w, yerr=fr_m_err, color=FR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, label="FR", capsize=4)
    ax.bar([1 - w/2], [ctr_f], w, yerr=ctr_f_err, color=CTR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([1 + w/2], [fr_f], w, yerr=fr_f_err, color=FR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.set_xticks(x)
    ax.set_xticklabels(["Male", "Female"])
    ax.set_ylabel("FRET decay half-time (min)")
    ax.set_title("V1 ATP usage\n(lower = faster ATP use)")
    ax.text(0, 12.3, "**\np=0.0067\n\u221224%", ha="center", fontsize=8)
    ax.text(1, 10.8, "n.s.\np=0.18\n\u221212%", ha="center", fontsize=8)
    ax.legend(fontsize=8, loc="upper left")
    ax.set_ylim(0, 13.5)

    # Panel B: OSI
    ax = axes[1]
    ctr_m, fr_m = 0.58, 0.42
    ctr_f, fr_f = 0.60, 0.52
    ctr_m_err = [[ctr_m - 0.51], [0.65 - ctr_m]]
    fr_m_err = [[fr_m - 0.36], [0.49 - fr_m]]
    ctr_f_err = [[ctr_f - 0.52], [0.67 - ctr_f]]
    fr_f_err = [[fr_f - 0.45], [0.58 - fr_f]]
    ax.bar([0 - w/2], [ctr_m], w, yerr=ctr_m_err, color=CTR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([0 + w/2], [fr_m], w, yerr=fr_m_err, color=FR_COLOR,
           edgecolor=MALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([1 - w/2], [ctr_f], w, yerr=ctr_f_err, color=CTR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.bar([1 + w/2], [fr_f], w, yerr=fr_f_err, color=FR_COLOR,
           edgecolor=FEMALE_COLOR, linewidth=1.5, capsize=4)
    ax.set_xticks(x)
    ax.set_xticklabels(["Male", "Female"])
    ax.set_ylabel("Orientation selectivity index")
    ax.set_title("V1 orientation selectivity")
    ax.text(0, 0.72, "***\np=0.0009\n\u221227%", ha="center", fontsize=8)
    ax.text(1, 0.72, "n.s.\np=0.08\n\u221213%", ha="center", fontsize=8)
    ax.set_ylim(0, 0.85)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.tight_layout()
    savefig(fig, "fig3_atp_osi")


def fig_schema():
    """Schematic of experimental pipeline."""
    fig, ax = plt.subplots(figsize=(10, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    def box(x, y, w, h, text, color="#f0f0f0"):
        p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                           linewidth=1.2, edgecolor="black", facecolor=color)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=9)

    def arrow(x1, y1, x2, y2):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                                     arrowstyle="->,head_length=6,head_width=4",
                                     linewidth=1.2, color="black"))

    # Row 1: cohort
    box(0.3, 2.6, 2.2, 1.0,
        "Adult mice 7-9 wk\nCTR vs FR (85% BW)\n2-3 weeks", color="#e8f4fb")
    # Row 2: three assays
    box(3.3, 3.2, 2.2, 0.8, "Serum leptin\nAMPK / PPAR\u03b1", color="#fff4e6")
    box(3.3, 2.0, 2.2, 0.8, "V1 RNA-seq\nDESeq2 + GSEA", color="#fff4e6")
    box(3.3, 0.8, 2.2, 0.8,
        "Two-photon imaging:\nATeam1.03YEMK ATP\nGCaMP6s OSI", color="#fff4e6")
    # Output
    box(6.5, 2.0, 3.0, 0.8,
        "Sex-specific effects\n(Bayes factor analysis)", color="#e2f0d9")

    arrow(2.5, 3.3, 3.3, 3.6)
    arrow(2.5, 3.1, 3.3, 2.4)
    arrow(2.5, 2.8, 3.3, 1.2)
    arrow(5.5, 3.6, 6.5, 2.6)
    arrow(5.5, 2.4, 6.5, 2.4)
    arrow(5.5, 1.2, 6.5, 2.2)

    fig.tight_layout()
    savefig(fig, "fig_schema_experiment")


if __name__ == "__main__":
    os.makedirs(FIG_DIR, exist_ok=True)
    fig1_weight_leptin_ampk()
    fig2_rnaseq()
    fig3_atp_osi()
    fig_schema()
    print("Figures generated in", FIG_DIR)
