# Experimental Log: Spatial Transcriptomics Platform Benchmarking

## Experiment 1: Capture sensitivity across platforms

Median genes detected per cell across three cancer types.

| Platform | Colon Adeno. | HCC | Ovarian | Mean Across Tissues |
|---|---|---|---|---|
| Stereo-seq v1.3 | 420 | 385 | 390 | 398 |
| Visium HD FFPE | 580 | 510 | 545 | 545 |
| Visium HD FF | 720 | 680 | 695 | 698 |
| CosMx 6K | 185 | 170 | 178 | 178 |
| Xenium 5K | 165 | 152 | 160 | 159 |

Note: CosMx and Xenium are targeted panels (6K and 5K genes respectively), so raw gene counts are not directly comparable to whole-transcriptome platforms.

## Experiment 2: Specificity (false positive rate)

Fraction of transcripts assigned to wrong cell or background.

| Platform | Background Rate (%) | Cross-Cell Contamination (%) | Overall Specificity |
|---|---|---|---|
| Stereo-seq v1.3 | 8.2 | 5.1 | 0.87 |
| Visium HD FFPE | 4.5 | 3.2 | 0.92 |
| Visium HD FF | 3.8 | 2.8 | 0.93 |
| CosMx 6K | 2.1 | 1.5 | 0.96 |
| Xenium 5K | 1.8 | 1.3 | 0.97 |

## Experiment 3: Diffusion control

Spatial spread of transcripts beyond expected cell boundary (um).

| Platform | Median Diffusion (um) | 95th Percentile (um) |
|---|---|---|
| Stereo-seq v1.3 | 3.2 | 8.5 |
| Visium HD FFPE | 2.1 | 5.8 |
| Visium HD FF | 1.8 | 5.2 |
| CosMx 6K | 0.8 | 2.1 |
| Xenium 5K | 0.6 | 1.8 |

## Experiment 4: Cell segmentation accuracy vs manual ground truth

| Platform | Precision | Recall | F1 Score |
|---|---|---|---|
| Stereo-seq v1.3 | 0.72 | 0.68 | 0.70 |
| Visium HD FFPE | 0.78 | 0.74 | 0.76 |
| Visium HD FF | 0.80 | 0.77 | 0.78 |
| CosMx 6K | 0.85 | 0.82 | 0.83 |
| Xenium 5K | 0.87 | 0.84 | 0.85 |

## Experiment 5: Concordance with scRNA-seq ground truth

Correlation of cell-type proportions (platform vs scRNA-seq).

| Platform | Pearson r | Spearman rho |
|---|---|---|
| Stereo-seq v1.3 | 0.82 | 0.79 |
| Visium HD FFPE | 0.88 | 0.85 |
| Visium HD FF | 0.91 | 0.88 |
| CosMx 6K | 0.90 | 0.87 |
| Xenium 5K | 0.89 | 0.86 |

## Notes

- Trade-off pattern: whole-transcriptome platforms (Visium HD, Stereo-seq) capture more genes but have higher diffusion; targeted platforms (CosMx, Xenium) have better specificity and segmentation but limited gene panels.
- Fresh frozen (FF) outperforms FFPE on Visium HD for sensitivity.
- Three cancer types used to ensure generalizability across tissue morphologies.
