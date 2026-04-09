# Idea Summary: Benchmarking DNA Foundation Models

## Working title
Benchmarking DNA Foundation Models for Genomic Sequence Classification

## Core question
How do recent DNA foundation language models compare when used as zero-shot
feature extractors across diverse genomic tasks? No one has done a systematic,
head-to-head, apples-to-apples comparison.

## Motivation / gap
- Multiple DNA foundation models released in 2023-2024 (DNABERT-2, Nucleotide
  Transformer v2, HyenaDNA, Caduceus-Ph, GROVER) with different architectures,
  training data, parameter counts
- Each paper benchmarks on its own cherry-picked tasks — no unified evaluation exists
- Practitioners don't know which model to use for which task
- Nobody has systematically studied embedding pooling strategies (summary token
  vs mean vs max) for these models
- Unclear whether general-purpose DNA models can replace specialized models
  (Enformer, Sei, AlphaGenome) for variant effect and gene expression tasks

## Core contribution (bullet form)
- Unified benchmark: 5 models, 57 classification datasets, 4 task categories
  (sequence classification, gene expression, variant effect, TAD recognition)
- Discovery that mean token pooling consistently beats default summary token
  pooling (4-9% AUC improvement), reducing inter-model performance variance
- Task-specific model rankings: no single winner — Caduceus-Ph best for human
  genome classification, DNABERT-2 for splice sites and yeast epigenetics,
  NT-v2 for pathogenic variant detection, HyenaDNA for long sequences and plant genomes
- Finding that general DNA foundation models fail at QTL prediction where
  specialized models (AlphaGenome, Enformer) dominate
- Controlled experiment showing multi-species pre-training data improves
  cross-species transfer

## Method in brief
- Freeze all model weights (zero-shot)
- Extract embeddings for each sequence
- Train random forest classifier on embeddings (5-fold CV with hyperparameter optimization)
- Compare using AUC (binary), accuracy (multi-class), Pearson correlation (regression)
- Statistical testing: DeLong's test for AUC, paired Wilcoxon signed-rank

## Target venue
Nature Communications
