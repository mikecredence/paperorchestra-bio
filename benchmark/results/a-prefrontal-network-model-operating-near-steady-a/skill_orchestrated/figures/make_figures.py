"""
Figure generation for the prefrontal network model paper.
All numerical values are taken verbatim from the experimental log.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# Academic styling
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "figure.dpi": 100,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
})

COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

OUT = Path(__file__).parent


# =============================================================
# Figure 1: Firing rates comparison (DATA-GROUNDED)
# Source: experimental log reports these exact values for steady
# and critical state networks at baseline and +5% input.
# =============================================================
def fig_firing_rates():
    conditions = ["Baseline\n(νX = 5 Hz)", "+5% input"]
    # Steady state: 5.2/20 (baseline), 7.8/26 (+5%)
    # Critical state: 5.5/21 (baseline), 15/42 (+5%)
    steady_E = [5.2, 7.8]
    steady_I = [20, 26]
    critical_E = [5.5, 15]
    critical_I = [21, 42]

    x = np.arange(len(conditions))
    width = 0.2

    fig, axes = plt.subplots(1, 2, figsize=(8, 3.2), sharex=True)

    # Panel A: Excitatory rates
    ax = axes[0]
    ax.bar(x - width/2, steady_E, width, label="Steady state",
           color=COLORS[0], edgecolor="black", linewidth=0.5)
    ax.bar(x + width/2, critical_E, width, label="Critical state",
           color=COLORS[1], edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Excitatory firing rate νE (Hz)")
    ax.set_xticks(x)
    ax.set_xticklabels(conditions)
    ax.set_title("A. Excitatory population")
    ax.legend(frameon=False, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Annotate values
    for i, v in enumerate(steady_E):
        ax.text(i - width/2, v + 0.3, f"{v}", ha="center", fontsize=8)
    for i, v in enumerate(critical_E):
        ax.text(i + width/2, v + 0.3, f"{v}", ha="center", fontsize=8)

    # Panel B: Inhibitory rates
    ax = axes[1]
    ax.bar(x - width/2, steady_I, width, label="Steady state",
           color=COLORS[0], edgecolor="black", linewidth=0.5)
    ax.bar(x + width/2, critical_I, width, label="Critical state",
           color=COLORS[1], edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Inhibitory firing rate νI (Hz)")
    ax.set_xticks(x)
    ax.set_xticklabels(conditions)
    ax.set_title("B. Inhibitory population")
    ax.legend(frameon=False, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for i, v in enumerate(steady_I):
        ax.text(i - width/2, v + 0.8, f"{v}", ha="center", fontsize=8)
    for i, v in enumerate(critical_I):
        ax.text(i + width/2, v + 0.8, f"{v}", ha="center", fontsize=8)

    plt.tight_layout()
    plt.savefig(OUT / "fig_firing_rates.pdf")
    plt.savefig(OUT / "fig_firing_rates.png")
    plt.close()


# =============================================================
# Figure 2: Model vs experiment comparison (DATA-GROUNDED)
# Source: experimental log reports ~50 Hz model, ~55 Hz experimental,
# 58 Hz theoretical onset, ±20 ms model, ±18 ms experimental.
# =============================================================
def fig_model_vs_experiment():
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.2))

    # Panel A: Oscillation frequencies
    ax = axes[0]
    labels = ["Experimental\n(PFC data)", "Model\n(simulation)", "Theory\n(onset)"]
    freqs = [55, 50, 58]
    bars = ax.bar(labels, freqs,
                  color=[COLORS[3], COLORS[0], COLORS[2]],
                  edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Oscillation frequency (Hz)")
    ax.set_title("A. Network oscillation frequency")
    ax.set_ylim(0, 70)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bar, v in zip(bars, freqs):
        ax.text(bar.get_x() + bar.get_width()/2, v + 1.5, f"{v} Hz",
                ha="center", fontsize=9)

    # Panel B: Correlation peak lags
    ax = axes[1]
    labels_lag = ["Experimental", "Model"]
    lags = [18, 20]
    bars = ax.bar(labels_lag, lags,
                  color=[COLORS[3], COLORS[0]],
                  edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Correlation peak lag (ms)")
    ax.set_title("B. Temporal correlation structure")
    ax.set_ylim(0, 26)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bar, v in zip(bars, lags):
        ax.text(bar.get_x() + bar.get_width()/2, v + 0.5, f"±{v} ms",
                ha="center", fontsize=9)

    plt.tight_layout()
    plt.savefig(OUT / "fig_model_vs_experiment.pdf")
    plt.savefig(OUT / "fig_model_vs_experiment.png")
    plt.close()


# =============================================================
# Figure 3: Network architecture schematic (SCHEMATIC)
# Source: N=5000 (NE=4000 excitatory, NI=1000 inhibitory),
# p=0.2, four synaptic currents (AMPA, NMDA, GABA, external AMPA).
# =============================================================
def fig_network_schematic():
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Excitatory population box (bigger, NE = 4000 = 80%)
    exc_box = FancyBboxPatch((1.0, 2.5), 3.0, 2.0,
                              boxstyle="round,pad=0.1",
                              facecolor="#ffcccc",
                              edgecolor="#d62728", linewidth=1.5)
    ax.add_patch(exc_box)
    ax.text(2.5, 3.7, "Excitatory", ha="center", fontsize=11, fontweight="bold")
    ax.text(2.5, 3.3, "N_E = 4,000", ha="center", fontsize=10)
    ax.text(2.5, 2.9, "(80%)", ha="center", fontsize=9, style="italic")

    # Inhibitory population box (smaller, NI = 1000 = 20%)
    inh_box = FancyBboxPatch((5.5, 2.8), 2.2, 1.5,
                              boxstyle="round,pad=0.1",
                              facecolor="#ccccff",
                              edgecolor="#1f77b4", linewidth=1.5)
    ax.add_patch(inh_box)
    ax.text(6.6, 3.7, "Inhibitory", ha="center", fontsize=11, fontweight="bold")
    ax.text(6.6, 3.3, "N_I = 1,000", ha="center", fontsize=10)
    ax.text(6.6, 2.95, "(20%)", ha="center", fontsize=9, style="italic")

    # Recurrent excitatory (AMPA + NMDA) — E to I
    arr1 = FancyArrowPatch((4.0, 3.7), (5.5, 3.7),
                            arrowstyle="->", mutation_scale=15,
                            color="#d62728", linewidth=1.5)
    ax.add_patch(arr1)
    ax.text(4.75, 3.95, "AMPA\n+NMDA", ha="center", fontsize=8, color="#d62728")

    # Inhibitory feedback (GABA) — I to E
    arr2 = FancyArrowPatch((5.5, 3.1), (4.0, 3.1),
                            arrowstyle="->", mutation_scale=15,
                            color="#1f77b4", linewidth=1.5)
    ax.add_patch(arr2)
    ax.text(4.75, 2.75, "GABA", ha="center", fontsize=8, color="#1f77b4")

    # Recurrent excitatory self-loop (E to E)
    arr3 = mpatches.FancyArrowPatch((1.2, 4.4), (1.2, 4.9),
                                    arrowstyle="->", mutation_scale=12,
                                    color="#d62728", linewidth=1.2,
                                    connectionstyle="arc3,rad=1.2")
    ax.add_patch(arr3)
    ax.text(0.4, 4.7, "E→E", fontsize=8, color="#d62728")

    # Inhibitory self-loop (I to I)
    arr4 = mpatches.FancyArrowPatch((7.5, 4.2), (7.5, 4.7),
                                    arrowstyle="->", mutation_scale=12,
                                    color="#1f77b4", linewidth=1.2,
                                    connectionstyle="arc3,rad=1.2")
    ax.add_patch(arr4)
    ax.text(8.0, 4.4, "I→I", fontsize=8, color="#1f77b4")

    # External input box
    ext_box = FancyBboxPatch((3.5, 0.5), 2.5, 1.0,
                              boxstyle="round,pad=0.05",
                              facecolor="#f0f0f0",
                              edgecolor="gray", linewidth=1)
    ax.add_patch(ext_box)
    ax.text(4.75, 1.0, "External input (AMPA)\nνX = 5 Hz",
            ha="center", fontsize=9)

    # Arrows from external to E and I
    arr5 = FancyArrowPatch((4.0, 1.5), (2.5, 2.4),
                            arrowstyle="->", mutation_scale=12,
                            color="gray", linewidth=1)
    arr6 = FancyArrowPatch((5.5, 1.5), (6.6, 2.7),
                            arrowstyle="->", mutation_scale=12,
                            color="gray", linewidth=1)
    ax.add_patch(arr5)
    ax.add_patch(arr6)

    # Title annotation
    ax.text(5, 5.6, "Prefrontal Network Model",
            ha="center", fontsize=12, fontweight="bold")
    ax.text(5, 5.2, "N = 5,000 LIF neurons, random connectivity p = 0.2",
            ha="center", fontsize=9, style="italic")

    plt.tight_layout()
    plt.savefig(OUT / "fig_network_schematic.pdf")
    plt.savefig(OUT / "fig_network_schematic.png")
    plt.close()


# =============================================================
# Figure 4: State diagram placeholder (PLACEHOLDER)
# The experimental log describes the qualitative structure of the
# state diagram in the (IAMPA/IGABA, IX/Itheta) plane but does not
# provide the exact boundary curve data.
# =============================================================
def fig_state_diagram_placeholder():
    fig, ax = plt.subplots(figsize=(5.5, 4))

    # Draw a schematic stability boundary — labeled as illustrative
    x = np.linspace(0.1, 2.5, 100)
    # A sketch-like monotonic boundary (illustrative only)
    y_boundary = 0.5 + 0.35 * np.log(x + 0.3)

    ax.fill_between(x, 0, y_boundary, alpha=0.2, color=COLORS[0],
                    label="Asynchronous stable (λ < 0)")
    ax.fill_between(x, y_boundary, 2.5, alpha=0.2, color=COLORS[3],
                    label="Synchronous oscillatory (λ > 0)")
    ax.plot(x, y_boundary, "k-", linewidth=1.5, label="Critical line (λ = 0)")

    # Mark steady and critical networks
    ax.plot(0.7, 0.2, "o", color=COLORS[0], markersize=10,
            markeredgecolor="black", label="Steady state network")
    ax.plot(1.2, 0.5, "*", color=COLORS[3], markersize=14,
            markeredgecolor="black", label="Critical state network")

    ax.set_xlabel(r"$I_{\mathrm{AMPA}} / I_{\mathrm{GABA}}$")
    ax.set_ylabel(r"$I_{X,E} / I_{\theta,E}$")
    ax.set_title("State diagram (schematic illustration)")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.set_xlim(0, 2.5)
    ax.set_ylim(0, 1.3)

    # Illustrative-only banner
    ax.text(1.25, 1.2,
            "Schematic: boundary shape not to scale",
            ha="center", fontsize=8, style="italic", color="gray",
            bbox=dict(boxstyle="round", facecolor="#f9f9f9",
                      edgecolor="gray", linewidth=0.5))

    plt.tight_layout()
    plt.savefig(OUT / "fig_state_diagram.pdf")
    plt.savefig(OUT / "fig_state_diagram.png")
    plt.close()


if __name__ == "__main__":
    print("Generating figures...")
    fig_firing_rates()
    print("  [1/4] fig_firing_rates")
    fig_model_vs_experiment()
    print("  [2/4] fig_model_vs_experiment")
    fig_network_schematic()
    print("  [3/4] fig_network_schematic")
    fig_state_diagram_placeholder()
    print("  [4/4] fig_state_diagram (schematic)")
    print("Done.")
