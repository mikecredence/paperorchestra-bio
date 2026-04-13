Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

# Idea Summary

## Working title
Modulation of Alpha Oscillations by Attention Is Predicted by Hemispheric Asymmetry of Subcortical Regions

## Core question
Do volumetric hemispheric asymmetries in subcortical structures (thalamus, basal ganglia nuclei) predict the degree of hemispheric lateralization in posterior alpha-band oscillation modulation during spatial attention, and does this relationship vary with perceptual load?

## Motivation / gap
- Extensive work on cortical contributions to spatial attention (dorsal attention network, frontal eye fields, intraparietal sulcus), but subcortical contributions are poorly understood
- MEG/EEG cannot reliably detect deep-source activity from thalamus and basal ganglia due to low SNR, leaving a methodological gap
- Animal studies show pulvinar and basal ganglia involvement in attention and alpha regulation, but human evidence is scarce
- No prior work has linked structural hemispheric asymmetry of subcortical nuclei to functional alpha lateralization in humans
- The relationship between perceptual load/distractor salience and subcortical engagement during attention is unknown
- Potential clinical relevance: structural atrophy in subcortical regions is linked to neurological disorders (Parkinson's, Alzheimer's, Huntington's) and could manifest as oscillatory biomarkers

## Core contribution (bullet form)
- Demonstrated that lateralization volume of globus pallidus, caudate nucleus, and thalamus significantly predicts attention-related hemispheric lateralization of alpha power (GLM p = 0.0007)
- Showed that different subcortical structures dominate under different load conditions: thalamus predicts alpha modulation in low-demand conditions, globus pallidus at intermediate load/salience, and caudate nucleus under the most demanding condition (high load + high salience distractor)
- Used a novel indirect approach combining structural MRI volumetrics with MEG-measured alpha power to bypass the limitation of directly measuring subcortical oscillatory activity
- Found that caudate nucleus is right-lateralized (p = 0.021) while putamen, nucleus accumbens, and globus pallidus showed no significant lateralization; thalamus trended toward left lateralization
- Validated results across a 2x2 factorial design crossing target perceptual load (high/low) with distractor salience (high/low) in 33 participants

## Method in brief
The study re-analyzed a previously collected dataset from 33 right-handed healthy volunteers (25 female, mean age 24 +/- 5.7 years) who performed a cued spatial attention change-detection task while MEG was recorded. Participants fixated centrally while face stimuli appeared in both hemifields; a directional cue indicated the target side. After a variable delay (1000-2000 ms), eye-gaze of each face shifted and participants reported the target gaze direction. A 2x2 factorial manipulation crossed target load (clear vs. noisy face) with distractor salience (clear vs. noisy distractor), producing four conditions.

Alpha power modulation was quantified in the -850 to 0 ms pre-target interval using a modulation index MI(alpha) reflecting relative power difference between attend-left and attend-right trials. Five symmetric sensor clusters per hemisphere showing strongest modulation were selected as ROIs. The hemispheric lateralization modulation HLM(alpha) was computed to capture individual differences in how strongly alpha power in the left hemisphere was modulated relative to the right. Subcortical volumes (thalamus, caudate, putamen, globus pallidus, nucleus accumbens) were extracted from structural MRIs using FreeSurfer, and lateralization volume (LV) was computed as (left - right) / (left + right).

A generalized linear model tested whether subcortical LV values predicted HLM(alpha). Model selection used AIC and BIC across all possible regressor combinations. The best model included thalamus, caudate nucleus, and globus pallidus as regressors. A multivariate regression further examined how these structures predicted alpha lateralization separately in each of the four load/salience conditions. Bayes factors were computed for correlations between subcortical structures and both HLM of rapid invisible frequency tagging (RIFT) signals and behavioral asymmetry.

## Target venue
eLife


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the subcortical asymmetry and alpha oscillation modulation study.

---

## Datasets and Participant Information

| Parameter | Value |
|-----------|-------|
| Total participants recruited | 35 |
| Excluded (consent / MRI quality) | 2 |
| Final sample | 33 |
| Sex (female / male) | 25 / 8 |
| Mean age (years +/- SD) | 24 +/- 5.7 |
| Handedness | All right-handed |
| Vision | Normal or corrected-to-normal |
| Payment | 15 GBP per hour |
| Ethics approval | STEM committee, University of Birmingham |

---

## Experimental Design Parameters

| Parameter | Value |
|-----------|-------|
| Number of blocks | 2 |
| Trials per block | 256 |
| Total trials | 512 |
| Session duration | ~45 minutes |
| Fixation duration | 1000 ms |
| Face stimulus duration | 1000 ms |
| Cue duration | 350 ms |
| Delay interval | 1000-2000 ms (variable) |
| Gaze shift duration | 150 ms |
| Response interval | 1000 ms |
| Stimulus eccentricity | 7 degrees from fixation |
| Stimulus diameter | 8 degrees visual angle |
| Noise mask pixel swap | 50% of stimulus pixels |
| Number of face identities | 8 |

---

## Condition Design (2x2 Factorial)

| Condition | Target Load | Distractor Salience | Target Appearance | Distractor Appearance |
|-----------|------------|---------------------|-------------------|----------------------|
| 1 | Low | Low | Clear face | Noisy face |
| 2 | High | Low | Noisy face | Noisy face |
| 3 | Low | High | Clear face | Clear face |
| 4 | High | High | Noisy face | Clear face |

---

## MEG Acquisition Parameters

| Parameter | Value |
|-----------|-------|
| System | 306-channel Elekta/MEGIN Neuromag |
| Sensor types | 204 planar gradiometers, 102 magnetometers |
| Sampling rate | 1000 Hz |
| Online bandpass filter | 0.1 - 330 Hz |
| Head position indicator (HPI) coils | 5 |
| Digitization | Polhemus Isotrak system |
| Analysis time window | -850 to 0 ms pre-target |
| Frequency band of interest | Alpha (8-12 Hz implied) |
| ROI sensors per hemisphere | 5 |
| Total ROI sensors | 10 |

---

## Structural MRI and Volumetric Analysis

| Parameter | Value |
|-----------|-------|
| MRI scanner | 3T (details from prior study) |
| Segmentation software | FreeSurfer |
| Subcortical structures measured | 5 (bilateral) |
| Structures | Thalamus, caudate nucleus, putamen, globus pallidus, nucleus accumbens |
| Lateralization volume formula | LV = (left - right) / (left + right) |

---

## Subcortical Volume Lateralization Results

| Structure | Lateralization Pattern | p-value | Significant? |
|-----------|----------------------|---------|-------------|
| Caudate nucleus | Right lateralized | 0.021 | Yes |
| Putamen | No significant lateralization | > 0.05 | No |
| Nucleus accumbens | No significant lateralization | > 0.05 | No |
| Globus pallidus | No significant lateralization | > 0.05 | No |
| Thalamus | Trend toward left lateralization | > 0.05 | No |

Fig 3B shows histograms of lateralization volume distributions for all five subcortical structures. Only the caudate nucleus distribution is shifted significantly from zero.

---

## Alpha Power Modulation Observations

Fig 2A shows time-frequency representations demonstrating power decrease contralateral to the cued hemifield and relative increase ipsilateral to it, consistent with standard spatial attention effects.

Fig 2B shows topographical distribution of MI(alpha) reflecting the relative difference between attend-right vs. attend-left trials. The strongest modulation is over posterior sensors.

Fig 2C shows MI(alpha) averaged over left and right hemisphere ROI sensors. The absolute modulation index increases gradually during the delay interval until target onset.

Fig 3A shows the distribution of HLM(alpha) across participants. No hemispheric bias was observed at the group level (p = 0.39), indicating substantial individual variability without systematic lateralization.

---

## GLM Model Selection: AIC and BIC Comparison

| Model (Regressors) | AIC | BIC | Selected? |
|---------------------|-----|-----|-----------|
| Thalamus only | Higher | Higher | No |
| Caudate only | Higher | Higher | No |
| Globus pallidus only | Higher | Higher | No |
| Putamen only | Higher | Higher | No |
| Nucleus accumbens only | Higher | Higher | No |
| Thalamus + Caudate | Lower | Lower | No |
| Thalamus + Globus pallidus | Lower | Lower | No |
| Caudate + Globus pallidus | Lower | Lower | No |
| Thalamus + Caudate + Globus pallidus | Lowest | Lowest | Yes (marked green in Table 1) |
| All 5 structures | Higher than best | Higher than best | No |

Table 1 and Table 2 in the paper enumerate all possible regressor combinations. The three-regressor model (thalamus, caudate nucleus, globus pallidus) had the lowest AIC value and was therefore selected as the best model.

---

## Best GLM Model Results (Overall, All Conditions Pooled)

| Metric | Value |
|--------|-------|
| Model regressors | Thalamus LV, Caudate LV, Globus pallidus LV |
| Model significance (vs. null) | p = 0.0007 |
| Dependent variable | HLM(alpha) |

Fig 4A displays the beta coefficients for the three-regressor model with standard error bars. Each of the three subcortical structures shows a statistically significant contribution.

---

## Beta Coefficients in Pooled Model (Fig 4A)

| Structure | Beta Estimate | Direction | Significance |
|-----------|--------------|-----------|-------------|
| Thalamus | Positive | Positive LV predicts positive HLM(alpha) | p < 0.05 |
| Caudate nucleus | Positive | Positive LV predicts positive HLM(alpha) | p < 0.05 |
| Globus pallidus | Positive | Positive LV predicts positive HLM(alpha) | p < 0.05 |

Fig 4B-D show scatter plots of individual subcortical structure lateralization volumes against HLM(alpha). Each structure shows a positive correlation, indicating that larger left-relative-to-right volume is associated with stronger left-hemisphere alpha modulation.

---

## Multivariate Regression by Load Condition (Fig 5)

| Condition | Thalamus Beta | Caudate Beta | Globus Pallidus Beta | Model p-value |
|-----------|--------------|-------------|---------------------|---------------|
| 1: Low load, Low salience | Significant (positive) | Not significant | Not significant | Part of overall model p = 0.001 |
| 2: High load, Low salience | Not significant | Not significant | Significant (positive) | Part of overall model p = 0.001 |
| 3: Low load, High salience | Not significant | Not significant | Significant (positive) | Part of overall model p = 0.001 |
| 4: High load, High salience | Not significant | Significant (positive) | Not significant | Part of overall model p = 0.001 |

Overall multivariate regression model significance: p = 0.001 (comparison with null model).

Fig 5 shows the beta coefficients with SEM error bars across all four conditions. The key finding is the dissociation: thalamus dominates the easy condition (condition 1), globus pallidus dominates intermediate conditions (conditions 2 and 3), and caudate dominates the most demanding condition (condition 4).

---

## Summary of Subcortical Contributions by Condition

| Task Demand Level | Dominant Predictor | Condition Description |
|-------------------|-------------------|----------------------|
| Lowest | Thalamus | Clear target, noisy distractor |
| Intermediate (high load OR high salience) | Globus pallidus | Noisy target + noisy distractor OR clear target + clear distractor |
| Highest | Caudate nucleus | Noisy target, clear distractor |

---

## Supplementary Analysis: RIFT and Behavioral Asymmetry (Supp Fig 1)

| Structure | Correlation with HLM(RIFT) (Bayes Factor) | Correlation with Behavioral Asymmetry (Bayes Factor) |
|-----------|------------------------------------------|-----------------------------------------------------|
| Thalamus | Reported in Table 3 | Reported in Table 3 |
| Caudate nucleus | Reported in Table 3 | Reported in Table 3 |
| Globus pallidus | Reported in Table 3 | Reported in Table 3 |
| Putamen | Reported in Table 3 | Reported in Table 3 |
| Nucleus accumbens | Reported in Table 3 | Reported in Table 3 |

Supplementary Figure 1A and 1E display beta coefficients for GLMs predicting HLM(RIFT) and behavioral asymmetry, respectively. The same three-regressor model was applied. Bayes factors in Table 3 compare the likelihood of each correlation under the alternative vs. null hypothesis.

---

## Behavioral Performance Observations

- Participants correctly detected gaze-shift direction in the cued face across all four conditions
- Performance was expected to vary across load/salience conditions, with higher load reducing accuracy and higher distractor salience increasing interference
- Behavioral data were used in conjunction with the HLM(alpha) measure but the primary analyses focused on the neural-structural relationship

---

## Key Statistical Methods

| Method | Application |
|--------|-------------|
| Generalized linear model (GLM) | Predict HLM(alpha) from subcortical LV values |
| AIC model selection | Choose optimal subset of subcortical regressors |
| BIC model selection | Cross-validate AIC-based selection |
| Multivariate regression | Predict HLM(alpha) separately per load condition |
| Pearson correlation | Bivariate relationships between LV and HLM(alpha) |
| Bayes factors | Evaluate evidence for correlations with RIFT and behavior |
| t-test | Assess group-level lateralization of volumes and HLM(alpha) |
| Time-frequency analysis | Compute alpha power in pre-target window |
| FreeSurfer segmentation | Extract bilateral subcortical volumes from MRI |

---

## Figure Summary

| Figure | Key Observation |
|--------|----------------|
| Fig 1A | Schematic of trial sequence: fixation, bilateral faces, directional cue, delay, gaze shift, response |
| Fig 1B | Examples of four stimulus conditions showing clear/noisy combinations |
| Fig 1C | Condition label table for the 2x2 design |
| Fig 2A | TFR plots confirm contralateral alpha decrease and ipsilateral increase |
| Fig 2B | Topographical MI(alpha) map with 10 selected ROI sensors |
| Fig 2C | MI(alpha) time course shows gradual increase in absolute modulation until target onset |
| Fig 3A | HLM(alpha) distribution shows no group hemispheric bias (p = 0.39) |
| Fig 3B | Subcortical volume lateralization histograms; caudate right-lateralized (p = 0.021) |
| Fig 4A | Three-regressor GLM beta coefficients all significant |
| Fig 4B-D | Individual scatter plots of LV vs HLM(alpha) for thalamus, caudate, globus pallidus |
| Fig 5 | Condition-specific beta coefficients reveal dissociation across load levels |
| Supp Fig 1 | GLM results for RIFT and behavioral asymmetry measures |

---

## Reference Count and Scope

| Parameter | Value |
|-----------|-------|
| Total references cited | 71 |
| Primary recording modality | MEG (306-channel) |
| Structural imaging modality | MRI (3T) |
| Analysis software (MEG) | MATLAB-based (implied) |
| Segmentation software | FreeSurfer |
| Experimental software | Psychophysics Toolbox 3.0.11 on MATLAB |
| Operating system | Windows 10 |
| Response device | NAtA technologies (Coquitlam, BC) |

