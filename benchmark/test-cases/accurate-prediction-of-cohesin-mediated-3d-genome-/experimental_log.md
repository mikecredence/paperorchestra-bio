# Experimental Log -- ChIPr: 3D genome prediction from 2D features

## 2024-01-10 -- Model architecture comparison (GM12878 cell line)

Pearson correlation between predicted and observed cohesin ChIA-PET interaction strength.

| Model | Pearson r | Spearman rho | RMSE |
|-------|----------|-------------|------|
| Deep Neural Network (DNN) | 0.85 | 0.82 | 0.31 |
| Random Forest | 0.83 | 0.80 | 0.34 |
| Gradient Boosting | 0.84 | 0.81 | 0.32 |
| Linear Regression (baseline) | 0.62 | 0.58 | 0.55 |

All three ChIPr models substantially outperform the linear baseline. DNN is slightly best.

## 2024-02-05 -- Cross-cell-line evaluation

Trained on GM12878, tested on other cell lines (DNN model).

| Training cell line | Test cell line | Pearson r | Spearman rho |
|-------------------|---------------|----------|-------------|
| GM12878 | K562 | 0.78 | 0.75 |
| GM12878 | HeLa-S3 | 0.74 | 0.71 |
| GM12878 | HUVEC | 0.72 | 0.69 |
| K562 | GM12878 | 0.76 | 0.73 |

Reasonable cross-cell-line generalization, though within-cell-line is always best.

## 2024-02-20 -- Feature importance analysis (Random Forest)

| Feature | Importance (%) |
|---------|---------------|
| Genomic distance | 28.5 |
| CTCF ChIP-Seq | 22.3 |
| RAD21 ChIP-Seq | 18.7 |
| SMC3 ChIP-Seq | 14.2 |
| H3K27ac | 6.8 |
| DNase-seq | 5.1 |
| H3K4me3 | 2.9 |
| Other features | 1.5 |

Distance and CTCF/cohesin signals dominate, consistent with loop-extrusion biology.

## 2024-03-08 -- Within-cell-line performance across four cell lines

| Cell line | DNN Pearson r | RF Pearson r | GB Pearson r |
|-----------|-------------|-------------|-------------|
| GM12878 | 0.85 | 0.83 | 0.84 |
| K562 | 0.83 | 0.81 | 0.82 |
| HeLa-S3 | 0.80 | 0.78 | 0.79 |
| HUVEC | 0.79 | 0.77 | 0.78 |

Consistent high performance across all four cell lines tested.

## 2024-03-22 -- Comparison with existing methods

| Method | GM12878 Pearson r | Requires Hi-C training | Cell input |
|--------|------------------|----------------------|------------|
| ChIPr (DNN) | 0.85 | No | ChIP-Seq only |
| DeepC | 0.80 | Yes | Hi-C + seq |
| Akita | 0.78 | Yes | Sequence only |
| HiC-Reg | 0.76 | Yes | ChIP-Seq |

ChIPr achieves competitive or better accuracy without requiring Hi-C data for training.
