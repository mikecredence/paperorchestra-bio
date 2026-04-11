# Idea Summary: Benchmarking DNA Foundation Models for Genomic and Genetic Tasks

## Working title
Benchmarking DNA Foundation Models for Genomic and Genetic Tasks

## Core question
How do current DNA foundation models (DNABERT-2, NT-v2, HyenaDNA, Caduceus-Ph, GROVER) compare on a level playing field across diverse genomic tasks when we strip away fine-tuning confounds and evaluate purely on the quality of their zero-shot embeddings?

## Motivation / gap
- Existing evaluations of DNA foundation models are biased because they rely on fine-tuning, which introduces confounds from layer selection, hyperparameter tuning, and parameter-efficient methods like LoRA
- A recent embedding-based benchmark (BEND) attempted to address fine-tuning bias by freezing model weights and appending a CNN, but its scope was limited to a handful of human genome tasks
- No study has systematically compared embedding pooling strategies (summary token vs. mean token vs. max pooling) across models and datasets, despite pooling choice potentially having large effects on downstream performance
- DNA foundation models have not been evaluated on genetic tasks such as variant effect prediction and QTL identification, where specialized genomic models (Enformer, Sei, AlphaGenome) are the current standard
- It remains unclear whether architectural differences (BERT-style bidirectional transformers vs. Hyena convolution vs. Mamba state-space models) or pre-training data composition (single-species vs. multi-species) drive performance differences
- There is no practical guidance for practitioners on which model to select for a given genomic or genetic analysis task

## Core contribution (bullet form)
- Demonstrated that mean token embedding consistently and significantly outperforms summary-token and max pooling across all five models, with AUC improvements ranging from 1.4% (GROVER) to 8.7% (HyenaDNA) on 52 binary classification datasets using DeLong's test at p < 0.01
- Benchmarked five DNA foundation models on 57 sequence classification datasets spanning human genome tasks, multispecies tasks, and epigenetic modification detection, revealing Caduceus-Ph as the top performer for human TFBS prediction and DNABERT-2 as strongest for splice site identification
- Showed that general-purpose DNA foundation models are competitive with specialized models for pathogenic variant identification (NT-v2 achieved AUC 0.73, outperforming Enformer at 0.69), but substantially lag behind track-prediction models for QTL tasks (AlphaGenome reached AUC 0.80 for sQTLs vs. best foundation model at 0.57)
- Evaluated gene expression prediction from zero-shot embeddings, finding modest average correlations (~0.12) for short-sequence models but notable improvement with longer context (HyenaDNA-450K at 0.137 significantly outperformed Enformer at 0.129)
- Conducted a pre-training experiment showing that retraining HyenaDNA on multi-species data improved performance on 14 of 49 datasets, particularly cross-species and epigenetic tasks (5mC detection AUC rose from 0.707 to 0.749)
- Investigated NT-v2 attention patterns for TAD boundary recognition, finding no evidence that the model captures higher-order chromatin organization without fine-tuning

## Method in brief
The benchmark evaluated five DNA foundation models using a zero-shot embedding approach to eliminate fine-tuning bias. For each model, DNA sequences were tokenized and passed through the frozen network to extract token-level embeddings from the final layer. Three output pooling strategies were tested: (1) sentence-level summary token (CLS/SEP), (2) mean of all token embeddings, and (3) element-wise maximum across tokens. The resulting fixed-dimensional sequence representations were fed to a random forest classifier (for classification tasks) or random forest regressor (for gene expression prediction), chosen for its minimal inductive bias and strong generalization.

For sequence classification, the study covered 57 datasets: 52 binary tasks (promoter identification, TFBS prediction, splice site detection, enhancer identification, open chromatin regions, epigenetic modifications across human, yeast, mouse, plant, and bacterial genomes) and 5 multi-class tasks (regulatory region types, splice site types, COVID variants, enhancer strength). Performance was measured by AUROC for binary tasks and accuracy for multi-class, with statistical significance assessed via one-sided DeLong's test at p < 0.01.

For variant effect quantification, the study used an embedding-subtraction approach: the difference between embeddings of reference and alternate allele sequences served as input features. This was evaluated on a pathogenic-vs-common SNP dataset and four QTL tasks (eQTL, sQTL, paQTL, ipaQTL) using nested cross-validation with chromosome-based splits. Results were compared against specialized genomic models (Enformer, Sei, AlphaGenome) that predict functional tracks from sequence. Runtime analysis measured inference time across sequence lengths from 64 to 524,288 nucleotides on an A100 GPU.

## Target venue
Nature Communications
