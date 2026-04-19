"""Generate figures for the multiscale spine framework paper.

All numerical values used here come verbatim from the experimental log:
  - Sample sizes: n=12 Hayama, n=16 Jyogashima, n=9 Tateyama
    (source: idea_summary methods sentence on shell collection)
  - g1 shifts: Jyogashima +0.25 vs Hayama (p=1.202e-5)
              Jyogashima +0.40 vs Tateyama (p=5.7e-6)
    (source: experimental_log methods_sentences[2])

Schematic figures (framework + morphospace) use only structural descriptions
from the idea summary and do not introduce new numerical values.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
OUT = os.path.dirname(os.path.abspath(__file__))


def save(name):
    plt.savefig(os.path.join(OUT, f"{name}.pdf"))
    plt.savefig(os.path.join(OUT, f"{name}.png"), dpi=200)
    plt.close()


# ---------------------------------------------------------------------------
# Figure 1: Framework schematic
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.0, 3.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis("off")

boxes = [
    (0.3, 1.3, 2.2, 1.4, "Molecular:\nActivator-Substrate\n{c1,c2,c3,c4,d1,d2}", PALETTE[0]),
    (3.0, 1.3, 2.2, 1.4, "Tissue:\nMorphoelastic rod\n{g1, g2}", PALETTE[1]),
    (5.7, 1.3, 2.2, 1.4, "Spine shape\n(time sequence)", PALETTE[2]),
    (8.4, 1.3, 1.4, 1.4, "Real\nshell spine", PALETTE[3]),
]
for (x, y, w, h, label, color) in boxes:
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                 linewidth=1.2, edgecolor=color, facecolor="white"))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=9)

for (x0, x1) in [(2.5, 3.0), (5.2, 5.7), (7.9, 8.4)]:
    ax.add_patch(FancyArrowPatch((x0, 2.0), (x1, 2.0), arrowstyle="->",
                                  mutation_scale=15, color="#333333"))

# QD loop: back from tissue (g1,g2) to molecular archive
ax.add_patch(FancyArrowPatch((4.1, 1.3), (1.4, 1.3), arrowstyle="->",
                              connectionstyle="arc3,rad=0.35",
                              mutation_scale=15, color="#888888"))
ax.text(2.75, 0.55, "MAP-Elites archive: {g1,g2} $\\to$ {c1,...,c4}",
        ha="center", va="center", fontsize=9, color="#555555")

ax.text(9.1, 3.4, "matching",
        ha="center", va="center", fontsize=9, color="#555555")
ax.text(5.0, 3.6, "Multiscale framework schematic",
        ha="center", va="center", fontsize=11, weight="bold")

plt.tight_layout()
save("fig_framework")


# ---------------------------------------------------------------------------
# Figure 2: Morphospace schematic (qualitative; g1 vs g2)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.0, 4.0))
g1_vals = [0.25, 0.5, 0.75]
g2_vals = [0.25, 0.5, 0.75]

for i, g1 in enumerate(g1_vals):
    for j, g2 in enumerate(g2_vals):
        # Qualitative spine silhouette: taller/straighter for lower g1,
        # more curved for higher g1, wider for higher g2.
        theta = np.linspace(0, np.pi * (0.4 + 0.7 * g1), 50)
        # Length decreases mildly with g1 (self-contact earlier), width ~ g2
        R = 0.35 * (1 - 0.3 * g1)
        cx = 0.5 + i
        cy = 0.5 + j
        x = cx + R * np.sin(theta) * (0.5 + g2)
        y = cy + R * (1 - np.cos(theta))
        ax.plot(x, y, color=PALETTE[0], linewidth=1.4)
        ax.plot([cx - 0.25 - 0.2 * g2, cx + 0.25 + 0.2 * g2],
                [cy, cy], color="#aaaaaa", linewidth=0.8)

ax.set_xticks([0.5, 1.5, 2.5])
ax.set_xticklabels([f"g1={v}" for v in g1_vals])
ax.set_yticks([0.5, 1.5, 2.5])
ax.set_yticklabels([f"g2={v}" for v in g2_vals])
ax.set_xlim(0, 3.2)
ax.set_ylim(0, 3.2)
ax.set_xlabel("g1 (growth rate)")
ax.set_ylabel("g2 (growing-region width)")
ax.set_title("Morphospace of simulated spine shapes")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
save("fig_morphospace")


# ---------------------------------------------------------------------------
# Figure 3: Population sample sizes
# ---------------------------------------------------------------------------
populations = ["Hayama", "Jyogashima", "Tateyama"]
n_shells = [12, 16, 9]   # from idea_summary methods shell collection
colors = [PALETTE[1], PALETTE[0], PALETTE[2]]

fig, ax = plt.subplots(figsize=(4.5, 3.2))
bars = ax.bar(populations, n_shells, color=colors, edgecolor="black", linewidth=0.6)
for bar, n in zip(bars, n_shells):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f"n={n}", ha="center", va="bottom", fontsize=10)
ax.set_ylabel("Number of shells collected")
ax.set_ylim(0, 20)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("Shell specimens per population")
plt.tight_layout()
save("fig_sample_sizes")


# ---------------------------------------------------------------------------
# Figure 4: Population-level g1 shifts with p-values
# ---------------------------------------------------------------------------
# Values sourced verbatim from experimental_log methods_sentences[2]:
#   Jyogashima g1 is on average 0.25 higher than Hayama (p = 1.202e-5)
#   Jyogashima g1 is on average 0.40 higher than Tateyama (p = 5.7e-6)
comparisons = ["Jyogashima\nvs Hayama", "Jyogashima\nvs Tateyama"]
shifts = [0.25, 0.40]
pvals = [1.202e-5, 5.7e-6]
colors = [PALETTE[0], PALETTE[2]]

fig, ax = plt.subplots(figsize=(4.8, 3.4))
bars = ax.bar(comparisons, shifts, color=colors, edgecolor="black", linewidth=0.6)
for bar, s, p in zip(bars, shifts, pvals):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015,
            f"+{s:.2f}\np = {p:.2e}", ha="center", va="bottom", fontsize=9)
ax.set_ylabel("Mean g1 shift (Jyogashima minus comparator)")
ax.set_ylim(0, 0.55)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("Population-level g1 differences\n(two-sided Wilcoxon rank-sum)")
plt.tight_layout()
save("fig_population_g1")

print("All figures written.")
