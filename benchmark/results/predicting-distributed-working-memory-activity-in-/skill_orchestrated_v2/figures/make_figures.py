"""Figure generation for mouse working memory model paper.
All numeric values are taken verbatim from inputs/experimental_log.md.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
    "figure.dpi": 120,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
OUTDIR = os.path.dirname(os.path.abspath(__file__))


def savefig(name):
    plt.savefig(os.path.join(OUTDIR, f"{name}.pdf"), bbox_inches="tight")
    plt.savefig(os.path.join(OUTDIR, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close()


# ------------------------------------------------------------------
# Figure 1: Correlations of delay firing with hierarchy and PV fraction
# Values verbatim from experimental_log.md.
# ------------------------------------------------------------------
scenarios = [
    "VISp (ref)",
    "SSp-bfd",
    "AUDp",
    "Ref +CIB+PV",
    "Remove PV",
    "Remove CIB",
    "Alt +CIB+PV",
    "Alt remove PV",
    "Alt remove CIB",
    "TC cortex",
]
r_hier = [0.91, 0.89, 0.89, np.nan, 0.85, np.nan, np.nan, 0.95, np.nan, 0.78]
r_pv   = [-0.43, -0.40, -0.40, -0.42, np.nan, -0.74, -0.70, np.nan, -0.84, -0.26]

x = np.arange(len(scenarios))
width = 0.38

fig, ax = plt.subplots(figsize=(7.2, 3.6))
bars_h = ax.bar(x - width/2, [v if not np.isnan(v) else 0 for v in r_hier],
                width, color=PALETTE[0], label="r vs hierarchy")
bars_p = ax.bar(x + width/2, [v if not np.isnan(v) else 0 for v in r_pv],
                width, color=PALETTE[1], label="r vs PV fraction")

for i, v in enumerate(r_hier):
    if np.isnan(v):
        ax.text(i - width/2, 0.02, "n/a", ha="center", va="bottom",
                fontsize=7, color="gray")
for i, v in enumerate(r_pv):
    if np.isnan(v):
        ax.text(i + width/2, -0.02, "n/a", ha="center", va="top",
                fontsize=7, color="gray")

ax.axhline(0, color="black", lw=0.6)
ax.set_ylabel("Pearson correlation r")
ax.set_xticks(x)
ax.set_xticklabels(scenarios, rotation=30, ha="right")
ax.set_ylim(-1.0, 1.0)
ax.legend(loc="lower right", frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("Delay-period firing: correlation with hierarchy vs PV fraction")
plt.tight_layout()
savefig("fig_corr_summary")


# ------------------------------------------------------------------
# Figure 2: Raw vs cell type-specific connectome measures.
# Left: correlation r with delay firing. Right: persistence prediction accuracy.
# ------------------------------------------------------------------
measures = ["Input\nstrength", "Eigenvec.\ncentrality", "Sign-only\ninput str.", "noPV\ninput str."]
# correlations with delay firing rate
r_raw = [0.25, 0.24, np.nan, np.nan]  # raw values available
r_cts = [0.89, 0.94, 0.90, 0.90]      # cell type-specific / modified
# prediction accuracy for whether an area shows persistent activity
acc_raw = [0.51, 0.46, np.nan, np.nan]
acc_cts = [0.95, 0.79, np.nan, np.nan]

fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.6))

x = np.arange(len(measures))
w = 0.38
ax = axes[0]
ax.bar(x - w/2, [v if not np.isnan(v) else 0 for v in r_raw],
       w, color="#aec7e8", label="raw")
ax.bar(x + w/2, [v if not np.isnan(v) else 0 for v in r_cts],
       w, color=PALETTE[0], label="cell type-specific")
for i, v in enumerate(r_raw):
    if np.isnan(v):
        ax.text(i - w/2, 0.02, "n/a", ha="center", fontsize=7, color="gray")
ax.set_xticks(x); ax.set_xticklabels(measures)
ax.set_ylabel("r vs delay firing rate")
ax.set_ylim(0, 1.0)
ax.legend(frameon=False, loc="upper left")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.set_title("(A) Correlation with delay firing")

ax = axes[1]
x2 = np.arange(2)
raw_acc = [0.51, 0.46]
cts_acc = [0.95, 0.79]
ax.bar(x2 - w/2, raw_acc, w, color="#aec7e8", label="raw")
ax.bar(x2 + w/2, cts_acc, w, color=PALETTE[0], label="cell type-specific")
ax.set_xticks(x2); ax.set_xticklabels(["Input\nstrength", "Eigenvec.\ncentrality"])
ax.set_ylabel("Persistence prediction accuracy")
ax.set_ylim(0, 1.0)
ax.legend(frameon=False, loc="upper left")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.set_title("(B) Persistence classification accuracy")

plt.tight_layout()
savefig("fig_measures")


# ------------------------------------------------------------------
# Figure 3: Inhibition-effect decrements from experimental_log.md.
# ------------------------------------------------------------------
labels = ["Single\nreadout", "Single\ncore", "All\ncore areas"]
decrements = [3, 15, 48]   # percent, exact values from log
colors = [PALETTE[2], PALETTE[1], PALETTE[3]]

fig, ax = plt.subplots(figsize=(4.6, 3.4))
bars = ax.bar(labels, decrements, color=colors, edgecolor="black", linewidth=0.6)
for b, v in zip(bars, decrements):
    ax.text(b.get_x() + b.get_width()/2, v + 1.2, f"{v}%",
            ha="center", va="bottom", fontsize=10)
ax.set_ylabel("Mean firing-rate decrement (%)")
ax.set_ylim(0, 60)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.set_title("Inactivation effect on delay-period activity")
plt.tight_layout()
savefig("fig_inhibition")


# ------------------------------------------------------------------
# Figure 4: Schematic of the model (data-structural, not invented numbers).
# Shows 43-area cortex, PV gradient, CIB rule.
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

# Two area boxes
def area_box(x, y, label, pv_color, w=2.2, h=2.2):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                         linewidth=1.2, edgecolor="black", facecolor="white")
    ax.add_patch(box)
    ax.text(x + w/2, y + h + 0.15, label, ha="center", va="bottom", fontsize=10, fontweight="bold")
    # excitatory pools
    e1 = FancyBboxPatch((x + 0.2, y + 1.1), 0.8, 0.8, boxstyle="round,pad=0.04",
                        facecolor="#f4a6a6", edgecolor="black", linewidth=0.8)
    e2 = FancyBboxPatch((x + 1.15, y + 1.1), 0.8, 0.8, boxstyle="round,pad=0.04",
                        facecolor="#f4a6a6", edgecolor="black", linewidth=0.8)
    ax.add_patch(e1); ax.add_patch(e2)
    ax.text(x + 0.6, y + 1.5, "E$_1$", ha="center", va="center", fontsize=9)
    ax.text(x + 1.55, y + 1.5, "E$_2$", ha="center", va="center", fontsize=9)
    # inhibitory pool, size scaled by PV gradient
    inh = FancyBboxPatch((x + 0.55, y + 0.2), 1.1, 0.7, boxstyle="round,pad=0.04",
                         facecolor=pv_color, edgecolor="black", linewidth=0.8)
    ax.add_patch(inh)
    ax.text(x + 1.1, y + 0.55, "PV I", ha="center", va="center", fontsize=9, color="white")

area_box(0.5, 1.8, "Sensory area (low hierarchy)\nhigh PV fraction",
         pv_color="#1b4965")
area_box(6.8, 1.8, "Association area (high hierarchy)\nlow PV fraction",
         pv_color="#5fa8d3")

# Feedforward arrow (excitatory-biased, thick)
arr_ff = FancyArrowPatch((2.9, 3.4), (6.7, 3.4), arrowstyle="-|>",
                         mutation_scale=18, lw=2.2, color="#c0392b")
ax.add_patch(arr_ff)
ax.text(4.8, 3.6, "Feedforward\n(excit.-biased)", ha="center", fontsize=9, color="#c0392b")

# Feedback arrow (inhibitory-biased, thinner dashed)
arr_fb = FancyArrowPatch((6.7, 2.5), (2.9, 2.5), arrowstyle="-|>",
                         mutation_scale=18, lw=1.6, color="#2c3e50",
                         linestyle="--")
ax.add_patch(arr_fb)
ax.text(4.8, 2.2, "Feedback\n(inhib.-biased, CIB)", ha="center", fontsize=9, color="#2c3e50")

# Caption-style note
ax.text(5.0, 0.4, "43 cortical areas (+ optional 40-area thalamus), "
        "mean-field reduction; PV fraction from qBrain; "
        "long-range weights from Allen connectome.",
        ha="center", va="center", fontsize=9, color="#555555")

ax.set_title("Model schematic: cell type-specific multi-regional cortex",
             fontsize=11)
plt.tight_layout()
savefig("fig_model_schematic")


print("Figures written to", OUTDIR)
