# Experimental Log: Benchmarking Nanopore Metagenomics Classification

## Experiment 1: Classifier performance on R9 chemistry mock communities

Evaluated taxonomic classifiers on mock community data generated with ONT R9 flowcells at species level.

| Classifier  | Approach          | Precision | Recall | F1 score |
|------------|-------------------|-----------|--------|----------|
| Kraken2    | Exact k-mer       | 0.82      | 0.88   | 0.85     |
| Centrifuge | Exact k-mer       | 0.85      | 0.84   | 0.845    |
| Kaiju      | Translated search | 0.78      | 0.81   | 0.795    |
| MMseqs2    | Translated search | 0.80      | 0.79   | 0.795    |
| Minimap2   | Alignment-based   | 0.87      | 0.90   | 0.885    |

## Experiment 2: Impact of R10 chemistry on classifier performance

Compared classifiers on R10 versus R9 chemistry data.

| Classifier  | F1 (R9) | F1 (R10) | Delta   | Direction |
|------------|---------|----------|---------|-----------|
| Kraken2    | 0.85    | 0.91     | +0.06   | Improved  |
| Centrifuge | 0.845   | 0.80     | -0.045  | Declined  |
| Kaiju      | 0.795   | 0.84     | +0.045  | Improved  |
| MMseqs2    | 0.795   | 0.76     | -0.035  | Declined  |
| Minimap2   | 0.885   | 0.92     | +0.035  | Improved  |

## Experiment 3: Abundance estimation accuracy

Bray-Curtis dissimilarity between predicted and known relative abundances (lower is better).

| Classifier  | BC dissimilarity (R9) | BC dissimilarity (R10) |
|------------|----------------------|------------------------|
| Kraken2    | 0.12                 | 0.08                   |
| Centrifuge | 0.10                 | 0.14                   |
| Kaiju      | 0.18                 | 0.13                   |
| MMseqs2    | 0.15                 | 0.19                   |
| Minimap2   | 0.07                 | 0.05                   |

## Experiment 4: Runtime and resource usage

| Classifier | Wall time (min) | Peak RAM (GB) | Database size (GB) |
|-----------|----------------|---------------|-------------------|
| Kraken2   | 2.5            | 16            | 45                |
| Centrifuge| 4.1            | 8             | 12                |
| Kaiju     | 12.3           | 32            | 65                |
| MMseqs2   | 18.7           | 24            | 38                |
| Minimap2  | 8.9            | 12            | 22                |
