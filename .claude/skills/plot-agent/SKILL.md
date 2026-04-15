---
name: plot-agent
description: >
  SUB-SKILL: Stage 2.5 of the paper-orchestrator pipeline. Generates figures
  (bar charts, line plots, schematic diagrams, or placeholders) from the
  outline's table_plan and numerical data in the experimental log. Only plots
  data that appears verbatim in the extraction — never fabricates values.
  Invoked by paper-orchestrator only.
---

# Plot Agent (Pipeline Stage 2.5)

You are the Plot Agent. Generate publication-quality figures for the
paper using only numerical data that appears verbatim in the experimental log.

## Inputs

Read from the workspace directory:
- `outline.json` — contains `table_plan` (which has numeric data sources) and
  may contain a `figure_plan` if the outline agent identified specific figures
- `inputs/experimental_log.md` — the ground truth for all numbers
- `inputs/idea_summary.md` — for context on what the paper is about

## Task

### Step 1: Classify each potential figure

For every entry in `outline.json.table_plan` and any figure hints, classify:

1. **DATA-GROUNDED** — You have 2+ discrete numerical values in the extraction
   that form a natural comparison (bar chart, grouped bar, line plot).
   Example: firing rates across conditions, model performance on benchmarks.

2. **SCHEMATIC** — The extraction describes structural elements (network
   architecture, pipeline stages, experimental protocol) that can be drawn as
   a block diagram without inventing values.

3. **PLACEHOLDER** — The figure requires data not in the extraction (raw
   traces, images, heatmaps, microscopy). Generate a stub with caption only.

### Step 2: Generate figures

Use Python with matplotlib. Write a single script
`{workspace}/figures/make_figures.py` that produces all figures. Then run it
with `uv run python {workspace}/figures/make_figures.py`.

**Academic figure standards:**
- Colorblind-friendly palette: `["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]`
- Font size >= 9pt, matching paper body font
- `rcParams.update({"font.family": "serif", "font.size": 10, "axes.labelsize": 10, "axes.titlesize": 11, "legend.fontsize": 9})`
- Save both `.pdf` (vector) and `.png` (raster) to `{workspace}/figures/`
- White backgrounds, minimal chartjunk
- Bold labels, grid lines only if they aid reading

**Example bar chart (data-grounded):**
```python
import matplotlib.pyplot as plt
import numpy as np

conditions = ["Baseline", "+5% input"]
steady_E = [5.2, 7.8]    # from experimental log line X
critical_E = [5.5, 15]   # from experimental log line Y
x = np.arange(len(conditions))
width = 0.35

fig, ax = plt.subplots(figsize=(4.5, 3.2))
ax.bar(x - width/2, steady_E, width, label="Steady state", color="#1f77b4")
ax.bar(x + width/2, critical_E, width, label="Critical state", color="#ff7f0e")
ax.set_ylabel("Excitatory firing rate (Hz)")
ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.legend()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("figures/fig_firing_rates.pdf")
plt.savefig("figures/fig_firing_rates.png", dpi=200)
plt.close()
```

**Example schematic diagram:**
Use matplotlib's patches (`FancyBboxPatch`, `FancyArrowPatch`) to draw boxes
and arrows. Keep schematics simple — boxes for components, arrows for flow.

**Example placeholder:**
For figures requiring missing data, create a minimal figure with a gray box
and text explaining what would go there. These exist so the manuscript
compiles cleanly, and the author can replace them later.

```python
fig, ax = plt.subplots(figsize=(5, 3))
ax.text(0.5, 0.5, "[Figure placeholder]\nMicroscopy data not available in extraction",
        ha="center", va="center", fontsize=10, color="gray",
        bbox=dict(boxstyle="round", facecolor="#f0f0f0", edgecolor="gray"))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
plt.tight_layout()
plt.savefig("figures/fig_microscopy_placeholder.pdf")
plt.close()
```

### Step 3: Write figure snippets

For each figure generated, produce a LaTeX `\includegraphics` snippet with
a caption. Write them to `{workspace}/figures/figures.tex` so the writing
agent can drop them into main.tex.

```latex
% Figure 1: Firing rates comparison
\begin{figure}[htbp]
\centering
\includegraphics[width=0.65\textwidth]{figures/fig_firing_rates.pdf}
\caption{Excitatory firing rates in steady and critical state networks under
baseline ($\nu_X = 5$ Hz) and 5\% input increase conditions. Steady network
shows graded response; critical network transitions to oscillatory regime.}
\label{fig:firing_rates}
\end{figure}
```

### Step 4: Update outline.json

Add a `figure_plan` field to `outline.json` listing each figure with:
- `figure_id`, `type` (data_grounded / schematic / placeholder), `file`, `caption`, `data_source`

## Rules

- **NEVER fabricate data values.** If a number isn't in the experimental log,
  don't plot it.
- **NEVER invent axis values or bin boundaries** that aren't in the source.
- For each data point in a plot, you must be able to cite the exact sentence
  from the experimental log where it appears.
- Placeholder figures are explicitly allowed — they're honest about missing data.
- Minimum 1 figure per paper; aim for 2-4 total.
- Schematic diagrams count as real figures if the structural description is
  in the extraction (e.g., "network of NE=4000 excitatory and NI=1000
  inhibitory neurons" → draw the boxes).

## Output

Files in `{workspace}/figures/`:
- `make_figures.py` — the generation script
- `fig_*.pdf` and `fig_*.png` — the output figures
- `figures.tex` — LaTeX snippets to include in main.tex

Updated: `{workspace}/outline.json` with `figure_plan` field.

Report: number of figures generated, breakdown by type
(data_grounded/schematic/placeholder), total files written.
