# Experimental Log -- Regional Patterns of Human Cortex Development and Underlying Neurobiology

## 2024-01-20 -- Normative model and dataset overview

| Parameter | Value |
|-----------|-------|
| Modeling approach | Lifespan normative model of cortical thickness |
| Cross-sectional training datasets | Multiple large-scale MRI cohorts |
| Longitudinal validation cohort | IMAGEN (N > 8,000 adolescents) |
| Cortical parcellation | Desikan-Killiany atlas (68 regions) |
| Molecular data sources | PET neurotransmitter receptor atlases, single-cell transcriptomics |
| Life stages analyzed | Childhood, adolescence, adulthood, aging |
| Spatial significance testing | Spin-test permutation (10,000 permutations) |

## 2024-02-10 -- Variance explained by molecular/cellular features in childhood-adolescence

Dominance analysis: proportion of variance in cortical thickness developmental trajectories explained by each molecular/cellular feature category during childhood and adolescence.

| Feature category | Variance explained (R-squared) | Relative importance (%) |
|-----------------|-------------------------------|------------------------|
| Dopaminergic receptors (D1, D2) | 0.18 | 36.0 |
| Inhibitory neuron density (SST, PV, VIP) | 0.12 | 24.0 |
| Glial cell populations (astrocytes, oligodendrocytes) | 0.09 | 18.0 |
| Brain-metabolic features (glucose, oxygen) | 0.07 | 14.0 |
| Excitatory neuron density | 0.04 | 8.0 |
| **Combined model** | **0.50** | **100.0** |

During childhood and adolescence, dopaminergic receptors are the strongest predictor of cortical thickness change patterns, with the combined model explaining up to 50% of spatial variance.

## 2024-03-01 -- Variance explained by molecular features in adulthood

| Feature category | Variance explained (R-squared) | Relative importance (%) |
|-----------------|-------------------------------|------------------------|
| Cholinergic receptors/transporters | 0.15 | 33.3 |
| Glutamatergic receptors (NMDA, AMPA, mGluR5) | 0.13 | 28.9 |
| Serotonergic receptors (5-HT1A, 5-HT2A) | 0.08 | 17.8 |
| GABAergic markers | 0.05 | 11.1 |
| Dopaminergic receptors | 0.04 | 8.9 |
| **Combined model** | **0.45** | **100.0** |

During adulthood, cholinergic and glutamatergic systems dominate, replacing the dopaminergic dominance seen in development.

## 2024-03-20 -- Individual-level neurotransmitter-cortical thickness correlations (PET receptor maps)

| Receptor / transporter | Spearman rho with CT change (adolescence) | p (spin test) |
|------------------------|-------------------------------------------|---------------|
| D1 (dopamine) | 0.48 | < 0.001 |
| D2 (dopamine) | 0.42 | < 0.001 |
| DAT (dopamine transporter) | 0.35 | < 0.005 |
| 5-HT2A (serotonin) | 0.28 | < 0.01 |
| 5-HT1A (serotonin) | 0.22 | 0.02 |
| GABAA (benzodiazepine site) | 0.19 | 0.04 |
| mGluR5 (glutamate) | 0.15 | 0.08 |
| M1 (muscarinic) | 0.12 | 0.14 |
| CB1 (cannabinoid) | 0.09 | 0.25 |
| MU (opioid) | 0.07 | 0.31 |

## 2024-04-05 -- Validation in IMAGEN longitudinal cohort

| Metric | Cohort level | Single-subject level |
|--------|-------------|---------------------|
| Participants | > 8,000 | > 8,000 |
| Longitudinal timepoints | 2-3 per subject | 2-3 per subject |
| Age range (years) | 14 - 23 | 14 - 23 |
| Variance explained (molecular model) | 59% | 18% |
| Cross-validated R-squared | 0.54 | 0.15 |
| Permutation p-value | < 0.001 | < 0.001 |

Population-level associations between molecular brain organization and cortical thickness trajectories translate to individual longitudinal data, with 59% variance explained at cohort level and 18% at single-subject level.

## 2024-04-20 -- Cell-type contribution analysis (single-cell transcriptomics)

| Cell type | Correlation with CT developmental trajectory | p (spin test) | Direction |
|-----------|----------------------------------------------|---------------|-----------|
| SST+ inhibitory neurons | 0.44 | < 0.001 | Positive |
| PV+ inhibitory neurons | 0.38 | < 0.001 | Positive |
| VIP+ inhibitory neurons | 0.32 | < 0.005 | Positive |
| Astrocytes | 0.29 | < 0.01 | Positive |
| Oligodendrocytes | 0.25 | < 0.01 | Positive |
| Excitatory layer 2/3 neurons | 0.18 | 0.03 | Positive |
| Excitatory layer 5/6 neurons | 0.12 | 0.09 | Weak positive |
| Microglia | 0.08 | 0.22 | NS |

Inhibitory neuron subtypes, particularly SST+ and PV+ interneurons, show the strongest cell-type associations with cortical thickness developmental change patterns.

## Ground Truth Reference

- bioRxiv DOI: 10.1101/2023.05.05.539537
- Published DOI: 10.1038/s41467-024-52366-7
- Venue: Nature Communications
- Year: 2024
