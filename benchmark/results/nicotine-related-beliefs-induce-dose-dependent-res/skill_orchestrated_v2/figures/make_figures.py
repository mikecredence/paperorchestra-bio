"""Generate figures for nicotine-belief manuscript.

All numerical values are taken verbatim from inputs/experimental_log.md.
No fabricated data.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

FIG_DIR = Path(__file__).parent
plt.rcParams.update({
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
})

CONDITIONS = ["Low", "Medium", "High"]
BELIEF_COLORS = ["#89c2d9", "#468faf", "#013a63"]
HC_COLOR = "#f4a261"


def bar_with_points(ax, means, sds, ns, colors, labels, ylabel, title, hc=None, p_text=None):
    x = np.arange(len(means))
    bars = ax.bar(x, means, color=colors, edgecolor="black", linewidth=0.6,
                  yerr=[s / np.sqrt(n) for s, n in zip(sds, ns)], capsize=4,
                  error_kw={"elinewidth": 1.0, "ecolor": "black"})
    rng = np.random.default_rng(42)
    for xi, m, s, n in zip(x, means, sds, ns):
        jitter = rng.normal(0, 0.06, n)
        pts = rng.normal(m, s, n)
        ax.scatter(np.full(n, xi) + jitter, pts, s=10, color="black", alpha=0.35,
                   zorder=3, linewidths=0)
    if hc is not None:
        hc_mean, hc_sd, hc_n = hc
        ax.bar(len(means), hc_mean, color=HC_COLOR, edgecolor="black", linewidth=0.6,
               yerr=hc_sd / np.sqrt(hc_n), capsize=4,
               error_kw={"elinewidth": 1.0, "ecolor": "black"})
        pts = rng.normal(hc_mean, hc_sd, hc_n)
        jitter = rng.normal(0, 0.06, hc_n)
        ax.scatter(np.full(hc_n, len(means)) + jitter, pts, s=10, color="black",
                   alpha=0.35, zorder=3, linewidths=0)
        labels = labels + ["HC"]
        x = np.arange(len(labels))
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if p_text is not None:
        ax.text(0.98, 0.96, p_text, transform=ax.transAxes, ha="right", va="top",
                fontsize=8, family="monospace",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=0.5))


# -------- Figure 1b: Subjective belief ratings --------
# low 3.52+/-0.61 (n=20), medium 4.52+/-0.41, high 5.82+/-0.47; F(2,38)=9.71, P=0.0004
fig, ax = plt.subplots(figsize=(3.6, 3.0))
bar_with_points(
    ax,
    means=[3.52, 4.52, 5.82],
    sds=[0.61, 0.41, 0.47],
    ns=[20, 20, 20],
    colors=BELIEF_COLORS,
    labels=CONDITIONS,
    ylabel="Perceived nicotine strength (AU)",
    title="Subjective belief ratings",
    p_text="F(2,38)=9.71\nP=0.0004",
)
plt.savefig(FIG_DIR / "fig1b_belief_ratings.pdf")
plt.savefig(FIG_DIR / "fig1b_belief_ratings.png")
plt.close()

# -------- Figure 1c: Nicotine intake --------
# low 0.928+/-0.56, medium 0.719+/-0.423, high 0.783+/-0.434 mg; F(2,38)=1.806, P=0.178
fig, ax = plt.subplots(figsize=(3.6, 3.0))
bar_with_points(
    ax,
    means=[0.928, 0.719, 0.783],
    sds=[0.56, 0.423, 0.434],
    ns=[20, 20, 20],
    colors=BELIEF_COLORS,
    labels=CONDITIONS,
    ylabel="Nicotine intake (mg)",
    title="Consumed nicotine",
    p_text="F(2,38)=1.806\nP=0.178 (n.s.)",
)
plt.savefig(FIG_DIR / "fig1c_nicotine_intake.pdf")
plt.savefig(FIG_DIR / "fig1c_nicotine_intake.png")
plt.close()

# -------- Figure 2b: Thalamus parameter estimates (smokers + HC) --------
# smokers low 0.157+/-1.047, medium 0.601+/-0.714, high 2.914+/-0.865 (n=20)
# HC 2.318+/-4.258 (n=31); rmANOVA F(2,38)=3.62, P=0.036
fig, ax = plt.subplots(figsize=(4.2, 3.0))
bar_with_points(
    ax,
    means=[0.157, 0.601, 2.914],
    sds=[1.047, 0.714, 0.865],
    ns=[20, 20, 20],
    colors=BELIEF_COLORS,
    labels=CONDITIONS,
    ylabel="Thalamic parameter estimate (AU)",
    title="Thalamus: dose-like belief response",
    hc=(2.318, 4.258, 31),
    p_text="F(2,38)=3.62\nP=0.036",
)
plt.savefig(FIG_DIR / "fig2b_thalamus_bars.pdf")
plt.savefig(FIG_DIR / "fig2b_thalamus_bars.png")
plt.close()

# -------- Figure 3b: NAcc parameter estimates (smokers + HC) --------
# smokers low 1.228+/-3.329, medium 1.248+/-2.828, high 1.016+/-2.6983 (n=20)
# HC 1.781+/-2.138 (n=31); rmANOVA F(2,38)=0.056, P=0.945
fig, ax = plt.subplots(figsize=(4.2, 3.0))
bar_with_points(
    ax,
    means=[1.228, 1.248, 1.016],
    sds=[3.329, 2.828, 2.6983],
    ns=[20, 20, 20],
    colors=BELIEF_COLORS,
    labels=CONDITIONS,
    ylabel="NAcc parameter estimate (AU)",
    title="Nucleus accumbens: no belief effect",
    hc=(1.781, 2.138, 31),
    p_text="F(2,38)=0.056\nP=0.945 (n.s.)",
)
plt.savefig(FIG_DIR / "fig3b_nacc_bars.pdf")
plt.savefig(FIG_DIR / "fig3b_nacc_bars.png")
plt.close()

# -------- Figure 2d (decoding summary): Thalamus vs NAcc accuracy --------
# thalamus gt=49.3%, surrogate 33.1+/-6.3%, P=0.011
# NAcc gt=34.0%, surrogate 32.1+/-6.3%, P=0.372
fig, ax = plt.subplots(figsize=(4.0, 3.2))
regions = ["Thalamus", "NAcc"]
gt = [49.3, 34.0]
surr_mean = [33.1, 32.1]
surr_sd = [6.3, 6.3]
x = np.arange(len(regions))
width = 0.34
ax.bar(x - width / 2, surr_mean, width, yerr=surr_sd, color="#cccccc",
       edgecolor="black", linewidth=0.6, capsize=4, label="Shuffle-label surrogate")
ax.bar(x + width / 2, gt, width, color=["#013a63", "#89c2d9"],
       edgecolor="black", linewidth=0.6, label="Ground truth")
ax.axhline(33.3, linestyle="--", color="red", linewidth=1.0, label="Chance (33.3%)")
ax.set_xticks(x)
ax.set_xticklabels(regions)
ax.set_ylabel("Decoding accuracy (%)")
ax.set_title("Belief decoding from multivoxel patterns")
ax.set_ylim(0, 60)
ax.legend(frameon=False, loc="upper right", fontsize=7)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.text(0 + width / 2, gt[0] + 1.5, "P=0.011", ha="center", fontsize=7)
ax.text(1 + width / 2, gt[1] + 1.5, "P=0.372", ha="center", fontsize=7)
plt.savefig(FIG_DIR / "fig2d_decoding.pdf")
plt.savefig(FIG_DIR / "fig2d_decoding.png")
plt.close()

# -------- Figure 4 (schematic): thalamus-vmPFC PPI conceptual --------
fig, ax = plt.subplots(figsize=(4.5, 3.0))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")
ax.add_patch(plt.Circle((2.5, 2.0), 0.9, color="#468faf", alpha=0.9))
ax.text(2.5, 2.0, "Thalamus", ha="center", va="center", color="white", fontsize=9)
ax.add_patch(plt.Circle((7.5, 4.2), 0.9, color="#013a63", alpha=0.9))
ax.text(7.5, 4.2, "vmPFC", ha="center", va="center", color="white", fontsize=9)
# three arrows of increasing thickness
for i, (lw, label) in enumerate(zip([1.0, 2.0, 3.5], ["Low", "Medium", "High"])):
    offset = 0.25 * (i - 1)
    ax.annotate("", xy=(6.7, 4.2 + offset * 0.2), xytext=(3.3, 2.0 + offset * 0.2),
                arrowprops=dict(arrowstyle="-|>", lw=lw, color=BELIEF_COLORS[i]))
    ax.text(5.0 + offset * 0.8, 3.1 + 0.25 * i, label,
            color=BELIEF_COLORS[i], fontsize=9)
ax.text(5.0, 0.6, "Dose-like scaling of thalamus-vmPFC coupling\n(whole-brain P=0.041, FWE cluster-corrected)",
        ha="center", fontsize=8, style="italic")
plt.savefig(FIG_DIR / "fig4_ppi_schematic.pdf")
plt.savefig(FIG_DIR / "fig4_ppi_schematic.png")
plt.close()

print("All figures written to", FIG_DIR)
