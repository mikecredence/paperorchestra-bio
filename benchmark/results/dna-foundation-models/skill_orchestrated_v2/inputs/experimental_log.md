# Experimental Log: Benchmarking DNA Foundation Models

## Models Evaluated

| Model | Architecture | Pre-training Data | Parameters | Embedding Dim | Max Input Length | Tokenization |
|-------|-------------|-------------------|------------|---------------|-----------------|--------------|
| DNABERT-2 | BERT + ALiBi | 135 species | 117M | 768 | No hard limit (quadratic scaling) | Byte Pair Encoding (BPE) |
| NT-v2 | BERT + Rotary Embeddings + Swish | 850 species | 500M | 1,024 | 12,000 nt | 6-mers sliding window |
| HyenaDNA | Decoder (Hyena operators) | Human reference genome only | 30M | 256 | 1,000,000 nt | Single nucleotide |
| Caduceus-Ph | MambaDNA (BiMamba + RC equivariance) | N/A | 35M | 256 | 131,000 nt | Single nucleotide |
| GROVER | BERT (12 transformer layers) | Human genome | 117M | 768 | 512 tokens (~2,000 nt avg) | BPE (600 optimization cycles) |

---

## Experiment 1: Pooling Methods Benchmark (52 Binary Classification Datasets)

### Number of datasets where mean token pooling was statistically superior (DeLong's test, p < 0.01)

| Model | Mean > Summary-token | Mean > Max pooling |
|-------|---------------------|--------------------|
| DNABERT-2 | 41/52 | 41/52 |
| NT-v2 | 42/52 | 42/52 |
| HyenaDNA | 35/52 | 35/52 |
| Caduceus-Ph | 37/52 | 37/52 |
| GROVER | 41/52 | 41/52 |

### Average AUC increase from summary-token to mean token embedding

| Model | Average AUC Increase (%) | IQR |
|-------|--------------------------|-----|
| DNABERT-2 | 4.0% | 2.0%--5.5% |
| NT-v2 | 6.8% | 3.7%--9.6% |
| HyenaDNA | 8.7% | 4.6%--12.9% |
| Caduceus-Ph | 5.9% | 2.8%--9.1% |
| GROVER | 1.4% | 0.7%--1.9% |

### Notable pooling improvement examples

| Task | Model | Summary-token AUC | Mean-token AUC | Improvement (%) | Significance |
|------|-------|--------------------|----------------|-----------------|--------------|
| Promoter ID, GM12878 | DNABERT-2 | 0.964 | 0.986 | 2.3% | p < 0.01, DeLong's test |
| Promoter ID, B. amyloliquefaciens | HyenaDNA | 0.689 | 0.864 | 25.4% | p < 0.01, DeLong's test |

### AUC score range across models by pooling method

| Pooling Method | Min Average AUC | Max Average AUC |
|----------------|-----------------|-----------------|
| Summary-token | 0.708 | 0.799 |
| Mean pooling | 0.795 | 0.822 |

---

## Experiment 2: Human Genome Region Classification (Mean Token Pooling)

Table 1 reports AUC results for binary sequence classification tasks on human genome including: promoter region identification (GM12878, HUVEC, HeLa-S3, NHEK), coding region detection, splice site donor and acceptor identification, enhancer identification (multiple datasets), transcription factor binding site identification (multiple datasets), and open chromatin region identification (multiple datasets).

### Key findings (Table 1)

- All five models achieved AUC > 0.8 on the majority of tasks
- Caduceus-Ph exhibited superior overall performance across multiple human genome classification tasks
- DNABERT-2 and Caduceus-Ph achieved statistically significant superior performance for promoter identification in GM12878, HUVEC, HeLa-S3, NHEK (p < 0.01, one-sided DeLong's test)
- DNABERT-2: splice site donor AUC 0.906, splice site acceptor AUC 0.897 (significantly outperforming other models)
- Caduceus-Ph consistently outperformed all other models for TFBS prediction
- Bolding criterion: higher than at least two other AUCs, p < 0.01 (one-sided DeLong's test)
- DNABERT-2, GROVER, Caduceus-Ph, and NT-v2 showed significant improvements over baseline CNN for GM12878 and HUVEC promoter identification

---

## Experiment 3: Multi-species Genome Region Classification (Mean Token Pooling)

Table 2 reports AUC results for multi-species tasks: promoter region prediction (4 datasets), human vs. worm classification, mouse TFBS identification.

### Key findings (Table 2)

| Task | Top Model(s) | AUC |
|------|-------------|-----|
| Arabidopsis TATA promoter | HyenaDNA | 0.961 |
| Arabidopsis NonTATA promoter | HyenaDNA | 0.955 |
| Human vs. Worm classification | Caduceus-Ph | 0.992 |
| Human vs. Worm classification | GROVER | 0.984 |
| R. capsulatus promoter | GROVER | 0.715 |

- HyenaDNA (pre-trained exclusively on human genomes) demonstrated unexpected advantage in Arabidopsis promoter identification
- No model achieved clear statistical superiority for B. amyloliquefaciens bacterial promoter identification
- DNA foundation models generally underperformed vs. baseline CNN for multispecies tasks
- Bolding criterion: higher than at least two other AUCs, p < 0.01 (one-sided DeLong's test)

---

## Experiment 4: Human and Multi-species Epigenetic Modification (Mean Token Pooling)

Table 3 reports AUC results for 5mC, 6mA detection in human; epigenetic marks detection in yeast; and 4mC detection in multiple species.

### Key findings (Table 3)

| Task | Model | AUC |
|------|-------|-----|
| Human 5mC detection | NT-v2 | 0.738 |
| Human 5mC detection | Caduceus-Ph | 0.783 |
| Human 5mC detection | GROVER | 0.744 |
| Human 6mA detection | NT-v2, Caduceus-Ph, GROVER | Statistically superior (p < 0.01) |
| A. thaliana 4mC | NT-v2 | 0.633 |
| C. elegans 4mC | NT-v2 | 0.649 |
| D. melanogaster 4mC | NT-v2 | 0.652 |
| E. coli 4mC | Caduceus-Ph | 0.628 |

- Epigenetic prediction AUC scores typically 10--15% lower than functional genomic region tasks
- For yeast epigenetic marks: multiple DNA foundation models outperformed baseline CNN (H3, H3K4me1, H3K79me3 -- five and four foundation models respectively showed superior performance)
- DNABERT-2 showed robust performance across yeast epigenetic marks
- Eukaryotic 4mC datasets (A. thaliana, C. elegans, D. melanogaster) treated as exploratory due to annotation methods

---

## Experiment 5: Multi-class Classification (5 Datasets)

| Task | Top Model | Accuracy |
|------|-----------|----------|
| Regulatory Region Type | HyenaDNA | 0.83 |
| Splice Site Type (NT dataset) | HyenaDNA | 0.563 |
| COVID Variants | DNABERT-2, GROVER | Not reported (leading) |
| Enhancer Strength | GROVER, DNABERT-2, Caduceus-Ph | > 0.7 |

---

## Experiment 6: Gene Expression Prediction (Random Forest Regression)

Table 4 reports overall performance in gene expression prediction.

### GTEx v8 dataset parameters
- Tissue: whole blood
- Subjects: 610
- Genes (short sequences): 21,004
- Short sequence length: TSS +/- 3,000 bp (~6,000 bp total)
- Long sequence length: TSS +/- 98K bp
- Long sequence genes: 768 (after filtering from 1,000 random)
- Gene expression: covariate-corrected residuals (covariates: sex, PEER factors, top genotype PCs)

### Average Pearson correlation (6k bp inputs)

| Model | Average Pearson r (6k bp) |
|-------|---------------------------|
| All short-sequence models | 0.114--0.123 |

- Random forest regression significantly outperformed XGBoost (all p < 0.001)
- Caduceus-Ph and HyenaDNA: highest average correlations among short-sequence models, significantly outperforming DNABERT-2 and GROVER
- GROVER (2048 bp input): slightly lower average correlation than other short-sequence models
- HyenaDNA-450K: significantly better performance than Enformer (p < 0.01)
- Extending sequence length: significantly improved performance for HyenaDNA (p < 0.001); improvement for Caduceus-Ph not statistically significant

### Top-predicted genes (6k bp inputs)

| Gene | Correlation | Note |
|------|-------------|------|
| CUTALP | > 0.89 | Top-predicted across all 5 short-sequence models |
| CPNE1 | Top 10 | Consistent across models |
| NT5C3B | Top 10 | Consistent across models |
| DDX11 | Top 10 | Consistent across models; also top for long-sequence models |
| PEX6 | Top 10 | Consistent across models |

### Top-predicted genes (long-sequence models, ~196K bp)

| Gene | Note |
|------|------|
| DDX11 | Highest correlations across all 3 long-sequence models |
| HLA-DRB5 | Highest correlations across all 3 long-sequence models |
| DHFR | Strong predictability |
| CD151 | Strong predictability; tetraspanin relevant to platelet activation/aggregation |

---

## Experiment 7: Variant Effect Quantification -- Pathogenic vs. Common SNPs

Table 5 reports overall performance in pathogenic vs. common variant classification.

### Dataset sizes
- Long sequences (196,608 bp): 22,222 pathogenic, 17,374 common
- Short sequences (6,000 bp): 22,239 pathogenic, 17,398 common
- Nested cross-validation: 3 independent test sets defined by chromosome groups

### Pathogenic variant identification performance

| Model | Average Test AUC | Cohen's d |
|-------|-----------------|-----------|
| NT-v2 | 0.73 | 0.88 |
| Caduceus-Ph | 0.70 | Not reported (top performer) |
| Enformer* | 0.69 | 0.73 |
| Sei* | Not reported | Not reported |
| Caduceus-Ph (long seq) | 0.62 | Not reported |

- NT-v2 substantially outperformed all other models including Enformer and Sei
- Short-sequence Caduceus-Ph (AUC 0.70) outperformed long-sequence Caduceus-Ph (AUC 0.62) for pathogenic SNP task
- Non-DNA foundation models annotated with asterisk (*)
- Bolding criterion: top 2 highest (absolute) values

---

## Experiment 8: Variant Effect Quantification -- QTL Classification

Table 6 reports overall performance in QTL variant effect quantification tasks: eQTL, sQTL, ipaQTL, paQTL.

### QTL dataset sizes (whole blood, GTEx v8 fine-mapped)
- eQTLs: 1,896
- sQTLs: 540
- ipaQTLs: 116
- paQTLs: 142
- Each putative causal QTL paired with matched non-causal variant

### QTL prediction performance (selected)

| Model | eQTL AUC | sQTL AUC | ipaQTL AUC | paQTL AUC |
|-------|----------|----------|------------|-----------|
| AlphaGenome* | Not reported | 0.80 | 0.86 | Not reported |
| Enformer* | 0.77 | Not reported | Not reported | Not reported |
| Caduceus-Ph | 0.65 | Not reported | Not reported | Not reported |
| Sei* (hidden state) | N/A | 0.65 | Not reported | Not reported |
| Sei* (output tracks) | N/A | 0.63 | Not reported | Not reported |

- AlphaGenome: highest AUC and Cohen's d across all 4 QTL types
- Enformer and Sei significantly outperformed general DNA foundation models
- Sei hidden states as predictive as final output tracks (sQTL: hidden 0.65 vs. output 0.63)
- Several foundation models (DNABERT-2, HyenaDNA, Caduceus-Ph long, GROVER) yielded average AUC slightly below 0.5 on smaller QTL datasets
- Performance highly sensitive to choice of holdout chromosomes in nested CV
- Bolding criterion: top 2 highest (absolute) performances per task

---

## Experiment 9: Pre-training Data Experiment (HyenaDNA Re-pretrained)

### Setup
- Original: HyenaDNA-1K pre-trained on human reference genome only
- New: HyenaDNA re-pretrained on DNABERT-2's multi-species dataset (135 species, 6 taxonomic categories)
- Comparable hyperparameters to original HyenaDNA-1K checkpoint

### Results across 49 evaluated datasets

| Outcome | Count |
|---------|-------|
| Multi-species significantly better (p < 0.01) | 14/49 |
| Original HyenaDNA-1K significantly better (p < 0.01) | 3/49 |

### Specific improvements with multi-species pre-training

| Task | Original AUC | Multi-species AUC |
|------|-------------|-------------------|
| Human 5mC detection | 0.707 | 0.749 |
| Human vs. Worm classification | 0.968 | 0.984 |

- Multi-species gains especially in cross-species generalization and epigenetic pattern recognition
- Original retained advantage in: human enhancer identification, human open chromatin region identification, yeast epigenetic mark prediction

---

## Experiment 10: TAD Region Recognition (NT-v2 Attention Analysis)

### Setup
- 1500 TAD-centered sequences (top 5% boundary strength, 2400 bp TAD regions centered in 6000 bp sequences)
- 1500 random background sequences (6000 bp)
- Attention matrices extracted and averaged across all layers and attention heads of NT-v2
- Other models excluded: HyenaDNA and Caduceus-Ph lack accessible attention mechanisms; DNABERT-2 lacks accessible attention matrices; GROVER limited by input length

### Result
- No distinct patterns in attention difference matrix (TAD-centered minus background)
- Heatmap shows predominantly uniform values near zero
- Minimal variation only along diagonal (self-attention)
- Conclusion: NT-v2 self-attention does not recognize TAD boundaries without fine-tuning

---

## Experiment 11: Runtime Analysis (Single A100 GPU)

- HyenaDNA models: most favorable scaling, particularly for longer sequences
- HyenaDNA-160K: stable performance for sequences below 2K nucleotides
- HyenaDNA-1M: excellent scaling at sequence lengths approaching 500K nucleotides
- DNABERT-2: competitive runtime near its ~2K nt limit; dramatic runtime increase beyond
- NT-v2: highest runtime across all sequence lengths (~2.5 seconds for 100 replications); highly stable; reflects 500M parameter model
- GROVER: fastest runtime among all models for sequences within 2K nt range
- Caduceus-Ph-131K: moderate performance with gradually increasing runtime
- Runtime measured as total seconds for 1000 replications using batch size 1
- No clear quadratic scaling observed (batch size 1 may not be sufficient to reveal this)

---

## Downstream Classifier Comparison

| Classifier | Result |
|------------|--------|
| Random forest | Selected as standard; strong performance, minimal hyperparameter tuning |
| Naive Bayes | Evaluated on all binary datasets; confirmed mean token pooling superiority |
| Elastic-net logistic regression | Competitive with random forest within mean pooling configuration |

- Random forest and elastic-net: most competitive classifiers
- Mean token embedding confirmed as superior pooling strategy across all classifiers

---

## Methods Parameters

| Parameter | Value |
|-----------|-------|
| Classification datasets | 57 total (52 binary, 5 multi-class) |
| Sequence length range | 41 bp to ~2,000 bp |
| Primary metric | AUROC (AUC) |
| Downstream classifier | Random forest |
| Statistical significance threshold | p < 0.01 |
| Gene expression tissue | Whole blood |
| GTEx version | v8 |
| Subjects (gene expression) | 610 |
| Genes (short seq) | 21,004 |
| Genes (long seq) | 768 |
| Short sequence length | TSS +/- 3,000 bp (~6,000 bp) |
| Long sequence length | TSS +/- 98K bp (~196K bp) |
| Pathogenic SNPs (long) | 22,222 |
| Common SNPs (long) | 17,374 |
| Pathogenic SNPs (short) | 22,239 |
| Common SNPs (short) | 17,398 |
| eQTLs | 1,896 |
| sQTLs | 540 |
| ipaQTLs | 116 |
| paQTLs | 142 |
| TAD sequences | 1,500 TAD-centered + 1,500 background |
| TAD boundary strength filter | Top 5% |
| TAD region size | 2,400 bp centered in 6,000 bp |
| Cross-validation (variant effect) | Nested, 3 independent test sets by chromosome groups |
| Pre-training experiment species | 135 species, 6 taxonomic categories |
| Runtime GPU | Single A100 |
| Runtime replications | 1,000 (batch size 1) |
| Sequence lengths tested (runtime) | 64 to 524,288 nucleotides |
| Reference genome | GRCh38/hg38 |
| DNase-I sequence length | 225--275 bp |
| 5mC/6mA sequence length | 41 bp |
| 4mC sequence length | 41 bp |

---

## Statistics Summary

| Test | Context |
|------|---------|
| One-sided DeLong's test | Pairwise comparison of AUC values between models and between pooling methods; significance threshold p < 0.01 |
| Nested cross-validation | Variant effect quantification; 3 independent test sets defined by chromosome groups |
| Random forest classification | Primary downstream classifier for sequence classification benchmark |
| Random forest regression | Gene expression prediction; significantly outperformed XGBoost (all p < 0.001) |
| XGBoost regression | Compared against random forest for gene expression prediction |
| Naive Bayes | Evaluated as alternative downstream classifier |
| Elastic-net logistic regression | Evaluated as alternative downstream classifier |
| Cohen's d (effect size) | Reported for variant effect quantification tasks |
| Pearson correlation | Gene expression prediction accuracy metric |
| Mean squared error (MSE) | Secondary metric for gene expression prediction |

---

## Reference Count
40
