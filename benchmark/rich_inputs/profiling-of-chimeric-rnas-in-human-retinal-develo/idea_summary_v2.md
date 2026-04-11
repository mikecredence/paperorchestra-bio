# Idea Summary

## Working title
Profiling of Chimeric RNAs in Human Retinal Development with Retinal Organoids

## Core question
What is the landscape of chimeric RNAs during human retinal development, and does the chimeric RNA CTNNBIP1-CLSTN1 (CTCL) -- previously implicated in cerebral development -- also play a key role in retinogenesis?

## Motivation / gap
- Chimeric RNAs regulate stem/progenitor cell differentiation and CNS development, but their role in retinal development is completely unknown
- Retina is part of the CNS, yet no study has profiled chimeric RNAs across retinal developmental stages
- CTCL downregulation causes premature neuronal differentiation in cerebral organoids, but whether it functions in retinogenesis is untested
- Obtaining normal human retinal tissue is difficult; retinal organoids (ROs) from hESCs provide a model system spanning D0-D120
- The chimeric RNA transcriptome of the developing retina has not been catalogued

## Core contribution (bullet form)
- Presented the first expression atlas of chimeric RNAs throughout human retinal organoid development from D0 to D120 across 22 RO samples at 8 stages
- Found that intra-chromosomal chimeric RNAs increase with RO development (r2 = 0.93, p = 0.00076, Pearson correlation), while inter-chromosomal chimeric RNAs do not show this trend
- Identified that 61.9% of chimeric RNAs were formed between two protein-coding genes, with "In frame" chimeric RNAs accounting for 11.2% of events
- Confirmed four isoforms of CTCL in retinal organoids via PCR and Sanger sequencing
- Demonstrated that CTCL knockdown obstructed RO differentiation but promoted RPE differentiation, with thinner outer layers visible at D60
- Transcriptomic analysis of CTCL-knockdown organoids revealed alterations in EMT, extracellular matrix organization, and epithelial cell differentiation pathways rather than the expected Wnt signaling changes

## Method in brief
Human embryonic stem cell-derived retinal organoids (ROs) were cultured following established protocols from D0 to D120. Total RNA from 22 organoid samples spanning 8 developmental stages was sequenced using VAHTS Universal V6 RNA-seq Library Prep Kit for Illumina. Chimeric RNAs were identified using FusionCatcher software, with a stringency filter requiring at least one spanning unique read. Expression levels were quantified as log(spanning unique reads / total reads * 10,000,000). Parental gene expression was analyzed by mapping to hg38 with Hisat2 and assembling transcripts with featureCounts.

Loss-of-function experiments used a CRX-tdTomato hES reporter line. Lentiviral shRNA targeting CTCL was transduced into ROs at D12, with scramble shRNA as control. Knockdown efficiency was confirmed 48-72 hours post-infection. Organoids were collected at D60 for immunohistochemistry (markers: CRX, OTX2, VSX2, RCVRN, MITF, RPE65, PAX6), RNA sequencing, differential expression analysis, and GSEA using the R package clusterProfiler. Sequence motifs around fusion sites were analyzed with the seqLogo R package.

## Target venue
eLife
