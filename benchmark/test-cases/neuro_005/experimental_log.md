# Experimental Log: Competitive Interactions Shape Brain Dynamics Across Species

## Species and Datasets

| Species | N subjects | Parcellation | Regions | Imaging | Source |
|---------|-----------|-------------|---------|---------|--------|
| Human | 100 | Schaefer | 200 | rs-fMRI (HCP) | Human Connectome Project |
| Macaque | 19 | CHARM | 68 | rs-fMRI | PRIME-DE |
| Mouse | 10 | Allen CCFv3 | 52 | rs-fMRI | Gozzi lab |

## Model Variants Compared

| Model | Coupling | Description |
|-------|----------|-------------|
| Cooperative-only | Excitatory only | Positive coupling via structural connectivity |
| Cooperative-Competitive | Excitatory + Inhibitory | Modular cooperative + diffuse long-range competitive |
| Null (random) | Shuffled | Structural connectivity randomized |

## Key Results: Functional Connectivity Fitting

| Species | Model | FC correlation (r) | FCD KS-distance | Metastability |
|---------|-------|--------------------|-----------------|---------------|
| Human | Cooperative-only | 0.38 | 0.42 | 0.011 |
| Human | Cooperative-Competitive | **0.71** | **0.18** | **0.024** |
| Macaque | Cooperative-only | 0.35 | 0.45 | 0.009 |
| Macaque | Cooperative-Competitive | **0.65** | **0.21** | **0.019** |
| Mouse | Cooperative-only | 0.31 | 0.51 | 0.008 |
| Mouse | Cooperative-Competitive | **0.58** | **0.25** | **0.017** |

## Information-Theoretic Measures

| Species | Model | Synergy (bits) | Redundancy (bits) | Syn/Red ratio |
|---------|-------|----------------|--------------------|----|
| Human | Cooperative-only | 0.12 | 0.31 | 0.39 |
| Human | Coop-Competitive | **0.28** | 0.22 | **1.27** |
| Macaque | Coop-Competitive | **0.24** | 0.19 | **1.26** |
| Mouse | Coop-Competitive | **0.21** | 0.18 | **1.17** |

## Reservoir Computing: Computational Capacity

| Species | Model | Memory capacity | Nonlinear capacity | Total capacity |
|---------|-------|----|----|----|
| Human | Cooperative-only | 3.2 | 4.1 | 7.3 |
| Human | Coop-Competitive | **5.8** | **7.2** | **13.0** |
| Macaque | Coop-Competitive | **4.9** | **6.1** | **11.0** |
| Mouse | Coop-Competitive | **4.1** | **5.3** | **9.4** |

## Competitive Interaction Architecture
- Cooperative interactions: predominantly within-module (modular structure)
- Competitive interactions: predominantly between-module (long-range, diffuse)
- Ratio competitive/cooperative coupling strength conserved across species: ~0.3-0.4
- Network modularity of competitive weights: significantly lower than cooperative (p < 0.001)

## Statistical Tests
- Model comparison: paired t-test, Bonferroni corrected (p < 0.05/3 species)
- FC fitting: Pearson correlation between simulated and empirical FC matrices
- FCD: Kolmogorov-Smirnov distance between simulated and empirical FCD distributions
- Reservoir computing: 10-fold cross-validation

## Ground Truth Reference
- bioRxiv DOI: 10.1101/2024.10.19.619194
- Published: Nature Neuroscience, DOI 10.1038/s41593-026-02205-3
