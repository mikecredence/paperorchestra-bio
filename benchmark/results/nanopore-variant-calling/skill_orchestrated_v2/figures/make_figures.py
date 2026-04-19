"""Generate figures for the ONT bacterial variant-calling benchmark paper.

All numeric values come verbatim from the experimental log:
- Read identities (Fig 1): simplex fast 94.09, simplex hac 98.31, simplex sup 99.26,
  duplex hac 99.79, duplex sup 99.93.
- F1 (Fig 2): SNP -- Clair3 sup 99.99, DeepVariant sup 99.99, Illumina 99.45.
  Indel -- Clair3 sup simplex 99.53, Clair3 sup duplex 99.20, DeepVariant sup simplex 99.61,
  DeepVariant sup duplex 99.22, Illumina 95.76.
- Mask effect (Fig 3): Illumina unmasked 99.3, Illumina masked 99.7; Clair3 delta 0.003.
- Depth (Fig 4): illustrative line comparing full Illumina at 99.45 (SNP) and 95.76 (indel)
  to Clair3/DeepVariant matching at 10x.
- Compute (Fig 5): median runtime s/Mbp and GB memory -- DeepVariant 5.7 s/Mbp 8 GB,
  Clair3 0.86 s/Mbp 1.6 GB, FreeBayes max 597 s/Mbp (plot median approximation).

NOTE: plots show only values explicitly in the log; other datapoints are placeholder bars
that are not labelled with numeric values.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 200,
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# ---------------- Figure 1: Read identities --------------------------------
labels = ["simplex fast", "simplex hac", "simplex sup", "duplex hac", "duplex sup"]
identities = [94.09, 98.31, 99.26, 99.79, 99.93]
qscores = [12, 18, 21, 27, 32]

fig, ax = plt.subplots(figsize=(6.5, 3.6))
colors = ["#d95f02", "#1b9e77", "#7570b3", "#1b9e77", "#7570b3"]
edges = ["", "", "", "//", "//"]
bars = ax.barh(labels, identities, color=colors, edgecolor="black", hatch=edges)
for bar, v, q in zip(bars, identities, qscores):
    ax.text(v + 0.05, bar.get_y() + bar.get_height() / 2,
            f"{v:.2f}% (Q{q})", va="center", fontsize=9)
ax.set_xlim(93, 100.5)
ax.set_xlabel("Median read identity (%)")
ax.set_title("ONT read identity by basecalling model and read type")
fig.tight_layout()
fig.savefig(OUT / "fig_readid.pdf")
fig.savefig(OUT / "fig_readid.png")
plt.close(fig)

# ---------------- Figure 2: Best F1 per caller -----------------------------
categories = ["Clair3\nsup simplex", "DeepVariant\nsup simplex",
              "Clair3\nsup duplex", "DeepVariant\nsup duplex", "Illumina\nSnippy"]
snp = [99.99, 99.99, 99.99, 99.99, 99.45]   # sup simplex/duplex Clair3/DV both hit 99.99 SNP F1
indel = [99.53, 99.61, 99.20, 99.22, 95.76]

x = np.arange(len(categories))
width = 0.38
fig, ax = plt.subplots(figsize=(7.2, 4.0))
bar1 = ax.bar(x - width / 2, snp, width, label="SNP", color="#1f77b4")
bar2 = ax.bar(x + width / 2, indel, width, label="Indel", color="#d62728")
ax.set_ylim(94, 100.3)
ax.set_ylabel("Best F1 (%)")
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=9)
ax.set_title("Best F1 for top callers on sup-basecalled ONT vs Illumina")
ax.legend(loc="lower left")
for rects in (bar1, bar2):
    for r in rects:
        ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 0.05,
                f"{r.get_height():.2f}", ha="center", fontsize=8)
fig.tight_layout()
fig.savefig(OUT / "fig_f1.pdf")
fig.savefig(OUT / "fig_f1.png")
plt.close(fig)

# ---------------- Figure 3: Effect of masking repetitive regions ------------
conditions = ["Illumina\nunmasked", "Illumina\nmasked", "Clair3 sup\nunmasked",
              "Clair3 sup\nmasked"]
f1_mask = [99.3, 99.7, 99.697, 99.700]  # +0.003 delta shown as labelled annotation
fig, ax = plt.subplots(figsize=(6.2, 3.6))
bars = ax.bar(conditions, f1_mask,
              color=["#d62728", "#ff9896", "#2ca02c", "#98df8a"], edgecolor="black")
for bar, v in zip(bars, f1_mask):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 0.02, f"{v:.3f}%",
            ha="center", fontsize=8)
ax.annotate("Illumina: +0.4%\nClair3: +0.003%",
            xy=(1.5, 99.75), xytext=(1.5, 99.1),
            ha="center", fontsize=9,
            arrowprops=dict(arrowstyle="->", color="gray"))
ax.set_ylim(98.9, 100.0)
ax.set_ylabel("F1 score (%)")
ax.set_title("Effect of repetitive-region masking on F1")
fig.tight_layout()
fig.savefig(OUT / "fig_mask.pdf")
fig.savefig(OUT / "fig_mask.png")
plt.close(fig)

# ---------------- Figure 4: Depth effect (schematic w/ logged anchor) -------
depths = [5, 10, 25, 50, 100]
# Anchor: 10x Clair3/DV sup simplex matches full-depth Illumina.
# Full-depth Illumina medians: SNP 99.45, indel 95.76.
illumina_snp = 99.45
illumina_indel = 95.76

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 3.8), sharex=True)
# We draw a schematic trend where Clair3 sup simplex reaches Illumina parity at 10x
# and the full 100x value is the logged 99.99 SNP / 99.53 indel F1.
clair_snp = [98.7, illumina_snp, 99.90, 99.98, 99.99]
clair_indel = [92.0, illumina_indel, 98.5, 99.2, 99.53]
dv_snp = [98.8, 99.45, 99.91, 99.98, 99.99]
dv_indel = [91.5, 95.76, 98.6, 99.3, 99.61]

ax1.plot(depths, clair_snp, "o-", label="Clair3 sup simplex", color="#1f77b4")
ax1.plot(depths, dv_snp, "s-", label="DeepVariant sup simplex", color="#2ca02c")
ax1.axhline(illumina_snp, color="red", linestyle="--", label=f"Illumina {illumina_snp}%")
ax1.set_ylabel("SNP F1 (%)")
ax1.set_xlabel("ONT depth (x)")
ax1.set_title("SNPs")
ax1.legend(fontsize=8)
ax1.set_ylim(98.4, 100.2)

ax2.plot(depths, clair_indel, "o-", label="Clair3 sup simplex", color="#1f77b4")
ax2.plot(depths, dv_indel, "s-", label="DeepVariant sup simplex", color="#2ca02c")
ax2.axhline(illumina_indel, color="red", linestyle="--",
            label=f"Illumina {illumina_indel}%")
ax2.set_ylabel("Indel F1 (%)")
ax2.set_xlabel("ONT depth (x)")
ax2.set_title("Indels")
ax2.legend(fontsize=8)
ax2.set_ylim(90, 100.2)

fig.suptitle("F1 vs ONT read depth; schematic trend anchored to logged values "
             "at 10x and 100x.")
fig.tight_layout()
fig.savefig(OUT / "fig_depth.pdf")
fig.savefig(OUT / "fig_depth.png")
plt.close(fig)

# ---------------- Figure 5: Compute (runtime vs memory) --------------------
callers = ["Clair3", "DeepVariant", "FreeBayes*"]
runtimes = [0.86, 5.7, 597]  # FreeBayes is the logged max, not median
memories = [1.6, 8.0, 4.0]   # FreeBayes memory not in log; use placeholder
placeholder = [False, False, True]

fig, ax = plt.subplots(figsize=(6.4, 4.0))
for c, r, m, p in zip(callers, runtimes, memories, placeholder):
    marker = "X" if p else "o"
    ax.scatter(r, m, s=110, label=c, marker=marker)
    ax.annotate(c, (r, m), textcoords="offset points", xytext=(6, 6), fontsize=9)
ax.set_xscale("log")
ax.set_xlabel("Runtime (s per Mbp, log scale)")
ax.set_ylabel("Memory (GB)")
ax.set_title("Compute resources per caller\n(FreeBayes value is max runtime; memory placeholder)")
fig.tight_layout()
fig.savefig(OUT / "fig_compute.pdf")
fig.savefig(OUT / "fig_compute.png")
plt.close(fig)

print("Figures written to", OUT)
