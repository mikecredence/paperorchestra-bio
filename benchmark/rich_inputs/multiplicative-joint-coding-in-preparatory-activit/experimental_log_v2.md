# Experimental Log

> Pre-writing data tables and observations for the multiplicative joint coding study in macaque motor cortex.

---

## Subjects and Recording Setup

| Parameter | Value |
|-----------|-------|
| Species | Rhesus macaque (Macaca mulatta) |
| Number of subjects | 3 (Monkeys C, G, S) |
| Sex | Male |
| Weight range | 5-10 kg |
| Recording area | Motor cortex (M1) |
| Recording devices | Implanted micro-electrode arrays and single electrodes |
| Array dataset | Monkey C (primary dataset for population analyses) |
| Single electrode datasets | Monkeys G and S (replication) |

---

## Task Design Parameters

| Parameter | Value |
|-----------|-------|
| Trial types | 3 (SR, DR-CW, DR-CCW) |
| Directions per trial type | 6 (0, 60, 120, 180, 240, 300 degrees) |
| Total conditions | 18 |
| Cue period duration | 400 ms |
| Memory period duration | 400-800 ms (variable) |
| Target arrangement | Regular hexagon corners |
| DR angular displacement | 120 degrees (CW or CCW) |
| Response window | 700-1200 ms to complete both reaches |
| Reach accuracy margin | 3 cm |
| Trial interleaving | Pseudo-random |
| Analysis inclusion | Correct trials only |

---

## Trial Type Breakdown

| Trial Type | Fraction | 1st Target | 2nd Target | Cue |
|------------|----------|-----------|-----------|-----|
| Single-reach (SR) | 1/3 | Green dot at one of 6 directions | None | Green dot |
| Double-reach CW | 1/3 | Green square at one of 6 directions | Green triangle, 120 deg CW from square | Square + triangle simultaneously |
| Double-reach CCW | 1/3 | Green square at one of 6 directions | Green triangle, 120 deg CCW from square | Square + triangle simultaneously |

---

## Behavioral Validation

| Metric | Value | Comparison |
|--------|-------|-----------|
| Speed profile correlation (DR vs SR, until 1st movement end) | 0.99 +/- 0.006 (mean +/- sd) | Extremely high similarity |
| sEMG correlation (extensor digitorum communis, until 1st ME) | High (specific r not extracted) | Consistent with kinematic equivalence |
| Trajectory overlap (1st reach) | No significant difference (one-way ANOVA, p > 0.05) | DR and SR first reaches are kinematically matched |

Fig 1b shows hand trajectories grouped by 1st/only reach direction from Monkey C. SR and DR trajectories overlap closely before the end of the first reach.

Fig 1c shows surface EMG and speed profiles for one typical session. The first-reach kinematics in DR trials are indistinguishable from SR trials.

---

## Event Markers

| Marker | Abbreviation | Description |
|--------|-------------|-------------|
| GO signal | GO | Central fixation dot turns off |
| 1st/only movement onset | MO | Hand leaves center |
| 1st/only movement end | ME | Hand arrives at 1st target |
| 2nd movement onset | MO2 | Hand leaves 1st target (DR only) |

---

## Single-Neuron Firing Patterns (Fig 2)

| Panel | Neuron Type | Alignment | Key Observation |
|-------|------------|-----------|-----------------|
| Fig 2a | Example cell 1 | MO | Heterogeneous firing across SR, CW, CCW conditions |
| Fig 2b | Example cell 2 | MO | Different modulation pattern |
| Fig 2c | Example cell 3 | GO | Shows preparatory activity differences |
| Fig 2d | Example cell 4 | MO | Further heterogeneity |

Fig 2 demonstrates that motor cortex neurons show highly heterogeneous firing patterns across conditions, with individual neurons modulated differently by 1st reach direction and 2nd reach context.

---

## Regression Model Specifications

| Model | Formula | Parameters |
|-------|---------|-----------|
| Additive | f_DR = f_1st + f_2nd + constant | Linear sum of directional tunings |
| Multiplicative | f_DR = f_1st * g(2nd_direction) | Gain modulation of 1st-reach tuning by 2nd target |
| Full model | f_DR = a * f_1st * g(2nd) + b * f_1st + c * f_2nd + d | Combined multiplicative and additive terms |
| Evaluation metric | Adjusted R2 | Sliding 200-ms window |
| Statistical threshold | p < 0.0005 | Comparison between models |

---

## Model Fitting: Population-Level Results (Fig 5)

| Time Window | Better Model | Significance |
|-------------|-------------|-------------|
| Peri-MO (-100 to 100 ms around MO) | Multiplicative > Additive | p < 0.0005 |
| Peri-ME (around movement end) | Additive > Multiplicative | p < 0.0005 |
| Preparatory period (pre-GO to MO) | Multiplicative dominates | Sustained significance |
| Execution period (MO to ME) | Transition to additive | Gradual shift |

Fig 5a (left panel) shows goodness-of-fit (averaged adjusted R2) for all fitting models in a 200-ms sliding window, with shaded standard error. The upper line marks the significance boundary (p < 0.0005) for the multiplicative vs. additive comparison.

Fig 5a (middle panel) presents scatter plots comparing goodness-of-fit at specific time points between the multiplicative and additive models.

---

## Example Neuron Model Fits (Fig 3)

| Row | 1st Reach Direction | Conditions Shown | Models Displayed |
|-----|-------------------|------------------|-----------------|
| Each row | Fixed 1st reach | SR, CW-60, CW-120, 180, CCW-120, CCW-60 | Data PSTH, Additive reconstruction, Multiplicative reconstruction, Full model |

Fig 3 shows one example neuron's normalized PSTHs alongside reconstructions from the additive, multiplicative, and full models, all aligned to MO. The multiplicative model captures the gain-like modulation visible in the data during the preparatory period.

---

## Directional Tuning Analysis (Fig 4)

| Time Window | R2 (Additive) | R2 (Multiplicative) | Observation |
|-------------|--------------|---------------------|-------------|
| Peri-MO (-100 to 100 ms) | Lower | Higher | Multiplicative captures gain modulation of tuning curves |
| Peri-ME | Higher | Lower | Additive captures independent parallel coding |

Fig 4a shows directional tuning curves around MO for the example neuron. DR condition firing rates are plotted in corresponding colors with Fourier expansion fits. The multiplicative model's tuning curves match the data better than the additive model's.

Fig 4b shows the same analysis around ME, where the pattern reverses.

---

## PCA-LDA Dimensionality Reduction Results (Fig 6)

| Projection | Observation |
|------------|-------------|
| Fig 6a: SR space | SR neural states cluster clearly by reaching direction |
| Fig 6b: DR projected onto SR space | DR states also cluster into 6 groups by 1st reach direction |
| Fig 6c: Within 1st-reach clusters | LDA reveals sub-clustering by 2nd reach direction |
| Variance explained | Calculated for two leading dimensions |

Fig 6 demonstrates that during preparation, neural population states for double-reach trials separate first by 1st reach direction (similar to SR), and then further sub-cluster according to 2nd reach direction within each 1st-reach group. This sub-clustering is the population-level signature of multiplicative joint coding.

---

## Population Vector Simulation (Fig 7)

| Model Type | PV Accuracy | Directional Bias |
|------------|-------------|-----------------|
| Single cosine (SR baseline) | Accurate | None |
| Additive model | Reduced accuracy | Systematic bias toward 2nd reach direction |
| Multiplicative model | Preserved accuracy | No systematic bias; robust linear readout maintained |

Fig 7a shows example model neurons simulated under three conditions. Fig 7b plots directional tuning curves with and without 2nd-reach modulation. Fig 7c shows population vectors for single and double reach under each model. The multiplicative model preserves the direction of the PV for the 1st reach, while the additive model distorts it.

---

## RNN Model Results (Fig 8)

| Component | Detail |
|-----------|--------|
| Architecture | Input layer, hidden layer, output layer |
| Input | Position signals for two targets simultaneously |
| Output | Population vector (PV), magnitude reflects movement tendency |
| Training task | Double-reach (same as behavioral task) |
| Key finding | Multiplicative joint coding spontaneously emerges during simulated preparation |

| RNN Analysis | Observation |
|--------------|-------------|
| Fig 8a | Schematic of RNN architecture |
| Fig 8b | Two example hidden-layer nodes show condition-dependent modulation resembling real neurons |
| Nonlinearity | Conspicuous nonlinear encoding properties emerge without being explicitly enforced |
| Transition | RNN also shows shift from multiplicative to additive coding around execution |

---

## Cross-Subject Replication

| Subject | Recording Method | Key Result |
|---------|-----------------|------------|
| Monkey C | Micro-electrode array | Primary dataset; all main analyses |
| Monkey G | Single electrodes | Multiplicative coding replicated |
| Monkey S | Single electrodes | Multiplicative coding replicated |

---

## Coding Mechanism Transition Summary

| Period | Dominant Coding | Interpretation |
|--------|----------------|---------------|
| Cue period | Mixed/emerging | Sequence information begins to emerge |
| Memory/preparatory period | Multiplicative joint coding | 1st and 2nd reach interact through gain modulation |
| Peri-movement onset | Multiplicative peaks | Strongest joint coding |
| Execution (MO to ME) | Transition to additive | Elements become independently represented |
| Post-1st-reach | Additive/parallel | 2nd reach preparation overlaps with 1st reach execution |

---

## Statistical Tests Summary

| Test | Application | Result |
|------|------------|--------|
| One-way ANOVA | Trajectory difference (SR vs DR) before 1st ME | p > 0.05 (no significant difference) |
| Adjusted R2 comparison | Multiplicative vs. additive model fit | p < 0.0005 (peri-MO) |
| Pearson correlation | Speed profiles DR vs SR | r = 0.99 +/- 0.006 |
| Sliding window analysis | 200-ms window, model comparison over time | Tracks transition from multiplicative to additive |

---

## Key Equations

| Equation | Description |
|----------|-------------|
| f_DR = f_1st + f_2nd + c | Additive model |
| f_DR = f_1st * g(theta_2nd) | Multiplicative model |
| f_DR = a * f_1st * g + b * f_1st + c * f_2nd + d | Full (combined) model |
| PV = sum of preferred directions weighted by firing rates | Population vector for readout |

---

## Figure Summary

| Figure | Content |
|--------|---------|
| Fig 1 | Task paradigm, trajectories, EMG/speed validation |
| Fig 2 | Four example neurons showing heterogeneous firing patterns |
| Fig 3 | Model fitting for one example neuron (data, additive, multiplicative, full) |
| Fig 4 | Directional tuning curves around MO and ME with R2 comparisons |
| Fig 5 | Population-level model comparison across time (sliding window R2) |
| Fig 6 | PCA-LDA dimensionality reduction showing sub-clustering |
| Fig 7 | Population vector simulation comparing additive vs. multiplicative coding |
| Fig 8 | RNN model results reproducing multiplicative joint coding |

---

## Reference Count

| Parameter | Value |
|-----------|-------|
| Total references cited | 59 |
