# Experimental Log: RNAseqCovarImpute: a multiple imputation procedure that outperforms complete case and single imputation differential expression analysis

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsMultiple imputation and differential expression analysis in RNAseqCovarImpute packageThe RNAseqCovarImpute package implements multiple imputation of missing covariates and differential gene expression analysis by 1) randomly binning genes into smaller groups, 2) creating M imputed datasets se
- An overview of how the method would be applied to a study measuring expression for 10,000 genes in 500 individuals/observations is shown in Figure 1.biorxiv;2023.05.11.540260v1/FIG1F1fig1Figure 1:Overview of Multiple Imputation Method Legend: A) Starting with a matrix of counts for 10,000 genes acro
- B) Separately within each bin, create M imputed datasets (Imp1 – Impm) using mice function.
- Simulations were conducted using 1) real covariate and real RNA-seq data from 1,044 individuals, 2) real covariate data and synthetic RNA-seq data with known signal, and 3) synthetic covariate data with known confounding structure and synthetic RNA-seq data with known signal (see methods for details
- Genes significantly associated with the predictor of interest at FDR <0.05 in these full data models were defined as true differentially expressed genes (DEGs).
- We explored scenarios with various levels of missing data ranging from 5-55% of participants having at least one missing data point, and under two missingness mechanisms: missing completely at random (MCAR) and missing at random (MAR).
- Missingness was simulated using the ampute function from the mice package (14).
- CC analyses dropped any individual with at least one missing data point, while SI imputed missing data using the missForest package (15).
- We report the average bias per gene per missingness scenario across all 10 simulations.Simulation #1: real covariates and real countsThe full data model uncovered 2,453 true DEGs associated with the predictor of interest while controlling for covariates.
- When simulated covariate missingness was MCAR, both imputation methods identified more true DEGs than CC (Figure 2A).
- RNAseqCovarImpute identified a larger percent of true DEGs than SI across all levels of missingness (range = 95.6-98.5% and 56.6-90.7%, respectively).
- RNAseqCovarImpute, SI, and CC methods performed similarly with respect to FDR (range = 2.9-13.8%, 1.9-14.8%, and 5.3-12.8%, respectively).
- Bias was more tightly centered around zero for RNAseqCovarImpute with respect to all genes (Figure 2B) and when only the 2,453 true DEGs were included (Figure 2C).biorxiv;2023.05.11.540260v1/FIG2F2fig2Figure 2:Simulation #1: Real Covariates and Real CountsLegend: Performance of complete-case, RNAseq
- Bias for all genes shown with one point per gene (B, E), while bias for true DEGs shown with box (median and interquartile range) and whisker (1.5* interquartile range) plots (C, F).When data were MAR, both imputation methods identified more true DEGs and fewer false positives compared to CC (Figure
- Again, RNAseqCovarImpute identified a larger percent of true DEGs than SI across all levels of missingness (range = 90.3-97.4% and 55.7-77.6%, respectively).
- While RNAseqCovarImpute and SI performed similarly with respect to FDR (range = 2.0-8.0% and 1.4-12.2%, respectively), FDR for CC was substantially higher (11.4-18.5%; Figure 2D).
- Again, bias was more tightly centered around zero for RNAseqCovarImpute with respect to all genes (Figure 2E) and when only true DEGs were included (Figure 2F).Simulation #2: real covariates and synthetic countsRNA-seq data were modified to add known signal using the seqgendiff package (16).
- As an initial diagnostic, we confirmed that the coefficients for each gene estimated from the limma-voom pipeline on this synthetic count table with no missingness closely matched our user defined coefficients (Supplemental Figure 1).
- In the set of simulations with a null gene association rate of 82.5% and an MCAR missingness mechanism, RNAseqCovarImpute identified the highest percent of true DEGs, followed sequentially by SI and CC (range = 96.8-99.1%, 78.9-95.9%, and 58.2-92.9%, respectively; Figure 3A).
- With respect to FDR, RNAseqCovarImpute and SI performed similarly (range 1.4-6.1% and 1.4-7.6%, respectively), while higher FDRs were observed for CC (range = 3.0-8.0%; Figure 3A).
- Bias was more tightly centered around zero for RNAseqCovarImpute compared to SI and CC (Figure 3B,C) Patterns were similar when data were MAR with respect to error (RNAseqCovarImpute, SI, and CC percent true DEGs ranges = 94.0-98.2%, 77.6-89.6%, and 61.1-93.2%, and FDR ranges = 0.9-3.9%, 1.2-7.7%, a
- Bias for all genes shown with one point per gene (B, E), while bias for true DEGs shown with box (median and interquartile range) and whisker (1.5* interquartile range) plots (C, F).All three methods performed slightly better in our sensitivity analysis with a null gene association rate of 50% rathe
- In general, RNAseqCovarImpute performed better than SI, and SI performed better than CC with respect to identifying true DEGs, limiting FDR, and limiting bias of true DEG coefficients under both MCAR (Figure 4A-C) and MAR (Figure 4D-F) missingness mechanisms.biorxiv;2023.05.11.540260v1/FIG4F4fig4Fig
- Bias for all genes shown with one point per gene (B, E), while bias for true DEGs shown with box (median and interquartile range) and whisker (1.5* interquartile range) plots (C, F).Simulation #3: synthetic covariates and synthetic countsSynthetic covariates were generated with a goal of V1 (the pre
- In general, RNAseqCovarImpute was the best performing method at identifying true DEGs and limiting FDR across all sample sizes (Figure 5).
- Moreover, across all missingness mechanisms, sample sizes, and levels of missingness, bias was more tightly centered around 0 for RNAseqCovarImpute compared with CC and SI methods with respect to all genes (Figure 6) and when only true DEGs were included (Figure 7).
- In sensitivity analyses exploring different correlations of V1 with V2-V5, RNAseqCovarImpute remained the best performer in general (Supplemental Figure 3).
- However, when covariate correlations with V1 were set to 40%, SI identified slightly more true positives than RNAseqCovarImpute, but at the cost of substantially higher FDR (FDR>60% in one instance; Supplemental Figure 3B).biorxiv;2023.05.11.540260v1/FIG5F5fig5Figure 5:Simulation #3: Synthetic Covar
- Mean ± standard error shown for false discovery rate (red) and percent of true positives identified (black) for MCAR (A) and MAR (B) missingness mechanisms.biorxiv;2023.05.11.540260v1/FIG6F6fig6Figure 6:Simulation #3: Synthetic Covariates and Synthetic Counts BiasLegend: Performance of complete-case
- Bias for all genes shown with one point per gene for MCAR (A) and MAR (B) missingness mechanisms.biorxiv;2023.05.11.540260v1/FIG7F7fig7Figure 7:Simulation #3: Synthetic Covariates and Synthetic Counts BiasLegend: Performance of complete-case, RNAseqCovarImpute, and single imputation analyses on ten 
- Bias for true DEGs shown with box (median and interquartile range) and whisker (1.5* interquartile range) plots for MCAR (A) and MAR (B) missingness mechanisms.Application of RNAseqCovarImpute in analysis of maternal age and placental transcriptomeTo demonstrate how RNAseqCovarImpute can implement m
- This analysis examined the association of maternal age with the placental transcriptome while controlling for 10 covariates including potential confounders, mediators, and precision variables.
- The causal relationships among these variables are illustrated in Figure 8.biorxiv;2023.05.11.540260v1/FIG8F8fig8Figure 8:Maternal Age to Placental Transcriptome Directed Acyclic GraphLegend: Conceptual model of association between maternal age (predictor) and the placental transcriptome (outcome).
- Precision variables could affect the outcome but have no clear casual effect on the predictor.Among 1,045 individuals included in this analysis, 6% (61) were missing data for at least one of the 10 covariates.
- In the CC, SI, and RNAseqCovarImpute MI analyses, maternal age was associated with 575, 214, and 382 DEGs, respectively (Figure 9A).
- The CC and SI analyses uncovered 96% (368) and 56% (214) of the significant DEGs from the MI method, respectively, while there were 30 DEGs exclusive to MI (Figure 9A).
- Although there were some differences, genes ranked from lowest to highest P-Value followed similar orders between the methods (Figure 9B).
- Many of the top DEGs, according to their significance and fold-change magnitude (Figure 9C-E), play roles in inflammatory processes and the immune response.
- S100A12 and S100A8 are pro-inflammatory calcium-, zinc- and copper-binding proteins, CXCL8 (IL-8) and IL1R2 are pro-inflammatory cytokines/cytokine receptors, SAA1 and CASC19 are known to be expressed in response to inflammation, while LILRA5, a leukocyte receptor gene, may play a role in triggering
- P-Value rankings for each method for the top 10 genes with the lowest P-Values from the multiple imputation analysis (B).
- Log2-adjusted fold-changes (LogFCs) shown for each one year increase in maternal age.Horizontal and vertical lines at P = 0.05 and LogFC ± 0.04, respectively.
- HGNC gene symbols shown for significant genes with false discovery rate adjusted P-value (P-adj) <0.05 and LogFC beyond 0.04 cutoff.

## Figure Descriptions

### Figure 1:
Overview of Multiple Imputation Method Legend: A) Starting with a matrix of counts for 10,000 genes across 500 observations, create 200 bins of 50 genes (default = 1 gene per 10 observations). B) Separately within each bin, create M imputed datasets (Imp1 – Impm) using mice function. Along with cova

### Figure 2:
Simulation #1: Real Covariates and Real CountsLegend: Performance of complete-case, RNAseqCovarImpute, and single imputation analyses on ten datasets with simulated missingness per missingness mechanism and level of missingness versus the full data differential expression model on the real covariate

### Figure 3:
Simulation #2: Real Covariates and Synthetic Counts with 82.5% Null Gene RateLegend: Performance of complete-case, RNAseqCovarImpute, and single imputation analyses on ten datasets with simulated missingness per missingness mechanism and level of missingness versus the full data differential express

### Figure 4:
Simulation #2: Real Covariates and Synthetic Counts with 50% Null Gene RateLegend: Performance of complete-case, RNAseqCovarImpute, and single imputation analyses on ten datasets with simulated missingness per missingness mechanism and level of missingness versus the full data differential expressio

### Figure 5:
Simulation #3: Synthetic Covariates and Synthetic Counts ErrorLegend: Performance of complete-case, RNAseqCovarImpute, and single imputation analyses on ten datasets with simulated missingness per missingness mechanism, level of missingness, and sample size versus the full data differential expressi

### Figure 6:
Simulation #3: Synthetic Covariates and Synthetic Counts BiasLegend: Performance of complete-case, RNAseqCovarImpute, and single imputation analyses on ten datasets with simulated missingness per missingness mechanism and level of missingness versus the full data differential expression model on the

### Figure 7:
Simulation #3: Synthetic Covariates and Synthetic Counts BiasLegend: Performance of complete-case, RNAseqCovarImpute, and single imputation analyses on ten datasets with simulated missingness per missingness mechanism and level of missingness versus the full data differential expression model on the

### Figure 8:
Maternal Age to Placental Transcriptome Directed Acyclic GraphLegend: Conceptual model of association between maternal age (predictor) and the placental transcriptome (outcome). Confounders are upstream causes of both the predictor and outcome. Mediators are on the causal pathway between the predict

### Figure 9:
Associations between Maternal Age and the Placental TranscriptomeLegend: Venn diagram depicts shared and distinct differentially expressed genes for each method (A). P-Value rankings for each method for the top 10 genes with the lowest P-Values from the multiple imputation analysis (B). Volcano plot

## References
Total references in published paper: 31

### Key References (from published paper)
- Applied missing data analysis with SPSS and (R) Studio (, 2019)
- Coming of age: ten years of next-generation sequencing technologies (, 2016)
- Cohort profile: the ECHO prenatal and early childhood pathways to health consortium (ECHO-PATHWAYS) (, 2022)
- Metal mixtures modeling identifies birth weight-associated gene networks in the placentas of childre (, 2023)
- Regression with missing X’s: a review (, 1992)
- Methods for Dealing With Missing Covariate Data in Epigenome-Wide Association Studies (, 2019)
- Imputation of missing covariate values in epigenome-wide analysis of DNA methylation data (, 2016)
- voom: Precision weights unlock linear model analysis tools for RNA-seq read counts (, 2014)
- limma powers differential expression analyses for RNA-sequencing and microarray studies (, 2015)
- Linear models and empirical bayes methods for assessing differential expression in microarray experi (, 2004)
- Controlling the false discovery rate: a practical and powerful approach to multiple testing (, 1995)
- mice: Multivariate imputation by chained equations in R (, 2011)
- MissForest—non-parametric missing value imputation for mixed-type data (, 2012)
- Data-based RNA-seq simulations by binomial thinning (, 2020)
- Validation of a DNA methylation microarray for 850,000 CpG sites of the human genome enriched in enh (, 2016)
- A systematic evaluation of single-cell RNA-sequencing imputation methods (, 2020)
- Framework for the treatment and reporting of missing data in observational studies: The Treatment An (, 2021)
- The use and reporting of multiple imputation in medical research–a review (, 2010)
- The rise of multiple imputation: a review of the reporting and implementation of the method in medic (, 2015)
- Prenatal exposure to particulate matter and placental gene expression (, 2022)
- A comprehensive assessment of associations between prenatal phthalate exposure and the placental tra (, 2021)
- Placental Transcriptomic Signatures of Prenatal Exposure to Hydroxy-Polycyclic Aromatic Hydrocarbons (, 2023)
- Maternal age at birth and child attention-deficit hyperactivity disorder: causal association or fami (, 2023)
- Parental age and attention-deficit/hyperactivity disorder (ADHD) (, 2017)
- Maternal age at childbirth and risk for ADHD in offspring: a population-based cohort study (, 2014)
- Camera: a competitive gene set test accounting for inter-gene correlation (, 2012)
- GAGE: generally applicable gene set enrichment for pathway analysis (, 2009)
- Miscellanea. Small-sample degrees of freedom with multiple imputation (, 1999)
- Placental transcriptomic signatures of spontaneous preterm birth (, 2023)
- Biomarkers of exposure to new and emerging tobacco delivery products (, 2017)

## Ground Truth Reference
- Figures: 9
- Tables: 0
- References: 31