"""Generate all figures for the Estimated Value paper.

Every numeric value below traces back to a sentence in the experimental log.
No values are invented.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = os.path.dirname(os.path.abspath(__file__))

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
    fig.savefig(os.path.join(OUT, name + ".png"), bbox_inches="tight", dpi=200)
    plt.close(fig)


# =============================================================================
# Figure 1: Task schematic (SCHEMATIC)
# Based on extraction: "choices between a certain gain ($5 / slight improvement)
# and a risky or ambiguous alternative with four possible outcomes."
# Four scenario panels: risky monetary, ambiguous monetary, risky medical,
# ambiguous medical. (From experimental log "four scenarios: risky monetary
# decisions (A), ambiguous monetary decisions (B), risky medical decisions (C),
# and ambiguous medical decisions (D)".)
# =============================================================================
def fig_task_schematic():
    fig, axes = plt.subplots(1, 4, figsize=(11, 2.8))
    titles = [
        "A. Risky monetary",
        "B. Ambiguous monetary",
        "C. Risky medical",
        "D. Ambiguous medical",
    ]
    # Risk probabilities used: 25%, 50%, 75% (extracted verbatim)
    # Ambiguity occluder sizes: 24%, 50%, 74% (extracted verbatim)
    for ax, title in zip(axes, titles):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_title(title, fontsize=10)
        ax.axis("off")

        # Certain option on left: $5 or slight improvement
        certain = FancyBboxPatch(
            (0.05, 0.35), 0.28, 0.3,
            boxstyle="round,pad=0.02",
            linewidth=1.2, edgecolor="black", facecolor="#f0f0f0",
        )
        ax.add_patch(certain)
        if "monetary" in title:
            ax.text(0.19, 0.5, "$5\nfor sure", ha="center", va="center", fontsize=9)
        else:
            ax.text(0.19, 0.5, "Slight\nimprovement", ha="center", va="center",
                    fontsize=9)

        # Uncertain lottery on right: bag with red/blue split
        x0, y0, w, h = 0.55, 0.18, 0.4, 0.64
        # Red/blue chip bag
        ax.add_patch(Rectangle((x0, y0), w, h / 2, facecolor="#4c72b0",
                               edgecolor="black", linewidth=1.0))
        ax.add_patch(Rectangle((x0, y0 + h / 2), w, h / 2, facecolor="#c44e52",
                               edgecolor="black", linewidth=1.0))

        if "Risky" in title:
            # Label probabilities 25/75 (representative)
            ax.text(x0 + w / 2, y0 + h / 4, "75%", ha="center", va="center",
                    color="white", fontsize=9, fontweight="bold")
            ax.text(x0 + w / 2, y0 + 3 * h / 4, "25%", ha="center", va="center",
                    color="white", fontsize=9, fontweight="bold")
        else:
            # Grey occluder showing ambiguity (e.g. 50% occluder)
            ax.add_patch(Rectangle((x0, y0 + h * 0.25), w, h * 0.5,
                                   facecolor="#7a7a7a", edgecolor="black",
                                   linewidth=1.0))
            ax.text(x0 + w / 2, y0 + h / 2, "?", ha="center", va="center",
                    color="white", fontsize=14, fontweight="bold")

        if "monetary" in title:
            ax.text(x0 + w / 2, y0 - 0.08, "$5/$8/$12/$25",
                    ha="center", va="top", fontsize=8)
        else:
            ax.text(x0 + w / 2, y0 - 0.08, "slight/moderate/\nmajor/complete",
                    ha="center", va="top", fontsize=8)

        # Choice bracket
        ax.annotate("", xy=(0.33, 0.5), xytext=(0.55, 0.5),
                    arrowprops=dict(arrowstyle="<->", color="black", lw=1.0))
        ax.text(0.44, 0.58, "choose", ha="center", va="bottom", fontsize=8,
                style="italic")

    fig.suptitle(
        "Risk probabilities: 25%, 50%, 75%   |   "
        "Ambiguity occluder sizes: 24%, 50%, 74%",
        fontsize=9, y=0.02,
    )
    save(fig, "fig1_task_schematic")


# =============================================================================
# Figure 2: Estimated added subjective values per category (DATA-GROUNDED)
# Values extracted verbatim from the experimental log "Results" section.
# Medical (in-person):  slight=6.93 (SD 1.79); +9.00 (2.62); +7.04 (2.89); +4.18 (2.41)
# Monetary (in-person): $5=7.22 (1.60); +4.13 (1.47); +6.23 (2.18); +8.77 (3.41)
# Medical (online):     slight=8.63 (2.54); +12.62 (4.25); +4.66 (2.56); +2.37 (1.61)
# Monetary (online):    $5=10.91 (2.72); +4.13 (1.84); +5.04 (2.35); +3.92 (2.18)
# =============================================================================
def fig_estimated_values():
    # Categories in the extraction use these exact labels.
    med_labels = ["slight", "moderate", "major", "complete"]
    mon_labels = ["$5", "$8", "$12", "$25"]

    # ADDED values (baseline then increments); the paper reports these as
    # "added values" per category.
    med_in = np.array([6.93, 9.00, 7.04, 4.18])
    med_in_sd = np.array([1.79, 2.62, 2.89, 2.41])
    mon_in = np.array([7.22, 4.13, 6.23, 8.77])
    mon_in_sd = np.array([1.60, 1.47, 2.18, 3.41])

    med_on = np.array([8.63, 12.62, 4.66, 2.37])
    med_on_sd = np.array([2.54, 4.25, 2.56, 1.61])
    mon_on = np.array([10.91, 4.13, 5.04, 3.92])
    mon_on_sd = np.array([2.72, 1.84, 2.35, 2.18])

    fig, axes = plt.subplots(2, 2, figsize=(8.8, 5.8))

    panels = [
        (axes[0, 0], "A. Medical (in-person, n=66)", med_labels, med_in, med_in_sd),
        (axes[0, 1], "B. Monetary (in-person, n=66)", mon_labels, mon_in, mon_in_sd),
        (axes[1, 0], "C. Medical (online, n=332)", med_labels, med_on, med_on_sd),
        (axes[1, 1], "D. Monetary (online, n=332)", mon_labels, mon_on, mon_on_sd),
    ]

    for ax, title, labels, means, sds in panels:
        x = np.arange(len(labels))
        ax.bar(x, means, yerr=sds, capsize=4, color=PALETTE[0],
               edgecolor="black", linewidth=0.8, alpha=0.85)
        for xi, m, s in zip(x, means, sds):
            ax.text(xi, m + s + 0.3, f"{m:.2f}", ha="center", va="bottom",
                    fontsize=8)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylabel("Added subjective value")
        ax.set_title(title)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_ylim(bottom=0)

    fig.tight_layout()
    save(fig, "fig2_estimated_values")


# =============================================================================
# Figure 3: Cross-domain association in ambiguity aversion beta (DATA-GROUNDED)
# Slopes + 89% HDPi from extraction:
# In-person:  mean slope = 0.76, 89% HDPi [0.63, 0.91]
# Online:     mean slope = 0.37, 89% HDPi [0.29, 0.44]
# We plot the two slopes as point estimates with the HDPi bars.  The x-axis
# is "sample", the y-axis is the slope (cross-domain regression coefficient).
# =============================================================================
def fig_cross_domain():
    fig, ax = plt.subplots(figsize=(5.0, 3.6))
    samples = ["In-person\n(n=66)", "Online\n(n=332)"]
    slopes = [0.76, 0.37]
    lows = [0.63, 0.29]
    highs = [0.91, 0.44]
    lower_err = [s - l for s, l in zip(slopes, lows)]
    upper_err = [h - s for s, h in zip(slopes, highs)]

    x = np.arange(len(samples))
    ax.errorbar(x, slopes, yerr=[lower_err, upper_err], fmt="o",
                markersize=9, color=PALETTE[3], ecolor="black", capsize=6,
                linewidth=2)
    for xi, s in zip(x, slopes):
        ax.text(xi + 0.08, s, f"{s:.2f}", va="center", fontsize=10,
                fontweight="bold")
    ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    ax.set_xticks(x)
    ax.set_xticklabels(samples)
    ax.set_ylabel(r"Robust regression slope:  medical $\beta$ on monetary $\beta$")
    ax.set_title("Cross-domain association in ambiguity aversion")
    ax.set_ylim(-0.1, 1.1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # HDPi labels
    ax.text(0, -0.05, "89% HDPi\n[0.63, 0.91]", ha="center", va="top",
            fontsize=8, color="gray")
    ax.text(1, -0.05, "89% HDPi\n[0.29, 0.44]", ha="center", va="top",
            fontsize=8, color="gray")
    fig.tight_layout()
    save(fig, "fig3_cross_domain")


# =============================================================================
# Figure 4: Simulation grid (DATA-GROUNDED)
# From extraction: tested (N, noise) = (30,0.1), (30,0.3), (30,0.5), (60,0.3),
# (60,0.5), (120,0.5), (300,0.5).  "With lower noise (0.1), the classic utility
# model provided a better fit.  However, as noise increased to 0.3 and 0.5, the
# estimated value model consistently showed superior performance, regardless of
# the number of subjects."
# We display the grid as a heat-map of which model wins.
# =============================================================================
def fig_simulations():
    pairs = [(30, 0.1), (30, 0.3), (30, 0.5),
             (60, 0.3), (60, 0.5),
             (120, 0.5), (300, 0.5)]
    winners = ["Classical", "Estimated", "Estimated",
               "Estimated", "Estimated", "Estimated", "Estimated"]

    Ns = sorted({p[0] for p in pairs})
    noises = sorted({p[1] for p in pairs})

    # Grid of tested / which model wins / not tested
    # 0 = not tested, 1 = Classical wins, 2 = Estimated wins
    grid = np.zeros((len(Ns), len(noises)), dtype=int)
    for (n, s), w in zip(pairs, winners):
        i = Ns.index(n)
        j = noises.index(s)
        grid[i, j] = 1 if w == "Classical" else 2

    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    cmap_vals = np.where(grid == 0, np.nan, grid.astype(float))

    # Draw the cells manually so we can label them clearly.
    for i, n in enumerate(Ns):
        for j, s in enumerate(noises):
            v = grid[i, j]
            if v == 0:
                ax.add_patch(Rectangle((j, i), 1, 1, facecolor="#f0f0f0",
                                       edgecolor="white", linewidth=1.5))
                ax.text(j + 0.5, i + 0.5, "—", ha="center", va="center",
                        color="gray", fontsize=10)
            else:
                color = PALETTE[1] if v == 1 else PALETTE[2]
                ax.add_patch(Rectangle((j, i), 1, 1, facecolor=color,
                                       edgecolor="white", linewidth=1.5,
                                       alpha=0.85))
                label = "Classical" if v == 1 else "Estimated"
                ax.text(j + 0.5, i + 0.5, label, ha="center", va="center",
                        color="white", fontsize=9, fontweight="bold")

    ax.set_xticks(np.arange(len(noises)) + 0.5)
    ax.set_xticklabels([f"{s:.1f}" for s in noises])
    ax.set_yticks(np.arange(len(Ns)) + 0.5)
    ax.set_yticklabels([f"N = {n}" for n in Ns])
    ax.set_xlim(0, len(noises))
    ax.set_ylim(len(Ns), 0)
    ax.set_xlabel("Simulation noise (SD)")
    ax.set_ylabel("Number of simulated participants")
    ax.set_title("Winning model in LOO comparison")
    ax.set_aspect("equal")
    fig.tight_layout()
    save(fig, "fig4_simulations")


if __name__ == "__main__":
    fig_task_schematic()
    fig_estimated_values()
    fig_cross_domain()
    fig_simulations()
    print("Generated 4 figures.")
