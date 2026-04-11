## Working title
Comprehensive Benchmarking of scRNA-seq-Based Copy Number Aberration Inference Tools Using Paired Multi-Omics Ground Truth

## Core question
How do the five leading computational tools for inferring copy number aberrations (CNAs) from single-cell RNA-seq data compare in accuracy, and what factors (reference settings, tumor purity, TME cells, tumor type) influence their performance?

## Motivation / gap
- CNAs play crucial roles in cancer initiation and progression, and their characterization at single-cell resolution is important for understanding tumor heterogeneity
- scDNA-seq is ideal for CNA detection but remains costly and low-coverage; scRNA-seq-based inference tools are a practical alternative
- Five popular tools exist (inferCNV, CopyKAT, SCEVAN, Numbat, CaSpER) with fundamentally different approaches (expression-only vs. expression + allele frequency), but no independent comprehensive benchmark had been conducted
- Users lack guidance on which tool to choose for specific tasks (tumor/normal classification, CNA profiling, subclone inference, aneuploidy in non-malignant cells)
- The impact of critical parameters like reference cell selection, tumor purity, and inclusion of tumor microenvironment cells on tool performance was uncharacterized

## Core contribution (bullet form)
- Benchmarked 5 tools across 4 evaluation criteria using paired scRNA-seq/scDNA-seq multi-omics ground truth from 8 CRC samples, 2 ALL samples, 1 glioma, 1 neuroendocrine tumor, and cell lines
- Numbat outperformed other tools across most evaluation criteria; CopyKAT was best when only expression matrix was available as input
- SCEVAN achieved the best performance in clonal breakpoint detection
- Numbat showed high sensitivity in copy number neutral LOH (cnLOH) detection, though with lower precision (false positives often from copy number deletions)
- Demonstrated that expression-based methods are more susceptible to tumor purity effects, and that including TME cells can improve performance
- Provided practical parameter optimization recommendations for each tool

## Method in brief
The benchmark used single-cell multi-omics datasets where DNA and RNA were profiled from the same cells, with CNAs from scDNA-seq serving as ground truth. Datasets included 8 colorectal cancer samples, 2 acute lymphoblastic leukemia samples, 1 glioma, 1 neuroendocrine tumor, the NPC43 cell line, and HUVEC cell line. Five tools were evaluated: expression-only methods (inferCNV using corrected moving averages, CopyKAT using integrative Bayesian segmentation, SCEVAN using multi-channel segmentation) and expression + allele methods (Numbat using haplotype-aware HMM with population-derived haplotypes, CaSpER using multiscale signal-processing with allelic shifts).

Performance was assessed across four tasks: (1) tumor vs. normal cell classification (F1 scores), (2) CNA profile accuracy (Pearson correlation between inferred and ground-truth profiles), (3) tumor subclone inference (comparison of clonal structures from scDNA and scRNA), and (4) aneuploidy detection in non-malignant cells. Additional analyses examined the impact of reference settings (specified vs. unspecified normal cells, one-pass vs. two-pass inferCNV), tumor purity levels, inclusion of TME cells, and sequencing depth on tool performance.

## Target venue
Briefings in Bioinformatics
