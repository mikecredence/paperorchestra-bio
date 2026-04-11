# Idea Summary

## Working title
Cross-Species Alignment Along the Chronological Axis Reveals Evolutionary Effects on Human Brain Structural Development

## Core question
Can we conjugate brain developmental phases between humans and macaques along a chronological (temporal) axis, and does such alignment reveal evolutionary effects on human brain anatomy?

## Motivation / gap
- Prior comparative neuroscience studies have focused on spatially aligning brains between humans and nonhuman primates, revealing morphological and connectomic differences
- Both humans and macaques show clear brain anatomical development over early life, but nobody has systematically linked developmental trajectories across species along the time axis
- Existing cross-species work identifies structural differences but does not quantify whether those differences reflect functional evolution along a temporal dimension
- No individual-level index exists to quantify cross-species developmental divergence for a given participant
- Behavioral significance of any cross-species developmental gap remains unexplored

## Core contribution (bullet form)
- Developed a brain structure-based cross-species age prediction model using multimodal MRI (sMRI + dMRI) features from 370 humans (ages 8-14) and 181 macaques (ages 2-4), achieving intra-species prediction R = 0.5729 (macaque) and R = 0.6153 (human)
- Demonstrated an asymmetric cross-species prediction: the macaque-trained model predicts human ages better (R = 0.4823) than the human-trained model predicts macaque ages (R = 0.2898)
- Introduced the Brain Cross-species Age Gap (BCAP) index to quantify individual-level evolutionary divergence along the developmental timeline
- Showed BCAP correlates significantly with behavioral phenotypes: negative correlation with Visual Sensitivity Test and positive correlation with Picture Vocabulary Test
- Identified that BCAP is primarily associated with language-related white matter pathways (e.g., arcuate fasciculus) and higher-order cognitive regions
- Results are robust across different feature selection criteria (62, 117, 239 features) and across sexes

## Method in brief
The approach uses multimodal brain imaging data (structural MRI and diffusion MRI) from the Human Connectome Project-Development (370 humans, 8-14 years) and University of Wisconsin-Madison (181 rhesus macaques, 2-4 years). Brain features include gray matter volume (GMV) and white matter tract measures (fractional anisotropy FA, mean diffusivity MD, radial diffusivity RD, axial diffusivity AD). Features are selected via Pearson correlation with age (p < 0.01) across 100 iterations, yielding 62 macaque and 225 human features for the primary analysis.

Separate prediction models are trained for each species to predict chronological age from anatomical features. Intra-species prediction validates model quality, while cross-species application (e.g., applying the macaque model to human data) tests developmental correspondence. The difference between predicted and actual age in cross-species application defines the brain age gap. The Brain Cross-species Age Gap (BCAP) is then computed as the residual from this cross-species prediction, serving as an individual index of evolutionary developmental divergence.

BCAP values are correlated with behavioral phenotypes (BIS/BAS, CBCL, Visual Sensitivity, Picture Vocabulary) and with specific brain features to identify which anatomical structures drive the cross-species divergence. Additional robustness checks use different feature counts (minimum MAE criterion yielding 117 macaque and 239 human features; top 62 shared features) and sex-stratified analyses.

## Target venue
eLife
