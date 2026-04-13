Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

## Working title

EEG-fMRI in awake rats reveals suppressed whole-brain sensory responsiveness during absence seizures, corroborated by mean-field simulations

## Core question

How does the brain's hemodynamic response to visual and somatosensory stimulation change during absence seizures compared to interictal periods, and can a computational mean-field model explain the observed suppression of sensory processing during ictal states?

## Motivation / gap

- Absence epilepsy causes transient consciousness impairment and is linked to neuropsychiatric comorbidities (attention, memory, mood deficits), but the neural mechanism underlying reduced responsiveness to environmental stimuli during seizures remains poorly understood
- Prior human neuroimaging studies of absence epilepsy have been conducted exclusively at rest, without controlled external stimulation; therefore, how the brain manages incoming sensory information during spike-and-wave discharges (SWDs) is unknown
- Existing fMRI studies in rodent epilepsy models typically use curarized or anesthetized animals, confounding the interpretation of brain states; awake-state imaging with simultaneous EEG is technically difficult
- The loud acoustic noise from standard EPI sequences is a major stressor for awake rats, increasing motion artifacts and suppressing spontaneous seizure generation
- No prior study has combined awake-state fMRI of absence seizures with sensory stimulation paradigms and computational modeling to bridge the gap between hemodynamic observations and neural dynamics

## Core contribution (bullet form)

- Established a zero-echo-time (ZTE) fMRI protocol for non-curarized awake GAERS rats, achieving 35.8 dB lower acoustic noise than EPI (78.7 dB vs. 114.5 dB) and mean framewise displacement of only 0.69 +/- 0.32 um
- Demonstrated that whole-brain hemodynamic responses to both visual and whisker stimulation are globally suppressed and spatially restricted during ictal periods relative to interictal periods (F-contrast maps, p < 0.05 cluster-corrected)
- Showed that cortical hemodynamic responses become negatively polarized during seizures despite sensory stimulation, suggesting active suppression rather than mere absence of activation
- Mean-field simulation using an AdEx (Adaptive Exponential) model reproduced the spike-and-wave discharge dynamics and revealed restricted propagation of stimulation-evoked activity during ictal states, matching fMRI findings
- Identified specific brain structures differentially engaged: visual cortex, superior colliculus, and lateral geniculate nucleus for visual stimulation; barrel field somatosensory cortex and ventral posteromedial thalamus for whisker stimulation, with frontal cortex (prelimbic, cingulate, secondary motor) activated in both modalities during interictal state
- Signal change with ZTE was approximately 0.3% (vs. 1-1.5% with GE-EPI), but with substantially reduced susceptibility-induced distortions and EEG gradient artifacts

## Method in brief

Eleven adult GAERS rats (8-12 months, 6 male / 5 female) were implanted with carbon fiber EEG electrodes over motor and somatosensory cortex plus a cerebellar reference. After a multi-week habituation protocol to the restraint holder and scanner noise, animals underwent awake EEG-fMRI sessions using a quiet ZTE sequence on a 9.4T Bruker scanner with a custom transmit-receive loop coil (spatial SNR ~25, temporal SNR 30-60). Visual stimulation was delivered via bilateral optical fiber cables near the eyes, and whisker stimulation via bilateral air-puff tips. In each 45-minute scanning session, 6-second stimulation blocks were delivered during both interictal baseline periods and spontaneous absence seizures, with EEG used to classify each block as ictal or interictal post hoc.

Whole-brain hemodynamic response functions (HRFs) were modeled using a GLM with gamma basis functions. Parameter estimates were computed voxel-wise, and F-contrast maps (p < 0.05, cluster-corrected) compared interictal vs. ictal stimulation responses. ROI-based HRF analyses with extreme beta-value comparisons were performed for visual pathway structures (visual cortex, superior colliculus, lateral geniculate nucleus) and somatosensory pathway structures (barrel field cortex, ventral posteromedial thalamus). A separate analysis characterized the hemodynamic signature of seizures themselves (without stimulation) across cortical and subcortical regions. Additionally, a mean-field simulation based on the AdEx neuron model was developed to reproduce both asynchronous irregular (interictal) and SWD (ictal) dynamics by modulating the adaptation current strength, allowing virtual stimulation experiments to test whether activity propagation is inherently restricted during the ictal regime.

## Target venue

eLife


## Experimental Log

# Experimental Log: Absence Seizure Impairment of Sensory Perception via EEG-fMRI in Awake Rats

## 1. Experimental Design Overview

| Parameter | Detail |
|---|---|
| Animal model | GAERS (Genetic Absence Epilepsy Rats from Strasbourg) |
| Total animals | 11 adult rats |
| Age | 8-12 months |
| Weight | 260 +/- 21 g |
| Sex distribution | 6 males, 5 females |
| Housing | Individual cages, 12/12 h light-dark cycle |
| Room temperature | 22 +/- 2 C |
| Humidity | 50-60% |
| Ethical approval | Comite Local GIN, C2EA-04; EU Directive 2010/63/EU |

## 2. EEG Implantation Details

| Component | Specification |
|---|---|
| Electrode material | Carbon fiber (WPI Sarasota FL) |
| Electrode tip length | ~5 mm brush-like |
| Electrode lead length | ~30 mm |
| Recording site 1 | Right motor cortex (AP: +2, ML: +2.5 mm) |
| Recording site 2 | Right primary somatosensory cortex (AP: -2.5, ML: +3 mm) |
| Reference/ground | Cerebellum (AP: -12, ML: +2 mm) |
| Anesthesia for surgery | Isoflurane (induction 5%, maintenance 1-2%) |
| Local anesthetic | Lidocaine hydrochloride (2g/100ml, 0.05 ml/site) |
| Fixation method | Cyanoacrylate + dental cement (Selectaplus) |

## 3. MRI Acquisition Parameters

| Parameter | ZTE Sequence | EPI Sequence |
|---|---|---|
| Scanner | 9.4T Bruker | 9.4T Bruker |
| Coil type | Transmit-receive loop coil | Standard |
| Peak acoustic noise (dB) | 78.7 | 114.5 |
| Noise difference | 35.8 dB lower (approx. 62x weaker sound pressure) | Reference |
| Spatial SNR | ~25 | Not reported for this study |
| Temporal SNR | 30-60 | Not reported for this study |
| Signal change (visual stim) | ~0.3% | 1-1.5% |
| Susceptibility distortions | Minimal | More pronounced |
| EEG gradient artifacts | Lower amplitude | Higher amplitude |

## 4. Motion Parameters During Awake Imaging

| Metric | Value (ZTE, this study) | Comparison (EPI, prior study) |
|---|---|---|
| Mean framewise head translation | 0.69 +/- 0.32 um | Not directly comparable |
| Mean head rotation | 0.79 +/- 0.55 deg | Not directly comparable |
| Maximum head displacement | 12.8 +/- 11.6 um | Not directly comparable |
| Maximum displacement in voxels | 0.03 +/- 0.02 voxels | Not directly comparable |
| Maximum rotation | 18.1 +/- 12.9 deg | Not directly comparable |
| Motion occurrences/min (ZTE) | 0.43 +/- 0.45 | -- |
| Motion occurrences/min (EPI, prior) | 1.0 +/- 0.20 | -- |
| Motion occurrences/min (MB-SWIFT, prior) | 0.48 +/- 0.23 | -- |

Fig 2E: Average framewise displacement across all included sessions shown with standard deviation band; motion levels are extremely low, confirming suitability of ZTE for awake rat imaging.

## 5. Stimulation Paradigm

| Parameter | Visual Stimulation | Whisker Stimulation |
|---|---|---|
| Delivery method | Bilateral optical fiber cables near eyes | Bilateral air-puff via plastic tips to whiskers |
| Block duration | 6 seconds | 6 seconds |
| Session length | 45 minutes | 45 minutes |
| States captured | Interictal baseline, ictal (during seizure), seizure-terminated-by-stim | Interictal baseline, ictal (during seizure), seizure-terminated-by-stim |

## 6. Seizure Characteristics During fMRI

| Parameter | Value |
|---|---|
| Scanning period | 45 minutes per session |
| SWD frequency | 2-5 Hz (characteristic of absence epilepsy) |
| EEG pattern | Spike-and-wave discharges |
| Seizure classification | Post-hoc from recorded TTL events and EEG |

Table 1 reports occurrences per 45-min session of each stimulation type (interictal stim, ictal stim, stim that terminated seizure) as well as seizure counts and durations during scanning.

## 7. Visual Stimulation Group -- Interictal Responses

| Brain Region | Activation Status (Interictal) | Pathway Role |
|---|---|---|
| Visual cortex (bilateral) | Strong positive activation | Primary visual processing |
| Superior colliculus | Positive activation | Subcortical visual relay |
| Lateral geniculate nucleus (thalamus) | Positive activation | Thalamic visual relay |
| Frontal cortex (prelimbic) | Positive activation | Attentional processing |
| Cingulate cortex | Positive activation | Attentional/executive processing |
| Secondary motor cortex | Positive activation | Motor planning integration |

Fig 3A (interictal panel): F-contrast maps show robust bilateral activation in visual cortex, superior colliculus, and thalamic nuclei including LGN during interictal visual stimulation.

## 8. Visual Stimulation Group -- Ictal vs. Interictal Comparison

| Brain Region | Interictal Response | Ictal Response | Difference Direction |
|---|---|---|---|
| Visual cortex | Positive BOLD | Negative / suppressed | Reduced during seizure |
| Superior colliculus | Positive BOLD | Suppressed | Reduced during seizure |
| Lateral geniculate nucleus | Positive BOLD | Suppressed | Reduced during seizure |
| Frontal cortex | Positive BOLD | Suppressed | Reduced during seizure |
| Cortical ROIs (general) | Positive HRF | Negatively polarized HRF | Inverted polarity |

Fig 3A (difference panel): The interictal-minus-ictal contrast reveals widespread significant differences across the visual pathway, confirming suppression of sensory responses during seizures.

Fig 4A: HRF comparison in visual ROIs shows positive hemodynamic responses during interictal stimulation but negatively deflected responses during ictal stimulation. The extreme beta-value analysis confirms statistically significant differences between the two states.

## 9. Whisker Stimulation Group -- Interictal Responses

| Brain Region | Activation Status (Interictal) | Pathway Role |
|---|---|---|
| Somatosensory cortex (barrel field) | Strong positive activation | Primary whisker representation |
| Ventral posteromedial thalamus (VPM) | Positive activation | Thalamic somatosensory relay |
| Frontal cortex | Positive activation | Attentional integration |

Fig 3B (interictal panel): F-contrast maps show expected somatosensory pathway activation with prominent barrel field and VPM thalamic responses during interictal whisker stimulation.

## 10. Whisker Stimulation Group -- Ictal vs. Interictal Comparison

| Brain Region | Interictal Response | Ictal Response | Difference Direction |
|---|---|---|---|
| Barrel field (somatosensory cortex) | Positive BOLD | Suppressed / negative | Reduced during seizure |
| VPM thalamus | Positive BOLD | Suppressed | Reduced during seizure |
| Frontal cortex | Positive BOLD | Suppressed | Reduced during seizure |
| Cortical ROIs (general) | Positive HRF | Negatively polarized HRF | Inverted polarity |

Fig 3B (difference panel): Interictal-minus-ictal difference maps confirm significant reductions in somatosensory pathway activation during seizures.

Fig 4B: HRF comparison in somatosensory ROIs parallels visual group findings -- positive responses in interictal state become negative during ictal state. Statistical comparison of extreme beta values confirms significant differences.

## 11. Seizure-Only Hemodynamic Analysis (No Stimulation)

| Brain Region | Seizure Response Polarity | Notes |
|---|---|---|
| Somatosensory cortex (initiation zone) | Positive / mixed | Believed seizure initiation zone in GAERS |
| Thalamus | Positive | Essential role during ictal state |
| Other cortical regions | Variable | Seizure propagation from barrel cortex |

Fig 5A: F-contrast maps for the seizure regressor (without stimulation) show widespread activation pattern associated with spike-and-wave discharges.

Fig 5B: HRFs in selected ROIs during seizures (without stimulation) show characteristic hemodynamic signature of absence seizures with region-specific polarity patterns.

## 12. Statistical Analysis Framework

| Analysis Step | Method |
|---|---|
| GLM basis functions | Gamma basis functions |
| Parameter estimation | Voxel-wise beta estimation |
| Contrast maps | F-contrast |
| Significance threshold | p < 0.05 |
| Multiple comparisons correction | Cluster-level correction |
| ROI HRF computation | Gamma basis functions multiplied by average beta value over ROI, summed |
| State comparison | Extreme beta-values over ROI, compared between interictal and ictal |
| Software for activation maps | Aedes (https://github.com/mjnissi/aedes) |

## 13. Mean-Field Simulation Results

| Simulation Parameter | Interictal (AI) State | Ictal (SWD) State |
|---|---|---|
| Dynamics type | Asynchronous Irregular (AI) | Spike-and-wave discharge (SWD) |
| Model type | AdEx (Adaptive Exponential integrate-and-fire) mean-field | Same |
| Control parameter | Adaptation current strength (lower) | Adaptation current strength (higher) |
| Response to virtual stimulation | Activity propagates broadly | Activity propagation restricted |

| Simulation Observable | Description |
|---|---|
| LFP pattern | Model captures SWD oscillatory pattern matching experimental EEG |
| Membrane potential | Alternating burst/silent periods during SWD |
| Stimulation propagation (interictal) | Stimulus-evoked activity spreads to connected regions |
| Stimulation propagation (ictal) | Stimulus-evoked activity confined, limited spatial spread |

Fig 6A-B: Mean-field model generates AI dynamics (representing interictal) and SWD dynamics (representing ictal) by modulating adaptation current strength.

Fig 6C: LFP and membrane potential from the model capture the SWD pattern observed experimentally.

Fig 6D-F (or equivalent): Simulated stimulation during interictal state shows broad activity propagation, while stimulation during ictal state shows restricted propagation, consistent with the fMRI observations of suppressed sensory responses.

## 14. Key Methodological Observations

| Observation | Detail |
|---|---|
| ZTE sensitivity advantage | ZTE-fMRI suggested to be 67% more sensitive than standard BOLD EPI due to detection of T1-relaxation rate changes from tissue oxygenation |
| ZTE contrast mechanism | Sensitive to cerebral blood flow changes (unlike T2*-weighted EPI) |
| Seizure occurrence conditions | Require calm, stress-free awake state; acoustic noise is most significant stress factor |
| Habituation protocol | Multi-week procedure based on prior published methods |
| Restraint system | 3D-printed parts compatible with Bruker rat bed, designed in 123D CAD |
| Pilot comparison | One animal compared ZTE vs. EPI; ZTE selected for main experiments |

## 15. Summary of Key Findings by Modality

| Finding | Visual Group | Whisker Group |
|---|---|---|
| Interictal activation pattern | Expected visual pathway | Expected somatosensory pathway |
| Frontal cortex involvement | Present (attention-related) | Present (attention-related) |
| Ictal response suppression | Global, significant | Global, significant |
| Cortical HRF polarity during seizure | Negative despite stimulation | Negative despite stimulation |
| Spatial extent of ictal response | Restricted vs. interictal | Restricted vs. interictal |
| Consistency with mean-field model | Good agreement | Good agreement |

## 16. Implications for Absence Epilepsy Pathophysiology

| Hypothesis | Support from Data |
|---|---|
| Sensory processing is suppressed during absence seizures | Confirmed: both visual and somatosensory responses suppressed |
| Suppression contributes to impaired consciousness | Consistent with observed negative cortical HRFs during seizures |
| Seizure dynamics restrict propagation of stimulus-driven activity | Confirmed by mean-field simulation |
| Somatosensory cortex (seizure initiation zone) remains functional during interictal periods | Confirmed by robust barrel field activation to whisker stimulation |
| Thalamic subnetworks coordinate SWD via feedforward inhibition and burst firing | Consistent with model parameters and thalamic hemodynamic patterns |

