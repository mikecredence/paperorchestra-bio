## Working title

Benchmarking DNA foundation models across genomic and genetic tasks

## Core question

How do current DNA foundation models compare on diverse genomic and genetic tasks, and what embedding strategies yield the best performance?

## Motivation / gap

- DNA foundation models (DNABERT-2, Nucleotide Transformer V2, HyenaDNA, Caduceus-Ph, GROVER) are rapidly emerging but lack comprehensive, unbiased evaluation
- It is unclear which model excels at which task, or whether general-purpose models can match specialized ones
- The effect of different pooling/embedding strategies (mean token, CLS, etc.) on downstream performance has not been systematically studied

## Core contribution

- Present a comprehensive benchmark of five DNA foundation models across sequence classification, gene expression prediction, variant effect quantification, and TAD region recognition
- Show that mean token embedding consistently and significantly outperforms other pooling strategies for sequence classification
- Reveal that general-purpose DNA foundation models are competitive for pathogenic variant identification but less effective for gene expression prediction and causal QTL identification compared to specialized models
- Provide a framework for model selection depending on the genomic task

## Method in brief

- Zero-shot embeddings from five pre-trained DNA foundation models
- Tasks: sequence classification, gene expression prediction, variant effect quantification, TAD boundary recognition
- Pooling strategy comparison: mean token, CLS token, max pooling, etc.
- Comparison against task-specific specialized models as baselines
- Standardized evaluation metrics per task (AUROC, Spearman correlation, etc.)

## Target venue

Nature Communications
