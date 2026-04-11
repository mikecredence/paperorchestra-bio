# Experimental Log: Benchmarking DNA Foundation Models for Genomic and Genetic Tasks

> Raw data log from benchmarking five DNA foundation models on genomic and genetic tasks using zero-shot embeddings.

---

## 1. Models Under Evaluation

| Model | Architecture | Pre-training Data | Tokenization | Parameters | Embedding Dim | Max Input Length |
|-------|-------------|-------------------|-------------|------------|---------------|-----------------|
| DNABERT-2 | BERT + ALiBi | 135 species (incl. human ref) | Byte Pair Encoding (BPE) | ~117M | 768 | No hard limit (quadratic scaling) |
| NT-v2 | BERT + Rotary Embeddings | 850 species (incl. human ref) | 6-mer sliding window | ~500M | 1024 | 12,000 nt |
| HyenaDNA | Hyena (long convolution, decoder) | Human reference genome | Single nucleotide | ~6.6M (1K config) | 256 | Up to 1M nt |
| Caduceus-Ph | Mamba (bidirectional SSM) | Human reference genome | Single nucleotide | ~6.6M | 256 | Up to 131K nt |
| GROVER | BERT-style | Human reference genome | BPE | ~100M | 768 | ~2K nt |

---

## 2. Datasets Overview

- **Total sequence classification datasets**: 57
  - 52 binary classification datasets
  - 5 multi-class classification datasets
- **Gene expression prediction**: GTEx blood tissue gene expression (restricted access)
- **Variant effect quantification**: Pathogenic vs. common SNPs, plus 4 QTL types (eQTL, sQTL, paQTL, ipaQTL)
- **TAD recognition**: 1500 TAD-centered sequences + 1500 background sequences for NT-v2 attention analysis

---

## 3. Pooling Method Benchmark (52 Binary Classification Datasets)

### 3.1 Number of Datasets Where Mean Token Pooling Significantly Outperformed Other Methods (DeLong's test, p < 0.01)

| Model | Mean > Summary Token (out of 52) | Mean > Max Pooling (out of 52) |
|-------|----------------------------------|-------------------------------|
| DNABERT-2 | 41 | 41 |
| NT-v2 | 42 | 42 |
| HyenaDNA | 35 | 35 |
| Caduceus-Ph | 37 | 37 |
| GROVER | 41 | 41 |

### 3.2 Average AUC Improvement from Summary Token to Mean Token Embedding

| Model | Mean AUC Improvement | IQR of Improvement |
|-------|---------------------|--------------------|
| DNABERT-2 | 4.0% | 2.0% - 5.5% |
| NT-v2 | 6.8% | 3.7% - 9.6% |
| HyenaDNA | 8.7% | 4.6% - 12.9% |
| Caduceus-Ph | 5.9% | 2.8% - 9.1% |
| GROVER | 1.4% | 0.7% - 1.9% |

### 3.3 Range of Average AUC Scores Across Models by Pooling Method

| Pooling Method | Min Average AUC | Max Average AUC |
|---------------|-----------------|-----------------|
| Summary token | 0.708 | 0.799 |
| Mean token | 0.795 | 0.822 |

**Observation (Fig 2):** Boxplots show mean token pooling produces tighter AUC distributions with higher medians across all five models compared to summary-token and max pooling.

**Notable specific examples:**
- Promoter identification (GM12878): mean token improved DNABERT-2 AUC from 0.964 to 0.986 (2.3% increase, p < 0.01)
- Promoter identification (B. amyloliquefaciens): mean token improved HyenaDNA AUC from 0.689 to 0.864 (25.4% increase, p < 0.01)

---

## 4. Sequence Classification: Human Genome Tasks (Table 1)

All results use mean token pooling. Bolded values indicate significantly higher than at least two other models (one-sided DeLong's test, p < 0.01).

| Task | DNABERT-2 | NT-v2 | HyenaDNA | Caduceus-Ph | GROVER |
|------|-----------|-------|----------|-------------|--------|
| DNase I Hypersensitive | 0.8666 | 0.8524 | 0.8295 | **0.8799** | 0.857 |
| Human TFBS 1 | 0.8382 | 0.8315 | 0.8301 | **0.8796** | 0.8618 |
| Human TFBS 2 | 0.821 | 0.809 | 0.8205 | **0.8687** | 0.8495 |
| Human TFBS 3 | 0.7896 | 0.7974 | 0.7875 | **0.8249** | 0.8158 |
| Human TFBS 4 | 0.726 | 0.7103 | 0.7149 | **0.7725** | 0.763 |
| Human TFBS 5 | 0.9204 | 0.9149 | 0.9159 | 0.9294 | **0.931** |
| Promoter GM12878 | **0.9856** | 0.9835 | 0.976 | **0.9865** | 0.9839 |
| Promoter HUVEC | **0.9903** | 0.987 | 0.9817 | 0.9896 | 0.9885 |
| Promoter Hela-S3 | **0.9886** | 0.9838 | 0.981 | 0.9871 | 0.9857 |
| Promoter NHEK | 0.9501 | 0.9323 | 0.9271 | **0.9567** | 0.9507 |
| Splice Acceptor | **0.8969** | 0.7928 | 0.7946 | 0.8449 | 0.8041 |
| Coding Region | 0.9438 | 0.9289 | 0.9406 | **0.9735** | 0.9594 |
| Splice Donor | **0.9056** | 0.8198 | 0.8128 | 0.8535 | 0.819 |
| Enhancer | **0.8717** | 0.8674 | 0.8339 | 0.8384 | 0.8554 |
| Enhancer Cohn | **0.8223** | 0.7894 | 0.7754 | 0.821 | 0.8161 |
| Enhancer Ensembl | 0.9369 | 0.9389 | 0.9356 | **0.9431** | 0.9382 |
| Open Chromatin Region | 0.7253 | 0.7183 | 0.7191 | **0.765** | 0.7455 |
| Promoter All 300 bps | 0.9426 | 0.9445 | 0.9394 | **0.9519** | 0.9402 |
| Promoter All 70 bps | 0.8311 | 0.8527 | 0.832 | **0.8748** | 0.8506 |
| Promoter NonTATA 251 bps | 0.9297 | 0.8905 | 0.928 | **0.9426** | 0.9395 |
| Promoter NonTATA 300 bps | 0.9765 | 0.9758 | 0.9662 | **0.9834** | 0.9728 |
| Promoter NonTATA 70 bps | 0.8531 | 0.8729 | 0.8516 | **0.8961** | 0.8704 |
| Promoter TATA 300 bps | 0.7646 | 0.7791 | **0.8077** | 0.76 | 0.78 |
| Promoter TATA 70 bps | 0.7781 | 0.7947 | 0.7827 | **0.8103** | 0.796 |

**Key findings:**
- Caduceus-Ph dominates TFBS prediction tasks (highest in 5/6 TFBS datasets)
- DNABERT-2 is strongest for splice site prediction (Acceptor: 0.897, Donor: 0.906)
- All models achieve AUC > 0.8 on the majority of human genome tasks
- Promoter identification in cell lines GM12878, HUVEC, Hela-S3, NHEK: DNABERT-2 and Caduceus-Ph achieve statistically significant superior performance

---

## 5. Sequence Classification: Multispecies Tasks (Table 2)

All results use mean token pooling. Bolded values: significantly higher than at least two other AUCs (p < 0.01, DeLong's test).

| Task | DNABERT-2 | NT-v2 | HyenaDNA | Caduceus-Ph | GROVER |
|------|-----------|-------|----------|-------------|--------|
| Promoter Arabidopsis NonTATA | 0.9457 | 0.9395 | **0.9547** | 0.9437 | 0.949 |
| Promoter Arabidopsis TATA | 0.951 | 0.95 | **0.9609** | 0.9372 | 0.9486 |
| Promoter B. amyloliquefaciens | 0.8518 | 0.8225 | 0.8643 | **0.8686** | 0.8617 |
| Promoter R. capsulatus | 0.6855 | 0.6746 | 0.7116 | 0.67 | **0.7154** |
| Human vs. Worm | 0.9799 | 0.9785 | 0.9502 | **0.9915** | 0.9843 |
| Mouse TFBS 1 | **0.711** | 0.704 | 0.5899 | 0.6841 | 0.6947 |
| Mouse TFBS 2 | 0.9072 | 0.9005 | 0.8996 | **0.9472** | 0.9093 |
| Mouse TFBS 3 | 0.9308 | 0.9269 | 0.8944 | **0.9351** | 0.9327 |
| Mouse TFBS 4 | **0.7622** | 0.6942 | 0.588 | 0.7047 | 0.6815 |
| Mouse TFBS 5 | 0.6783 | 0.7077 | 0.627 | **0.715** | 0.6822 |

**Key findings:**
- HyenaDNA showed unexpected advantages in Arabidopsis promoter tasks
- Human vs. worm classification: Caduceus-Ph (0.992) and GROVER (0.984) strongest
- R. capsulatus: no model achieved clear statistical superiority (AUC ~0.67-0.72), suggesting challenges in prokaryotic genome generalization
- Baseline CNN generally outperformed foundation models on multispecies tasks

---

## 6. Epigenetic Modification Detection (Table 3)

All results use mean token pooling. Bolded values: significantly higher than at least two other AUCs (p < 0.01).

| Task | DNABERT-2 | NT-v2 | HyenaDNA | Caduceus-Ph | GROVER |
|------|-----------|-------|----------|-------------|--------|
| Human 5mC | 0.685 | 0.7377 | 0.6843 | **0.783** | 0.7437 |
| Human 6mA | 0.7351 | 0.7508 | 0.7377 | **0.7731** | 0.7671 |
| Yeast H3 | **0.9137** | 0.8951 | 0.8996 | **0.9285** | 0.9056 |
| Yeast H3K14ac | **0.7597** | 0.7407 | 0.7067 | 0.7297 | 0.7301 |
| Yeast H3K36me3 | **0.7989** | 0.7849 | 0.7395 | 0.7662 | 0.7533 |
| Yeast H3K4me1 | **0.7306** | 0.7115 | 0.6994 | 0.7071 | 0.696 |
| Yeast H3K4me2 | **0.7078** | 0.6847 | 0.6854 | 0.6895 | 0.6939 |
| Yeast H3K4me3 | **0.6813** | 0.6603 | 0.6486 | 0.6595 | 0.668 |
| Yeast H3K79me3 | **0.8565** | 0.8436 | 0.8215 | 0.845 | 0.8427 |
| Yeast H3K9ac | **0.7922** | 0.7687 | 0.7555 | 0.7779 | 0.7692 |
| Yeast H4 | **0.9314** | 0.9104 | 0.8983 | 0.9304 | 0.908 |
| Yeast H4ac | **0.7473** | 0.7263 | 0.6979 | 0.7235 | 0.7175 |
| A. thaliana 4mC | 0.5994 | **0.6332** | 0.5941 | 0.6146 | 0.6026 |
| C. elegans 4mC | 0.5985 | **0.6487** | 0.5964 | 0.5964 | 0.6057 |
| D. melanogaster 4mC | 0.6147 | **0.6519** | 0.6096 | 0.6161 | 0.6167 |
| E. coli 4mC | 0.5492 | 0.6028 | 0.6105 | **0.6283** | 0.5851 |
| G. pickeringii 4mC | 0.5958 | 0.6302 | 0.6292 | **0.6348** | 0.6293 |
| G. subterraneus 4mC | 0.5802 | 0.6145 | 0.609 | 0.6079 | 0.6061 |

**Key findings:**
- Human epigenetic modifications: NT-v2, Caduceus-Ph, and GROVER consistently strong; Caduceus-Ph achieves 0.783 for 5mC
- Yeast epigenetic marks: DNABERT-2 shows robust performance across the full range of yeast marks
- 4mC detection across species: NT-v2 leads for A. thaliana, C. elegans, and D. melanogaster
- Epigenetic prediction is typically 10-15% lower AUC than functional genomic region classification tasks
- Baseline CNN generally outperformed foundation models on epigenetic tasks

---

## 7. Multi-Class Classification Tasks

| Task | DNABERT-2 | NT-v2 | HyenaDNA | Caduceus-Ph | GROVER |
|------|-----------|-------|----------|-------------|--------|
| Regulatory Region Type | - | - | **0.83** | - | - |
| Splice Site Type (NT dataset) | - | - | **0.563** | - | - |
| COVID Variants | Top | - | - | - | Top |
| Enhancer Strength | >0.7 | - | - | >0.7 | >0.7 |

**Key findings:**
- HyenaDNA demonstrated exceptional multi-class performance, especially for regulatory region type classification (accuracy 0.83) and splice site type classification (accuracy 0.563)
- DNABERT-2 and GROVER lead for COVID variant classification
- GROVER, DNABERT-2, and Caduceus-Ph comparable for enhancer strength (all >0.7)

---

## 8. Gene Expression Prediction (Table 4)

Random forest regression on GTEx blood tissue. All short-sequence models use ~6K bp input centered on TSS (except GROVER at 2048 bp). Long-sequence models use extended context.

| Model | Input Seq Length | Avg Prediction Correlation | Avg Prediction MSE |
|-------|-----------------|---------------------------|-------------------|
| DNABERT-2 | 6,000 bp | 0.121 | 0.236 |
| NT-v2 | 6,000 bp | 0.122 | 0.236 |
| HyenaDNA | 6,000 bp | 0.122 | 0.235 |
| Caduceus-Ph | 6,000 bp | 0.123 | 0.234 |
| GROVER | 2,048 bp | 0.114 | 0.233 |
| HyenaDNA-450K | 196,608 bp | **0.137** | **0.226** |
| Caduceus-Ph (long) | 131,072 bp | 0.127 | 0.227 |
| Enformer* | 196,608 bp | 0.129 | 0.227 |

*Non-DNA foundation model (specialized for gene expression)

**Key findings:**
- Average correlations are modest across all models (~0.11-0.14)
- Among short-sequence models, Caduceus-Ph and HyenaDNA slightly outperform others
- GROVER with shorter 2048 bp input slightly lower than other short-sequence models
- HyenaDNA-450K (0.137) significantly outperformed Enformer (0.129) at p < 0.01
- Extending sequence length significantly improved HyenaDNA performance (p < 0.001), but improvement for Caduceus-Ph was not statistically significant
- Random forest regression significantly outperformed XGBoost for all models (p < 0.001)
- Certain genes consistently predicted with high accuracy (correlations up to 0.9)
- Top predicted gene with 6K bp input: CUTALP (correlation > 0.89 across all five short-sequence models)
- Other highly predictable genes (short context): CPNE1, NT5C3B, DDX11, PEX6
- Top predicted genes with long context: DDX11, HLA-DRB5, DHFR, CD151

**Observation (Fig 3):** Histograms for HyenaDNA and HyenaDNA-450K show similar distribution patterns with slight positive skew, indicating most genes have modest predictability but a subset shows strong sequence-expression relationships.

---

## 9. Pathogenic vs. Common Variant Effect Quantification (Table 5)

Embedding subtraction method. Metrics are averages across three independent test sets from nested cross-validation with chromosome-based splits. Asterisk (*) denotes non-DNA foundation models.

| Model | AUC | Cohen's d |
|-------|-----|-----------|
| Sei*, hidden states | 0.6598 | 0.5573 |
| Sei*, output tracks | 0.664 | 0.6046 |
| Enformer*, hidden states | **0.688** | 0.7269 |
| Enformer*, output tracks | 0.6662 | 0.6542 |
| DNABERT-2 | 0.538 | 0.1338 |
| NT-v2 | **0.7319** | **0.8813** |
| HyenaDNA | 0.612 | 0.3952 |
| HyenaDNA-450K (long) | 0.6261 | 0.4493 |
| Caduceus-Ph | 0.6959 | **0.7354** |
| Caduceus-Ph (long) | 0.6243 | 0.4615 |
| GROVER | 0.6029 | 0.3693 |

**Key findings:**
- NT-v2 is the clear top performer: AUC 0.732 and Cohen's d 0.881, outperforming all models including Enformer (AUC 0.688) and Sei (AUC 0.664)
- Caduceus-Ph is second best among foundation models (AUC 0.696, Cohen's d 0.735)
- DNABERT-2 performs poorly on this task (AUC 0.538)
- Short-sequence Caduceus-Ph (AUC 0.696) outperformed its long-sequence counterpart (AUC 0.624), suggesting larger genomic context may dilute local SNP signal with embedding subtraction
- Similarly, HyenaDNA short (0.612) vs. HyenaDNA-450K long (0.626) showed only modest improvement from longer context

---

## 10. QTL Variant Effect Quantification (Table 6)

### AUC Scores

| Model | eQTL | sQTL | paQTL | ipaQTL |
|-------|------|------|-------|--------|
| AlphaGenome*, output tracks | **0.8029** | **0.7147** | **0.7543** | **0.8644** |
| Sei*, hidden states | 0.7561 | 0.6534 | 0.6189 | 0.6071 |
| Sei*, output tracks | 0.7497 | 0.6276 | 0.6553 | 0.606 |
| Enformer*, hidden states | **0.7744** | **0.6662** | 0.6737 | 0.6919 |
| Enformer*, output tracks | 0.7699 | 0.6174 | 0.666 | 0.6587 |
| DNABERT-2 | 0.5702 | 0.5795 | 0.5066 | 0.4694 |
| NT-v2 | 0.6091 | 0.5047 | 0.5251 | 0.6019 |
| HyenaDNA | 0.6117 | 0.5531 | 0.4699 | 0.448 |
| HyenaDNA-450K (long) | 0.6027 | 0.5262 | 0.5521 | 0.5093 |
| Caduceus-Ph | 0.6492 | 0.5666 | 0.5082 | 0.5678 |
| Caduceus-Ph (long) | 0.6265 | 0.5703 | 0.4649 | 0.5203 |
| GROVER | 0.5896 | 0.4742 | 0.4494 | 0.4759 |

### Cohen's d Values

| Model | eQTL | sQTL | paQTL | ipaQTL |
|-------|------|------|-------|--------|
| AlphaGenome*, output tracks | **1.287** | **0.7872** | **0.9824** | **1.6347** |
| Sei*, hidden states | 1.0335 | 0.553 | 0.4538 | 0.4126 |
| Sei*, output tracks | 1.0116 | 0.4936 | 0.5503 | 0.4227 |
| Enformer*, hidden states | **1.1102** | 0.6115 | 0.6028 | 0.6576 |
| Enformer*, output tracks | 1.1085 | 0.4129 | 0.5457 | 0.5691 |
| DNABERT-2 | 0.2371 | 0.2825 | 0.024 | -0.0756 |
| NT-v2 | 0.3956 | -0.004 | 0.0658 | 0.3837 |
| HyenaDNA | 0.3877 | 0.2018 | -0.0768 | -0.2048 |
| HyenaDNA-450K (long) | 0.3605 | 0.0757 | 0.2068 | 0.0733 |
| Caduceus-Ph | 0.5484 | 0.2278 | 0.0456 | 0.2324 |
| Caduceus-Ph (long) | 0.4913 | 0.2464 | -0.1151 | 0.075 |
| GROVER | 0.319 | -0.0978 | -0.1393 | -0.072 |

**Key findings:**
- Specialized track-prediction models drastically outperform general DNA foundation models on all QTL tasks
- AlphaGenome is the standout: highest AUC and Cohen's d across all four QTL types (e.g., sQTL AUC 0.80, ipaQTL AUC 0.86)
- Enformer (eQTL AUC 0.77) vastly exceeds the best foundation model Caduceus-Ph (eQTL AUC 0.65)
- Sei hidden states often as predictive as output tracks (e.g., sQTL: hidden 0.653 vs. output 0.628)
- Several foundation models yield AUC below 0.5 on smaller QTL datasets (ipaQTL, paQTL, sQTL), indicating instability with small sample sizes
- Negative Cohen's d values for some models (e.g., GROVER sQTL: -0.098) suggest predictions worse than random on some chromosome splits
- Nested cross-validation design reveals high variance: performance highly sensitive to holdout chromosome choice on small datasets

---

## 11. Pre-Training Data Experiment

Re-pretrained HyenaDNA on DNABERT-2's multi-species dataset (135 species) using hyperparameters comparable to original HyenaDNA-1K checkpoint.

| Metric | Original HyenaDNA-1K | Re-pretrained HyenaDNA (multi-species) |
|--------|----------------------|---------------------------------------|
| Datasets with significant improvement (of 49) | 3 | 14 |
| Human 5mC detection AUC | 0.707 | 0.749 |
| Human vs. Worm classification AUC | 0.968 | 0.984 |

**Key findings:**
- Multi-species pre-training improved performance on 14/49 datasets, particularly for cross-species generalization and epigenetic pattern recognition
- Original HyenaDNA-1K was superior on only 3/49 datasets (human enhancer identification, human open chromatin, yeast epigenetic marks)
- Improvements most prominent in tasks requiring cross-species knowledge or diverse epigenetic signals

---

## 12. TAD Boundary Recognition (NT-v2 Attention Analysis)

- Processed 1500 TAD-centered sequences and 1500 background sequences through NT-v2
- Extracted and averaged attention matrices across all layers and attention heads
- If NT-v2 recognized TAD structures, expected vertical band of positive values at central region (token positions ~300-700) in the difference heatmap

**Result:** Difference heatmap between TAD-centered and background attention matrices showed no distinctive vertical band pattern. NT-v2's self-attention mechanism does not recognize TAD boundaries without fine-tuning.

**Limitation:** Other models could not be analyzed: HyenaDNA and Caduceus-Ph lack accessible attention mechanisms; DNABERT-2 lacks accessible attention matrices; GROVER has input length limitations precluding meaningful TAD-scale analysis.

---

## 13. Runtime Analysis (Fig 4)

Measured as total seconds for 1000 replications, batch size 1, A100 GPU. Sequence lengths from 64 to 524,288 nucleotides.

| Model | Performance Characteristics |
|-------|---------------------------|
| GROVER | Fastest runtime for sequences within supported range (~2K nt) |
| HyenaDNA-160K | Stable performance for shorter sequences (<2K nt) |
| HyenaDNA-1M | Excellent scaling up to ~500K nt |
| DNABERT-2 | Competitive for sequences near recommended limit (~2K nt); dramatic runtime spike beyond that |
| NT-v2 | Consistently highest runtime across all lengths (~2.5s per 100 reps); very stable (reflects 500M parameter size) |
| Caduceus-Ph-131K | Moderate performance with gradually increasing runtime as sequence length grows |

**Key observation (Fig 4):** Despite logarithmic scale of sequence lengths, none of the models show clear quadratic scaling, suggesting attention computation was not the dominant factor within batch size 1 experiments. Dashed vertical lines in figure mark where models exceed supported/recommended input limits or GPU memory capacity.

---

## 14. Classifier Selection

| Classifier | Outcome |
|-----------|---------|
| Random Forest | Selected as standard; strong generalization, minimal inductive bias |
| Naive Bayes | Evaluated on all binary datasets; underperformed random forest |
| Elastic-Net Logistic Regression | Evaluated on all binary datasets; underperformed random forest |
| XGBoost (for regression) | Tested for gene expression; significantly outperformed by random forest (all p < 0.001) |

---

## 15. Summary of Model Strengths by Task Category

| Task Category | Best Performing Model(s) | Notes |
|--------------|-------------------------|-------|
| Human TFBS prediction | Caduceus-Ph | Consistent top performer across 5/6 TFBS datasets |
| Splice site prediction | DNABERT-2 | Donor: 0.906, Acceptor: 0.897 |
| Human promoter identification | DNABERT-2, Caduceus-Ph | Both significantly superior for multiple cell lines |
| Human epigenetic modifications | Caduceus-Ph, NT-v2, GROVER | NT-v2 strong for 5mC/6mA; Caduceus-Ph highest absolute AUC |
| Yeast epigenetic marks | DNABERT-2 | Robust across full range of yeast marks |
| 4mC detection (multi-species) | NT-v2 | Top for A. thaliana, C. elegans, D. melanogaster |
| Multi-class regulatory regions | HyenaDNA | Accuracy 0.83 for regulatory region type |
| Multispecies promoters | HyenaDNA | Arabidopsis promoter tasks |
| Gene expression prediction | Caduceus-Ph, HyenaDNA | Short context; HyenaDNA-450K best overall (0.137 corr) |
| Pathogenic variant identification | NT-v2 | AUC 0.732, outperforming all including Enformer |
| QTL identification | AlphaGenome* (specialized) | Foundation models substantially lag; best is Caduceus-Ph at eQTL 0.649 |

---

## 16. Statistical Methods Used

| Method | Application |
|--------|------------|
| One-sided DeLong's test (p < 0.01) | Pairwise AUC comparisons for sequence classification |
| Pearson correlation | Gene expression prediction accuracy |
| Cohen's d effect size | Variant effect quantification tasks |
| Nested cross-validation (chromosome-based splits) | Variant effect and QTL tasks (3 independent test sets) |
| Wilcoxon signed-rank test | Comparing classifiers and pooling methods across datasets |

---

## 17. Key Datasets and Sources

| Dataset Category | Source / Count |
|-----------------|---------------|
| Sequence classification (binary) | 52 datasets from multiple published sources |
| Sequence classification (multi-class) | 5 datasets |
| Gene expression | GTEx blood tissue (restricted access) |
| Pathogenic vs. common SNPs | Genomics Long-Range Benchmark (HuggingFace) |
| QTL variants (eQTL, sQTL, paQTL, ipaQTL) | Borzoi paper repository (Google Cloud) |
| TAD sequences | Basenji Hi-C repository (Google Cloud) |
| Processed benchmark data | HuggingFace Hub: hfeng3/dna_foundation_benchmark_dataset |
