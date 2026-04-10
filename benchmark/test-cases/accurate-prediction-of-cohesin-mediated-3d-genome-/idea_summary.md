## Working title

ChIPr: Predicting cohesin-mediated 3D genome organization from 2D chromatin features

## Core question

Can we accurately predict cohesin-mediated chromatin interaction strength (ChIA-PET / Hi-C) between any two genomic loci using cheaper, more accessible ChIP-Seq and other 2D chromatin features?

## Motivation / gap

- 3D genome organization (loops, TADs) influences gene regulation, replication, and repair
- ChIA-PET and Hi-C experiments are expensive, time-consuming, require tens to hundreds of millions of cells, and are hard to optimize
- Cohesin is a well-established key determinant of 3D genome organization
- Predicting 3D contacts from cheaper 1D/2D data (ChIP-Seq, accessibility, etc.) would greatly expand the scope of 3D genome studies

## Core contribution

- Present ChIPr (Chromatin Interaction Predictor), a suite of regression models (deep neural network, random forest, gradient boosting) to predict cohesin-mediated chromatin interactions
- Comprehensive benchmarks across four cell lines showing predictions correlate well with experimental ChIA-PET data
- Show the approach generalizes across cell types and can leverage readily available ChIP-Seq features

## Method in brief

- Input features: ChIP-Seq peaks for cohesin subunits (RAD21, SMC3), CTCF, histone marks, DNase-seq, and genomic distance
- Output: predicted interaction strength (contact frequency) for any pair of loci
- Three model architectures: DNN, random forest, gradient boosting
- Training and evaluation on matched ChIA-PET data in four cell lines
- Cross-cell-line generalization tests

## Target venue

Genome Biology
