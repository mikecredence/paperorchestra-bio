## Working title

Spatial and temporal pattern of structure-function coupling of human brain connectome with development

## Core question

How does the coupling between structural connectivity (SC) and functional connectivity (FC) of the brain develop across childhood and adolescence, and what are the genetic and cellular mechanisms underlying this developmental trajectory?

## Motivation / gap

- Brain structural circuitry shapes functional synchronization patterns that support complex cognitive and behavioural abilities, but the developmental dynamics of SC-FC coupling are poorly understood
- Prior work has focused on SC-FC coupling in adults but did not characterize its spatial heterogeneity and developmental trajectory from childhood to early adulthood
- The relative contributions of intracortical microstructure versus extracortical white matter projections to structure-function coupling remain unclear
- The transcriptomic architecture underlying heterogeneous developmental changes in SC-FC coupling has not been systematically characterized using the Allen Human Brain Atlas

## Core contribution (bullet form)

- Characterize SC-FC coupling across 439 participants aged 5.7 to 21.9 years using a multilinear model integrating both intracortical (microstructure profile covariance, MPC) and extracortical (white matter connectome communication models) structural connectivity to predict functional connectivity
- Demonstrate that SC-FC coupling is strongest in visual and somatomotor networks, consistent with evolutionary expansion gradients, myelin content, and the functional principal gradient
- Show that developmental changes in SC-FC coupling are heterogeneous across cortex, dominated by increases in somatomotor, frontoparietal, dorsal attention, and default mode networks
- Reveal that SC-FC coupling encodes individual differences in cognitive ability during development
- Link the spatial pattern of developmental SC-FC coupling changes to gene expression via PLS regression: positive association with oligodendrocyte-related pathways and negative association with astrocyte-related genes

## Method in brief

Multimodal MRI data (T1w/T2w ratio for intracortical microstructure, diffusion MRI for structural connectivity, resting-state fMRI for functional connectivity) from 439 HCP-Development participants aged 5.7-21.9 years. Microstructure profile covariance (MPC) computed from T1w/T2w ratio captures intracortical microstructural similarity. White matter connectome (WMC) derived from diffusion tractography with five communication models (shortest path, navigation, search information, communicability, diffusion). A multilinear regression predicts regional FC from combined MPC and WMC features, yielding per-node adjusted R-squared as the SC-FC coupling metric. Generalized additive models characterize nonlinear developmental trajectories. Spin-test permutation (1000 permutations) for spatial correlation significance. Partial least squares regression with Allen Human Brain Atlas gene expression data identifies transcriptomic correlates.

## Target venue

eLife
