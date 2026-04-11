# Idea Summary

## Working title
RNAseqCovarImpute: A Multiple Imputation Procedure That Outperforms Complete Case and Single Imputation Differential Expression Analysis

## Core question
Can multiple imputation of missing covariate data, incorporating high-dimensional gene expression in the imputation model via a gene-binning strategy, improve differential expression analysis over complete case and single imputation approaches?

## Motivation / gap
- Missing covariate data is ubiquitous in large observational studies but has not been addressed for transcriptomic outcomes
- Standard MI requires including outcome in the imputation model, infeasible with tens of thousands of genes
- Complete case analysis drops individuals, reducing power and potentially introducing bias
- Single imputation ignores uncertainty, leading to overconfident standard errors
- No R package integrates MI with the limma-voom RNA-seq pipeline
- Sequencing costs are declining, making transcriptomics increasingly common in epidemiologic studies

## Core contribution (bullet form)
- Developed gene-binning strategy (default 1 gene per 10 individuals) enabling MI to include gene expression in imputation predictor matrices
- Demonstrated superior performance across 3 simulation studies: real covariates + real counts (N=1,044), real covariates + synthetic counts, fully synthetic data
- MI identified more true positive DEGs without FDR inflation across MCAR and MAR missingness at 10-50% levels
- Showed reduced bias compared to CC and SI across sample sizes of 100-1,000
- Applied to maternal age-placental transcriptome analysis, identifying shared and distinct DEGs
- Released RNAseqCovarImpute R package integrating with limma-voom

## Method in brief
The method bins genes randomly into groups (~1 gene per 10 observations), creates M imputed datasets per bin using mice R package with log-CPM included as predictors, fits voom + lmFit models per bin/imputation using a global mean-variance curve, un-bins and applies squeezeVar empirical Bayes, pools with Rubin's rules, and adjusts for FDR. Three simulation studies compared MI, SI, and CC across MCAR/MAR missingness mechanisms at multiple levels.

## Target venue
Genome Biology
