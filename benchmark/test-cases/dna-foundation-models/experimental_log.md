# Experimental Log: DNA Foundation Models Benchmark

## Models Under Test

| Model | Params | Architecture | Embedding Dim | Max Input | Pre-training Data |
|-------|--------|-------------|---------------|-----------|-------------------|
| DNABERT-2 | 117M | BERT + ALiBi | 768 | No hard limit | 135 species genomes |
| NT-v2 | 500M | BERT | 1024 | 12K nt | 850 species genomes |
| HyenaDNA | 30M | Decoder + Hyena operators | 256 | 1M nt | Human genome only |
| Caduceus-Ph | ~35M | SSM (BiMamba) | 256 | 131K nt | Multi-species |
| GROVER | 117M | Transformer encoder | 768 | ~2K nt | Multi-species |

## Baselines
- Task-specific CNN (3 conv layers: 64/128/256 channels, trained end-to-end)
- Enformer (196K bp input, hidden states and output tracks)
- Sei (hidden states and 21,907 output tracks)
- AlphaGenome (specialized variant effect predictor)

## Sequence Classification Results (AUC, mean token pooling)

### Human genome (selected tasks)
- Splice site donor: DNABERT-2 0.906, Caduceus 0.854, NT-v2 0.820, GROVER 0.819, HyenaDNA 0.813
- Splice site acceptor: DNABERT-2 0.897, Caduceus 0.845, GROVER 0.804, HyenaDNA 0.795, NT-v2 0.793
- Coding region: Caduceus 0.974, GROVER 0.959, DNABERT-2 0.944, HyenaDNA 0.941, NT-v2 0.929
- Promoter GM12878: Caduceus 0.987, DNABERT-2 0.986, GROVER 0.984, NT-v2 0.984, HyenaDNA 0.976
- Enhancer: DNABERT-2 0.872, NT-v2 0.867, GROVER 0.855, Caduceus 0.838, HyenaDNA 0.834
- TFBS 1: Caduceus 0.880, GROVER 0.862, DNABERT-2 0.838, NT-v2 0.832, HyenaDNA 0.830

### Multi-species (selected tasks)
- Arabidopsis TATA promoter: HyenaDNA 0.961, DNABERT-2 0.951, NT-v2 0.950, GROVER 0.949, Caduceus 0.937
- Human vs worm: Caduceus 0.992, GROVER 0.984, DNABERT-2 0.980, NT-v2 0.979, HyenaDNA 0.950

### Epigenetic modifications (selected tasks)
- Human 5mC: Caduceus 0.783, GROVER 0.744, NT-v2 0.738, DNABERT-2 0.685, HyenaDNA 0.684
- Yeast H3: Caduceus 0.929, DNABERT-2 0.914, GROVER 0.906, HyenaDNA 0.900, NT-v2 0.895
- Yeast H4: DNABERT-2 0.931, Caduceus 0.930, NT-v2 0.910, GROVER 0.908, HyenaDNA 0.898

## Pooling Strategy Impact (AUC improvement: summary -> mean token)
- DNABERT-2: +4.0% (IQR 2.0-5.5%)
- NT-v2: +6.8% (IQR 3.7-9.6%)
- HyenaDNA: +8.7% (IQR 4.6-12.9%)
- Caduceus-Ph: +5.9% (IQR 2.8-9.1%)
- GROVER: +1.4% (IQR 0.7-1.9%)
- Mean pooling significantly better on 35-42 of 52 binary datasets per model (DeLong p<0.01)

## Gene Expression Prediction (Pearson correlation, MSE)
- Short seq (6K bp): all models ~0.12 correlation, ~0.235 MSE (near-indistinguishable)
- HyenaDNA-450K (196K bp): 0.137 corr, 0.226 MSE (significant improvement p<0.001)
- Enformer (196K bp): 0.129 corr, 0.227 MSE

## Variant Effect Prediction

### Pathogenic vs common SNPs (6K bp context, AUC)
- NT-v2: 0.732 (Cohen's d 0.881) -- BEST
- Caduceus: 0.696 (d=0.735)
- Enformer hidden: 0.688 (d=0.727)
- Sei output: 0.664 (d=0.605)
- HyenaDNA: 0.612 (d=0.395)
- GROVER: 0.603 (d=0.369)
- DNABERT-2: 0.538 (d=0.134) -- SURPRISINGLY BAD

### QTL prediction -- foundation models LOSE to specialized
- eQTL: AlphaGenome 0.803 >> Enformer 0.774 >> Caduceus 0.649 >> HyenaDNA 0.612 >> NT-v2 0.609 >> GROVER 0.590 >> DNABERT-2 0.570
- ipaQTL: AlphaGenome 0.864 >> Enformer 0.692 >> NT-v2 0.602 >> Caduceus 0.568 >> GROVER 0.476 >> DNABERT-2 0.469 >> HyenaDNA 0.448

## Pre-training Data Diversity (HyenaDNA retrained on multi-species)
- 14 of 49 datasets showed significant improvement
- 5mC: 0.707 -> 0.749 (+5.9%)
- 3 datasets worse (human enhancer, open chromatin, yeast marks)

## Runtime (1000 reps)
- Short seqs (<2K nt): GROVER fastest
- Long seqs (>100K nt): HyenaDNA best scaling
- NT-v2: highest latency but most stable (~2.5s constant across lengths)

## Ground Truth Reference
- bioRxiv DOI: 10.1101/2024.08.16.608288
- Published: Nature Communications, DOI 10.1038/s41467-025-65823-8
