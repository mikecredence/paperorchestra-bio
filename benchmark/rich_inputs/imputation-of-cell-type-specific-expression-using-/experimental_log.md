# Experimental Log: Penalised regression improves imputation of cell-type specific expression using RNA-seq data from mixed cell populations compared to domain-specific methods

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- This design also allowed us to split our data into training (80 samples) and testing (between 52 and 71 samples depending on cell type) sets (Fig 2A) to compare the performance of potential imputation approaches.biorxiv;2023.09.11.556650v4/FIG2F2fig2Fig 2.Data and study design.(A) CLUSTER samples by
- TPM from sorted cells (CD4, CD8, CD14, and CD19) from 80 training samples were used to generate custom signature genes using the CIBERSORTxFractions module.
- For each cell type, we trained a LASSO/ridge model on PBMC and sorted cells with 5-fold cross-validation and used this to predict cell-type gene expression in the test samples.
- We compared imputed cell-type expressions with the observed ones and evaluated and benchmarked the performance using Pearson correlation, RMSE and a novel measure, differential gene expression (DGE) recovery.Estimation accuracy of sample-level cell frequenciesCIBERSORTx comes equipped with an inbuil
- We created a custom signature using our sorted cell expression in the training set (Fig 2B).
- We deconvoluted CD4, CD8, CD14, and CD19 cell fractions from PBMC mixed cells based on different scenarios: CIBERSORTx with inbuilt (CIBX-inbuilt) and custom (CIBX-custom) matrices, bMIND using the custom matrix (bMIND-custom), debCAM using cell-type specific markers derived from expression in our s
- We note that CD14 predicted fractions were overestimated regardless of approach and CD4 generally under-estimated (Fig 3).biorxiv;2023.09.11.556650v4/FIG3F3fig3Fig 3.Prediction accuracy of cell fractions by cell type (column) and approaches (row).Pearson correlation (R) and root mean square errors (
- CIBX-inbuilt: CIBERSORTx fraction deconvolution using the inbuilt signature matrix; CIBX-custom: CIBERSORTx fraction deconvolution using the custom signature matrix; bMIND-custom: bMIND fraction estimation using the custom signature matrix; debCAM-custom: debCAM fraction estimation using cell-type s
- In addition to predicted expression by CIBERSORTx using inbuilt and custom signature matrices, we derived cell-type expression profiles using true cell fractions (estimated by flow cytometry) with bMIND and swCAM algorithms (Fig 2B).
- While CIBERSORTx predicts only a subset of the most confident genes (5779-11794 depending on cell type), all other methods were able to predict expression for all or almost all 18871 genes across cell types (S1 Fig).Despite the differing number of imputed genes among methods (S1 Fig), initial analys
- These were also high, and only marginally different from baseline correlations, limiting the utility of this measure to discriminate among methods (S2 Fig).biorxiv;2023.09.11.556650v4/FIG4F4fig4Fig 4.Prediction accuracy of sample-level cell-type expression by approach.(A) Pearson correlation and (B)
- Correlation varied considerably between genes, irrespective of approaches (Fig 4C).
- All methods had comparable correlation per gene for each cell type, except for swCAM, which exhibited suboptimal performance for CD8, CD14, and CD19 (Fig 4C).
- Similar RMSE per gene was seen for each cell type across methods, although LASSO and ridge had slightly lower median values than other approaches (Fig 4D).
- Because different methods imputed values for different genes, we also compared methods restricting to the common gene sets predicted by all methods and found broadly the same ordering of methods by performance (S3 Fig).Recovery of significant genes in association testingDespite correlation and RMSE 
- DGE recovery measured the degree to which significant and non-significant signals in the observed data could be correctly identified in the imputed data (S4 and S5 Fig).
- This pattern was consistent across four simulated scenarios: either dichotomous or continuous phenotypes with or without covariate adjustment (Fig 5).
- Different methods can predict expression for different numbers of genes (S1 Fig), and we confirmed the broad pattern was also consistent when restricting to the common genes predicted by all approaches (S6 Fig).
- More detailed examination in the dichotomous phenotype setting showed that, generally, LASSO and ridge had higher sensitivity than CIBERSORTx, bMIND and swCAM, but also lower specificity (S7A Fig).
- In all cases, imputed estimates of log2 fold changes were attenuated in the imputed data, with average slopes of 0.60-0.70 in CIBERSORTx inbuilt, 0.64-0.76 in CIBERSORTx custom, 0.66-0.85 in bMIND, 0.55-0.90 in swCAM, 0.69-0.76 in LASSO and 0.68-0.76 in ridge (S7C Fig).biorxiv;2023.09.11.556650v4/FI
- For each simulated phenotype, the receiver operating characteristic curve and AUC were estimated by FDR fixed at 0.05 in the observed data and varied FDRs from 0 to 1 by 0.05 in the imputed data.
- Box plots showed the AUC distributions, with horizontal lines from the bottom to the top for 25%, 50 % and 75 % quantiles, respectively.
- CIBX-inbuilt: CIBERSORTx with the inbuilt signature matrix; CIBX-custom: CIBERSORTx with a custom signature matrix; bMIND: bMIND with flow fractions; swCAM: swCAM with flow fractions; LASSO/ridge: regularised multi-response Gaussian models.To provide a broader range of scenarios to compare these met
- albincas for 3 hours to untreated cells, in three settings: either unadjusted for batch, adjusted using batch as a covariate, or adjusted using Combat-seq This allowed us to consider different models including covariates or different ways to account for batch effects.
- We varied training sample size from 20 (25%) to 80 (100%) samples.
- LASSO and ridge regression consistently outperformed other methods across all cell types, regardless of whether raw or batch-corrected DGE results, in which batch effects were accounted for as a covariate or batch-corrected read counts by Combat-seq were used (Fig 6).
- This dominance persisted in further analysis of common gene sets (S8 Fig).
- All our results, taken together, suggest that regularised multivariate models performed better than the other three deconvolution-based methods.biorxiv;2023.09.11.556650v4/FIG6F6fig6Fig 6.Differential gene expression (DGE) recovery based on pseudobulk data.We varied training sample size from 20 (25%
- albicans after 3 hours (3hCA) vs untreated (UT).
- batch+cond: same as cond, and with batch (V2 & V3 chemistry) as a covariate in the 3hCA vs UT DGE model.
- Combat-seq cond: Combat-seq batch-corrected read counts were used in DGE analysis of 3hCA vs UT.
- For each pseudobulk data, the receiver operating characteristic curve and AUC were estimated by FDR fixed at 0.05 in the observed DGE results and varied FDRs from 0 to 1 by 0.05 in the DGE results using imputed expression.
- Note that CIBX-inbuilt is not shown for CD19/Combat-Seq cond.
- This is because it was able to impute < 60 genes, compared to ∼ 1,000 for CIBX-custom and > 11,000 for other methods, so estimates of AUC are very noisy.
- CIBX-inbuilt: CIBERSORTx with the inbuilt signature matrix; CIBX-custom: CIBERSORTx with a custom signature matrix based on pure cell expression in the training samples; bMIND: bMIND with true fractions; swCAM: swCAM with true fractions; LASSO/ridge: regularised multi-response Gaussian models.Comput
- For all methods, CPU time increased approximately exponentially with respect to training sample size but memory usage remained the same (S9 Fig).

## Tables

### S1 Table.
> Summary of existing deconvolution approaches.


### S2 Table.
> Computational time and memory usage by approach based on the CLUSTER data.


### S3 Table.
> Computational time and memory usage by approach based on the eQTLgen pseudobulk data.


## Figure Descriptions

### Fig 1.
Multi-response LASSO/ridge models for predicting sample-level cell-type expression.We utilised gene expression data from pure cell types (such as CD4, CD8, CD14, and CD19) and a mixed cell type (such as PBMC), all obtained from the same subjects as our training data. For each cell type, we clustered

### Fig 2.
Data and study design.(A) CLUSTER samples by cell type (row) and subject (column). Cells are coloured based on the availability of RNA (Y for yes, N for no), and the top panel annotations indicate the RNA sequencing batch (Batch) (B) Data analysis workflow. Transcripts per million (TPM) were calcula

### Fig 3.
Prediction accuracy of cell fractions by cell type (column) and approaches (row).Pearson correlation (R) and root mean square errors (RMSE) were calculated between estimated fractions (y-axis) and flow cytometry measures (x-axis). Each point is a testing sample and dashed blue lines indicate y = x. 

### Fig 4.
Prediction accuracy of sample-level cell-type expression by approach.(A) Pearson correlation and (B) log root mean square error (RMSE) comparing observed to predicted cell-type expression of genes from the same subjects, one estimate per subject. (C) Pearson correlation and (D) log RMSE between obse

### Fig 5.
Differential gene expression (DGE) recovery based on CLUSTER data.Area under curve (AUC) distributions estimated in held out test data by approach and cell type (columns) for each scenario (rows). Scenarios differed in simulated dichotomous (dichPheno)/ continuous (contPheno) phenotypes, with/withou

### Fig 6.
Differential gene expression (DGE) recovery based on pseudobulk data.We varied training sample size from 20 (25%) to 80 (100%) (x-axis) and quantified area under curve (AUC) in held out test data for DGE recovery (y-axis) by cell type (columns) for each scenario (rows). cond: raw aggregated read cou

### S1 Fig.
Overlap of predicted genes by CIBERSORTx using inbuilt (CIBX-inbuilt) and our custom signatures (CIBX-custom), bMIND, swCAM, LASSO and ridge.Predicted genes were defined as those with variations in expression across subjects. For each panel (cell type), the right bar plot indicates the numbers of pr

### S2 Fig.
Distributions of Pearson correlations (y-axis) between observed and imputed expression across genes from the same/different (diff) subjects and correlation between observed expression in different individuals in matched cell types (ObsDiff) by cell type and approach.One estimate per subject. CIBX-in

### S3 Fig.
Prediction accuracy of sample-level cell-type expression by approach.For each cell type, genes common across approaches were used. No. common genes are 3837 for CD4, 6274 for CD8, 5185 for CD14, and 2689 for CD19, respectively. (A) Pearson correlation and (B) log root mean square error (RMSE) compar

### S4 Fig.
Comparisons of log 2 fold changes in genes between the observed (x-axis) and imputed (y-axis) data by method (column) and by recovery status (row).DGE analysis was carried out using limma based on one of the simulated phenotypes. An FDR of 0.05 was used in both observed and imputed data here, and CD

### S5 Fig.
Receiver operating characteristic (ROC) curves and estimated area under curve (AUC, numbers noted) by cell type (row) and approach (column) based on one simulated phenotype.FDR was fixed at 0.05 in the observed data and varied from 0 to 1 by 0.05 in the imputed data. Dashed lines indicate y = x.

### S6 Fig.
Differential gene expression (DGE) recovery.Area under curve (AUC) distributions by approach and cell type (columns) for each scenario (rows). Scenarios differed in simulated dichotomous (dichPheno)/ continuous (contPheno) phenotypes, with/without sex as a covariate in the DGE analysis of the common

### S7 Fig.
Detailed examination of DGE recovery measures calling significance at FDR < 0.05 in both imputed and observed data.(A) Distributions of sensitivity and specificity of DGE recovery by cell type and approach. Each point is a simulated phenotype. (B) R-squared (Rsq, y-axis) and (C) slopes of imputed lo

### S8 Fig.
Differential gene expression (DGE) recovery based on pseudobulk data.We varied training sample size from 20 (25%) to 80 (100%) (x-axis) and quantified area under curve (AUC) for DGE recovery (y-axis) by cell type (columns) for each scenario (rows). cond: raw aggregated read counts were used for DGE 

### S9 Fig.
Resource metrics based on pseudobulk data.(A) CPU time in minutes (B) memory GB usage in the nature logarithm scale (y-axis) across 25%, 50%, 75% and 100% percentage of 80 train samples (x-axis). For serial jobs, swCAM, LASSO and ridge, CPU time was summed together for the same pseudobulk data, and 

### S10 Fig.
Differences between inbuilt and custom signature genes, and debCAM cell-type specific genes.(A) Expression of inbuilt signature genes (N=547) in 22 leukocyte subsets, curated by the CIBERSORTx team from microarray gene expression. For each gene (row), expression is centred to the mean and scaled by 

### S11 Fig.
Gating strategy for sorting cells into different immune cells.Initial gating was performed with forward (FSC) and side (SSC) scatters to isolate lymphocytes (PBMC). Further gating with FSC-A and FSC-W was done to exclude doublets. Live cells were selected based on the gating with DAPI. The live cell

### S12 Fig.
The first four principal components (PC) from PCA analysis of log2 (count-per-million) expression derived from (A) raw read counts (B) Combat-Seq batch-adjusted read counts in RNAseq samples used in this work.

### S13 Fig.
Frequencies (A) and percentages (B) of subjects by batch and training/testing set.

### S14 Fig.
Pearson correlations of cell fractions between 22 leucocyte (LM22) and ground-truth flow cell types.Columns are LM22 cell subsets split by their merged classes (top annotation). Rows are ground-truth cell types. Each cell is coloured based on the strength of the correlation.

## References
Total references in published paper: 39

### Key References (from published paper)
- Gene expression profiling of CD8+ T cells predicts prognosis in patients with Crohn disease and ulce (, 2011)
- A CD8+ T cell transcription signature predicts prognosis in autoimmune disease (, 2010)
- Novel expression signatures identified by transcriptional analysis of separated leucocyte subsets in (, 2010)
- T-cell exhaustion, co-stimulation and clinical outcome in autoimmunity and infection (, 2015)
- In Silico Cell-Type Deconvolution Methods in Cancer Immunotherapy (, 2020)
- Profiling Cell Type Abundance and Expression in Bulk Tissues with CIBERSORTx (, 2020)
- Computational deconvolution of transcriptomics data from mixed cell populations (, 2018)
- Quantifying tumor-infiltrating immune cells from transcriptomics data (, 2018)
- Cell type–specific gene expression differences in complex tissues (, 2010)
- Robust enumeration of cell subsets from tissue expression profiles (, 2015)
- Comprehensive analyses of tumor immunity: implications for cancer immunotherapy (, 2016)
- Simultaneous enumeration of cancer and immune cell types from bulk tumor gene expression data (, 2017)
- Determining cell type abundance and expression from bulk tissues with digital cytometry (, 2019)
- Fast and robust deconvolution of tumor infiltrating lymphocyte from expression profiles using least  (, 2019)
- Molecular and pharmacological modulators of the tumor immune contexture revealed by deconvolution of (, 2019)
- CDSeq: A novel complete deconvolution method for dissecting heterogeneous samples using gene express (, 2019)
- Using multiple measurements of tissue to estimate subject- and cell-type-specific gene expression (, 2020)
- debCAM: a bioconductor R package for fully unsupervised deconvolution of complex tissues (, 2020)
- CDSeqR: fast complete deconvolution for gene expression data from bulk tissues (, 2021)
- Bayesian estimation of cell type-specific gene expression with prior derived from single-cell data (, 2021)
- Computational deconvolution to estimate cell type-specific gene expression from bulk data (, 2021)
- A computational method for direct imputation of cell type-specific expression profiles and cellular  (, 2021)
- swCAM: estimation of subtype-specific expressions in individual samples with unsupervised sample-wis (, 2022)
- A benchmark for RNA-seq deconvolution analysis under dynamic testing environments (, 2021)
- Comprehensive evaluation of transcriptome-based cell-type quantification methods for immuno-oncology (, 2019)
- Benchmarking of cell type deconvolution pipelines for transcriptomics data (, 2020)
- Single-cell RNA-sequencing of peripheral blood mononuclear cells reveals widespread, context-specifi (, 2022)
- International League of Associations for Rheumatology classification of juvenile idiopathic arthriti (, 2004)
- Nextflow enables reproducible computational workflows (, 2017)
- STAR: ultrafast universal RNA-seq aligner (, 2013)

## Ground Truth Reference
- Figures: 20
- Tables: 3
- References: 39