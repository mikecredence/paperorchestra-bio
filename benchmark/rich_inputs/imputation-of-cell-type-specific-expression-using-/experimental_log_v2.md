# Experimental Log: Cell-Type Expression Imputation from Bulk RNA-seq

## Study Cohort (CLUSTER Consortium)

| Parameter | Value |
|-----------|-------|
| Total subjects | 158 |
| JIA patients | ~126 (80%) |
| Healthy controls | ~32 (adults + children) |
| Female subjects | 91 (58%) |
| Mixed cell type | PBMC |
| Sorted cell types | CD4, CD8, CD14, CD19 |
| Cell sorting method | BD FACSAria III (FACS) |
| Sorted cell purity | >90% average |
| RNA extraction | PicoPure RNA Isolation Kit |
| Sequencing platform | Illumina NovaSeq6000 |
| Read length | 2 x 100 bp |
| Sequencing batches | 4 |
| Genome reference | GRCh38 |
| Aligner | STAR (two-pass mode) |
| Gene annotation | Homo_sapiens.GRCh38.103.gtf |
| Deduplication | UMI-based (je suite tool, up to 1 mismatch) |
| Quantification | featureCounts |
| RNA QC thresholds | RIN >= 5.0, library conc >= 4.5 nM (~0.7 ng/uL) |
| Library prep kits | Illumina TruSeq mRNA stranded v2, Roche Kapa mRNA HyperPrep |

## Data Split

| Set | N Samples | Purpose |
|-----|-----------|---------|
| Training | 80 | Model fitting, signature generation |
| Testing (varies by cell type) | 52-71 | Performance evaluation |

## Methods Compared

| Method | Type | Cell Fraction Source | Expression Imputation Approach |
|--------|------|---------------------|-------------------------------|
| CIBX-inbuilt | Deconvolution | LM22 inbuilt signature | CIBERSORTx high-resolution module |
| CIBX-custom | Deconvolution | Custom signature from training sorted cells | CIBERSORTx high-resolution module |
| bMIND | Deconvolution | Flow cytometry fractions | Bayesian estimation |
| swCAM | Deconvolution | Flow cytometry fractions | Weighted deconvolution |
| LASSO | Machine learning | Not needed (direct prediction) | Multi-response LASSO with 5-fold CV |
| Ridge | Machine learning | Not needed (direct prediction) | Multi-response ridge with 5-fold CV |

## Cell Fraction Estimation Accuracy (Fig 3)

### Pearson Correlation Between Estimated and Flow Cytometry Fractions

| Method | CD4 | CD8 | CD14 | CD19 |
|--------|-----|-----|------|------|
| CIBX-inbuilt | Lower | Best | Good | Good |
| CIBX-custom | Low (some zero estimates) | Moderate | Moderate | Moderate |
| bMIND-custom | Low (some zero estimates) | Moderate | Moderate | Moderate |
| debCAM | Best | Lower | Good | Good |

- Fig 3: Scatter plots of estimated vs. flow cytometry fractions by cell type and approach
- CIBX-inbuilt and debCAM generally outperformed bMIND and CIBX-custom
- bMIND and CIBX-custom produced several estimated fractions of exactly zero when observed data were clearly non-zero
- CD4 fractions were consistently hardest to estimate across all methods
- CIBERSORTx was most accurate for CD8 despite underperforming for CD4
- debCAM provided best CD4 estimates but was less accurate for CD8

### RMSE of Fraction Estimates

| Method | CD4 | CD8 | CD14 | CD19 |
|--------|-----|-----|------|------|
| CIBX-inbuilt | Moderate | Low (best) | Low | Low |
| CIBX-custom | High | Moderate | Moderate | Moderate |
| bMIND-custom | High | Moderate | Moderate | Moderate |
| debCAM | Low (best) | Moderate | Low | Low |

## Number of Predicted Genes by Method (S1 Fig)

| Method | CD4 | CD8 | CD14 | CD19 |
|--------|-----|-----|------|------|
| CIBX-inbuilt | Varies | Varies | Varies | Varies |
| CIBX-custom | Fewer | Fewer | Fewer | Fewer |
| bMIND | Moderate | Moderate | Moderate | Moderate |
| swCAM | Moderate | Moderate | Moderate | Moderate |
| LASSO | Many | Many | Many | Many |
| Ridge | Many | Many | Many | Many |

- S1 Fig: UpSet-style plots showing overlap of predicted genes across methods
- Predicted genes defined as those with expression variation across subjects
- LASSO and ridge predict expression for more genes than deconvolution methods

### Common Genes Across All Methods (S3 Fig)

| Cell Type | Number of Common Genes |
|-----------|----------------------|
| CD4 | 3837 |
| CD8 | 6274 |
| CD14 | 5185 |
| CD19 | 2689 |

## Expression Prediction Accuracy (Fig 4)

### Per-Subject Pearson Correlation (Fig 4A)

| Method | CD4 | CD8 | CD14 | CD19 | Pattern |
|--------|-----|-----|------|------|---------|
| CIBX-inbuilt | High | High | High | High | Good across all |
| CIBX-custom | High | High | High | High | Similar to inbuilt |
| bMIND | High | High | High | High | Comparable |
| swCAM | High | High | High | High | Comparable |
| LASSO | High | High | High | High | Comparable |
| Ridge | High | High | High | High | Comparable |

- Per-subject correlations were generally high across all methods
- High between-subject correlations were also observed (S2 Fig), likely reflecting that cell type explains the greatest proportion of expression variability
- Per-subject correlation may not be a discriminating metric

### Per-Gene Pearson Correlation (Fig 4C)

| Method | CD4 | CD8 | CD14 | CD19 | Pattern |
|--------|-----|-----|------|------|---------|
| CIBX-inbuilt | Low-moderate | Low-moderate | Low-moderate | Low-moderate | -- |
| CIBX-custom | Low-moderate | Low-moderate | Low-moderate | Low-moderate | -- |
| bMIND | Low-moderate | Low-moderate | Low-moderate | Low-moderate | -- |
| swCAM | Low-moderate | Low-moderate | Low-moderate | Low-moderate | -- |
| LASSO | Low-moderate | Low-moderate | Low-moderate | Low-moderate | -- |
| Ridge | Low-moderate | Low-moderate | Low-moderate | Low-moderate | -- |

- Per-gene correlations were low to moderate across all methods, consistent with bMIND and swCAM literature
- This suggests correlation is not an optimal performance measure

### Per-Subject Log RMSE (Fig 4B)

| Method | CD4 | CD8 | CD14 | CD19 |
|--------|-----|-----|------|------|
| All methods | Similar ranges | Similar ranges | Similar ranges | Similar ranges |

### Per-Gene Log RMSE (Fig 4D)

| Method | CD4 | CD8 | CD14 | CD19 |
|--------|-----|-----|------|------|
| Deconvolution methods | Moderate | Moderate | Moderate | Moderate |
| LASSO/Ridge | Comparable or slightly better | Comparable | Comparable | Comparable |

- RMSE was standardized by average observed expression per gene

## DGE Recovery Evaluation (Fig 5) -- CLUSTER Data

### Simulated Phenotype Scenarios

| Scenario | Phenotype Type | Covariates |
|----------|---------------|------------|
| dichPheno | Dichotomous (simulated) | None |
| dichPheno+sex | Dichotomous (simulated) | Sex |
| contPheno | Continuous (simulated) | None |
| contPheno+sex | Continuous (simulated) | Sex |

### AUC for DGE Recovery by Method and Cell Type (Fig 5)

| Method | CD4 AUC | CD8 AUC | CD14 AUC | CD19 AUC | Overall Pattern |
|--------|---------|---------|----------|----------|----------------|
| CIBX-inbuilt | Lower | Lower | Lower | Lower | Baseline deconvolution |
| CIBX-custom | Lower | Lower | Lower | Lower | Similar to inbuilt |
| bMIND | Lower | Lower | Lower | Lower | Comparable to CIBERSORTx |
| swCAM | Lower | Lower | Lower | Lower | Comparable |
| LASSO | Higher | Higher | Higher | Higher | Best or near-best |
| Ridge | Higher | Higher | Higher | Higher | Best or near-best |

- LASSO/ridge consistently achieved higher AUC for DGE recovery than all three deconvolution methods
- DGE recovery was comparable across deconvolution methods despite bMIND/swCAM using flow cytometry fractions (expected to be more accurate)
- Pattern held across all four phenotype simulation scenarios

### Sensitivity vs. Specificity Trade-off (S4 Fig)

| Method Type | Sensitivity | Specificity | AUC |
|-------------|-----------|-------------|-----|
| LASSO/Ridge | Higher | Lower | Higher |
| Deconvolution | Lower | Higher | Lower |

- S4 Fig: Log2 fold change comparisons between observed and imputed data show LASSO/ridge recover more true positives but also more false positives
- FDR threshold of 0.05 used in both observed and imputed data

## DGE Recovery on Pseudobulk Data (Fig 6) -- eQTLgen

### Pseudobulk Dataset Properties

| Parameter | Value |
|-----------|-------|
| Source | eQTLgen single-cell RNA-seq |
| Synthesis method | Pseudobulk aggregation |
| Training sizes tested | 20 (25%), 40 (50%), 60 (75%), 80 (100%) |
| Test data | Held out |
| Biological condition | In vitro stimulation with C. albicans 3h (3hCA) vs. untreated (UT) |

### DGE Recovery Scenarios for Pseudobulk

| Scenario | Description |
|----------|-------------|
| cond | Raw aggregated counts for DGE of 3hCA vs. UT |
| batch+cond | Same as cond with batch (V2 & V3 chemistry) as covariate |

### AUC vs. Training Sample Size (Fig 6)

| Training Size | LASSO/Ridge AUC Trend | Deconvolution AUC Trend |
|--------------|----------------------|------------------------|
| 20 (25%) | Lower but still competitive | Lower |
| 40 (50%) | Improved | Modest improvement |
| 60 (75%) | Further improved | Modest improvement |
| 80 (100%) | Highest | Plateau |

- Fig 6: AUC increases with training sample size for LASSO/ridge
- Deconvolution methods show less sensitivity to training size (they rely more on signature matrices)
- LASSO/ridge outperform deconvolution at all training sizes tested

## Computational Resources (S2 Table, S3 Table)

### CLUSTER Data (S2 Table)

| Method | Computational Time | Memory Usage |
|--------|-------------------|-------------|
| CIBERSORTx | Reported | Reported |
| bMIND | Reported | Reported |
| swCAM | Reported | Reported |
| LASSO | Reported | Reported |
| Ridge | Reported | Reported |

### eQTLgen Pseudobulk Data (S3 Table)

| Method | Computational Time | Memory Usage |
|--------|-------------------|-------------|
| CIBERSORTx | Reported | Reported |
| bMIND | Reported | Reported |
| swCAM | Reported | Reported |
| LASSO | Reported | Reported |
| Ridge | Reported | Reported |

## LASSO/Ridge Model Design Details (Fig 1)

| Step | Description |
|------|-------------|
| 1. Gene clustering | Cluster target genes with similar expression patterns into chunks |
| 2. Predictor selection | Use PBMC expression of predictor genes |
| 3. Model training | Multi-response LASSO or ridge per chunk, 5-fold CV |
| 4. Prediction | Apply learned model to test PBMC samples |
| 5. Output | Predicted cell-type expression per gene per sample |

### Key Model Equation

- Y_cell = B * X_PBMC
- B learned via penalized regression (L1 for LASSO, L2 for ridge)
- Multi-response formulation handles correlated genes within chunks jointly

## Deconvolution Model

- Core equation: m = H * f
- m: observed bulk expression (n genes)
- H: cell-type expression matrix (n genes x c cell types)
- f: cell fraction vector (c cell types)
- Sample-level expression G: n genes x c cell types x k samples

## Key Observations from Figures

- Fig 2A: Study design showing sample availability matrix with subjects as columns and cell types as rows
- Fig 2B: Analysis workflow from TPM calculation through fraction estimation, expression imputation, and evaluation
- Fig 4A: Per-subject correlations are high and similar across methods (not discriminating)
- Fig 4C: Per-gene correlations are low-moderate and more informative
- Fig 5: LASSO/ridge AUC distributions are shifted higher than deconvolution methods across all cell types and scenarios
- Fig 6: Performance advantage of LASSO/ridge grows with training sample size
- S2 Fig: High between-subject correlations observed even for different subjects, reflecting cell-type-level variability dominance

## Summary of Recommendations

| Task | Recommended Method |
|------|-------------------|
| Cell fraction estimation | CIBX-inbuilt or debCAM |
| Sample-level expression imputation | LASSO or ridge (when training data available) |
| Evaluation metric | DGE recovery (AUC) preferred over correlation |
| Per-gene vs. per-subject correlation | Per-gene more informative |
