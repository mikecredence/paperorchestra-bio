# Experimental Log: PEPerMINT: Peptide Abundance Imputation in Mass Spectrometry-based Proteomics using Graph Neural Networks

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- S8 of the Supplement.Abundance-based evaluationWe first performed an abundance-based evaluation via the sample-wise RMSE for four datasets with artificially introduced missing values and two DDA/DIA datasets with ground truth values acquired using the DIA (Fig.
- Particularly, we find that our PEPerMINT imputation method gives the best performance across all evaluated datasets, outperforming the second best-performing method (BPCA) by up to 20% on the breast cancer dataset.
- We obtain similar results for dataset-wise mean absolute error as an alternative metric (see Supplement).biorxiv;2024.03.23.586248v1/FIG3F3fig3Fig.
- 3.A: Sample-wise RMSE of all evaluated imputation methods on all six benchmark datasets with 95% confidence interval error bars (bootstrapped).
- B: Results for the prostate cancer (A1) dataset stratified by their fraction of missing values over the samples (see supplement for stratified results of other datasets).
- 3B for the prostate cancer dataset; similar results for other datasets, see Supplement).
- 4 shows the results for statistically comparing imputation methods using a Wilcoxon signed-rank test (see Methods).
- 3, the Wilcoxon test compares individual imputed values without averaging the error per dataset sample.
- S4).biorxiv;2024.03.23.586248v1/FIG4F4fig4Fig.
- 4.Pairwise comparison of different imputation methods by statistical significance test results (see Methods).
- Colors encode how many of the six evaluated datasets the imputation method given in the row performs significantly better (5% significance level) than the imputation method given in the column (insignificant test results increase the count by 0.5).
- 5 shows that our method is performing better than the other methods, with the highest area under the ROC curve (AUC).
- S5) supports this result.biorxiv;2024.03.23.586248v1/FIG5F5fig5Fig.
- 5.ROC curve for the performance of DE analysis of peptides on the HeLa-E.coli dataset imputed with different imputation methods with 5% FDR thresholds marked (dots).
- The latter fits with the characteristics of data acquired via MS because high abundance values commonly are proportionally less influenced by measurement noise and are, therefore, assumed to be more reliable [49].
- 5, we find that by filtering at a predicted uncertainty threshold of 0.2 in Fig.
- 6C, we can obtain an AUC of 0.84, compared to an AUC of 0.78 for the PEPerMINT imputation alone (vs.
- 0.68 without imputation, see Supplement).
- This further validates the quality and benefit of the uncertainty predictions given by our method.biorxiv;2024.03.23.586248v1/FIG6F6fig6Fig.
- 6.PEPerMINT’s predicted uncertainty for the imputed values for the HeLa-E.coli dataset (see Supplement for other datasets).
- B: Imputed values ordered by their predicted uncertainty with RMSE computed over different uncertainty quantiles [50].
- The yellow ROC curve (≤ 1.0 uncertainty) is identical to the yellow PEPerMINT ROC curve from Fig.

## Tables

### Table 1.
> Overview of imputation methods used for our benchmark. We capture basic methods, more complex ones, and imputation methods based on deep neural networks representing all three generally considered cat


### Table 2.
> Overview of benchmark datasets and their characteristics including availability via ProteomeXchange, dataset ground-truth category (masked: removed abundance values, DDA/DIA, mixture: mixture of known


## Figure Descriptions

### Fig. 1.
Overview of our PEPerMINT imputation method and our benchmarking framework. (A) Our PEPerMINT imputation model combines both peptide sequence information and abundance values across samples into a latent representation. Structural information is included via a peptide-peptide graph using a graph att

### Fig. 2.
Simplified representation of the architecture of PEPerMINT with input feature representations (grey) and learnable (multilayer) transformations (blue). See Supplement Fig. S1 for a detailed visualization.

### Fig. 3.
A: Sample-wise RMSE of all evaluated imputation methods on all six benchmark datasets with 95% confidence interval error bars (bootstrapped). B: Results for the prostate cancer (A1) dataset stratified by their fraction of missing values over the samples (see supplement for stratified results of othe

### Fig. 4.
Pairwise comparison of different imputation methods by statistical significance test results (see Methods). Colors encode how many of the six evaluated datasets the imputation method given in the row performs significantly better (5% significance level) than the imputation method given in the column

### Fig. 5.
ROC curve for the performance of DE analysis of peptides on the HeLa-E.coli dataset imputed with different imputation methods with 5% FDR thresholds marked (dots). Our PEPerMINT imputation method (yellow) outperforms other methods, having the largest area under the curve (AUC).

### Fig. 6.
PEPerMINT’s predicted uncertainty for the imputed values for the HeLa-E.coli dataset (see Supplement for other datasets). A: Imputed abundance values vs. ground truth colored by predicted uncertainty (low: dark blue, high: yellow). B: Imputed values ordered by their predicted uncertainty with RMSE c

## References
Total references in published paper: 52

### Key References (from published paper)
- Proteome and proteomics: new technologies, new concepts, and new words (, 1998)
- mRNAs, proteins and the emerging principles of gene expression control (, 2020)
- Computational methods for understanding mass spectrometry–based shotgun proteomics data (, 2018)
- Recent advances of data-independent acquisition mass spectrometry-based proteomics (, 2023)
- Accurate proteome-wide label-free quantification by delayed normalization and maximal peptide ratio  (, 2014)
- iPQF: a new peptide-to-protein summarization method using peptide spectra characteristics to improve (, 2016)
- Normalization and missing value imputation for label-free LC-MS analysis (, 2012)
- Accounting for the multiple natures of missing values in label-free quantitative proteomics data set (, 2016)
- A comprehensive evaluation of popular proteomics software workflows for label-free proteome quantifi (, 2017)
- Dealing with missing values in proteomics data (, 2022)
- Proper imputation of missing values in proteomics datasets for differential expression analysis (, 2021)
- Comparative assessment and novel strategy on methods for imputing proteomics data (, 2022)
- A bayesian missing value estimation method for gene expression profile data (, 2003)
- Review, evaluation, and discussion of the challenges of missing value imputation for mass spectromet (, 2015)
- ProJect: a powerful mixed-model missing value imputation method (, 2023)
- Predicting missing proteomics values using machine learning: Filling the gap using transcriptomics a (, 2022)
- DeepImpute: an accurate, fast, and scalable deep neural network method to impute single-cell rna-seq (, 2019)
- Mass spectrometry-based proteomics imputation using self supervised deep learning (, 2023)
- Using deep learning to extrapolate protein expression measurements (, 2020)
- ProtTrans: Toward understanding the language of life through self-supervised learning (, 2021)
- Multiple imputation: a flexible tool for handling missing data (, 2015)
- Graph signal processing, graph neural network and graph learning on biological data: a systematic re (, 2021)
- Graph neural networks for predicting protein functions (, 2019)
- Mobility data improve forecasting of covid-19 incidence trends using graph neural networks (, 2023)
- NAguideR: performing and prioritizing missing value imputations for consistent bottom-up proteomic a (, 2020)
- DEP2: an upgraded comprehensive analysis toolkit for quantitative proteomics data (, 2023)
- MSnbase-an R/Bioconductor package for isobaric tagged mass spectrometry data visualization, processi (, 2012)
- A modular and expandable ecosystem for metabolomics data annotation in R (, 2022)
- A comparative study of evaluating missing value imputation methods in label-free proteomics (, 2021)
- Scikit-learn: Machine learning in python (, 2011)

## Ground Truth Reference
- Figures: 6
- Tables: 2
- References: 52