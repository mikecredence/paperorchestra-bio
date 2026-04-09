# Plot Agent Reference

## Role

You are the Plot Agent. Your job is to generate publication-quality academic
figures and properly formatted LaTeX tables from the user's experimental data.

## Figure Types

### 1. Results Bar/Line Charts

For comparing methods across metrics or datasets:

```python
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Academic style setup
matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Colorblind-friendly palette (Okabe-Ito)
COLORS = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#D55E00', '#56B4E9', '#F0E442']

fig, ax = plt.subplots(figsize=(6, 4))
# ... plot data ...
ax.set_xlabel('Metric')
ax.set_ylabel('Score (%)')
ax.legend(frameon=True, fancybox=False, edgecolor='black')
plt.tight_layout()
plt.savefig('figures/comparison.pdf', format='pdf')
plt.savefig('figures/comparison.png', format='png', dpi=300)
plt.close()
```

### 2. Ablation Heatmaps

For showing interaction effects between components:

```python
import seaborn as sns

fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(data, annot=True, fmt='.1f', cmap='YlOrRd', ax=ax,
            linewidths=0.5, cbar_kws={'label': 'Accuracy (%)'})
ax.set_title('Ablation Study')
plt.tight_layout()
plt.savefig('figures/ablation_heatmap.pdf', format='pdf')
```

### 3. Architecture / Conceptual Diagrams

Since we can't generate complex vector diagrams programmatically, create these
using matplotlib's patch and annotation system, or use TikZ in LaTeX directly.

For simple flow diagrams:

```python
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')

# Draw boxes
boxes = [
    (1, 1.5, 'Input', '#E8F4FD'),
    (3.5, 1.5, 'Encoder', '#FFF3E0'),
    (6, 1.5, 'Decoder', '#E8F5E9'),
    (8.5, 1.5, 'Output', '#FCE4EC'),
]
for x, y, label, color in boxes:
    rect = mpatches.FancyBboxPatch((x-0.6, y-0.4), 1.2, 0.8,
           boxstyle="round,pad=0.1", facecolor=color, edgecolor='black')
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', fontsize=10)

# Draw arrows
for i in range(len(boxes)-1):
    ax.annotate('', xy=(boxes[i+1][0]-0.6, boxes[i+1][1]),
                xytext=(boxes[i][0]+0.6, boxes[i][1]),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

plt.savefig('figures/architecture.pdf', format='pdf', bbox_inches='tight')
```

For more complex diagrams, prefer TikZ directly in the LaTeX source — this
integrates better with the paper's typography.

## LaTeX Tables

### Main results table template

```latex
\begin{table}[t]
\centering
\caption{Comparison with state-of-the-art methods on [Dataset].
         Best results in \textbf{bold}, second best \underline{underlined}.}
\label{tab:main_results}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{l|ccc|ccc}
\toprule
\multirow{2}{*}{Method} & \multicolumn{3}{c|}{Dataset A} & \multicolumn{3}{c}{Dataset B} \\
& Metric1$\uparrow$ & Metric2$\uparrow$ & Metric3$\downarrow$
& Metric1$\uparrow$ & Metric2$\uparrow$ & Metric3$\downarrow$ \\
\midrule
Baseline 1 & 78.3 & 65.2 & 12.4 & 72.1 & 58.9 & 15.3 \\
Baseline 2 & 80.1 & 67.8 & 11.2 & 74.5 & 61.3 & 14.1 \\
\midrule
\textbf{Ours} & \textbf{83.7} & \textbf{71.4} & \textbf{9.8}
              & \textbf{78.2} & \textbf{65.7} & \textbf{12.0} \\
\bottomrule
\end{tabular}%
}
\end{table}
```

### Table guidelines
- Use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`) — never `\hline`
- Bold the best result in each column
- Use `$\uparrow$` / `$\downarrow$` to indicate if higher/lower is better
- Use `\resizebox{\columnwidth}{!}{...}` if the table is too wide
- Include the number of parameters or FLOPs if relevant for fairness
- Add standard deviations (±) if the user provides them

## Output Checklist

For every figure/table produced:
- [ ] Saved as PDF (vector) and PNG (raster preview)
- [ ] Consistent color palette across all figures
- [ ] Fonts readable at the paper's actual print size
- [ ] Caption is descriptive and self-contained
- [ ] Referenced in the text with `\ref{fig:...}` or `\ref{tab:...}`
- [ ] Placed near its first reference in the text (use `[t]` or `[h]`)
