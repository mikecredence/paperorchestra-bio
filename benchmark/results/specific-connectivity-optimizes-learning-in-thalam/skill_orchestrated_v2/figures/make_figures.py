"""Figure generation for "Specific Connectivity Optimizes Learning in
Thalamocortical Loops" (paper-orchestrator v2 pipeline).

Every numeric value used here is traceable to a statement in the
experimental log. No values are invented.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------
# Figure 1: Architecture schematic
# ---------------------------------------------------------------------
def fig_schematic():
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis("off")

    # Cortex box
    cortex = FancyBboxPatch((0.8, 3.4), 4.0, 2.0,
                            boxstyle="round,pad=0.1",
                            fc="#e8f0fb", ec="#1f77b4", lw=1.6)
    ax.add_patch(cortex)
    ax.text(2.8, 4.4, "Cortex\nN = 256", ha="center", va="center", fontsize=10)

    # Thalamus box
    thal = FancyBboxPatch((6.5, 3.7), 2.6, 1.4,
                          boxstyle="round,pad=0.1",
                          fc="#fdeedc", ec="#ff7f0e", lw=1.6)
    ax.add_patch(thal)
    ax.text(7.8, 4.4, "Thalamus\nM = 32", ha="center", va="center", fontsize=10)

    # Recurrent arrow on cortex
    ax.annotate("", xy=(1.2, 5.2), xytext=(0.6, 4.8),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#333"))
    ax.text(0.2, 5.1, r"$W_{CC}$", fontsize=10)

    # CT arrow (cortex -> thalamus)
    ax.annotate("", xy=(6.45, 4.6), xytext=(4.85, 4.6),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#333"))
    ax.text(5.6, 4.85, r"$W_{TC}$", fontsize=10)

    # TC arrow (thalamus -> cortex)
    ax.annotate("", xy=(4.85, 4.1), xytext=(6.45, 4.1),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2ca02c"))
    ax.text(5.6, 3.75, r"$W_{CT}$ (plastic)", fontsize=10, color="#2ca02c")

    # Input arrow
    ax.annotate("", xy=(0.8, 4.4), xytext=(0.0, 4.4),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#555"))
    ax.text(0.0, 4.65, r"$x_t$", fontsize=10)

    # Output arrow
    ax.annotate("", xy=(4.8, 2.6), xytext=(2.8, 3.4),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#555"))
    ax.text(4.7, 2.5, r"$y_t = W_o h_t$", fontsize=10)

    # Caption text
    ax.text(5.0, 1.3,
            "Recurrent cortex is reciprocally connected to an uncoupled\n"
            "thalamic population via corticothalamic ($W_{TC}$) and\n"
            "thalamocortical ($W_{CT}$) weights. Only $W_{CT}$ is updated\n"
            "by the local RFLO plasticity rule.",
            ha="center", va="center", fontsize=9, color="#333")

    save(fig, "fig_schematic")


# ---------------------------------------------------------------------
# Figure 2: Idealized M=1 performance across tasks
# (data from results_subspace block in experimental log)
# ---------------------------------------------------------------------
def fig_idealized_m1():
    # Values reported verbatim:
    # Motor control: Random 1.2, PC 1.2, Readout 2.1
    # Working memory: Random 1.9, PC 2.5, Readout 1.8
    labels = ["Random", "PC", "Readout"]
    motor = [1.2, 1.2, 2.1]
    wm = [1.9, 2.5, 1.8]

    x = np.arange(len(labels))
    w = 0.38

    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    b1 = ax.bar(x - w/2, motor, w, label="Motor control", color=PALETTE[0])
    b2 = ax.bar(x + w/2, wm, w, label="Working memory", color=PALETTE[1])

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel(r"Median $-\log(1 - R^2)$")
    ax.set_title(r"Task performance at maximum compression ($M = 1$)")
    ax.legend(frameon=False, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.06,
                    f"{b.get_height():.1f}", ha="center", va="bottom", fontsize=8)
    ax.set_ylim(0, 3.0)

    save(fig, "fig_idealized_m1")


# ---------------------------------------------------------------------
# Figure 3: Cumulative thalamic variance captured by top k cortical PCs
# Uses only the two verbatim values at k=5 and the total R^2 at k=all.
# ---------------------------------------------------------------------
def fig_thalamic_variance():
    # Reported values (verbatim):
    # top-5 PC explainable variance: Motor 0.29 +/- 0.02, WM 0.63 +/- 0.04
    # total R^2 using all cortex: Motor 0.46 +/- 0.01, WM 0.70 +/- 0.01
    tasks = ["Motor control", "Working memory"]
    top5_mean = [0.29, 0.63]
    top5_err = [0.02, 0.04]
    all_mean = [0.46, 0.70]
    all_err = [0.01, 0.01]

    x = np.arange(len(tasks))
    w = 0.38

    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.bar(x - w/2, top5_mean, w, yerr=top5_err, capsize=4,
           label="Top 5 cortical PCs", color=PALETTE[0])
    ax.bar(x + w/2, all_mean, w, yerr=all_err, capsize=4,
           label="All cortical neurons", color=PALETTE[2])
    ax.set_xticks(x); ax.set_xticklabels(tasks)
    ax.set_ylabel(r"Fraction of thalamic variance explained")
    ax.set_title("Cortical dimensions capturing thalamic activity")
    ax.legend(frameon=False, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 0.85)

    save(fig, "fig_thalamic_variance")


# ---------------------------------------------------------------------
# Figure 4: Meta-learning error reduction factor
# Motor control: 5.8, Working memory: 5.1 (verbatim)
# ---------------------------------------------------------------------
def fig_metalearning_gain():
    tasks = ["Motor control", "Working memory"]
    gain = [5.8, 5.1]
    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    bars = ax.bar(tasks, gain,
                  color=[PALETTE[0], PALETTE[1]], width=0.55)
    ax.set_ylabel("Median fold error reduction\n(random vs. meta-learned $W_{TC}$)")
    ax.set_title("Meta-learned vs. random corticothalamic weights")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axhline(1.0, color="gray", ls="--", lw=0.8)
    ax.text(1.5, 1.2, "no gain", color="gray", fontsize=8, ha="right")
    for b, v in zip(bars, gain):
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.1,
                f"{v}x", ha="center", va="bottom", fontsize=10)
    ax.set_ylim(0, 7)

    save(fig, "fig_metalearning_gain")


# ---------------------------------------------------------------------
# Figure 5: Behavior decoding R^2 and sample sizes
# Motor R^2 0.93, 3 sessions, 101 thalamic neurons
# WM R^2 0.97, 5 sessions, 72 thalamic neurons (verbatim)
# ---------------------------------------------------------------------
def fig_behavior_decoding():
    tasks = ["Motor control", "Working memory"]
    r2 = [0.93, 0.97]
    sessions = [3, 5]
    neurons = [101, 72]

    fig, axes = plt.subplots(1, 2, figsize=(6.2, 3.0))

    ax = axes[0]
    bars = ax.bar(tasks, r2, color=[PALETTE[0], PALETTE[1]], width=0.55)
    ax.set_ylim(0, 1.05); ax.set_ylabel(r"$R^2$ (behavior from cortex)")
    ax.set_title("Behavior decoding")
    for b, v in zip(bars, r2):
        ax.text(b.get_x() + b.get_width()/2, v + 0.02,
                f"{v:.2f}", ha="center", va="bottom", fontsize=9)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    ax = axes[1]
    x = np.arange(len(tasks))
    w = 0.38
    ax.bar(x - w/2, sessions, w, label="Sessions", color=PALETTE[3])
    ax.bar(x + w/2, neurons, w, label="Thalamic neurons", color=PALETTE[4])
    ax.set_xticks(x); ax.set_xticklabels(tasks)
    ax.set_ylabel("Count"); ax.set_title("Dataset size")
    ax.legend(frameon=False)
    for xi, s, n in zip(x, sessions, neurons):
        ax.text(xi - w/2, s + 2, str(s), ha="center", fontsize=9)
        ax.text(xi + w/2, n + 2, str(n), ha="center", fontsize=9)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 120)

    plt.tight_layout()
    save(fig, "fig_behavior_decoding")


if __name__ == "__main__":
    fig_schematic()
    fig_idealized_m1()
    fig_thalamic_variance()
    fig_metalearning_gain()
    fig_behavior_decoding()
    print("OK: 5 figures written to", OUT)
