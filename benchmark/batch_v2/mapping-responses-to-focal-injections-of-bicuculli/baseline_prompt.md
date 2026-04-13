Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

# Idea Summary: Rostro-caudal mapping of the expiratory oscillator in the lateral parafacial region

## Working title
Mapping the core site for active expiration generation along the rostro-caudal axis of the lateral parafacial region using focal bicuculline injections

## Core question
Where along the rostro-caudal axis of the lateral parafacial region (pFL) does GABAergic disinhibition produce the strongest and most sustained active expiration, and can multivariate respiratory analysis pinpoint the core site of the expiratory oscillator?

## Motivation / gap
- The expiratory oscillator in the ventral medulla lacks a definitive anatomical marker and is silent at rest, making it difficult to localize precisely
- Prior pharmacological and optogenetic studies targeted locations near the caudal tip of the facial nucleus (VIIc), spanning roughly -0.2 to +0.5 mm from VIIc
- Chemogenetic inhibition at VIIc only partially suppressed expiratory output -- abdominal recruitment still occurred during sleep, suggesting the core may lie elsewhere
- Similarly, chemogenetic inhibition at +0.5 mm reduced but did not eliminate bicuculline/strychnine-induced ABD signals
- No systematic study has quantified respiratory responses across the full rostro-caudal extent of the pFL to identify which sub-region drives the most potent active expiration
- A multivariate approach to characterizing the respiratory cycle (rather than single-variable comparisons) could better discriminate between injection sites

## Core contribution (bullet form)
- Bicuculline injections at five rostro-caudal locations (-0.2 to +0.8 mm from VIIc) all recruited ABD activity, but response robustness varied systematically along the axis
- The most rostral pFL sites (+0.6 and +0.8 mm from VIIc) produced the strongest and longest-lasting changes in tidal volume (29% increase at +0.6 mm), minute ventilation (42% increase at +0.6 mm), and VE/VO2 ratio (73-82% increase)
- ABD response duration was approximately 17 min at rostral sites versus only 2.4 min at the most caudal site (-0.2 mm)
- The +0.6 mm location initiated responses fastest (before the second injection) and was the only site showing a post-inspiratory ABD peak (5/6 rats)
- Multivariate trajectory analysis of the respiratory cycle (airflow, DIA EMG, ABD EMG) differentiated injection sites and identified the rostral pFL as the core region for active expiration generation
- cFos analysis confirmed bicuculline activated cells locally (~300 um spread) without activating PHOX2B+ RTN neurons above baseline

## Method in brief
Adult male Sprague-Dawley rats (n=35, ~340 g) were anesthetized with urethane and instrumented with tracheal cannulae for airflow measurement, EMG electrodes in oblique abdominal and diaphragm muscles, and femoral vein cannulae for drug delivery. Supplemental O2 (30%) was provided and end-tidal CO2 was monitored. Vagotomy was performed bilaterally. Bicuculline methochloride (200 uM in HEPES, 200 nL per side) or HEPES vehicle was pressure-injected bilaterally into the pFL at coordinates spanning -0.2 to +0.8 mm from VIIc. Injection sites were confirmed with fluorobeads and immunohistochemistry for cFos, PHOX2B, ChAT, and TH.

Respiratory responses were quantified by computing mean respiratory cycles from airflow, integrated DIA EMG, and integrated ABD EMG signals at 2-minute time bins. Normalized area under each signal was calculated for three respiratory phases (late-E, inspiratory, and post-I). Standard respiratory variables (respiratory rate, tidal volume, minute ventilation, O2 consumption, VE/VO2) were measured over time. A multivariate trajectory analysis projected the three-signal mean cycle into 3D space and measured deviations from baseline trajectories using Procrustes-like distance metrics, enabling simultaneous assessment of all respiratory signals across the full breathing cycle.

Statistical comparisons used one-way ANOVA with Tukey or Bonferroni post-hoc tests, repeated-measures ANOVA, Kruskal-Wallis with Dunn post-hoc tests, and Wilcoxon rank-sum tests. Effect sizes were reported as eta-squared values.

## Target venue
eLife


## Experimental Log

# Experimental Log: Rostro-caudal mapping of pFL active expiration responses

> Lab notebook and data compilation for bicuculline injection mapping study

## Experimental Design

### Subjects and Groups

| Parameter | Value |
|-----------|-------|
| Species/Strain | Sprague-Dawley rats, adult male |
| Total animals | 35 |
| Mean weight (g) | 340.4 +/- 13.2 |
| Anesthesia induction | 5% isoflurane |
| Anesthesia maintenance | Urethane 1.5-1.7 g/kg IV |
| Supplemental O2 | 30% |
| Body temperature | 37 +/- 1 C |
| Vagotomy | Bilateral, mid-cervical, 2 mm resection |

### Injection Group Allocation

| Group (mm from VIIc) | n (bicuculline) | n (CTRL/HEPES) |
|-----------------------|-----------------|----------------|
| -0.2 mm | 5 | -- |
| +0.1 mm | 7 | -- |
| +0.4 mm | 5 | -- |
| +0.6 mm | 6 | -- |
| +0.8 mm | 5 | -- |
| CTRL (HEPES) | -- | 7 |
| **Total** | **28** | **7** |

### Injection Parameters

| Parameter | Value |
|-----------|-------|
| Drug | Bicuculline methochloride (200 uM in HEPES) |
| Vehicle | HEPES buffer with fluorobeads |
| Injection volume | 200 nL per side (bilateral) |
| Injection rate | 100 nL/min |
| Pipette tip diameter | 30 um |
| Number of injections | 2 per experiment (separated by interval) |
| Stereotaxic setup | Bregma 5 mm below lambda |

---

## Histological Analysis

### cFos Cell Counting Results

| Group | Peak cFos+ cells/hemisection | cFos+/PHOX2B+ cells/hemisection |
|-------|------------------------------|--------------------------------|
| CTRL (HEPES) | 44.7 +/- 4.0 | 2.3 +/- 1.0 |
| -0.2 mm | 89.7 | 2.4 +/- 0.4 (pooled bicuculline) |
| +0.1 mm | 123.1 | 2.4 +/- 0.4 (pooled bicuculline) |
| +0.4 mm | 110.2 | 2.4 +/- 0.4 (pooled bicuculline) |
| +0.6 mm | 98.3 | 2.4 +/- 0.4 (pooled bicuculline) |
| +0.8 mm | 101.2 | 2.4 +/- 0.4 (pooled bicuculline) |
| Bicuculline mean | 104.5 +/- 5.1 | 2.4 +/- 0.4 |

Key observations:
- cFos+ cell counts dropped to 44.8 +/- 1.2 per section beyond injection boundaries for all bicuculline groups
- Fluorobead spread was approximately 300 um from core of injection
- No overlap between injection sites and PHOX2B+ cells in the RTN
- No overlap between injection sites and TH+ cells in C1 or A5 regions
- cFos+/PHOX2B+ double-labeled cells did not differ between CTRL and bicuculline groups, confirming RTN was not activated above baseline

---

## ABD Response Characteristics

### Response Incidence and Qualitative Features

| Group | Responders / Total | Late-E component | Tonic expiratory component | Post-I ABD peak |
|-------|--------------------|------------------|---------------------------|-----------------|
| -0.2 mm | 3/5 | Yes | No | No |
| +0.1 mm | 7/7 | Yes | No | No |
| +0.4 mm | 5/5 | Yes | No | No |
| +0.6 mm | 6/6 | Yes | Yes | Yes (5/6 rats) |
| +0.8 mm | 5/5 | Yes | Yes | No |

### Temporal Dynamics of ABD Response

| Group | Response onset delay (sec) | ABD response duration (min) | Onset relative to injections |
|-------|---------------------------|----------------------------|------------------------------|
| -0.2 mm | 20.3 +/- 13.4 | 2.4 +/- 1.1 | After 2nd injection |
| +0.1 mm | 32.5 +/- 20.6 | -- | After 2nd injection |
| +0.4 mm | 40.1 +/- 28.7 | -- | After 2nd injection |
| +0.6 mm | 88.7 +/- 32.3 (before 2nd inj) | 17.6 +/- 2.7 | After 1st injection |
| +0.8 mm | 23.1 +/- 19.8 | 17.1 +/- 3.3 | After 2nd injection |

Statistical tests for response duration:
- One-Way ANOVA: p = 0.043, eta-squared = 0.41
- Tukey post-hoc: -0.2 vs +0.6 mm: p = 0.048; -0.2 vs +0.8 mm: p = 0.041

Observations:
- Most robust ABD responses (by integrated EMG amplitude) occurred within first 2 min post-second injection across all groups
- Caudal groups (-0.2, +0.1, +0.4 mm) declined to zero by 18 min post-injection
- Rostral groups (+0.6, +0.8 mm) maintained detectable responses beyond 20 min
- The +0.6 mm group uniquely initiated responses after the first injection, with amplification after the second

---

## Expiratory Flow Measures

### Late-E Peak Amplitude (V)

| Group | Max Late-E Peak Amplitude (V) | Time of max (min post-2nd inj) |
|-------|-------------------------------|-------------------------------|
| -0.2 mm | -0.014 +/- 0.004 | 2-4 |
| +0.1 mm | -0.021 +/- 0.007 | 2-4 |
| +0.4 mm | -0.023 +/- 0.004 | 2-4 |
| +0.6 mm | -0.033 +/- 0.007 | 2-4 |
| +0.8 mm | -0.027 +/- 0.011 | 6-8 |

One-Way ANOVA for max late-E peak amplitude: p = 0.41 (not significant)

### Late-E Peak Area (V.s)

| Group | Max Late-E Peak Area (V.s) |
|-------|---------------------------|
| -0.2 mm | -0.0014 +/- 0.0007 |
| +0.1 mm | -0.0035 +/- 0.0015 |
| +0.4 mm | -0.0038 +/- 0.0011 |
| +0.6 mm | -0.0056 +/- 0.0010 |
| +0.8 mm | -0.0047 +/- 0.0019 |

One-Way ANOVA for max late-E area: p = 0.41 (not significant)

Note: Although individual comparisons of late-E peak amplitude and area did not reach significance, a clear trend of increasing values at more rostral sites was observed.

---

## Standard Respiratory Variables

### Respiratory Rate Changes

| Group | Min RR (bpm) | % Drop from baseline | Time of minimum (min post-inj) |
|-------|-------------|---------------------|-------------------------------|
| -0.2 mm | 37.08 +/- 1.36 | 12% | 2 |
| +0.1 mm | 37.2 +/- 2.0 | 17% | 4 |
| +0.4 mm | 40.1 +/- 1.6 | 9% | 4 |
| +0.6 mm | 32.3 +/- 1.2 | 25% | 6 |
| +0.8 mm | 30.2 +/- 2.9 | 24% | 6 |

### Inspiratory and Expiratory Duration

| Phase | Baseline (s) | Response (s) | Wilcoxon Z | p-value |
|-------|-------------|-------------|-----------|---------|
| Inspiratory time (Ti) | 0.318 +/- 0.043 | 0.279 +/- 0.034 | 3.24 | 0.001 |
| Expiratory time (TE) | 1.029 +/- 0.161 | 1.313 +/- 0.188 | 4.49 | 0.001 |

Interpretation: The drop in respiratory rate was driven by prolonged expiration and shortened inspiration across all groups.

### Tidal Volume (VT) Changes

| Group | Peak VT (ml/kg) | % Change from baseline | Time of peak (min) |
|-------|----------------|----------------------|-------------------|
| -0.2 mm | 7.0 +/- 0.4 | +8% | 4 |
| +0.1 mm | 8.0 +/- 0.3 | +16% | 4 |
| +0.4 mm | -- | -- | 4 |
| +0.6 mm | 10.8 +/- 0.5 | +29% | 4 |
| +0.8 mm | -- | -- | 4 |

One-Way ANOVA for max VT: p = 0.02, eta-squared = 0.42
Bonferroni: -0.2 vs +0.6 mm: p = 0.002; +0.1 vs +0.6 mm: p = 0.02

### Minute Ventilation (VE) Changes

| Group | Peak/Min VE (ml/min/kg) | % Change from baseline | Direction |
|-------|------------------------|----------------------|-----------|
| -0.2 mm | 255.4 +/- 16.2 | -12% | Decrease |
| +0.1 mm | -- | -- | -- |
| +0.4 mm | -- | -- | Increase |
| +0.6 mm | 414.3 +/- 22.7 | +42% | Increase |
| +0.8 mm | -- | -- | Increase |

One-Way Repeated Measures ANOVA: p = 0.001, eta-squared = 0.59
Bonferroni (rostral vs -0.2 mm): p = 0.0004

Key finding: VE was driven by decreased respiratory rate at caudal sites (causing net VE decrease), but by increased VT at rostral sites (overcoming the rate decrease to produce net VE increase).

### Oxygen Consumption (VO2) Changes

| Group | Min VO2 (ml/min/kg) | % Drop from baseline |
|-------|--------------------|--------------------|
| -0.2 mm | 17.3 +/- 3.3 | -10% |
| +0.1 mm | -- | ~ baseline |
| +0.4 mm | -- | ~ baseline |
| +0.6 mm | 11.8 +/- 0.8 | -33% |
| +0.8 mm | 12.2 +/- 6.1 | -25% |

One-Way Repeated Measures ANOVA: p = 0.0001, eta-squared = 0.59
Post-hoc: rostral sites significantly lower than caudal sites

### Ventilatory Efficiency (VE/VO2) Changes

| Group | Peak VE/VO2 | % Change from baseline | Time of peak (min post-2nd inj) |
|-------|------------|----------------------|-------------------------------|
| -0.2 mm | -- | ~ baseline | -- |
| +0.1 mm | -- | ~ baseline | -- |
| +0.4 mm | -- | ~ baseline | -- |
| +0.6 mm | 34.8 +/- 3.0 | +73% | 6-8 |
| +0.8 mm | 38.7 +/- 12.8 | +82% | 6-8 |

One-Way Repeated Measures ANOVA: p = 0.001, eta-squared = 0.55

The combination of increased VE and decreased VO2 at rostral sites produced hyperventilation, an effect absent at caudal sites.

---

## Phase-Specific Respiratory Analysis

### Late-E Phase Responses (Normalized Area)

Fig 5D observations: Injections at all locations induced negative airflow deflections. The +0.6 mm site showed significantly elevated expiratory airflow vs CTRL from 4 to 12 min post-injection.

| Comparison | Time range significant | Test statistic | p-value |
|------------|----------------------|---------------|---------|
| +0.6 mm vs CTRL (4 min) | 4-12 min | KW H(5) = 14.66 | 0.012, Dunn p < 0.001 |
| +0.6 mm vs CTRL (12 min) | -- | KW H(5) = 18.35 | 0.003, Dunn p < 0.001 |
| +0.6 mm vs -0.2 mm (8 min) | 8-20 min | KW H(4) = 11.41 | 0.022, Dunn p < 0.001 |
| Rostral ABD vs CTRL/caudal | 8-14 min | KW H(5) = 20.81 | < 0.001, Dunn p < 0.001 |

### Inspiratory Phase Responses

| Comparison | Time range | Test statistic | p-value |
|------------|-----------|---------------|---------|
| +0.6 mm vs CTRL (airflow, 2 min) | 2-12 min | KW H(4) = 13.25 | 0.021, Dunn p < 0.001 |
| +0.6 mm vs CTRL (airflow, 12 min) | -- | KW H(4) = 14.58 | 0.012, Dunn p = 0.001 |
| +0.6 mm vs +0.4 mm (airflow, 10 min) | 10-12 min | KW H(4) = 10.50 | 0.033, Dunn p = 0.004 |
| +0.6 mm vs +0.4 mm (airflow, 12 min) | -- | KW H(5) = 10.93 | 0.027, Dunn p = 0.003 |

Note: ABD contribution during inspiration was negligible (raw ABD EMG inactive during this phase; residual integrated signal attributed to exponential decay from integration).

### Post-Inspiratory Phase Responses

| Comparison | Time bin | Test statistic | p-value |
|------------|---------|---------------|---------|
| +0.8 mm ABD EMG vs others (6 min) | 6 min | KW H(4) = 10.37 | 0.035, Dunn p = 0.002 |
| +0.8 mm ABD EMG vs others (16 min) | 16 min | KW H(4) = 9.52 | 0.049, Dunn p = 0.005 |

Post-I airflow deflections most pronounced at +0.6 and +0.8 mm groups.

---

## Multivariate Trajectory Analysis

### 3D Respiratory Trajectory Deviations

Fig 6 shows 3D trajectories (airflow x DIA EMG x ABD EMG) computed from mean cycles at baseline vs response time bins.

| Group | Trajectory deviation pattern | Duration of significant deviation |
|-------|-----------------------------|---------------------------------|
| CTRL | Minimal deviation from baseline | No significant deviations |
| -0.2 mm | Small transient deviation | Short-lived (< 4 min) |
| +0.1 mm | Moderate deviation | Short-to-medium |
| +0.4 mm | Moderate deviation | Medium |
| +0.6 mm | Large sustained deviation in ABD-airflow plane | Extended (4-16+ min) |
| +0.8 mm | Large sustained deviation in ABD-airflow plane | Extended (4-16+ min) |

### Procrustes-like Distance Metrics

The multivariate distance measure (combining deformations across all three signals and all respiratory phases) differentiated between injection sites more effectively than any single respiratory variable.

| Comparison | Significant time bins | KW p-value range |
|-----------|----------------------|-----------------|
| +0.6 mm vs CTRL | Multiple from 4-12 min | p < 0.05 |
| +0.6 mm vs -0.2 mm | Multiple from 8-20 min | p < 0.05 |
| +0.8 mm vs CTRL | Multiple from 6-14 min | p < 0.05 |

Fig 6F-G: The combined trajectory deviation metric shows rostral sites produce the most pronounced and sustained multivariate respiratory changes. Kruskal-Wallis tests at each time bin confirm significant between-group differences (p < 0.05 at multiple time points), with Dunn post-hoc tests identifying rostral sites as the primary drivers.

---

## Summary of Effect Sizes Across Measures

| Measure | ANOVA p-value | Eta-squared | Best-responding group |
|---------|--------------|-------------|----------------------|
| ABD response duration | 0.043 | 0.41 | +0.6 / +0.8 mm |
| Max Tidal Volume | 0.02 | 0.42 | +0.6 mm |
| Max Minute Ventilation | 0.001 | 0.59 | +0.6 mm |
| Min O2 Consumption | 0.0001 | 0.59 | +0.6 / +0.8 mm |
| Max VE/VO2 | 0.001 | 0.55 | +0.8 mm |
| Late-E peak amplitude | 0.41 | -- | NS trend toward +0.6 mm |
| Late-E peak area | 0.41 | -- | NS trend toward +0.6 mm |

---

## Datasets, Baselines, and Metrics

### Recorded Signals
- Tracheal airflow (via flow transducer + carrier demodulator)
- Integrated ABD EMG (oblique abdominals)
- Integrated DIA EMG (diaphragm)
- End-tidal CO2 (gas analyzer)
- O2 fraction (gas analyzer)

### Derived Metrics
- Respiratory rate (bpm)
- Tidal volume (ml/kg)
- Minute ventilation (ml/min/kg)
- O2 consumption (ml/min/kg), calculated per Depocas and Hart (1957)
- VE/VO2 ratio
- Inspiratory time (Ti) and expiratory time (TE)
- Late-E peak amplitude (V) and area (V.s)
- Normalized area under mean-cycle signals for three respiratory phases
- 3D trajectory deviation (Procrustes-like multivariate distance)

### Immunohistochemistry Markers
- cFos (immediate early gene, activity marker)
- PHOX2B (RTN marker)
- ChAT (cholinergic/motor neuron marker)
- TH (catecholaminergic marker for C1/A5)
- Fluorobeads (injection site marker)

### Statistical Methods
- One-Way ANOVA with Tukey or Bonferroni post-hoc
- One-Way Repeated Measures ANOVA with Bonferroni
- Kruskal-Wallis with Dunn post-hoc (Sidak correction)
- Wilcoxon rank-sum test
- Effect size: eta-squared
- Significance threshold: alpha = 0.05 (some comparisons at p < 0.005)

### Figure Observations Summary
- Fig 2: Injection sites ventrolateral to VII, no RTN/TH overlap; cFos peaks at injection cores
- Fig 3: Rostral sites show longer-lasting ABD responses; +0.6 mm initiates after first injection
- Fig 4: VT and VE increase most at rostral sites; VO2 drops selectively at rostral sites; VE/VO2 increases only at +0.6/+0.8 mm
- Fig 5: Phase-decomposed analysis shows late-E phase carries strongest effects; inspiratory airflow also elevated at rostral sites
- Fig 6: 3D trajectory analysis provides the clearest differentiation between injection sites; rostral sites show largest and most sustained deviations from baseline respiratory patterns

