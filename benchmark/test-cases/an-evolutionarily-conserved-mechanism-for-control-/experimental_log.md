# Experimental Log -- tRNA thiolation and plant immunity

## 2024-01-08 -- Pathogen growth assay: cgb mutant susceptibility

Pseudomonas syringae pv. tomato DC3000 spray inoculation, bacterial counts at 3 dpi.

| Genotype | Bacterial titer (log10 CFU/cm2) | Fold vs WT |
|----------|-------------------------------|------------|
| Col-0 (WT) | 5.2 | 1.0x |
| cgb (rol5) | 7.1 | ~80x |
| ctu2 | 6.9 | ~50x |
| cgb + ROL5 (complemented) | 5.4 | ~1.6x |
| npr1-1 | 6.8 | ~40x |

Both cgb and ctu2 are dramatically hyper-susceptible, comparable to the known immune mutant npr1-1.

## 2024-01-25 -- tRNA thiolation assay (APM gel)

Thiolated tRNA fraction measured by APM-Northern for tRNA-Lys(UUU), tRNA-Glu(UUC), tRNA-Gln(UUG).

| Genotype | tRNA-Lys s2U (%) | tRNA-Glu s2U (%) | tRNA-Gln s2U (%) |
|----------|-----------------|-----------------|-----------------|
| Col-0 (WT) | 92 | 88 | 85 |
| cgb (rol5) | <5 | <5 | <5 |
| ctu2 | <5 | <5 | <5 |

Thiolation is essentially abolished in both mutants.

## 2024-02-12 -- ROL5-CTU2 physical interaction (co-IP)

| Bait | Prey | Detected |
|------|------|----------|
| ROL5-GFP | CTU2-HA | Yes (+++) |
| GFP alone | CTU2-HA | No |
| ROL5-GFP | HA alone | No |

Confirmed direct physical interaction, consistent with yeast NCS6-NCS2 complex.

## 2024-03-05 -- Translational reprogramming (ribosome profiling)

Translation efficiency (TE) changes upon immune activation (flg22 treatment, 6 h).

| Gene set | WT delta-TE (log2) | cgb delta-TE (log2) | p-value (WT vs cgb) |
|----------|-------------------|--------------------|--------------------|
| All genes | +0.02 | +0.01 | 0.85 |
| Immune-response genes | +0.45 | +0.12 | 2e-8 |
| Long proteins (>800 aa) | +0.38 | +0.05 | 5e-6 |
| SA-pathway genes | +0.52 | +0.08 | 1e-9 |

Translational upregulation of immune genes during defense is strongly compromised in cgb, especially for long proteins.

## 2024-03-20 -- NPR1 protein levels

Western blot quantification (normalized to actin), with and without SA treatment.

| Genotype | NPR1 protein (mock) | NPR1 protein (+SA) | Fold induction |
|----------|--------------------|--------------------|---------------|
| Col-0 (WT) | 1.0 | 4.8 | 4.8x |
| cgb (rol5) | 0.6 | 1.2 | 2.0x |
| ctu2 | 0.5 | 1.1 | 2.2x |

NPR1 accumulation is severely impaired in thiolation-deficient mutants, explaining reduced SA signaling.

## 2024-04-02 -- Transcriptional reprogramming (RNA-seq)

Number of differentially expressed genes (DEGs) upon flg22 treatment (|log2FC| > 1, FDR < 0.05).

| Genotype | Upregulated DEGs | Downregulated DEGs | Total DEGs |
|----------|-----------------|-------------------|-----------|
| Col-0 (WT) | 1245 | 890 | 2135 |
| cgb (rol5) | 620 | 510 | 1130 |

Transcriptional reprogramming is also partially compromised (roughly half as many DEGs).
