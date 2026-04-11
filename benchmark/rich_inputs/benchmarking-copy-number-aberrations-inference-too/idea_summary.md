# Idea Summary: Benchmarking copy number aberrations inference tools using single-cell multi-omics datasets

## Working title
Benchmarking copy number aberrations inference tools using single-cell multi-omics datasets

## Core question
AbstractCopy number aberrations (CNAs) are an important type of genomic variation which play a crucial role in the initiation and progression of cancer. With the explosion of single-cell RNA sequencing (scRNA-seq), several computational methods have been developed to infer CNAs from scRNA-seq studies. However, to date, no independent studies have comprehensively benchmarked their performance. Herein, we evaluated five state-of-the-art methods based on their performance in tumor vs normal cell cl

## Motivation / gap


## Core contribution (bullet form)
Extracted from abstract:
AbstractCopy number aberrations (CNAs) are an important type of genomic variation which play a crucial role in the initiation and progression of cancer. With the explosion of single-cell RNA sequencing (scRNA-seq), several computational methods have been developed to infer CNAs from scRNA-seq studies. However, to date, no independent studies have comprehensively benchmarked their performance. Herein, we evaluated five state-of-the-art methods based on their performance in tumor vs normal cell classification, CNAs profile accuracy, tumor subclone inference and aneuploidy identification in non-malignant cells. Our results showed that Numbat outperformed others across most evaluation criteria, while CopyKAT excelled in scenarios when expression matrix alone was used as input. In specific tasks, SCEVAN showed the best performance in clonal breakpoint detection and Numbat showed high sensitivity in copy number neutral LOH (cnLOH) detection. Additionally, we investigated how referencing settings, inclusion of tumor microenvironment cells, tumor type, and tumor purity impact the performance of these tools. This study provides a valuable guideline for researchers in selecting the appropriate methods for their datasets.

## Method in brief
MethodsBenchmark datasets collectionThe CRC dataset was sourced from the study by Zhou et al.[22]. Both raw FASTQ files and processed gene expression count matrices for scRNA-seq were downloaded from the Genome Sequence Archive of the National Genomics Data Center (NGDC) with the accession number HRA000201. The glioma, NPC43 and HUVEC cell line data were obtained from the study by Yu et al[24] with gene expression count matrices for scRNA-seq available from the NCBI Gene Expression Omnibus under accession number GSE185269. The Neuro dataset was sourced from the study by Cui et al[26]. Both raw FASTQ files and processed gene expression count matrices for scRNA-seq were downloaded from the Genome Sequence Archive of the National Genomics Data Center (NGDC) with the accession number PRJCA002946. The GX109 dataset was sourced from the study by Huang et al[31]. Raw FASTQ data were aligned to the genome to generate BAM files, following the processing methods described in the original articles by Zhou et al, Yu et al and Cui.[22, 24, 26]. Additionally, the processed count matrix for two acute lymphoblastic leukemia samples was obtained from the study by Zachariadis et al with accession number GSE144296[23]. Chromosomal copy number variations in scDNA-seq data and cell type annotations for all these datasets was acquired directly from the authors.Workflows for inferCNV[16], CopyKAT[17], SCEVAN[18], Numbat[19] and CaSpER[20] InferCNVIt utilizes a corrected moving average technique to 

## Target venue
Briefings in Bioinformatics
