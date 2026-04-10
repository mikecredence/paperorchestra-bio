# Experimental Log -- Structure-Function Coupling of Human Brain Connectome with Development

## 2024-01-15 -- Cohort and imaging summary

| Parameter | Value |
|-----------|-------|
| Dataset | HCP-Development |
| Participants (N) | 439 |
| Age range (years) | 5.7 - 21.9 |
| Mean age (years) | 14.2 |
| Imaging modalities | T1w/T2w ratio, dMRI, rs-fMRI |
| Cortical parcellation | 360 regions (Glasser HCP-MMP1.0) |
| Communication models tested | 5 (shortest path, navigation, search information, communicability, diffusion) |
| Gene expression source | Allen Human Brain Atlas |

## 2024-02-01 -- Group-level SC-FC coupling across cortical regions

Adjusted R-squared from multilinear model predicting FC from MPC + WMC communication models.

| Measure | Value |
|---------|-------|
| Mean adjusted R-squared | 0.14 |
| SD of adjusted R-squared | 0.08 |
| Min adjusted R-squared | 0.03 |
| Max adjusted R-squared | 0.45 |
| Significance threshold | p < 0.05 (1000 spin-test permutations) |

Regions with significant coupling included postcentral gyrus, precentral gyrus, paracentral lobule, superior temporal gyrus, middle frontal gyrus, superior parietal lobule, cingulate gyrus, and occipital lobe.

## 2024-02-20 -- SC-FC coupling by Yeo 7-network assignment

| Functional network | Mean SC-FC coupling (adj. R-squared) | SD | Rank |
|--------------------|--------------------------------------|------|------|
| Visual | 0.28 | 0.08 | 1 |
| Somatomotor | 0.22 | 0.09 | 2 |
| Dorsal attention | 0.15 | 0.11 | 3 |
| Default mode | 0.13 | 0.13 | 4 |
| Frontoparietal | 0.11 | 0.12 | 5 |
| Ventral attention | 0.09 | 0.10 | 6 |
| Limbic | 0.07 | 0.11 | 7 |

SC-FC coupling is strongest in sensory-motor networks and weakest in limbic areas, consistent with the sensory-fugal gradient of evolutionary cortical expansion.

## 2024-03-05 -- Developmental trajectories of SC-FC coupling (GAM results)

| Network | Beta (coupling change/year) | p-value | % regions significant (FDR q < 0.05) |
|---------|----------------------------|---------|--------------------------------------|
| Somatomotor | +0.012 | 1.2e-06 | 72% |
| Frontoparietal | +0.010 | 3.8e-05 | 65% |
| Dorsal attention | +0.009 | 8.5e-05 | 58% |
| Default mode | +0.008 | 2.1e-04 | 52% |
| Ventral attention | +0.006 | 1.5e-03 | 38% |
| Visual | +0.003 | 0.042 | 22% |
| Limbic | +0.002 | 0.15 | 12% |

Developmental changes are dominated by increases in higher-order association networks during adolescence.

## 2024-03-20 -- Cognitive association analysis

| Cognitive domain | Correlation with SC-FC coupling (r) | p-value |
|-----------------|--------------------------------------|---------|
| Total cognition composite | 0.23 | < 0.001 |
| Executive function | 0.19 | < 0.005 |
| Processing speed | 0.17 | < 0.01 |
| Working memory | 0.15 | < 0.05 |
| Episodic memory | 0.11 | 0.06 |

## 2024-04-05 -- Spatial correlation with cortical organizational features

| Feature | Spearman rho | p-value (spin test) |
|---------|-------------|---------------------|
| Evolutionary cortical expansion | 0.52 | < 0.001 |
| T1w/T2w myelin map | 0.61 | < 0.001 |
| Functional principal gradient (G1) | 0.58 | < 0.001 |
| Cortical thickness | -0.22 | 0.035 |
| Surface area | 0.15 | 0.12 |

## 2024-04-20 -- Gene expression analysis (PLS regression with Allen Brain Atlas)

| GO term / Pathway | Association direction | FDR q-value |
|-------------------|----------------------|-------------|
| Oligodendrocyte differentiation | Positive | < 0.001 |
| Myelination | Positive | < 0.005 |
| Axon ensheathment | Positive | < 0.01 |
| Astrocyte development | Negative | < 0.005 |
| Synaptic signaling | Negative | < 0.01 |
| Neurotransmitter transport | Negative | 0.012 |
| Ion channel activity | Mixed | 0.032 |

Developmental increase in SC-FC coupling is positively associated with oligodendrocyte/myelination pathways and negatively associated with astrocyte-related genes, suggesting white matter maturation as a key biological driver.

## Ground Truth Reference

- bioRxiv DOI: 10.1101/2023.09.11.557107
- Published DOI: 10.7554/eLife.93325
- Venue: eLife
- Year: 2024
