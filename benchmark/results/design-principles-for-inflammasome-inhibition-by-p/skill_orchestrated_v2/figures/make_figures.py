"""
Figure generation for "Design Principles for Inflammasome Inhibition by POPs"
All numerical values are taken verbatim from inputs/experimental_log.md and
outline.json. No values are invented.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 10,
        "axes.titlesize": 11,
        "legend.fontsize": 9,
        "figure.dpi": 120,
    }
)

COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
OUTDIR = Path(__file__).parent
OUTDIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Figure 1: Rosetta interface energies (DeltaG, REU) - homotypic vs POP-PYD
# ---------------------------------------------------------------------------
# Values from outline.json / experimental_log.md:
#   ASCPYD-ASCPYD (top-half sum) = -35.9   (homotypic)
#   POP1-ASCPYD  (top-half sum)  = -24.7
#   POP1-ASCPYD  (bottom-half)   = -34.3
#   POP3-ASCPYD  (bottom-half)   = -34.6
#   NLRP3PYD-NLRP3PYD            = -31.4
#   POP1-NLRP3PYD                = -30.5
#   IFI16PYD top-half POP3       = -9.6
#   Exemplar symmetric ASC 1a/1b = -22.1

fig, ax = plt.subplots(figsize=(6.2, 3.6))

groups = ["ASC$_{PYD}$", "NLRP3$_{PYD}$", "IFI16$_{PYD}$\n(top)"]
homotypic_top = [-35.9, -31.4, float("nan")]   # IFI16 top-half homotypic not numerically given
pop_top = [-24.7, -30.5, -9.6]  # POP1 top-half (ASC, NLRP3) and POP3 top-half (IFI16)
pop_labels = ["POP1", "POP1", "POP3"]

x = np.arange(len(groups))
width = 0.36

bars_h = ax.bar(
    x - width / 2,
    [v if not np.isnan(v) else 0 for v in homotypic_top],
    width,
    color=COLORS[0],
    label="Homotypic PYD--PYD",
    edgecolor="black",
    linewidth=0.6,
)
bars_p = ax.bar(
    x + width / 2,
    pop_top,
    width,
    color=COLORS[1],
    label="POP--PYD",
    edgecolor="black",
    linewidth=0.6,
)

for bar, v in zip(bars_h, homotypic_top):
    if not np.isnan(v):
        ax.text(bar.get_x() + bar.get_width() / 2, v - 1.8, f"{v:.1f}",
                ha="center", va="top", fontsize=8)
for bar, v, lbl in zip(bars_p, pop_top, pop_labels):
    ax.text(bar.get_x() + bar.get_width() / 2, v - 1.8, f"{lbl}\n{v:.1f}",
            ha="center", va="top", fontsize=8)

ax.axhline(0, color="gray", linewidth=0.6)
ax.set_ylabel(r"Interface energy $\Delta G$ (REU, top-half sum)")
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_title("Rosetta interface energies: homotypic vs POP--PYD")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.invert_yaxis()  # more negative (more favourable) points downward
ax.legend(loc="lower right", frameon=False)
plt.tight_layout()
plt.savefig(OUTDIR / "fig_rosetta_dg.pdf")
plt.savefig(OUTDIR / "fig_rosetta_dg.png", dpi=200)
plt.close()


# ---------------------------------------------------------------------------
# Figure 2: Cellular suppression of PYD filaments/puncta by POPs (1200 ng)
# Values (% suppression relative to eGFP control):
#   ASCPYD:  POP1 20, POP2 ~80 (used "up to ~80% reduction"), POP3 ~80
#   ASCFL puncta: POP1 ~30, POP2 ~80, POP3 ~80
#   AIM2PYD: POP1 ~60, POP2 ~essentially eliminated (use 95), POP3 ~95
#   IFI16PYD: POP1 ~60, POP2 ~95, POP3 ~95
#   NLRP3PYD: POP1 70; POP2/POP3 values not directly reported at 1200 ng ->
#     omit to avoid fabrication; add from 600 ng POP3 = 40-50% (use 45)
#   NLRP6PYD: POP1 60; same caveat.
#
# Strategy: plot only values explicitly in log at 1200 ng POP to stay faithful.
#   ASCPYD: POP1=20, POP2=80 (ASCFL puncta listed), POP3=80 (cells context)
# To avoid fabrication we keep only the clearly stated 1200 ng numbers:
#   POP1 at 1200 ng: ASCPYD 20, AIM2PYD 60, IFI16PYD 60, NLRP3PYD 70, NLRP6PYD 60
# ---------------------------------------------------------------------------

targets = ["ASC$_{PYD}$", "AIM2$_{PYD}$", "IFI16$_{PYD}$", "NLRP3$_{PYD}$", "NLRP6$_{PYD}$"]
pop1_sup = [20, 60, 60, 70, 60]  # all verbatim from log/outline at 1200 ng POP1

fig, ax = plt.subplots(figsize=(6.2, 3.4))
bars = ax.bar(targets, pop1_sup, color=COLORS[2], edgecolor="black", linewidth=0.6)
for bar, v in zip(bars, pop1_sup):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 1.5, f"{v}%",
            ha="center", va="bottom", fontsize=9)

ax.set_ylabel("Filament suppression (\\%) vs eGFP control")
ax.set_title("POP1 suppression of PYD filament assembly in HEK293T (1200 ng POP1-eGFP)")
ax.set_ylim(0, 100)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.axhline(50, color="gray", linewidth=0.4, linestyle="--")
plt.tight_layout()
plt.savefig(OUTDIR / "fig_pop1_suppression.pdf")
plt.savefig(OUTDIR / "fig_pop1_suppression.png", dpi=200)
plt.close()


# ---------------------------------------------------------------------------
# Figure 3: POP2/POP3 concentration ranges used in FRET assays
# Values verbatim from experimental_log.md:
#   ASCPYD assay:
#     POP1: 50, 150 uM
#     POP2: 3.3, 6.7, 13.3, 26.7, 40 uM
#     POP3: 3.25, 7.5, 15, 20, 30 uM
#   AIM2PYD assay:
#     POP1: 25, 50, 100, 150 uM
#     POP2: 12.5, 25, 50, 75 uM
#     POP3: 7.5, 15, 30, 40, 50 uM
#   NLRP6PYD assay:
#     POP1: 25, 50, 100 uM
#     POP2: 30, 60, 120 uM
#     POP3: 15, 30, 60 uM
# Plot concentration series per POP for each substrate.
# ---------------------------------------------------------------------------

fret_data = {
    "ASC$_{PYD}$ (2.5 \u00b5M)": {
        "POP1": [50, 150],
        "POP2": [3.3, 6.7, 13.3, 26.7, 40],
        "POP3": [3.25, 7.5, 15, 20, 30],
    },
    "AIM2$_{PYD}$ (2.5 \u00b5M)": {
        "POP1": [25, 50, 100, 150],
        "POP2": [12.5, 25, 50, 75],
        "POP3": [7.5, 15, 30, 40, 50],
    },
    "NLRP6$_{PYD}$ (2.5 \u00b5M)": {
        "POP1": [25, 50, 100],
        "POP2": [30, 60, 120],
        "POP3": [15, 30, 60],
    },
}

fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), sharey=True)
pop_colors = {"POP1": COLORS[0], "POP2": COLORS[1], "POP3": COLORS[3]}

for ax, (substrate, series) in zip(axes, fret_data.items()):
    ypos = 0
    ylabels = []
    for pop, concs in series.items():
        ypos += 1
        ax.scatter(concs, [ypos] * len(concs),
                   s=70, color=pop_colors[pop], edgecolor="black",
                   linewidth=0.6, zorder=3)
        # connect to show range
        ax.plot([min(concs), max(concs)], [ypos, ypos],
                color=pop_colors[pop], alpha=0.5, linewidth=2, zorder=2)
        ylabels.append(pop)
    ax.set_yticks(range(1, len(series) + 1))
    ax.set_yticklabels(ylabels)
    ax.set_xscale("log")
    ax.set_xlim(1, 200)
    ax.set_xlabel("POP concentration (\u00b5M)")
    ax.set_title(substrate)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", which="both", linestyle=":", alpha=0.4)

fig.suptitle("POP concentration series used in FRET polymerization assays",
             fontsize=11)
plt.tight_layout()
plt.savefig(OUTDIR / "fig_fret_concentrations.pdf")
plt.savefig(OUTDIR / "fig_fret_concentrations.png", dpi=200)
plt.close()


# ---------------------------------------------------------------------------
# Figure 4: Schematic of the Rosetta honeycomb interface strategy
# Six Type-1/2/3 a/b interfaces around a central PYD protomer. Structural
# description from outline.json; no numeric invention.
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(5.6, 5.2))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal")
ax.axis("off")

# central hexagon position: origin
def hex_vertices(cx, cy, r):
    return np.array([
        (cx + r * np.cos(np.deg2rad(60 * k + 30)),
         cy + r * np.sin(np.deg2rad(60 * k + 30)))
        for k in range(6)
    ])

def draw_hex(ax, cx, cy, r, facecolor, label=None, edgecolor="black"):
    v = hex_vertices(cx, cy, r)
    poly = plt.Polygon(v, closed=True, facecolor=facecolor,
                       edgecolor=edgecolor, linewidth=1.1)
    ax.add_patch(poly)
    if label:
        ax.text(cx, cy, label, ha="center", va="center", fontsize=9)

r = 0.18
# central
draw_hex(ax, 0.0, 0.0, r, "#f6d860", label="PYD$_{c}$")
# six neighbours
angles = np.deg2rad(np.arange(0, 360, 60))
interface_labels = ["Type 1a", "Type 2a", "Type 3a",
                    "Type 1b", "Type 2b", "Type 3b"]
neighbour_color = "#cde3ff"
for angle, lbl in zip(angles, interface_labels):
    # centre-to-centre distance = sqrt(3)*r
    dist = np.sqrt(3) * r
    nx, ny = dist * np.cos(angle), dist * np.sin(angle)
    draw_hex(ax, nx, ny, r, neighbour_color)
    # label halfway
    ax.text(0.62 * nx, 0.62 * ny, lbl, ha="center", va="center",
            fontsize=8, color="#222222",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=1.2))

ax.text(0, -0.9, "Honeycomb sideview: central protomer engages six\n"
                "neighbours via Type 1a/b, 2a/b, 3a/b interfaces",
        ha="center", va="center", fontsize=9)

plt.tight_layout()
plt.savefig(OUTDIR / "fig_honeycomb_schematic.pdf")
plt.savefig(OUTDIR / "fig_honeycomb_schematic.png", dpi=200)
plt.close()


# ---------------------------------------------------------------------------
# Figure 5: Model schematic - POP1 as decoy adaptor for upstream receptors
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(7.5, 3.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis("off")


def block(ax, x, y, w, h, text, color, fontsize=9):
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor=color, edgecolor="black", linewidth=0.9)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize)


def arrow(ax, x1, y1, x2, y2, color="black"):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        arrowstyle="-|>", mutation_scale=14,
                        color=color, linewidth=1.2)
    ax.add_patch(a)


# Canonical model row (top)
ax.text(0.1, 3.6, "Canonical (homology-based) model:", fontsize=9, style="italic")
block(ax, 0.2, 2.7, 1.6, 0.6, "POP1", "#ffd4a3")
arrow(ax, 1.8, 3.0, 2.4, 3.0)
block(ax, 2.4, 2.7, 1.6, 0.6, "ASC$_{PYD}$", "#a3cbff")
arrow(ax, 4.0, 3.0, 4.6, 3.0)
block(ax, 4.6, 2.7, 1.9, 0.6, "caspase-1 / IL-1$\\beta$", "#cfcfcf")
ax.text(7.0, 3.0, "(POP1 blocks ASC)", fontsize=8)

# Revised model row (bottom)
ax.text(0.1, 1.9, "Revised (this work) design principle:", fontsize=9, style="italic")
block(ax, 0.2, 0.9, 1.6, 0.6, "POP1", "#ffd4a3")
arrow(ax, 1.8, 1.2, 2.4, 1.2, color="#d62728")
block(ax, 2.4, 0.9, 2.0, 0.6, "Receptor PYDs\n(AIM2,IFI16,NLRP3,NLRP6)", "#c3efc3", fontsize=7)
arrow(ax, 4.4, 1.2, 5.0, 1.2)
block(ax, 5.0, 0.9, 1.6, 0.6, "ASC$_{PYD}$", "#a3cbff")
arrow(ax, 6.6, 1.2, 7.2, 1.2)
block(ax, 7.2, 0.9, 1.9, 0.6, "caspase-1 / IL-1$\\beta$", "#cfcfcf")
ax.text(0.2, 0.4,
        "POP1 acts as a decoy adaptor upstream of ASC. POP2/POP3 additionally"
        " block ASC nucleation.",
        fontsize=8)

plt.tight_layout()
plt.savefig(OUTDIR / "fig_model_schematic.pdf")
plt.savefig(OUTDIR / "fig_model_schematic.png", dpi=200)
plt.close()


print("Generated 5 figures in", OUTDIR)
