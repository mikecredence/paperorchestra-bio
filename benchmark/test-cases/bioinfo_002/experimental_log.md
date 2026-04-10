# Experimental Log -- DREAM Challenge: Deep learning for gene regulation

## 2024-01-20 -- Training dataset overview

| Property | Value |
|----------|-------|
| Total promoter sequences | ~6.7 million |
| Sequence length | 80 bp |
| Organism | Saccharomyces cerevisiae |
| Expression measurement | FACS-based MPRA (fluorescence bins) |
| Training / validation / test split | 80% / 10% / 10% |

## 2024-03-01 -- Leaderboard: held-out random sequences (Pearson r)

Top-performing models on random held-out test set.

| Team / Model | Architecture | Pearson r | Spearman rho | Training strategy |
|-------------|-------------|----------|-------------|------------------|
| Team A | CNN + attention | 0.956 | 0.948 | Data augmentation (RC) |
| Team B | Transformer | 0.953 | 0.945 | Curriculum learning |
| Team C | Hybrid CNN-Transformer | 0.951 | 0.943 | Multi-task + augmentation |
| Team D | Deep CNN | 0.948 | 0.940 | Standard |
| Team E | ResNet-style | 0.944 | 0.936 | Mixup augmentation |
| Baseline (linear) | Ridge regression on k-mers | 0.820 | 0.805 | -- |

All top models use neural networks; performance is closely clustered among top 5.

## 2024-03-15 -- Benchmark: natural yeast promoters

| Team / Model | Pearson r | Delta from random test |
|-------------|----------|----------------------|
| Team A | 0.88 | -0.076 |
| Team B | 0.91 | -0.043 |
| Team C | 0.90 | -0.051 |
| Team D | 0.85 | -0.098 |
| Team E | 0.84 | -0.104 |

Models trained on random sequences show varying generalization to natural promoters; Team B (Transformer) generalizes best.

## 2024-03-28 -- Benchmark: motif insertion sensitivity

Correlation between predicted and measured expression changes upon known motif insertion.

| Team / Model | Motif sensitivity (Pearson r) | TATA-box response | GCN4 motif response |
|-------------|------------------------------|------------------|---------------------|
| Team A | 0.82 | 0.88 | 0.76 |
| Team B | 0.85 | 0.90 | 0.80 |
| Team C | 0.83 | 0.89 | 0.78 |
| Team D | 0.78 | 0.84 | 0.72 |
| Team E | 0.76 | 0.82 | 0.70 |

Transformer-based models capture motif-level regulatory grammar best.

## 2024-04-10 -- Architecture ablation (organizer analysis)

Impact of key architectural choices (averaged across re-trained variants).

| Component | Present | Absent | Delta Pearson r |
|-----------|---------|--------|----------------|
| Reverse-complement augmentation | 0.954 | 0.941 | +0.013 |
| Attention layers | 0.952 | 0.938 | +0.014 |
| Residual connections | 0.949 | 0.935 | +0.014 |
| Curriculum learning | 0.951 | 0.944 | +0.007 |
| Larger model (>5M params) | 0.953 | 0.946 | +0.007 |

Attention and RC augmentation provide the largest individual gains.

## 2024-04-20 -- Expression-matched pair discrimination

Accuracy at distinguishing sequences with similar expression levels.

| Team / Model | Pair discrimination accuracy (%) |
|-------------|--------------------------------|
| Team A | 72.5 |
| Team B | 74.8 |
| Team C | 73.1 |
| Team D | 68.2 |
| Baseline | 55.3 |

This benchmark differentiates models the most -- substantial spread among top performers.
