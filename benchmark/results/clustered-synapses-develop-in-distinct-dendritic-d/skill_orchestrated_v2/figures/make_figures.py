"""Generate figures for the dendritic-domain paper. All numeric values come verbatim
from the experimental extraction in inputs/experimental_log.md."""
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
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
FIGDIR = os.path.dirname(os.path.abspath(__file__))


def save(fig, stem):
    fig.savefig(os.path.join(FIGDIR, stem + ".pdf"))
    fig.savefig(os.path.join(FIGDIR, stem + ".png"), dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Fig 1: Spine vs shaft synaptic transmission frequency at two ages
# Source (experimental log):
#   P8-10: spine 0.55 +/- 0.09 min^-1, shaft 0.16 +/- 0.03 min^-1
#   P12-13: spine 0.67 +/- 0.07 min^-1, shaft 0.23 +/- 0.03 min^-1
# ---------------------------------------------------------------------------
ages = ["P8-10", "P12-13"]
spine_mean = [0.55, 0.67]
spine_sem = [0.09, 0.07]
shaft_mean = [0.16, 0.23]
shaft_sem = [0.03, 0.03]

x = np.arange(len(ages))
width = 0.35
fig, ax = plt.subplots(figsize=(4.5, 3.2))
ax.bar(x - width / 2, spine_mean, width, yerr=spine_sem, capsize=3,
       color=PALETTE[1], edgecolor="black", linewidth=0.5, label="Spine")
ax.bar(x + width / 2, shaft_mean, width, yerr=shaft_sem, capsize=3,
       color=PALETTE[0], edgecolor="black", linewidth=0.5, label="Shaft")
ax.set_xticks(x)
ax.set_xticklabels(ages)
ax.set_ylabel(r"Transmission frequency (min$^{-1}$)")
ax.set_xlabel("Age")
ax.set_ylim(0, 0.85)
ax.legend(frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
save(fig, "fig_transmission_rates")


# ---------------------------------------------------------------------------
# Fig 2: Domain features across development
# Source:
#   Extent: P8-10 18.7 +/- 6.1 um; P12-13 22.5 +/- 6.4 um (STD)
#   Synapses/domain: P8-10 3.2 +/- 1.7; P12-13 6.0 +/- 3.2 (STD)
#   Density (per 100 um): P8-10 1.4 +/- 0.7; P12-13 2.6 +/- 1.0 (STD)
#   Coverage (%): P8-10 27.2 +/- 16.2; P12-13 61.3 +/- 29.4 (STD)
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(11, 3.0))
features = [
    ("Extent (\u00b5m)", [18.7, 22.5], [6.1, 6.4]),
    ("Synapses / domain", [3.2, 6.0], [1.7, 3.2]),
    ("Density (/100 \u00b5m)", [1.4, 2.6], [0.7, 1.0]),
    ("Dendrite covered (%)", [27.2, 61.3], [16.2, 29.4]),
]
for ax, (label, means, stds) in zip(axes, features):
    ax.bar(ages, means, yerr=stds, capsize=4,
           color=[PALETTE[2], PALETTE[3]],
           edgecolor="black", linewidth=0.5)
    ax.set_ylabel(label)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
plt.tight_layout()
save(fig, "fig_domain_features")


# ---------------------------------------------------------------------------
# Fig 3: Local co-activity inside vs outside domains at each age
# Source:
#   Young (P8-10): in 0.08 +/- 0.02; out 0.02 +/- 0.01 (SEM)
#   Older (P12-13): in 0.06 +/- 0.01; out 0.04 +/- 0.01 (SEM)
# ---------------------------------------------------------------------------
in_mean = [0.08, 0.06]
in_sem = [0.02, 0.01]
out_mean = [0.02, 0.04]
out_sem = [0.01, 0.01]

x = np.arange(len(ages))
fig, ax = plt.subplots(figsize=(4.5, 3.2))
ax.bar(x - width / 2, in_mean, width, yerr=in_sem, capsize=3,
       color=PALETTE[3], edgecolor="black", linewidth=0.5, label="Inside domain")
ax.bar(x + width / 2, out_mean, width, yerr=out_sem, capsize=3,
       color="#bbbbbb", edgecolor="black", linewidth=0.5, label="Outside domain")
ax.set_xticks(x)
ax.set_xticklabels(ages)
ax.set_ylabel("Local co-activity")
ax.set_xlabel("Age")
ax.set_ylim(0, 0.12)
ax.legend(frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
save(fig, "fig_coactivity")


# ---------------------------------------------------------------------------
# Fig 4: Schematic / model for domain formation across P8 -> P14
# Source: Fig 7D model described qualitatively in extraction.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 2.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

stages = ["Early P8", "Mid P10", "Late P13 (pre-eye-opening)"]
xs = [1.2, 4.7, 8.2]
for cx, label in zip(xs, stages):
    # dendritic stretch
    ax.plot([cx - 0.9, cx + 0.9], [1.2, 1.2], color="#444444", linewidth=2.5)
    ax.text(cx, 2.3, label, ha="center", fontsize=10)

rng = np.random.default_rng(0)

# Early: sparse random synapses
for cx in [xs[0]]:
    pts = rng.uniform(-0.85, 0.85, 4)
    for p in pts:
        ax.scatter(cx + p, 1.2, s=20, color=PALETTE[0], edgecolor="black",
                   linewidth=0.3, zorder=3)

# Mid: a few small domains
for cx in [xs[1]]:
    domain_centers = [-0.5, 0.4]
    colors = [PALETTE[1], PALETTE[2]]
    for dc, col in zip(domain_centers, colors):
        for dp in [-0.12, 0.0, 0.12]:
            ax.scatter(cx + dc + dp, 1.2, s=24, color=col,
                       edgecolor="black", linewidth=0.3, zorder=3)
    # an outsider that will undergo depression
    ax.scatter(cx + 0.8, 1.2, s=16, color="#bbbbbb",
               edgecolor="black", linewidth=0.3, zorder=3)

# Late: multiple dense domains covering most of dendrite
for cx in [xs[2]]:
    dom_params = [(-0.7, PALETTE[1]), (-0.2, PALETTE[2]),
                  (0.35, PALETTE[3]), (0.8, PALETTE[4])]
    for dc, col in dom_params:
        for dp in [-0.12, -0.04, 0.04, 0.12]:
            ax.scatter(cx + dc + dp, 1.2, s=26, color=col,
                       edgecolor="black", linewidth=0.3, zorder=3)

# arrows between stages
for a, b in [(xs[0] + 1.0, xs[1] - 1.0), (xs[1] + 1.0, xs[2] - 1.0)]:
    ax.annotate("", xy=(b, 1.2), xytext=(a, 1.2),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#333333"))

ax.text(5.0, 0.35, "Co-active synapses potentiate within domains;"
        " desynchronized inputs depress",
        ha="center", fontsize=9, style="italic", color="#333333")

plt.tight_layout()
save(fig, "fig_domain_schematic")


# ---------------------------------------------------------------------------
# Fig 5: Schematic of experimental setup (whole-cell + two-photon imaging)
# Source: methods section in extraction.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

# neuron
soma = mpatches.Circle((3.2, 2.5), 0.55, facecolor="#f0c584",
                       edgecolor="black", linewidth=1.0, zorder=2)
ax.add_patch(soma)
# apical dendrite
ax.plot([3.2, 3.2], [3.05, 4.4], color="#a06d2b", linewidth=3, zorder=1)
ax.plot([3.2, 2.3], [4.0, 4.6], color="#a06d2b", linewidth=2, zorder=1)
ax.plot([3.2, 4.1], [4.0, 4.6], color="#a06d2b", linewidth=2, zorder=1)
# basal dendrites
for x_end, y_end in [(2.2, 1.8), (4.2, 1.8), (2.6, 1.3), (3.8, 1.3)]:
    ax.plot([3.2, x_end], [2.0, y_end], color="#a06d2b", linewidth=2)

# patch pipette
ax.plot([3.2, 0.4], [2.5, 0.6], color="#555555", linewidth=2)
ax.text(0.3, 0.3, "Patch pipette\n(+QX-314)", fontsize=8, ha="left")

# two-photon beam
ax.annotate("", xy=(3.2, 4.3), xytext=(6.5, 4.3),
            arrowprops=dict(arrowstyle="->", lw=1.5, color=PALETTE[0]))
ax.text(6.6, 4.3, "2-photon\nGCaMP6s +\nDsRed", fontsize=9, va="center")

# voltage trace
ax.plot([6.5, 6.7, 6.8, 6.85, 7.05, 7.2, 7.4, 7.6],
        [2.5, 2.5, 2.1, 2.3, 2.5, 2.4, 2.5, 2.5],
        color=PALETTE[3], linewidth=1.2)
ax.text(6.5, 3.0, "Somatic barrage\n(voltage clamp, -30 mV)", fontsize=8)

ax.text(5.0, 0.1, "Mouse V1 L2/3 pyramidal neuron, P8-P13",
        ha="center", fontsize=9, style="italic")
plt.tight_layout()
save(fig, "fig_setup_schematic")

print("done.")
