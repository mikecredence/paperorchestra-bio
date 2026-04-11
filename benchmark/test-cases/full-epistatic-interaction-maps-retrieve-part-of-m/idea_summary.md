# Idea Summary: Full epistatic interaction maps retrieve part of missing heritability and improve phenotypic prediction

## Working title
Full epistatic interaction maps retrieve part of missing heritability and improve phenotypic prediction

## Core question
AbstractThe first Genome Wide Association Studies (GWAS) shed light on the concept of missing heritability. It constitutes a mystery with transcending consequences from plant to human genetics. This mystery lies in the fact that a large proportion of phenotypes are not explained by unique or simple genomic modifications. One has to invoke genetic interactions among different loci, also known as epistasis, to partly account for it. However, current GWAS statistical models are moderately scalable,

## Motivation / gap


## Core contribution (bullet form)
Extracted from abstract:
AbstractThe first Genome Wide Association Studies (GWAS) shed light on the concept of missing heritability. It constitutes a mystery with transcending consequences from plant to human genetics. This mystery lies in the fact that a large proportion of phenotypes are not explained by unique or simple genomic modifications. One has to invoke genetic interactions among different loci, also known as epistasis, to partly account for it. However, current GWAS statistical models are moderately scalable, very sensitive to False Discovery Rate (FDR) corrections and, even combined with High Performance Computing (HPC), they can take years to evaluate for a full combinatorial epistatic space for a single phenotype. Here we propose a modeling approach, named Next-Gen GWAS (NGG) that evaluates, within hours, >60 billions of single nucleotide polymorphism (SNP) combinatorial first-order interactions, on a reasonable computer power. We first benchmark NGG on state of the art GWAS model results, and applied this to Arabidopsis thaliana providing 2D epistatic maps at gene resolution. We demonstrate on several phenotypes that a large proportion of the missing heritability can i) be retrieved with this modeling approach, ii) indeed lies in epistatic interactions and iii) can be used to improve phenotype prediction.

## Method in brief
METHODSDataArabidopsis dataset corresponds to data issued from the 1001 genome project (13) and kindly provided by Arthur Korte lab. It consists of a genotype matrix above mentioned as genotype or X matrix containing 9124892 SNPs and 1135 ecotypes. For NGG analysis MAF is controlled (0.3<MAF) resulting in a MAFed X’ matrix containing 346094 SNPs for Campos et al. (2021) and between 341067 and 371956 SNPs, for Atwell et al, (2010).SimulationsThe simulations (Fig. 1) are performed on R. Code can be found at (https://github.com/CarluerJB)Computer powerThis work has been performed on a PowerEdge T640 DELL Server, RAM 377 Go, 4 NVIDIA Quadro RTX 6000 (24Go).


## Target venue
Genome Biology
