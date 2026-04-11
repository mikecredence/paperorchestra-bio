## Working title

Biphasic V1 population dynamics underlying perceptual similarity masking revealed by voltage-sensitive dye imaging in behaving macaques

## Core question

Does the primary visual cortex (V1) contribute to similarity masking -- the phenomenon where detecting a target becomes harder as its orientation approaches that of the background -- and if so, what are the spatiotemporal dynamics of the neural signals that correlate with this behavioral effect?

## Motivation / gap

- Similarity masking (harder detection when target resembles background) is a fundamental perceptual phenomenon underlying camouflage, but its neural basis is not well understood
- Contextual modulation in V1 is well documented, but whether and how V1 population responses specifically account for orientation-dependent detection difficulty has not been directly tested during behavior
- Prior work on masking focused mainly on contrast gain control; the role of orientation-specific interactions at different spatial scales (retinotopic vs. columnar) in V1 has not been dissected
- No study has examined the temporal dynamics of V1 masking signals at both retinotopic and columnar scales simultaneously during a detection task
- The link between nonlinear normalization models and population-level masking dynamics in vivo during behavior is missing

## Core contribution (bullet form)

- Demonstrated that macaque monkeys show similarity masking behavior matching human psychophysics: detection d-prime is lowest when target and background orientations match, across five contrast combinations
- Discovered a biphasic temporal profile of V1 population responses: an initial transient phase where target responses are paradoxically enhanced by similar backgrounds, followed by a sustained phase where similar backgrounds suppress target responses consistent with behavioral masking
- Showed that columnar-scale (orientation map) signals correlate with behavioral masking earlier and more robustly than retinotopic-scale signals; integrated columnar responses were positively correlated with behavior across all contrast conditions tested
- Decomposed population responses into orientation-selective clusters (12 equally spaced preferred orientations), revealing that the sustained suppression is driven by reduced activation of target-aligned neurons while orthogonal neurons remain less affected
- Showed a simple delayed divisive normalization model qualitatively reproduces the biphasic dynamics, suggesting a gain control mechanism in V1 underlies the phenomenon

## Method in brief

Two macaque monkeys performed a target detection task while V1 population responses were measured with voltage-sensitive dye imaging (VSDI) through a chronic cranial chamber with transparent artificial dura. On each trial, a 4-degree background grating (4 cpd) was flashed at approximately 3 degrees eccentricity, with a small horizontal Gabor target (4 cpd, 0.33 degree FWHM envelope) added on 50% of trials. Background orientation varied randomly (0 to 90 degrees relative to the horizontal target). Monkeys indicated target presence with a saccade to the target location and target absence by maintaining fixation. Five combinations of target and background contrast were tested.

Neural analysis was performed at two spatial scales. At the retinotopic scale, a Gaussian template matching the target's spatial profile was applied to extract the amplitude of the target-evoked response across the V1 map. At the columnar scale, an orientation-selective template was computed from the V1 orientation map to extract the relative strength of activity in columns tuned to the target orientation versus orthogonal orientations. For finer analysis, each pixel was assigned to one of 12 orientation-selective cluster maps based on its preferred orientation, and population tuning curves were constructed from the VSD response decomposed across these clusters. Neural-behavioral correlations were computed between the orientation-dependent modulation of the template responses and the behavioral d-prime at matching orientations, tracked over time. A delayed divisive normalization model was used to test whether a simple gain control computation could account for the biphasic dynamics.

## Target venue

eLife
