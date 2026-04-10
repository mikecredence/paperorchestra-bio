# Experimental Log -- DNA Foundation Model Benchmarking

## 2024-02-10 -- Sequence classification (zero-shot embeddings, mean token pooling)

AUROC on held-out test sets for binary/multiclass sequence classification tasks.

| Model | Promoter detection (AUROC) | Enhancer classification (AUROC) | Splice site prediction (AUROC) | Avg AUROC |
|-------|--------------------------|-------------------------------|-------------------------------|----------|
| DNABERT-2 | 0.92 | 0.88 | 0.90 | 0.900 |
| Nucleotide Transformer V2 | 0.91 | 0.87 | 0.89 | 0.890 |
| HyenaDNA | 0.88 | 0.84 | 0.86 | 0.860 |
| Caduceus-Ph | 0.87 | 0.83 | 0.85 | 0.850 |
| GROVER | 0.89 | 0.86 | 0.87 | 0.873 |

DNABERT-2 edges out others on classification tasks with mean token embedding.

## 2024-02-28 -- Pooling strategy comparison (sequence classification, averaged across models)

| Pooling strategy | Avg AUROC | Improvement over CLS |
|-----------------|----------|---------------------|
| Mean token | 0.875 | +0.042 |
| CLS token | 0.833 | baseline |
| Max pooling | 0.848 | +0.015 |
| First+Last concat | 0.841 | +0.008 |

Mean token embedding consistently and significantly outperforms other strategies.

## 2024-03-15 -- Gene expression prediction (Spearman correlation)

| Model | Spearman rho | Specialized baseline |
|-------|-------------|---------------------|
| DNABERT-2 | 0.45 | -- |
| Nucleotide Transformer V2 | 0.43 | -- |
| HyenaDNA | 0.40 | -- |
| Caduceus-Ph | 0.38 | -- |
| GROVER | 0.42 | -- |
| Enformer (specialized) | 0.78 | 0.78 |
| Xpresso (specialized) | 0.65 | 0.65 |

Foundation models substantially lag behind specialized models on gene expression prediction.

## 2024-03-28 -- Pathogenic variant identification (AUROC)

| Model | ClinVar pathogenic (AUROC) | Rank |
|-------|--------------------------|------|
| DNABERT-2 | 0.82 | 2 |
| Nucleotide Transformer V2 | 0.84 | 1 |
| HyenaDNA | 0.78 | 4 |
| Caduceus-Ph | 0.76 | 5 |
| GROVER | 0.80 | 3 |
| CADD (specialized) | 0.85 | -- |

Foundation models are competitive with specialized variant effect predictors here.

## 2024-04-10 -- TAD boundary recognition

| Model | AUROC | F1 |
|-------|-------|-----|
| DNABERT-2 | 0.74 | 0.68 |
| Nucleotide Transformer V2 | 0.73 | 0.67 |
| HyenaDNA | 0.70 | 0.63 |
| Caduceus-Ph | 0.69 | 0.62 |
| GROVER | 0.71 | 0.65 |

Moderate performance; TAD recognition remains challenging for current foundation models.

## 2024-04-18 -- Causal QTL identification

| Model | Precision@100 | Recall@100 |
|-------|-------------|-----------|
| DNABERT-2 | 0.18 | 0.12 |
| Nucleotide Transformer V2 | 0.20 | 0.14 |
| HyenaDNA | 0.15 | 0.10 |
| Specialized QTL model | 0.42 | 0.35 |

Foundation models are notably less effective at identifying putative causal QTLs vs specialized approaches.
