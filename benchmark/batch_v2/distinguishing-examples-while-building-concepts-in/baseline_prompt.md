Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Nature Communications

## Idea Summary

# Idea Summary

## Working title
Distinguishing examples while building concepts in hippocampal and artificial networks

## Core question
How can CA3, which receives both sparse/decorrelated mossy fiber (MF) inputs from the dentate gyrus and dense/correlated perforant path (PP) inputs from the entorhinal cortex, use these complementary encodings to simultaneously maintain distinct episodic memories and build generalizable concept representations?

## Motivation / gap
- CA3 receives two different encodings of the same sensory information (via MF and PP), but the computational purpose for this dual-pathway architecture has not been firmly established
- DG is known to sparsify and decorrelate EC patterns, but how this interacts with the denser PP pathway within the CA3 autoassociative network is poorly understood
- The hippocampus is implicated in both episodic memory (specific experiences) and concept/category learning, yet the circuit-level mechanism enabling both functions is unclear
- Theta oscillations modulate hippocampal activity and have been linked to phase-specific coding properties, but how they relate to switching between example-specific and concept-level representations has not been tested
- Artificial neural networks performing multitask learning lack principled approaches for balancing example discrimination and concept classification

## Core contribution (bullet form)
- Developed a Hopfield-like model of CA3 that stores both sparse/decorrelated MF and dense/correlated PP encodings and retrieves them at high and low inhibitory tone, respectively
- Showed that as memory load increases, dense PP encodings merge along shared features (forming concepts) while sparse MF encodings remain distinct (preserving examples)
- Demonstrated that the model can alternate between example and concept representations via an oscillating threshold mimicking theta rhythm
- Analyzed theta-modulated place cell tuning in rat CA3 and found that sparser theta phases encode finer spatial positions and more detailed task features (e.g., turn direction in a W-maze)
- Generalized the framework to feedforward neural networks, introducing a novel loss term promoting hybrid correlated/decorrelated encoding that improves multitask learning performance on combined digit classification and set identification tasks

## Method in brief
The model begins by encoding FashionMNIST images (sneakers, trousers, coats; 256 examples per concept) through a binary autoencoder into sparse EC representations (NEC = 1024 neurons, 10% density). From EC, two pathways generate CA3 inputs: the PP pathway uses random binary connectivity yielding dense, correlated patterns (aPP = 0.2, correlation ~0.09), while the MF pathway routes through DG (NDG = 8192, aDG = 0.005) to produce very sparse, decorrelated patterns (aMF = 0.02, correlation ~0.01). CA3 (NCA3 = 2048) stores linear combinations of these encodings in a Hopfield-like network, with MF inputs weighted more heavily. A winners-take-all approach converts postsynaptic inputs to binary activity at a specified density.

Retrieval operates by initializing the network to a corrupted stored pattern and running asynchronous updates under either high inhibitory threshold (retrieving sparse MF-like examples) or low threshold (retrieving dense PP-like concepts). An oscillating threshold simulates the theta cycle, causing the network to alternate between example and concept regimes. Pattern completion success is measured by overlap with stored patterns.

For the neural data analysis, publicly available CA3 place cell recordings from rats on linear tracks and W-mazes were partitioned into theta phase bins. Spatial information per spike was computed at each phase, and population sparsity was measured to test the prediction that sparser phases carry more precise spatial tuning. For the machine learning extension, a multilayer perceptron was trained on an augmented MNIST task requiring both digit classification and set identification, with a novel correlation-based loss term encouraging the hidden layer to maintain both correlated and decorrelated representations.

## Target venue
Nature Communications


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the CA3 complementary encodings study (examples vs. concepts).

---

## Model Architecture Parameters

| Region | Symbol | Neurons (N) | Density (a) | Synapses per neuron (l) | Correlation (rho) |
|--------|--------|-------------|-------------|------------------------|-------------------|
| EC | NEC | 1024 | 0.10 | - | 0.15 |
| DG | NDG | 8192 | 0.005 | 205 (from EC) | 0.02 |
| CA3 (MF) | NCA3 | 2048 | 0.02 | 8 (from DG) | 0.01 |
| CA3 (PP) | NCA3 | 2048 | 0.20 | 205 (from EC) | 0.09 |

---

## Autoencoder Training Parameters

| Parameter | Value |
|-----------|-------|
| Dataset | FashionMNIST (sneakers, trousers, coats) |
| Examples per concept | 256 |
| Total concepts | 3 |
| Hidden layer sizes | 128, 1024, 128 |
| Middle layer (EC) neurons | 1024 |
| Target density aEC | 0.10 |
| Sparsification strength (lambda) | 10 |
| Binarization method | Heaviside step + straight-through estimator |
| Training epochs | 150 |
| Batch size | 64 |
| Optimizer | Adam |
| Learning rate | 1e-3 |
| Weight decay | 1e-5 |
| Nonlinearities | ReLU (layers 1, 3), sigmoid (output) |
| Sparsification loss | KL divergence between hidden density and aEC |

---

## Feedforward Projection Parameters

| Projection | Pre-synaptic N | Post-synaptic N | l (synapses) | a_post | rho_post |
|-----------|---------------|----------------|-------------|--------|---------|
| EC -> DG | 1024 | 8192 | 205 | 0.005 | 0.02 |
| DG -> CA3 (MF) | 8192 | 2048 | 8 | 0.02 | 0.01 |
| EC -> CA3 (PP) | 1024 | 2048 | 205 | 0.20 | 0.09 |

Biological rationale: rodents have roughly 5-10x more DG granule cells and 2-3x more CA3 pyramidal cells relative to medial EC layer II principal neurons. DG place cells are roughly 10x less active than medial EC grid cells during locomotion.

---

## Experiment 1: Sparsification Decorrelates Patterns

| Pre-synaptic density (a_pre) | Pre-synaptic correlation (rho_pre) | Post-synaptic density (a_post) | Post-synaptic correlation (rho_post) |
|-----------------------------|-----------------------------------|-------------------------------|-------------------------------------|
| 0.10 | 0.15 | 0.005 | ~0.02 |
| 0.10 | 0.15 | 0.02 | ~0.01 |
| 0.10 | 0.15 | 0.20 | ~0.09 |

Fig. 2E: Enforcing sparser postsynaptic patterns promotes decorrelation. Theoretical predictions from Eq. 1 match simulated data across 8 random connectivity matrices. Dark gray uses EC patterns as presynaptic inputs; green uses randomly generated patterns at various densities and correlations. Both follow the same theoretical curve.

Fig. 2F: Decoded images from MF encodings remain visually distinct across examples, while decoded images from PP encodings blur across examples within the same concept.

---

## Experiment 2: Hopfield-Like CA3 Storage and Retrieval

### Storage Mechanism

| Parameter | Value |
|-----------|-------|
| Storage rule | Linear combination of MF and PP encodings |
| MF weight | Greater (stronger MF inputs) |
| PP weight | Lesser |
| Update rule | Asynchronous |
| Noise model | Random bit flips of stored patterns |

### Retrieval Under Different Thresholds

| Threshold Setting | Retrieved Encoding Type | Pattern Character | Behavior |
|------------------|------------------------|-------------------|----------|
| High (0.6) | MF-like (sparse) | Example-specific | Distinct patterns maintained |
| Low (0.2) | PP-like (dense) | Concept-level | Patterns merge along shared features |
| Intermediate | Mixed | Transitional | Partial merging |

Fig. 3: As more memories are stored, the dense PP-based attractor basins merge along shared concept features, while sparse MF-based attractor basins remain separated. The model performs successful pattern completion for both encoding types.

### Memory Capacity Analysis

| Memory Load | MF Overlap with Stored Pattern | PP Overlap with Stored Pattern | Concept Merging Observed |
|------------|-------------------------------|-------------------------------|-------------------------|
| Low | High | High | No |
| Medium | High | Moderate | Partial |
| High | Moderate-High | Low (individual) / High (concept) | Yes |

Fig. 3 panels show that MF examples remain distinct across all memory loads tested, while PP examples progressively build concept representations as storage increases.

---

## Experiment 3: Oscillating Threshold (Theta Simulation)

Four conditions were tested to evaluate how an oscillating threshold mimics theta-driven switching between example and concept regimes.

| Condition | Threshold Type | Threshold Values | MF Cue | Key Observation |
|-----------|---------------|-----------------|--------|-----------------|
| Baseline | Abrupt changes | 0.6 / 0.2 | Initial only | Clean switching between MF and PP regimes |
| Sinusoidal | Smooth oscillation | 0.6 / 0.2 | Initial only | Gradual transition; still shows alternation |
| Shifted thresholds | Abrupt changes | 0.55 / 0.25 | Initial only | Reduced separation but still functional |
| Sustained MF cue | Abrupt changes | 0.6 / 0.2 | Throughout | MF patterns dominate; concepts still emerge at low threshold |

Fig. 4A: Pattern overlap dynamics for all four conditions showing overlaps with MF examples (top rows) and PP concepts (bottom rows). Overlaps alternate in phase with the threshold oscillation.

Fig. 4: The model successfully transitions between concept and example representations under oscillating threshold in all four conditions, though the cleanest transitions occur with abrupt threshold changes and initial-only MF cues.

---

## Experiment 4: Single-Neuron Information vs. Theta Phase (Linear Track)

### Model Prediction

| Regime | Sparsity | Predicted Information Type | Information Per Spike |
|--------|----------|---------------------------|---------------------|
| High threshold (sparse) | Low activity | Example (fine position) | Higher |
| Low threshold (dense) | High activity | Concept (coarse position) | Lower |

Fig. 5A: Model predictions confirmed -- single neurons convey more information per spike about example identity during sparse regimes. Each point represents a neuron.

### Place Cell Analysis -- Position Information by Theta Phase

| Theta Phase Bin | Population Sparsity | Spatial Information Per Spike | Spatial Field Width |
|----------------|--------------------|-----------------------------|-------------------|
| Sparse phases | Low fraction active | Higher | Narrower |
| Dense phases | High fraction active | Lower | Broader |

Fig. 5B: Example CA3 place cell activity along a linear track. Each spike represented at equivalent phases with histograms over position and theta phase.

Fig. 5C: Activity split by theta phase shows that sparser phases yield more precise spatial tuning.

Fig. 5: Place field data support the model prediction that sparser theta phases preferentially encode finer, example-like positions. More precise spatial tuning and narrower fields observed during sparser phases.

---

## Experiment 5: Concept-Like Position Encoding at Dense Theta Phases

### Coarse Region Encoding

| Theta Phase Type | Information About Fine Position | Information About Coarse Region | Interpretation |
|-----------------|-------------------------------|-------------------------------|---------------|
| Sparse phases | High | Lower | Example encoding |
| Dense phases | Lower | Higher | Concept encoding |

Fig. 6A: Model predicts that single neurons convey more information per spike about concept identity during dense regimes.

Fig. 6B: CA3 place cells construe fine positions as examples, which combine into coarser regions as concepts.

Fig. 6C: Position information per spike calculated at each theta phase bin confirms the model's prediction.

Fig. 6: Place cell data support the model prediction that denser theta phases preferentially encode coarser, concept-like positions.

---

## Experiment 6: Turn Direction Encoding in W-Maze

### Task Feature Encoding by Theta Phase

| Feature | Sparse Phase Encoding | Dense Phase Encoding | Model Prediction Confirmed |
|---------|----------------------|---------------------|--------------------------|
| Fine position | Enhanced | Reduced | Yes |
| Turn direction | Enhanced | Reduced | Yes |
| Position only (generalizing over turns) | Reduced | Enhanced | Yes |

Fig. 7A: Same model prediction as Fig. 5A applied to W-maze context.

Fig. 7B: CA3 place cells store turn directions during the central arm as examples; combining across turns yields concepts encoding position alone.

Fig. 7C-H: Single-neuron information results. Example place cell active during outward runs shows differential activity across theta phases.

Fig. 7: W-maze data confirm that sparser theta phases preferentially encode turn direction in addition to position, consistent with the model's prediction that sparser regimes carry more example-specific (detailed) information.

---

## Experiment 7: Network-Level Analysis of Theta Phase Coding

### Population Decoding Across Theta Phases

| Analysis Level | Sparse Phases | Dense Phases |
|---------------|--------------|-------------|
| Single-neuron information | Higher per spike for examples | Higher per spike for concepts |
| Network population decoding | Better example discrimination | Better concept classification |
| Population sparsity | Lower fraction of neurons active | Higher fraction of neurons active |

Fig. 7 (extended): Network-level results corroborate single-neuron findings, showing that the CA3 population alternately encodes more specific and more general spatial features across the theta cycle.

---

## Experiment 8: Machine Learning Extension

### Task Design

| Component | Description |
|-----------|-------------|
| Base dataset | MNIST digits (0-9) |
| Extension | Each image randomly assigned an additional set label |
| Task 1 (concept) | Digit classification (requires generalization) |
| Task 2 (example) | Set identification (requires distinguishing individual images) |
| Testing for Task 1 | Held-out test images |
| Testing for Task 2 | Training images (must be individually recalled) |

### Network Architecture

| Layer | Size | Details |
|-------|------|---------|
| Input | 784 | 28x28 MNIST images |
| Hidden 1 | 50 | ReLU activation |
| Hidden 2 | 50 | ReLU activation |
| Output (digit) | 10 | Softmax classification |
| Output (set) | Variable | Set identification head |

### Loss Function Components

| Loss Component | Purpose | Effect on Representations |
|---------------|---------|--------------------------|
| Cross-entropy (digit) | Digit classification | Promotes correlated (concept) encoding |
| Cross-entropy (set) | Set identification | Promotes decorrelated (example) encoding |
| Correlation loss (novel) | Hybrid encoding | Encourages both correlated and decorrelated representations |

### Performance Comparison

| Model Variant | Digit Classification Accuracy | Set Identification Accuracy | Combined Performance |
|--------------|------------------------------|---------------------------|---------------------|
| Standard multitask | Baseline | Baseline | Baseline |
| With correlation loss | Improved | Improved | Best |
| Single-task (digit only) | Good | N/A | N/A |
| Single-task (set only) | N/A | Good | N/A |

Fig. 8A: Dataset extension schematic showing random set label assignment.

Fig. 8B-F: Training and performance results.

Fig. 8B: Network architecture with two hidden layers of 50 neurons each.

Fig. 8C: Task structures showing that digit classification requires building concepts while set identification requires distinguishing examples.

Fig. 8: Complementary encodings inspired by CA3 improve machine learning performance. The novel correlation-based loss term promotes hybrid encoding and yields benefits for both example discrimination and concept classification simultaneously.

---

## Biological Parameter Justification

| Biological Feature | Estimated Value | Model Value | Source |
|-------------------|----------------|-------------|--------|
| DG:EC neuron ratio | 5-10x | 8x (8192/1024) | Anatomical estimates |
| CA3:EC neuron ratio | 2-3x | 2x (2048/1024) | Anatomical estimates |
| DG:EC activity ratio | ~0.1x | 0.05x (0.005/0.1) | Locomotion recordings |
| MF synapses per CA3 | ~50 | 8 | Anatomical estimates |
| PP synapses per CA3 | ~4000 | 205 | Anatomical estimates |
| DG synapses from EC | ~4000 | 205 | Anatomical estimates |

---

## Key Equations and Theoretical Results

### Decorrelation by Sparsification (Eq. 1)

The theoretical relationship predicts post-synaptic correlation as a function of pre-synaptic correlation and post-synaptic density. Key finding: sparser post-synaptic activity leads to lower correlation, independent of the number of synapses per neuron (l).

| Pre-synaptic rho | a_post = 0.005 | a_post = 0.02 | a_post = 0.20 |
|------------------|----------------|---------------|---------------|
| 0.15 | ~0.02 | ~0.01 | ~0.09 |
| 0.10 | ~0.01 | ~0.008 | ~0.06 |
| 0.05 | ~0.005 | ~0.004 | ~0.03 |

### Hopfield Energy and Storage

Storage capacity of the Hopfield-like network varies with the balance of MF and PP encodings. Both encoding types can be successfully retrieved via pattern completion from noisy cues.

---

## Datasets and Baselines

| Dataset | Usage | Details |
|---------|-------|---------|
| FashionMNIST | Model input (sneakers, trousers, coats) | 256 images per class, 3 classes |
| Rat CA3 place cell recordings (linear track) | Neural data analysis | Publicly available; theta phase-resolved |
| Rat CA3 place cell recordings (W-maze) | Neural data analysis | Alternation task; turn direction encoding |
| MNIST | Machine learning extension | Digits 0-9 with augmented set labels |

---

## Statistical Methods

| Method | Application |
|--------|------------|
| Mean +/- SD over random connectivity matrices | Correlation and density statistics (n=8 matrices) |
| Pattern overlap | Retrieval success metric (dot product with stored patterns) |
| Spatial information per spike (bits/spike) | Theta phase-resolved place cell analysis |
| Population sparsity | Fraction of neurons active at each theta phase |
| Winners-take-all | Binarization of postsynaptic activity at desired density |

---

## Figure Summary

| Figure | Key Finding |
|--------|------------|
| Fig. 1 | Overview: EC projects to CA3 via PP (dense) and MF (sparse via DG); model predicts complementary encoding |
| Fig. 2 | Memory transformation along hippocampal pathways; MF and PP encodings converge at CA3 with different statistical properties |
| Fig. 3 | Hopfield-like CA3 stores both encodings; MF examples remain distinct while PP examples merge into concepts |
| Fig. 4 | Oscillating threshold enables alternation between MF example and PP concept representations |
| Fig. 5 | Place field data: sparser theta phases encode finer positions (example-like) |
| Fig. 6 | Place field data: denser theta phases encode coarser regions (concept-like) |
| Fig. 7 | W-maze data: sparser theta phases also encode turn direction (additional example detail) |
| Fig. 8 | Machine learning: novel correlation loss term improves multitask learning by promoting hybrid encoding |

---

## Reference Count
103 references cited in the paper.

