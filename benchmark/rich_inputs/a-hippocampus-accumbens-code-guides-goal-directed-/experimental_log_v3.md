# Experimental Log: Hippocampus-Accumbens Code for Goal-Directed Behavior

## Animals and Sample Sizes

| Parameter | Value |
|-----------|-------|
| Thy1-GCaMP6s mice (imaging) | n = 6 |
| C57Bl/6 mice (total) | n = 16 |
| Mice for behavioral training | n = 18 |
| Total GCaMP-expressing neurons | 5,372 |
| Putative dHPC-to-NAc neurons | 444 |
| Imaging sessions | 19 |
| Total place cells | 1,750 |
| dHPC-to-NAc place cells | 169 |
| ChR2 mice (optogenetics) | n = 4 |
| EYFP control mice (optogenetics) | n = 3 |

---

## Behavioral Training (Figure 1)

Mice trained over 5 days on a 360 cm textile belt with six textured zones and a 30 cm hidden reward zone.

### Training progression (repeated-measures ANOVA, n = 18 mice)

| Measure | F-statistic | Correction | p |
|---------|------------|------------|---|
| Rewarded laps per session | F(4) = 6.344 | GG-correction | < 0.05 |
| Anticipatory licking | F(4) = 3.803 | N/A | < 0.05 |
| Reward licking | F(4) = 4.276 | GG-correction | < 0.05 |

### Supplementary training metrics (repeated-measures ANOVA, Figure S1)

| Measure | F-statistic | Correction | p |
|---------|------------|------------|---|
| Average velocity | F(4) = 2.631 | N/A | 0.0430 |
| Number of laps run | F(4) = 8.771 | GG-corrected | < 0.001 |
| Number of licks | F(4) = 3.883 | GG-corrected | 0.0326 |
| Ratio of rewarded laps | F(4) = 3.331 | N/A | 0.0157 |

Training cohorts: n = 9 (cohort 1), n = 9 (cohort 2).

---

## Experiment 1: Enhanced Spatial Coding by dHPC-to-NAc Neurons (Figure 2)

### Place cell proportions (chi-squared test)

| Measure | dHPC- | dHPC-to-NAc | Test statistic | p |
|---------|-------|-------------|----------------|---|
| Place cell proportion | 1,581/4,928 (32%) | 169/444 (38%) | chi-squared(1, 5372) = 6.364 | 0.012 |

### Spatial tuning characteristics (Welch's t-test)

| Measure | Test statistic | p |
|---------|----------------|---|
| Spatial information rate | Welch's t(186.55) = 4.770 | < 0.001 |
| Sparsity | Welch's t(218.79) = 3.657 | < 0.001 |
| Reliability (in-place field per lap) | Welch's t(203.46) = 2.479 | 0.014 |
| In-place field activity | Welch's t(190.32) = 2.884 | 0.0044 |

### Place field width (Figure S4, Kolmogorov-Smirnov test)

| Measure | dHPC- quartiles | dHPC-to-NAc quartiles | Test | p |
|---------|-----------------|----------------------|------|---|
| Place field width | 35.6 / 51.7 / 69.0 cm | 36.5 / 58.9 / 69.0 cm | KS test, D = 0.116 | 0.0299 |

---

## Experiment 2: Place Fields Modulated by Local Cues and Reward Zone (Figure 3)

### Place field boundary accumulation (permutation test + chi-squared)

Both dHPC- and dHPC-to-NAc place field start and end positions overrepresented at >99.9th percentile compared to randomly shuffled distributions.

| Measure | chi-squared statistic | p |
|---------|----------------------|---|
| PF start positions (dHPC-to-NAc vs dHPC-) | chi-squared(1, 5134) = 5.735 | 0.033 |
| PF end positions (dHPC-to-NAc vs dHPC-) | chi-squared(1, 5217) = 4.397 | 0.036 |
| PF center positions (texture boundaries) | chi-squared(1, 5372) = 1.646 | 0.1995 |

### Reward zone overrepresentation (Figure 3E-F)

2-way ANOVA:

| Factor | F-statistic | p |
|--------|------------|---|
| Success | F_success(1,1) = 54.918 | < 0.001 |
| Projection | F_projection(1,1) = 0.958 | 0.338 |
| Interaction | F_interaction(1,1) = 2.969 | 0.098 |

Post-hoc Welch's t-tests with Bonferroni correction:

| Comparison | Test statistic | p |
|------------|----------------|---|
| dHPC- (high vs low success) | t_dHPC-(3.561) = 3.698 | 0.051 |
| dHPC-to-NAc (high vs low success) | t_dHPC-to-NAc(3.479) = 8.671 | 0.0036 |
| Low success (dHPC- vs dHPC-to-NAc) | t_low_success(13.629) = 0.093 | 1 |
| High success (dHPC- vs dHPC-to-NAc) | t_high_success(3.952) = 2.075 | 0.215 |

### Correlation: success rate vs place fields near reward zone (Figure S4F)

Pearson correlation: r_dHPC-(15) = 0.622, p = 0.0107

### Reward zone decoding (Figure 3G, Wilcoxon's test)

| Comparison | Test statistic | n | p |
|------------|----------------|---|---|
| dHPC-to-NAc vs sample-matched dHPC- | Wilcoxon's W(9) = 5.0 | 10 imaging sessions | 0.0195 |

---

## Experiment 3: Velocity Coding (Figure 4)

### Speed-excited neurons (chi-squared test)

| Population | Proportion | chi-squared | p |
|------------|-----------|-------------|---|
| dHPC- | 13% | chi-squared(1, 5372) = 2.565 | 0.109 |
| dHPC-to-NAc | 16% | -- | -- |

### Speed-inhibited neurons (chi-squared test)

| Population | Proportion | chi-squared | p |
|------------|-----------|-------------|---|
| dHPC- | 15% | chi-squared(1, 5372) = 13.66 | 0.00022 |
| dHPC-to-NAc | 21% | -- | -- |

### Representative speed-excited neuron (linear regression)

slope = 7.43 x 10^-4, intercept = -2.097 x 10^-3, r = 0.937, p = 0.0058

### Representative speed-inhibited neuron (linear regression)

slope = -1.0437 x 10^-4, intercept = 2.814 x 10^-3, r = -0.933, p = 0.0065

Speed-modulated neurons classified at p < 0.05 after Benjamini/Hochberg FDR correction.

---

## Experiment 4: Appetitive Licking Modulation (Figure 5)

### Population-level lick modulation (two-way mixed ANOVA, Figure 5C)

| Factor | F-statistic | p |
|--------|------------|---|
| Lick timing | F_licktiming(1, 5370) = 2.843 | 0.0918 |
| Projection | F_projection(1, 5370) = 43.779 | < 0.001 |
| Interaction | F_interaction(1, 5370) = 7.073 | 0.0079 |

Post-hoc t-tests with Bonferroni correction:

| Comparison | Test statistic | p |
|------------|----------------|---|
| dHPC- | t_dHPC-(4927) = 0.871 | 0.768 |
| dHPC-to-NAc | t_dHPC-to-NAc(443) = 2.470 | 0.0277 |

### Single-cell lick modulation (chi-squared tests)

Total lick-modulated neurons: 1,268 (24%)

| Cell type | dHPC- | dHPC-to-NAc | chi-squared | p |
|-----------|-------|-------------|-------------|---|
| Lick-excited | 3.8% | 7.4% | chi-squared(1, 5372) = 13.018 | 0.00031 |
| Lick-inhibited | 19.7% | 17.1% | chi-squared(1, 5372) = 1.626 | 0.202 |

### Supplementary lick modulation (Figure S5)

| Measure | Test statistic | p |
|---------|----------------|---|
| Consummatory licking depression (2-way mixed ANOVA) | F_reward_timing(2, 10740) = 19.380 (GG-corrected) | < 0.001 |
| F_projection | F(1, 5370) = 0.798 | 0.372 |
| F_interaction | F(2, 10740) = 5.559 | 0.0039 |
| Lick modulation (pre-post difference) | Welch's t(496.11) = 2.379 | 0.0177 |
| Lick index | Welch's t(454.19) = 2.729 | 0.0066 |

---

## Experiment 5: Optogenetic Stimulation (Figure 6)

### Mouth motion (paired t-tests)

| Group | Test statistic | p |
|-------|----------------|---|
| ChR2 | t(3) = 7.485 | 0.00494 |
| EYFP | t(2) = 1.353 | 0.309 |

Additional report: pChR2 = 0.0099, pEYFP = 0.617

### Velocity change (paired t-tests)

| Group | Test statistic | p |
|-------|----------------|---|
| ChR2 | t(3) = -3.551 | 0.0381 |
| EYFP | t(2) = -1.263 | 0.334 |

---

## Experiment 6: Conjunctive Coding (Figure 7)

### Space x Velocity conjunctive coding (chi-squared tests)

| Comparison | chi-squared | p |
|------------|-------------|---|
| Place cells speed-inhibited vs non-place cells (dHPC-) | chi-squared(1, 4928) = 522.71 | < 0.001 |
| Place cells speed-inhibited vs non-place cells (dHPC-to-NAc) | chi-squared(1, 444) = 75.02 | < 0.001 |
| dHPC-to-NAc vs dHPC- place cells speed-inhibited | chi-squared(1, 1750) = 8.977 | 0.0027 |
| Speed-excited in non-place vs place cells (dHPC-) | chi-squared(1, 4928) = 20.034 | < 0.001 |
| Speed-excited in non-place vs place cells (dHPC-to-NAc) | chi-squared(1, 444) = 9.966 | < 0.001 |
| dHPC-to-NAc vs dHPC- non-place cells speed-excited | chi-squared(1, 3622) = 6.255 | < 0.05 |

### Space x Licking conjunctive coding

| Comparison | chi-squared | p |
|------------|-------------|---|
| Lick-excited in place vs non-place cells (dHPC-) | chi-squared(1, 4928) = 114.515 | < 0.001 |
| Lick-excited in place vs non-place cells (dHPC-to-NAc) | chi-squared(1, 444) = 23.248 | < 0.001 |
| dHPC-to-NAc vs dHPC- lick-excited place cells | chi-squared(1, 1750) = 9.442 | < 0.05 |
| dHPC-to-NAc vs dHPC- lick-excited non-place cells | chi-squared(1, 3622) = 0.488 | 0.485 |
| Lick-inhibited place vs non-place cells | all chi-squared | all p > 0.05 |

Place cells: 8% lick-excited vs 2% non-place cells (p < 0.001); dHPC-to-NAc: 15% vs 3% (p < 0.001)

### Velocity x Licking conjunctive coding

| Comparison | chi-squared | p |
|------------|-------------|---|
| Lick-excited in speed-inhibited cells (dHPC-) | chi-squared(2, 4928) = 100.484 | < 0.001 |
| Lick-excited in speed-inhibited cells (dHPC-to-NAc) | chi-squared(2, 444) = 27.608 | < 0.001 |
| Lick-excited enriched in speed-inhibited dHPC-to-NAc vs dHPC- | chi-squared(1, 830) = 6.564 | < 0.05 |
| Lick-inhibited in speed-excited cells (dHPC-) | chi-squared(2, 4928) = 290.832 | < 0.001 |
| Lick-inhibited in speed-excited cells (dHPC-to-NAc) | chi-squared(2, 444) = 18.825 | < 0.001 |

Speed-inhibited lick-excited: 11% vs 2% speed-excited (p < 0.001); dHPC-to-NAc: 20% vs 1% (p < 0.001). Speed-excited lick-inhibited: 40% vs 6% speed-inhibited (p < 0.001).

---

## Experiment 7: GLM Confirms Conjunctive Coding (Figure 8)

GLM variance explained: close to 40% on test datasets.

### Single-feature modulation (chi-squared tests)

| Feature | chi-squared(1, 5372) | p |
|---------|---------------------|---|
| Position | 93.634 | < 0.001 |
| Velocity | 141.86 | < 0.001 |
| Licking | 10.050 | 0.0015 |

### Conjunctive coding combinations (chi-squared tests)

| Combination | chi-squared(1, 5372) | p |
|-------------|---------------------|---|
| Position & Velocity | 163.97 | < 0.001 |
| Position & Licking | 26.029 | < 0.001 |
| Velocity & Licking | 27.145 | < 0.001 |
| Position & Velocity & Licking | 34.993 | < 0.001 |

### N-feature coding neuron proportions (chi-squared tests)

| Category | chi-squared(1, 5372) | Direction |
|----------|---------------------|-----------|
| Non-coding | 35.382 | overrepresented in dHPC- |
| Single-coding | 0.0057 | comparable |
| Dual-coding | 61.336 | overrepresented in dHPC-to-NAc |
| Triple-coding | 30.447 | overrepresented in dHPC-to-NAc |

Overall conjunctive coding: 44% dHPC-to-NAc vs 19% dHPC- (p < 0.001, chi-squared)

### Reward zone decoding (Figure 8G, Wilcoxon's test)

Conjunctive vs non-conjunctive coding neurons: Wilcoxon's W(18) = 14.0, p < 0.001

### GLM supplementary (Figure S6)

| Measure | Test statistic | p |
|---------|----------------|---|
| GLM R2 (dHPC-to-NAc vs dHPC-) | Welch's t(615.15) = 2.147 | 0.032 |
| Feature importance: position | Welch's t(2508.09) = 2.162 | 0.031 |
| Feature importance: licking | Welch's t(1879.75) = 9.328 | < 0.001 |
| Feature importance: velocity | Welch's t(2609.15) = 0.881 | 0.378 |
| R2 drop: position | Welch's t(523.23) = 5.984 | < 0.001 |
| R2 drop: velocity | Welch's t(497.69) = 7.704 | < 0.001 |
| R2 drop: licking | Welch's t(552.63) = 0.3626 | 0.717 |

---

## Methods Parameters

### Viral Vectors

| Virus | Titer | Volume | Target | Coordinates |
|-------|-------|--------|--------|-------------|
| AAVrg-pgk-Cre (Addgene #24593) | 1 x 10^13 vg/ml | 2 x 500 nl at 100 nl/min | NAc (ipsilateral right) | -1.3 mm AP, -1.0 mm lateral, 5.0 and 4.3 mm ventral (Bregma) |
| AAV5-hSyn-DIO-mCherry (Addgene #50459) | 1.1 x 10^13 vg/ml | 200 nl | dHPC (ipsilateral) | 3.38 mm AP, -2.5 mm lateral, 1.8 mm ventral (Bregma, 10-degree angle) |
| AAV2-CaMKII-hChR2(H134R)-EYFP-WPRE (UNC #AV4381E) | 4 x 10^12 TU | 200 nl each bilateral | dHPC | 3.38 mm AP, +/- 2.5 mm lateral, 1.8 mm ventral (Bregma, 10-degree angle) |
| rAAV2-CaMKII-EYFP (UNC #AV6650) | 4.3 x 10^12 TU | 200 nl each bilateral | dHPC | 3.38 mm AP, +/- 2.5 mm lateral, 1.8 mm ventral (Bregma, 10-degree angle) |

### Surgery Parameters

| Parameter | Value |
|-----------|-------|
| Anesthesia | ketamine (0.13 mg/g) + xylazine (0.01 mg/g), i.p. |
| Post-surgery analgesia | buprenorphine (0.05 mg/kg), thrice daily for 3 days |
| Cranial window cannula | 1.7 mm long, 3 mm outer diameter, stainless-steel |
| Coverslip diameter | 3 mm |
| Skull hole diameter | 0.5 mm (injection), 3 mm (cranial window) |
| Skin incision | 5 mm |

### Optogenetic Stimulation Parameters

| Parameter | Value |
|-----------|-------|
| Fiber-optic cannula coordinates | +1.3 mm AP, +/-1 mm lateral, -4.9 mm ventral (brain surface, Bregma) |
| Laser wavelength | 473 nm |
| Light intensity | 5 mW (at fiber output) |
| Pulse frequency | 20 Hz |
| Pulse duration | 5 ms |
| Maximum stimulation duration | 10 seconds |

### Imaging Parameters

| Parameter | Value |
|-----------|-------|
| Excitation laser (GCaMP6s) | 920 nm (Ti:sapphire, Chameleon Ultra II) |
| Excitation laser (mCherry) | 1045 nm (fixed-wavelength, Spectra Physics) |
| Objective | 16x (N16XLWD-PF, Nikon) |
| GCaMP emission filter | 525/40 nm bandpass |
| mCherry emission filter | 590/40 nm bandpass |
| Frame rate | 15.2 Hz (1024 x 1024) or 30.5 Hz (512 x 512) |
| Field of view | 350-850 um square |
| Signal collection rate | 10 kHz |

### Behavioral Task Parameters

| Parameter | Value |
|-----------|-------|
| Belt length | 360 cm |
| Belt width | 7 cm |
| Number of textured zones | 6 |
| Reward zone length | 30 cm |
| Anticipation zone length | 30 cm |
| Training duration | 5 days, 15 minutes per day |
| Food restriction | ~80% of daily food pellets |
| Weight loss | 10-20% of original weight |
| Camera acquisition rate | 25 or 75 Hz |
| Camera resolution | 782 x 582 pixels |

### Analysis Parameters

| Parameter | Value |
|-----------|-------|
| Spatial bins | 45 bins of 8 cm |
| Velocity threshold for spatial analysis | >2 cm/s |
| Shuffle iterations for place cell ID | 1000x |
| Shuffle threshold for place cell ID | 95th percentile |
| Velocity bins for speed modulation | 1 cm/s bins from 2 to 30 cm/s |
| FDR correction method | Benjamini/Hochberg |
| Lick bout threshold | <2 seconds between events |
| Appetitive lick onset | preceded by >=3 seconds absence of licks |
| GLM train/validation/test ratio | 0.8/0.1/0.1 |
| GLM shuffled models per feature | 100 |
| GLM significance threshold | >95% (96/100) of shuffled models |
| GLM temporal smoothing | Gaussian window 0.5 s (SD = 2) |
| GLM temporal downsampling | 3 Hz |
| CaImAn version | v1.6.2 |
| NormCorre parameters | max_shifts = 40, num_frames_split = 2000, overlaps = 46, splits_els = 4, strides = 255 |
| Successful laps definition | >=50% relative licking in reward + anticipation zones and reward received |
| High success trials | >=50% successful laps |

---

## Statistics Summary

All statistical tests used in this study:

1. **Repeated-measures ANOVA** (with Greenhouse-Geisser correction where noted) - training progression (Figure 1D), supplementary training metrics (Figure S1)
2. **Chi-squared test** - place cell proportions, speed modulation proportions, lick modulation proportions, conjunctive coding proportions (Figures 2D, 3C-D, 4D, 4H, 5H-I, 7B, 7D, 7F, 8B-C, 8E)
3. **Welch's t-test** - spatial tuning characteristics, place field width, lick modulation indices (Figures 2E-H, S5D-E, S6)
4. **Two-way ANOVA** - reward zone overrepresentation (Figure 3F)
5. **Two-way mixed ANOVA** - population lick modulation (Figure 5C), consummatory licking (Figure S5C)
6. **Post-hoc t-tests with Bonferroni correction** - following ANOVAs (Figures 3F, 5C, S5C)
7. **Wilcoxon's signed-rank test** - reward zone decoding accuracy (Figures 3G, 8G)
8. **Paired t-test** - optogenetic stimulation effects (Figure 6)
9. **Permutation test** (1000x bootstrap) - place field boundary overrepresentation (Figure 3C-D)
10. **Kolmogorov-Smirnov test** - place field width distributions (Figure S4B)
11. **Pearson correlation** - reward zone overrepresentation vs behavioral success (Figure S4F)
12. **Linear regression** - velocity modulation (Figure 4)
13. **Benjamini/Hochberg FDR correction** - velocity modulation classification
14. **Generalized linear Poisson model** - conjunctive coding with shuffle-based significance (Figure 8)
15. **SVM linear classifier** - reward zone decoding (Figures 3G, 8F-G)

All data presented as mean +/- SEM. Significance threshold: p < 0.05.
