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
