# Experimental Log -- Metagenomic classification benchmarking (long reads)

## 2024-01-15 -- Species-level classification accuracy on synthetic datasets

Average F1 score across seven synthetic datasets (species level).

| Tool | Type | Avg Precision | Avg Recall | Avg F1 |
|------|------|-------------|-----------|--------|
| Minimap2 | General mapper | 0.91 | 0.88 | 0.89 |
| Ram | General mapper | 0.90 | 0.87 | 0.88 |
| Kraken2 (nt) | Kmer-based | 0.85 | 0.83 | 0.84 |
| Centrifuge | Kmer-based | 0.82 | 0.80 | 0.81 |
| MetaMaps | Mapping-based | 0.86 | 0.82 | 0.84 |
| CLARK | Kmer-based | 0.80 | 0.78 | 0.79 |
| Kaiju (protein) | Protein-based | 0.78 | 0.85 | 0.81 |
| Diamond (protein) | Protein-based | 0.76 | 0.84 | 0.80 |

General-purpose mappers match or exceed specialized tools on accuracy.

## 2024-02-05 -- Runtime and resource usage

Benchmarked on synthetic dataset 1 (1M reads, ~10 Gb).

| Tool | Wall time (min) | Peak RAM (GB) | Speed category |
|------|----------------|--------------|---------------|
| Kraken2 | 3.2 | 48 | Fast |
| Centrifuge | 4.5 | 32 | Fast |
| CLARK | 5.1 | 52 | Fast |
| Minimap2 | 32.0 | 12 | Moderate |
| Ram | 28.5 | 14 | Moderate |
| MetaMaps | 45.0 | 22 | Slow |
| Kaiju | 18.0 | 28 | Moderate |
| Diamond | 55.0 | 8 | Slow |

Minimap2/Ram are ~10x slower than Kraken2 but use ~4x less RAM.

## 2024-02-22 -- Mock community evaluation (ZymoBIOMICS)

Species-level L1 distance (lower is better) on ZymoBIOMICS mock with known composition.

| Tool | L1 distance | Species detected (of 10) | False positives |
|------|------------|-------------------------|----------------|
| Minimap2 | 0.05 | 10 | 2 |
| Ram | 0.06 | 10 | 3 |
| Kraken2 | 0.09 | 10 | 12 |
| Centrifuge | 0.11 | 10 | 18 |
| MetaMaps | 0.07 | 10 | 5 |

General mappers produce fewer false positives on mock communities.

## 2024-03-08 -- Abundance range detection (0.0001% to 20%)

Detection sensitivity at varying relative abundances.

| Abundance (%) | Minimap2 detected | Kraken2 detected | Kaiju detected |
|---------------|------------------|-----------------|---------------|
| 20.0 | Yes | Yes | Yes |
| 5.0 | Yes | Yes | Yes |
| 1.0 | Yes | Yes | Yes |
| 0.1 | Yes | Yes | Yes |
| 0.01 | Yes | Yes | Partial |
| 0.001 | Partial | Partial | No |
| 0.0001 | No | No | No |

All tools struggle below 0.001% abundance.

## 2024-03-25 -- Unknown species scenario

Synthetic dataset with 30% reads from species absent from reference databases.

| Tool | Classified (%) | Correctly unclassified (%) | Misclassified (%) |
|------|---------------|--------------------------|-------------------|
| Minimap2 | 68 | 28 | 4 |
| Kraken2 | 82 | 8 | 10 |
| Centrifuge | 79 | 10 | 11 |
| Kaiju | 75 | 18 | 7 |

Kraken2/Centrifuge over-classify unknown reads; mapping-based tools are more conservative.
