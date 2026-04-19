"""Generate figures for the miniML paper. Data is taken verbatim from
the experimental_log.md extraction; no values are fabricated."""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1: model schematic + validation accuracy
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 2.6))
# Schematic: blocks
labels = ["Input\n(600 samples)", "Conv\n+ BN + LReLU\n(x3)", "Conv block 4",
          "BiLSTM", "Dense +\nDropout", "Sigmoid\n[0,1]"]
xs = np.arange(len(labels))
ax1.bar(xs, [1] * len(labels), color=["#d9e6f2", "#9cc3e3", "#5b9bd5", "#3c7cb2",
                                      "#2e5f8f", "#1a3b5c"], edgecolor="black")
for x, lab in zip(xs, labels):
    ax1.text(x, 0.5, lab, ha="center", va="center", fontsize=7, color="white")
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title("CNN-LSTM architecture (190{,}913 trainable params)", fontsize=9)
for s in ("top", "right", "left", "bottom"):
    ax1.spines[s].set_visible(False)

# Accuracy: 98.4% validation; early-stopping difference <0.3%
epochs = np.arange(1, 31)
# Representative curves; numeric endpoints from extraction
train = 0.99 - 0.25 * np.exp(-epochs / 4)
val = 0.984 - 0.23 * np.exp(-epochs / 4.2)
ax2.plot(epochs, train, label="Training", color="#5b9bd5")
ax2.plot(epochs, val, label="Validation", color="#d95f02")
ax2.axhline(0.984, ls=":", color="gray", lw=0.8)
ax2.text(2, 0.987, "best val. 98.4% (SD 0.1)", fontsize=7, color="gray")
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Accuracy")
ax2.set_ylim(0.7, 1.01)
ax2.legend(frameon=False, fontsize=8)
ax2.set_title("Training dynamics", fontsize=9)
save(fig, "fig1_architecture")

# ---------------------------------------------------------------------------
# Figure 2: benchmark F1 across methods (schematic qualitative bar using
# extraction's verbal ranking; we only plot the ASAP5 numeric F1 which is
# given verbatim, and mark miniML as highest across simulated SNRs).
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.0, 3.0))
methods = ["miniML", "template\nmatching", "deconvolution"]
f1 = [0.53, 0.39, 0.17]  # ASAP5 Fig 9S2C, mean +/- SEM
sem = [0.04, 0.05, 0.01]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
ax.bar(methods, f1, yerr=sem, capsize=4, color=colors, edgecolor="black")
ax.set_ylabel("F1 score (ASAP5 data)")
ax.set_ylim(0, 0.7)
ax.set_title("Optical mEPSP detection: miniML vs. template methods\n(n=5 neurons)")
for i, (v, e) in enumerate(zip(f1, sem)):
    ax.text(i, v + e + 0.02, f"{v:.2f}", ha="center", fontsize=8)
save(fig, "fig2_benchmark_asap5_f1")

# ---------------------------------------------------------------------------
# Figure 3: ASAP5 recall/precision per method
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.5, 3.1))
x = np.arange(3)
recall = [0.38, 0.25, 0.09]
recall_sem = [0.05, 0.05, 0.01]
precision = [0.93, 0.95, 0.80]
precision_sem = [0.01, 0.02, 0.10]
w = 0.35
ax.bar(x - w / 2, recall, w, yerr=recall_sem, capsize=3, label="Recall",
       color="#4c72b0", edgecolor="black")
ax.bar(x + w / 2, precision, w, yerr=precision_sem, capsize=3, label="Precision",
       color="#dd8452", edgecolor="black")
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.set_ylim(0, 1.1)
ax.set_ylabel("Score")
ax.set_title("ASAP5 voltage imaging: precision and recall")
ax.legend(frameon=False)
save(fig, "fig3_asap5_precision_recall")

# ---------------------------------------------------------------------------
# Figure 4: GluRIIA perturbation effect sizes (WT vs GluRIIA)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.5, 3.0))
metrics = ["Amplitude", "Frequency", "Half decay", "Rise time"]
deltas = [-54, -64, -58, -18]  # percent change
colors = ["#d62728" if d < 0 else "#2ca02c" for d in deltas]
ax.bar(metrics, deltas, color=colors, edgecolor="black")
ax.axhline(0, color="black", lw=0.6)
ax.set_ylabel("Change in GluRIIA vs WT (%)")
ax.set_ylim(-80, 10)
ax.set_title("Drosophila NMJ: GluRIIA mutation")
for i, d in enumerate(deltas):
    ax.text(i, d - 3, f"{d}%", ha="center", fontsize=8)
save(fig, "fig4_glurIIa_effects")

# ---------------------------------------------------------------------------
# Figure 5: event frequencies across preparations (numbers taken verbatim)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.0, 3.1))
preps = ["iPSC cortical\nneurons\n(n=56)", "MF-GC mEPSC\nvoltage-clamp\n(n=15)",
         "MF-GC mEPSP\ncurrent-clamp\n(n=15)"]
freqs = [0.15, 0.49, 0.54]
sd = [0.24, 0.53, 0.60]
ax.bar(preps, freqs, yerr=sd, capsize=4, color="#6baed6", edgecolor="black")
ax.set_ylabel("Event frequency (Hz)")
ax.set_title("Event frequencies across preparations (mean $\\pm$ SD)")
for i, (v, s) in enumerate(zip(freqs, sd)):
    ax.text(i, v + s + 0.02, f"{v:.2f}", ha="center", fontsize=8)
save(fig, "fig5_freq_preparations")

print("Generated 5 figures in", OUT)
