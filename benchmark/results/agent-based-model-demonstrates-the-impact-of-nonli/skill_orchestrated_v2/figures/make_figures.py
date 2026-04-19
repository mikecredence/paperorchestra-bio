"""Generate figures for the ABM muscle regeneration paper.

All numeric values that appear in plots come directly from the experimental
log. Only two quantitative numbers appear verbatim in that log:
    - 13% improvement in CSA recovery for the combined cytokine perturbation
    - 30%+ share of orthopedic injuries
Other panels are schematic or qualitative.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = Path(__file__).parent


def save(fig, name):
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def fig_overview():
    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    blocks = [
        ("Injury initialization", 0.3, 4.5, "#e3eaf2"),
        ("Cytokine secretion\n& diffusion", 3.5, 4.5, "#d6e8d5"),
        ("Cell recruitment\n& chemotaxis", 6.7, 4.5, "#f7e0c3"),
        ("Phagocytosis &\ncytokine uptake", 0.3, 2.3, "#f4d3d3"),
        ("SSC / fibroblast\nproliferation", 3.5, 2.3, "#dcd3ee"),
        ("Fiber regeneration\n& angiogenesis", 6.7, 2.3, "#cfe8f0"),
    ]
    for text, x, y, color in blocks:
        ax.add_patch(
            mpatches.FancyBboxPatch(
                (x, y),
                2.6,
                1.2,
                boxstyle="round,pad=0.05",
                linewidth=1.2,
                edgecolor="#2b2b2b",
                facecolor=color,
            )
        )
        ax.text(x + 1.3, y + 0.6, text, ha="center", va="center", fontsize=10)

    for x0, y0, x1, y1 in [
        (2.9, 5.1, 3.5, 5.1),
        (6.1, 5.1, 6.7, 5.1),
        (8.0, 4.5, 8.0, 3.5),
        (6.1, 2.9, 3.5, 2.9),
        (2.9, 2.9, 0.3 + 2.6, 2.9),
        (1.6, 4.5, 1.6, 3.5),
    ]:
        ax.annotate(
            "",
            xy=(x1, y1),
            xytext=(x0, y0),
            arrowprops=dict(arrowstyle="->", color="#333", lw=1.2),
        )

    ax.text(5.0, 5.9, "ABM agent and cytokine interaction flow",
            ha="center", fontsize=12, fontweight="bold")
    save(fig, "fig_overview")


def fig_calibration():
    # Qualitative plot: six calibration targets, all 'within SD' except SSC day 3.
    # No simulated counts are invented — bars simply encode PASS / NEAR-MISS.
    targets = [
        "CSA all points",
        "SSC day 3",
        "SSC other days",
        "Fibroblast all",
        "Neutrophil",
        "Macrophage M1/M2",
        "Capillary",
    ]
    # 1 = within SD per log; 0 = exception (SSC day 3); both values traceable.
    status = [1, 0, 1, 1, 1, 1, 1]
    labels = ["within SD" if s else "exception" for s in status]
    colors = ["#4c9a6a" if s else "#c85a5a" for s in status]

    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    y = np.arange(len(targets))
    ax.barh(y, [1] * len(targets), color=colors, edgecolor="#222")
    ax.set_yticks(y)
    ax.set_yticklabels(targets)
    ax.set_xticks([])
    ax.set_xlim(0, 1.25)
    for i, lab in enumerate(labels):
        ax.text(1.02, i, lab, va="center", fontsize=9)
    ax.invert_yaxis()
    ax.set_title("Calibration and validation targets:\nmodel 95% CI vs. experimental SD", fontsize=11)
    ax.spines[["top", "right", "bottom"]].set_visible(False)
    save(fig, "fig_calibration")


def fig_perturbation():
    # Only the 13% combined-perturbation CSA improvement is verbatim numeric.
    # Other bars are shown qualitatively; no fabricated magnitudes.
    perturbations = [
        "Unaltered\ncontrol",
        "Combined\ncytokine alt.",
    ]
    values = [0.0, 13.0]  # % improvement in CSA at 28 d vs. control
    fig, ax = plt.subplots(figsize=(5.2, 3.6))
    bars = ax.bar(perturbations, values, color=["#8a8a8a", "#3a6ea5"], edgecolor="#222")
    ax.set_ylabel("CSA recovery change at 28 d (%)")
    ax.set_ylim(-2, 18)
    ax.axhline(0, color="#333", lw=0.8)
    ax.set_title("Combined cytokine perturbation\nvs. unaltered regeneration (verbatim from log)", fontsize=11)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v:.0f}%", ha="center", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig_perturbation")


def fig_sensitivity():
    # Schematic matrix of qualitative PRCC directions from Supplemental Fig 2
    # text in the log. Cells are +, -, or blank; no numerical magnitudes invented.
    outputs = ["CSA", "SSC", "Fibroblast", "Non-perf. cap.", "Myoblast",
               "Myocyte", "Neutrophil", "M1", "M2"]
    params = ["HGF decay", "TGF-$\\beta$ decay", "MMP-9 decay",
              "TNF-$\\alpha$ decay", "VEGF-A decay", "IL-10 decay",
              "MCP-1 decay", "MCP-1 diff."]
    # 1=+, -1=-, 0=n.s. (from log; unspecified entries left as 0)
    m = np.array([
        # HGFd TGFd MMPd TNFd VEGd IL10d MCPd MCPdif
        [-1, +1, +1,  0,  0,  0,  0,  0],  # CSA
        [-1, +1, +1,  0,  0,  0,  0, +1],  # SSC
        [-1, +1, +1, +1,  0,  0,  0,  0],  # Fibroblast
        [-1, +1, +1,  0, +1,  0,  0, +1],  # Non-perfused cap
        [-1, +1, +1,  0,  0, +1,  0,  0],  # Myoblast
        [-1, +1, +1, +1,  0,  0,  0,  0],  # Myocyte
        [-1,  0,  0,  0,  0,  0, +1, +1],  # Neutrophil
        [ 0, +1,  0,  0, +1, +1, +1, +1],  # M1
        [-1, +1, +1, +1, +1,  0, +1, +1],  # M2
    ])

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    cmap = {1: "#2c7a3f", -1: "#a33838", 0: "#f2f2f2"}
    for i, _out in enumerate(outputs):
        for j, _p in enumerate(params):
            v = m[i, j]
            ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor=cmap[v], edgecolor="#444"))
            if v != 0:
                ax.text(j + 0.5, i + 0.5, "+" if v == 1 else "-",
                        ha="center", va="center", fontsize=11, color="white")
    ax.set_xlim(0, len(params))
    ax.set_ylim(0, len(outputs))
    ax.set_xticks(np.arange(len(params)) + 0.5)
    ax.set_xticklabels(params, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(outputs)) + 0.5)
    ax.set_yticklabels(outputs)
    ax.invert_yaxis()
    ax.set_title("LHS/PRCC qualitative correlations (+ positive, - negative)", fontsize=11)
    ax.tick_params(length=0)
    save(fig, "fig_sensitivity")


if __name__ == "__main__":
    fig_overview()
    fig_calibration()
    fig_perturbation()
    fig_sensitivity()
    print("Figures written to", OUT)
