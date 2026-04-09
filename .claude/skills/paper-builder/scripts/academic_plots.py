#!/usr/bin/env python3
"""
Academic plotting utilities for paper-builder.

Provides consistent, publication-quality styling for matplotlib figures.
Import and call setup_academic_style() before creating any plots.

Usage:
    from academic_plots import setup_academic_style, COLORS, save_figure
    setup_academic_style()
    fig, ax = plt.subplots()
    # ... plot ...
    save_figure(fig, 'figures/my_plot')
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# Okabe-Ito colorblind-friendly palette
COLORS = {
    'blue':    '#0072B2',
    'orange':  '#E69F00',
    'green':   '#009E73',
    'pink':    '#CC79A7',
    'red':     '#D55E00',
    'skyblue': '#56B4E9',
    'yellow':  '#F0E442',
    'black':   '#000000',
}
COLOR_LIST = list(COLORS.values())


def setup_academic_style(font_size: int = 10, use_serif: bool = True):
    """Apply publication-quality matplotlib defaults."""
    font_family = 'serif' if use_serif else 'sans-serif'
    serif_fonts = ['Times New Roman', 'DejaVu Serif', 'Palatino', 'Georgia']
    sans_fonts = ['Helvetica', 'Arial', 'DejaVu Sans']

    matplotlib.rcParams.update({
        # Fonts
        'font.family': font_family,
        'font.serif': serif_fonts,
        'font.sans-serif': sans_fonts,
        'font.size': font_size,
        'axes.labelsize': font_size + 1,
        'axes.titlesize': font_size + 2,
        'xtick.labelsize': font_size - 1,
        'ytick.labelsize': font_size - 1,
        'legend.fontsize': font_size - 1,

        # Figure
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,

        # Axes
        'axes.grid': True,
        'grid.alpha': 0.3,
        'grid.linewidth': 0.5,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.linewidth': 0.8,

        # Ticks
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'xtick.major.width': 0.8,
        'ytick.major.width': 0.8,

        # Legend
        'legend.frameon': True,
        'legend.fancybox': False,
        'legend.edgecolor': 'black',
        'legend.framealpha': 0.9,

        # Lines
        'lines.linewidth': 1.5,
        'lines.markersize': 6,

        # Text
        'text.usetex': False,  # set True if full LaTeX is available and desired
        'mathtext.fontset': 'cm',
    })


def save_figure(fig, path_stem: str, formats=('pdf', 'png')):
    """Save figure in multiple formats for paper inclusion."""
    for fmt in formats:
        filepath = f"{path_stem}.{fmt}"
        fig.savefig(filepath, format=fmt)
        print(f"  Saved: {filepath}")
    plt.close(fig)


def comparison_bar_chart(
    methods: list[str],
    metrics: dict[str, list[float]],
    title: str = "",
    ylabel: str = "Score (%)",
    highlight_method: str | None = None,
    figsize: tuple = (7, 4),
) -> plt.Figure:
    """
    Create a grouped bar chart comparing methods across metrics.

    Args:
        methods: List of method names
        metrics: Dict mapping metric names to lists of values (one per method)
        title: Chart title
        ylabel: Y-axis label
        highlight_method: Method name to highlight (e.g., "Ours")
        figsize: Figure size

    Returns:
        matplotlib Figure
    """
    setup_academic_style()
    fig, ax = plt.subplots(figsize=figsize)

    n_methods = len(methods)
    n_metrics = len(metrics)
    x = np.arange(n_metrics)
    width = 0.8 / n_methods

    for i, method in enumerate(methods):
        values = [metrics[m][i] for m in metrics]
        offset = (i - n_methods / 2 + 0.5) * width
        color = COLOR_LIST[i % len(COLOR_LIST)]
        alpha = 1.0

        if highlight_method and method == highlight_method:
            edgecolor = 'black'
            linewidth = 1.5
        else:
            edgecolor = 'none'
            linewidth = 0

        ax.bar(x + offset, values, width * 0.9,
               label=method, color=color, alpha=alpha,
               edgecolor=edgecolor, linewidth=linewidth)

    ax.set_xlabel('')
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(list(metrics.keys()))
    ax.legend()

    plt.tight_layout()
    return fig


def line_chart(
    x_values: list,
    series: dict[str, list[float]],
    xlabel: str = "",
    ylabel: str = "",
    title: str = "",
    figsize: tuple = (6, 4),
) -> plt.Figure:
    """
    Create a line chart with multiple series.

    Args:
        x_values: X-axis values (shared across all series)
        series: Dict mapping series names to lists of y-values
        xlabel, ylabel, title: Axis labels and title
        figsize: Figure size

    Returns:
        matplotlib Figure
    """
    setup_academic_style()
    fig, ax = plt.subplots(figsize=figsize)

    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p']
    for i, (name, values) in enumerate(series.items()):
        ax.plot(x_values, values,
                color=COLOR_LIST[i % len(COLOR_LIST)],
                marker=markers[i % len(markers)],
                label=name, markeredgecolor='white', markeredgewidth=0.5)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    ax.legend()

    plt.tight_layout()
    return fig


def latex_table(
    headers: list[str],
    rows: list[list],
    caption: str = "",
    label: str = "",
    bold_best: bool = True,
    higher_better: list[bool] | None = None,
) -> str:
    """
    Generate a LaTeX table string with booktabs formatting.

    Args:
        headers: Column headers
        rows: List of rows, each a list of values
        caption: Table caption
        label: LaTeX label
        bold_best: Whether to bold the best value per column
        higher_better: List of bools indicating if higher is better per column
                       (None = all higher-is-better)

    Returns:
        LaTeX table string
    """
    n_cols = len(headers)
    if higher_better is None:
        higher_better = [True] * (n_cols - 1)  # skip first col (method name)

    # Find best values per column (skip column 0 = method names)
    best_vals = {}
    if bold_best:
        for col_idx in range(1, n_cols):
            numeric_vals = []
            for row in rows:
                try:
                    numeric_vals.append((float(row[col_idx]), row))
                except (ValueError, TypeError):
                    pass
            if numeric_vals:
                hb = higher_better[col_idx - 1] if col_idx - 1 < len(higher_better) else True
                best_val = max(numeric_vals, key=lambda x: x[0] if hb else -x[0])[0]
                best_vals[col_idx] = best_val

    # Build LaTeX
    col_spec = "l" + "c" * (n_cols - 1)
    lines = [
        r"\begin{table}[t]",
        r"\centering",
    ]
    if caption:
        lines.append(rf"\caption{{{caption}}}")
    if label:
        lines.append(rf"\label{{{label}}}")

    lines.extend([
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\toprule",
        " & ".join(headers) + r" \\",
        r"\midrule",
    ])

    for row in rows:
        cells = []
        for col_idx, val in enumerate(row):
            cell_str = str(val)
            if col_idx in best_vals:
                try:
                    if float(val) == best_vals[col_idx]:
                        cell_str = rf"\textbf{{{cell_str}}}"
                except (ValueError, TypeError):
                    pass
            cells.append(cell_str)
        lines.append(" & ".join(cells) + r" \\")

    lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    # Demo: generate sample figures
    setup_academic_style()

    # Bar chart demo
    fig = comparison_bar_chart(
        methods=["Baseline A", "Baseline B", "Ours"],
        metrics={
            "Accuracy": [78.3, 80.1, 83.7],
            "F1 Score": [65.2, 67.8, 71.4],
            "Precision": [72.1, 74.5, 78.2],
        },
        ylabel="Score (%)",
        highlight_method="Ours",
    )
    save_figure(fig, "/tmp/demo_bar")

    # Table demo
    table = latex_table(
        headers=["Method", "Acc $\\uparrow$", "F1 $\\uparrow$", "Err $\\downarrow$"],
        rows=[
            ["Baseline A", "78.3", "65.2", "12.4"],
            ["Baseline B", "80.1", "67.8", "11.2"],
            ["Ours", "83.7", "71.4", "9.8"],
        ],
        caption="Comparison on benchmark dataset.",
        label="tab:main_results",
        higher_better=[True, True, False],
    )
    print(table)
