Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

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


## Experimental Log

# Experimental Log: Neural Correlates of Perceptual Similarity Masking in V1

## Subjects and Recording Setup

| Parameter | Value |
|-----------|-------|
| Species | Macaca mulatta (macaque monkey) |
| Number of subjects | 2 |
| Recording method | Voltage-sensitive dye imaging (VSDI) |
| Imaging access | Cranial chamber with transparent artificial dura |
| Imaging region | V1 (primary visual cortex) |
| Imaging ROI size | 8 x 8 mm |
| V2 visibility | Completely hidden in lunate sulcus based on retinotopic mapping |

## Stimulus Parameters

| Parameter | Value |
|-----------|-------|
| Background grating | 4 cpd, cosine-centered, raised-cosine-masked |
| Background size | 4 degrees |
| Background eccentricity | ~3 degrees |
| Target | Horizontal Gabor, cosine-centered |
| Target spatial frequency | 4 cpd |
| Target envelope | 0.33 degree FWHM |
| Target orientation | Horizontal (fixed) |
| Background orientation range | 0 to 90 degrees (relative to target) |
| Orientation randomization | Between trials |
| Target presence | 50% of trials |
| Response for target present | Saccade to target location |
| Response for target absent | Maintain fixation |

## Contrast Conditions Tested

| Condition Label | Target Contrast | Background Contrast |
|-----------------|----------------|---------------------|
| T12 Bg7 | 12% | 7% |
| T24 Bg12 | 24% | 12% |
| T12 Bg12 | 12% | 12% |
| T24 Bg24 | 24% | 24% |
| T06 Bg7 | 6% | 7% |

## Experiment Summary (Table 1)

| Metric | Description |
|--------|-------------|
| Total experiment counts | Multiple experiments per contrast condition per monkey |
| Trial counts | Included in analysis for Figures 2, 4, 5, 7, and supplements |
| Background orientations pooled | Clockwise and anticlockwise orientations with same disparity from target were pooled |

## Behavioral Results (Fig 2)

### Detection Sensitivity (d-prime) Across Conditions

| Condition | Background at 0 deg (matched) | Background at 90 deg (orthogonal) | Uniform Background (no grating) | Masking Trend |
|-----------|-------------------------------|-----------------------------------|--------------------------------|---------------|
| T12 Bg7 | Lowest d' | Higher d' | Highest d' (baseline) | Gaussian-shaped masking |
| T24 Bg12 | Lowest d' | Higher d' | Highest d' (baseline) | Gaussian-shaped masking |
| T12 Bg12 | Lowest d' | Higher d' | Highest d' (baseline) | Gaussian-shaped masking |
| T24 Bg24 | Lowest d' | Higher d' | Highest d' (baseline) | Gaussian-shaped masking |
| T06 Bg7 | Lowest d' | Higher d' | Highest d' (baseline) | Gaussian-shaped masking |

- Fig 2A: Detection performance plotted as d-prime vs. background orientation for all five contrast combinations
- Performance fitted with inverted Gaussian function at each contrast combination
- At all five conditions, d' was lowest when background matched target orientation (0 degrees)
- General performance reduction from uniform background to any grating background
- Fig 2B: Relationship between d' and optimal percent correct performance
- Macaque behavioral data confirm similarity masking effect matching human psychophysics

### Reaction Time Results (Fig 2C)

| Observation | Detail |
|-------------|--------|
| Metric | Reaction time from stimulus onset to saccade initiation (Hit trials) |
| Uniform background | Shown as dotted lines |
| Grating backgrounds | Shown as solid lines per orientation |
| Dependency on orientation | Complex, in some cases non-monotonic |
| Error bars | Standard error of the mean |

- Reaction times showed complex dependency on target-background orientation similarity
- Some conditions showed non-monotonic patterns

## Neural Analysis: Retinotopic Scale (Fig 4)

### VSD Response and Decoder (Fig 3)

| Component | Description |
|-----------|-------------|
| Retinotopic template | Gaussian spatial profile matched to target location |
| Doubly-whitened decoding | Whitened for noise and target-absent baseline |
| Template extraction | Amplitude of target-evoked response at retinotopic location |
| Spatial scale | Large-scale retinotopic map |

### Retinotopic Template Dynamics (Fig 4)

| Phase | Time Window (Approx.) | Response to Similar BG | Response to Orthogonal BG | Behavioral Correlation |
|-------|----------------------|------------------------|---------------------------|----------------------|
| Initial transient | Early (~50-100 ms post-stimulus) | Enhanced (paradoxically stronger) | Weaker | Anti-correlated with behavior |
| Sustained phase | Later (~100-250 ms post-stimulus) | Suppressed (weaker signal) | Stronger signal | Positively correlated with behavior |

- Fig 4A (T12 Bg7): Background-only response time courses grouped by orientation
- Fig 4B (T12 Bg7): Target+background response shows biphasic dynamics
- Fig 4D: Neural sensitivity computed from template responses
- Fig 4E: Correlation between neural and behavioral masking effects over time, showing sign reversal
- Fig 4F: Behavioral d' for reference
- Fig 4G-L: Same format for T24 Bg12 condition, showing similar biphasic pattern

### Retinotopic Integrated Response vs. Behavior

| Contrast Condition | Integrated Response Correlation with Behavior |
|-------------------|----------------------------------------------|
| T12 Bg7 | Uncorrelated or anti-correlated |
| T24 Bg12 | Uncorrelated or anti-correlated |
| Other conditions | Variable (see Fig 4 - supplement 1D) |

- Temporally integrated retinotopic responses were often uncorrelated or anti-correlated with behavioral performance
- Suggests retinotopic scale alone does not fully explain behavioral masking

## Neural Analysis: Columnar Scale (Fig 5)

### Columnar Template

| Component | Description |
|-----------|-------------|
| Orientation map | Obtained per experiment from VSDI |
| Template type | Orientation-selective: extracts relative strength of target-tuned vs. orthogonal-tuned activity |
| Positive response | Stronger activation of neurons tuned to target (0 degrees) |
| Negative response | Stronger activation of neurons tuned orthogonal to target |

### Columnar Template Dynamics (Fig 5)

| Phase | Time Window (Approx.) | Response to Similar BG | Response to Orthogonal BG | Behavioral Correlation |
|-------|----------------------|------------------------|---------------------------|----------------------|
| Initial transient | Early (~50-80 ms) | Enhanced (paradoxical) | Weaker | Anti-correlated with behavior |
| Sustained phase | Later (~80-200+ ms) | Suppressed | Stronger | Positively correlated with behavior |

- Biphasic dynamics were more pronounced at the columnar scale than at the retinotopic scale
- Fig 5A-F: T12 Bg7 condition at columnar scale
- Fig 5G-L: T24 Bg12 condition at columnar scale
- Fig 5E, K: Positive correlation between neural and behavioral masking occurred earlier at columnar scale than retinotopic scale
- The sign reversal from anti-correlation to positive correlation happened sooner for columnar signals

### Columnar Integrated Response vs. Behavior

| Contrast Condition | Integrated Columnar Response Correlation with Behavior |
|-------------------|-------------------------------------------------------|
| T12 Bg7 | Positively correlated |
| T24 Bg12 | Positively correlated |
| All other conditions | Positively correlated (see Fig 5 - supplement 1D) |

- Integrated columnar responses were positively correlated with behavior across ALL target and background contrast conditions
- This is in contrast to the retinotopic scale results, which were inconsistent
- Suggests behavioral performance is dominated by columnar-scale V1 signals in the sustained phase

## Comparison: Retinotopic vs. Columnar Scale

| Feature | Retinotopic Scale | Columnar Scale |
|---------|-------------------|----------------|
| Biphasic dynamics | Present | Present (more pronounced) |
| Positive correlation onset | Later | Earlier |
| Robustness across contrasts | Variable | Consistent across all conditions |
| Integrated response-behavior correlation | Often uncorrelated/anti-correlated | Positively correlated for all conditions |
| Interpretation | Broad spatial target detection signal | Fine-grained orientation-specific competition |

## Orientation-Selective Population Analysis (Fig 6)

### Orientation Cluster Decomposition

| Parameter | Value |
|-----------|-------|
| Number of orientation clusters | 12 (equally spaced) |
| Cluster assignment | Based on preferred orientation per pixel from orientation map |
| Analysis window | Windowed to retinotopic profile of target |

### Population Tuning Curve Observations (Fig 6)

| Phase | Tuning Curve Shape | Target-Aligned Neurons | Orthogonal Neurons |
|-------|-------------------|----------------------|-------------------|
| Initial transient | Peak at background orientation | Enhanced when BG matches target | Less affected |
| Sustained phase | Peak shifted/reduced at background orientation | Suppressed when BG matches target | Relatively maintained |

- Fig 6A: Orientation map windowed to target retinotopic profile
- Fig 6B: Pixels assigned to 12 orientation-selective cluster maps
- Fig 6C: Orientation-selective decomposition of VSD response
- Population tuning curve peaks at the presented grating orientation initially
- During sustained phase, suppression of target-aligned neurons drives the masking signal

## Correct Trials Analysis (Fig 4 - supplement 2)

| Analysis | Result |
|----------|--------|
| Correct trials only (hits + correct rejections) | Biphasic dynamics preserved |
| Comparison to all-trials analysis | Similar temporal pattern |
| Implication | Decision/attention-related top-down signals unlikely to be the primary driver |

- Re-examining results while excluding error trials confirmed that biphasic dynamics hold for the subset of correct trials
- This reduces the likelihood that the observed dynamics reflect decision or attention-related top-down modulation

## Normalization Model (Fig 7)

### Model Description

| Component | Description |
|-----------|-------------|
| Model type | Delayed divisive normalization |
| Normalization pool | Delayed relative to excitatory drive |
| Key feature | Normalization signal builds up over time, initially absent |
| Prediction | Early response dominated by excitatory drive (similarity enhances), late response dominated by normalization (similarity suppresses) |

### Model Predictions vs. Data

| Temporal Phase | Model Prediction | Data Match |
|---------------|-----------------|------------|
| Early transient | Similar backgrounds enhance response (normalization not yet engaged) | Yes - paradoxical enhancement observed |
| Late sustained | Similar backgrounds suppress response (normalization fully engaged) | Yes - suppression consistent with behavioral masking |
| Sign reversal timing | Depends on normalization delay | Qualitatively matches observed reversal |

- The delayed divisive normalization model qualitatively accounts for the biphasic dynamics
- The delay in the normalization signal explains why similar backgrounds initially enhance rather than suppress target responses
- Once normalization fully engages, the suppressive effect of similar backgrounds emerges

## Supplementary Results

### Retinotopic Template Dynamics - All Contrast Conditions (Fig 4 - supplement 1)

| Condition | Biphasic Pattern | Correlation with Behavior (Integrated) |
|-----------|-----------------|---------------------------------------|
| T12 Bg7 | Present | Variable |
| T24 Bg12 | Present | Variable |
| T12 Bg12 | Present | Variable |
| T24 Bg24 | Present | Variable |
| T06 Bg7 | Present | Variable |

### Columnar Template Dynamics - All Contrast Conditions (Fig 5 - supplement 1)

| Condition | Biphasic Pattern | Correlation with Behavior (Integrated) |
|-----------|-----------------|---------------------------------------|
| T12 Bg7 | Present (pronounced) | Positive |
| T24 Bg12 | Present (pronounced) | Positive |
| T12 Bg12 | Present (pronounced) | Positive |
| T24 Bg24 | Present (pronounced) | Positive |
| T06 Bg7 | Present (pronounced) | Positive |

### Retinotopy Mapping (Fig 3 - supplement 1)

| Feature | Description |
|---------|-------------|
| Mapping stimulus | Special retinotopic scanning stimuli |
| Contour lines | Polar angles relative to horizontal meridian |
| V1-V2 border | Estimated at 270 degrees polar angle |
| Target placement | Confirmed within V1 based on retinotopic map |

## Key Metrics and Definitions

| Metric | Definition |
|--------|-----------|
| d-prime (d') | Signal detection measure: z(hit rate) - z(false alarm rate) |
| Hit | Correctly reporting target present |
| False alarm | Reporting target present when absent |
| Retinotopic template | Gaussian spatial template at target location |
| Columnar template | Orientation-selective template from orientation map |
| Neural sensitivity | Template response amplitude as function of background orientation |
| Behavioral masking | d' reduction as function of orientation similarity |
| Neural-behavioral correlation | Correlation between neural sensitivity and d' across orientations |

## Datasets and Baselines

| Dataset | Description |
|---------|-------------|
| Behavioral data | Pooled within each monkey across experiments per contrast condition |
| Neural data (VSDI) | Time-resolved population responses from V1 |
| Baseline (behavioral) | Performance on uniform gray background (no grating) |
| Baseline (neural) | Target-absent trial responses |
| Orientation pooling | Clockwise and anticlockwise same-disparity orientations combined |

## Reference Count

- Total references cited: 49
- Key references for contextual modulation: Angelucci et al. 2017, Cavanaugh et al. 2002
- Key references for normalization: Carandini and Heeger 2012, Schwartz and Simoncelli 2001
- Key references for similarity masking psychophysics: Foley 1994, Sebastian et al. 2017

