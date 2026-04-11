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
