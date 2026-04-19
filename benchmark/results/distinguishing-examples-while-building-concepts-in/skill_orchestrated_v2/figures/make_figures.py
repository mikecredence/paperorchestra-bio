"""Generate figures for distinguishing-examples-while-building-concepts paper.

All numerical values come from the experimental log verbatim. No fabricated data.
"""
import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
OUT = os.path.dirname(os.path.abspath(__file__))


def save(fig, name):
    fig.savefig(os.path.join(OUT, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ----------------------------------------------------------------------------
# Figure 1: Pathway schematic (EC -> DG -> MF -> CA3 and EC -> PP -> CA3)
# ----------------------------------------------------------------------------
def fig_pathways():
    fig, ax = plt.subplots(figsize=(6.5, 3.2))

    def box(xy, w, h, text, color):
        p = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02",
                           linewidth=1.2, facecolor=color, edgecolor="black")
        ax.add_patch(p)
        ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center",
                fontsize=10)

    # EC, DG, CA3 boxes
    box((0.02, 0.40), 0.16, 0.25, "EC", "#e6f0fa")
    box((0.40, 0.70), 0.16, 0.22, "DG", "#efe6fa")
    box((0.76, 0.40), 0.18, 0.25, "CA3", "#fae6e6")

    # Arrows: EC -> DG (part of MF route), EC -> CA3 (PP direct)
    a1 = FancyArrowPatch((0.18, 0.60), (0.40, 0.82), arrowstyle="->",
                         color=PALETTE[4], lw=1.6, mutation_scale=14)
    ax.add_patch(a1)
    a2 = FancyArrowPatch((0.56, 0.78), (0.76, 0.58), arrowstyle="->",
                         color=PALETTE[4], lw=1.6, mutation_scale=14)
    ax.add_patch(a2)
    # EC -> CA3 direct (PP)
    a3 = FancyArrowPatch((0.18, 0.50), (0.76, 0.50), arrowstyle="->",
                         color=PALETTE[1], lw=1.8, mutation_scale=14,
                         connectionstyle="arc3,rad=-0.15")
    ax.add_patch(a3)

    ax.text(0.30, 0.92, "~4000 synapses", fontsize=8, color=PALETTE[4])
    ax.text(0.62, 0.88, "MF: ~50 synapses", fontsize=8, color=PALETTE[4])
    ax.text(0.30, 0.33, "PP: ~4000 synapses (dense, correlated)", fontsize=8,
            color=PALETTE[1])

    ax.set_xlim(0, 1)
    ax.set_ylim(0.15, 1)
    ax.axis("off")
    ax.set_title("Hippocampal pathways to CA3: dual MF and PP inputs",
                 fontsize=11)
    save(fig, "fig_pathways")


# ----------------------------------------------------------------------------
# Figure 2: Encoding statistics across regions (density and correlation)
# ----------------------------------------------------------------------------
def fig_density_correlation():
    regions = ["EC", "DG", "MF (CA3)", "PP (CA3)"]
    # From experimental_log.md (Methods): aEC=0.1, aDG=0.005, aMF=0.02, aPP=0.2
    densities = [0.10, 0.005, 0.02, 0.20]
    # Within-concept correlations: rhoEC=0.15, rhoDG=0.02, rhoMF=0.01, rhoPP=0.09
    correlations = [0.15, 0.02, 0.01, 0.09]

    x = np.arange(len(regions))
    width = 0.38

    fig, ax = plt.subplots(figsize=(6.2, 3.5))
    bars1 = ax.bar(x - width / 2, densities, width,
                   label="Density $a$", color=PALETTE[0])
    bars2 = ax.bar(x + width / 2, correlations, width,
                   label=r"Within-concept correlation $\rho$",
                   color=PALETTE[1])

    for b, v in zip(bars1, densities):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.005, f"{v:g}",
                ha="center", va="bottom", fontsize=8)
    for b, v in zip(bars2, correlations):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.005, f"{v:g}",
                ha="center", va="bottom", fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(regions)
    ax.set_ylabel("Value")
    ax.set_ylim(0, 0.25)
    ax.set_title("Encoding statistics by region")
    ax.legend(frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    save(fig, "fig_density_correlation")


# ----------------------------------------------------------------------------
# Figure 3: Valid cell counts per analysis
# ----------------------------------------------------------------------------
def fig_valid_cells():
    # From experimental_log.md: Fig 6E scales yield 47/49/56 CA3 and
    # 122/137/144 CA1 at track scales 1/16, 1/8, 1/4.
    scales = ["1/16", "1/8", "1/4"]
    ca3 = [47, 49, 56]
    ca1 = [122, 137, 144]
    x = np.arange(len(scales))
    width = 0.38

    # Two-panel: left = track scale analysis; right = W-maze + fields counts.
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.3))

    b1 = ax1.bar(x - width / 2, ca3, width, label="CA3", color=PALETTE[3])
    b2 = ax1.bar(x + width / 2, ca1, width, label="CA1", color=PALETTE[0])
    for b, v in zip(list(b1) + list(b2), ca3 + ca1):
        ax1.text(b.get_x() + b.get_width() / 2, v + 2, str(v),
                 ha="center", va="bottom", fontsize=8)
    ax1.set_xticks(x)
    ax1.set_xticklabels(scales)
    ax1.set_xlabel("Track scale")
    ax1.set_ylabel("Valid place cells")
    ax1.set_title("Coarse-position analysis (Fig. 6E)")
    ax1.legend(frameon=False)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Right panel: valid fields Fig 5L (35 CA3, 47 CA1) and W-maze (99, 187).
    labels = ["Place fields\n(Fig. 5L)", "W-maze neurons\n(Fig. 7)"]
    ca3_r = [35, 99]
    ca1_r = [47, 187]
    xr = np.arange(len(labels))
    b3 = ax2.bar(xr - width / 2, ca3_r, width, label="CA3", color=PALETTE[3])
    b4 = ax2.bar(xr + width / 2, ca1_r, width, label="CA1", color=PALETTE[0])
    for b, v in zip(list(b3) + list(b4), ca3_r + ca1_r):
        ax2.text(b.get_x() + b.get_width() / 2, v + 3, str(v),
                 ha="center", va="bottom", fontsize=8)
    ax2.set_xticks(xr)
    ax2.set_xticklabels(labels)
    ax2.set_ylabel("Valid cells / fields")
    ax2.set_title("Inclusion counts")
    ax2.legend(frameon=False)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    save(fig, "fig_valid_cells")


# ----------------------------------------------------------------------------
# Figure 4: Multitask ML architecture schematic with HalfCorr
# ----------------------------------------------------------------------------
def fig_ml_schematic():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))

    def box(xy, w, h, text, color):
        p = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02",
                           linewidth=1.1, facecolor=color, edgecolor="black")
        ax.add_patch(p)
        ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center",
                fontsize=9)

    def arrow(a, b):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="->", lw=1.2,
                                     mutation_scale=10, color="black"))

    # Input
    box((0.02, 0.40), 0.14, 0.20, "Input\nMNIST", "#eeeeee")
    # Hidden 1 (100 neurons)
    box((0.22, 0.40), 0.18, 0.20, "Hidden 1\n(100, tanh)", "#e6f0fa")
    # Hidden 2 split: correlated half (50) + decorrelated half (50)
    box((0.46, 0.56), 0.20, 0.16, "Correlated half\n(50 neurons)", "#ffe0cc")
    box((0.46, 0.30), 0.20, 0.16, "Decorrelated half\n(50 neurons, HalfCorr)",
        "#e0ccff")
    # Output heads
    box((0.76, 0.56), 0.20, 0.16, "Digit head\n(10 classes)", "#eeeeee")
    box((0.76, 0.30), 0.20, 0.16, "Set head\n(S classes)", "#eeeeee")

    arrow((0.16, 0.50), (0.22, 0.50))
    arrow((0.40, 0.55), (0.46, 0.64))
    arrow((0.40, 0.45), (0.46, 0.38))
    arrow((0.66, 0.64), (0.76, 0.64))
    arrow((0.66, 0.38), (0.76, 0.38))

    ax.text(0.56, 0.18,
            "HalfCorr: DeCorr penalty applied to second half only\n"
            "(Baseline: no penalty; DeCorr: both halves)",
            ha="center", fontsize=9, style="italic", color="dimgray")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.1, 0.82)
    ax.axis("off")
    ax.set_title("Multitask perceptron with HalfCorr loss (Fig. 8 analogue)")
    save(fig, "fig_ml_schematic")


# ----------------------------------------------------------------------------
# Figure 5: Threshold-selected retrieval schematic
# ----------------------------------------------------------------------------
def fig_retrieval_schematic():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.0))

    # Threshold trace
    t = np.linspace(0, 4 * np.pi, 400)
    theta_trace = 0.35 + 0.25 * np.sign(np.sin(t))
    ax1.plot(t, theta_trace, color="black", lw=1.4)
    ax1.fill_between(t, 0.60, where=(theta_trace > 0.5),
                     color=PALETTE[0], alpha=0.15, label=r"high $\theta$ (sparse)")
    ax1.fill_between(t, 0, 0.60, where=(theta_trace < 0.25),
                     color=PALETTE[1], alpha=0.15, label=r"low $\theta$ (dense)")
    ax1.set_ylabel(r"Threshold $\theta'$")
    ax1.set_xlabel("Time (arbitrary)")
    ax1.set_yticks([0.0, 0.25, 0.5])
    ax1.set_title("Theta-like threshold oscillation")
    ax1.set_xticks([])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.legend(frameon=False, loc="center right", fontsize=8)

    # Schematic: high threshold -> MF example; low threshold -> PP concept.
    ax2.axis("off")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    ax2.add_patch(FancyBboxPatch((0.05, 0.55), 0.40, 0.30,
                                 boxstyle="round,pad=0.02",
                                 facecolor="#e6f0fa", edgecolor="black"))
    ax2.text(0.25, 0.78, "High $\\theta'$ = 0.5", ha="center", fontsize=10)
    ax2.text(0.25, 0.63, "Sparse, decorrelated\nMF example retrieved",
             ha="center", fontsize=9, color=PALETTE[4])

    ax2.add_patch(FancyBboxPatch((0.55, 0.15), 0.40, 0.30,
                                 boxstyle="round,pad=0.02",
                                 facecolor="#ffe0cc", edgecolor="black"))
    ax2.text(0.75, 0.38, "Low $\\theta'$ = 0", ha="center", fontsize=10)
    ax2.text(0.75, 0.23, "Dense, correlated\nPP concept retrieved",
             ha="center", fontsize=9, color=PALETTE[1])

    ax2.annotate("", xy=(0.55, 0.35), xytext=(0.45, 0.65),
                 arrowprops=dict(arrowstyle="->", color="gray"))
    ax2.set_title("Threshold selects retrieval mode")

    plt.tight_layout()
    save(fig, "fig_retrieval_schematic")


if __name__ == "__main__":
    fig_pathways()
    fig_density_correlation()
    fig_valid_cells()
    fig_ml_schematic()
    fig_retrieval_schematic()
    print("All figures written to", OUT)
