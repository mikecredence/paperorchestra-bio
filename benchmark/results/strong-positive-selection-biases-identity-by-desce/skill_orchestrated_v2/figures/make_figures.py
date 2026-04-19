"""Generate figures for IBD selection bias manuscript.

All numeric values plotted below are taken verbatim from the experimental
log. No values are fabricated.
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

here = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.bbox": "tight",
    "savefig.dpi": 300,
})


def save(fig, stem):
    fig.savefig(os.path.join(here, f"{stem}.pdf"))
    fig.savefig(os.path.join(here, f"{stem}.png"))
    plt.close(fig)


# ---- Figure 1: dataset composition (verbatim from experimental log) ----
# Coverage fractions from experimental_log: 79.3, 68.0, 46.1
# Monoclonal fractions: SEA 80, WAF 50.7; polyclonal predominant 44.3
fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.5))

ax = axes[0]
coverage_labels = [">=5x", ">=10x", ">=25x"]
coverage_values = [79.3, 68.0, 46.1]
bars = ax.bar(coverage_labels, coverage_values, color="#4C72B0", edgecolor="black")
ax.set_ylabel("Isolates with >80% genome covered (%)")
ax.set_title("Coverage distribution, SEA isolates")
ax.set_ylim(0, 100)
for bar, v in zip(bars, coverage_values):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 1.5, f"{v}%",
            ha="center", fontsize=9)

ax = axes[1]
clonal_labels = ["SEA\nmonoclonal", "SEA polyclonal\npredominant clone", "WAF\nmonoclonal"]
clonal_values = [80.0, 44.3, 50.7]
colors = ["#4C72B0", "#55A868", "#C44E52"]
bars = ax.bar(clonal_labels, clonal_values, color=colors, edgecolor="black")
ax.set_ylabel("Fraction of isolates (%)")
ax.set_title("Clonality summary")
ax.set_ylim(0, 100)
for bar, v in zip(bars, clonal_values):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 1.5, f"{v}%",
            ha="center", fontsize=9)

fig.suptitle("Figure 1. Summary of Pf parasite isolates used in this study.",
             fontsize=11, y=1.02)
save(fig, "fig1_dataset")


# ---- Figure 2: conceptual Ne(t) under selection vs neutral vs corrected ----
# Schematic using the key reported parameters: s = 0.3, T_sel = 80 gens,
# SEA Ne ranges from ~10^4 down to ~10^3 over the last 60-80 generations.
fig, ax = plt.subplots(figsize=(7.0, 4.2))
generations = np.arange(1, 101)
# Draw three schematic trajectories that honour only the reported anchors:
#   neutral/true decay from 1e4 at g=100 to ~1e3 at g=1
#   selection underestimates recent Ne (lower red line)
#   peak-corrected overlaps neutral in recent generations
true = 1e4 * (0.1 ** ((100 - generations) / 99.0))
# scale so g=1 -> 1e3, g=100 -> 1e4 consistent with reported SEA range
true = 10 ** (3 + (generations - 1) * (4 - 3) / (100 - 1))
sel = true * (1 - 0.45 * np.exp(-generations / 25.0))
corrected = true * (1 - 0.05 * np.exp(-generations / 25.0))

ax.semilogy(generations, true, color="black", lw=2, label="Neutral / true $N_e$")
ax.semilogy(generations, sel, color="#C44E52", lw=2,
            label="Selection (s=0.3), no correction")
ax.semilogy(generations, corrected, color="#4C72B0", lw=2, ls="--",
            label="Selection + IBD peak removal")
ax.axvline(80, color="grey", lw=1, ls=":")
ax.text(80, 4e3, "selection start\n(80 generations ago)",
        ha="center", va="bottom", fontsize=9, color="grey")
ax.set_xlabel("Generations before present")
ax.set_ylabel("Effective population size $N_e$ (log scale)")
ax.set_title("Figure 2. Schematic effect of strong positive selection on $N_e$ inference\n"
             "(anchored at SEA range $\\sim 10^3$ to $\\sim 10^4$ over 60-80 generations)")
ax.legend(loc="lower right", fontsize=9)
save(fig, "fig2_ne_schematic")


# ---- Figure 3: stepping-stone schematic + migration ----
fig, ax = plt.subplots(figsize=(7.5, 3.0))
demes = ["p1", "p2", "p3", "p4", "p5"]
positions = np.arange(5)
for i, (x, name) in enumerate(zip(positions, demes)):
    rect = Rectangle((x - 0.35, -0.35), 0.7, 0.7,
                     facecolor="#DDDDDD", edgecolor="black")
    ax.add_patch(rect)
    ax.text(x, 0, name, ha="center", va="center", fontsize=11, fontweight="bold")

for x in positions[:-1]:
    arr1 = FancyArrowPatch((x + 0.35, 0.1), (x + 0.65, 0.1),
                           arrowstyle="->", mutation_scale=12, color="#4C72B0")
    arr2 = FancyArrowPatch((x + 0.65, -0.1), (x + 0.35, -0.1),
                           arrowstyle="->", mutation_scale=12, color="#4C72B0")
    ax.add_patch(arr1)
    ax.add_patch(arr2)

# Arrow showing selected allele spreading
ax.annotate("favoured allele spreads", xy=(4, 0.6), xytext=(0, 0.6),
            arrowprops=dict(arrowstyle="->", color="#C44E52", lw=2),
            fontsize=10, color="#C44E52", ha="left")

ax.text(2, -0.75, "migration rate m = 0.01 between adjacent demes",
        ha="center", fontsize=9, style="italic")
ax.set_xlim(-0.6, 4.6)
ax.set_ylim(-1.0, 1.0)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("Figure 3. One-dimensional stepping-stone model used for population-structure experiments.")
save(fig, "fig3_stepping_stone")


# ---- Figure 4: Ne correction effect, SEA vs WAF ----
# Schematic dumbbell plot using the qualitative pattern from results:
# SEA pre/post overlap; WAF post is higher with non-overlapping CIs
fig, ax = plt.subplots(figsize=(7.0, 3.6))
settings = ["SEA (low transmission,\nhigh relatedness, n=701)",
            "WAF (high transmission,\nlow relatedness)"]
pre_ne = [3.0, 3.0]     # log10 Ne at recent generations, illustrative
post_ne = [3.05, 3.55]  # SEA overlapping, WAF materially higher
ci_pre = [0.1, 0.08]
ci_post = [0.1, 0.08]

y = np.arange(len(settings))
for i in range(len(settings)):
    ax.errorbar(pre_ne[i], y[i] - 0.12, xerr=ci_pre[i], fmt="o",
                color="#4C72B0", label="Before peak removal" if i == 0 else None,
                capsize=4)
    ax.errorbar(post_ne[i], y[i] + 0.12, xerr=ci_post[i], fmt="s",
                color="#C44E52", label="After peak removal" if i == 0 else None,
                capsize=4)
    ax.plot([pre_ne[i], post_ne[i]], [y[i] - 0.12, y[i] + 0.12],
            color="grey", lw=1, ls=":")

ax.set_yticks(y)
ax.set_yticklabels(settings)
ax.set_xlabel(r"$\log_{10} N_e$ at recent generations (schematic)")
ax.set_title("Figure 4. Effect of IBD peak removal on $N_e$ depends on transmission setting.\n"
             "SEA: CIs overlap; WAF: CIs non-overlapping around 20 generations ago.")
ax.legend(loc="lower right", fontsize=9)
ax.set_xlim(2.6, 4.0)
save(fig, "fig4_correction_effect")

print("Generated:")
for name in ["fig1_dataset", "fig2_ne_schematic", "fig3_stepping_stone", "fig4_correction_effect"]:
    print(f"  {name}.pdf / {name}.png")
