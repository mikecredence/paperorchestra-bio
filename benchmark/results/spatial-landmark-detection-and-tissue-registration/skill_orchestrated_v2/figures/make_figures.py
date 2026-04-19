"""Schematic figure generation for the ELD manuscript.

No numerical values are plotted from synthetic data; all figures are schematic
diagrams describing pipelines that are explicitly laid out in the experimental
log. The one piece of quantitative text that appears (drop-out probability of
10%) is taken verbatim from the extracted statistical report.
"""

from __future__ import annotations

import os

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 10,
        "axes.titlesize": 11,
        "legend.fontsize": 9,
        "savefig.dpi": 200,
    }
)

PALETTE = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "accent": "#2ca02c",
    "warn": "#d62728",
    "deep": "#9467bd",
    "grey": "#6c6c6c",
    "bg": "#f3f5f8",
}

HERE = os.path.dirname(os.path.abspath(__file__))


def _box(ax, xy, width, height, text, facecolor=PALETTE["bg"], edgecolor=PALETTE["primary"], text_color="black", fontsize=9):
    x, y = xy
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=1.2,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=text_color,
        wrap=True,
    )


def _arrow(ax, start, end, color=PALETTE["grey"], style="->", lw=1.4):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle=style,
        color=color,
        lw=lw,
        mutation_scale=14,
    )
    ax.add_patch(arrow)


def _save(fig, stem):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(HERE, f"{stem}.{ext}"))
    plt.close(fig)


def fig_pipeline():
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    _box(ax, (0.1, 1.4), 1.6, 1.2, "Sections A, B\n(H&E / Visium / ISS / MSI)", facecolor="#eaf2fb")
    _box(ax, (2.1, 2.1), 1.7, 0.9, "Hourglass\nlandmark detector", facecolor="#fff4ea", edgecolor=PALETTE["secondary"])
    _box(ax, (2.1, 0.6), 1.7, 0.9, "Manual\nannotation (opt.)", facecolor="#eaf7ea", edgecolor=PALETTE["accent"])
    _box(ax, (4.2, 1.4), 1.8, 1.2, "TPS / Homography\nregistration", facecolor="#f5ecfa", edgecolor=PALETTE["deep"])
    _box(ax, (6.3, 1.4), 1.7, 1.2, "Registered pair\n(B -> A)", facecolor=PALETTE["bg"])
    _box(ax, (8.2, 1.4), 1.7, 1.2, "Common\nCoordinate\nFramework", facecolor="#fdecec", edgecolor=PALETTE["warn"])

    _arrow(ax, (1.7, 2.4), (2.1, 2.55))
    _arrow(ax, (1.7, 1.6), (2.1, 1.05))
    _arrow(ax, (3.8, 2.55), (4.2, 2.2))
    _arrow(ax, (3.8, 1.05), (4.2, 1.8))
    _arrow(ax, (6.0, 2.0), (6.3, 2.0))
    _arrow(ax, (8.0, 2.0), (8.2, 2.0))

    ax.set_title("ELD end-to-end workflow: detector, TPS registration, common coordinate framework", fontsize=11)
    fig.tight_layout()
    _save(fig, "fig_pipeline")


def fig_errors():
    fig, ax = plt.subplots(figsize=(7.0, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    _box(ax, (0.1, 1.4), 1.7, 1.2, "Input image I", facecolor="#eaf2fb")
    _box(ax, (2.0, 2.3), 1.6, 0.9, "Detector f", facecolor="#fff4ea", edgecolor=PALETTE["secondary"])
    _box(ax, (2.0, 0.7), 1.6, 0.9, "Affine warp T", facecolor="#eaf7ea", edgecolor=PALETTE["accent"])
    _box(ax, (4.0, 2.3), 1.8, 0.9, "Landmarks p", facecolor="#f5ecfa", edgecolor=PALETTE["deep"])
    _box(ax, (4.0, 0.7), 1.8, 0.9, "Landmarks on\nwarped image", facecolor="#fdecec", edgecolor=PALETTE["warn"])

    _arrow(ax, (1.8, 2.0), (2.0, 2.6))
    _arrow(ax, (1.8, 2.0), (2.0, 1.2))
    _arrow(ax, (3.6, 2.6), (4.0, 2.6))
    _arrow(ax, (3.6, 1.2), (4.0, 1.2))
    _arrow(ax, (4.9, 2.3), (4.9, 1.6), style="<->", color=PALETTE["grey"], lw=1.4)

    ax.text(
        7.2,
        3.2,
        "Consistency error:\ncompare f(I) and f(T(I))",
        ha="left",
        va="top",
        fontsize=9,
        color=PALETTE["primary"],
    )
    ax.text(
        7.2,
        2.1,
        "Forward error:\nregress annotated points\nfrom detected landmarks",
        ha="left",
        va="top",
        fontsize=9,
        color=PALETTE["secondary"],
    )
    ax.text(
        7.2,
        0.9,
        "Backward error:\nregress detected landmarks\nfrom annotated points",
        ha="left",
        va="top",
        fontsize=9,
        color=PALETTE["warn"],
    )

    ax.set_title("Three landmark-detector error metrics evaluated on MAFL and AFLW", fontsize=11)
    fig.tight_layout()
    _save(fig, "fig_errors")


def fig_3d_workflow():
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    _box(ax, (0.1, 1.8), 2.0, 1.2, "Reference slice R\n(from z-stack)", facecolor="#eaf2fb")
    _box(ax, (0.1, 0.2), 2.0, 1.2, "Source S +\nnoisy counterpart S'", facecolor="#eaf7ea", edgecolor=PALETTE["accent"])

    _box(ax, (2.6, 1.5), 1.8, 1.8, "Anchor detector\n(shared weights)", facecolor="#fff4ea", edgecolor=PALETTE["secondary"])

    _box(ax, (4.9, 2.1), 1.9, 1.0, "TPS(S -> R)\nrigid(S -> R)", facecolor="#f5ecfa", edgecolor=PALETTE["deep"])
    _box(ax, (4.9, 0.7), 1.9, 1.0, "TPS(S' -> R)", facecolor="#fdecec", edgecolor=PALETTE["warn"])

    _box(ax, (7.3, 1.5), 2.5, 1.6, "Similarity + area-change\nloss -> anchors stable\n(20 landmarks)", facecolor=PALETTE["bg"])

    _arrow(ax, (2.1, 2.4), (2.6, 2.4))
    _arrow(ax, (2.1, 0.8), (2.6, 1.7))
    _arrow(ax, (4.4, 2.6), (4.9, 2.6))
    _arrow(ax, (4.4, 1.8), (4.9, 1.2))
    _arrow(ax, (6.8, 2.6), (7.3, 2.4))
    _arrow(ax, (6.8, 1.2), (7.3, 2.0))

    ax.set_title("ELD z-stack adaptation: anchor points constrained by area change", fontsize=11)
    fig.tight_layout()
    _save(fig, "fig_3d_workflow")


def fig_multimodal_workflow():
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    _box(ax, (0.1, 2.2), 1.9, 1.2, "Modality A\n(e.g. H&E)", facecolor="#eaf2fb")
    _box(ax, (0.1, 0.4), 1.9, 1.2, "Modality B\n(e.g. Visium / MSI)", facecolor="#eaf7ea", edgecolor=PALETTE["accent"])

    _box(ax, (2.4, 2.2), 1.8, 1.2, "Detector A\n+ latent $z_A$", facecolor="#fff4ea", edgecolor=PALETTE["secondary"])
    _box(ax, (2.4, 0.4), 1.8, 1.2, "Detector B\n+ latent $z_B$", facecolor="#fff4ea", edgecolor=PALETTE["secondary"])

    _box(ax, (4.7, 1.3), 2.0, 1.4, "Cross-modality TPS\nregistration", facecolor="#f5ecfa", edgecolor=PALETTE["deep"])

    _box(ax, (7.1, 1.3), 2.7, 1.4, "Optimise latent similarity\nbetween $z_A$ and $z_B$\n(16 landmarks)", facecolor=PALETTE["bg"])

    _arrow(ax, (2.0, 2.8), (2.4, 2.8))
    _arrow(ax, (2.0, 1.0), (2.4, 1.0))
    _arrow(ax, (4.2, 2.6), (4.7, 2.2))
    _arrow(ax, (4.2, 1.2), (4.7, 1.7))
    _arrow(ax, (6.7, 2.0), (7.1, 2.0))

    ax.set_title("Cross-modality ELD: per-modality detectors with latent-space alignment", fontsize=11)
    fig.tight_layout()
    _save(fig, "fig_multimodal_workflow")


def main():
    fig_pipeline()
    fig_errors()
    fig_3d_workflow()
    fig_multimodal_workflow()


if __name__ == "__main__":
    main()
