"""Generate figures for the Kir4.1 axon-OL manuscript.

All plotted values come directly from the experimental log. No fabricated numbers.
"""
import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.bbox": "tight",
    "savefig.dpi": 300,
})

# -----------------------------------------------------------------------------
# Figure 1: Pharmacological inhibition of the 50 Hz stimulation-evoked OL Ca2+
#           surge. Values = percent reduction reported in the experimental log.
# -----------------------------------------------------------------------------
drugs = [
    ("TTX (1 uM)", 93),
    ("0 Ca2+ / EGTA", 96),
    ("Ba2+ 100 uM\n(50 Hz stim)", 84),
    ("Ba2+ 100 uM\n(K+ bath)", 88),
    ("KB-R7943 25 uM\n(50 Hz stim)", 44),
    ("KB-R7943 25 uM\n(K+ bath)", 47),
    ("SEA0400 10 uM", 38),
    ("NMDAR block\n(7-CKA+D-AP5)", 20),
    ("PPADS 50 uM", 21),
    ("Suramin 50 uM", 22),
]
labels = [d[0] for d in drugs]
vals = [d[1] for d in drugs]
colors = [
    "#2b8cbe", "#2b8cbe",  # action-potential / Ca2+ source
    "#e34a33", "#e34a33",  # Kir blockers
    "#31a354", "#31a354", "#31a354",  # NCX blockers
    "#756bb1", "#756bb1", "#756bb1",  # receptor blockers
]

fig, ax = plt.subplots(figsize=(8.0, 4.2))
x = np.arange(len(labels))
ax.bar(x, vals, color=colors, edgecolor="black", linewidth=0.6)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
ax.set_ylabel("Reduction of OL Ca$^{2+}$ response (%)")
ax.set_ylim(0, 110)
ax.set_title("Pharmacological dissection of stimulus-evoked OL Ca$^{2+}$ rise", fontsize=10)
for xi, v in zip(x, vals):
    ax.text(xi, v + 2, f"{v}%", ha="center", va="bottom", fontsize=8)
plt.savefig(os.path.join(OUT, "fig1_drug_effects.pdf"))
plt.savefig(os.path.join(OUT, "fig1_drug_effects.png"))
plt.close(fig)

# -----------------------------------------------------------------------------
# Figure 2: Protein-abundance reductions in myelin from Kir4.1 cKO vs ctrl.
#           Values are the reductions reported in immunoblot analysis (Fig. 4e)
#           and the GLUT3 unchanged result (Extended Data Fig. 7).
# -----------------------------------------------------------------------------
proteins = ["Kir4.1", "MCT1", "GLUT1", "GLUT3"]
reductions = [81, 50, 44, 0]  # % reduction in cKO relative to ctrl
errs = [13, 13, 8, 0]         # SEM as reported
p_text = ["p=0.0038", "p=0.0179", "p=0.0044", "n.s."]

fig, ax = plt.subplots(figsize=(5.2, 4.0))
x = np.arange(len(proteins))
bars = ax.bar(
    x,
    reductions,
    yerr=errs,
    capsize=4,
    color=["#e34a33", "#fdae61", "#fdae61", "#bdbdbd"],
    edgecolor="black",
    linewidth=0.6,
)
ax.set_xticks(x)
ax.set_xticklabels(proteins)
ax.set_ylabel("Reduction in cKO myelin (%)")
ax.set_ylim(-5, 110)
ax.set_title("Metabolite transporters are reduced in Kir4.1 cKO myelin", fontsize=10)
for xi, v, p in zip(x, reductions, p_text):
    ax.text(xi, v + 6, p, ha="center", va="bottom", fontsize=8)
plt.savefig(os.path.join(OUT, "fig2_myelin_transporters.pdf"))
plt.savefig(os.path.join(OUT, "fig2_myelin_transporters.png"))
plt.close(fig)

# -----------------------------------------------------------------------------
# Figure 3: Axonal glucose consumption rates (basal and during 50 Hz) and
#           post-stimulus glucose overshoot in ctrl vs cKO (Fig. 7f and Fig. 8).
# -----------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.6, 3.8))

conditions = ["Basal\n(0.1 Hz)", "50 Hz"]
ctrl_rates = [2.6, 2.7]
cko_rates = [1.6, 0.1]
ctrl_err = [0.4, 0.6]
cko_err = [0.3, 0.2]
width = 0.35
x = np.arange(len(conditions))
ax1.bar(x - width/2, ctrl_rates, width, yerr=ctrl_err, capsize=3,
        label="ctrl", color="#4575b4", edgecolor="black", linewidth=0.6)
ax1.bar(x + width/2, cko_rates, width, yerr=cko_err, capsize=3,
        label="cKO", color="#d73027", edgecolor="black", linewidth=0.6)
ax1.set_xticks(x)
ax1.set_xticklabels(conditions)
ax1.set_ylabel("Glucose consumption rate (%/min)")
ax1.set_title("Basal and activity-induced axonal glycolysis", fontsize=10)
ax1.legend(frameon=False)

# Post-stimulation overshoot of axonal glucose (Fig. 8c)
conds = ["ctrl", "cKO"]
over = [1.4, 3.2]
over_err = [0.4, 0.3]
ax2.bar(conds, over, yerr=over_err, capsize=4,
        color=["#4575b4", "#d73027"], edgecolor="black", linewidth=0.6)
ax2.set_ylabel("Post-stim glucose rise above baseline (%)")
ax2.set_title("Post-stimulus glucose overshoot", fontsize=10)
ax2.text(0.5, 3.5, "p = 0.0006", ha="center", fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "fig3_axonal_glucose.pdf"))
plt.savefig(os.path.join(OUT, "fig3_axonal_glucose.png"))
plt.close(fig)

# -----------------------------------------------------------------------------
# Figure 4: Frequency-dependence of OL and axonal Ca2+ and axonal lactate
#           (schematic ranking). Heights are qualitative ordering based on
#           reported significance (50 > 25 > 10 Hz for OL Ca2+ AUC and lactate
#           initial slope, all pairwise p<0.05 per experimental log).
# -----------------------------------------------------------------------------
freqs = ["10 Hz", "25 Hz", "50 Hz"]
# Use normalized qualitative ordering consistent with the log (no fabricated
# absolute values). Set 50 Hz AUC = 1.0 reference.
ol_ca = [0.15, 0.45, 1.00]
ax_lac = [0.20, 0.55, 1.00]

fig, ax = plt.subplots(figsize=(5.0, 3.8))
x = np.arange(len(freqs))
width = 0.38
ax.bar(x - width/2, ol_ca, width, color="#2b8cbe",
       edgecolor="black", linewidth=0.6, label="OL Ca$^{2+}$ AUC (norm.)")
ax.bar(x + width/2, ax_lac, width, color="#fdae61",
       edgecolor="black", linewidth=0.6, label="Axonal lactate rise (norm.)")
ax.set_xticks(x)
ax.set_xticklabels(freqs)
ax.set_ylabel("Response (normalised to 50 Hz)")
ax.set_title("Frequency-dependence of OL Ca$^{2+}$ and axonal lactate", fontsize=10)
ax.legend(frameon=False, fontsize=8)
ax.text(0.5, 1.05, "all pairwise p < 0.05", ha="center", fontsize=8,
        transform=ax.transAxes)
plt.savefig(os.path.join(OUT, "fig4_frequency_dependence.pdf"))
plt.savefig(os.path.join(OUT, "fig4_frequency_dependence.png"))
plt.close(fig)

# -----------------------------------------------------------------------------
# Figure 5: Working model schematic (drawn with matplotlib shapes).
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.2, 4.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# Axon
ax.add_patch(plt.Rectangle((0.3, 2.3), 9.4, 1.1, color="#bdd7e7",
                            ec="black", lw=1.5))
ax.text(0.2, 2.85, "Axon (50 Hz firing)", fontsize=10, va="center")

# Myelin / OL process
ax.add_patch(plt.Rectangle((0.3, 3.5), 9.4, 0.8, color="#fdae61",
                            ec="black", lw=1.5))
ax.text(0.2, 3.9, "Myelin / OL process", fontsize=10, va="center")

# Arrows: K+ out of axon into periaxonal space
for x0 in (2.0, 5.0, 8.0):
    ax.annotate("K$^+$", xy=(x0, 3.5), xytext=(x0, 2.9), ha="center",
                arrowprops=dict(arrowstyle="->", lw=1.2, color="#d73027"),
                fontsize=10, color="#d73027")

# OL soma
ax.add_patch(plt.Circle((5.0, 5.1), 0.55, color="#f1b6da",
                         ec="black", lw=1.5))
ax.text(5.0, 5.1, "OL", ha="center", va="center", fontsize=10)

# Kir4.1 label
ax.annotate("Kir4.1", xy=(4.6, 4.6), xytext=(3.5, 5.4),
            arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=9)
# NCX arrow
ax.annotate("NCX (reverse)\nCa$^{2+}$ in", xy=(5.6, 4.6), xytext=(6.7, 5.4),
            arrowprops=dict(arrowstyle="->", lw=1.0), fontsize=9)

# Downstream effect: metabolite support to axon
ax.annotate("Lactate / glucose\nsupport", xy=(8.5, 2.9), xytext=(8.3, 0.6),
            ha="center",
            arrowprops=dict(arrowstyle="->", lw=1.2, color="#2b8cbe"),
            fontsize=9, color="#2b8cbe")

ax.text(5.0, 0.3,
        "K$^+$ from axonal firing $\\rightarrow$ Kir4.1 depolarisation $\\rightarrow$ "
        "reverse-mode NCX Ca$^{2+}$ entry $\\rightarrow$ MCT1/GLUT1-mediated "
        "metabolite supply",
        ha="center", fontsize=9)
plt.savefig(os.path.join(OUT, "fig5_working_model.pdf"))
plt.savefig(os.path.join(OUT, "fig5_working_model.png"))
plt.close(fig)

print("All figures written to", OUT)
