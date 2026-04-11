# Experimental Log: SPEAR Multi-Omics Signature Model

## Experiment 1: Gaussian Simulation

### Simulation Setup

| Parameter | Value |
|-----------|-------|
| Number of simulated factors | 5 |
| Predictive factors (used for Y) | 2 (factors 1 and 2) |
| Non-predictive factors (X only) | 3 (factors 3, 4, 5) |
| Number of omics assays | 4 |
| Features per assay | 500 |
| Total features | 2000 |
| Training samples | 500 |
| Test samples | 2000 |
| Signal-to-noise ratios | Low, Moderate, High |
| Independent iterations per ratio | 10 |
| Response type | Gaussian |

### Methods Compared

| Method | Type |
|--------|------|
| SPEAR (w = 0) | Supervised factor model, pure prediction |
| SPEAR (w = 0.5) | Supervised factor model, balanced |
| SPEAR (w = 1) | Supervised factor model, structure-weighted |
| SPEAR (w = CV) | Supervised factor model, cross-validated w |
| MOFA + Lasso | Unsupervised factors + downstream Lasso |
| Lasso | Direct Lasso on concatenated features |

### MSE Results (Fig 2A)

| Method | Low Signal MSE | Moderate Signal MSE | High Signal MSE |
|--------|---------------|-------------------|-----------------|
| SPEAR (w=1) | Moderate | Significantly lower than MOFA | Lowest |
| SPEAR (w=0) | Higher | Higher than w=1 | Higher than w=1 |
| MOFA + Lasso | Higher | Higher than SPEAR w=1 | Moderate |
| Lasso | Highest | Highest | Highest |

SPEAR w=1 significantly outperformed MOFA at moderate signal-to-noise ratio.

### Factor Recovery (Fig 2C, Moderate Signal)

| Method | Factor 1 Recovered | Factor 2 Recovered | Factor 3 Recovered | Factor 4 Recovered | Factor 5 Recovered |
|--------|-------------------|-------------------|-------------------|-------------------|-------------------|
| SPEAR (w=1) | Yes | Yes | Yes | Yes | Yes |
| SPEAR (w=0) | Merged with F2 | Merged with F1 | No | No | No |
| MOFA | No | No | Yes | No | Yes |

SPEAR (w=1) correctly identified all five simulated factors. MOFA only identified factors 3 and 5 (uncorrelated factors), likely due to lack of supervision. SPEAR (w=0) condensed all predictive signal into a single factor.

### Factor-Response Correlation (Fig 2B)

| Method | Factors correlated with Y |
|--------|--------------------------|
| SPEAR (w=1) | 2 factors (matching ground truth) |
| SPEAR (w=0) | 1 factor (merged predictive signal) |
| MOFA | 0 factors strongly correlated |

## Experiment 2: TCGA Breast Cancer (TCGA-BC)

### Dataset Characteristics

| Parameter | Value |
|-----------|-------|
| Cancer type | Breast invasive carcinoma |
| Response type | Multinomial (tumor subtypes) |
| Subtypes | LumA, LumB, Basal, Her2, Normal-like |
| Omics assays | mRNA, protein (RPPA), CNV, DNA methylation |
| Total features | Tens of thousands |

### Prediction Results: LumB Subtype AUROC (Fig 3B)

| Method | AUROC (LumB) | 95% CI |
|--------|-------------|--------|
| SPEAR | Highest | Narrowest CI |
| MOFA | Lower | Wider CI |
| Lasso | Lower | Wider CI |
| DIABLO | Comparable | -- |
| iClusterBayes | Lower | -- |

Significance tests (2000 stratified bootstrap replicates):
- SPEAR vs MOFA: p <= 0.05 (*)
- SPEAR vs Lasso: p <= 0.005 (**)

### AUROC Plot (Fig 3C)

Fig 3A shows SPEAR model correctly predicts tumor subtypes with clear separation in test samples.
Fig 3C shows AUROC curves for LumB prediction across all methods; SPEAR dominates.

### Downstream Interpretation (Fig 4)

| Factor | Biological Interpretation |
|--------|--------------------------|
| Factor 1 | Separates Basal from Luminal; enriched for Estrogen Response pathway |
| Factor 2 | Separates Her2 subtype; enriched for relevant signaling |
| Factor 3 | Further subtype discrimination |

Fig 4A: Violin plots of factor scores by tumor subtype show clear group separation.
Fig 4B: 3D scatter embedding by factors 1-3 shows clustering by subtype.
Fig 4C: GSEA dotplot shows enriched pathways per factor with directionality.
Fig 4D: GSEA enrichment plot for Estrogen Response (Early) Hallmark pathway in Factor 1.

## Experiment 3: COVID-19 Severity Prediction

### Dataset Characteristics

| Parameter | Value |
|-----------|-------|
| Response type | Ordinal (WHO severity scale) |
| Severity categories | Mild, Moderate, Severe |
| Omics assays | mRNA, protein, metabolomics |
| Total features | Tens of thousands |

### Prediction Results: Moderate Class AUROC (Fig 3F)

| Method | AUROC (Moderate) | 95% CI |
|--------|-----------------|--------|
| SPEAR | Highest | Narrowest CI |
| MOFA | Lower | Wider CI |
| Lasso | Lower | Wider CI |
| DIABLO | Lower | -- |

Significance tests:
- SPEAR vs MOFA: p <= 0.0005 (***)
- SPEAR vs Lasso: p <= 0.005 (**)

Fig 3E shows SPEAR correctly separates severity classes in test predictions.
Fig 3G shows AUROC curves for Moderate severity prediction.

### Downstream Interpretation (Fig 5)

| Factor | Biological Interpretation |
|--------|--------------------------|
| Factor 2 | Separates Severe from Mild/Moderate; enriched for IL6 JAK STAT3 signaling |
| Factor 8 | Further severity discrimination |

Fig 5A: Factor 2 scores increase monotonically with WHO severity.
Fig 5B: Factor 8 scores also associate with severity.
Fig 5C: GSEA plot for IL6 JAK STAT3 Signaling in Factor 2 shows enrichment among proteins ranked by projection coefficients.
Fig 5D: 2D embedding by factors 2 and 8 shows severity-dependent clustering.

## Weight Parameter Analysis

| w Value | Behavior |
|---------|----------|
| w >= 1 | Emphasizes multi-omics structure in X |
| 0 < w < 1 | Gradually shifts emphasis toward predicting Y |
| w ~ 0 | Pure prediction, ignores X structure |
| w (CV selected) | Automatically balances; favors larger w |

Cross-validation selects the largest w whose error falls within 1 SD of the minimum, favoring structure-preserving factors when supported by data.

## SPEAR Model Features

| Feature | Description |
|---------|-------------|
| Automatic factor rank estimation | Estimates minimum number of factors adaptively |
| ARD (Automatic Relevance Determination) | Allows asymmetric assay contributions per factor |
| Spike-and-slab priors | Feature-level sparsity |
| Posterior probability selection | Features selected at P(non-zero) > 0.95 |
| Regression coefficients | Sparse predictive features per factor |
| Projection coefficients | Full factor influence on all analytes |
| Response types | Gaussian, ordinal, multinomial, binomial, multiple |

## Comparison Methods

| Method | Category | Key Difference from SPEAR |
|--------|----------|--------------------------|
| MOFA | Unsupervised factor model | No response supervision |
| Lasso | Supervised regression | No factor structure |
| DIABLO | Supervised multi-block | PLS-based, not Bayesian |
| iClusterBayes | Bayesian clustering | Clustering-based, not predictive regression |

## Key Figure Observations Summary

- Fig 1: Workflow shows X and Y jointly modeled, automatic factor estimation, VB inference, prediction, and downstream interpretation
- Fig 2A: Boxplots of test MSE across signal levels; SPEAR w=1 consistently best at moderate/high signal
- Fig 2B: Scatterplots of factor scores vs Y; SPEAR w=1 shows two correlated factors matching ground truth
- Fig 2C: Correlation matrices showing factor recovery; SPEAR w=1 recovers all 5, MOFA recovers only 2
- Fig 3A,E: Test sample predictions show good class separation for both datasets
- Fig 3B,F: AUROC bar charts with bootstrap CIs and significance stars
- Fig 3C,G: Full AUROC curves
- Fig 4: TCGA-BC downstream analysis with violin plots, 3D embedding, GSEA
- Fig 5: COVID-19 downstream analysis with factor-severity relationships and pathway enrichment

## Software and Implementation

| Item | Detail |
|------|--------|
| Language | R |
| Package | SPEAR |
| Repository | https://bitbucket.org/kleinstein/SPEAR |
| Inference | Variational Bayes |
| Cross-validation | K-fold for weight selection |
