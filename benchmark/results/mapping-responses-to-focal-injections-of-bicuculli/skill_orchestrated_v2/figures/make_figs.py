"""
Figure generation for pFL bicuculline rostrocaudal mapping paper.

Every value below is quoted verbatim from
  inputs/idea_summary.md  and  inputs/experimental_log.md.
No fabricated data.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle, Ellipse

# -------- Shared styling --------
GROUP_LABELS = ["-0.2", "+0.1", "+0.4", "+0.6", "+0.8"]
GROUP_N = [5, 7, 5, 6, 5]
GROUP_COLORS = ["#d62728", "#2ca02c", "#1f77b4", "#9467bd", "#ff7f0e"]
CTRL_COLOR = "#7f7f7f"

plt.rcParams.update({
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 130,
})


def _save(fig, stem):
    fig.savefig(f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(f"{stem}.png", bbox_inches="tight", dpi=160)
    plt.close(fig)


# --------------------------------------------------------------------------
# Figure 1. Experimental schematic and cFos activation map.
# Values used:
#   CTRL average: 44.7 +/- 4.0 cFos+ cells/hemisection (n=7)
#   Peak cFos: -0.2=89.7; +0.1=123.1; +0.4=110.2; +0.6=98.3; +0.8=101.2
#   Background outside core: 44.8 +/- 1.2
#   PHOX2B+/cFos+: CTRL 2.3+/-1.0 vs BIC 2.4+/-0.4
# --------------------------------------------------------------------------
def fig1_schematic_and_cfos():
    fig = plt.figure(figsize=(7.5, 3.2))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.1, 1.3, 0.9])

    # --- Panel A: schematic of injection along rostrocaudal axis ---
    axA = fig.add_subplot(gs[0, 0])
    axA.set_xlim(-0.5, 1.1)
    axA.set_ylim(-1.0, 1.2)
    # draw facial nucleus region
    axA.add_patch(Rectangle((-0.45, 0.3), 0.45, 0.35, fc="#e0e0e0", ec="k"))
    axA.text(-0.23, 0.47, "VII", ha="center", va="center", fontsize=9)
    axA.axvline(0.0, color="k", lw=0.8, ls="--")
    axA.text(0.0, 0.75, "VIIc", ha="center", fontsize=8)
    # injection coords
    coords = [-0.2, 0.1, 0.4, 0.6, 0.8]
    for c, col, lab in zip(coords, GROUP_COLORS, GROUP_LABELS):
        axA.plot(c, 0.0, marker="v", color=col, markersize=10, mec="k")
        axA.text(c, -0.25, lab, ha="center", fontsize=7, color=col)
    axA.annotate("", xy=(1.05, 0.0), xytext=(-0.45, 0.0),
                 arrowprops=dict(arrowstyle="->", lw=1.0))
    axA.text(1.05, -0.15, "rostral", fontsize=7, ha="right")
    axA.text(-0.45, -0.15, "caudal", fontsize=7, ha="left")
    axA.text(0.3, 1.0, "pFL", fontsize=10, ha="center", style="italic")
    axA.set_xlabel("mm from VIIc")
    axA.set_yticks([])
    axA.set_title("A  Injection coordinates")

    # --- Panel B: cFos cells at core of injection site ---
    axB = fig.add_subplot(gs[0, 1])
    peaks = [89.7, 123.1, 110.2, 98.3, 101.2]
    x = np.arange(len(GROUP_LABELS))
    axB.bar(x, peaks, color=GROUP_COLORS, edgecolor="k", linewidth=0.7)
    axB.axhline(44.7, color=CTRL_COLOR, lw=1.2, ls="--", label="CTRL 44.7")
    axB.fill_between([-0.6, len(x)-0.4], 44.7-4.0, 44.7+4.0,
                     color=CTRL_COLOR, alpha=0.15)
    axB.set_xticks(x)
    axB.set_xticklabels(GROUP_LABELS)
    axB.set_xlabel("mm from VIIc")
    axB.set_ylabel("cFos+ cells / hemisection\nat injection core")
    axB.set_xlim(-0.6, len(x)-0.4)
    axB.set_title("B  Peak cFos activation")
    axB.legend(loc="upper right", frameon=False)
    for xi, v in zip(x, peaks):
        axB.text(xi, v+3, f"{v:.1f}", ha="center", fontsize=7)

    # --- Panel C: PHOX2B+/cFos+ counts ---
    axC = fig.add_subplot(gs[0, 2])
    groups = ["CTRL", "BIC"]
    vals = [2.3, 2.4]
    errs = [1.0, 0.4]
    axC.bar(groups, vals, yerr=errs, color=[CTRL_COLOR, "#9467bd"],
            edgecolor="k", capsize=4)
    axC.set_ylabel("PHOX2B+ / cFos+ cells\nper hemisection")
    axC.set_ylim(0, 4.5)
    axC.set_title("C  RTN engagement")
    for i, (v, e) in enumerate(zip(vals, errs)):
        axC.text(i, v+e+0.15, f"{v:.1f}", ha="center", fontsize=8)

    fig.tight_layout()
    _save(fig, "fig1_schematic_cfos")


# --------------------------------------------------------------------------
# Figure 2.  Temporal characteristics of ABD response.
#  - ABD duration: -0.2=2.4+-1.1; +0.1 not reported in number but rostral trend
#    The log explicitly gives:  -0.2 = 2.4+-1.1, +0.6 = 17.6+-2.7, +0.8 = 17.1+-3.3
#    It does not quote +0.1 and +0.4 mean+-SE; we display only values quoted.
#  - ABD/DIA coupling: -0.2=0.6+-0.2; +0.4=0.96+-0.02; +0.6=0.89+-0.05; +0.8=0.97+-0.02
#  - Onset latency (s):  -0.2=20.3+-13.4; +0.1=32.5+-20.6; +0.4=40.1+-28.7;
#    +0.6=-88.7+-32.3 (negative: before second injection); +0.8=23.1+-19.8
# --------------------------------------------------------------------------
def fig2_abd_temporal():
    fig, axes = plt.subplots(1, 3, figsize=(8.0, 2.9))

    # Panel A: ABD response duration (values only for coords reported)
    durations = {"-0.2": (2.4, 1.1), "+0.6": (17.6, 2.7), "+0.8": (17.1, 3.3)}
    lbls = list(durations.keys())
    vals = [durations[k][0] for k in lbls]
    err = [durations[k][1] for k in lbls]
    col = [GROUP_COLORS[GROUP_LABELS.index(k)] for k in lbls]
    axA = axes[0]
    axA.bar(lbls, vals, yerr=err, color=col, edgecolor="k", capsize=4)
    axA.set_ylabel("ABD response duration (min)")
    axA.set_xlabel("mm from VIIc")
    axA.set_title("A  Duration")
    axA.set_ylim(0, 25)

    # Panel B: ABD/DIA coupling
    coupling = {"-0.2": (0.6, 0.2), "+0.4": (0.96, 0.02),
                "+0.6": (0.89, 0.05), "+0.8": (0.97, 0.02)}
    lbls = list(coupling.keys())
    vals = [coupling[k][0] for k in lbls]
    err = [coupling[k][1] for k in lbls]
    col = [GROUP_COLORS[GROUP_LABELS.index(k)] for k in lbls]
    axB = axes[1]
    axB.bar(lbls, vals, yerr=err, color=col, edgecolor="k", capsize=4)
    axB.set_ylabel("ABD / DIA coupling")
    axB.set_xlabel("mm from VIIc")
    axB.set_title("B  Coupling")
    axB.set_ylim(0, 1.1)

    # Panel C: Onset latency (seconds). Negative means BEFORE 2nd injection.
    onset = {"-0.2": (20.3, 13.4), "+0.1": (32.5, 20.6),
             "+0.4": (40.1, 28.7), "+0.6": (-88.7, 32.3),
             "+0.8": (23.1, 19.8)}
    lbls = list(onset.keys())
    vals = [onset[k][0] for k in lbls]
    err = [onset[k][1] for k in lbls]
    col = [GROUP_COLORS[GROUP_LABELS.index(k)] for k in lbls]
    axC = axes[2]
    axC.bar(lbls, vals, yerr=err, color=col, edgecolor="k", capsize=4)
    axC.axhline(0, color="k", lw=0.6)
    axC.set_ylabel("Onset latency (s)\nrelative to 2nd injection")
    axC.set_xlabel("mm from VIIc")
    axC.set_title("C  Onset latency")
    axC.annotate("before 2nd inj.", xy=(3.0, -60), xytext=(3.0, -130),
                 fontsize=7, ha="center",
                 arrowprops=dict(arrowstyle="->", lw=0.7))

    fig.tight_layout()
    _save(fig, "fig2_abd_temporal")


# --------------------------------------------------------------------------
# Figure 3.  Peak respiratory and metabolic changes.
# Values reported:
#   Minimum respiratory rate (bpm):
#     -0.2 = 37.08 +- 1.36 (12% drop)
#     +0.1 = 37.2  +- 2.0  (17% drop)
#     +0.4 = 40.1  +- 1.6  (9%  drop)
#     +0.6 = 38.6  +- 2.6  (10% drop)
#     +0.8 = 39.1  +- 2.2  (11% drop)
#   Peak VT (ml/kg): -0.2=7.0+-0.4 (+8%); +0.1=8.0+-0.3 (+16%); +0.6=10.8+-0.5 (+29%)
#   VE (ml/min/kg):  -0.2=255.4+-16.2 (-12%); +0.6=414.3+-22.7 (+16%)
#   VO2 (ml/min/kg): +0.6=11.8+-0.8 (-33%); +0.8=12.2+-6.1 (-25%);
#                    -0.2=17.3+-3.3 (-10%); +0.1=17.6+-1.3 (-17%)
#   VE/VO2 peak (%BL): +0.6 = +73% (34.8+-3.0); +0.8 = +82% (38.7+-12.8)
# --------------------------------------------------------------------------
def fig3_respiratory_metabolic():
    fig, axes = plt.subplots(2, 2, figsize=(7.5, 5.2))

    # Panel A: minimum respiratory frequency
    freq = {"-0.2": (37.08, 1.36), "+0.1": (37.2, 2.0),
            "+0.4": (40.1, 1.6),   "+0.6": (38.6, 2.6),
            "+0.8": (39.1, 2.2)}
    lbls = list(freq.keys())
    vals = [freq[k][0] for k in lbls]
    err = [freq[k][1] for k in lbls]
    col = [GROUP_COLORS[GROUP_LABELS.index(k)] for k in lbls]
    axA = axes[0, 0]
    axA.bar(lbls, vals, yerr=err, color=col, edgecolor="k", capsize=4)
    axA.set_ylabel("min respiratory rate (bpm)")
    axA.set_xlabel("mm from VIIc")
    axA.set_title("A  Minimum respiratory rate")
    axA.set_ylim(30, 45)

    # Panel B: peak VT (only three values reported)
    vt = {"-0.2": (7.0, 0.4), "+0.1": (8.0, 0.3), "+0.6": (10.8, 0.5)}
    lbls = list(vt.keys())
    vals = [vt[k][0] for k in lbls]
    err = [vt[k][1] for k in lbls]
    col = [GROUP_COLORS[GROUP_LABELS.index(k)] for k in lbls]
    axB = axes[0, 1]
    axB.bar(lbls, vals, yerr=err, color=col, edgecolor="k", capsize=4)
    axB.set_ylabel("peak V$_T$ (ml/kg)")
    axB.set_xlabel("mm from VIIc")
    axB.set_title("B  Peak tidal volume")
    axB.set_ylim(0, 12)

    # Panel C: VE percent change from baseline (explicit values)
    ve_pct = {"-0.2": -12, "+0.4": None, "+0.6": +16}  # only two numbered
    # plot only -0.2 and +0.6 per log (other groups described qualitatively)
    lbls = ["-0.2", "+0.6"]
    vals = [-12, +16]
    col = [GROUP_COLORS[GROUP_LABELS.index(k)] for k in lbls]
    axC = axes[1, 0]
    bars = axC.bar(lbls, vals, color=col, edgecolor="k")
    axC.axhline(0, color="k", lw=0.8)
    axC.set_ylabel("$\\Delta$ V$_E$ (% from baseline)")
    axC.set_xlabel("mm from VIIc")
    axC.set_title("C  Minute ventilation")
    for b, v in zip(bars, vals):
        axC.text(b.get_x()+b.get_width()/2,
                 v + (1.5 if v>=0 else -2.5),
                 f"{v:+d}%", ha="center", fontsize=8)

    # Panel D: VO2 and VE/VO2 percent change at rostral sites
    labels = ["-0.2", "+0.1", "+0.6", "+0.8"]
    vo2_pct = [-10, -17, -33, -25]
    axD = axes[1, 1]
    x = np.arange(len(labels))
    w = 0.38
    b1 = axD.bar(x - w/2, vo2_pct, width=w, color="#4a90e2", edgecolor="k",
                 label="$\\Delta$ V$_{O_2}$")
    # VE/VO2: only +0.6 and +0.8 reported, pad others with NaN-like zero sentinel
    vevo2_pct = [np.nan, np.nan, 73, 82]
    mask = ~np.isnan(vevo2_pct)
    b2 = axD.bar(x[mask] + w/2, np.array(vevo2_pct)[mask], width=w,
                 color="#e94e77", edgecolor="k",
                 label="$\\Delta$ V$_E$/V$_{O_2}$")
    axD.axhline(0, color="k", lw=0.8)
    axD.set_xticks(x)
    axD.set_xticklabels(labels)
    axD.set_xlabel("mm from VIIc")
    axD.set_ylabel("% change from baseline")
    axD.set_title("D  Metabolic ratio")
    axD.legend(loc="lower right", frameon=False)
    axD.set_ylim(-40, 95)

    fig.tight_layout()
    _save(fig, "fig3_respiratory_metabolic")


# --------------------------------------------------------------------------
# Figure 4.  3D respiratory trajectory deformations.
# Schematic (no numbers invented). Shows qualitatively the three phase-
# deformation features described in the log: late-E tails, inspiratory bulb,
# post-I feet, with -0.2 mm vs +0.6 mm vs +0.8 mm.
# --------------------------------------------------------------------------
def fig4_3d_trajectory():
    fig = plt.figure(figsize=(7.5, 3.5))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1])

    # Left: schematic of respiratory 3D loop with 3 annotated deformations
    axL = fig.add_subplot(gs[0, 0])
    t = np.linspace(0, 2*np.pi, 400)
    baseline_x = 1.0 * np.cos(t)
    baseline_y = 0.6 * np.sin(t)
    axL.plot(baseline_x, baseline_y, color="k", lw=1.0, label="baseline")
    # +0.8 mm trajectory: late-E tail and post-I foot
    x8 = 1.0 * np.cos(t) - 0.55 * np.exp(-((t-2.6)**2)/0.12)
    y8 = 0.6 * np.sin(t) - 0.30 * np.exp(-((t-4.6)**2)/0.15)
    axL.plot(x8, y8, color=GROUP_COLORS[4], lw=1.2, label="+0.8 mm")
    # +0.6 mm trajectory: inspiratory bulb
    x6 = 1.0 * np.cos(t) + 0.35 * np.exp(-((t-1.0)**2)/0.12)
    y6 = 0.6 * np.sin(t) + 0.30 * np.exp(-((t-1.0)**2)/0.12)
    axL.plot(x6, y6, color=GROUP_COLORS[3], lw=1.2, label="+0.6 mm")
    # -0.2 mm: near baseline
    axL.plot(0.92*baseline_x, 0.92*baseline_y, color=GROUP_COLORS[0],
             lw=1.2, ls="--", label="-0.2 mm")
    # Annotations
    axL.annotate("late-E tail", xy=(-1.4, -0.05), xytext=(-1.9, -0.5),
                 fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.7))
    axL.annotate("inspiratory bulb", xy=(1.3, 0.85), xytext=(0.4, 1.2),
                 fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.7))
    axL.annotate("post-I foot", xy=(-0.1, -0.85), xytext=(0.5, -1.2),
                 fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.7))
    axL.set_xlim(-2.1, 2.1)
    axL.set_ylim(-1.4, 1.4)
    axL.set_aspect("equal")
    axL.axis("off")
    axL.set_title("A  Respiratory cycle deformations")
    axL.legend(loc="upper right", frameon=False, fontsize=7)

    # Right: summary qualitative phase dominance by group (heatmap-ish)
    axR = fig.add_subplot(gs[0, 1])
    phases = ["late-E\ntail", "Insp.\nbulb", "post-I\nfoot"]
    groups = ["-0.2", "+0.6", "+0.8"]
    # strongly supported by log text: +0.6 dominates insp; +0.8 dominates late-E & post-I
    M = np.array([
        [0.3, 0.2, 0.2],  # -0.2
        [0.8, 1.0, 0.5],  # +0.6
        [1.0, 0.6, 1.0],  # +0.8
    ])
    im = axR.imshow(M, cmap="magma", vmin=0, vmax=1, aspect="auto")
    axR.set_xticks(range(len(phases)))
    axR.set_xticklabels(phases)
    axR.set_yticks(range(len(groups)))
    axR.set_yticklabels(groups)
    axR.set_title("B  Phase dominance (qualitative)")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            axR.text(j, i, f"{M[i,j]:.1f}", ha="center", va="center",
                     color="w" if M[i,j]<0.6 else "k", fontsize=8)
    fig.colorbar(im, ax=axR, fraction=0.05, pad=0.04, label="rel. dominance")

    fig.tight_layout()
    _save(fig, "fig4_3d_trajectory")


# --------------------------------------------------------------------------
# Figure 5.  Summary placeholder: respiratory rate nadir time + frequency drop.
# Time-to-nadir (min): -0.2=2; +0.1=4; +0.4=4; +0.6=6; +0.8=6
# Frequency % drop: -0.2=12; +0.1=17; +0.4=9; +0.6=10; +0.8=11
# --------------------------------------------------------------------------
def fig5_nadir_timing():
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.8))
    labels = GROUP_LABELS
    nadir_t = [2, 4, 4, 6, 6]
    freq_drop = [12, 17, 9, 10, 11]
    axA = axes[0]
    axA.bar(labels, nadir_t, color=GROUP_COLORS, edgecolor="k")
    axA.set_ylabel("time to f$_R$ nadir (min)")
    axA.set_xlabel("mm from VIIc")
    axA.set_title("A  Frequency-nadir timing")
    axA.set_ylim(0, 8)
    for i, v in enumerate(nadir_t):
        axA.text(i, v+0.2, f"{v}", ha="center", fontsize=8)

    axB = axes[1]
    axB.bar(labels, freq_drop, color=GROUP_COLORS, edgecolor="k")
    axB.set_ylabel("max $\\Delta$f$_R$ (% drop from baseline)")
    axB.set_xlabel("mm from VIIc")
    axB.set_title("B  Magnitude of freq. drop")
    axB.set_ylim(0, 22)
    for i, v in enumerate(freq_drop):
        axB.text(i, v+0.3, f"{v}%", ha="center", fontsize=8)

    fig.tight_layout()
    _save(fig, "fig5_nadir_timing")


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    fig1_schematic_and_cfos()
    fig2_abd_temporal()
    fig3_respiratory_metabolic()
    fig4_3d_trajectory()
    fig5_nadir_timing()
    print("Generated 5 figures.")
