## Working title

Guiding Discovery of Protein Sequence-Structure-Function Relationships via In Silico Screening with AlphaFold2 and FFT Docking

## Core question

Can a high-throughput in silico pipeline coupling AlphaFold2 structure prediction with Fast Fourier Transform (FFT) docking predict enzyme enantioselectivity and reactivity, thereby guiding protein engineering without exhaustive experimental screening?

## Motivation / gap

- Protein engineering for novel catalysts is powerful but bottlenecked by labor-intensive expression and screening
- The sequence-structure-function paradigm is well known, but computational pipelines that traverse all three levels at scale are lacking
- AlphaFold2 can predict structures, but connecting predicted structures to functional predictions (enantioselectivity, reactivity) in a high-throughput manner has not been demonstrated

## Core contribution

- Development of a high-throughput in silico sequence-structure-function pipeline: sequence -> AlphaFold2 structure -> FFT docking -> functional prediction
- Benchmarking on an ancestral sequence library of fungal flavin-dependent monooxygenases (FDMOs)
- Predicted enantioselectivities and reactivities correlate well with experimental screens
- Pipeline captures known enantioselectivity changes across the phylogenetic tree
- Application of ensemble decision tree models and explainable AI to identify structure-function determinants

## Method in brief

We take an ancestral sequence library of fungal flavin-dependent monooxygenases. Each sequence is folded with AlphaFold2, then FFT-based docking (e.g., ClusPro or similar) places the substrate in the active site. Docking poses are scored to predict enantioselectivity (R vs S product ratio) and reactivity. Predictions are validated against existing experimental screens of an available protein subset. Ensemble decision tree models (random forest / gradient boosting) are trained on structural descriptors, and explainable AI (SHAP) identifies which structural features drive selectivity.

## Target venue

Bioinformatics
