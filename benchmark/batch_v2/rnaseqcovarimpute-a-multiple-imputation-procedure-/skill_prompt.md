Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Genome Biology

## Idea Summary

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


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the RNAseqCovarImpute method.

---

## Method Pipeline Overview

| Step | Description | Default Parameter |
|------|-------------|------------------|
| 1. Bin genes | Random grouping | 1 gene per 10 individuals |
| 2. Multiple imputation per bin | mice R package; log-CPM in predictor | M imputations |
| 3. voom + lmFit per bin/imputation | Global mean-variance curve | Modified voom function |
| 4. Un-bin + squeezeVar | Empirical Bayes variance shrinkage | Per M set |
| 5. Pool with Rubin's rules | Combined coefficients, SEs, p-values | Standard Rubin's |
| 6. FDR adjustment | Multiplicity correction | BH method |

---

## Simulation Study Design

| Parameter | Sim 1 | Sim 2 | Sim 3 |
|-----------|-------|-------|-------|
| Covariates | Real | Real | Synthetic (known confounding) |
| Counts | Real RNA-seq | Synthetic (known signal) | Synthetic (known signal) |
| N | 1,044 | 1,044 | 100, 250, 500, 1,000 |
| Missingness | MCAR, MAR | MCAR, MAR | MCAR, MAR |
| Levels | 10%, 30%, 50% | 10%, 30%, 50% | 10%, 30%, 50% |
| Null gene rate | N/A | 82.5%, 50% | Simulation-defined |
| Replicates | 10 per condition | 10 per condition | 10 per condition |
| Methods | CC, SI, MI | CC, SI, MI | CC, SI, MI |

---

## Simulation 1 Results: Real Covariates + Real Counts

| Missingness | Method | True Positives | FDR Control | Bias (all genes) | Bias (true DEGs) |
|-------------|--------|---------------|-------------|------------------|-----------------|
| MCAR 10% | CC | Baseline | Controlled | Moderate | Moderate |
| MCAR 10% | SI | Improved | Controlled | Reduced | Reduced |
| MCAR 10% | MI | Best | Controlled | Lowest | Lowest |
| MCAR 30% | CC | Reduced | Controlled | Increased | Increased |
| MCAR 30% | MI | Best | Controlled | Low | Low |
| MCAR 50% | CC | Most reduced | Controlled | Highest | Highest |
| MCAR 50% | MI | Best | Controlled | Moderate | Moderate |
| MAR 10% | CC | Baseline | Controlled | Potentially biased | Potentially biased |
| MAR 10% | MI | Best | Controlled | Lowest | Lowest |
| MAR 30% | MI | Best | Controlled | Low | Low |
| MAR 50% | MI | Best | Controlled | Moderate | Moderate |

Fig. 2: Error, bias for all genes, and bias for true DEGs across MCAR (A-C) and MAR (D-F).

---

## Simulation 2 Results: Synthetic Counts with Known Signal

### 82.5% Null Gene Rate

| Missingness | Method | TP Rate | FDR |
|-------------|--------|---------|-----|
| MCAR | CC | Lower | Controlled |
| MCAR | SI | Intermediate | Slightly elevated |
| MCAR | MI | Highest | Controlled |
| MAR | CC | Lower | Controlled |
| MAR | MI | Highest | Controlled |

### 50% Null Gene Rate

| Missingness | Method | TP Rate | FDR |
|-------------|--------|---------|-----|
| MCAR | CC | Lower | Controlled |
| MCAR | SI | Intermediate | More elevated |
| MCAR | MI | Highest | Controlled |

Fig. 3: Results at 82.5% null rate. Fig. 4: Results at 50% null rate.

---

## Simulation 3 Results: Fully Synthetic Data

| Sample Size | Method | TP at 30% MCAR | FDR at 30% MCAR |
|------------|--------|----------------|-----------------|
| 100 | CC | Low | Controlled |
| 100 | MI | Improved | Controlled |
| 250 | CC | Moderate | Controlled |
| 250 | MI | Improved | Controlled |
| 500 | CC | Moderate-high | Controlled |
| 500 | MI | Improved | Controlled |
| 1,000 | CC | High | Controlled |
| 1,000 | MI | Highest | Controlled |

Fig. 5: FDR and TP rates across sample sizes for MCAR (A) and MAR (B).
Fig. 6-7: Bias analysis across all conditions.

---

## Application: Maternal Age and Placental Transcriptome

| Method | DEGs Found | Unique DEGs | Shared with MI |
|--------|-----------|-------------|---------------|
| CC | Subset | Some | Partial overlap |
| SI | Subset | Some | Partial overlap |
| MI | Largest set | Additional unique | Reference |

Fig. 9A: Venn diagram of shared/distinct DEGs. Fig. 9B: P-value rankings for top 10 MI genes.
Fig. 9C-E: Volcano plots for CC, SI, MI.
Fig. 8: Directed acyclic graph of maternal age to placental transcriptome relationships.

---

## Imputation Methods (mice R package)

| Variable Type | Imputation Method |
|--------------|------------------|
| Continuous | Predictive mean matching |
| Binary | Logistic regression |
| Categorical | Polytomous regression |
| Ordered | Proportional odds |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Pipeline overview: binning, imputation, modeling, pooling |
| Fig. 2 | Sim 1: MI identifies more TPs without FDR inflation |
| Fig. 3-4 | Sim 2: Advantages hold with synthetic signal at two null rates |
| Fig. 5 | Sim 3: MI advantages scale with sample size |
| Fig. 6-7 | Bias minimized by MI across conditions |
| Fig. 8-9 | Applied analysis: MI finds most DEGs for maternal age association |

---

## Reference Count
31 references cited.

