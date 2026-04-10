# Experimental Log -- UBP5 and PRC2 in Arabidopsis

## 2024-01-20 -- Protein interaction screen

Identified UBP5 as interactor of SWINGER (PRC2 catalytic subunit) and PWO1 (PRC2-associated factor) via IP-MS. Confirmed by reciprocal co-IP.

### UBP5 interaction partners (top hits)

| Protein | Complex | Enrichment (fold over control) | p-value |
|---|---|---|---|
| SWINGER (SWN) | PRC2 | 8.5 | <0.001 |
| PWO1 | PRC2-associated | 6.2 | <0.001 |
| CLF | PRC2 | 3.1 | <0.01 |
| EMF2 | PRC2 | 2.4 | <0.05 |

## 2024-02-15 -- CRISPR-Cas9 ubp5 mutant generation

Generated two independent ubp5 alleles via CRISPR-Cas9. Both show frameshift leading to loss of function. Confirmed by Western blot (no UBP5 protein detected).

### Developmental phenotype comparison

| Trait | WT (Col-0) | ubp5-1 | ubp5-2 | Significance |
|---|---|---|---|---|
| Rosette leaf number at bolting | 12.3 | 16.8 | 17.1 | p<0.001 |
| Days to flowering | 28.5 | 35.2 | 34.8 | p<0.001 |
| Root length 10 DAG (cm) | 4.2 | 3.1 | 3.0 | p<0.01 |
| Silique length (mm) | 14.5 | 11.2 | 10.9 | p<0.01 |

ubp5 mutants show delayed flowering, more rosette leaves, shorter roots and siliques -- consistent with enhanced PRC2-mediated repression of developmental genes.

## 2024-03-10 -- Chromatin profiling (ChIP-seq)

### H2Aub and H3K27me3 changes in ubp5 vs WT

| Histone mark | Genes with increased signal in ubp5 | Genes with decreased signal in ubp5 | Net direction |
|---|---|---|---|
| H2Aub | 1,845 | 312 | Gain |
| H3K27me3 | 1,220 | 185 | Gain |

Loss of UBP5 leads to accumulation of H2Aub (expected -- deubiquitinase is gone) and also local H3K27me3 gain, suggesting coordinated reinforcement of repression.

### UBP5 binding at PRC2 motifs

| Genomic feature | % UBP5 peaks overlapping | Expected by chance |
|---|---|---|
| PRC2 recruiting motifs (telobox/RY) | 62% | 8% |
| H3K27me3 domains | 55% | 12% |
| Active promoters (H3K4me3) | 15% | 18% |
| Intergenic regions | 10% | 35% |

Strong preferential binding of UBP5 at PRC2-associated chromatin regions.

## 2024-04-05 -- Stress response assays

| Condition | WT survival (%) | ubp5 survival (%) | p-value |
|---|---|---|---|
| Drought (14 d water withholding) | 72 | 38 | <0.01 |
| Salt (150 mM NaCl, 10 d) | 65 | 41 | <0.01 |
| Cold (4C, 7 d then recovery) | 80 | 55 | <0.05 |

ubp5 mutants are significantly more sensitive to abiotic stress, supporting role of UBP5 in stress-responsive gene de-repression.

## 2024-04-20 -- RNA-seq summary

| Category | Upregulated in ubp5 | Downregulated in ubp5 |
|---|---|---|
| Total DEGs (|log2FC|>1, FDR<0.05) | 480 | 1,105 |
| PRC2 target genes among DEGs | 52 (11%) | 685 (62%) |

Majority of DEGs are downregulated in ubp5 -- consistent with enhanced repression when UBP5 is absent.
