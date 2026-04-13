Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: PLOS Computational Biology

## Idea Summary

# Idea Summary

## Working title
Quantifying the Distribution of Feature Values over Data Represented in Arbitrary Dimensional Spaces

## Core question
Can a graph-based topological metric quantify how structured a given feature is distributed over a data cloud in arbitrary D-dimensional spaces, without relying on clustering or linear correlation assumptions?

## Motivation / gap
- Identifying whether a feature has structured distribution over a point cloud is a general problem across neuroscience, data science, and image analysis
- Most existing structure quantification methods depend on cluster analysis, which is suboptimal for continuous features and non-discrete data clouds
- Linear correlation metrics fail for complex, convoluted distributions
- Decoder-based approaches are highly model-dependent and do not directly quantify structure
- No existing method works robustly across arbitrary dimensions, handles both scalar and vectorial features, and distinguishes local from global structure

## Core contribution (bullet form)
- Introduced the Structure Index (SI), a graph-based metric ranging from 0 (random) to 1 (maximal structure) that quantifies feature distribution over point clouds in any dimensional space
- Demonstrated robustness: SI remains consistent when toy models are embedded into increasing dimensionality (tested from 2D up to high D), with varying point cloud sizes (tested with 9,000-40,000 points), and across signal-to-noise ratios
- Extended SI to vectorial features, enabling quantification of how multiple related variables interact and jointly structure data
- Applied SI to head-direction cell neural manifold data, retrieving consistent feature structure from both high-dimensional (original neuron space) and low-dimensional (3D manifold) representations during awake, REM, and nREM states
- Provided general-purpose applications to sound categorization (spectro-temporal features in 128D time-stamp space) and image segmentation, demonstrating broad applicability
- Showed SI can detect local vs global structure by varying the number of nearest neighbors (k parameter)

## Method in brief
The SI divides feature values into n equal bins, assigning each data point to a bin-group. For each pair of bin-groups u and v, the overlapping score OS(u -> v) is computed as the ratio of k-nearest neighbors of all points in u that belong to v. This produces an adjacency matrix M (n x n) representing a weighted directed graph. The SI is then defined as 1 minus the mean weighted degree of the nodes after scaling: SI = 1 - (mean_degree / scaling_factor), where the scaling ensures SI = 0 for a uniform random distribution and SI = 1 for maximal separation. The distance metric for nearest neighbors can be Euclidean, geodesic, cosine, or any other appropriate measure.

For vectorial features, bin-groups are defined by combinations of binned values across multiple feature dimensions. The SI framework naturally extends by treating the vectorial feature as defining composite bin-groups. The key parameter is k (number of nearest neighbors), which can be tuned to detect local structure (small k) versus global structure (large k). Three toy models -- a 2D linear gradient (40,000 points), a 3D solid ball (40,000 points), and a 3D lamp (32,000 points) -- were used to validate robustness across dimensionality embedding, cloud density, bin number, and noise levels.

## Target venue
PLOS Computational Biology


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the Structure Index (SI) metric study.

---

## Toy Model Datasets

| Model | Dimensionality | Points | Feature Description |
|-------|---------------|--------|-------------------|
| 2D linear gradient | 2D | 40,000 | Feature distributed along gradient |
| 3D solid ball | 3D | 40,000 | Feature distributed along radius |
| 3D lamp | 3D | 32,000 | Feature varies along three axes |
| 2D local vs global pattern | 2D | 9,000 | Local or global feature distribution |
| 3D sphere (vectorial) | 3D | 40,000 | Angles theta and phi |
| D-dimensional sphere | D-dim (varied) | 8D x 40,000 per D | D-1 angles as features |

---

## Experiment 1: SI Robustness to Embedded Dimensionality

Objects embedded into increasing dimensions by adding noise and rotating.

| Toy Model | Intrinsic Dimension | Embedded Dimensions Tested | SI Behavior |
|-----------|--------------------|--------------------------|----|
| 2D gradient | 2 | 2, 5, 10, 20, 50, 100+ | Consistent (stable plateau) |
| 3D ball | 3 | 3, 5, 10, 20, 50, 100+ | Consistent (stable plateau) |
| 3D lamp | 3 | 3, 5, 10, 20, 50, 100+ | Consistent (stable plateau) |

Fig. 3C: SI showed consistent response across increasing embedded dimensionality for all three models.

---

## Experiment 2: Effect of Point Cloud Size

| Number of Points (2D space) | SI Stability |
|----------------------------|-------------|
| ~500 | Some variability |
| ~1,000 | Reasonably stable |
| ~5,000 | Stable |
| ~10,000 | Stable |
| ~40,000 | Stable |

Fig. 3D: SI performs smoothly for a wide range of point counts when examined in 2 dimensions.

---

## Experiment 3: Effect of Number of Bin-Groups

| Number of Bins | SI Response (Gradient) | SI Response (Ball) | SI Response (Lamp) |
|---------------|----------------------|-------------------|----|
| 5 | Stable | Stable | Stable |
| 10 | Stable | Stable | Stable |
| 20 | Stable | Stable | Stable |
| 50 | Stable | Stable | Stable |
| 100 | Slight variation | Slight variation | Slight variation |

Fig. 3E: SI performs consistently for a range of bin-groups, though topological characteristics of the data cloud can influence results at extremes.

---

## Experiment 4: Signal-to-Noise Ratio Sensitivity

Gaussian noise added across all dimensions.

| SNR Level | SI Trend |
|-----------|---------|
| High SNR (low noise) | SI near maximum for structured data |
| Moderate SNR | SI decreasing but captures trends |
| Low SNR (high noise) | SI reduced but still discriminates structure from randomness |

Fig. 3F: SI captures structural trends even under high noise levels, demonstrating suitability for experimental data.

---

## Experiment 5: Local vs Global Structure Detection

| k (neighbors) | Local Pattern SI | Global Pattern SI | Shuffled Control |
|---------------|-----------------|-------------------|-----------------|
| Small k | Higher (detects local structure) | Lower | Near 0 |
| Medium k | Moderate | Moderate | Near 0 |
| Large k | Lower | Higher (detects global structure) | Near 0 |

Fig. 2A: Local pattern simulated with 9,000 points in 2D -- feature values organized locally.
Fig. 2B: Global pattern -- same 2D cloud with global feature distribution.
Fig. 2C: SI as function of number of neighbors distinguishes local from global organization. Data tested against shuffled distribution (99th percentile threshold).

---

## Experiment 6: Vectorial Feature -- 3D Sphere

| Feature | SI Value | Interpretation |
|---------|----------|---------------|
| Theta only | Intermediate | Single angle structure |
| Phi only | Intermediate | Single angle structure |
| Vectorial (theta, phi) | Higher | Combined structure captured |

Fig. 4A: 3D sphere defined by trigonometric equations with angles theta and phi.
Fig. 4B: SI for each individual angle and for the vectorial feature combination.

---

## Experiment 7: D-dimensional Sphere Extension

| Dimensionality D | Points per D | Feature Type | SI Pattern |
|-----------------|-------------|-------------|-----------|
| 3 | 40,000 | D-1 angles (2) | Baseline |
| 5 | 40,000 | D-1 angles (4) | Maintained |
| 8 | 40,000 | D-1 angles (7) | Maintained |
| 10 | 40,000 | D-1 angles (9) | Maintained |

Fig. 4C: D-dimensional sphere with N = 40,000 points per D. SI captures vectorial structure across increasing dimensionality.

---

## Experiment 8: Neural Manifold -- Head-Direction System

| Data Source | Original Space | Reduced Space | Feature |
|-------------|---------------|---------------|---------|
| Head direction cells | N-dimensional (N neurons) | 3D manifold | Head direction angle |

| Brain State | SI (Original Space) | SI (3D Manifold) | Consistency |
|-------------|--------------------|-----------------|----|
| Awake | High structure | High structure | Concordant |
| REM sleep | Moderate structure | Moderate structure | Concordant (preserved) |
| nREM sleep | Low/no structure | Low/no structure | Concordant |

Fig. 5A: Neural manifold framework -- firing rates in N-dimensional space projected to subspace.
Fig. 5B: 3D manifold from head direction system with angle projected over data cloud.
Fig. 5C: SI values in original (og) and reduced (3D) spaces for awake, REM, and nREM states. Head-direction representation preserved during REM, consistent with mental replay hypothesis.

---

## Experiment 9: Sound Categorization Application

| Feature Space | Dimensionality | Feature Assessed | SI Result |
|--------------|---------------|-----------------|----------|
| Spectro-temporal | 128 time stamps | Sound category labels | Structure detected |

Fig. 5 (bottom panels): SI applied to auditory coding of spectro-temporal features in a 128-dimensional space built from individual time stamps.

---

## Experiment 10: Image Segmentation Application

| Application | Feature Type | Space | SI Result |
|-------------|-------------|-------|----------|
| Histological image segmentation | Pixel categories | Multidimensional pixel space | Structure quantified |

SI applied to image data, demonstrating potential for image segmentation tasks in histology and related fields.

---

## Key SI Properties Summary

| Property | Description | Validated? |
|----------|-------------|-----------|
| Range | 0 (random) to 1 (maximal structure) | Yes |
| Dimension-agnostic | Works in arbitrary D | Yes (up to 100+ D) |
| Scalar features | Continuous or discrete | Yes |
| Vectorial features | Multi-variable | Yes |
| Local vs global tuning | Via k parameter | Yes |
| Distance metric flexibility | Euclidean, geodesic, cosine | Yes |
| Robustness to noise | Degrades gracefully | Yes |
| Robustness to cloud size | Stable above ~1000 points | Yes |
| Robustness to bin number | Stable across reasonable range | Yes |

---

## Mathematical Definition Summary

| Component | Formula/Description |
|-----------|-------------------|
| Overlapping Score OS(u->v) | Ratio of k-nearest neighbors of points in u that belong to v |
| Adjacency Matrix M | n x n matrix where entry (a,b) = OS(ua -> vb) |
| Structure Index SI | 1 - (mean weighted degree / scaling factor) |
| SI = 0 | Uniform random distribution (full overlapping) |
| SI = 1 | Maximal separation (zero overlapping between bins) |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Conceptual illustration: feature gradient vs random distribution; overlapping matrix and graph |
| Fig. 2 | Local vs global structure detection via k-neighbor parameter |
| Fig. 3 | Robustness across dimensionality, cloud size, bin number, and noise |
| Fig. 4 | Vectorial feature extension; D-dimensional sphere results |
| Fig. 5 | Neural manifold application; sound and image categorization demonstrations |

---

## Reference Count
21 references cited.

