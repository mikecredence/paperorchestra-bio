Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

# Idea Summary

## Working title
Factorized visual representations in the primate visual system and deep neural networks

## Core question
Is factorization -- encoding different scene parameters (object identity, pose, viewpoint, background, lighting) in orthogonal subspaces of population activity -- a normative principle of biological visual representations, and do deep neural network models that factorize scene parameters better predict primate neural and behavioral data?

## Motivation / gap
- Object classification has been proposed as the principal objective of the ventral visual stream, but beyond a performance threshold, better classification does not yield better neural predictions -- motivating the search for additional normative principles
- Visual cortical neurons encode many types of information simultaneously (identity, pose, viewpoint), but how these different information types are geometrically organized in population activity space is poorly characterized
- Prior work has focused on invariance (discarding non-class information) as the strategy for supporting classification, but high-level cortical neurons clearly retain non-class information -- suggesting an alternative strategy
- The concept of disentanglement in machine learning typically requires independent factors to be encoded by distinct individual neurons, which is overly restrictive for neural populations; a subspace-level measure of factorization is needed
- No systematic study has tested whether factorization of individual scene parameters (lighting, background, viewpoint, pose) in DNN models predicts their similarity to primate neural and behavioral data across multiple independent datasets

## Core contribution (bullet form)
- Introduced formal measures of factorization and invariance for neural population codes, quantifying whether variance driven by different scene parameters occupies orthogonal subspaces
- Showed that factorization of object pose and background from identity increases from macaque V4 to IT and strongly contributes to improved identity decoding performance
- Conducted a large-scale analysis across a diverse library of DNN models, finding that models with higher factorization of scene parameters (especially object pose) are consistently more predictive of neural and behavioral data across 12 datasets from monkeys and humans
- Demonstrated that invariance to scene parameters was not as consistently associated with neural/behavioral prediction as factorization, suggesting that retaining non-class information in factorized subspaces is preferred over discarding it
- Showed that combining factorization with classification performance in a regression model significantly improved prediction of the most brainlike models, addressing the saturating relationship between classification and neural predictivity
- Controlled for confounds including model architecture (ResNet-50 subset analysis), dimensionality, and classification performance

## Method in brief
Factorization was measured using a PCA-based approach. For a given scene parameter (e.g., object pose), the fraction of parameter-induced variance that avoids the subspace spanned by all other parameters was computed. Specifically, the variance driven by one parameter was projected onto the subspace containing the majority of variance for all other parameters -- factorization is the fraction of variance that does NOT fall within this other-parameter subspace. Invariance was computed by comparing overall parameter-induced variance to the variance induced by other parameters. Both measures were applied to neural population responses (single-unit and multi-unit) and DNN layer activations.

For neural data, three macaque datasets (V4 and IT single-units; IT multi-units from chronic arrays; object recognition behavior) and three human datasets (two fMRI studies, one behavioral) were used -- 12 datasets total (Table S1). The DNN model library included supervised models (AlexNet, ResNet), self-supervised contrastive models (MoCo, SimCLR), and other unsupervised models, predominantly using ResNet-50 architecture (Table S2). For each model, factorization and invariance were computed for four scene parameters (lighting, background, camera viewpoint, object pose) using rendered 3D object stimuli with n=10 parameter levels each. Model "brainlikeness" was assessed as predictive power for neural responses (encoding model fits) or behavioral patterns across all 12 datasets. Regression analyses tested whether factorization improved prediction of brainlike models beyond classification performance or dimensionality alone.

## Target venue
eLife


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the factorized visual representations study.

---

## Neural and Behavioral Datasets (Table S1)

| Dataset ID | Species | Data Type | Brain Area | Measure | Images | Recording Sites | Key Features |
|-----------|---------|-----------|------------|---------|--------|----------------|-------------|
| E1 | Macaque | Multi-unit activity | V4, CIT, PIT, AIT | Neural responses | Large set | Multi-electrode arrays | Chronic arrays, many images per site |
| E2 | Macaque | Single-unit spiking | V4, anterior ventral IT | Neural responses | Moderate set | Penetrating electrodes | Gold standard, well-isolated neurons |
| E3 | Macaque | Behavioral | - | Object recognition per-image accuracy | Same as E2 | - | Image-by-image classification |
| F1 | Human | fMRI | V4, HVC | Voxel responses | Color images | Voxels | Standard resolution |
| F2 | Human | fMRI | V4, HVC | Voxel responses | Grayscale images | Voxels | Different image set from F1 |
| I1 | Human | Behavioral | - | Per-image classification | Same as E3 | - | Same study as macaque behavior |
| I2 | Human | Behavioral | - | Image-by-distractor class performance | Varied | - | Additional behavioral metric |

E1 advantage: Order of magnitude more images tested per recording site than E2. E2 advantage: Well-isolated single neurons, targeting anterior ventral IT near base of skull (highest hierarchical level). Datasets complement each other in recording location and methodology.

---

## Computational Model Library (Table S2)

| Model Category | Examples | Architecture | Training Objective |
|---------------|----------|-------------|-------------------|
| Supervised classification | AlexNet, ResNet | Various | ImageNet classification |
| Self-supervised contrastive | MoCo, SimCLR | ResNet-50 | Contrastive learning |
| Other unsupervised | Various | Various | Reconstruction, colorization, etc. |
| Random baseline | Untrained | ResNet-50 | None (random weights) |

Majority of models used ResNet-50 architecture. For each model, factorization and invariance were measured in the final 5 layers.

---

## Scene Parameters for Factorization/Invariance Measurement

| Parameter | Levels | Variation Method |
|-----------|--------|-----------------|
| Lighting | 10 | Rendered 3D scenes with varied illumination |
| Background | 10 | Different background contexts |
| Camera viewpoint | 10 | Different camera angles |
| Object pose | 10 | Different orientations of the object |

Stimuli: 3D rendered objects with independently varied scene parameters, enabling controlled measurement of parameter-specific variance in model and neural responses.

---

## Experiment 1: Factorization and Invariance in Macaque V4 vs. IT

### Key Metrics (PCA-based method)

| Metric | V4 | IT | Direction | Significance |
|--------|----|----|-----------|-------------|
| Factorization (identity from position) | Lower | Higher | Increased V4 -> IT | Significant |
| Invariance (to position) | Lower | Higher | Increased V4 -> IT | Significant |
| Identity decoding performance | Lower | Higher | Improved V4 -> IT | Significant |

Fig. 2A (left): Factorization of object identity and position increased from macaque V4 to IT (dataset E1, multi-unit activity).

Fig. 2A (right): Invariance also increased from V4 to IT. Combined with increased factorization of remaining variance, this led to higher identity decoding in IT.

### Contribution to Identity Decoding

| Component | Contribution to IT Decoding |
|-----------|---------------------------|
| Factorization | Strong positive contribution |
| Invariance | Positive contribution |
| Combined | Better than either alone |

Fig. 2B: Factorization strongly contributed to improving object identity decoding performance in IT relative to V4.

---

## Experiment 2: Factorization vs. Invariance in Shuffled Controls

| Measure | V4 (shuffle-corrected) | IT (shuffle-corrected) | Above Zero? |
|---------|----------------------|----------------------|-------------|
| Normalized factorization | Significantly > 0 | Significantly > 0 | Yes for both |
| Normalized invariance | Present | Present | Yes |

Fig. S1: Shuffling image identities of population vectors accounts for increases driven purely by covariance changes between V4 and IT. Normalized factorization remained significantly above zero for both brain areas.

---

## Experiment 3: DNN Model Factorization vs. Neural Predictivity

### Correlation Between Model Properties and Brainlikeness

| Scene Parameter | Factorization vs. IT Predictivity (r) | Invariance vs. IT Predictivity (r) | Factorization Stronger? |
|----------------|--------------------------------------|-----------------------------------|----------------------|
| Object pose | Positive (strong) | Weak or absent | Yes |
| Camera viewpoint | Positive (moderate) | Weak/inconsistent | Yes |
| Background | Positive (moderate) | Positive (moderate) | Comparable |
| Lighting | Positive (moderate) | Positive (weak) | Yes |

Fig. 4A: Scatter plots for IT single-units (E2 dataset) showing correlation between model neural predictivity and factorization/invariance for each scene parameter. Each dot is a different model (penultimate layer). Factorization in trained models consistently exceeds random network levels.

Fig. 4B: Similar scatter plots showing that invariance to object pose is NOT consistently associated with better neural prediction, unlike factorization.

---

## Experiment 4: Cross-Dataset Consistency of Factorization-Brainlikeness Relationship

### PCA-Based Factorization Correlations (Fig. 5A)

| Dataset Type | Lighting | Background | Viewpoint | Object Pose |
|-------------|----------|------------|-----------|-------------|
| Macaque neurons (V4) | Positive | Positive | Positive | Positive |
| Macaque neurons (IT) | Positive | Positive | Positive | Positive (strong) |
| Human fMRI (V4) | Positive | Positive | Positive | Positive |
| Human fMRI (HVC) | Positive | Positive | Positive | Positive |
| Macaque behavior | Positive | Positive | Positive | Positive |
| Human behavior | Positive | Positive | Positive | Positive |

### Invariance Correlations (Fig. 5B)

| Dataset Type | Lighting | Background | Viewpoint | Object Pose |
|-------------|----------|------------|-----------|-------------|
| Macaque neurons (V4) | Positive | Positive | Weak/absent | Weak/absent |
| Macaque neurons (IT) | Positive | Positive | Weak/absent | Weak/absent |
| Human fMRI (V4) | Variable | Variable | Weak | Weak |
| Human fMRI (HVC) | Variable | Variable | Weak | Weak |
| Macaque behavior | Variable | Variable | Weak | Weak |
| Human behavior | Variable | Variable | Weak | Weak |

Fig. 5: Factorization of scene parameters (PCA-based method) consistently correlates with brainlike DNN models across all 12 datasets. Invariance to camera viewpoint or object pose is NOT consistently indicative of brainlikeness, unlike factorization.

---

## Experiment 5: Architecture-Controlled Analysis (ResNet-50 only)

### Factorization-Brainlikeness Correlation (ResNet-50 subset)

| Scene Parameter | Correlation with Neural Predictivity | Consistent with Full Library? |
|----------------|-------------------------------------|------------------------------|
| Object pose | Positive | Yes |
| Camera viewpoint | Positive | Yes |
| Background | Positive | Yes |
| Lighting | Positive | Yes |

Fig. S3: Same analysis as Fig. 5C restricted to ResNet-50 architecture models. Main finding replicated: factorization of scene parameters correlates with better neural predictions, controlling for architecture.

---

## Experiment 6: Factorization Combined with Classification

### Regression Analysis (Fig. 6)

| Predictor | Average Brain Predictivity (across datasets) |
|-----------|---------------------------------------------|
| Classification performance alone | Moderate (faded black bar) |
| Dimensionality alone | Lower (faded pink bar) |
| Factorization alone (each parameter) | Moderate (faded colored bars) |
| Classification + Factorization (combined) | Highest (unfaded bars) |

Fig. 6: Linearly combining factorization with classification in a regression model produced significant improvements in predicting the most brainlike models. This improvement was not accounted for by classification or dimensionality alone.

---

## Experiment 7: Addressing the Saturating Classification-Neural Predictivity Trend

### Object Pose Factorization Resolves Saturation (Fig. 7)

| Dataset | Classification vs. Neural Predictivity | Classification + Pose Factorization vs. Neural Predictivity |
|---------|---------------------------------------|-----------------------------------------------------------|
| Macaque E1 (IT multi-units) | Saturating/reversing trend | Monotonic positive trend |
| Macaque E2 (IT single-units) | Saturating/reversing trend | Monotonic positive trend |
| Human F1 (fMRI) | Saturating trend | Improved monotonic trend |
| Human F2 (fMRI) | Saturating trend | Improved monotonic trend |

Fig. 7 (top row): Scatter plots showing that neural/voxel predictivity saturates or even reverses for models with increasingly good classification performance.

Fig. 7 (bottom row): Adding object pose factorization eliminates this saturation, producing a consistently positive relationship.

---

## Simulation: Factorized vs. Non-Factorized Coding (Fig. 1C)

### Setup

| Parameter | Value |
|-----------|-------|
| Dimensions | 10 total (3 shown in visualization) |
| Variables | 2 binary variables |
| Noise | i.i.d. Gaussian |
| Alignment parameter | a (0 = orthogonal/factorized, >0 = non-orthogonal/entangled) |
| Geometry | Square (factorized) to parallelogram (entangled) |

### Results

| Alignment (a) | Linear Separability | Few-Shot Classifier Performance | Many-Shot Performance |
|--------------|--------------------|---------------------------------|----------------------|
| 0 (orthogonal) | Yes | Best | Good |
| Low (slight misalignment) | Yes | Good | Good |
| High (strong misalignment) | Yes | Poor | Moderate |

Fig. 1C: Even when linear separability of variables is maintained, decreasing orthogonality (from factorized square to entangled parallelogram geometry) degrades classifier performance in the few training-samples regime with noise. This motivates factorization as important beyond mere linear separability.

---

## Formal Definitions

### Factorization Measure

| Component | Description |
|-----------|-------------|
| a (other_param_subspace) | Subspace containing majority of variance for all other parameters |
| b (param_subspace) | Subspace containing majority of variance for the parameter of interest |
| Factorization | Fraction of parameter-induced variance that avoids the other_param_subspace |
| Range | 0 (fully entangled) to 1 (fully factorized) |

### Invariance Measure

| Component | Description |
|-----------|-------------|
| c (var_other_param) | Variance induced by other parameters |
| Parameter-induced variance | Variance within a class driven by the parameter |
| Invariance | Ratio comparing parameter variance to other-parameter variance |
| Range | Low (highly sensitive) to high (invariant to parameter) |

Fig. 1B: Schematic showing how factorization and invariance are computed from variance in two different linear subspaces.

---

## Key Quantitative Summary

| Finding | Datasets Supporting | Consistency |
|---------|-------------------|-------------|
| Factorization increases V4 -> IT | E1, E2 | Strong |
| Invariance increases V4 -> IT | E1, E2 | Strong |
| Factorization predicts brainlikeness | All 12 datasets | Consistent |
| Invariance predicts brainlikeness | Partial (background, lighting) | Inconsistent for viewpoint/pose |
| Pose factorization most important | IT/HVC datasets | Strong |
| Classification + factorization > classification alone | All 12 datasets | Significant improvement |
| Results hold for ResNet-50 subset | Architecture-controlled | Replicated |

---

## Relationship to Prior Concepts

| Concept | Relationship to Factorization |
|---------|------------------------------|
| Disentanglement (ML) | Related but more restrictive -- requires distinct individual neurons |
| Abstraction (representational geometry) | Related -- abstract representations should be highly factorized |
| Manifold disentanglement | Closely related -- factorization generalizes to high-dimensional parameters |
| Tolerance/invariance | Complementary strategy, not competing |
| Dimensionality | Facilitating factor -- high-D representations may enable factorization |

---

## Statistical Methods

| Method | Application |
|--------|------------|
| PCA-based subspace identification | Computing factorization and invariance metrics |
| Linear encoding models | Predicting neural/voxel responses from model features |
| Pearson correlation | Relating model factorization to brainlikeness |
| Linear regression | Combining classification + factorization to predict brainlikeness |
| Shuffle control | Subtracting covariance-driven increases in factorization |
| Architecture-matched analysis | Restricting to ResNet-50 models to control confounds |

---

## Figure Summary

| Figure | Key Finding |
|--------|------------|
| Fig. 1 | Framework: factorization vs. invariance as strategies for disentangling object identity; simulation shows factorization benefits few-shot classification |
| Fig. 2 | Macaque V4 to IT: factorization increases and contributes to identity decoding |
| Fig. 3 | Schematic of meta-analysis pipeline: measure model factorization/invariance, then correlate with brainlikeness |
| Fig. 4 | Example dataset: DNN factorization (especially pose) correlates with IT neural predictivity; invariance does not consistently |
| Fig. 5 | Cross-dataset: factorization consistently correlates with brainlikeness across 12 datasets; invariance is inconsistent |
| Fig. 6 | Combined regression: factorization + classification predicts brainlikeness better than either alone |
| Fig. 7 | Factorization resolves the saturating classification-neural predictivity trend for IT/HVC data |
| Fig. S1 | Shuffle-controlled factorization remains significant in V4 and IT |
| Fig. S2 | Full scatter plots for all datasets |
| Fig. S3 | ResNet-50 architecture-controlled analysis replicates main findings |

---

## Reference Count
48 references cited in the paper.

