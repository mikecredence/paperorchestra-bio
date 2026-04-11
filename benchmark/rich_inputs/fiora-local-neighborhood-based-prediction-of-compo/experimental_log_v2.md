# Experimental Log: Fiora Mass Spectra Prediction

## Training Data Overview

| Library | Compounds | Spectra | Key Sources | Notes |
|---------|-----------|---------|-------------|-------|
| NIST 2017 | Large commercial library | Multiple per compound | Various experimental setups | Standard reference library |
| MS-Dial | Curated collection | Multiple per compound | RIKEN, various contributors | Accessible metadata including collision energies |
| Combined training | Merged NIST + MS-Dial | After deduplication | Both libraries | 80% train split |
| Validation split | 10% of combined | Held out | Same sources | Hyperparameter tuning |
| Test split | 10% of combined | Held out | Same sources | Final evaluation |

## External Evaluation Datasets

| Dataset | Year | Description | Use |
|---------|------|-------------|-----|
| CASMI 2016 challenge | 2016 | Unknown compounds for identification | Independent benchmark; high coverage distribution |
| CASMI 2022 challenge | 2022 | Unknown compounds for identification | Independent benchmark; more difficult |
| BMDMS-NP library | Published | Retention time reference values | RT evaluation |
| MS-Dial CCS | Published | Collision cross section values | CCS evaluation |

## Baseline Algorithms

| Algorithm | Type | Ionization Modes | Energy Levels | Notes |
|-----------|------|-----------------|---------------|-------|
| CFM-ID | Combinatorial fragmentation | Positive and negative | Fixed discrete levels | Trained on different dataset |
| ICEBERG | Neural network (global embeddings) | Positive only | Varies | State-of-the-art at time of study |
| Fiora | GNN edge prediction (local neighborhood) | Positive and negative (unified model) | Continuous collision energy | Proposed method |

## Graph Neural Network Architecture Comparison (Fig 2)

| Architecture | Type | Median Cosine Similarity (validation) | Performance Rank |
|-------------|------|---------------------------------------|-----------------|
| GCN | Graph convolutional network | Highest tier | 1-2 |
| RGCN | Relational graph convolutional network | Highest tier | 1-2 |
| GAT | Graph attention network | Lower | 3 |
| Transformer | Attention-based | Lower | 4 |

- Fig 2 shows median cosine similarity vs network depth (number of graph convolution layers)
- Error bars represent 95% confidence intervals
- Peak performance reached between 3 and 6 layers, then falls off
- GCN and RGCN outperform attention-based mechanisms (GAT and Transformer)
- Key finding: short-range local structural relationships are sufficient; deeper networks do not help

## Spectral Prediction Quality: Median Cosine Similarity (Table 1)

| Test Set | Ion Mode | Fiora | ICEBERG | CFM-ID |
|----------|----------|-------|---------|--------|
| NIST 2017 test | Positive | Best | Second | Third |
| NIST 2017 test | Negative | Best | N/A (pos only) | Third |
| MS-Dial test | Positive | Best | Second | Third |
| MS-Dial test | Negative | Best | N/A | Third |
| CASMI 2016 | Positive | Best | Second | Third |
| CASMI 2022 | Positive | Best | Second | Third |

- Fiora surpasses both ICEBERG and CFM-ID across all test sets and ionization modes
- ICEBERG only operates in positive ionization mode
- The performance gain over CFM-ID is even larger for negative spectra since Fiora trains a unified model

## Structural Similarity Analysis (Fig 3)

| Tanimoto Similarity Interval | Description | Fiora Performance | CFM-ID Performance | ICEBERG Performance |
|-----------------------------|-------------|-------------------|-------------------|---------------------|
| 0.0-0.2 | Very dissimilar to training | Lowest but still higher than baselines | Lowest | Lowest |
| 0.2-0.4 | Low similarity | Improving | Lower | Lower than Fiora |
| 0.4-0.6 | Moderate similarity | Good | Moderate | Moderate |
| 0.6-0.8 | High similarity | High | Improving | Improving |
| 0.8-1.0 | Very similar to training | Highest | High | High |

- Fig 3 shows cosine similarity at intervals of structural similarity (max Tanimoto via Morgan fingerprints, 2048 bits, radius 3)
- Results shown for positive ionization spectra for fair comparison across all algorithms
- CFM-ID was trained on a different dataset, so Tanimoto intervals do not reflect actual similarity for that model
- Fiora maintains higher cosine scores across all similarity ranges

## Molecular Embedding Analysis (Fig 4)

| Compound Superclass | Prediction Quality | Notes |
|--------------------|--------------------|-------|
| Lipids and lipid-like | Varies by subclass | Largest class |
| Organoheterocyclic | Generally good | Well-represented |
| Benzenoids | Good | Common in training |
| Organic acids | Good | Common in training |
| Phenylpropanoids | Moderate | Smaller class |

- Fig 4a: UMAP visualization of molecular graph embeddings color-coded by ClassyFire superclass
- Clear clustering by compound superclass demonstrates that Fiora learns meaningful structural relationships
- Fig 4b: Cosine similarity split by compound superclass shows prediction quality variation across chemical classes

## Retention Time and CCS Prediction (Fig 5)

| Property | Test Source | Metric | Performance | Deviation Threshold |
|----------|-----------|--------|-------------|-------------------|
| Retention time (RT) | BMDMS-NP library | Parity plot | Good correlation with ground truth | Dashed lines at +/- 30 sec |
| Collision cross section (CCS) | MS-Dial library | Parity plot | Good correlation with ground truth | Dashed lines at +/- 10% |

- Fig 5a: RT parity plot; diagonal = perfect prediction; most points cluster near diagonal
- Fig 5b: CCS parity plot; similar good agreement
- Fiora is the only model providing all three predictions (MS/MS spectra, RT, CCS) from molecular structure

## CASMI Challenge Analysis (Fig 6)

| Dataset | Metric | Fiora Trend | Optimistic Upper Bound |
|---------|--------|-------------|----------------------|
| CASMI 2016 | Cosine similarity vs peak intensity coverage | High; approaches upper bound at high coverage | Dotted line in figure |
| CASMI 2022 | Cosine similarity vs peak intensity coverage | Good; lower than 2016 (harder dataset) | Dotted line in figure |

- Fig 6 shows cosine similarity over peak intensity coverage for CASMI 2016 and 2022
- Dotted line describes optimistic upper bound (max cosine at given coverage)
- Occasional outliers above the bound arise from differences in fragment annotation tolerance (50 ppm relative for Fiora) vs cosine calculation tolerance (0.05 Da absolute)
- CASMI 2016 represents standard dataset with high coverage; CASMI 2022 is more challenging
- Merging spectra predicted at three collision energy steps used in CASMI 2016 experiment yields better simulation than predicting at the average CE

## Collision Energy Effects

| Strategy | Description | Performance |
|----------|-------------|-------------|
| Single average CE | Predict at mean of experimental CEs | Good |
| Multi-CE merge | Predict at each experimental CE, merge | Better than single average |
| Fixed CE (CFM-ID) | Discrete energy levels only | Limited flexibility |

- Predicting spectra at any given collision energy is a significant advance over fixed energy levels in CFM-ID
- Continuous CE modeling allows matching experimental conditions precisely

## Runtime Comparison (Table 2)

| Algorithm | Hardware | Predictions (all test sets) | Total Runtime | Relative Speed |
|-----------|----------|---------------------------|---------------|---------------|
| Fiora (GPU) | GPU-accelerated | All compounds at all CEs | Fastest | Reference |
| ICEBERG | CPU/GPU | Subset (positive only) | Slower | Slower |
| CFM-ID | CPU | Subset (fixed CEs) | Slowest | Slowest |

- Fiora is the only software that predicted all compounds at all collision energies
- Number of predictions varies across algorithms due to their specifications
- GPU acceleration provides significant throughput for large-scale library expansion

## Fragment Ion Space Construction

| Parameter | Value |
|-----------|-------|
| Bond break type | Single edge removal |
| Hydrogen rearrangements | Up to 4 H losses per fragment |
| Fragment space F(G) | All subgraph pairs from edge removal x H-loss variants |
| Precursor stability | Predicted as separate parameter (sigma) |
| Probability model | Softmax over all fragment abundances + precursor |
| Neutral losses | Modeled alongside fragment ions |

## Model Architecture Details

| Component | Description |
|-----------|-------------|
| Input | Molecular structure graph (from SMILES) |
| Node features | Atom properties |
| Edge features | Bond properties |
| Graph convolutions | 3-6 layers (optimal range) |
| Edge prediction | Bond break tendency / fragment abundance |
| Covariates | Ionization mode, CE (continuous), instrument type, MW |
| Auxiliary heads | RT prediction, CCS prediction |
| Charge handling | [M+H]+ and [M-H]- at final stage |

## Key Metrics and Definitions

| Metric | Definition |
|--------|-----------|
| Cosine similarity | Dot product of normalized experimental and predicted spectral vectors |
| Tanimoto similarity | Jaccard index on Morgan fingerprints (2048 bits, radius 3) |
| Peak intensity coverage | Fraction of experimental spectral intensity explained by predicted peaks |
| Break tendency | Statistical measure of bond dissociation likelihood (Allen et al. 2015) |
| Fragment abundance (theta) | Predicted log-scale abundance for each possible fragment ion |
| Precursor stability (sigma) | Predicted stability of intact precursor under given conditions |
| UMAP | Uniform Manifold Approximation and Projection for embedding visualization |
| ClassyFire | Compound classification system for organizing by chemical superclass |

## Knowledge Bases Referenced

| Database | Size Context | Use |
|----------|-------------|-----|
| PubChem | Orders of magnitude larger than spectral DBs | Chemical structures and properties |
| HMDB | Large | Known metabolite structures |
| GNPS | Smaller (spectral) | Public spectral reference library |
| METLIN | Smaller (spectral) | Public spectral reference library |

- Spectral databases are orders of magnitude smaller than chemical structure databases
- This gap motivates in silico spectral prediction to bridge the coverage difference

## Identification Rates in CASMI Challenges

| Challenge | Year | Best In Silico Recall | Context |
|-----------|------|----------------------|---------|
| CASMI | 2016 | Up to 34% | For previously unknown compounds |
| CASMI | 2022 | Below 30% | Most recent challenge |

- These low identification rates highlight the ongoing need for improved spectral prediction tools

## Reference Count

- Total references cited: 49
