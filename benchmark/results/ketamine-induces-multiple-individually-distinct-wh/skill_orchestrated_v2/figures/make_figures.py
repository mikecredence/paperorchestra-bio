"""Generate figures for the ketamine whole-brain connectivity paper.

All numerical values are drawn verbatim from the experimental log
(idea_summary.md statistical_sentences) and outline.json table_plan.
No values are invented.
"""

import os
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))


def _save(fig, name):
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---- Fig 1: variance explained by significant PCs -----------------
# Neural PC1=14.1, PC2=10.4 ; Behavioral PC1=29.0, PC2=12.0
labels = ["Neural\nPC1", "Neural\nPC2", "Behavioral\nPC1", "Behavioral\nPC2"]
values = [14.1, 10.4, 29.0, 12.0]
colors = ["#3b4cc0", "#6a8bd8", "#c9382b", "#dd7b6e"]

fig, ax = plt.subplots(figsize=(5.2, 3.4))
bars = ax.bar(labels, values, color=colors, edgecolor="black", linewidth=0.8)
ax.set_ylabel("Variance explained (%)")
ax.set_title("Variance explained by significant PCs")
ax.set_ylim(0, 34)
for b, v in zip(bars, values):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v:.1f}%",
            ha="center", va="bottom", fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
_save(fig, "fig1_variance")


# ---- Fig 2: effective dimensionality across drugs -----------------
# LSD 8.7+/-0.3 ; psilocybin 8.6+/-0.3 ; ketamine 12.8+/-0.7
# F(2,60)=564, p<.001
drugs = ["LSD", "Psilocybin", "Ketamine"]
means = [8.7, 8.6, 12.8]
errs = [0.3, 0.3, 0.7]
colors2 = ["#b39cd0", "#6a4c93", "#4a4a4a"]

fig, ax = plt.subplots(figsize=(4.6, 3.4))
bars = ax.bar(drugs, means, yerr=errs, color=colors2, edgecolor="black",
              linewidth=0.8, capsize=6,
              error_kw={"elinewidth": 1.2, "ecolor": "black"})
ax.set_ylabel("Effective dimensionality")
ax.set_title(r"Effective dimensionality of $\Delta$GBC response")
ax.set_ylim(0, 15)
for b, m, e in zip(bars, means, errs):
    ax.text(b.get_x() + b.get_width() / 2, m + e + 0.3,
            f"{m:.1f}$\\pm${e:.1f}", ha="center", va="bottom", fontsize=9)
# significance bracket ketamine vs LSD, psilocybin
y = 14.0
ax.plot([0, 2], [y, y], color="black", linewidth=1)
ax.plot([1, 2], [y - 0.6, y - 0.6], color="black", linewidth=1)
ax.text(1.0, y + 0.1, "***", ha="center", va="bottom", fontsize=11)
ax.text(1.5, y - 0.5, "***", ha="center", va="bottom", fontsize=11)
ax.spines[["top", "right"]].set_visible(False)
_save(fig, "fig2_dimensionality")


# ---- Fig 3: gene expression correlations --------------------------
# PC1 vs SST r=0.47; PC1 vs PVALB r=-0.22
# Neuro-behavioral PC1 vs SST r=0.29; vs PVALB r=-0.14
groups = ["Neural PC1", "Neuro-behavioral PC1"]
sst = [0.47, 0.29]
pvalb = [-0.22, -0.14]

x = np.arange(len(groups))
width = 0.36

fig, ax = plt.subplots(figsize=(5.4, 3.4))
b1 = ax.bar(x - width / 2, sst, width, color="#d62728", edgecolor="black",
            linewidth=0.8, label="SST")
b2 = ax.bar(x + width / 2, pvalb, width, color="#1f77b4", edgecolor="black",
            linewidth=0.8, label="PVALB")
ax.axhline(0, color="black", linewidth=0.6)
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_ylabel("Spatial correlation r")
ax.set_title("Gene expression correlations with ketamine PCs")
ax.set_ylim(-0.4, 0.6)
for b, v in zip(b1, sst):
    ax.text(b.get_x() + b.get_width() / 2,
            v + (0.03 if v >= 0 else -0.07),
            f"{v:+.2f}", ha="center", va="bottom", fontsize=9)
for b, v in zip(b2, pvalb):
    ax.text(b.get_x() + b.get_width() / 2,
            v + (0.03 if v >= 0 else -0.07),
            f"{v:+.2f}", ha="center", va="bottom", fontsize=9)
ax.legend(loc="upper right", frameon=False)
ax.spines[["top", "right"]].set_visible(False)
_save(fig, "fig3_gene_corr")


# ---- Fig 4: neuro-behavioral PC1 map vs PANSS subscale maps -------
# r=0.69, 0.93, 0.89
panss = ["PANSS\nPositive", "PANSS\nNegative", "PANSS\nGeneral"]
rvals = [0.69, 0.93, 0.89]

fig, ax = plt.subplots(figsize=(4.6, 3.4))
bars = ax.bar(panss, rvals, color=["#e07a5f", "#3d405b", "#81b29a"],
              edgecolor="black", linewidth=0.8)
ax.set_ylabel("Spatial r with neuro-behavioral PC1 map")
ax.set_title("Neuro-behavioral PC1 tracks PANSS topography")
ax.set_ylim(0, 1.05)
for b, v in zip(bars, rvals):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.02, f"r={v:.2f}",
            ha="center", va="bottom", fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
_save(fig, "fig4_panss_map_corr")


if __name__ == "__main__":
    print("Wrote:", sorted(os.listdir(OUT)))
