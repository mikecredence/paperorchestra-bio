"""Generate figures for the CHO manuscript.

All numerical values are copied verbatim from the experimental log; nothing is fabricated.
"""
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent

# ----------------------------------------------------------------------------
# Figure 1: CHO pipeline schematic
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 2.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

boxes = [
    (0.3, "Raw signal\n(ECoG/EEG/SEEG)"),
    (2.3, "Step 1\n1/f fit $\\rightarrow$\nbounding boxes"),
    (4.5, "Step 2\nreject boxes with\n< 2 cycles"),
    (6.9, "Step 3\nauto-correlation\nperiodicity test"),
    (9.0, "Fundamental\noscillations\n(when/where/what)"),
]
for i, (x, label) in enumerate(boxes):
    color = "#eef5ff" if i == 0 or i == len(boxes) - 1 else "#fff4e6"
    ax.add_patch(
        plt.Rectangle(
            (x - 0.9, 0.9), 1.8, 1.2, facecolor=color, edgecolor="#333", lw=1.2
        )
    )
    ax.text(x, 1.5, label, ha="center", va="center", fontsize=9)
    if i < len(boxes) - 1:
        nxt = boxes[i + 1][0]
        ax.annotate(
            "",
            xy=(nxt - 0.95, 1.5),
            xytext=(x + 0.95, 1.5),
            arrowprops=dict(arrowstyle="->", color="#444", lw=1.3),
        )

ax.text(
    5.0,
    2.65,
    "Cyclic Homogeneous Oscillation (CHO) detection pipeline",
    ha="center",
    fontsize=11,
    fontweight="bold",
)
plt.tight_layout()
fig.savefig(OUT / "fig_pipeline.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig_pipeline.png", bbox_inches="tight", dpi=200)
plt.close(fig)

# ----------------------------------------------------------------------------
# Figure 2: resting-state fundamental frequency + duration per region
# ----------------------------------------------------------------------------
regions = ["Auditory\n(BA 41/42)", "Motor\n(BA 4)", "Broca's area", "Hippocampus"]
freqs_hz = [11, 7, 17, 8]
durations_ms = [450, 450, 500, 450]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.2))
colors = ["#3b7ddd", "#e95d5d", "#2fa88d", "#8e5ac9"]
ax1.bar(regions, freqs_hz, color=colors, edgecolor="#222")
ax1.set_ylabel("Dominant fundamental frequency (Hz)")
ax1.set_title("Resting-state frequency")
ax1.set_ylim(0, 20)
for i, v in enumerate(freqs_hz):
    ax1.text(i, v + 0.4, f"{v} Hz", ha="center", fontsize=9)

ax2.bar(regions, durations_ms, color=colors, edgecolor="#222")
ax2.set_ylabel("Average oscillation duration (ms)")
ax2.set_title("Resting-state duration")
ax2.set_ylim(0, 600)
for i, v in enumerate(durations_ms):
    ax2.text(i, v + 10, f"{v} ms", ha="center", fontsize=9)

plt.tight_layout()
fig.savefig(OUT / "fig_resting_frequencies.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig_resting_frequencies.png", bbox_inches="tight", dpi=200)
plt.close(fig)

# ----------------------------------------------------------------------------
# Figure 3: entropy of oscillation detection across 64 EEG channels (lower = more focal)
# ----------------------------------------------------------------------------
methods = ["CHO", "FOOOF"]
alpha_entropy = [3.82, 4.15]
beta_entropy = [4.05, 4.15]
max_entropy = 4.16

x = np.arange(len(methods))
w = 0.35
fig, ax = plt.subplots(figsize=(5.5, 3.4))
b1 = ax.bar(x - w / 2, alpha_entropy, w, label="Alpha band", color="#3b7ddd", edgecolor="#222")
b2 = ax.bar(x + w / 2, beta_entropy, w, label="Beta band", color="#e95d5d", edgecolor="#222")
ax.axhline(max_entropy, ls="--", color="#555", label=f"Max entropy ({max_entropy})")
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.set_ylabel("Entropy across 64 EEG channels")
ax.set_title("Spatial focality of oscillation detection\n(lower entropy $=$ more focal)")
ax.set_ylim(3.0, 4.3)
for bars in (b1, b2):
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.01,
            f"{bar.get_height():.2f}",
            ha="center",
            fontsize=9,
        )
ax.legend(loc="lower right", fontsize=8)
plt.tight_layout()
fig.savefig(OUT / "fig_entropy.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig_entropy.png", bbox_inches="tight", dpi=200)
plt.close(fig)

# ----------------------------------------------------------------------------
# Figure 4: onset/offset of 7 Hz oscillations in auditory cortex
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 3.0))

ax.axvline(0, color="#444", lw=1.2)
ax.text(0, 1.08, "Auditory\nstimulus", ha="center", va="bottom", fontsize=9, color="#444")

# Button press (average reaction time 200 ms)
ax.axvline(200, color="#2fa88d", lw=1, ls=":")
ax.text(200, 1.08, "Button\npress\n(200 ms)", ha="center", va="bottom", fontsize=9, color="#2fa88d")

# Offset peak at 300 ms post-stimulus
ax.axvline(300, color="#e95d5d", lw=1.3)
ax.text(300, 1.08, "Offset peak\n(300 ms)", ha="center", va="bottom", fontsize=9, color="#e95d5d")

# Onset peak at 950 ms post-stimulus
ax.axvline(950, color="#3b7ddd", lw=1.3)
ax.text(950, 1.08, "Onset peak\n(950 ms)", ha="center", va="bottom", fontsize=9, color="#3b7ddd")

# Shading illustrating suspension interval
ax.axvspan(300, 950, facecolor="#f1f1f1", alpha=0.8)
ax.text(625, 0.45, "Oscillations suspended\n(~650 ms)", ha="center", fontsize=10, color="#444")

# Average de-sync / re-sync
ax.annotate(
    "avg. de-sync 250 ms",
    xy=(250, 0.18),
    xytext=(250, 0.18),
    ha="center",
    fontsize=9,
    color="#e95d5d",
)
ax.annotate(
    "avg. re-sync 900 ms",
    xy=(900, 0.18),
    xytext=(900, 0.18),
    ha="center",
    fontsize=9,
    color="#3b7ddd",
)

ax.set_xlim(-500, 1500)
ax.set_ylim(0, 1.3)
ax.set_xlabel("Time relative to auditory stimulus (ms)")
ax.set_yticks([])
ax.set_title("CHO-detected onset/offset of 7 Hz oscillations in auditory cortex (ECoG)")
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
plt.tight_layout()
fig.savefig(OUT / "fig_onset_offset.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig_onset_offset.png", bbox_inches="tight", dpi=200)
plt.close(fig)

print("Wrote 4 figures to", OUT)
