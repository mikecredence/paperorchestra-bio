## Working title

Penalized regression outperforms deconvolution methods for imputing sample-level cell-type expression from bulk PBMC RNA-seq

## Core question

Can general-purpose machine learning methods (multi-response LASSO and ridge regression) impute sample-level cell-type-specific gene expression from mixed-cell bulk RNA-seq more accurately than domain-specific deconvolution tools, and how should prediction accuracy be evaluated?

## Motivation / gap

- Single-cell and sorted-cell RNA-seq remain expensive for large cohorts; many studies use bulk PBMC RNA-seq, losing cell-type-specific signals
- Computational deconvolution can estimate cell fractions and average cell-type expression, but sample-level imputation (needed for quantitative trait analysis) is less commonly addressed
- Existing deconvolution tools (CIBERSORTx, bMIND, debCAM/swCAM) have not been systematically benchmarked on real matched data where both mixed and sorted expression exist for the same individuals
- No prior work has applied multi-response LASSO/ridge regression to this imputation task
- Standard evaluation metrics (Pearson correlation) may be misleading -- per-gene correlations are often low even when per-subject correlations are high, and high between-subject correlations may simply reflect cell-type identity rather than accurate imputation
- A more informative evaluation metric based on differential gene expression (DGE) recovery is needed

## Core contribution (bullet form)

- Benchmarked 5 methods (CIBERSORTx inbuilt, CIBERSORTx custom, bMIND, swCAM, LASSO, ridge) on real CLUSTER data (N=158 subjects, PBMC + sorted CD4/CD8/CD14/CD19) with 80 training / 52-71 test samples
- Validated on pseudobulk data synthesized from eQTLgen single-cell RNA-seq, varying training size from 20 to 80 samples
- Proposed DGE recovery as a novel evaluation metric that measures ability to reconstruct differential expression signals, outperforming simple correlation
- LASSO/ridge showed higher AUC for DGE recovery than all three deconvolution methods across cell types and scenarios
- LASSO/ridge had higher sensitivity but lower specificity for DGE recovery compared to deconvolution approaches
- Demonstrated that per-gene correlation is more informative than per-subject correlation, and that correlation alone is insufficient for evaluating imputation quality

## Method in brief

The CLUSTER consortium collected PBMC RNA-seq and FACS-sorted cell RNA-seq (CD4, CD8, CD14, CD19) from the same 158 subjects (126 JIA patients, 32 controls). After standard processing (STAR alignment, UMI deduplication, featureCounts, TPM normalization), the data were split into 80 training and 52-71 test samples per cell type. For deconvolution, CIBERSORTx was run with both its inbuilt LM22 signature and a custom signature derived from training sorted-cell data; bMIND and swCAM used flow cytometry fractions. The linear mixture model posits m = Hf, where m is observed bulk expression, H is a cell-type expression matrix, and f is the vector of cell fractions.

For the ML approach, genes were clustered into chunks of similar expression patterns within each cell type. For each chunk, a multi-response LASSO or ridge model was trained to predict sorted-cell expression from PBMC predictor genes using 5-fold cross-validation. The key equation is: Y_cell = B * X_PBMC, where B is the learned coefficient matrix. This approach directly learns the mapping from mixed to pure expression without requiring explicit cell fraction estimation.

DGE recovery evaluation simulated phenotypes (dichotomous and continuous, with and without sex covariate), ran DGE on both observed sorted-cell data and imputed data, and compared results using AUC of true/false positive rates at varying FDR thresholds. Pseudobulk validation used eQTLgen scRNA-seq data aggregated to simulate bulk mixtures, with a stimulation condition (C. albicans 3h) providing real biological signal for DGE testing.

## Target venue

PLOS Computational Biology
