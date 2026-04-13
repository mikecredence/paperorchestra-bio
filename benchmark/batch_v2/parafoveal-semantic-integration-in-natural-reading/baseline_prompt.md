Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title
Early parafoveal semantic integration during natural reading measured with RIFT and MEG

## Core question
Can semantic information from parafoveal words be integrated with the evolving sentence context *before* the reader fixates on those words, and if so, how early does this integration begin?

## Motivation / gap
- Prior work debated whether parafoveal processing extends beyond orthographic/phonological features to semantics, especially in English
- The boundary paradigm (eye-tracking only) cannot distinguish pre-fixation integration effects from cross-saccade mismatch effects
- No direct neural measure of parafoveal semantic processing during natural reading existed
- Unknown whether semantic information is merely *extracted* from the parafovea or actively *integrated* with context
- Unknown how individual differences in parafoveal processing relate to reading speed

## Core contribution (bullet form)
- Developed a RIFT (Rapid Invisible Frequency Tagging at 60 Hz) paradigm combined with MEG and eye tracking to probe parafoveal processing during natural sentence reading
- Demonstrated significantly weaker 60 Hz tagging responses for contextually incongruent vs. congruent target words during pre-target fixations (p = 0.011, cluster-based permutation test, n = 29)
- Showed the congruency effect emerges within 100 ms of fixating the pre-target word, indicating very early semantic integration
- Found that the RIFT congruency effect correlates with individual reading speed (Spearman rho = -0.39, p = 0.037), linking parafoveal integration to reading efficiency
- RIFT source localized to left visual association cortex (Brodmann area 18, MNI [-9, -97, 3])

## Method in brief
Thirty-six native English speakers (34 after exclusion) silently read 160 one-line sentences while MEG and eye movements were co-recorded. Each sentence contained an unpredictable target noun that was either congruent or incongruent with the sentence context. Target words were flickered at 60 Hz on a 1440 Hz projector using Rapid Invisible Frequency Tagging (RIFT). Pre-target and target words were counterbalanced across participants so that the same word pairs appeared in both conditions.

MEG coherence at 60 Hz between sensors and the photodiode-measured tagging signal was computed to quantify the neural tagging response. Sensors showing significant tagging responses were identified via cluster-based permutation tests comparing pre-target (flicker) and baseline (no flicker) intervals. Time-resolved coherence analyses were performed on the pre-target fixation period to capture the dynamics of parafoveal attention allocation. Source localization used Dynamic Imaging of Coherent Sources (DICS) beamforming.

## Target venue
eLife


## Experimental Log

# Experimental Log: Parafoveal Semantic Integration in Natural Reading

## Participants and Setup

| Parameter | Value |
|-----------|-------|
| Recruited | 36 |
| Excluded | 2 (poor eye tracking / sleep) |
| Analyzed | 34 (23 females) |
| Age (mean +/- SD) | 22.5 +/- 2.8 years |
| Handedness | All right-handed |
| Compensation | 15 GBP/hour or course credits |
| With RIFT response | 29 out of 34 |

## Stimulus Design

| Parameter | Value |
|-----------|-------|
| Total sentences | 277 |
| Filler sentences | 117 |
| Experimental sentences | 160 |
| Target word pairs | 80 |
| Sentence frames per pair | 2 |
| Conditions per pair | 4 (2 congruent, 2 incongruent) |
| Pre-target word type | Adjective |
| Target word type | Noun |
| Pre-target word length | 4-8 letters |
| Target word length | 4-7 letters |
| Max sentence length | 15 words or 85 letters |
| Target position constraints | Never first 3 or last 3 words |
| Counterbalance versions | 2 (A and B) |

## Tagging and Recording Parameters

| Parameter | Value |
|-----------|-------|
| Tagging frequency | 60 Hz |
| Projector refresh rate | 1440 Hz |
| MEG system | 306-channel (Elekta/MEGIN) |
| Eye tracker | Co-registered |
| Fixation cross duration | 1.2-1.6 s |
| Gaze-contingent box fixation | 0.2 s |

## RIFT Response Sensor Identification

| Metric | Value |
|--------|-------|
| Cluster permutation p-value | < 0.01 |
| Participants with RIFT response | 29 / 34 |
| Sensors per participant (mean +/- SD) | 7.9 +/- 4.5 |
| Source location | Left visual association cortex |
| Brodmann area | 18 |
| MNI coordinates | [-9, -97, 3] mm |

## Eye Movement Results

### First Fixation Duration on Pre-Target Word

| Comparison | Statistic | Value |
|-----------|-----------|-------|
| Congruent vs Incongruent | t(33) | 0.84 |
| | p (two-sided) | 0.407 |
| | Cohen's d | 0.14 |
| Interpretation | No significant parafoveal effect in eye movement data |

### First Fixation Duration on Target Word

| Comparison | Statistic | Value |
|-----------|-----------|-------|
| Congruent vs Incongruent | t(33) | 5.99 |
| | p (two-sided) | 9.83e-7 |
| | Cohen's d | 1.03 |
| Interpretation | Strong congruity effect after fixation on target |

### Later Eye Movement Measures (Supplementary)

| Measure | Effect Direction | Significance |
|---------|-----------------|--------------|
| Total gaze duration | Longer for incongruent | Significant |
| Likelihood of refixation (pre-target) | Higher for incongruent | t(33) = 7.83, p = 5.04e-9, d = 1.34 |
| Likelihood of refixation (target) | Higher for incongruent | Significant |

## RIFT Coherence Results -- Pre-Target Interval

### Magnitude of Pre-Target Coherence

| Condition | Relative Coherence |
|-----------|-------------------|
| Congruent target | Higher |
| Incongruent target | Lower (reduced) |
| Statistical test | Cluster-based permutation |
| p-value | 0.011 |
| n | 29 |

### Onset Latency

| Condition | Onset |
|-----------|-------|
| Congruent | Earlier |
| Incongruent | Later |
| Interpretation | Delayed allocation of attention to incongruent parafoveal words |

### Time Course

| Time Window | Observation |
|-------------|-------------|
| Within first 100 ms of pre-target fixation | Congruency effect already detectable |
| Full pre-target fixation | Sustained difference |

## RIFT Coherence Results -- Target Interval

| Observation | Detail |
|-------------|--------|
| Congruent vs Incongruent | No significant difference during target fixation |
| Interpretation | Semantic integration primarily during parafoveal preview, not during direct fixation |

## RIFT Coherence by Word Position

| Word Position (relative to target N) | Coherence Pattern |
|--------------------------------------|-------------------|
| N-3 | No significant tagging |
| N-2 | Beginning of tagging response |
| N-1 (pre-target) | Peak tagging with congruency effect |
| N (target) | Tagging response present, no congruency effect |
| N+1 | Reduced tagging |

Fig 2C shows coherence at 60 Hz increases as fixation position approaches the target word, peaking at the pre-target word (N-1).

## Individual Differences Analysis

| Correlation | Statistic | Value |
|-------------|-----------|-------|
| RIFT congruency effect vs reading speed | Spearman rho | -0.39 |
| | p-value | 0.037 |
| | n | 29 |
| Reading speed measure | Words per second (congruent sentences) |
| RIFT effect measure | Coherence difference (incongruent minus congruent) during pre-target fixation |

Fig 5 shows a scatter plot where participants with larger RIFT congruency effects (more negative coherence difference for incongruent) tend to read faster.

## Behavioral Pre-Tests for Stimulus Validation

| Test | Purpose | Outcome |
|------|---------|---------|
| Cloze probability | Ensure target words are unpredictable | All targets had low constraint contexts |
| Congruity rating | Confirm congruent/incongruent categorization | Validated by independent raters |

## Word Characteristics (Table 1)

| Property | Pre-target Words | Target Words | Post-target Words |
|----------|-----------------|--------------|-------------------|
| Word type | Adjective | Noun | -- |
| Length range (letters) | 4-8 | 4-7 | -- |
| Frequency | Controlled | Counterbalanced within pairs | -- |
| Predictability | -- | Low (unpredictable) | -- |

## Key Figure Observations

- Fig 1A: Paradigm shows gaze-contingent sentence presentation with cross-fixation, box trigger, and full sentence display
- Fig 1B (left): No significant difference in pre-target first fixation durations between conditions
- Fig 1B (right): Large significant difference in target first fixation durations
- Fig 2A: Topography of RIFT sensors clusters over posterior regions
- Fig 2B: DICS source localization places the tagging response in left BA18
- Fig 2C: Position-dependent coherence profile showing progressive increase toward target
- Fig 3A: Pre-target coherence spectra show clear 60 Hz peak for both conditions, with congruent > incongruent
- Fig 3B: Time-resolved coherence shows earlier and stronger onset for congruent condition
- Fig 3C: Onset latency analysis quantifies the timing difference
- Fig 4: Target interval coherence shows no significant congruency effect
- Fig 5: Negative correlation between RIFT effect magnitude and reading speed
- Supplementary Fig 1: Regression probabilities and total gaze durations support post-fixation congruity effects

## Interpretation Notes

Two possible explanations considered for the reduced RIFT response to incongruent targets:
1. Attentional redistribution: when parafoveal semantic content cannot integrate with context, attention shifts back to currently fixated word (covert regression)
2. Internal/external attentional shift: incongruent content demands more internal processing resources, reducing external (visual/RIFT) responses

Both explanations are consistent with a model where semantic integration happens during parafoveal preview.

## Methodological Considerations

| Issue | Approach |
|-------|----------|
| Model bias | Used composite omit maps for RIFT analysis |
| Multiple comparisons | Cluster-based permutation tests |
| Confounds from word properties | Counterbalanced target pairs across sentence frames |
| Cross-saccade mismatch | RIFT measures pre-fixation processing, avoiding mismatch confound |
| Individual sensor selection | Data-driven selection per participant |

## Datasets and Baselines

| Item | Description |
|------|-------------|
| Dataset | 160 experimental sentences, 117 fillers |
| Primary measure | 60 Hz coherence during pre-target fixation |
| Baseline | Pre-sentence interval (no flicker) |
| Comparison conditions | Congruent vs incongruent target words |
| Analysis software | FieldTrip (MEG), custom MATLAB scripts |
| Statistical framework | Cluster-based permutation testing, paired t-tests |

