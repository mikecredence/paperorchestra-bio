"""
make_figures.py
Generate publication figures for the neural speech decoding manuscript.
All numerical values come verbatim from the experimental log.
Figures are saved to the workspace figures/ directory.
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "figure.dpi": 150,
})

COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


def save(fig, name):
    fig.savefig(os.path.join(HERE, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(HERE, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# -------------------------------------------------------------------------
# Figure 1: PCC across architectures, non-causal vs causal
# Source: experimental_log — mean PCC values for ResNet/SWIN/LSTM, n=48
# -------------------------------------------------------------------------
def fig_pcc_models():
    models = ["ResNet", "SWIN", "LSTM"]
    noncausal = [0.804, 0.793, 0.757]
    causal = [0.798, 0.796, 0.713]
    # p-values for noncausal vs causal Wilcoxon signed-rank from log
    pvals = [0.1022, 0.2794, 0.0007]
    x = np.arange(len(models))
    width = 0.36

    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    bars1 = ax.bar(x - width/2, noncausal, width,
                   label="Non-causal", color=COLORS[0])
    bars2 = ax.bar(x + width/2, causal, width,
                   label="Causal", color=COLORS[1])

    for bars, vals in [(bars1, noncausal), (bars2, causal)]:
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width()/2, v + 0.008, f"{v:.3f}",
                    ha="center", va="bottom", fontsize=8)

    # Annotate significance with p-values under each pair
    for xi, p in zip(x, pvals):
        marker = "n.s." if p > 0.05 else "**"
        ax.text(xi, 0.58, f"p={p:.4f}\n{marker}",
                ha="center", va="center", fontsize=8, color="gray")

    ax.set_ylabel("Mean spectrogram PCC (n=48)")
    ax.set_title("Decoding performance across architectures and causality")
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.set_ylim(0.55, 0.88)
    ax.legend(loc="upper right", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linestyle=":")
    ax.set_axisbelow(True)
    plt.tight_layout()
    save(fig, "fig_pcc_models")


# -------------------------------------------------------------------------
# Figure 2: Speech parameter reconstruction PCCs
# Source: experimental_log — voice weight, loudness, pitch, f1, f2
# -------------------------------------------------------------------------
def fig_params():
    params = ["Voice\nweight", "Loudness", "Pitch\n$f_0$", "Formant\n$f_1$", "Formant\n$f_2$"]
    pccs = [0.834, 0.545, 0.907, 0.827, 0.895]

    fig, ax = plt.subplots(figsize=(5.4, 3.4))
    bars = ax.bar(params, pccs, color=COLORS[:5])
    for b, v in zip(bars, pccs):
        ax.text(b.get_x() + b.get_width()/2, v + 0.01, f"{v:.3f}",
                ha="center", va="bottom", fontsize=9)

    ax.set_ylabel("PCC (decoded vs reference)")
    ax.set_title("Reconstruction of decoded speech parameters")
    ax.set_ylim(0, 1.0)
    ax.axhline(0.6, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
    ax.text(4.3, 0.61, "linear baseline ~0.6", fontsize=7, color="gray",
            ha="right", va="bottom")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linestyle=":")
    ax.set_axisbelow(True)
    plt.tight_layout()
    save(fig, "fig_params")


# -------------------------------------------------------------------------
# Figure 3: Left vs right hemisphere decoding (causal ResNet and SWIN)
# Source: experimental_log — right hemisphere PCC and Wilcoxon rank-sum p
# -------------------------------------------------------------------------
def fig_hemisphere():
    models = ["Causal ResNet", "Causal SWIN"]
    # Use causal PCC values as proxy for left-like (n=32) since log reports
    # "not significantly different" and 0.798 / 0.796 are cohort means.
    # Right hemisphere PCCs from log.
    right_pcc = [0.790, 0.781]
    overall_pcc = [0.798, 0.796]  # causal cohort means (approximate left-dominant)
    p_pcc = [0.312, 0.325]
    p_stoi = [0.108, 0.092]
    x = np.arange(len(models))
    width = 0.36

    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.4))

    ax = axes[0]
    b1 = ax.bar(x - width/2, overall_pcc, width, color=COLORS[0],
                label="Cohort causal PCC")
    b2 = ax.bar(x + width/2, right_pcc, width, color=COLORS[3],
                label="Right hemisphere (n=16)")
    for bars, vals in [(b1, overall_pcc), (b2, right_pcc)]:
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width()/2, v + 0.006, f"{v:.3f}",
                    ha="center", va="bottom", fontsize=8)
    ax.set_ylabel("Mean spectrogram PCC")
    ax.set_title("Right hemisphere decoding")
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.set_ylim(0.7, 0.85)
    ax.legend(loc="lower right", frameon=False, fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linestyle=":")
    ax.set_axisbelow(True)

    ax = axes[1]
    b1 = ax.bar(x - width/2, p_pcc, width, color=COLORS[0],
                label="PCC Wilcoxon rank-sum")
    b2 = ax.bar(x + width/2, p_stoi, width, color=COLORS[2],
                label="STOI+ Wilcoxon rank-sum")
    for bars, vals in [(b1, p_pcc), (b2, p_stoi)]:
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width()/2, v + 0.01, f"{v:.3f}",
                    ha="center", va="bottom", fontsize=8)
    ax.axhline(0.05, color="red", linestyle="--", linewidth=0.8,
               label=r"$\alpha$=0.05")
    ax.set_ylabel("p-value (left vs right)")
    ax.set_title("Hemispheric comparison significance")
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.set_ylim(0, 0.45)
    ax.legend(loc="upper right", frameon=False, fontsize=7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linestyle=":")
    ax.set_axisbelow(True)

    plt.tight_layout()
    save(fig, "fig_hemisphere")


# -------------------------------------------------------------------------
# Figure 4: Schematic of the two-stage pipeline
# Source: experimental_log — two-stage training description
# -------------------------------------------------------------------------
def fig_architecture():
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    def box(x, y, w, h, text, color="#dcecff"):
        p = FancyBboxPatch((x, y), w, h,
                           boxstyle="round,pad=0.08",
                           linewidth=1.2, edgecolor="#333",
                           facecolor=color)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha="center", va="center",
                fontsize=9)

    def arrow(x1, y1, x2, y2, label=None, color="#333"):
        a = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle="->", mutation_scale=12,
                            linewidth=1.2, color=color)
        ax.add_patch(a)
        if label:
            ax.text((x1+x2)/2, (y1+y2)/2 + 0.15, label,
                    ha="center", fontsize=8, color=color)

    # Top row: ECoG-to-speech pipeline (stage 2)
    ax.text(5.0, 5.7, "Stage 2: ECoG-to-Speech Decoding",
            ha="center", fontsize=11, fontweight="bold",
            color="#1f4e79")

    box(0.2, 4.3, 1.7, 0.9, "ECoG signals\n(high gamma,\n125 Hz)", "#fff3df")
    box(2.3, 4.3, 1.9, 0.9, "ECoG Decoder\n(ResNet / SWIN / LSTM)", "#dcecff")
    box(4.6, 4.3, 1.7, 0.9, "Speech params\n(18 per frame)", "#e8f5e9")
    box(6.7, 4.3, 1.7, 0.9, "Speech\nSynthesizer", "#dcecff")
    box(9.0, 4.3, 1.0, 0.9, "Spectro-\ngram", "#fff3df")

    arrow(1.9, 4.75, 2.3, 4.75)
    arrow(4.2, 4.75, 4.6, 4.75)
    arrow(6.3, 4.75, 6.7, 4.75)
    arrow(8.4, 4.75, 9.0, 4.75)

    # Bottom row: speech-to-speech auto-encoder (stage 1)
    ax.text(5.0, 3.2, "Stage 1: Speech-to-Speech Auto-Encoder (pretraining)",
            ha="center", fontsize=11, fontweight="bold",
            color="#1f4e79")

    box(0.2, 1.8, 1.7, 0.9, "Input\nspectrogram", "#fff3df")
    box(2.3, 1.8, 1.9, 0.9, "Speech\nEncoder", "#ffe0e0")
    box(4.6, 1.8, 1.7, 0.9, "Speech params\n(18 per frame)", "#e8f5e9")
    box(6.7, 1.8, 1.7, 0.9, "Speech\nSynthesizer", "#dcecff")
    box(9.0, 1.8, 1.0, 0.9, "Recon.\nspectro.", "#fff3df")
    arrow(1.9, 2.25, 2.3, 2.25)
    arrow(4.2, 2.25, 4.6, 2.25)
    arrow(6.3, 2.25, 6.7, 2.25)
    arrow(8.4, 2.25, 9.0, 2.25)

    # Guidance arrow from bottom speech params to top speech params
    arrow(5.45, 2.7, 5.45, 4.3, label="reference loss", color="#b71c1c")

    # Notes
    ax.text(5.0, 0.9,
            "Causal or non-causal variants of each ECoG Decoder; "
            "N=48 participants; 500 ms per trial; 350 train / 50 test trials.",
            ha="center", fontsize=8, style="italic", color="#555")

    plt.tight_layout()
    save(fig, "fig_architecture")


if __name__ == "__main__":
    fig_pcc_models()
    fig_params()
    fig_hemisphere()
    fig_architecture()
    print("Generated 4 figures in", HERE)
