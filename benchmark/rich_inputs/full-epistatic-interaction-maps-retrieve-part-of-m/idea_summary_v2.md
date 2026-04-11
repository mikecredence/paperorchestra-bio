# Idea Summary

## Working title
Full Epistatic Interaction Maps Retrieve Part of Missing Heritability and Improve Phenotypic Prediction

## Core question
Can a scalable computational approach exhaustively evaluate all pairwise SNP epistatic interactions across the genome, retrieve the missing heritability that standard single-locus GWAS cannot explain, and improve phenotype prediction using the recovered epistatic signals?

## Motivation / gap
- Standard GWAS approaches explain only a fraction of the heritable variation for most traits, a long-standing problem known as missing heritability
- Epistasis (gene-gene interactions) is widely suspected to account for a substantial portion of this missing heritability, but evaluating the full combinatorial space is computationally prohibitive
- Current GWAS statistical models for epistasis are moderately scalable, highly sensitive to false discovery rate (FDR) corrections, and can take years to compute for a single phenotype even with high-performance computing
- Existing mixed model methods (e.g., EMMA) handle single-locus effects well but cannot be extended to the full pairwise interaction space at genome scale
- No existing framework provides 2D epistatic maps at gene resolution for real organisms within a practical compute time
- Machine learning models for phenotype prediction have not been systematically compared using inputs derived from epistatic interaction signals vs. single-locus signals alone

## Core contribution (bullet form)
- Developed Next-Gen GWAS (NGG), a GPU-accelerated framework that evaluates over 60 billion pairwise SNP interactions within hours on a single server with 4 GPUs
- Benchmarked NGG against the standard EMMA mixed model on Arabidopsis thaliana data and showed largely concordant 1D-GWAS signals, including recovery of the FLC locus for flowering time
- Generated 2D epistatic interaction maps at gene resolution for multiple phenotypes, evaluating 61.2 billion SNP combinations
- Demonstrated that epistatic interactions substantially increase explained heritability (adjusted R-squared) beyond what 1D-GWAS signals provide alone, using PCA-based analysis
- Showed that SNP markers from epistatic signals improve machine learning phenotype prediction across multiple ML models (SVM, RF, DNN, Gaussian processes, LASSO, Elastic-Net) for 18 elemental concentration phenotypes in Arabidopsis
- Applied the method to both Atwell et al. (2010) and Campos et al. (2021) Arabidopsis datasets, covering flowering time and ionomic phenotypes

## Method in brief
NGG operates on genotype matrices from the 1001 Genomes Arabidopsis project. The genotype matrix (X) contains up to 9,124,892 SNPs across 1,135 ecotypes. After minor allele frequency (MAF) filtering at MAF > 0.3, the working matrix is reduced to roughly 341,000-372,000 SNPs. For each SNP pair, NGG estimates the effect (theta) on the phenotype using a regression-like approach, with the Col-0 reference genome as the baseline. A bootstrap procedure identifies signals emerging from noise. The diagonal of the resulting 2D map contains single-SNP effects (equivalent to 1D-GWAS), while off-diagonal elements represent pairwise epistatic interactions.

The full pairwise computation is accelerated using GPU parallelism on 4 NVIDIA Quadro RTX 6000 cards (24 GB each) on a PowerEdge T640 server with 377 GB RAM. For heritability estimation, PCA is applied to the interaction signals, and adjusted R-squared is measured with increasing numbers of principal components, comparing 1D-only signals (diagonal) against 1D + 2D signals (diagonal + off-diagonal triangle). Machine learning prediction uses six different model types trained on varying numbers of SNP features (50, 100, 500, 1000) derived from either 1D-only or 1D+2D signals, with phenotype discretization into 3 or 5 classes.

## Target venue
Genome Biology
