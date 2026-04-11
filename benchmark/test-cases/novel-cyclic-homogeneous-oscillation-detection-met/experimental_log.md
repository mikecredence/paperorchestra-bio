# Experimental Log: Novel Cyclic Homogeneous Oscillation Detection Method for High Accuracy and Specific Characterization of Neural Dynamics

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- The second section reports physiological results by comparing the accuracy of CHO with that of established methods in detecting oscillations within in-vivo recordings.Synthetic resultsTo determine the specificity and sensitivity of CHO in detecting neural oscillations, we applied CHO to synthetic no
- As shown in Figure 4, we generated 5s-long 1/f signals composed of pink noise and added non-sinusoidal oscillations of different lengths (one cycle, two-and-a-half cycles, 1s-duration, and 3s-duration).
- The rightmost panel of Figure 4A shows two examples of non-sinusoidal oscillations (two-and-a-half cycles and 2s-duration) along with their power spectra.
- As can be seen in Figure 4A, longer non-sinusoidal oscillations exhibit stronger harmonic peaks.biorxiv;2023.10.04.560843v2/FIG4F4fig4Figure 4.Performance of CHO in detecting synthetic non-sinusoidal oscillations.(A) We evaluated CHO by verifying its specificity, sensitivity, and accuracy in detecti
- (B-D) CHO outperformed existing methods in detecting the fundamental frequency of non-sinusoidal oscillation (FOOOF: fitting oscillations one over f (Donoghue et al., 2020), OEvent (Neymotin et al., 2022): Oscillation event detection method, and SPRiNT (Wilson et al., 2022): Spectral Parameterizatio
- (C) However, at SNR-levels of alpha oscillations found in EEG and ECoG recordings (i.e., -7 dB and -6 dB, respectively), the sensitivity of CHO in detecting the peak frequency of non-sinusoidal oscillation is comparable to that of SPRiNT.
- (F) Similar to the results shown in (C) CHO can effectively detect the fundamental frequency and onset/offset for more than half of all oscillations at SNR-levels of alpha oscillations found in EEG and ECoG recordings.Figure 4—figure supplement 1.
- SNR Histograms of EEG and ECoG.Figure 4—figure supplement 2.
- Synthetic sinusoidal oscillations.biorxiv;2023.10.04.560843v2/FIGS41F11figs41Figure 4—figure supplement 1.SNR Histograms of EEG (A) and ECoG (B).biorxiv;2023.10.04.560843v2/FIGS42F12figs42Figure 4—figure supplement 2.Synthetic sinusoidal oscillations.Our results in Figure 4B-D demonstrate that CHO o
- For example, the average specificity of SPRiNT was below 0.3, which was significantly lower than the robust specificity of CHO across the entire range of SNR.
- Based on our physiological datasets, we found the average SNR of oscillations in EEG and ECoG to be -7 dB and -6 dB, respectively (Figure 4—figure Supplement 1).
- In this analysis, CHO outperformed the OEvent method in specificity but not sensitivity, as shown in Figure 4E-G.
- Specifically, we found performance trends similar to those in our previous simulation result (Figure 4B-D).
- Specifically, we evaluated CHO on electrocorticographic (ECoG, x1–x8, 8 subjects) and electroencephalographic (EEG, y1–y7, 7 subjects) signals recorded during the pre-stimulus period of an auditory reaction time task.
- Furthermore, we also evaluated CHO on signals recorded during resting state from cortical areas and hippocampus using ECoG (ze1–ze8, N=6) and stereo EEG (zs1–zs6, 6 subjects).Electrocorticographic (ECoG) resultsIn the auditory reaction time task, we expected to observe neural low-frequency oscillati
- As shown in Figure 5A for one representative subject, FOOOF detected the presence of alpha, and beta oscillations within temporal and motor cortex.
- We found this pattern to be consistent across subjects, as shown in Figure 5B and Figure 5—figure Supplement 1.biorxiv;2023.10.04.560843v2/FIGS51F13figs51Figure 5—figure supplement 1.ECoG results using FOOOF and CHO for all subjects.biorxiv;2023.10.04.560843v2/FIG5F5fig5Figure 5.Validation of CHO in
- An asterisk (*) indicates statistically significant differences in oscillation detection between CHO and FOOOF (Wilcoxon rank-sum test, p<0.05 after Bonferroni correction).Figure 5—figure supplement 1.
- We used FreeSurfer (Fischl, 2012) to determine the associated cerebral region for each ECoG location.
- Each subject performed approximately 400 trials of a simple auditory reaction-time task.
- We analyzed the neural oscillations during the 1.5-second-long pre-stimulus period within each trial.
- Notably, within the beta band, excluding specific regions such as precentral, pars opercularis, and caudal middle frontal areas, CHO’s beta oscillation detection rate was significantly lower than that of FOOOF (Wilcoxon rank-sum test, p < 0.05 after Bonferroni correction).
- This suggests comparable detection rates between CHO and FOOOF in premotor and Broca’s areas, while the detection of beta oscillations by FOOOF in other regions, such as the temporal area, may represent harmonics of theta or alpha, as illustrated in Figure 5A and B.
- Indeed, the EEG results mainly exhibit alpha and beta oscillations during the pre-stimulus periods of the auditory reaction time task, as shown in Figure 6.
- We found these results to be consistent across subjects (see Figure 6B, C and Figure 6—figure Supplement 1).biorxiv;2023.10.04.560843v2/FIGS61F14figs61Figure 6—figure supplement 1.Results from seven EEG subjects using the FOOOF and CHO methods.biorxiv;2023.10.04.560843v2/FIG6F6fig6Figure 6.Validatio
- In contrast, CHO detected alpha-band oscillations primarily within visual areas and detected more focal beta-band oscillations over the pre-motor area, similar to the ECoG results shown in Figure 5.
- An asterisk (*) indicates statistically significant differences in oscillation detection between CHO and FOOOF (Wilcoxon rank-sum test, p<0.05 after Bonferroni correction).
- CHO exhibited lower entropy values of alpha and beta occurrence than FOOOF across 64 channels.
- FOOOF detected alpha and beta oscillations in visual cortex than in pre-motor cortex.Figure 6—figure supplement 1.
- We used EEG electrode locations according to the 10-10 electrode system (Nuwer, 2018) and assigned each electrode to the appropriate underlying cortex (e.g., O1 and O2 for the visual cortex).
- Each subject performed 200 trials of a simple auditory reaction-time task.
- We analyzed the neural oscillations during the 1.5-second-long pre-stimulus period.
- However, CHO exhibited a greater alpha detection rate for the visual cortex than for the pre-motor cortex, as shown in Figure 6B and C.
- The entropy of CHO’s alpha oscillation occurrences (3.82) was lower than that of FOOOF (4.15), with a maximal entropy across 64 electrodes of 4.16.
- Furthermore, in the beta band, CHO’s entropy (4.05) was smaller than that of FOOOF (4.15).
- As illustrated in Figure 6C, CHO found fewer alpha oscillations in pre-motor cortex (FC2 and FC4) than in occipital cortex (O1 and O2), while FOOOF found more beta oscillations occurrences in pre-motor cortex (FC2 and FC4) than in occipital cortex.
- Based on the principle of event-related de-/synchronization (ERD/ERS, Pfurtscheller and Da Silva 1999), cortical neurons may be de-synchronized to process an auditory stimulus.
- As shown in Figure 7, CHO successfully detected offset times of 7 Hz neural oscillations.
- Of note, the detection of onset times peaks 950 ms post-stimulus, which occurs significantly later than the button press that happens 200 ms post-stimulus (Figure 7B).biorxiv;2023.10.04.560843v2/FIG7F7fig7Figure 7.Application of CHO in determining the spatiotemporal characteristics of neural oscilla
- Fundamental oscillations were centered around 7 Hz (left histogram).
- Onset and offset times during pre-stimulus period exhibited a uniform distribution, indicating that 7 Hz oscillations randomly started and stopped during this period.
- A trough in the onset and a peak in the offset of 7 Hz oscillations is visible from the histograms, indicating a general decrease of the presence of neural oscillations immediately following the auditory stimulus.
- The subjects responded with a button press within 200 ms of the auditory stimulus, on average.
- The prominent peak in the offset and onset of oscillations at 300 ms and 950 ms post-stimulus, respectively, indicates a suspension of oscillations in response to the auditory stimulus, and their reemergence after the execution of the button press behavior.Similar to the distribution of onset times,
- After stimulus onset, the distribution becomes Gaussian, with a peak of offset detections at 300 ms post-stimulus, or 200 ms post-response (i.e., the button press) (Figure 7C).In summary, this means that, on average, the detected 7 Hz oscillations de-synchronized 250 ms and synchronized 900 ms, post
- Specifically, we were interested in the frequency and duration of hippocampal oscillations, which are known to be non-sinusoidal and a hallmark of memory processing (Buzsaki, 2006; Lundqvist et al., 2016).
- Using the CHO method, we plotted a representative example of detected hippocampal fast theta bursts (Lega et al., 2012; Goyal et al., 2020), as shown in Figure 8.
- As expected, the non-sinusoidal alpha-band oscillations also resulted in harmonic oscillations in the beta band, which, while not clearly visible in the power spectrum (Figure 8B), can be clearly seen in the time-frequency analysis (Figure 8D and Figure 8E).
- In contrast to the ECoG and EEG results, the frequency of beta-band oscillations in the hippocampus exhibited a frequency close to the alpha-band (8–14 Hz).
- CHO found primarily alpha-band oscillations in the hippocampus (see Figure 8—figure Supplement 1).
- When comparing the consistency between CHO and FOOOF across hippocampal locations, CHO exhibits more specific results with less overlap between alpha and beta locations and almost no detection in the low-gamma band (30–40 Hz).
- For example, subject zs4 in Figure 8—figure Supplement 1 shows alpha and beta locations mutually supplement each other when using CHO but not when using the FOOOF method.
- However, we did not find a statistically significant difference between CHO and FOOOF due to the small number of subjects and variable electrode locations within hippocampus across the six SEEG subjects.biorxiv;2023.10.04.560843v2/FIGS81F15figs81Figure 8—figure supplement 1.All results from six SEEG
- (B) Power spectrum (blue) and 1/f trend (red) for one electrode within the anterior-medial left hippocampus (red dot in A).
- The power spectrum of a 10-second-long hippocampal signal indicates the presence of neural activity over a 1/f trend across a wide frequency band up to 30 Hz.
- (D) This detection is based on first denoising the power spectrum using 1/f fitting (principle criterion #1 of CHO), which yields initial bounding boxes that include short-cycled oscillations and harmonics.
- (E) The auto-correlation step then successfully removes all short-cycled oscillations and harmonics, with only those bounding boxes remaining that exhibit a fundamental frequency.Figure 8—figure supplement 1.
- Next, we investigated electrodes belonging to the primary auditory cortex (i.e., Brodmann areas 41 and 42), as shown in Figure 9A.
- We found that 7 and 11 Hz oscillations were the predominant neural oscillations for electrodes near the primary auditory cortex.
- The average duration of an 11 Hz oscillation was 450 ms.
- Next, our results for primary motor cortex (i.e., Brodmann area 4) showed that 7 Hz was the pre-dominant oscillation frequency in the motor cortex with 450 ms duration on average, as shown in Figure 9B.
- We found that motor cortex exhibits more beta-band oscillations (around 500 ms duration) than the auditory cortex.
- Next, Broca’s area exhibited characteristics similar to those of the motor cortex, however, with a predominant beta-band frequency of 17 Hz, which is lower than the 22 or 24 Hz oscillations found in the motor cortex (Figure 9C).
- Lastly, using SEEG electrodes, we investigated neural oscillations within the human hippocampus (Figure 9D).
- This analysis showed that 8 Hz was the predominant oscillatory frequency in the hippocampus with a 450 ms duration on average.
- During the resting state, neural alpha- and beta-band oscillations within the hippocampus were shorter than in the motor cortex (p<0.05, Wilcoxon rank sum test, N=6).biorxiv;2023.10.04.560843v2/FIG9F9fig9Figure 9.Application of CHO in determining the fundamental frequency and duration of neural osci
- (A) In primary auditory cortex (Brodmann area 41/42), the most dominant frequency and duration in the auditory cortex was 11 Hz with 450 ms duration.
- (B) The primary motor cortex’s most dominant frequency was 7 Hz with 450 ms duration, but more beta rhythms were detected with >500 ms duration than in auditory cortex.
- (D) Hippocampus primarily exhibits 8 Hz oscillations with 450 ms duration.

## Figure Descriptions

### Figure 1.
Examples of non-sinusoidal and sinusoidal neural oscillations recorded from the human auditory cortex.Detecting the presence, onset/offset, and fundamental frequency of non-sinusoidal oscillations is challenging. This is because the power spectrum of the non-sinusoidal theta-band oscillation (A) exh

### Figure 2.
Using auto-correlation to determine the fundamental frequency of non-sinusoidal and sinusoidal neural oscillations recorded from the human auditory cortex.(A) Temporal dynamics of non-sinusoidal (left) and sinusoidal (right) neural oscillation and (B) their auto-correlation. The periodicity of peaks

### Figure 3.
Procedural steps of CHO.(A) First, to identify periodic oscillations, CHO removes the underlying 1/f aperiodic noise in the time-frequency space and generates initial bounding boxes of candidate oscillations. (B) In the second step, CHO rejects bounding boxes that exhibit less than two oscillatory c

### Figure 4.
Performance of CHO in detecting synthetic non-sinusoidal oscillations.(A) We evaluated CHO by verifying its specificity, sensitivity, and accuracy in detecting the fundamental frequency of non-sinusoidal oscillatory bursts (2.5 cycles, 1–3 seconds long) convolved with 1/f noise. (B-D) CHO outperform

### Figure 4—figure supplement 1.
SNR Histograms of EEG (A) and ECoG (B).

### Figure 4—figure supplement 2.
Synthetic sinusoidal oscillations.

### Figure 5—figure supplement 1.
ECoG results using FOOOF and CHO for all subjects.

### Figure 5.
Validation of CHO in detecting oscillations in ECoG signals.(A) We applied CHO and FOOOF to determine the fundamental frequency of oscillations from ECoG signals recorded during the pre-stimulus period of an auditory reaction time task. FOOOF detected oscillations primarily in the alpha- and beta-ba

### Figure 6—figure supplement 1.
Results from seven EEG subjects using the FOOOF and CHO methods.

### Figure 6.
Validation of CHO in detecting oscillations in EEG signals.(A) We applied CHO and FOOOF to determine the fundamental frequency of oscillations from EEG signals recorded during the pre-stimulus period of an auditory reaction time task. FOOOF primarily detected alpha-band oscillations over frontal/vis

### Figure 7.
Application of CHO in determining the spatiotemporal characteristics of neural oscillations in ECoG signals during a reaction-time task.(A) We selected those cortical locations (red) from all locations (black) that exhibited a significant broadband gamma response to an auditory stimulus in a reactio

### Figure 8—figure supplement 1.
All results from six SEEG subjects using the FOOOF and CHO methods.

### Figure 8.
Application of CHO in determining the fundamental frequency and duration of hippocampal oscillations in SEEG signals during resting state.(A) We recorded hippocampal oscillations from one representative human subject implanted with SEEG electrodes within the left anterior hippocampus. (B) Power spec

### Figure 9.
Application of CHO in determining the fundamental frequency and duration of neural oscillations in auditory cortex, motor cortex, Broca’s area, and hippocampus during resting state.This figure presents the distribution of detected oscillations in a 2-dimensional frequency/duration histogram and proj

### 


## References
Total references in published paper: 64

### Key References (from published paper)
- American clinical neurophysiology society guideline 2: guidelines for standard electrode position no (, 2016)
- VERA - A Versatile Electrode Localization Framework. Zenodo (, 2022)
- An iterative search algorithm to identify oscillatory dynamics in neurophysiological time series (, 2022)
- Cross-frequency phase–phase coupling between theta and gamma oscillations in the hippocampus (, 2012)
- An electrode cap tested (, 1982)
- Periodic/Aperiodic parameterization of transient oscillations (PAPTO)–Implications for healthy agein (, 2022)
- Hilbert-and wavelet-based signal analysis: are they really different approaches? (, 2004)
- Rhythms of the Brain (, 2006)
- Neuronal oscillations in cortical networks (, 2004)
- Emerging technologies for improved deep brain stimulation (, 2019)
- Stimulating at the right time: phase-specific deep brain stimulation (, 2017)
- High gamma power is phase-locked to theta oscillations in human neocortex (, 2006)
- Human θ oscil-lations related to sensorimotor integration and spatial learning (, 2003)
- Real-time brain oscillation detection and phase-locked stimulation using autoregressive spectral est (, 2011)
- Filters: when, why, and how (not) to use them (, 2019)
- Cycle-by-cycle analysis of neural oscillations (, 2019)
- Nonsinusoidal beta oscillations reflect cortical pathophysiology in Parkinson’s disease (, 2017)
- Oscillatory phase modulates the timing of neuronal activations and resulting behavior (, 2016)
- Spontaneous travelling cortical waves gate perception in behaving primates (, 2020)
- Modulations in oscillatory activity with amplitude asymmetry can produce cognitively relevant event- (, 2010)
- Parameterizing neural power spectra into periodic and aperiodic components (, 2020)
- Methodological considerations for studying neural oscillations (, 2022)
- Lateralization of event-related beta desynchronization in the EEG during pre-cued reaction time task (, 2005)
- Understanding harmonic structures through instantaneous frequency (, 2022)
- FreeSurfer (, 2012)
- Rhythms for cognition: communication through coherence (, 2015)
- Discovering recurring patterns in electrophysiological recordings (, 2017)
- Cortical oscillations and speech processing: emerging computational principles and operations (, 2012)
- Functionally distinct high and low theta oscillations in the human hippocampus (, 2020)
- α-Oscillations in the monkey sensorimotor network influence discrimination performance by rhythmical (, 2011)

## Ground Truth Reference
- Figures: 15
- Tables: 0
- References: 64