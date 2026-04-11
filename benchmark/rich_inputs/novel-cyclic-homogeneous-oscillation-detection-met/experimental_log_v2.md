# Experimental Log

> Pre-writing data tables and observations for the CHO (Cyclic Homogeneous Oscillation) detection method study.

---

## Datasets Used

| Dataset | Modality | N Subjects | Task/State | Institution | Key Details |
|---------|----------|-----------|-----------|-------------|-------------|
| ECoG auditory RT | ECoG | 8 (x1-x8, 4 female) | Auditory reaction time (pre-stimulus) | Albany Medical Center | Platinum-iridium electrodes, 4 mm diameter, 2.3 mm exposed, 10 mm spacing |
| EEG auditory RT | EEG | 7 (y1-y7, all male) | Auditory reaction time (pre-stimulus) | Same task as ECoG | 64 electrodes, modified 10-20 system |
| ECoG resting state | ECoG | 6 (ze1-ze6, 1 female) | Resting state | Albany Medical Center | Extensive lateral STG coverage, 3-10 mm electrode spacing |
| SEEG resting state | SEEG | 6 (zs1-zs6, 3 female) | Resting state | Barnes Jewish Hospital, St. Louis | Hippocampal contacts |

---

## Subject Demographics

| Group | N | Sex Distribution | Mean Age | Age Range | Notes |
|-------|---|-----------------|----------|-----------|-------|
| ECoG auditory RT (x1-x8) | 8 | 4 female | 41 +/- 14 | Not specified | Average IQ = 96 +/- 18, range 75-120 |
| EEG auditory RT (y1-y7) | 7 | All male | 27 +/- 3.6 | Not specified | Healthy controls |
| ECoG resting (ze1-ze6) | 6 | 1 female | 46 | 31-69 | Epilepsy patients |
| SEEG resting (zs1-zs6) | 6 | 3 female | 46 +/- 16.6 | Not specified | Epilepsy patients |

---

## Electrode Specifications

| Parameter | ECoG (Auditory RT) | ECoG (Resting) | SEEG |
|-----------|-------------------|----------------|------|
| Material | Platinum-iridium | Platinum-iridium | Approved for human use |
| Diameter | 4 mm (2.3 mm exposed) | Varies (3-10 mm spacing) | Depth electrodes |
| Spacing | 10 mm center-to-center | 3-10 mm | Varies |
| Embedding | Silicone | PMT Corp. | Ad-Tech / PMT |
| Hemisphere (auditory RT) | Left: x1, x3, x6, x7; Right: x2, x4, x5, x8 | Not specified | Bilateral hippocampus |
| Manufacturer | Ad-Tech Medical Corp., PMT Corp. | PMT Corp. | Ad-Tech, PMT Corp. |

---

## CHO Method: Three Criteria

| Criterion | Description | Purpose |
|-----------|-------------|---------|
| 1 | Peaks over 1/f noise must be present in time-frequency domain | Reject aperiodic power |
| 2 | Oscillation must exhibit at least two complete cycles | Distinguish oscillations from EP/ERP and spike artifacts |
| 3 | Periodicity of raw signal must match auto-correlation periodicity | Identify fundamental frequency; reject harmonic false positives |

---

## CHO Procedural Steps (Fig 3)

| Step | Operation | Input | Output |
|------|-----------|-------|--------|
| A | Remove 1/f aperiodic noise in time-frequency space | Raw signal time-frequency map | Initial bounding boxes of candidate oscillations |
| B | Reject bounding boxes with < 2 oscillatory cycles | Bounding boxes from step A | Filtered bounding boxes |
| C | Compute auto-correlation within each bounding box; verify frequency match | Filtered bounding boxes + raw signal | Final validated oscillation detections with fundamental frequency |

---

## Comparison Methods

| Method | Full Name | Domain | Reference |
|--------|-----------|--------|-----------|
| FOOOF | Fitting Oscillations One Over F | Frequency | Donoghue et al., 2020 |
| OEvent | Oscillation Event Detection | Time-frequency | Neymotin et al., 2022 |
| SPRiNT | Spectral Parameterization Resolved in Time | Time-frequency | Wilson et al., 2022 |
| CHO | Cyclic Homogeneous Oscillation | Time + frequency + auto-correlation | This study |

---

## Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Signal type | Non-sinusoidal oscillatory bursts |
| Burst duration | 2.5 cycles, spanning 1-3 seconds |
| Noise type | 1/f (pink noise) |
| Total signal duration | 5 seconds |
| Burst variations tested | 1 cycle, 2.5 cycles, 1 s duration, 3 s duration |
| SNR range | Varied across full range |
| Physiological SNR benchmarks | EEG alpha: -7 dB; ECoG alpha: -6 dB |

---

## Synthetic Results: Peak Frequency Detection (Fig 4B-D)

| Method | Specificity | Sensitivity | Accuracy | False Positives | True Negatives |
|--------|------------|-------------|----------|----------------|----------------|
| CHO | Highest | Comparable to SPRiNT at physiological SNR | Highest overall | Fewest | Most |
| FOOOF | Lower | Higher at some SNR | Lower | More | Fewer |
| OEvent | Lower | Varies | Lower | More | Fewer |
| SPRiNT | Lower | Comparable to CHO at physiological SNR | Lower | More | Fewer |

Fig 4B shows that CHO outperformed all existing methods in specificity for detecting fundamental frequency of non-sinusoidal oscillations.

Fig 4C shows that at SNR levels typical of alpha oscillations in EEG (-7 dB) and ECoG (-6 dB), CHO sensitivity is comparable to SPRiNT.

Fig 4D demonstrates that overall accuracy of CHO exceeds all comparison methods across SNR levels.

---

## Synthetic Results: Peak Frequency + Onset/Offset Detection (Fig 4E-G)

| Method | Specificity (freq + timing) | Sensitivity (freq + timing) | Accuracy (freq + timing) |
|--------|---------------------------|---------------------------|------------------------|
| CHO | Highest | Lower at very low SNR, comparable at physiological SNR | Highest |
| FOOOF | Lower | N/A (does not detect onset/offset) | N/A |
| OEvent | Lower | Higher at some SNR | Lower |
| SPRiNT | Lower | Comparable at physiological SNR | Lower |

Fig 4E-G parallel the frequency-only results but add the additional requirement of correctly detecting onset and offset times. CHO maintains its specificity advantage.

Fig 4F shows that CHO can effectively detect fundamental frequency plus onset/offset for more than half of all oscillations at physiologically relevant SNR levels.

---

## Synthetic Sinusoidal Oscillation Results (Supp Fig 4-2)

| Observation | Detail |
|-------------|--------|
| CHO on purely sinusoidal signals | Still outperforms existing methods in specificity |
| Sensitivity trend | Increases with increasing SNR |
| Implication | CHO advantage is not limited to non-sinusoidal signals |

---

## Physiological SNR Reference Values

| Modality | Oscillation Band | Typical SNR |
|----------|-----------------|-------------|
| EEG | Alpha | -7 dB |
| ECoG | Alpha | -6 dB |

Supplementary Figure 4-1 shows SNR histograms for EEG and ECoG datasets confirming these typical values.

---

## ECoG Auditory Reaction Time Results (Fig 5)

| Method | Alpha Detection | Beta Detection | Spatial Specificity |
|--------|----------------|----------------|---------------------|
| FOOOF | Alpha and beta over STG and pre-motor area | Broad beta across multiple areas including STG | Lower -- beta detected over STG (likely harmonic of non-sinusoidal alpha) |
| CHO | Alpha primarily within STG | Focal beta over pre-motor area only, NOT STG | Higher -- beta restricted to pre-motor cortex |

Fig 5A compares FOOOF and CHO oscillation maps from ECoG signals during the pre-stimulus period. CHO eliminates the spurious beta detections over STG that FOOOF reports.

Fig 5B investigates whether beta over STG (detected by FOOOF) is actually a harmonic of non-sinusoidal alpha. CHO's auto-correlation criterion correctly rejects these harmonics.

---

## ECoG Results by Subject (Supp Fig 5-1)

| Observation | Detail |
|-------------|--------|
| Subject-level consistency | FOOOF and CHO results shown for all 8 ECoG subjects |
| Pattern | CHO consistently produces more spatially focal beta detections than FOOOF |
| Alpha | Both methods detect alpha over auditory cortex, but CHO is more selective |

---

## EEG Auditory Reaction Time Results (Fig 6)

| Method | Alpha Detection | Beta Detection | Spatial Specificity |
|--------|----------------|----------------|---------------------|
| FOOOF | Alpha over frontal/visual areas; beta across all areas (focus on central) | Broad distribution | Lower |
| CHO | Alpha primarily within visual/occipital areas | Focal beta over pre-motor/central area | Higher |

Fig 6A shows that CHO detected occipital alpha and more spatially specific pre-motor beta from EEG signals, whereas FOOOF reported broader distributions.

---

## EEG Results by Subject (Supp Fig 6-1)

| Observation | Detail |
|-------------|--------|
| All 7 EEG subjects | FOOOF and CHO results shown individually |
| Consistency | CHO produces more anatomically plausible oscillation maps across subjects |

---

## SEEG Hippocampal Resting State Results

| Finding | Detail |
|---------|--------|
| Hippocampal oscillation fundamental frequency | Theta band identified as fundamental |
| Apparent alpha/beta peaks | Determined to be harmonics of non-sinusoidal theta |
| Method advantage | CHO auto-correlation criterion correctly identifies theta as the fundamental, rejecting harmonic peaks |
| N subjects | 6 SEEG subjects |

---

## Non-Sinusoidal Oscillation Characterization

| Feature | CHO Capability |
|---------|---------------|
| Asymmetry detection | Auto-correlation peak/trough asymmetry indicates non-sinusoidal waveform |
| Waveform shape | Can be extracted from validated bounding boxes |
| Fundamental frequency | Determined by auto-correlation periodicity, immune to harmonic confounds |

Fig 2 shows examples of non-sinusoidal (left) and sinusoidal (right) neural oscillations from human auditory cortex, along with their auto-correlations. The non-sinusoidal signal shows asymmetric auto-correlation peaks/troughs.

---

## Auto-Correlation Approach Details (Fig 2)

| Signal Type | Auto-Correlation Feature | Frequency Determination |
|-------------|------------------------|------------------------|
| Non-sinusoidal | Asymmetric peaks and troughs | Peak spacing reveals fundamental period |
| Sinusoidal | Symmetric peaks and troughs | Peak spacing confirms frequency |
| Harmonic-contaminated spectrum | Multiple spectral peaks | Auto-correlation resolves true fundamental |

---

## Harmonic Problem Illustration (Fig 1)

| Panel | Observation |
|-------|-------------|
| Fig 1A | Non-sinusoidal theta-band oscillation from human auditory cortex |
| Fig 1B | Power spectrum shows multiple harmonic peaks in alpha and beta bands |
| Fig 1C | Time-frequency domain also shows harmonic peaks |
| Implication | Without auto-correlation criterion, harmonics would be falsely detected as independent oscillations |

---

## Key Performance Claims

| Claim | Supporting Evidence |
|-------|--------------------|
| High specificity | Fewest false positives across all SNR levels in simulation (Fig 4B, 4E) |
| Comparable sensitivity at physiological SNR | Matches SPRiNT at -7 dB (EEG) and -6 dB (ECoG) (Fig 4C, 4F) |
| Highest overall accuracy | Combined specificity and sensitivity advantage (Fig 4D, 4G) |
| Anatomically specific detections | Beta restricted to pre-motor in ECoG; alpha to STG/occipital (Fig 5, 6) |
| Correct hippocampal fundamental | Theta identified as fundamental, not alpha/beta harmonics (SEEG results) |

---

## Applications Discussed

| Application | Relevance |
|-------------|-----------|
| Closed-loop neuromodulation | Accurate onset/offset detection enables real-time feedback |
| Brain-computer interfaces | Precise oscillation characterization improves BCI decoding |
| Neurofeedback | Reliable frequency identification avoids training on harmonic artifacts |
| Neurological diagnostics | Oscillatory biomarkers require specific, accurate detection |
| Interregional communication | Understanding "when/where/what" of oscillations essential for studying brain networks |

---

## Software and Technical Parameters

| Parameter | Value |
|-----------|-------|
| 1/f estimation | Spectral parameterization (similar to FOOOF approach) |
| Auto-correlation | Standard normalized auto-correlation of raw signal within bounding box |
| Minimum cycle requirement | 2 complete cycles |
| Bounding box generation | From peaks exceeding 1/f threshold in time-frequency domain |

---

## Reference Count and Scope

| Parameter | Value |
|-----------|-------|
| Total references cited | 64 |
| Recording modalities used | ECoG, EEG, SEEG |
| Total subjects across all datasets | 27 (8 + 7 + 6 + 6) |
| Comparison methods | 3 (FOOOF, OEvent, SPRiNT) |
| Simulation types | Non-sinusoidal bursts + sinusoidal control |
