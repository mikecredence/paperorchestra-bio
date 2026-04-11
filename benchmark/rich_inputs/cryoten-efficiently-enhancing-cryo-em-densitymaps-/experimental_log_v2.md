# Experimental Log: CryoTEN Cryo-EM Map Enhancement

## Overview

Development and evaluation of CryoTEN, a 3D U-Net transformer with EPA attention for enhancing cryo-EM density maps. Trained on 1,295 maps, validated on 76, tested on 150 independent maps. Compared against DeepEMhancer and EMReady.

---

## Data Collection and Preprocessing

### Table 1: Dataset Composition

| Split | Number of Maps | Purpose |
|-------|---------------|---------|
| Training | 1,295 | Model training |
| Validation | 76 | Hyperparameter tuning |
| Test | 150 | Independent blind evaluation |
| Total | 1,521 | All non-redundant map-structure pairs |

### Table 2: Data Filtering Criteria

| Filter | Threshold |
|--------|-----------|
| Resolution range | 2-7 Angstroms |
| CC mask minimum | > 0.7 |
| CC box minimum | > 0.6 |
| Sequence identity clustering | 30% (MMseqs2) |
| Map axes | Orthogonal only |
| Maps per PDB structure | 1 (if multiple available) |
| PDB structures per map | 1 (if multiple available) |

### Table 3: Data Processing Parameters

| Parameter | Value |
|-----------|-------|
| Resampled grid size | 1 Angstrom |
| Normalization | 0-1 range (99.999th percentile) |
| Training block size (initial) | 64 x 64 x 64 |
| Training stride | 50 |
| Training block size (on-the-fly crop) | 48 x 48 x 48 |
| Inference block size | 48 x 48 x 48 |
| Simulated map function | Reference Gaussian |
| FSC resolution for Gaussian | FSC@0.143 (unmasked) |

### Table 4: Simulated Map Generation

| Parameter | Formula Component |
|-----------|------------------|
| Density at grid point y | rho_c(y) = sum over atoms of A_i * C * exp(-k * ||y - x_i||^2) |
| A_i | Atomic number of ith atom |
| k | pi / (0.9 * R0)^2 |
| R0 | Unmasked FSC@0.143 resolution |
| C | (k/pi)^(3/2) |
| Tool used | phenix.mtriage for FSC computation |

---

## Evaluation on Primary Maps (150 Test Maps)

### Table 5: Average Map-Model Validation Metrics (Primary Maps)

| Metric | Deposited Primary Maps | CryoTEN Processed Maps | Improvement |
|--------|----------------------|----------------------|-------------|
| FSC@0.143 (Angstroms) | 3.55 | 2.45 | 30.99% better resolution |
| FSC@0.5 (Angstroms) | 6.38 | 3.73 | 41.54% better resolution |
| CC box | Lower | Higher | Substantial improvement |
| CC mask | Lower | Higher | Substantial improvement |
| CC peaks | Lower | Higher | Substantial improvement |
| Q-score | Lower | Higher | Improved atom resolvability |

### Table 6: Percentage of Maps Improved

| Metric | % Maps Improved |
|--------|----------------|
| FSC@0.143 | 100% (150/150) |
| FSC@0.5 | 96% (144/150) |

Fig 2a: Half-violin and box plots showing FSC@0.143 resolution distribution -- CryoTEN-processed maps consistently show better (lower) resolution values than deposited primary maps.
Fig 2b: FSC@0.5 resolution distributions showing similar improvement pattern (7 outliers with FSC@0.5 > 20 Angstroms in deposited maps hidden for visualization).
Fig 2c: Q-score distributions showing improved atom resolvability after CryoTEN processing.
Fig 2d-f: CC box, CC mask, and CC peaks distributions all show substantial improvements.

---

## Evaluation on Half Maps (70 Test Maps)

### Table 7: Average Map-Model Validation Metrics (Half Maps)

| Metric | Deposited Half Maps | CryoTEN Processed Half Maps | Direction |
|--------|--------------------|-----------------------------|-----------|
| FSC@0.143 | Baseline | Improved | Better resolution |
| FSC@0.5 | Baseline | Improved | Better resolution |
| CC box | Baseline | Improved | Higher correlation |
| CC mask | Baseline | Improved | Higher correlation |
| CC peaks | Baseline | Improved | Higher correlation |
| Q-score | Baseline | Improved | Better resolvability |

Note: Detailed values are in Table 2 of the paper. CryoTEN generalizes well to half maps, not just primary maps.

---

## De Novo Structure Modeling Evaluation

### Table 8: Structure Modeling Quality (700 Chains from 124 Maps)

| Metric | From Deposited Maps | From CryoTEN Maps | Improvement |
|--------|--------------------|--------------------|-------------|
| Residue coverage | Baseline | Higher | Better structural completeness |
| Sequence match score | Baseline | Higher | Better sequence agreement |

Protein structures built from CryoTEN-processed density maps have substantially better quality than those built from original deposited maps, as measured by automatic de novo modeling.

### Table 9: Structure Modeling by Resolution Category

| Resolution Category | Number of Maps | Deposited Residue Coverage | CryoTEN Residue Coverage | Deposited Seq Match | CryoTEN Seq Match |
|--------------------|---------------|---------------------------|-------------------------|--------------------|--------------------|
| Low resolution | 10 | Baseline | Improved | Baseline | Improved |
| Medium resolution | 93 | Baseline | Improved | Baseline | Improved |
| High resolution | 21 | Baseline | Improved | Baseline | Improved |

Table 4 in the paper provides the full breakdown. CryoTEN robustly improves structure modeling across all resolution categories, with 124 maps grouped into low (10), medium (93), and high (21) resolution bins.

---

## Comparison with State-of-the-Art Methods

### Table 10: Map Quality Comparison (131 Primary Maps)

| Metric | Deposited Maps | DeepEMhancer | EMReady | CryoTEN |
|--------|---------------|-------------|---------|---------|
| FSC@0.143 (Angstroms) | Baseline | Best | Second | Close to best |
| FSC@0.5 (Angstroms) | Baseline | Competitive | Competitive | Competitive |
| CC box | Baseline | Competitive | Competitive | Competitive |
| CC mask | Baseline | Competitive | Competitive | Competitive |
| CC peaks | Baseline | Competitive | Competitive | Competitive |
| Q-score | Baseline | Competitive | Competitive | Competitive |

Note: 131 maps used for three-way comparison (subset of the 150 test maps where all methods could be applied). CryoTEN ranks second in map quality improvement overall.

### Table 11: Computational Efficiency Comparison (20-Map Benchmark)

| Method | Avg Processing Time | GPU Memory | Batch Size |
|--------|--------------------|------------|------------|
| DeepEMhancer | Slower (baseline) | Higher | 40 |
| EMReady | Slowest | Highest | 40 |
| CryoTEN | >10x faster than others | Much less | 40 |

All three methods benchmarked on the same subset of 20 maps with batch size 40, on the same hardware. CryoTEN achieves >10x speedup and substantially lower GPU memory consumption compared to both DeepEMhancer and EMReady.

### Table 12: Quality vs Efficiency Trade-off Summary

| Method | Map Quality Rank | Speed Rank | Memory Rank |
|--------|-----------------|------------|-------------|
| DeepEMhancer | 1st (best quality) | 2nd | 2nd |
| EMReady | Competitive | 3rd (slowest) | 3rd (most memory) |
| CryoTEN | 2nd | 1st (>10x faster) | 1st (least memory) |

---

## Model Architecture

### Table 13: CryoTEN Architecture Details

| Component | Description |
|-----------|-------------|
| Overall architecture | 3D U-Net style transformer |
| Attention mechanism | EPA (Efficient Pair-wise Attention) |
| Encoder structure | Multiple downsampling stages with attention |
| Decoder structure | Corresponding upsampling stages with skip connections |
| Residual blocks | ConvRes blocks within encoder and decoder |
| Input | 48 x 48 x 48 density blocks |
| Output | Enhanced 48 x 48 x 48 density blocks |

Fig 1b shows the full CryoTEN model architecture with training/evaluation pipeline.
Fig 1c details the encoder, decoder, and ConvRes block structures.

---

## Visual Quality Examples

### Table 14: Example Map Enhancement (EMD-22338 / PDB 7JHJ)

| Contour Level | Deposited Map | CryoTEN Enhanced Map |
|--------------|---------------|---------------------|
| Lower contour | Noisy, poor definition | Cleaner, better definition |
| Recommended contour | Moderate quality | Substantially improved |
| Higher contour | Missing density regions | More complete density |

Fig 3a: Deposited density map (blue) at three contour levels superimposed with known protein structure (PDB 7JHJ).
Fig 3b: CryoTEN enhanced map (green) at three contour levels showing improved agreement with protein structure. Density volume matched for direct comparison.

---

## Tools and Resources Used

### Table 15: Software and Databases

| Tool / Resource | Purpose |
|----------------|---------|
| RCSB PDB | Source of protein structures |
| EMDB | Source of deposited cryo-EM maps |
| phenix.mtriage | FSC resolution computation |
| phenix.map_model_cc | CC score computation (CC box, CC mask, CC peaks) |
| phenix.auto_sharpen | Global sharpening baseline |
| UCSF Chimera (mapq plugin) | Q-score computation |
| MMseqs2 | Sequence clustering for redundancy removal |
| DeepEMhancer | Competing DL method for comparison |
| EMReady | Competing DL method for comparison |

### Table 16: Evaluation Metrics Definitions

| Metric | Description |
|--------|-------------|
| FSC@0.143 | Unmasked Fourier Shell Correlation at 0.143 threshold (map-model resolution) |
| FSC@0.5 | Unmasked Fourier Shell Correlation at 0.5 threshold |
| CC box | Cross-correlation between entire experimental and model-calculated maps |
| CC mask | Cross-correlation within the molecular mask region only |
| CC peaks | Cross-correlation around highest-density regions |
| Q-score | Atom resolvability measure |
| Residue coverage | Fraction of residues successfully modeled in de novo structure |
| Sequence match score | Agreement between modeled and known protein sequence |

---

## Key Observations

- CryoTEN improves 100% of test maps at FSC@0.143 threshold, demonstrating robust enhancement
- The >10x speed advantage and lower memory footprint make CryoTEN practical for large-scale processing pipelines
- Enhancement generalizes from primary maps to half maps
- Structure modeling improvements hold across low, medium, and high resolution maps
- The EPA attention mechanism enables the transformer to capture long-range dependencies in 3D density without prohibitive computational cost
- Training on simulated maps from known structures provides clean targets that guide the model to denoise and sharpen experimental maps
