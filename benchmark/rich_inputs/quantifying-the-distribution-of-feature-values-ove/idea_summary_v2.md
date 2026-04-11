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
