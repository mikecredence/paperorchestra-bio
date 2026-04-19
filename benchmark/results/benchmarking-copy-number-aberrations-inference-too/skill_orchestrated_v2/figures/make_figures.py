"""Generate figures for the CNA benchmark paper.

All numerical data traces back verbatim to the experimental log.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
OUTDIR = os.path.dirname(os.path.abspath(__file__))


def save(fig, name):
    fig.savefig(os.path.join(OUTDIR, f"{name}.pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUTDIR, f"{name}.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------- Figure 1: Benchmarking workflow schematic ----------
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

# Input boxes (left)
ax.add_patch(FancyBboxPatch((0.2, 4.0), 2.2, 1.2, boxstyle="round,pad=0.08",
                            facecolor="#e8f0fb", edgecolor="#1f77b4"))
ax.text(1.3, 4.6, "scRNA-seq\n(expression)", ha="center", va="center", fontsize=9)

ax.add_patch(FancyBboxPatch((0.2, 2.0), 2.2, 1.2, boxstyle="round,pad=0.08",
                            facecolor="#fcebd8", edgecolor="#ff7f0e"))
ax.text(1.3, 2.6, "scRNA-seq\n+ BAM / BAF", ha="center", va="center", fontsize=9)

ax.add_patch(FancyBboxPatch((0.2, 0.2), 2.2, 1.2, boxstyle="round,pad=0.08",
                            facecolor="#dff3d8", edgecolor="#2ca02c"))
ax.text(1.3, 0.8, "paired scDNA-seq\n(ground truth)", ha="center", va="center", fontsize=9)

# Tool boxes (middle)
tools_exp = ["inferCNV", "CopyKAT", "SCEVAN"]
for i, t in enumerate(tools_exp):
    y = 4.0 + 0.5 - i * 0.5
    ax.add_patch(FancyBboxPatch((3.2, y), 1.6, 0.4, boxstyle="round,pad=0.05",
                                facecolor="white", edgecolor="#1f77b4"))
    ax.text(4.0, y + 0.2, t, ha="center", va="center", fontsize=9)

tools_ae = ["Numbat", "CaSpER"]
for i, t in enumerate(tools_ae):
    y = 2.5 - i * 0.5
    ax.add_patch(FancyBboxPatch((3.2, y), 1.6, 0.4, boxstyle="round,pad=0.05",
                                facecolor="white", edgecolor="#ff7f0e"))
    ax.text(4.0, y + 0.2, t, ha="center", va="center", fontsize=9)

# Arrows from inputs to tools
ax.add_patch(FancyArrowPatch((2.4, 4.6), (3.2, 4.2), arrowstyle="->", mutation_scale=12, color="#1f77b4"))
ax.add_patch(FancyArrowPatch((2.4, 2.6), (3.2, 2.2), arrowstyle="->", mutation_scale=12, color="#ff7f0e"))

# Evaluation tasks (right)
tasks = [
    "Tumour/normal classification",
    "CNA profile accuracy",
    "Subclonal structure",
    "Aneuploidy in TME cells",
]
for i, t in enumerate(tasks):
    y = 4.6 - i * 1.1
    ax.add_patch(FancyBboxPatch((5.6, y), 3.8, 0.7, boxstyle="round,pad=0.05",
                                facecolor="#f5f5f5", edgecolor="gray"))
    ax.text(7.5, y + 0.35, t, ha="center", va="center", fontsize=9)

# Arrow from tools to tasks
ax.add_patch(FancyArrowPatch((4.8, 3.2), (5.6, 3.2), arrowstyle="->", mutation_scale=14, color="gray"))
ax.add_patch(FancyArrowPatch((2.4, 0.8), (5.6, 3.0), arrowstyle="->", mutation_scale=12, color="#2ca02c", linestyle=":"))
ax.text(3.9, 1.4, "ground truth", color="#2ca02c", fontsize=8, style="italic")

ax.text(5.0, 5.5, "Benchmarking Framework", ha="center", fontsize=12, fontweight="bold")
save(fig, "fig_workflow")


# ---------- Figure 2: TME inclusion rescues inferCNV F1 ----------
# Data source: statistical_sentences line 3 — CRC02 (88%): 0 -> 1; CRC22 (91%): 0.5 -> 0.9; CRC03 (67%): 0.55 -> 0.99
samples = ["CRC02\n(88% tumour)", "CRC22\n(91% tumour)", "CRC03\n(67% tumour)"]
f1_epi = [0.0, 0.5, 0.55]
f1_tme = [1.0, 0.9, 0.99]

x = np.arange(len(samples))
width = 0.35
fig, ax = plt.subplots(figsize=(5.2, 3.4))
b1 = ax.bar(x - width / 2, f1_epi, width, label="Epithelial only", color=PALETTE[0])
b2 = ax.bar(x + width / 2, f1_tme, width, label="Epithelial + TME", color=PALETTE[1])
for bars in (b1, b2):
    for rect in bars:
        h = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, h + 0.02, f"{h:.2f}",
                ha="center", va="bottom", fontsize=8)
ax.set_ylabel("F1 score (tumour vs normal)")
ax.set_title("inferCNV: TME inclusion rescues tumour-dominated samples")
ax.set_xticks(x); ax.set_xticklabels(samples)
ax.set_ylim(0, 1.15)
ax.legend(loc="upper left", frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
save(fig, "fig_tme_rescue")


# ---------- Figure 3: LOH breakdown for Numbat ----------
# Data source: statistical_sentences line 7 — 14/17 (~82%) of Numbat LOH were CNV events
labels = ["Non-neutral CNV\n(14 of 17, ~82%)", "True cnLOH\n(3 of 17, ~18%)"]
sizes = [14, 3]
colors = [PALETTE[3], PALETTE[2]]

fig, ax = plt.subplots(figsize=(4.5, 3.4))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct="%1.0f%%",
    startangle=90, wedgeprops={"edgecolor": "white", "linewidth": 1.2},
    pctdistance=0.72,
)
for at in autotexts:
    at.set_color("white"); at.set_fontweight("bold")
ax.set_title("Numbat LOH calls audited against paired scDNA-seq")
plt.tight_layout()
save(fig, "fig_loh_breakdown")


# ---------- Figure 4: One-pass vs two-pass inferCNV schematic ----------
fig, ax = plt.subplots(figsize=(7.5, 3.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")

# One-pass (top)
ax.text(0.4, 3.4, "One-pass", fontsize=10, fontweight="bold")
ax.add_patch(FancyBboxPatch((1.8, 2.9), 1.8, 0.9, boxstyle="round,pad=0.06",
                            facecolor="#e8f0fb", edgecolor="#1f77b4"))
ax.text(2.7, 3.35, "All cells\n(no reference)", ha="center", va="center", fontsize=9)
ax.add_patch(FancyArrowPatch((3.7, 3.35), (5.0, 3.35), arrowstyle="->", mutation_scale=12))
ax.add_patch(FancyBboxPatch((5.1, 2.9), 1.8, 0.9, boxstyle="round,pad=0.06",
                            facecolor="white", edgecolor="gray"))
ax.text(6.0, 3.35, "inferCNV", ha="center", va="center", fontsize=9)
ax.add_patch(FancyArrowPatch((7.0, 3.35), (8.3, 3.35), arrowstyle="->", mutation_scale=12))
ax.add_patch(FancyBboxPatch((8.4, 2.9), 1.5, 0.9, boxstyle="round,pad=0.06",
                            facecolor="#fcebd8", edgecolor="#ff7f0e"))
ax.text(9.15, 3.35, "CNAs\n(may mis-center)", ha="center", va="center", fontsize=8)

# Two-pass (bottom)
ax.text(0.4, 1.4, "Two-pass", fontsize=10, fontweight="bold")
ax.add_patch(FancyBboxPatch((1.8, 0.9), 1.8, 0.9, boxstyle="round,pad=0.06",
                            facecolor="#e8f0fb", edgecolor="#1f77b4"))
ax.text(2.7, 1.35, "All cells", ha="center", va="center", fontsize=9)
ax.add_patch(FancyArrowPatch((3.7, 1.35), (5.0, 1.35), arrowstyle="->", mutation_scale=12))
ax.add_patch(FancyBboxPatch((5.1, 0.9), 1.8, 0.9, boxstyle="round,pad=0.06",
                            facecolor="white", edgecolor="gray"))
ax.text(6.0, 1.55, "1st run", ha="center", va="center", fontsize=9)
ax.text(6.0, 1.15, "predict normals", ha="center", va="center", fontsize=7, style="italic")
ax.add_patch(FancyArrowPatch((7.0, 1.35), (8.3, 1.35), arrowstyle="->", mutation_scale=12))
ax.add_patch(FancyBboxPatch((8.4, 0.9), 1.5, 0.9, boxstyle="round,pad=0.06",
                            facecolor="#dff3d8", edgecolor="#2ca02c"))
ax.text(9.15, 1.55, "2nd run", ha="center", va="center", fontsize=9)
ax.text(9.15, 1.15, "corrected CNAs", ha="center", va="center", fontsize=7, style="italic")
save(fig, "fig_two_pass")

print("All figures written to", OUTDIR)
