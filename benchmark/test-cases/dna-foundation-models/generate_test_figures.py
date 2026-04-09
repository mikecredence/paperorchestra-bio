"""Generate test figures from the DNA Foundation Models benchmark data."""
import sys
sys.path.insert(0, '.claude/skills/paper-builder/scripts')

from academic_plots import setup_academic_style, save_figure, comparison_bar_chart
import matplotlib.pyplot as plt
import numpy as np

setup_academic_style()

# --- Figure 1: Pooling Strategy Impact ---
models = ['DNABERT-2', 'NT-v2', 'HyenaDNA', 'Caduceus-Ph', 'GROVER']
improvements = [4.0, 6.8, 8.7, 5.9, 1.4]
iqr_lower = [2.0, 3.7, 4.6, 2.8, 0.7]
iqr_upper = [5.5, 9.6, 12.9, 9.1, 1.9]
errors_lower = [v - l for v, l in zip(improvements, iqr_lower)]
errors_upper = [u - v for v, u in zip(improvements, iqr_upper)]

fig, ax = plt.subplots(figsize=(7, 4))
colors = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#56B4E9']
bars = ax.bar(models, improvements, color=colors, width=0.6,
              yerr=[errors_lower, errors_upper], capsize=4,
              error_kw={'linewidth': 1.2, 'color': '#333333'})
ax.set_ylabel('AUC Improvement (%)\n(summary → mean token pooling)')
ax.set_title('Impact of Pooling Strategy on Model Performance')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_ylim(0, 15)
for bar, val in zip(bars, improvements):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
            f'+{val}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()
save_figure(fig, 'benchmark/test-cases/dna-foundation-models/fig_pooling')
print("Saved: fig_pooling.pdf / fig_pooling.png")

# --- Figure 2: Variant Effect Prediction ---
fig, ax = plt.subplots(figsize=(8, 4.5))
tasks = ['Pathogenic SNPs', 'eQTL', 'ipaQTL']
models_ve = ['NT-v2', 'Caduceus', 'Enformer', 'HyenaDNA', 'DNABERT-2', 'AlphaGenome']
data = {
    'NT-v2':      [0.732, 0.609, 0.602],
    'Caduceus':   [0.696, 0.649, 0.568],
    'Enformer':   [0.688, 0.774, 0.692],
    'HyenaDNA':   [0.612, 0.612, 0.448],
    'DNABERT-2':  [0.538, 0.570, 0.469],
    'AlphaGenome':[None,  0.803, 0.864],
}
colors_ve = ['#E69F00', '#CC79A7', '#999999', '#009E73', '#0072B2', '#D55E00']

x = np.arange(len(tasks))
width = 0.13
for i, (model, color) in enumerate(zip(models_ve, colors_ve)):
    vals = [v if v is not None else 0 for v in data[model]]
    offset = (i - len(models_ve)/2 + 0.5) * width
    bars = ax.bar(x + offset, vals, width, label=model, color=color)
    # Gray out missing values
    for j, v in enumerate(data[model]):
        if v is None:
            bars[j].set_alpha(0.15)

ax.set_ylabel('AUC')
ax.set_title('Variant Effect Prediction: Foundation vs Specialized Models')
ax.set_xticks(x)
ax.set_xticklabels(tasks)
ax.legend(loc='upper right', fontsize=7.5, ncol=2)
ax.set_ylim(0.4, 0.95)
ax.axhline(y=0.5, color='gray', linewidth=0.5, linestyle='--', alpha=0.5)
plt.tight_layout()
save_figure(fig, 'benchmark/test-cases/dna-foundation-models/fig_variant_effect')
print("Saved: fig_variant_effect.pdf / fig_variant_effect.png")

print("\nDone! Generated 2 test figures.")
