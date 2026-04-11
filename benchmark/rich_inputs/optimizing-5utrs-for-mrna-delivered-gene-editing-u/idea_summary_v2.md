# Idea Summary

## Working title
Optimizing 5'UTRs for mRNA-Delivered Gene Editing Using Deep Learning

## Core question
Can deep learning models trained on massively parallel reporter assay data be used to design de novo 5'UTR sequences that maximize protein expression from mRNA therapeutics, specifically for mRNA-delivered gene editing enzymes?

## Motivation / gap
- mRNA therapeutics are rapidly advancing (COVID vaccines, protein replacement, cancer immunotherapy) but methods to optimize the primary sequence for increased expression remain underdeveloped
- Most mRNA therapies use 5'UTRs from alpha- and beta-globin genes by default, leaving substantial room for optimization
- UTR effects are difficult to predict because cis-regulatory elements affect multiple molecular processes and interact with cell-type-specific RNA-binding proteins and microRNAs
- Quantitative deep learning models predicting translation from 5'UTR sequence have recently emerged but have not been applied to guide de novo UTR design for therapeutics
- The degree to which 5'UTR performance is conserved across cell types relevant to mRNA therapeutics (T cells, hepatocytes) was unknown
- megaTAL gene editors are well-suited to mRNA delivery due to their compact single-chain design, but optimal 5'UTR sequences for these cargo have not been explored

## Core contribution (bullet form)
- Measured translation efficiency (Mean Ribosome Load) from ~205,000 randomized 5'UTR variants across three cell types (HEK293T, T cells, HepG2) and found MRL highly correlated between cell lines (r2 = 0.837-0.871 between different cell types)
- Demonstrated that Optimus 5-Prime, trained only on HEK293T data, generalizes well to T cells and HepG2 predictions (r2 up to 0.937 on held-out test set)
- Designed de novo 5'UTRs using gradient descent (Fast SeqProp) and generative neural networks (Deep Exploration Networks/DENs), with and without VAE regularization, achieving gene editing efficiencies exceeding 40% for TGFBR2 and 80% for PDCD1 in K562 cells
- Found that designed 5'UTRs matched or exceeded the performance of the top 0.02% of random MPRA library sequences, with one design achieving up to 50% higher TGFBR2 editing than all controls
- Developed a new model, Optimus 5-Prime(25), for fully randomized 25-nt 5'UTRs, capturing effects near the 5' cap including out-of-frame uAUG positional effects and 5'-proximal poly-C/T enhancement
- Showed that editing efficiency is correlated between cell types and gene targets, though the single best-performing UTR was specific to one cargo and cell type

## Method in brief
The study uses Massively Parallel Reporter Assays (MPRAs) based on polysome profiling. In vitro transcribed (IVT) mRNA libraries with either a 50-nt fully random region (preceded by a 25-nt constant segment) or a 25-nt fully random region (preceded only by GGG for T7 transcription) were transfected into HEK293T, T cells, and HepG2 cells. After 8 hours of incubation with cycloheximide, cell lysates were fractionated on sucrose gradients to separate polysome fractions, and each fraction was sequenced. Mean Ribosome Load (MRL) was calculated for each 5'UTR by multiplying normalized read counts by corresponding ribosome numbers. After filtering for sequences with at least 100 reads across all datasets, approximately 204,803 common variants were obtained.

For model-based design, the previously developed Optimus 5-Prime convolutional neural network was used as the predictive oracle. Two design algorithms were employed: Fast SeqProp (gradient-based sequence optimization) and Deep Exploration Networks (DENs, generative neural networks that take random latent vectors and output optimized sequences). Both approaches were tested with and without Variational AutoEncoder (VAE) regularization to constrain designs to the distribution of natural-like sequences. Designed 5'UTRs were then experimentally validated by incorporating them into mRNA encoding megaTAL gene editing enzymes targeting TGFBR2 and PDCD1 genes, transfecting into K562 and Jurkat cells, and measuring gene editing efficiency via flow cytometry for surface protein knockout.

## Target venue
Nature Communications
