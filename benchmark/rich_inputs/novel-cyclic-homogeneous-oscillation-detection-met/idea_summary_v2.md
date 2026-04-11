# Idea Summary

## Working title
Novel Cyclic Homogeneous Oscillation Detection Method for High Accuracy and Specific Characterization of Neural Dynamics

## Core question
Can we develop an oscillation detection method that accurately distinguishes the fundamental frequency of non-sinusoidal neural oscillations from their harmonics, thereby reducing false positives that plague conventional frequency-domain approaches?

## Motivation / gap
- Neural oscillations are frequently non-sinusoidal, generating harmonic peaks in the power spectrum that existing methods misidentify as independent oscillations
- Traditional detection relies on identifying peaks over 1/f noise in the frequency domain, which cannot distinguish fundamental frequencies from harmonics
- This harmonic confound significantly inflates false-positive detection rates and distorts characterization of neural dynamics
- Determining the "when" (onset/offset), "where" (brain region), and "what" (fundamental frequency) of oscillations is foundational for understanding brain function, but current methods fail on non-sinusoidal signals
- A recent review paper identified determining the fundamental frequency of non-sinusoidal oscillations as an open methodological challenge
- Existing methods (FOOOF, OEvent, SPRiNT) operate primarily in frequency or time-frequency domains and assume predominantly sinusoidal, stationary oscillations

## Core contribution (bullet form)
- Introduced three fundamental criteria for characterizing neural oscillations: (1) peaks over 1/f in time-frequency domain, (2) at least two complete cycles, (3) periodicity matching between the signal and its auto-correlation
- Demonstrated that CHO outperforms FOOOF, OEvent, and SPRiNT in specificity and accuracy on synthetic non-sinusoidal oscillatory bursts across a range of SNR levels
- At physiologically relevant SNR levels (EEG: -7 dB; ECoG: -6 dB), CHO sensitivity for detecting fundamental frequency is comparable to SPRiNT while maintaining far fewer false positives
- Validated on ECoG (8 subjects) and EEG (7 subjects) during an auditory reaction time task, detecting auditory alpha and pre-motor beta oscillations with greater spatial specificity than FOOOF
- Determined the fundamental frequency of hippocampal oscillations in 6 SEEG subjects during resting state, identifying theta as the true fundamental rather than apparent alpha/beta peaks
- Detected focal beta oscillations over pre-motor cortex (not STG) in ECoG, whereas FOOOF detected broad beta across both regions -- CHO provides more anatomically specific results

## Method in brief
CHO operates in three sequential steps. First, the method removes underlying 1/f aperiodic noise in the time-frequency domain (using spectral parameterization similar to FOOOF) and generates initial bounding boxes around candidate oscillation events where spectral peaks exceed the 1/f threshold. Second, CHO rejects any bounding boxes containing fewer than two complete oscillatory cycles, which filters out evoked/event-related potentials and spike artifacts that have spectral signatures resembling theta or alpha oscillations. Third, the auto-correlation of the raw signal within each surviving bounding box is computed to determine the true periodic frequency. Bounding boxes are rejected if the periodicity of the raw signal does not match the frequency identified in the time-frequency map. This final criterion is the key innovation: positive peaks in the auto-correlation reveal the fundamental frequency even for non-sinusoidal signals, and asymmetry in the auto-correlation peaks/troughs indicates non-sinusoidal waveform shape.

Evaluation was performed on synthetic data consisting of non-sinusoidal oscillatory bursts (2.5 cycles, 1-3 seconds long) convolved with 1/f (pink) noise at varying SNR levels. Sensitivity (true positive rate), specificity (true negative rate), and overall accuracy were computed for detecting both the peak frequency alone and the combined peak frequency plus onset/offset. The method was then validated on four physiological datasets: ECoG from 8 subjects and EEG from 7 subjects performing an auditory reaction time task (pre-stimulus analysis), ECoG resting state from 6 subjects with STG coverage, and SEEG resting state from 6 subjects with hippocampal electrode contacts.

## Target venue
eLife
