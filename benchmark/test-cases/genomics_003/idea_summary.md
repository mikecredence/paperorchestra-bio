## Working title

Benchmarking Clustering, Alignment, and Integration Methods for Spatial Transcriptomics

## Core question

Which computational methods perform best for spatial domain clustering, tissue slice alignment, and multi-slice integration in spatial transcriptomics, and how do they compare across diverse datasets and experimental conditions?

## Motivation / gap

- Spatial transcriptomics (ST) is rapidly growing, but defining spatially coherent regions (clustering) and aligning/integrating multiple tissue slices remain challenging
- Many specialized ST methods have been developed that leverage spatial information, but no comprehensive benchmark exists
- Without benchmarks, users cannot make informed method choices, and developers lack clear targets for improvement

## Core contribution

- Systematic benchmark of state-of-the-art clustering, alignment, and integration algorithms for ST
- Evaluation across a wide range of real and simulated datasets varying in size, technology, species, and complexity
- Multiple evaluation metrics: ARI, UMAP visualization, layer-wise alignment accuracy, spot-to-spot alignment accuracy, spatial coherence score (SCS), and 3D reconstruction quality
- Practical guidelines for method selection based on dataset characteristics

## Method in brief

We will collect a diverse panel of real ST datasets (10x Visium, MERFISH, Slide-seq, etc.) across species (human, mouse) and tissues, plus simulated datasets with known ground truth. We will run published clustering methods, alignment methods, and integration methods with default and tuned parameters. Evaluation will use ARI for clustering, alignment accuracy (layer-wise, spot-to-spot) for alignment, SCS for spatial coherence, and UMAP visualization for qualitative assessment. 3D reconstruction will be evaluated where applicable.

## Target venue

Genome Biology
