# Experimental Log

> Pre-writing data tables and observations for the digital telomere measurement by long-read sequencing study.

---

## Datasets and Sample Cohorts

| Cohort | N | Source | Description |
|--------|---|--------|-------------|
| Healthy donors (aging) | 14 | PBLs | Aged 18-77 years, cross-sectional |
| Young cohort | 5 | PBLs | Ages 18-20 |
| Middle cohort | 6 | PBLs | Ages 35-65 |
| Elder cohort | 3 | PBLs | Ages >70 |
| RTEL1 mutants | 7 | PBLs | Healthy carriers (solid outline) and diseased carriers (dashed outline) |
| TBD evaluation patient | 1 | PBLs / bone marrow biopsy | Stanford hospital, potential TBD |
| Colorectal carcinoma | 20 | Benign + malignant colonic tissue | Patient-matched pairs |
| TIN2 mutant hESCs | 3 genotypes | Cell culture | Wild-type, 284R het, 284R hom |
| TERT knockout hESCs | Time series | Cell culture | 66-108 days post Cre-mediated knockout |
| Total samples | ~63 | Various | Healthy + diseased combined |

---

## Methods Compared

| Method | Type | Resolution | Input DNA | Limitations |
|--------|------|-----------|-----------|-------------|
| Telometer (this work) | Nanopore long-read sequencing | 30-40 bp precision | Less than TRF/flow-FISH | Requires long-read sequencer |
| TRF Southern blot | Hybridization | Coarse mean | High | Overestimates by up to several thousand bp |
| Flow-FISH | Fluorescence hybridization | Relative mean | Moderate | Overestimates by ~1500 bp on average; limited to PBLs |
| qPCR | Amplification | Relative content | Low | No distribution info |
| STELA | PCR of chromosome ends | Preferentially short | Low | Polymerase processivity limit |
| TeSLA | Adapter-ligated fragments | Preferentially short | Low | Polymerase processivity limit |

---

## Experiment 1: Method Validation - Telomere Capture vs. Whole Genome Sequencing

Fig. 1B: Head-to-head comparison of telomere length distributions from a single HEK 293T DNA source prepared by telomere capture versus whole genome sequencing. Distributions are highly concordant.

| Library Prep Method | Telomeres per Gigabase | Distribution Concordance |
|--------------------|-----------------------|------------------------|
| Telomere capture | Several thousand-fold enriched | High concordance |
| Whole genome sequencing | Low (telomeres are tiny fraction of genome) | Reference distribution |

Fig. 1C: Telomeres per gigabase sequenced is dramatically higher for telomere capture than whole genome.

---

## Experiment 2: Correlation with Gold-Standard Methods

Fig. 1D-G: Digital mean telomere length correlated with TRF Southern blot and flow-FISH.

| Comparison | Correlation | Systematic Bias |
|-----------|------------|-----------------|
| Telometer mean vs. TRF | High (strong positive correlation) | TRF overestimates by up to several thousand bp |
| Telometer mean vs. flow-FISH | High (strong positive correlation) | Flow-FISH overestimates by ~1500 bp on average |
| Telometer mean vs. qPCR | Positive correlation | qPCR provides relative not absolute |

---

## Experiment 3: Measurement Precision by Bootstrapping

Fig. 1H: Standard error of measurement decays exponentially with additional telomere measurements.

| Number of Telomere Reads | Approximate Standard Error (bp) | Trend |
|--------------------------|--------------------------------|-------|
| Low (~50) | High (>100 bp) | Exponential decay |
| Moderate (~200) | Moderate (~50-80 bp) | Decreasing |
| High (~500+) | Approaching 30-40 bp | Asymptotic minimum |

Maximal precision plateau: 30-40 base pairs.

---

## Experiment 4: Telomere Attrition in TIN2 Mutant hESCs

Fig. 2A: Telomere length distributions of wild-type, 284R heterozygous, and 284R homozygous TIN2 mutant hESCs.

| Genotype | Mean Telomere Length | Distribution Shape |
|----------|---------------------|--------------------|
| Wild-type TIN2 | Longest | Normal-like, centered at longer lengths |
| TIN2 284R heterozygous | Intermediate | Shifted leftward |
| TIN2 284R homozygous | Shortest | Further leftward shift, more short telomeres |

Fig. 2C: Stacked bar graphs of telomere length fractions by TIN2 genotype show increasing short-telomere fraction with increasing mutation dosage.

---

## Experiment 5: Telomere Attrition Post TERT Knockout in hESCs

Fig. 2B: Telomere length distributions of hESCs 66 to 108 days after Cre-mediated TERT knockout.

| Days Post TERT-KO | Mean Telomere Length | Short Telomere Fraction | Long Telomere Fraction |
|-------------------|---------------------|------------------------|----------------------|
| 66 | Longest in series | Lowest | Highest |
| ~80 | Intermediate | Increasing | Decreasing |
| ~95 | Shorter | Further increase | Further decrease |
| 108 | Shortest in series | Highest | Lowest |

Fig. 2D: Stacked bar graphs show progressive accumulation of short telomeres over time post TERT-KO.

Fig. 2E: Linear regression of telomere length summary statistics versus days post TERT-KO shows negative slope for all quartiles.

---

## Experiment 6: De Novo Telomere Elongation

Fig. 2 describes de novo telomere addition by overexpression of the telomerase catalytic core in a cell line with stable telomeres.

| Condition | Effect on Telomere Length | Chromosome Preference |
|-----------|--------------------------|----------------------|
| Telomerase overexpression | Elongation observed | Chromosomes with shorter first-quartile telomeres show more elongation |
| Control (no overexpression) | Stable telomeres | N/A |

Key finding: More significant elongation occurs at chromosomes with shorter first-quartile telomere lengths, providing novel evidence for preferential telomerase action at the shortest telomeres in humans.

---

## Experiment 7: Healthy Human Aging - Telomere Length vs. Age

Fig. 3A: Telomere length distributions from PBLs of 14 healthy individuals aged 18-77 years.

| Age Group | N | Mean Telomere Length | Median | Q1 | Q3 |
|-----------|---|---------------------|--------|----|----|
| Young (18-20) | 5 | Longest | Longest | Longest | Longest |
| Middle (35-65) | 6 | Intermediate | Intermediate | Intermediate | Intermediate |
| Elder (>70) | 3 | Shortest | Shortest | Shortest | Shortest |

Fig. 3D: Donor age correlates with mean, median, Q1, and Q3 telomere lengths.

Fig. 3E: Linear regressions of summary statistics versus donor age.

| Statistic | Rate of Decline (bp/year) | Relative Slope |
|-----------|--------------------------|----------------|
| Mean | ~24 | Reference |
| Median | ~24 | Similar to mean |
| Q3 (75th percentile) | Steeper than Q1 | Faster loss of long telomeres |
| Q1 (25th percentile) | Shallower than Q3 | Slower loss of short telomeres |

The 24 bp/year rate closely agrees with earlier cross-sectional TRF estimates from over 1100 human PBL DNA samples.

Fig. 3D: Wilcoxon rank-sum test comparing age cohorts shows significant differences (p-values reported).

---

## Experiment 8: Telomere Length Fraction Analysis in Aging

Fig. 3H: Fraction of telomeres of various size bins across aging cohorts.

| Telomere Size Fraction | Trend with Age | Notes |
|----------------------|----------------|-------|
| Very short (<2 kb) | Relatively stable | Exception to general trend |
| Short (2-4 kb) | Relatively stable | Exception to general trend |
| Medium-short (4-6 kb) | Increases with age | Accumulation of shorter telomeres |
| Medium (6-8 kb) | Increases with age | Becomes dominant fraction |
| Medium-long (8-10 kb) | Decreases with age | Shrinking fraction |
| Long (10-12 kb) | Decreases with age | Progressive loss |
| Very long (>12 kb) | Decreases steeply with age | Most rapid loss |

Key observation: The two shortest fractions appear relatively stable with age in PBLs, while longer fractions shrink progressively.

---

## Experiment 9: Telomere Biology Disorders - RTEL1 Mutations

Fig. 3B: Telomere length distributions from PBLs of 7 RTEL1 mutant individuals.

| RTEL1 Status | Telomere Distribution | Short Telomere Accumulation | Clinical Phenotype |
|-------------|----------------------|---------------------------|-------------------|
| Healthy carrier | Shorter than age-matched controls | Moderate | No overt disease |
| Diseased carrier | Much shorter than age-matched controls | Pronounced | TBD manifestations |

The accumulation of short telomeres is more pronounced in diseased carriers and correlates with phenotypic severity.

---

## Experiment 10: TBD Evaluation Patient (TINF2 Mutation)

Fig. 3C: Telomere distributions from PBLs or bone marrow biopsy DNA of a patient under evaluation for potential TBD.

| Finding | Details |
|---------|---------|
| Mutation discovered | Previously undescribed frameshift in DC-patch of TINF2 (p.Gln298fs) |
| Clinical presentation | CMML, pulmonary fibrosis, short telomeres for age group |
| Telomere distribution | Markedly shifted toward short telomeres |

---

## Experiment 11: Colorectal Carcinoma Cohort - Benign vs. Malignant Tissue

Fig. 4A: Grid box and violin plots for 20 individuals showing patient-matched benign (red) and malignant (blue) colonic tissue.

| Tissue Type | N | Mean Telomere Length | Comparison |
|------------|---|---------------------|-----------|
| Benign colonic epithelium | 20 | Longer | Reference |
| Malignant colonic tissue | 20 | Shorter | Wilcoxon rank-sum test, p-values reported per patient |

Fig. 4B: Linear regression of benign tissue telomere summary statistics vs. patient age.

Fig. 4C: Linear regression analysis for malignant tissue vs. patient age.

| Tissue | Statistic | Correlation with Age |
|--------|-----------|---------------------|
| Benign | Mean | Negative correlation (shortens with age) |
| Benign | Median | Negative correlation |
| Malignant | Mean | Variable, weaker correlation |
| Malignant | Median | Variable |

---

## Experiment 12: Machine Learning Classification - Healthy vs. TBD

A binary classification model was trained to distinguish healthy individuals from those with telomere biology disorders.

| Feature Set | Input | Model Type | Cross-Validated Accuracy |
|------------|-------|-----------|------------------------|
| Telomere distribution statistics | Mean, median, Q1, Q3, fractions | ML binary classifier | High accuracy reported |
| Combined features | Distribution shape parameters | Neural network / ensemble | Robust classification |

The model leverages the richer distributional information (not just mean) available from long-read sequencing.

---

## Chromosome-Specific Observations

| Observation | Evidence |
|-------------|----------|
| Individual telomeres anchored to specific chromosomes | Alignment to T2T human genome |
| Preferential telomerase elongation at shortest telomeres | Chromosome-resolved analysis post-overexpression |
| Chromosome-specific telomere length variation | Visible in per-chromosome distributions |

---

## Technical Parameters

| Parameter | Value |
|-----------|-------|
| Sequencing platform | Oxford Nanopore Technologies (ONT) |
| Also compatible with | PacBio HiFi |
| Reference genome | T2T human genome assembly |
| Telomere definition | Terminal repeat to final two consecutive repeats before subtelomeric sequence |
| Enrichment fold | Several thousand-fold for telomere capture |
| Measurement precision | 30-40 bp (asymptotic) |
| Pipeline name | Telometer |
| Attrition rate (healthy aging) | ~24 bp/year (mean and median in PBLs) |
| Sample size (total) | ~63 healthy and diseased samples |
| Reference count | 42 |

---

## Key Findings Summary

| Finding | Significance |
|---------|-------------|
| Q3 telomere length decreases faster than Q1 with age | Longer telomeres are preferentially lost during aging |
| Two shortest telomere fractions remain stable with age in PBLs | Possible negative selection of cells with very short telomeres |
| TBD patients show pronounced short telomere accumulation | Correlates with phenotypic severity |
| Novel TINF2 frameshift (p.Gln298fs) discovered | New mutation associated with CMML and pulmonary fibrosis |
| TRF overestimates mean telomere length | Up to several thousand bp due to digestion conditions |
| Flow-FISH overestimates mean | By ~1500 bp on average |
| ML classifier separates healthy from TBD | Uses distributional features beyond mean |
