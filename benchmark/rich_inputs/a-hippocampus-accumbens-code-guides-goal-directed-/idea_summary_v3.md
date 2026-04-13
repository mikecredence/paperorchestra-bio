## Working title
A hippocampus-accumbens code guides goal-directed appetitive behavior

## Core question
What specific spatial, contextual, and behavioral information does the dorsal hippocampus (dHPC) route to the nucleus accumbens (NAc) during goal-directed navigation, and does this information stream play a causal role in appetitive behavior?

## Motivation / gap
- The hippocampus processes memory and spatial information, but which output pathways send which types of information to guide memory-driven behavior remains poorly understood
- Hippocampal principal neurons are structurally and functionally diverse in terms of morphology, electrophysiology, and projection patterns, but data on large populations of identified projection neurons during behavior is scarce
- The NAc is proposed as the interface between limbic and motor circuitry, yet the specific contents of the hippocampal information stream reaching NAc are largely unknown
- Electrophysiological studies of projection-specific hippocampal coding are limited by relatively low sample sizes or indirect connectivity measurements
- While disabling HPC-to-NAc projections diminishes conditioned place preference, evidence for projection-specific reward zone representations and their behavioral consequences has remained sparse

## Core contribution (bullet form)
- Identified a significantly higher proportion of place cells in dHPC-to-NAc neurons (169/444 neurons; 38%) compared to dHPC- neurons (1,581/4,928 neurons; 32%; chi-squared test, p = 0.012), with higher spatial information rate (Welch's t(186.55) = 4.770, p < 0.001), sparsity (Welch's t(218.79) = 3.657, p < 0.001), reliability (Welch's t(203.46) = 2.479, p = 0.014), and in-place field activity (Welch's t(190.32) = 2.884, p = 0.0044)
- Speed-inhibited neurons are overrepresented in dHPC-to-NAc population (21% vs. 15%, chi-squared(1, 5372) = 13.66, p = 0.00022), while speed-excited proportions are comparable (16% vs. 13%, p = 0.109)
- Appetitive licking-excited neurons are overrepresented in dHPC-to-NAc neurons (7.4% vs. 3.8%, chi-squared(1, 5372) = 13.018, p = 0.00031), while lick-inhibited proportions do not differ (17.1% vs. 19.7%, p = 0.20)
- Optogenetic activation of dHPC terminals in NAc induced mouth movement (paired t-test, t(3) = 7.485, p = 0.00494 for ChR2; t(2) = 1.353, p = 0.309 for EYFP) and deceleration (t(3) = -3.551, p = 0.0381 for ChR2; t(2) = -1.263, p = 0.334 for EYFP)
- GLM analysis confirmed enhanced conjunctive coding in dHPC-to-NAc neurons (44% vs. 19% conjunctive coding neurons, p < 0.001, chi-squared), with increased proportions for position (chi-squared(1, 5372) = 93.634), velocity (chi-squared(1, 5372) = 141.86), and licking (chi-squared(1, 5372) = 10.050)
- Conjunctive coding neurons allow a linear decoder to classify the presence of reward zone more accurately than non-conjunctive coding neurons (Wilcoxon's W(18) = 14.0, p < 0.001)

## Method in brief
We employed dual-color two-photon calcium imaging in Thy1-GCaMP6s mice to simultaneously record from large populations of hippocampal neurons while identifying NAc-projecting neurons via retrograde labeling with mCherry. AAVrg-pgk-Cre (titer: 1 x 10^13 vg/ml) was injected into the NAc (coordinates: -1.3 mm AP, -1.0 mm lateral, 5.0 and 4.3 mm ventral, relative to Bregma; 2 x 500 nl at 100 nl/min) and AAV5-hSyn-DIO-mCherry (titer: 1.1 x 10^13 vg/ml; 200 nl) into dHPC (3.38 mm AP, -2.5 mm lateral, 1.8 mm ventral, at 10-degree angle). Imaging was performed after 5 days of behavioral training on a 360 cm textile belt with six textured zones including a 30 cm hidden reward zone and 30 cm anticipation zone. A total of 5,372 GCaMP-expressing neurons including 444 putative dHPC-to-NAc neurons were obtained across 6 mice and 19 imaging sessions.

Place cells were identified by comparing spatial information content against 1000x randomly shuffled distributions (95th percentile threshold). Velocity modulation was assessed by linear regression of calcium activity against 1 cm/s velocity bins from 2 to 30 cm/s, with Benjamini/Hochberg FDR correction at p < 0.05. Appetitive lick modulation was assessed using Wilcoxon's non-parametric paired test on pre/post calcium activity. A generalized linear model (GLM) using position, velocity, and appetitive licking as predictors was trained with 3 x 100 shuffled models per feature to determine significant contributions (>95% of shuffled models showing reduced R2). For optogenetic experiments, AAV2-CaMKII-hChR2(H134R)-EYFP-WPRE (titer: 4 x 10^12 TU) or rAAV2-CaMKII-EYFP (titer: 4.3 x 10^12 TU) was injected bilaterally into dHPC (200 nl each), with fiber-optic cannulas implanted bilaterally on NAc (+1.3 mm AP, +/-1 mm lateral, -4.9 mm ventral). Stimulation was delivered at 5 mW, 473 nm, 20 Hz (5 ms pulses) for up to 10 seconds (n = 4 ChR2, n = 3 EYFP mice).

Reward zone decoding used an SVM-based linear classifier cross-validated on odd/even laps. Population comparisons used sample size-matched random subsets of the larger population. All data are presented as mean +/- SEM with significance threshold at p < 0.05.

## Target venue
Nature Communications
