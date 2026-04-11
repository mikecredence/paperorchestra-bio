# Experimental Log

> Pre-writing data tables and observations for the sex-specific neocortical resilience study.

---

## Animal Groups

| Group | n (varies by experiment) | Weight | Diet |
|-------|------------------------|--------|------|
| CTR Male | 8-17 | 27.82 g [95% CI: 26.84-28.79] | Ad libitum |
| FR Male | 8-19 | Reduced to 85% | 27% restriction |
| CTR Female | 7-23 | 23.21 g [95% CI: 22.35-24.07] | Ad libitum |
| FR Female | 6-11 | Reduced to 85% | 39% restriction |

Male vs female baseline weight: t = 7.58, df = 66, p < 0.001.

---

## Experiment 1: Food Intake and Weight Loss

| Comparison | t-statistic | df | p-value |
|-----------|-------------|-----|---------|
| CTR male vs FR male (food intake) | 4.81 | 25 | < 0.0001 |
| CTR male vs CTR female (food intake) | 0.013 | 25 | 0.99 |
| CTR female vs FR female (food intake) | 6.59 | 25 | < 0.0001 |
| FR male vs FR female (food intake) | 1.93 | 25 | 0.07 |
| CTR male vs FR male (weight) | 11.36 | 25 | < 0.0001 |
| CTR female vs FR female (weight) | 8.36 | 25 | < 0.0001 |

Fig. 1A: Animal weight across time. Fig. 1B: Daily food intake with percent restriction shown.
Fig. 1C: Final weights. Females required 40% more restriction for equivalent weight loss.

---

## Experiment 2: Serum Leptin

| Comparison | t-statistic | df | p-value | n |
|-----------|-------------|-----|---------|---|
| CTR male vs FR male | 4.58 | 66 | < 0.0001 | 17 CTR, 19 FR |
| CTR female vs FR female | 1.00 | 66 | 0.32 | 23 CTR, 11 FR |

Fig. 1D: Serum leptin approximately 3-fold decreased in FR males; no significant change in FR females.

---

## Experiment 3: Molecular Pathways in V1

### AMPK Thr172 Phosphorylation (normalized by total AMPK)

| Comparison | t-statistic | df | p-value | n |
|-----------|-------------|-----|---------|---|
| CTR male vs FR male | 2.28 | 39 | 0.022 | 11 CTR, 15 FR |
| CTR female vs FR female | 0.64 | 39 | 0.11 | 11 CTR, 6 FR |

### PPARalpha DNA Binding Activity (normalized to protein)

| Comparison | t-statistic | df | p-value | n |
|-----------|-------------|-----|---------|---|
| CTR male vs FR male | 4.81 | 30 | 0.013 | 5 CTR, 11 FR |
| CTR female vs FR female | 0.0016 | 30 | 0.99 | 9 CTR, 9 FR |

Fig. 1E: AMPK phosphorylation and PPARalpha activity in V1 tissue across sex and diet.

---

## Experiment 4: RNA Sequencing of V1

| Metric | Males | Females |
|--------|-------|---------|
| DEGs with food restriction (adj p < 0.1) | Significant number | Far fewer / none significant |
| Overlap between sexes (Venn diagram) | Minimal | Minimal |
| AMPK pathway | Significantly modulated | Not significantly modulated |
| mTOR pathway | Significantly modulated | Not significantly modulated |
| PPARalpha pathway | Significantly modulated | Not significantly modulated |
| Oxidative phosphorylation | Significantly modulated | Not significantly modulated |

Fig. 2A: RNA sequencing schema. Fig. 2B: Volcano plots showing DEGs by sex.
Fig. 2: Cellular energy pathways more robustly changed by food restriction in males.

---

## Experiment 5: ATP Usage in V1

| Condition | Male CTR vs FR | Female CTR vs FR |
|-----------|---------------|-----------------|
| Visual stimulation (natural scenes) | Significant decrease in FR | No significant change |
| No visual stimulation (dark) | No significant change | No significant change |

Fig. 3A: ATP imaging setup with ATeam1.03YEMK mice.
Fig. 3B: FRET signal traces during visual stimulation.
Supp. Fig. 1: ATP usage unaffected by food restriction in absence of visual stimulation in both sexes.

---

## Experiment 6: Orientation Selectivity

| Measure | Male CTR | Male FR | Female CTR | Female FR |
|---------|----------|---------|-----------|-----------|
| Orientation selectivity index | Higher | Decreased | Baseline | No significant change |
| Population coding precision | Higher | Decreased | Baseline | No significant change |

Fig. 3: Orientation selectivity and ATP usage in V1 more robustly decreased by food restriction in males.

---

## Experiment 7: Bayes Factor Analysis

| Parameter | Males BF10 | Females BF10 | Males Effect Size | Females Effect Size |
|-----------|-----------|-------------|------------------|-------------------|
| Serum leptin | Strong evidence (> 10) | Weak evidence (< 3) | Large | Small |
| AMPK phosphorylation | Moderate-strong | Weak | Moderate | Small |
| PPARalpha activity | Strong | Weak/absent | Large | Negligible |
| ATP usage | Moderate-strong | Weak | Moderate | Small |
| Orientation selectivity | Moderate | Weak | Moderate | Small |

Supp. Fig. 3: Bayes factor analysis confirms food restriction effects more robust in males across all parameters.

---

## Pupil Diameter Control

| Comparison | t-statistic | df | p-value | n |
|-----------|-------------|-----|---------|---|
| Male vs Female (pooled across diet) | 0.82 | 18 | 0.42 | 7 CTR males, 8 FR females, 1 CTR female, 4 FR females |

Supp. Fig. 2: Pupil diameter during visual stimulation not affected by sex or food restriction.

---

## Summary of Sex-Specific Effects

| Measure | Males: FR Effect | Females: FR Effect |
|---------|-----------------|-------------------|
| Food restriction required | 27% of ad lib | 39% of ad lib |
| Serum leptin | Decreased 3-fold | No significant change |
| AMPK phosphorylation | Increased | No significant change |
| PPARalpha activity | Increased | No significant change |
| V1 RNA-seq pathways | Multiple pathways changed | No significant pathway changes |
| V1 ATP usage | Decreased | No significant change |
| V1 orientation selectivity | Decreased | No significant change |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Females require greater food restriction; leptin maintained in females |
| Fig. 2 | RNA-seq shows energy pathways modulated in males only |
| Fig. 3 | ATP usage and orientation selectivity decreased in males only |
| Supp. 1 | No effect without visual stimulation in either sex |
| Supp. 2 | Pupil diameter unaffected by sex or diet |
| Supp. 3 | Bayes factors confirm more robust effects in males |

---

## Reference Count
57 references cited.
