Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Nature Communications

## Idea Summary

## Working title
Cardiac Cycle Timing Modulates Neural Representations of Reward Prediction Errors During Learning

## Core question
Does the timing of reward-related outcomes relative to the cardiac cycle (systole vs diastole) modulate neural representations of prediction errors and influence learning performance?

## Motivation / gap
- Cardiac cycle phases are known to modulate perception of near-threshold sensory stimuli, but effects on internal non-sensory representations are unknown
- Prediction errors (PEs) drive reinforcement learning but their interaction with interoceptive signals has not been studied
- Absolute PE magnitude can be near-threshold even when associated with suprathreshold sensory events, enabling dissociation of cardiac effects on internal vs sensory representations
- The cardiac-related neural signal (CRS) measured via EEG is known to carry predictions about bodily state, but its relationship to learning has not been established
- No prior work has linked cardiac cycle timing to computational model-derived learning indices

## Core contribution (bullet form)
- Demonstrated that single-trial CRS magnitude discriminates between high and low absolute PEs but not between positive and negative signed PEs
- Showed that absolute PE discrimination from CRS-locked EEG is reduced when outcomes occur during systole compared to diastole (analogous to sensory suppression during systole)
- Found that participants with stronger cardiac-cycle-dependent PE discrimination exhibited higher learning rates and greater task accuracy
- The simpler RL model without cue bias outperformed the biased model (BIC = 362.17 vs 377.40), suggesting no face/house bias
- Machine learning discrimination (Az) of high vs low absolute PE peaked significantly above chance using CRS-locked EEG data
- 32 participants analyzed (35 recruited, 3 excluded for EEG noise)

## Method in brief
Thirty-two participants performed a reward-guided decision task (modified weather prediction task) with face and house cues predicting orange or blue outcomes. Four association schemes (highly predictive anticorrelated, highly predictive correlated, variable predictive, non-predictive) modulated learning across eight blocks of 60 trials (480 total). EEG (64 channels) and ECG were recorded simultaneously, with a 4-second outcome period ensuring multiple heartbeats per trial (mean 4.58, SD 0.85 heartbeats).

Choices were modeled using two reinforcement learning models (with and without cue bias), compared via BIC. Prediction errors were decomposed into absolute PE (surprise/salience) and signed PE (better/worse than expected). CRS was extracted from EEG locked to R-wave peaks during the outcome period. Machine learning classification (discriminant analysis, cross-validated Az) was used to decode high vs low absolute PE from CRS-locked EEG. Cardiac cycle effects were assessed by comparing CRS and PE discrimination for outcomes occurring during systole vs diastole.

## Target venue
Nature Communications


## Experimental Log

# Experimental Log: Cardiac Cycle and Reward Learning

## Participants

| Parameter | Value |
|-----------|-------|
| Recruited | 35 |
| Excluded (EEG noise) | 3 |
| Analyzed | 32 |
| Mean age +/- SD | 24 +/- 7.13 years |
| Female | 10 |
| Handedness (Edinburgh, mean +/- SD) | 0.83 +/- 0.13 |
| All right-handed | Yes |

## Task Design

| Parameter | Value |
|-----------|-------|
| Task type | Modified weather prediction / reward-guided decision |
| Cue types | Face and house images (10 each, 512x512 px) |
| Response options | Orange or blue (circles, 125x125 px) |
| Outcome period | 4 seconds |
| Mean heartbeats per outcome | 4.58 +/- 0.85 |
| Blocks | 8 (60 trials each) |
| Total trials | 480 |
| Association schemes | 4 types |
| Viewing distance | 70 cm |
| EEG channels | 64 |

## Association Schemes (Fig 1C)

| Scheme | Abbreviation | Cue-Colour Association |
|--------|-------------|----------------------|
| Highly predictive anticorrelated | HA | Each stimulus predicts different colour |
| Highly predictive correlated | HC | Both stimuli predict same colour |
| Variable predictive | VP | One stimulus predictive, other not |
| Non-predictive | NP | No cue-colour associations |

Each scheme played twice during the session. Two new objects per block.

## Computational Modeling (Fig 1D-H)

### Model Comparison

| Model | BIC | Description |
|-------|-----|-------------|
| Simple prediction (no cue bias) | 362.17 | Better fit |
| Cue-biased prediction | 377.40 | Worse fit |
| Winner | Simple model | No face/house bias |

### RL Parameters (Fig 1E-G)

| Parameter | Range/Distribution |
|-----------|-------------------|
| Learning rate (alpha) | Estimated per participant |
| Temperature (beta) | Estimated per participant |
| Prediction error types | Absolute PE (surprise) and Signed PE (valence) |

## CRS Morphology and PE Discrimination (Fig 2)

### CRS Waveform Analysis

| ROI | Electrodes | CRS Feature |
|-----|-----------|-------------|
| Fronto-central | Clustered FC electrodes | Prominent CRS component |
| Central-parietal | Clustered CP electrodes | Prominent CRS component |

### CRS by PE Type (Fig 2B-D)

| Comparison | CRS Difference | Significance |
|-----------|----------------|-------------|
| Positive vs Negative Signed PE | No significant difference | NS |
| High vs Low Absolute PE | Significant difference | p < 0.05 |

Key finding: CRS magnitude tracks absolute PE (surprise/salience) but not signed PE (valence).

## Machine Learning Discrimination (Fig 3)

### Absolute PE Discrimination (High vs Low)

| Analysis | Metric | Value |
|----------|--------|-------|
| Method | Cross-validated discriminant analysis | -- |
| Metric | Area under curve (Az) | -- |
| Data | CRS-locked EEG, highest vs lowest quantile of absolute PE | -- |
| Result | Significant discrimination above chance | p < 0.05 |
| Peak timing | Around CRS peak latency | -- |

Fig 3A: Data selection using highest and lowest absolute PE quantiles.
Fig 3B: Discriminator performance (Az) averaged across N=32 subjects shows significant above-chance discrimination.

## Cardiac Cycle Effects (Fig 4)

### CRS Amplitude: Systole vs Diastole (Fig 4B)

| Phase | CRS Magnitude | Comparison |
|-------|--------------|------------|
| Systole (first CRS after outcome) | Lower | -- |
| Diastole (first CRS after outcome) | Higher | -- |
| Difference | Significant (N=32) | Violin plot distribution |

### Absolute PE Discrimination by Cardiac Phase

| Cardiac Phase | PE Discrimination (Az) | Comparison |
|--------------|----------------------|------------|
| Outcome at systole | Lower discrimination | -- |
| Outcome at diastole | Higher discrimination | -- |
| Difference | Significant | Parallels sensory suppression at systole |

Key finding: Just as perception of near-threshold sensory stimuli is reduced at systole, discrimination of near-threshold absolute PEs is also reduced when outcomes occur at systole.

### Individual Differences: Cardiac Modulation vs Learning (Fig 4)

| Correlation | Variables | Direction |
|-------------|-----------|-----------|
| Cardiac PE discrimination difference (diastole - systole) vs Learning rate | Positive | Higher cardiac modulation = higher learning rate |
| Cardiac PE discrimination difference vs Task accuracy (rewards) | Positive | Higher cardiac modulation = more rewards |

Participants who show stronger cardiac-cycle-dependent PE discrimination exhibit better learning outcomes.

### Block-Type Specificity

| Block Type | CRS-Learning Relationship |
|-----------|--------------------------|
| Predictive blocks (HA, HC, VP) | Relationship between CRS and learning present |
| Non-predictive blocks (NP) | No relationship (learning not possible) |

## Control Analyses (Supplementary Figures)

### Trial Count Balance (Supplementary Fig 3A)

| Factor | Systole vs Diastole | Result |
|--------|-------------------|--------|
| Trial counts by block type | Balanced | No confound |

### Absolute PE by Cardiac Phase (Supplementary Fig 3B)

| Phase | Mean Absolute PE | Significance |
|-------|-----------------|-------------|
| Systole | Similar | NS (N=32) |
| Diastole | Similar | No difference in PE magnitude by phase |

### Reward by Cardiac Phase (Supplementary Fig 3C)

| Phase | Mean Reward | Significance |
|-------|------------|-------------|
| Systole | Similar | NS (N=32) |
| Diastole | Similar | No difference in reward by phase |

Neither absolute PE values nor reward frequency differ between cardiac phases, ruling out trivial confounds.

### Valence and Absolute PE Controls (Supplementary Fig 4)

| Analysis | Result |
|----------|--------|
| Outcome valence confound check | No unaccounted effects |
| Absolute PE confound check | No unaccounted effects |

## Behavioral Results (Supplementary Fig 1)

### Accuracy by Block Type

| Block Type | Mean Accuracy | Relative |
|-----------|--------------|----------|
| HA (highly predictive anticorrelated) | Highest | Best learning |
| HC (highly predictive correlated) | High | Good learning |
| VP (variable predictive) | Moderate | Partial learning |
| NP (non-predictive) | Lowest (~chance) | No learning possible |

### Reaction Times by Block Type

| Block Type | Log-Transformed RT |
|-----------|-------------------|
| Predictive blocks | Faster |
| Non-predictive | Slower |

Prediction strength is the primary modulator of adaptive behavior.

## Key Figure Observations

- Fig 1A: Task schematic with CRS recording during 4-second outcome period
- Fig 1B: Example cue-colour associations
- Fig 1C: Prediction strengths across the four block types
- Fig 1D: Model prediction of choices matches behavioral data
- Fig 2A: Grand average CRS waveforms across scalp ROIs, time-locked to R-wave
- Fig 2B: No CRS difference for positive vs negative signed PE
- Fig 2C-D: Significant CRS difference for high vs low absolute PE
- Fig 3: Machine learning Az shows significant above-chance absolute PE discrimination
- Fig 4A: Schematic of systole/diastole phases and outcome timing
- Fig 4B: CRS amplitude difference between systole and diastole outcomes
- Supplementary Fig 1: Accuracy and RT data confirm prediction strength drives behavior
- Supplementary Fig 2: Individual subject Az values for PE discrimination
- Supplementary Figs 3-4: Control analyses ruling out confounds

## Methods Summary

| Component | Detail |
|-----------|--------|
| EEG system | 64-channel cap |
| ECG | Standard electrode on chest |
| CRS extraction | R-wave locked EEG epochs |
| RL models | Standard Q-learning with/without cue bias |
| Model comparison | BIC |
| ML classification | Cross-validated discriminant analysis (Az) |
| Cardiac phase | Systole vs diastole based on R-wave timing |
| Statistical tests | Paired t-tests, correlations, violin plots |

