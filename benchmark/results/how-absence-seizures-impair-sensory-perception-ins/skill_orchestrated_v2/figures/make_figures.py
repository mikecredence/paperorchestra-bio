"""Generate figures for the ZTE-fMRI GAERS paper. All numerical values are copied
verbatim from inputs/experimental_log.md. No values are fabricated."""

import os

import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
    }
)


def save(fig, stem):
    fig.savefig(os.path.join(OUT, f"{stem}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, f"{stem}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# Figure 1: Motion occurrences across sequences
# ZTE (current study): 0.43 +/- 0.45 motions/min
# EPI (Stenroos et al. 2018): 1.0 +/- 0.20 motions/min
# MB-SWIFT (Paasonen et al. 2020): 0.48 +/- 0.23 motions/min
fig, ax = plt.subplots(figsize=(4.2, 3.2))
labels = ["ZTE\n(current)", "EPI\n(Stenroos 2018)", "MB-SWIFT\n(Paasonen 2020)"]
means = [0.43, 1.0, 0.48]
sds = [0.45, 0.20, 0.23]
colors = ["#2b6cb0", "#b83939", "#2f855a"]
xpos = np.arange(len(labels))
ax.bar(xpos, means, yerr=sds, color=colors, edgecolor="black", linewidth=0.7,
       capsize=4, alpha=0.85)
ax.set_xticks(xpos)
ax.set_xticklabels(labels)
ax.set_ylabel("Motions per minute")
ax.set_title("Head motion during awake rat fMRI")
ax.spines[["top", "right"]].set_visible(False)
save(fig, "fig_motion")

# Figure 2: Extreme beta-values, visual cortex
# baseline: 2.8 +/- 1.7; ictal: -6.0 +/- 2.0; end-seizure: 8.1 +/- 7.0
fig, ax = plt.subplots(figsize=(4.2, 3.2))
labels = ["Baseline\n(interictal)", "Ictal\n(seizure)", "Stim ends\nseizure"]
means = [2.8, -6.0, 8.1]
sds = [1.7, 2.0, 7.0]
colors = ["#2b6cb0", "#b83939", "#7c3aed"]
xpos = np.arange(len(labels))
ax.bar(xpos, means, yerr=sds, color=colors, edgecolor="black", linewidth=0.7,
       capsize=4, alpha=0.85)
ax.axhline(0, color="black", linewidth=0.6)
ax.set_xticks(xpos)
ax.set_xticklabels(labels)
ax.set_ylabel("Extreme beta-value (visual cortex ROI)")
ax.set_title("Visual cortex HRF during stimulation")
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, 0.93, "*** p < 0.001", transform=ax.transAxes, ha="center", fontsize=9)
save(fig, "fig_beta_visual")

# Figure 3: Extreme beta-values, barrel cortex
# baseline: 4.1 +/- 1.9; ictal: -9.0 +/- 1.9; end-seizure: 4.8 +/- 2.9
fig, ax = plt.subplots(figsize=(4.2, 3.2))
labels = ["Baseline\n(interictal)", "Ictal\n(seizure)", "Stim ends\nseizure"]
means = [4.1, -9.0, 4.8]
sds = [1.9, 1.9, 2.9]
colors = ["#2b6cb0", "#b83939", "#7c3aed"]
xpos = np.arange(len(labels))
ax.bar(xpos, means, yerr=sds, color=colors, edgecolor="black", linewidth=0.7,
       capsize=4, alpha=0.85)
ax.axhline(0, color="black", linewidth=0.6)
ax.set_xticks(xpos)
ax.set_xticklabels(labels)
ax.set_ylabel("Extreme beta-value (barrel cortex ROI)")
ax.set_title("Barrel cortex HRF during stimulation")
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, 0.93, "*** p < 0.001", transform=ax.transAxes, ha="center", fontsize=9)
save(fig, "fig_beta_barrel")

# Figure 4: Voxels activated, interictal vs ictal
# Interictal shows 136% more activated voxels than ictal:
# interictal / ictal = 2.36, so if ictal = 100, interictal = 236
# We present this as relative counts normalized to ictal = 100.
fig, ax = plt.subplots(figsize=(3.8, 3.2))
labels = ["Ictal", "Interictal"]
vals = [100, 236]  # relative (ictal = 100); interictal = 100 * (1 + 1.36)
colors = ["#b83939", "#2b6cb0"]
xpos = np.arange(len(labels))
ax.bar(xpos, vals, color=colors, edgecolor="black", linewidth=0.7, alpha=0.85)
ax.set_xticks(xpos)
ax.set_xticklabels(labels)
ax.set_ylabel("Activated voxels (ictal = 100)")
ax.set_title("Interictal vs ictal spatial extent")
ax.spines[["top", "right"]].set_visible(False)
ax.text(1.0, 240, "+136%", ha="center", fontsize=10, fontweight="bold")
save(fig, "fig_voxels")

# Figure 5: Schematic of stimulation relative to SWD classification
# Not a quantitative figure -- we draw a simple schematic of the four cases.
fig, ax = plt.subplots(figsize=(6.0, 3.0))
cases = [
    ("Interictal baseline", "stim only", 0.10, 0.80, "#2b6cb0"),
    ("Ictal (pure seizure)", "SWD ongoing throughout stim", 0.35, 0.80, "#b83939"),
    ("Stim ends seizure", "SWD ends shortly after stim", 0.60, 0.80, "#7c3aed"),
    ("Stim triggers SWD", "SWD follows stim onset", 0.85, 0.80, "#2f855a"),
]
for (title, sub, x, y, c) in cases:
    ax.add_patch(plt.Rectangle((x - 0.1, y - 0.5), 0.2, 0.3, fill=True,
                               facecolor=c, alpha=0.6, edgecolor="black"))
    ax.text(x, y + 0.02, title, ha="center", fontsize=9, fontweight="bold")
    ax.text(x, y - 0.62, sub, ha="center", fontsize=8)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_title("Classification of stimulation blocks relative to SWD", fontsize=11)
save(fig, "fig_schematic")

print("Figures written to", OUT)
