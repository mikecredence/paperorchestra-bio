# Experimental Log: Competitive Interactions in Mammalian Brain Dynamics

## Datasets

| Dataset | Species | N Subjects | Parcellation | SC Source | FC Source |
|---------|---------|------------|-------------|-----------|-----------|
| Human Connectome Project (HCP) | Human | 100 | Schaefer-100 (100 cortical ROIs) | Subject-specific diffusion tractography | fMRI (1200 volumes, TR=720ms, 2mm isotropic) |
| Macaque | Macaca mulatta | 19 | Species-specific atlas | Diffusion tractography + CoCoMac tract-tracing | fMRI |
| Mouse | Mus musculus | 10 | Species-specific atlas | Allen Institute tract-tracing | fMRI |

### Human fMRI Acquisition Parameters

| Parameter | Value |
|-----------|-------|
| Source | HCP Release Q3, 900 data release |
| T1-weighted | FOV 224x224 mm, 0.7 mm isotropic, TR 2400 ms, TE 2.14 ms, flip angle 8 degrees |
| fMRI (EPI) | 2 mm isotropic, TR 720 ms, TE 33.1 ms, flip angle 52 degrees, 72 slices |
| Volumes | 1200 (first 10 removed for steady state) |
| Preprocessing | HCP minimal preprocessing + CONN toolbox denoising |
| Denoising method | Anatomical CompCor (5 WM PCs, 5 CSF PCs, 6 motion params + derivatives, ART artifact regressors) |
| Filtering | Band-pass 0.008-0.09 Hz |
| Replication parcellation | Schaefer-232 (200 cortical + 32 subcortical ROIs) |

## Model Specification

### Stuart-Landau Oscillator (Hopf Model)

| Parameter | Description |
|-----------|-------------|
| Local dynamics | Nonlinear Stuart-Landau oscillator |
| Dynamical regime | Poised near (just below) critical Hopf bifurcation |
| Working point | Edge-of-bifurcation (found to produce most faithful FC and dynamics) |
| State variable per region | Complex amplitude (real and imaginary parts) |
| Intrinsic frequency | Region-specific |
| Bifurcation parameter | Controls distance from critical point |

### Model Fitting Procedure

| Step | Description |
|------|-------------|
| Initialization | SC-weighted coupling between oscillators |
| Optimization target | Minimize difference between empirical and simulated FC (zero-lag and lagged) |
| Weight update | Iterative, individual connection weights updated per subject |
| Cooperative-only model | All weights constrained positive |
| Cooperative+competitive model | Weight signs allowed to vary (negative permitted, not imposed) |
| Fitting level | Single-subject |

## Experiment 1: Model Fit to Functional Connectivity (Fig 2)

### Group-Level FC Correlation

| Species | Cooperative-Only Model (r) | Cooperative+Competitive Model (r) | Improvement |
|---------|---------------------------|-----------------------------------|-------------|
| Human | High | Up to 0.95 | Substantial |
| Macaque | High | Up to 0.95 | Substantial |
| Mouse | High | Up to 0.95 | Substantial |

- Fig 2A: Species-specific matrices showing group-average empirical (left half) and simulated (right half) FC for cooperative-only model
- Fig 2B: Same format for cooperative+competitive model, visually closer match to empirical FC
- Correlation coefficient between empirical and simulated FC reported for each species and model variant
- Competitive model consistently outperforms cooperative-only across all three species

## Experiment 2: Subject Specificity and Identifiability (Fig 3)

### Differential Identifiability

| Species | Cooperative-Only Identifiability | Cooperative+Competitive Identifiability |
|---------|----------------------------------|-----------------------------------------|
| Human | Moderate | Higher |
| Macaque | Moderate | Higher |
| Mouse | Moderate | Higher |

- Fig 3A: Matrix of FC similarity between each empirical subject (columns) and each simulated subject (rows)
- Brighter diagonal indicates greater subject-specific accuracy
- Fig 3B: Differential identifiability defined as difference between self-self similarity (diagonal) and self-other similarity (off-diagonal)
- Models with competitive interactions produced consistently greater differential identifiability across species

## Experiment 3: Emergent Dynamical Properties (Fig 4)

### Metastability

| Species | Empirical Metastability | Cooperative-Only Model | Cooperative+Competitive Model |
|---------|------------------------|------------------------|-------------------------------|
| Human | Reference level | Higher than empirical (excessive synchrony) | Closer to empirical |
| Macaque | Reference level | Higher than empirical | Closer to empirical |
| Mouse | Reference level | Higher than empirical | Closer to empirical |

- Metastability operationalized as temporal standard deviation of the Kuramoto order parameter (KOP)
- Fig 4A: Cooperative-only models consistently show higher metastability than real brains
- Adding competitive interactions brings metastability closer to empirically observed levels
- Maximum observed synchrony is significantly higher for cooperative-only model (often approaching total synchronization, confirmed in Fig S12)
- Competitive interactions play a stabilizing role, preventing runaway global activity

### Local-Global Hierarchy (Intrinsic-Driven Ignition)

| Species | Cooperative-Only IDI | Cooperative+Competitive IDI |
|---------|---------------------|-----------------------------|
| Human | Lower | Higher (greater hierarchy) |
| Macaque | Lower | Higher |
| Mouse | Lower | Higher |

- Fig 4B: Intrinsic-driven ignition (IDI) measures co-occurrence of high-activity "driver events" across regions
- Competitive interactions increased divergence between local and global activity patterns
- This produces greater hierarchical organization

### Synergistic Information

| Species | Cooperative-Only Synergy | Cooperative+Competitive Synergy |
|---------|-------------------------|---------------------------------|
| Human | Lower | Higher |
| Macaque | Lower | Higher |
| Mouse | Lower | Higher |

- Synergy quantified using partial information decomposition (PID)
- Competitive interactions produce greater levels of synergistic (beyond-pairwise) information
- This was an emergent property, not explicitly optimized during model fitting

## Experiment 4: Architecture of Competitive Interactions

### Spatial Organization

| Property | Cooperative Interactions | Competitive Interactions |
|----------|------------------------|--------------------------|
| Spatial pattern | Modular (within-network) | Diffuse (between-network) |
| Connection distance | Short-range dominant | Long-range dominant |
| Network structure | Clustered within functional modules | Spanning across functional modules |
| Consistency | Consistent across species | Consistent across species |

- Cooperative interactions are organized in modular fashion, connecting regions within the same functional network
- Competitive interactions are diffuse and long-range, connecting regions across different functional networks
- This pattern is remarkably consistent across human, macaque, and mouse

## Experiment 5: Cognitive Matching (Fig 5) - Human Only

### NeuroSynth Meta-Analytic Matching

| Model | Mean Cognitive Matching Score | Interpretation |
|-------|------------------------------|----------------|
| Cooperative-only | Lower | Simulated brain states less similar to canonical cognitive maps |
| Cooperative+competitive | Higher | Simulated brain states more closely match cognitive meta-analytic maps |
| Empirical | Reference | Actual brain activity matching to 123 NeuroSynth maps |

- Fig 5A: At each time point, cognitive matching score computed as best spatial correlation between brain activity and 123 NeuroSynth meta-analytic brain maps
- Overall index obtained by averaging across entire scan duration
- Higher NeuroSynth matching indicates simulated brain activity more closely resembles canonical cognitive patterns
- Competitive interactions increase the match between simulated activity and canonical cognitive operations

## Experiment 6: Neuromorphic Computing / Reservoir Computing (Fig 6)

### Memory Task Performance

| Reservoir Connectivity | Task | Performance |
|-----------------------|------|-------------|
| Cooperative-only effective connectivity | Memory (delayed recall) | Lower accuracy |
| Cooperative+competitive effective connectivity | Memory (delayed recall) | Higher accuracy |
| Random connectivity (control) | Memory (delayed recall) | Baseline |

- Fig 6A: Reservoir computing architecture with input layer, reservoir (recurrent neural network), and linear readout
- Reservoirs endowed with effective brain connectivity patterns
- Readout module trained to reproduce delayed versions of input signal
- Competitive generative interactions produced superior computational performance on memory tasks
- This demonstrates a functional/computational advantage of competitive interactions

### Reservoir Computing Architecture

| Component | Description |
|-----------|-------------|
| Input layer | Feeds signal into reservoir |
| Reservoir | Nonlinear recurrent neural network with brain-derived connectivity |
| Readout | Linear module trained on reservoir states |
| Task | Reproduce delayed version of input (memory capacity test) |
| Evaluation | Accuracy of delayed signal reproduction |

## Replication and Robustness

### Alternative Parcellation (Schaefer-232)

| Analysis | Schaefer-100 | Schaefer-232 (200 cortical + 32 subcortical) |
|----------|-------------|-----------------------------------------------|
| Main FC fit result | Competitive model superior | Replicated |
| Emergent dynamics | Competitive model superior | Replicated |

- Main results replicated using the finer 232-ROI parcellation
- Robustness confirmed across parcellation granularity

### Structural Connectivity Sources

| Species | SC Method | Symmetrized |
|---------|-----------|-------------|
| Human | In-vivo diffusion tractography (subject-specific) | No (bilateral) |
| Macaque | Diffusion tractography + CoCoMac tract-tracing | Yes (for cross-species comparison) |
| Mouse | Allen Institute tract-tracing (full) | Yes (for cross-species comparison) |

## Summary of Cross-Species Consistency

| Property | Human | Macaque | Mouse |
|----------|-------|---------|-------|
| Competitive model better FC fit | Yes | Yes | Yes |
| Closer metastability | Yes | Yes | Yes |
| Greater synergy | Yes | Yes | Yes |
| Greater hierarchy (IDI) | Yes | Yes | Yes |
| Greater identifiability | Yes | Yes | Yes |
| Modular cooperative / diffuse competitive | Yes | Yes | Yes |

## Interpretation of Maximum Synchrony (Fig S12)

| Model | Maximum Observed Synchrony | Interpretation |
|-------|---------------------------|----------------|
| Cooperative-only | High (often approaching total synchronization) | Reciprocal excitation creates runaway activity |
| Cooperative+competitive | Lower, more realistic | Competitive interactions prevent excessive synchrony |
| Empirical | Moderate | Natural balance of integration and segregation |

## Key Metrics and Definitions

| Metric | Definition |
|--------|-----------|
| FC correlation | Pearson correlation between upper-triangular elements of empirical and simulated FC matrices |
| Metastability | Temporal standard deviation of Kuramoto order parameter |
| Kuramoto order parameter (KOP) | Measure of instantaneous global synchrony |
| Synergy | Synergistic component from partial information decomposition |
| IDI (Intrinsic-Driven Ignition) | Number of co-occurring high-activity events across regions |
| Differential identifiability | Diagonal minus off-diagonal in subject-by-subject FC similarity matrix |
| Cognitive matching | Best spatial correlation with 123 NeuroSynth maps at each time point |
| Reservoir memory capacity | Accuracy of delayed input reproduction in reservoir computing framework |

## Baselines and Controls

| Comparison | Condition 1 | Condition 2 |
|------------|-------------|-------------|
| Model type | Cooperative-only (positive weights only) | Cooperative+competitive (signed weights) |
| Fitting target | Empirical FC (zero-lag + lagged) | Same |
| Emergent properties | Not optimized, measured post-hoc | Same |
| Cross-species | Human, macaque, mouse | Consistent patterns |
| Parcellation robustness | Schaefer-100 | Schaefer-232 |

## Reference Count

- Total references cited: 175
