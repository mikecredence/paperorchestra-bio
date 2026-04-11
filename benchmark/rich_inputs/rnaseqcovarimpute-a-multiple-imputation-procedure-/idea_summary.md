# Idea Summary: RNAseqCovarImpute: a multiple imputation procedure that outperforms complete case and single imputation differential expression analysis

## Working title
RNAseqCovarImpute: a multiple imputation procedure that outperforms complete case and single imputation differential expression analysis

## Core question
AbstractMissing covariate data is a common problem that has not been addressed in observational studies of gene expression. Here we present a multiple imputation (MI) method that accommodates high dimensional transcriptomic data by binning genes, creating separate MI datasets and differential expression models within each bin, and pooling results with Rubin’s rules. Simulation studies using real and synthetic data show that this method outperforms complete case and single imputation analyses at 

## Motivation / gap


## Core contribution (bullet form)
Extracted from abstract:
AbstractMissing covariate data is a common problem that has not been addressed in observational studies of gene expression. Here we present a multiple imputation (MI) method that accommodates high dimensional transcriptomic data by binning genes, creating separate MI datasets and differential expression models within each bin, and pooling results with Rubin’s rules. Simulation studies using real and synthetic data show that this method outperforms complete case and single imputation analyses at uncovering true positive differentially expressed genes, limiting false discovery rates, and minimizing bias. This method is easily implemented via an R package, “RNAseqCovarImpute” that integrates with the limma-voom pipeline.

## Method in brief
Materials and MethodsMultiple imputation and differential expression analysis in RNAseqCovarImpute package Binning genesThe default is approximately 1 gene per 10 individuals in the study, but the user can specify a different ratio. For example, in a study with 500 participants and 10,000 genes, 200 bins of 50 genes would be created using the default ratio. When the total number of genes is not divisible by the bin size, the method flexibly creates bins of two different sizes. For example, if the same hypothetical study included 10,001 genes, 199 bins of 50 and 1 bin of 51 genes would be created. The order of the features (e.g., ENSEMBL gene identifiers) should be randomized before binning.Data imputationData are imputed using the mice R package with its default predictive modeling methods, which are predictive mean matching, logistic regression, polytomous regression, and proportional odds modeling for continuous, binary, categorical, and unordered variables, respectively (14). The user may specify “M”, the number of imputed datasets, and “maxit”, the number of iterations for each imputation. M imputed datasets are created separately for each gene bin, where the imputation predictor matrix includes all covariates along with the log-CPM for all the genes in a particular bin. Thus, each gene bin contains M sets of imputed data.Differential expression analysisDEGs are determined via the limma-voom pipeline. This procedure fits weighted linear models for each gene that take into

## Target venue
Genome Biology
