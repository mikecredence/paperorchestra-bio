"""Figure generator for cross-species BCAP paper.

Every value plotted traces directly to a statement in the experimental log.
No fabricated numbers: bar heights, correlation values, and labels are copied
from the extracted statistical reports in inputs/experimental_log.md.
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
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
})

HERE = os.path.dirname(os.path.abspath(__file__))
PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


def save(fig, name):
    fig.savefig(os.path.join(HERE, name + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(HERE, name + ".png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------------
# Figure 1: Schematic of the cross-species age prediction pipeline
# ------------------------------------------------------------------
def fig_pipeline():
    fig, ax = plt.subplots(figsize=(7.2, 3.3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    boxes = [
        (0.2, 1.4, 1.8, 1.2, "sMRI + dMRI\n(N=370 humans,\nN=181 macaques)", "#d6eaf8"),
        (2.4, 1.4, 1.8, 1.2, "GMV + FA/MD/\nAD/RD features\n(260 total)", "#d5f5e3"),
        (4.6, 1.4, 1.8, 1.2, "Feature selection\n(p<0.01 + 100\niterations)", "#fcf3cf"),
        (6.8, 1.4, 1.8, 1.2, "Prediction\nmodels\n(10-fold CV)", "#fadbd8"),
    ]
    for (x, y, w, h, label, color) in boxes:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                     facecolor=color, edgecolor="black", linewidth=0.8))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=9)

    for x_src, x_dst in [(2.0, 2.4), (4.2, 4.6), (6.4, 6.8)]:
        ax.add_patch(FancyArrowPatch((x_src, 2.0), (x_dst, 2.0),
                                     arrowstyle="->", mutation_scale=14, color="black"))

    # Downstream outputs
    ax.add_patch(FancyBboxPatch((8.9, 2.55), 1.0, 0.8, boxstyle="round,pad=0.05",
                                 facecolor="#e8daef", edgecolor="black", linewidth=0.8))
    ax.text(9.4, 2.95, "Intra-\nspecies R,\nMAE", ha="center", va="center", fontsize=8)

    ax.add_patch(FancyBboxPatch((8.9, 1.4), 1.0, 0.8, boxstyle="round,pad=0.05",
                                 facecolor="#e8daef", edgecolor="black", linewidth=0.8))
    ax.text(9.4, 1.8, "Cross-\nspecies R,\nMAE", ha="center", va="center", fontsize=8)

    ax.add_patch(FancyBboxPatch((8.9, 0.25), 1.0, 0.8, boxstyle="round,pad=0.05",
                                 facecolor="#e8daef", edgecolor="black", linewidth=0.8))
    ax.text(9.4, 0.65, "BCAP\npercentile\nrank index", ha="center", va="center", fontsize=8)

    for y in (2.95, 1.8, 0.65):
        ax.add_patch(FancyArrowPatch((8.6, 2.0), (8.9, y), arrowstyle="->",
                                     mutation_scale=11, color="black"))

    ax.set_title("Brain structure based cross-species age prediction pipeline")
    save(fig, "fig1_pipeline")


# ------------------------------------------------------------------
# Figure 2: Within- and cross-species prediction performance
# Data: extracted statistical sentences (lines 4, 5, 7, 8 of inputs)
# ------------------------------------------------------------------
def fig_prediction_performance():
    conditions = ["62M / 225H\n(common)", "117M / 239H\n(min-MAE)", "62M / 62H\n(top shared)"]
    mac_in = [0.5729, 0.5825, 0.5729]
    hum_in = [0.6153, 0.6039, 0.6818]
    mac_to_hum = [0.4823, 0.4018, 0.4822]
    hum_to_mac = [0.2898, 0.3223, 0.2094]

    mac_mae = [0.3758, 0.3675, 0.3760]
    hum_mae = [1.1236, 1.1388, 1.0025]
    mtoh_mae = [8.3610, 7.7185, 8.3606]
    htom_mae = [7.6157, 7.9514, 6.1083]

    x = np.arange(len(conditions))
    width = 0.2

    fig, (axR, axM) = plt.subplots(1, 2, figsize=(9.0, 3.6))

    axR.bar(x - 1.5 * width, mac_in, width, label="Mac->Mac", color=PALETTE[2])
    axR.bar(x - 0.5 * width, hum_in, width, label="Hum->Hum", color=PALETTE[0])
    axR.bar(x + 0.5 * width, mac_to_hum, width, label="Mac->Hum", color=PALETTE[1])
    axR.bar(x + 1.5 * width, hum_to_mac, width, label="Hum->Mac", color=PALETTE[4])
    axR.set_ylabel("Pearson R (predicted vs. actual age)")
    axR.set_xticks(x)
    axR.set_xticklabels(conditions)
    axR.set_ylim(0, 0.8)
    axR.set_title("Prediction correlation")
    axR.legend(ncol=2, fontsize=8, loc="upper right")
    for s in ("top", "right"):
        axR.spines[s].set_visible(False)

    axM.bar(x - 1.5 * width, mac_mae, width, label="Mac->Mac", color=PALETTE[2])
    axM.bar(x - 0.5 * width, hum_mae, width, label="Hum->Hum", color=PALETTE[0])
    axM.bar(x + 0.5 * width, mtoh_mae, width, label="Mac->Hum", color=PALETTE[1])
    axM.bar(x + 1.5 * width, htom_mae, width, label="Hum->Mac", color=PALETTE[4])
    axM.set_ylabel("MAE (years)")
    axM.set_xticks(x)
    axM.set_xticklabels(conditions)
    axM.set_title("Prediction error (MAE)")
    for s in ("top", "right"):
        axM.spines[s].set_visible(False)

    fig.suptitle("Intra- and cross-species age prediction across feature sets", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    save(fig, "fig2_prediction_performance")


# ------------------------------------------------------------------
# Figure 3: |Delta brain age| vs actual age correlations
# Data: lines 9, 10 (main) and 26, 27 (supplement 4)
# ------------------------------------------------------------------
def fig_age_gap():
    conds = ["Mac->Hum\n(62/225 feats)", "Hum->Mac\n(62/225 feats)",
             "Mac->Hum\n(117/239 feats)", "Hum->Mac\n(117/239 feats)"]
    rvals = [0.9813, -0.3759, 0.9828, -0.3318]
    maes = [2.7120, 4.8697, 3.3545, 5.2055]
    colors = [PALETTE[1], PALETTE[4], PALETTE[1], PALETTE[4]]

    fig, (axR, axM) = plt.subplots(1, 2, figsize=(8.4, 3.4))

    bars = axR.bar(conds, rvals, color=colors, edgecolor="black", linewidth=0.5)
    axR.axhline(0, color="black", linewidth=0.5)
    axR.set_ylabel("Pearson R\n(|Delta brain age| vs actual age)")
    axR.set_ylim(-0.6, 1.1)
    axR.set_title("Age effects on cross-species prediction error")
    for s in ("top", "right"):
        axR.spines[s].set_visible(False)
    for b, r in zip(bars, rvals):
        axR.text(b.get_x() + b.get_width() / 2,
                 r + (0.03 if r >= 0 else -0.08),
                 f"R = {r:+.4f}", ha="center", va="bottom" if r >= 0 else "top",
                 fontsize=8)

    axM.bar(conds, maes, color=colors, edgecolor="black", linewidth=0.5)
    axM.set_ylabel("MAE (years)")
    axM.set_title("Gap magnitude")
    for s in ("top", "right"):
        axM.spines[s].set_visible(False)
    for i, m in enumerate(maes):
        axM.text(i, m + 0.1, f"{m:.4f}", ha="center", va="bottom", fontsize=8)

    fig.tight_layout()
    save(fig, "fig3_age_gap")


# ------------------------------------------------------------------
# Figure 4: Top-correlating features with age
# Data: lines 13-16 of inputs
# ------------------------------------------------------------------
def fig_features():
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.0))

    # (A) macaque-specific GM + WM (line 13)
    mac_names = ["L PFCdl", "L PMCm", "R PFCdl", "R PFCom", "R PFCcl",
                 "L SLF II", "R UF"]
    mac_vals = [0.4003, 0.3966, 0.3723, 0.3478, 0.3427, 0.3067, 0.2901]
    mac_colors = [PALETTE[2]] * 5 + [PALETTE[0]] * 2
    axes[0, 0].barh(mac_names[::-1], mac_vals[::-1],
                    color=mac_colors[::-1], edgecolor="black", linewidth=0.5)
    axes[0, 0].set_xlabel("Pearson R with age")
    axes[0, 0].set_title("(A) Macaque-specific features")
    axes[0, 0].set_xlim(0, 0.55)
    for s in ("top", "right"):
        axes[0, 0].spines[s].set_visible(False)

    # (B) human-specific GM + WM (line 14)
    hum_names = ["L Putamen", "R Pallidum", "L post. insula",
                 "L Pallidum", "R S1",
                 "R SLF I", "L IFOF", "L AF", "R IFOF", "L SLF I"]
    hum_vals = [0.4437, 0.4284, 0.3915, 0.3884, 0.3703,
                0.4138, 0.3665, 0.3459, 0.3445, 0.3443]
    hum_colors = [PALETTE[2]] * 5 + [PALETTE[0]] * 5
    axes[0, 1].barh(hum_names[::-1], hum_vals[::-1],
                    color=hum_colors[::-1], edgecolor="black", linewidth=0.5)
    axes[0, 1].set_xlabel("Pearson R with age")
    axes[0, 1].set_title("(B) Human-specific features")
    axes[0, 1].set_xlim(0, 0.55)
    for s in ("top", "right"):
        axes[0, 1].spines[s].set_visible(False)

    # (C) Shared GM features (line 15)
    shared_hum = ["R post. insula", "L CCp", "L PMCvl", "R CCp", "R PCip"]
    shared_hum_v = [0.3769, 0.3583, 0.3523, 0.3466, 0.3433]
    shared_mac = ["R CCa", "L CCa", "R PMCm", "L PCs", "R PCi"]
    shared_mac_v = [0.4694, 0.4274, 0.4235, 0.4228, 0.4035]
    y = np.arange(len(shared_hum))
    axes[1, 0].barh(y - 0.2, shared_hum_v[::-1], height=0.4,
                    color=PALETTE[0], label="Human", edgecolor="black", linewidth=0.5)
    axes[1, 0].barh(y + 0.2, shared_mac_v[::-1], height=0.4,
                    color=PALETTE[2], label="Macaque", edgecolor="black", linewidth=0.5)
    axes[1, 0].set_yticks(y)
    axes[1, 0].set_yticklabels(["#{}".format(i + 1) for i in range(5)][::-1])
    axes[1, 0].set_xlabel("Pearson R with age")
    axes[1, 0].set_title("(C) Shared GM features (rank 1..5)")
    axes[1, 0].set_xlim(0, 0.55)
    axes[1, 0].legend(loc="lower right", fontsize=8)
    for s in ("top", "right"):
        axes[1, 0].spines[s].set_visible(False)

    # (D) Shared WM features (line 16)
    shared_hum_wm = ["L CT", "R CT", "R STR", "L STR", "L Cs:Pg"]
    shared_hum_wm_v = [0.4654, 0.4499, 0.3344, 0.3212, 0.2341]
    shared_mac_wm = ["R CT", "L CT", "R UF", "L SLF II", "L STR"]
    shared_mac_wm_v = [0.4189, 0.3746, 0.3497, 0.3067, 0.3046]
    y = np.arange(len(shared_hum_wm))
    axes[1, 1].barh(y - 0.2, shared_hum_wm_v[::-1], height=0.4,
                    color=PALETTE[0], label="Human", edgecolor="black", linewidth=0.5)
    axes[1, 1].barh(y + 0.2, shared_mac_wm_v[::-1], height=0.4,
                    color=PALETTE[2], label="Macaque", edgecolor="black", linewidth=0.5)
    axes[1, 1].set_yticks(y)
    axes[1, 1].set_yticklabels(["#{}".format(i + 1) for i in range(5)][::-1])
    axes[1, 1].set_xlabel("Pearson R with age")
    axes[1, 1].set_title("(D) Shared WM features (rank 1..5)")
    axes[1, 1].set_xlim(0, 0.55)
    axes[1, 1].legend(loc="lower right", fontsize=8)
    for s in ("top", "right"):
        axes[1, 1].spines[s].set_visible(False)

    # Legend for GM/WM coloring in A and B
    gm_patch = mpatches.Patch(color=PALETTE[2], label="Gray matter")
    wm_patch = mpatches.Patch(color=PALETTE[0], label="White matter")
    fig.legend(handles=[gm_patch, wm_patch], loc="upper center",
               ncol=2, bbox_to_anchor=(0.5, 1.02), fontsize=9, frameon=False)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    save(fig, "fig4_features")


# ------------------------------------------------------------------
# Figure 5: BCAP associations
# Data: lines 17, 18 of inputs
# ------------------------------------------------------------------
def fig_bcap():
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0))

    # (A) Behavior (line 17): note that |-2051| is reported as "R = -2051" in text;
    # this is evidently a typo for -0.2051 (p = 0.0056 is consistent).
    beh_names = ["Picture vocabulary\ntest", "Visual sensitivity\ntest"]
    beh_vals = [0.1588, -0.2051]
    bars = axes[0].bar(beh_names, beh_vals,
                       color=[PALETTE[0], PALETTE[3]],
                       edgecolor="black", linewidth=0.5)
    axes[0].axhline(0, color="black", linewidth=0.5)
    axes[0].set_ylabel("Pearson R with BCAP")
    axes[0].set_title("(A) Behavioral associations with BCAP")
    axes[0].set_ylim(-0.3, 0.25)
    for b, v, p in zip(bars, beh_vals, ["P = 0.0323", "P = 0.0056"]):
        axes[0].text(b.get_x() + b.get_width() / 2,
                     v + (0.015 if v >= 0 else -0.015),
                     f"R = {v:+.4f}\n{p}",
                     ha="center",
                     va="bottom" if v >= 0 else "top", fontsize=8)
    for s in ("top", "right"):
        axes[0].spines[s].set_visible(False)

    # (B) WM FA + GM BCAP correlations (line 18)
    tract_names = ["L AF", "L OR", "R AF",
                   "AC", "R SLF III", "FM"]
    tract_vals = [0.3784, 0.3232, 0.3035,
                  0.1215, 0.1166, -0.1221]
    gm_names = ["R PFCdl", "R PFCcl", "R PFCvl", "R PFCdm", "R PFCm",
                "R Amyg", "R Acc", "L Acc", "L Pu", "L Amyg"]
    gm_vals = [0.4685, 0.4324, 0.4287, 0.3915, 0.3890,
               -0.1759, -0.181, -0.1811, -0.2104, -0.2151]

    combined_names = tract_names + [""] + gm_names
    combined_vals = tract_vals + [0] + gm_vals
    colors = ([PALETTE[0]] * 3 + [PALETTE[4]] * 3 +
              ["white"] +
              [PALETTE[0]] * 5 + [PALETTE[4]] * 5)
    ypos = np.arange(len(combined_names))
    axes[1].barh(ypos, combined_vals[::-1],
                 color=colors[::-1], edgecolor="black", linewidth=0.4)
    axes[1].set_yticks(ypos)
    axes[1].set_yticklabels(combined_names[::-1])
    axes[1].axvline(0, color="black", linewidth=0.5)
    axes[1].set_xlabel("Pearson R with BCAP")
    axes[1].set_title("(B) WM tracts (FA) and GM regions")
    for s in ("top", "right"):
        axes[1].spines[s].set_visible(False)

    pos_patch = mpatches.Patch(color=PALETTE[0], label="Positive association")
    neg_patch = mpatches.Patch(color=PALETTE[4], label="Negative association")
    axes[1].legend(handles=[pos_patch, neg_patch], loc="lower right", fontsize=8)

    fig.tight_layout()
    save(fig, "fig5_bcap")


if __name__ == "__main__":
    os.makedirs(HERE, exist_ok=True)
    fig_pipeline()
    fig_prediction_performance()
    fig_age_gap()
    fig_features()
    fig_bcap()
    print("Generated 5 figures (.pdf + .png each) in", HERE)
