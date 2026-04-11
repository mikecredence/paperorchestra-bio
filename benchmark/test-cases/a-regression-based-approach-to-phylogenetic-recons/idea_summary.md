# Idea Summary: A regression based approach to phylogenetic reconstruction from multi-sample bulk DNA sequencing of tumors

## Working title
A regression based approach to phylogenetic reconstruction from multi-sample bulk DNA sequencing of tumors

## Core question
AbstractMotivationDNA sequencing of multiple bulk samples from a tumor provides the opportunity to investigate tumor heterogeneity and reconstruct a phylogeny of a patient’s cancer. However, since bulk DNA sequencing of tumor tissue measures thousands of cells from a heterogeneous mixture of distinct sub-populations, accurate reconstruction of the tumor phylogeny requires simultaneous deconvolution of cancer clones and inference of ancestral relationships, leading to a challenging computational 

## Motivation / gap
- 1IntroductionTumor evolution is characterized by the accumulation of somatic genomic alterations that alter the fitness of sub-populations of cells, leading to unregulated growth.
- Over the past ten years, high-coverage DNA sequencing of bulk tumor samples has proven tremendously successful in deciphering this complex evolutionary process [1–3].
- There are now dozens of computational techniques [4–12] to accurately and efficiently identify distinct sub-populations of cells in a tumor sample and reconstruct the evolutionary history, or a phylog
- Application of these techniques can help identify the genomic alterations that drive tumor growth [13, 14].
- Recent studies have demonstrated that intra-tumor heterogeneity is more prevalent than previously reported (reviewed in [15]).

## Core contribution (bullet form)
Extracted from abstract:
AbstractMotivationDNA sequencing of multiple bulk samples from a tumor provides the opportunity to investigate tumor heterogeneity and reconstruct a phylogeny of a patient’s cancer. However, since bulk DNA sequencing of tumor tissue measures thousands of cells from a heterogeneous mixture of distinct sub-populations, accurate reconstruction of the tumor phylogeny requires simultaneous deconvolution of cancer clones and inference of ancestral relationships, leading to a challenging computational problem. Many existing methods for phylogenetic reconstruction from bulk sequencing data do not scale to large datasets, such as recent datasets containing upwards of ninety samples with dozens of distinct sub-populations.ResultsWe develop an approach to reconstruct phylogenetic trees from multi-sample bulk DNA sequencing data by separating the reconstruction problem into two parts: a structured regression problem for a fixed tree 𝒯, and an optimization over tree space. We derive an algorithm for the regression sub-problem by exploiting the unique, combinatorial structure of the matrices appearing within the problem. This algorithm has both asymptotic and empirical improvements over linear programming (LP) approaches to the problem. Using our algorithm for this regression sub-problem, we develop fastBE, a simple method for phylogenetic inference from multi-sample bulk DNA sequencing data. We demonstrate on simulated data with hundreds of samples and upwards of a thousand distinct sub-populations that fastBE outperforms existing approaches in terms of reconstruction accuracy, sample efficiency, and runtime. Owing to its scalability, fastBE also enables phylogenetic reconstruction directly from indvidual mutations without requiring the clustering of mutations into clones. On real data from fourteen B-progenitor acute lymphoblastic leukemia patients, fastBE infers similar phylogenies to the existing, state-of-the-art method, but with fewer violations of a widely used evolutionary constraint and better agreement to the observed mutational frequencies. Finally, we show that on two patient-derived colorectal cancer models, fastBE also infers phylogenies with less violation of a widely used evolutionary constraint compared to existing methods, and leads to distinct interpretations of the intra-tumor heterogeneity.AvailabilityfastBE is implemented in C++ and is available at: github.com/raphael-group/fastBE.

## Method in brief
Methods not available from XML.

## Target venue
PLOS Computational Biology
