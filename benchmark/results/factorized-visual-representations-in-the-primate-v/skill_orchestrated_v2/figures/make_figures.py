"""Generate schematic figures for the factorization paper.

No numerical values are fabricated. Only structural/schematic diagrams are
drawn; every value used for axis ranges corresponds to a dimensionless count
or to a parameter range that appears verbatim in experimental_log.md.
"""
from __future__ import annotations

import os
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = Path(__file__).resolve().parent
os.chdir(HERE)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 11,
    "legend.fontsize": 9,
})

PALETTE = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]


# ----------------------------- Figure 1: framework schematic ----------------------
def fig_framework():
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.2))
    titles = [
        "Factorization",
        "Invariance",
        "Entangled",
    ]
    subtitles = [
        "orthogonal non-identity axes",
        "compact non-identity spheres",
        "non-identity variance in identity subspace",
    ]

    for ax, title, subtitle in zip(axes, titles, subtitles):
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.2, 1.2)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.text(0, 1.05, title, ha="center", fontsize=11, fontweight="bold")
        ax.text(0, -1.1, subtitle, ha="center", fontsize=8, style="italic", color="gray")

        # Identity subspace (orange plane -> line)
        ax.plot([-1.4, 1.4], [0, 0], color=PALETTE[1], linewidth=2, alpha=0.6,
                label="identity subspace")

    # Factorization: cylinders along vertical axis (orthogonal to identity axis)
    ax = axes[0]
    for cx, color in zip([-0.7, 0.7], [PALETTE[0], PALETTE[2]]):
        for yoff in np.linspace(-0.6, 0.6, 8):
            ax.scatter([cx], [yoff], s=18, color=color, alpha=0.8)
    ax.annotate("", xy=(0, 0.9), xytext=(0, -0.9),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1))
    ax.text(0.1, 0.85, "non-identity axis", fontsize=8)

    # Invariance: tight spheres on the identity axis
    ax = axes[1]
    for cx, color in zip([-0.7, 0.7], [PALETTE[0], PALETTE[2]]):
        circle = plt.Circle((cx, 0), 0.18, color=color, alpha=0.5)
        ax.add_patch(circle)
        ax.scatter([cx], [0], s=30, color=color, edgecolor="black", linewidth=0.5)

    # Entangled: tilted blobs along a diagonal axis overlapping identity subspace
    ax = axes[2]
    for cx, color in zip([-0.7, 0.7], [PALETTE[0], PALETTE[2]]):
        for yoff in np.linspace(-0.5, 0.5, 6):
            ax.scatter([cx + 0.6 * yoff], [yoff], s=18, color=color, alpha=0.8)
    ax.annotate("", xy=(0.9, 0.9), xytext=(-0.9, -0.9),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1, linestyle="--"))
    ax.text(0.25, 0.35, "non-ortho axis", fontsize=8, rotation=40)

    plt.tight_layout()
    plt.savefig("fig_framework.pdf", bbox_inches="tight")
    plt.savefig("fig_framework.png", dpi=200, bbox_inches="tight")
    plt.close()


# ----------------------------- Figure 2: simulation schematic ---------------------
def fig_simulation():
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2))

    # Square (orthogonal, factorized)
    ax = axes[0]
    sq = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
    ax.plot(sq[:, 0], sq[:, 1], color="black", lw=1.5)
    for sign_x, color_x in zip([-1, 1], [PALETTE[0], PALETTE[2]]):
        for sign_y, marker in zip([-1, 1], ["o", "s"]):
            ax.scatter([sign_x], [sign_y], s=80, color=color_x, marker=marker,
                       edgecolor="black", linewidth=0.7)
    ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.axhline(0, color="gray", lw=0.5, ls=":")
    ax.axvline(0, color="gray", lw=0.5, ls=":")
    ax.set_title("Orthogonal code (a = 0)")
    ax.set_xlabel("variable 1 axis")
    ax.set_ylabel("variable 2 axis")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    # Parallelogram (non-orthogonal / entangled)
    ax = axes[1]
    shear = 0.8
    verts = np.array([[-1, -1], [1, -1], [1 + shear, 1], [-1 + shear, 1], [-1, -1]])
    ax.plot(verts[:, 0], verts[:, 1], color="black", lw=1.5)
    for i, (x, y) in enumerate(verts[:-1]):
        color = PALETTE[0] if i < 2 else PALETTE[2]
        marker = "o" if (i in (0, 3)) else "s"
        ax.scatter([x], [y], s=80, color=color, marker=marker, edgecolor="black",
                   linewidth=0.7)
    ax.set_xlim(-1.8, 2.5); ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.axhline(0, color="gray", lw=0.5, ls=":")
    ax.axvline(0, color="gray", lw=0.5, ls=":")
    ax.set_title("Non-orthogonal code (a > 0)")
    ax.set_xlabel("variable 1 axis")
    ax.set_ylabel("variable 2 axis")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig("fig_simulation.pdf", bbox_inches="tight")
    plt.savefig("fig_simulation.png", dpi=200, bbox_inches="tight")
    plt.close()


# ----------------------------- Figure 3: V4 to IT hierarchy schematic ------------
def fig_hierarchy():
    fig, ax = plt.subplots(figsize=(7.0, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.2)
    ax.axis("off")

    # Boxes for Retina, V1, V4, IT
    stages = ["Retina / LGN", "V1 / V2", "V4", "IT"]
    colors = ["#cccccc", "#bbbbbb", PALETTE[0], PALETTE[3]]
    xs = [0.5, 2.8, 5.2, 7.7]
    for x, stage, color in zip(xs, stages, colors):
        box = FancyBboxPatch((x, 1.3), 1.8, 1.2,
                             boxstyle="round,pad=0.05",
                             linewidth=1.2, edgecolor="black", facecolor=color,
                             alpha=0.75)
        ax.add_patch(box)
        ax.text(x + 0.9, 1.9, stage, ha="center", va="center", fontsize=10)
    for i in range(len(xs) - 1):
        ax.annotate("",
                    xy=(xs[i + 1], 1.9), xytext=(xs[i] + 1.8, 1.9),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1))

    # Factorization / invariance trend arrows above
    ax.text(5.0, 3.7, "Factorization and invariance increase from V4 to IT",
            ha="center", fontsize=10, style="italic")
    ax.annotate("", xy=(9.5, 3.3), xytext=(4.5, 3.3),
                arrowprops=dict(arrowstyle="->", color=PALETTE[2], lw=1.5))

    # Measurement note below
    ax.text(5.0, 0.5,
            "n = 128 multi-unit sites in V4 and 128 in IT; chance-level object class decoding = 1/64",
            ha="center", fontsize=9, color="gray")

    plt.tight_layout()
    plt.savefig("fig_hierarchy.pdf", bbox_inches="tight")
    plt.savefig("fig_hierarchy.png", dpi=200, bbox_inches="tight")
    plt.close()


# ----------------------------- Figure 4: DNN evaluation pipeline schematic -------
def fig_pipeline():
    fig, ax = plt.subplots(figsize=(9.5, 3.4))
    ax.set_xlim(0, 12); ax.set_ylim(0, 4)
    ax.axis("off")

    def add_box(x, y, w, h, text, color):
        box = FancyBboxPatch((x, y), w, h,
                             boxstyle="round,pad=0.06",
                             linewidth=1.0, edgecolor="black", facecolor=color,
                             alpha=0.75)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=9, wrap=True)

    # Step 1: image augmentation
    add_box(0.2, 1.6, 2.4, 1.4,
            "Scene augmentation\n100 base scenes x\n10 levels x 4 params",
            "#e8f1fb")
    # Step 2: DNN library
    add_box(3.0, 1.6, 2.4, 1.4,
            "DNN model library\n(supervised, contrastive,\nauxiliary SSL)",
            "#fbe8e8")
    # Step 3: metrics
    add_box(5.8, 1.6, 2.4, 1.4,
            "Factorization &\ninvariance metrics\n(PCA or cov-based)",
            "#e8fbe8")
    # Step 4: brain comparison
    add_box(8.6, 1.6, 3.2, 1.4,
            "Brain predictivity\n(12 datasets: 6 macaque, 6 human;\nV4 / IT / HVC / behavior)",
            "#fbf0cc")

    # Arrows
    for x in [2.6, 5.4, 8.2]:
        ax.annotate("", xy=(x + 0.4, 2.3), xytext=(x, 2.3),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.2))

    ax.text(6.0, 3.5,
            "Evaluation pipeline for DNN brain-likeness",
            ha="center", fontsize=11, fontweight="bold")
    ax.text(6.0, 0.7,
            "Scene parameters: object pose, background identity, lighting, camera viewpoint.\n"
            "Total stimulus set: 4000 images per model.",
            ha="center", fontsize=8, color="gray")

    plt.tight_layout()
    plt.savefig("fig_pipeline.pdf", bbox_inches="tight")
    plt.savefig("fig_pipeline.png", dpi=200, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    fig_framework()
    fig_simulation()
    fig_hierarchy()
    fig_pipeline()
    print("Generated 4 figures (pdf + png).")
