Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Nature Mental Health

## Idea Summary

## Working title

Dose-dependent neural responses in a thalamic circuit driven by beliefs about nicotine strength in human smokers

## Core question

Can subjective beliefs about the nicotine content of an e-cigarette modulate brain activity in a dose-dependent manner -- analogous to pharmacological dose-response curves -- in circuits known to be affected by nicotine, even when actual nicotine intake is held constant?

## Motivation / gap

- Beliefs profoundly influence behavior and wellbeing, but the precise mapping between subjective beliefs and neural substrates is largely unknown
- Placebo research has shown binary (all-or-none) effects of beliefs on neural responses to nicotine, but no study has tested whether beliefs can produce graded, dose-dependent neural modulation
- Pharmacological dose-response relationships are well established for nicotine, alcohol, and other drugs in the brain, but this framework has rarely been applied to cognitive constructs like beliefs
- The thalamus contains one of the highest densities of nicotinic acetylcholine receptors (nAChRs) in the human brain and shows dose-dependent responses to actual nicotine, making it a strong candidate region for belief-driven modulation
- PET studies show that habitual smoking behavior can produce substantial nAChR occupancy in the thalamus even with minimal nicotine, but the mechanism linking subjective beliefs to this neural effect is unclear

## Core contribution (bullet form)

- Instructed beliefs about nicotine strength ("low", "medium", "high") successfully modulated perceived nicotine strength in smokers (rated 3.52, 4.52, 5.82 on 10-point scale; rmANOVA F(2,38)=9.71, P=0.0004, partial eta-squared=0.34)
- Thalamic activity during a value-based decision-making task increased parametrically with belief dosage (cluster-level PFWE=0.006), while actual nicotine intake, metabolism (cotinine), and baseline saturation (CO levels) did not differ across conditions
- Functional coupling between thalamus and ventromedial prefrontal cortex (vmPFC) also scaled parametrically to belief dosage, revealing a circuit-level dose-response relationship
- Striatal (nucleus accumbens) reward-related responses did not differ across belief conditions (rmANOVA P=0.945), demonstrating anatomical specificity of the belief effect to thalamus
- Subjective perception of nicotine strength correlated parametrically with thalamic neural activity across individuals, bridging the gap between subjective experience and neural representation

## Method in brief

Twenty nicotine-dependent adults (final sample after exclusions; 6 females, mean age 41.1 years, range 24-61, minimum 10 cigarettes/day for over 1 year) completed three fMRI sessions spaced approximately one week apart. In each session, participants were instructed that an e-cigarette contained either "low", "medium", or "high" nicotine, while actual nicotine content was held constant at 1.2%. After 20 minutes of controlled vaping, participants performed a value-based decision-making task in the scanner. Saliva samples were collected before and after vaping for cotinine quantification via LC-MS/MS, and exhaled CO was measured before vaping as a baseline saturation index.

The fMRI analysis focused on reward-tracking signals (parametric modulation by market return) across belief conditions using a repeated-measures ANOVA design. A priori regions of interest included the thalamus (independent anatomical mask) and nucleus accumbens. Psychophysiological interaction (PPI) analysis was used to assess belief-dependent changes in functional connectivity between thalamus and vmPFC. An exploratory comparison was made with a separate healthy control cohort (N=31 after exclusions, 15 females, mean age 28 years) who performed the same decision-making task without any nicotine manipulation. Power analysis based on prior work yielded a required sample of N=18-20 (Cohen's d=0.69 for reward learning in a similar design; 90% power at alpha=0.05).

## Target venue

Nature Mental Health


## Experimental Log

# Experimental Log: Nicotine-Related Beliefs and Dose-Dependent Thalamic Responses

## Participants

### Smoker Cohort

| Parameter | Value |
|-----------|-------|
| Total enrolled | 23 |
| Final sample | 20 |
| Excluded | 3 (1 software malfunction, 1 fell asleep, 1 lost behavioral data) |
| Sex | 6 females, 14 males |
| Age (mean +/- SD) | 41.1 +/- 11.97 years |
| Age range | 24-61 years |
| Handedness | All right-handed |
| Smoking criteria | Minimum 10 cigarettes/day for over 1 year |
| Exclusion: vaping experience | No prior e-cigarette use |
| Exclusion: quit attempts | Not currently attempting to quit |
| Exclusion: illicit drugs | None in past 2 months |
| Sessions per participant | 3 fMRI sessions |
| Session spacing | Approximately 1 week apart |

### Healthy Control Cohort

| Parameter | Value |
|-----------|-------|
| Total enrolled | 33 |
| Final sample | 31 |
| Excluded | 2 (excessive head movement > 3 mm) |
| Sex | 15 females, 16 males |
| Age (mean +/- SD) | 28 +/- 9 years |
| Nicotine status | Non-smokers (nicotine addiction as exclusion criterion) |
| Task | Same decision-making task, same imaging facility |

### Power Analysis

| Parameter | Value |
|-----------|-------|
| Reference effect size | Cohen's d = 0.69 (from prior fMRI nicotine-belief study, N=24/condition) |
| Target power | 90% (for primary analysis), 95% (for G*Power calculation) |
| Alpha | 0.05 (two-tailed) |
| Minimum N from prior study | 20 per condition |
| Minimum N from G*Power (rmANOVA, 3 measurements, f=0.4) | 18 |

## Experimental Design

### Session Structure (Fig 1A)

| Step | Procedure |
|------|-----------|
| 1 | Collect saliva sample (pre-vaping cotinine) |
| 2 | Measure exhaled CO (baseline saturation) |
| 3 | Instruct belief condition ("low", "medium", or "high" nicotine) |
| 4 | Vaping period (20 minutes, e-cigarette at 1.2% nicotine) |
| 5 | Collect saliva sample (post-vaping cotinine) |
| 6 | fMRI scan during decision-making task |

### Belief Manipulation

| Condition | Instructed Nicotine Strength | Actual Nicotine Content |
|-----------|-----------------------------|-----------------------|
| Low | "Low" nicotine | 1.2% (constant) |
| Medium | "Medium" nicotine | 1.2% (constant) |
| High | "High" nicotine | 1.2% (constant) |

## Sanity Check 1: Subjective Belief Manipulation (Fig 1B)

### Perceived Nicotine Strength (10-point scale)

| Condition | Mean | SD | Units |
|-----------|------|----|-------|
| Low | 3.52 | 0.61 | AU |
| Medium | 4.52 | 0.41 | AU |
| High | 5.82 | 0.47 | AU |

| Statistical Test | Value |
|-----------------|-------|
| Test type | Repeated-measures ANOVA |
| F statistic | F(2,38) = 9.71 |
| P value | 0.0004 |
| Effect size (partial eta-squared) | 0.34 |
| 90% CI for eta-squared | 0.12 to 0.48 |
| Result | Perceived nicotine strength increased with instructed belief |

## Sanity Check 2: Nicotine Intake (Fig 1C)

### Consumed Nicotine (mg)

| Condition | Mean | SD |
|-----------|------|----|
| Low | 0.928 | 0.56 |
| Medium | 0.719 | 0.423 |
| High | 0.783 | 0.434 |

| Statistical Test | Value |
|-----------------|-------|
| Test type | Repeated-measures ANOVA |
| F statistic | F(2,38) = 1.806 |
| P value | 0.178 |
| Result | No significant difference in nicotine intake across belief conditions |

- Nicotine intake computed as change in cartridge weight multiplied by actual nicotine percentage (1.2%)
- Vaping time controlled at 20 minutes
- Overall nicotine consumed comparable to amounts from traditional cigarettes in prior studies

## Sanity Check 3: Cotinine (Nicotine Metabolism) (Fig 1D)

### Vaping-Induced Change in Cotinine Concentration (ng/mL)

| Statistical Test | Value |
|-----------------|-------|
| Test type | Repeated-measures ANOVA |
| F statistic | F(2,32) = 0.959 |
| P value | 0.393 |
| Result | No significant difference in cotinine changes across conditions |

- Cotinine measured via high-performance liquid chromatography tandem mass spectrometry (LC-MS/MS)
- Saliva samples collected pre- and post-vaping
- Confirms nicotine metabolism was comparable across belief conditions

## Sanity Check 4: Baseline CO Levels (Fig 1E)

### Exhaled Carbon Monoxide (ppm)

| Statistical Test | Value |
|-----------------|-------|
| Test type | Repeated-measures ANOVA |
| F statistic | F(2,32) = 0.364 |
| P value | 0.698 |
| Result | No significant difference in CO levels across conditions |

- CO measured before vaping as index of baseline nicotine saturation
- Ensures participants arrived at each session with comparable baseline saturation

## Summary of Sanity Checks

| Measure | Low vs. Medium vs. High | F statistic | P value | Significant? |
|---------|------------------------|-------------|---------|-------------|
| Perceived nicotine strength | 3.52 < 4.52 < 5.82 | F(2,38) = 9.71 | 0.0004 | Yes |
| Nicotine intake (mg) | 0.928 vs. 0.719 vs. 0.783 | F(2,38) = 1.806 | 0.178 | No |
| Cotinine change (ng/mL) | Comparable | F(2,32) = 0.959 | 0.393 | No |
| Exhaled CO (ppm) | Comparable | F(2,32) = 0.364 | 0.698 | No |

## Main Result 1: Thalamic Dose-Dependent Response (Fig 2)

### Whole-Brain Analysis (Fig 2A)

| Analysis | Result |
|----------|--------|
| Contrast | Effect of instructed beliefs on value-tracking signals |
| Design | rmANOVA across three belief conditions |
| Significant cluster | Thalamus |
| Cluster-level correction | PFWE = 0.006 |
| Cluster size threshold | k = 50 |

### Thalamic ROI Analysis (Fig 2B)

| Condition | Thalamic Reward-Related Activity | Direction |
|-----------|--------------------------------|-----------|
| Low belief | Lowest | Parametric increase |
| Medium belief | Intermediate | Parametric increase |
| High belief | Highest | Parametric increase |

| Statistical Test | Value |
|-----------------|-------|
| ROI mask | Independent thalamus mask (shown in purple) |
| Test | rmANOVA on parameter estimates |
| P value | 0.036 |
| Healthy controls | Shown for comparison (orange bar) |

- Activity in thalamus increased parametrically according to belief dosage
- Across individuals, subjective perception of nicotine strength correlated parametrically with thalamic neural activity

### Anatomical Context

| Feature | Detail |
|---------|--------|
| Thalamic nAChR density | Among highest in human brain |
| Quantification methods | Autoradiography and functional imaging |
| Key finding from prior PET | Habitual smoking produces substantial nAChR occupancy even with moderate/low nicotine |
| Posterior thalamus | Especially high nAChR density |
| Functional role | Central for gating incoming sensory information, attention enhancement |

## Main Result 2: Striatum Shows No Belief Effect (Fig 3)

### Whole-Brain Cross-Condition Activation (Fig 3A)

| Analysis | Result |
|----------|--------|
| Contrast | Brain activation tracking market return across ALL belief conditions (collapsed) |
| Significant region | Striatum (among others) activated across conditions |

### Nucleus Accumbens ROI (Fig 3B)

| Condition | NAcc Reward-Related Activity | Direction |
|-----------|------------------------------|-----------|
| Low belief | Similar | No parametric change |
| Medium belief | Similar | No parametric change |
| High belief | Similar | No parametric change |

| Statistical Test | Value |
|-----------------|-------|
| ROI mask | Independent nucleus accumbens mask |
| Test (rmANOVA) | P = 0.945 |
| Permutation test | P = 0.94 |
| Healthy controls | Shown for comparison (orange bar) |
| Result | No dose-dependent modulation by beliefs in striatum |

- Demonstrates anatomical specificity: belief-driven dose response is present in thalamus but not in striatum
- Striatal reward signals were present across all conditions but did not distinguish between belief levels

## Main Result 3: Thalamus-vmPFC Functional Connectivity (Fig 4)

### PPI Analysis

| Analysis | Detail |
|----------|--------|
| Method | Psychophysiological interaction (PPI) |
| Seed region | Thalamus |
| Target region | vmPFC |
| Contrast | Effect of instructed beliefs on thalamus-vmPFC coupling |

### Connectivity Strength (Fig 4B)

| Condition | Thalamus-vmPFC Coupling | Direction |
|-----------|------------------------|-----------|
| Low belief | Lowest | Parametric increase |
| Medium belief | Intermediate | Parametric increase |
| High belief | Highest | Parametric increase |

- Functional coupling between thalamus and vmPFC scaled parametrically to belief dosage
- vmPFC is implicated in value representations and state representations
- This reveals a circuit-level dose-response relationship driven by beliefs

## Comparison: Thalamus vs. Striatum Belief Modulation

| Region | Belief Dose-Response | P value (rmANOVA) | Interpretation |
|--------|---------------------|-------------------|----------------|
| Thalamus | Present (parametric increase with belief) | 0.036 (ROI); 0.006 (cluster-level FWE) | Belief-sensitive, dose-dependent |
| Nucleus accumbens | Absent (no modulation by belief) | 0.945 | Belief-insensitive |
| Thalamus-vmPFC coupling | Present (parametric increase) | Significant | Circuit-level belief effect |

## Decision-Making Task

| Feature | Description |
|---------|-------------|
| Task type | Value-based decision-making |
| Neural signal of interest | Reward-tracking (parametric modulation by market return) |
| Known engagement | Engages neural circuits affected by nicotine |
| Performed | During fMRI after vaping |

## Questionnaires and Assessments

| Instrument | Purpose |
|-----------|---------|
| Positive and Negative Affect Schedule | Mental health assessment |
| Beck Depression Inventory | Depression screening |
| Post-vaping nicotine strength rating | Manipulation check (10-point scale) |
| Fagerstrom Test (implied by inclusion criteria) | Nicotine dependence assessment |

## Key Metrics and Definitions

| Metric | Definition |
|--------|-----------|
| Perceived nicotine strength | Self-reported rating on 10-point scale after vaping |
| Nicotine intake | Change in e-cigarette cartridge weight x 1.2% nicotine content |
| Cotinine | Nicotine metabolite measured in saliva via LC-MS/MS |
| Exhaled CO | Carbon monoxide in expired breath (ppm), index of recent smoking |
| Value-tracking signal | fMRI BOLD parametric modulation by market return in decision task |
| PPI | Psychophysiological interaction: context-dependent functional connectivity |
| PFWE | Family-wise error corrected p-value at cluster level |
| Partial eta-squared | Effect size for repeated-measures ANOVA |

## Baselines and Controls

| Comparison | Purpose |
|------------|---------|
| Low vs. Medium vs. High belief | Within-subject parametric belief manipulation |
| Healthy controls (N=31) | Exploratory comparison for thalamic and striatal activity |
| Nicotine intake across conditions | Confirm constant pharmacological exposure |
| Cotinine across conditions | Confirm comparable metabolism |
| CO across conditions | Confirm comparable baseline saturation |
| Thalamus vs. NAcc | Anatomical specificity of belief effect |

## Reference Count

- Total references cited: 53

