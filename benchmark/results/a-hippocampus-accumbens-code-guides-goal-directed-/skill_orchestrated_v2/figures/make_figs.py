"""Generate figures from the hippocampus-accumbens experimental log.
All plotted numbers come VERBATIM from inputs/experimental_log.md /
inputs/idea_summary.md. No fabricated values.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})

# --- Figure 1: Place cell proportions and properties -------------------------
fig, axes = plt.subplots(1, 2, figsize=(6.2, 2.6))

# Panel A: Proportion of place cells (from idea_summary: 169/444=38%, 1581/4928=32%)
ax = axes[0]
labels = ["dHPC$-$", "dHPC$\\rightarrow$NAc"]
props = [1581 / 4928 * 100, 169 / 444 * 100]  # 32.08, 38.06
bars = ax.bar(labels, props, color=["#3fa34d", "#c0392b"], width=0.6)
ax.set_ylabel("Place cells (% of neurons)")
ax.set_title("Place cell proportion ($\\chi^2$ p = 0.012)")
for b, v, n, d in zip(bars, props, [1581, 169], [4928, 444]):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.8, f"{n}/{d}\n({v:.0f}%)",
            ha="center", va="bottom", fontsize=8)
ax.set_ylim(0, 45)

# Panel B: Conjunctive coding proportion (44% vs 19%)
ax = axes[1]
props2 = [19, 44]
bars = ax.bar(labels, props2, color=["#3fa34d", "#c0392b"], width=0.6)
ax.set_ylabel("Conjunctive-coding neurons (%)")
ax.set_title("Conjunctive coding ($\\chi^2$, p < 0.001)")
for b, v in zip(bars, props2):
    ax.text(b.get_x() + b.get_width() / 2, v + 1, f"{v}%", ha="center", fontsize=8)
ax.set_ylim(0, 55)

fig.tight_layout()
fig.savefig(OUT / "fig1_place_conjunctive.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig1_place_conjunctive.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# --- Figure 2: Speed modulation proportions ----------------------------------
fig, ax = plt.subplots(figsize=(4.6, 2.8))
categories = ["Speed-excited", "Speed-inhibited"]
dhpc_minus = [13, 15]
dhpc_nac = [16, 21]
x = np.arange(len(categories))
w = 0.35
ax.bar(x - w / 2, dhpc_minus, w, label="dHPC$-$", color="#3fa34d")
ax.bar(x + w / 2, dhpc_nac, w, label="dHPC$\\rightarrow$NAc", color="#c0392b")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel("% of neurons")
ax.set_title("Speed modulation (inhibited: p = 0.00022)")
for xi, (a, b) in enumerate(zip(dhpc_minus, dhpc_nac)):
    ax.text(xi - w / 2, a + 0.5, f"{a}%", ha="center", fontsize=8)
    ax.text(xi + w / 2, b + 0.5, f"{b}%", ha="center", fontsize=8)
ax.legend(frameon=False, loc="upper left")
ax.set_ylim(0, 28)
fig.tight_layout()
fig.savefig(OUT / "fig2_speed.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig2_speed.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# --- Figure 3: Licking modulation proportions --------------------------------
fig, ax = plt.subplots(figsize=(4.6, 2.8))
categories = ["Lick-excited", "Lick-inhibited"]
dhpc_minus = [3.8, 19.7]
dhpc_nac = [7.4, 17.1]
x = np.arange(len(categories))
w = 0.35
ax.bar(x - w / 2, dhpc_minus, w, label="dHPC$-$", color="#3fa34d")
ax.bar(x + w / 2, dhpc_nac, w, label="dHPC$\\rightarrow$NAc", color="#c0392b")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel("% of neurons")
ax.set_title("Appetitive licking modulation (excited: p < 0.001)")
for xi, (a, b) in enumerate(zip(dhpc_minus, dhpc_nac)):
    ax.text(xi - w / 2, a + 0.3, f"{a}%", ha="center", fontsize=8)
    ax.text(xi + w / 2, b + 0.3, f"{b}%", ha="center", fontsize=8)
ax.legend(frameon=False, loc="upper left")
ax.set_ylim(0, 25)
fig.tight_layout()
fig.savefig(OUT / "fig3_lick.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig3_lick.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# --- Figure 4: Optogenetic stimulation effects -------------------------------
# Values from exp log: ChR2 mouth t(3)=7.485 p=0.00494, EYFP t(2)=1.353 p=0.309
# Velocity: ChR2 t(3)=-3.551 p=0.0381, EYFP t(2)=-1.263 p=0.334
fig, axes = plt.subplots(1, 2, figsize=(6.2, 2.6))

ax = axes[0]
groups = ["EYFP\n(n=3)", "ChR2\n(n=4)"]
# Show schematic effect size based on qualitative description (increase in ChR2 only)
# Plot the reported t-statistics as effect magnitudes
mouth_t = [1.353, 7.485]
bars = ax.bar(groups, mouth_t, color=["#7f8c8d", "#2980b9"])
ax.set_ylabel("|t| for mouth motion change")
ax.set_title("Mouth motion (ChR2: p = 0.00494)")
for b, v, p in zip(bars, mouth_t, [0.309, 0.00494]):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.2, f"t={v}\np={p}",
            ha="center", fontsize=7.5)
ax.set_ylim(0, 10)

ax = axes[1]
vel_t = [-1.263, -3.551]
bars = ax.bar(groups, vel_t, color=["#7f8c8d", "#2980b9"])
ax.set_ylabel("t for velocity change")
ax.set_title("Velocity (ChR2: p = 0.0381)")
for b, v, p in zip(bars, vel_t, [0.334, 0.0381]):
    ax.text(b.get_x() + b.get_width() / 2, v - 0.25, f"t={v}\np={p}",
            ha="center", va="top", fontsize=7.5)
ax.axhline(0, color="k", linewidth=0.6)
ax.set_ylim(-5, 1)

fig.tight_layout()
fig.savefig(OUT / "fig4_opto.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig4_opto.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# --- Figure 5: Schematic of task and circuit --------------------------------
fig, ax = plt.subplots(figsize=(6.2, 2.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")

# Treadmill belt (360 cm, 30 cm reward zone shown at scale)
belt_x0, belt_x1, belt_y = 0.8, 9.2, 1.1
ax.add_patch(plt.Rectangle((belt_x0, belt_y), belt_x1 - belt_x0, 0.35,
                            facecolor="#eee", edgecolor="k"))
# reward zone (30/360 of belt ~ 8.3%)
rew_w = (belt_x1 - belt_x0) * (30 / 360)
ant_w = (belt_x1 - belt_x0) * (30 / 360)
rew_x = belt_x0 + (belt_x1 - belt_x0) * 0.6
ax.add_patch(plt.Rectangle((rew_x, belt_y), rew_w, 0.35,
                            facecolor="#f1c40f", edgecolor="k"))
ax.add_patch(plt.Rectangle((rew_x - ant_w, belt_y), ant_w, 0.35,
                            facecolor="#fef9e7", edgecolor="k"))
ax.text(rew_x + rew_w / 2, belt_y + 0.55, "Reward", ha="center", fontsize=8)
ax.text(rew_x - ant_w / 2, belt_y + 0.55, "Anticip.", ha="center", fontsize=8)
ax.text(belt_x0, belt_y - 0.18, "0 cm", fontsize=7)
ax.text(belt_x1, belt_y - 0.18, "360 cm", fontsize=7, ha="right")

# Circuit diagram
ax.add_patch(plt.Circle((2.2, 2.4), 0.28, facecolor="#fadbd8", edgecolor="k"))
ax.text(2.2, 2.4, "dHPC", ha="center", va="center", fontsize=8)
ax.add_patch(plt.Circle((6.5, 2.4), 0.28, facecolor="#d6eaf8", edgecolor="k"))
ax.text(6.5, 2.4, "NAc", ha="center", va="center", fontsize=8)
ax.annotate("", xy=(6.22, 2.4), xytext=(2.48, 2.4),
            arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.6))
ax.text(4.35, 2.5, "dHPC$\\rightarrow$NAc (AAVrg-Cre + DIO-mCherry)",
        ha="center", fontsize=8)
ax.text(5, 0.55, "360-cm self-propelled treadmill, 30-cm hidden reward zone",
        ha="center", fontsize=8)

fig.savefig(OUT / "fig5_schematic.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig5_schematic.png", dpi=180, bbox_inches="tight")
plt.close(fig)

print("Generated 5 figures.")
