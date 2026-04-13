# Idea Summary

## Working title
Benchmarking DNA Foundation Models for Genomic and Genetic Tasks

## Core question
How do state-of-the-art DNA foundation language models (DNABERT-2, NT-v2, HyenaDNA, Caduceus-Ph, GROVER) compare in zero-shot embedding quality across diverse genomic and genetic tasks, and what roles do architecture, pre-training data, and embedding pooling strategies play in determining task-specific performance?

## Motivation / gap
- Current evaluations of DNA foundation models are biased because they are conducted after fine-tuning, which introduces confounds from layer selection, hyperparameter tuning, and parameter-efficient fine-tuning methods
- A recent approach using frozen embeddings with an appended CNN partially mitigates fine-tuning bias but was limited in scope to several human genome analysis tasks only
- There is no comprehensive benchmark spanning diverse genomic tasks across multiple species, sequence lengths, and biological feature types (classification, regression, variant effect quantification, chromatin structure)
- The comparative efficacy of embedding pooling methods (summary token, mean token, maximum pooling) in DNA sequence analysis remains understudied despite significant potential impact
- The impact of pre-training data composition (multi-species vs. human-only) on model generalizability lacks controlled experimental evidence

## Core contribution (bullet form)
- Demonstrated that mean token embedding consistently and significantly outperforms summary-token and maximum pooling, with average AUC improvements of 1.4%--8.7% across models and 52 binary classification datasets; mean token pooling was statistically superior (DeLong's test, p < 0.01) in 35--42 out of 52 datasets depending on model
- Benchmarked 5 DNA foundation models across 57 diverse datasets spanning 4 major categories (human genome region classification, multi-species genome region classification, human epigenetic trait classification, multi-species epigenetic trait classification), revealing distinct model-specific strengths
- Showed that general-purpose DNA foundation models (NT-v2: AUC 0.73, Cohen's d 0.88) surprisingly outperform specialized models including Enformer (AUC 0.69, Cohen's d 0.73) in pathogenic variant identification, while specialized models (AlphaGenome: AUC 0.80 for sQTLs, AUC 0.86 for ipaQTLs) dominate QTL prediction tasks
- Provided controlled pre-training experiment showing that re-pretraining HyenaDNA on multi-species data yielded statistically significant improvements in 14 of 49 datasets, with specific gains such as 5mC detection AUC increasing from 0.707 to 0.749 and human vs. worm classification from 0.968 to 0.984
- Evaluated gene expression prediction revealing modest average Pearson correlations (0.114--0.123) for 6k bp inputs, while identifying consistently highly predictable genes (CUTALP: correlation > 0.89 across all 5 short-sequence models)
- Investigated TAD region recognition via NT-v2 attention patterns (1500 TAD-centered vs. 1500 background sequences) finding no evidence of inherent higher-order chromatin structure learning

## Method in brief
We evaluated five DNA foundation models using a zero-shot embedding paradigm to minimize evaluation bias. For each of 57 sequence classification datasets (52 binary, 5 multi-class), DNA sequences were passed through frozen foundation models to generate token-level embeddings from the final layer. Three pooling strategies (sentence-level summary token [CLS/SEP], mean token, maximum pooling) were applied to produce fixed-dimensional sequence representations. A random forest classifier was trained on the resulting embeddings using labeled training data and evaluated on held-out test sets, with AUROC as the primary metric. Statistical significance of performance differences was assessed using one-sided DeLong's test with a threshold of p < 0.01. We also compared against naive Bayes and elastic-net logistic regression as downstream classifiers and a baseline CNN trained directly on sequences.

For gene expression prediction, we used GTEx v8 whole blood data (610 subjects, 21,004 genes) with subject-specific DNA sequences (TSS +/- 3,000 bp for short; TSS +/- 98K bp for long inputs, 768 genes after filtering). Covariate-corrected expression residuals served as prediction targets. Random forest regression was used after demonstrating significantly better performance than XGBoost (all p < 0.001). For variant effect quantification, we constructed paired reference/alternative sequences for pathogenic vs. common SNPs (22,222 pathogenic, 17,374 common for long sequences; 22,239 pathogenic, 17,398 common for short sequences) and for putative causal QTLs from GTEx v8 fine-mapped data (1,896 eQTLs, 540 sQTLs, 116 ipaQTLs, 142 paQTLs) using nested cross-validation with chromosome-based splits across 3 independent test sets.

For the pre-training experiment, HyenaDNA was re-pretrained on DNABERT-2's multi-species dataset (135 species, 6 taxonomic categories) maintaining comparable hyperparameters to the original HyenaDNA-1K checkpoint. TAD recognition analysis used NT-v2 attention matrices averaged across all layers and heads for 1500 TAD-centered sequences (top 5% boundary strength) and 1500 random background sequences of 6000 bp.

## Target venue
Nature Communications
