## Working title

ScopeDTI: Semi-inductive dataset construction and framework optimization for practical drug-target interaction prediction

## Core question

Can a large-scale semi-inductive dataset combined with an optimized deep learning framework integrating 3D structural representations substantially improve drug-target interaction prediction, particularly in the challenging inductive setting where both drugs and targets are unseen during training?

## Motivation / gap

- Deep learning DTI methods show strong benchmark performance but limited real-world applicability due to data constraints
- Existing benchmark datasets (Human, BindingDB, KIBA) are small and lack diversity, leading to overestimated performance
- The inductive scenario (both drug and protein absent from training) is the most practically relevant for novel DTI discovery but remains highly challenging
- Most DTI frameworks fail to leverage 3D structural information for both compounds and proteins

## Core contribution

- Construct a large-scale, balanced semi-inductive human DTI dataset from 13 public repositories, expanding data volume by up to 100-fold versus common benchmarks
- Develop the SCOPE model integrating 3D protein and compound representations, graph neural networks, and bilinear attention for cross-domain interaction capture
- Demonstrate consistent outperformance across multiple datasets using semi-inductive split strategy
- Validate predictions experimentally with drug-target binding assays
- Release open-access tools and datasets

## Method in brief

ScopeDTI aggregates and curates interaction data from 13 public databases with bias filtering to reduce annotation artifacts. The SCOPE model encodes 3D protein structures and 3D molecular conformations with graph neural networks, using a bilinear attention mechanism to model drug-protein interactions. Evaluation uses AUROC, AUPRC, accuracy, sensitivity, and specificity across transductive, semi-inductive, and fully inductive splits on BindingDB, Human, KIBA, and the proprietary SCOPE dataset.

## Target venue

Nature Communications
