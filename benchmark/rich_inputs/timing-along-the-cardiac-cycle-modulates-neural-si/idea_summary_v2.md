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
