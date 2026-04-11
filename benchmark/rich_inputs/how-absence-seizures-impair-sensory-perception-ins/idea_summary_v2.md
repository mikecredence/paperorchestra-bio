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
