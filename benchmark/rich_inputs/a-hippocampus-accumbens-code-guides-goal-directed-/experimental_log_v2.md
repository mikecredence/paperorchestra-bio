# Experimental Log

> Pre-writing data tables and observations for the hippocampus-accumbens goal-directed navigation study.

---

## Animal and Recording Summary

| Parameter | Value |
|-----------|-------|
| Species/Strain (imaging) | Thy1-GCaMP6s mice (GP4.3, Jackson Lab) |
| Species/Strain (optogenetics) | C57Bl/6 mice |
| Total mice (imaging) | 6 |
| Total mice (optogenetics) | 16 |
| Total mice (behavioral training only) | 18 |
| Sex | Male and female |
| Light cycle | 12h reversed dark-light |
| Housing temperature | 21C |
| Experimental phase | Dark phase |

---

## Behavioral Task Parameters

| Parameter | Value |
|-----------|-------|
| Treadmill belt length | 360 cm |
| Number of textured zones | 6 |
| Reward zone length | 30 cm |
| Anticipation zone length | 30 cm (preceding reward zone) |
| Reward type | Liquid reward (dispensed once per lap upon licking) |
| Training duration | 5 days |
| Head fixation | Yes |
| Locomotion | Self-propelled treadmill |

---

## Training Progression (Repeated-Measures ANOVA, n=18 mice)

| Behavioral Measure | ANOVA F-statistic | df | Correction | Significance |
|-------------------|-------------------|-----|------------|-------------|
| Rewarded laps per session | F = 6.344 | 4 | Greenhouse-Geisser | p < 0.01 |
| Anticipatory licking | F = 3.803 | 4 | None specified | p < 0.05 |
| Reward zone licking | F = 4.276 | 4 | Greenhouse-Geisser | p < 0.05 |

Fig. 1B: Representative traces of one mouse's behavior on training day 1 vs. day 5, showing increased licking specificity near the reward zone.

Fig. 1C: Licking in both anticipation and reward zones increases over the five training days.

Fig. 1D: Number of rewarded laps, anticipatory licking, and reward licking all significantly increase across training sessions.

---

## Viral Vectors and Injection Coordinates

| Vector | Target | Coordinates (relative to Bregma) | Volume |
|--------|--------|----------------------------------|--------|
| AAVrg-pgk-Cre (Addgene #24593) | NAc (retrograde labeling) | AP -1.3 mm, ML -1.0 mm, DV -5.0 and -4.3 mm | 2 x 500 nl at 100 nl/min |
| AAV5-hSyn-DIO-mCherry (Addgene #50459) | dHPC (CA1/subiculum) | Not fully specified | 200 nl |
| AAV2-CaMKII-ChR2-EYFP (UNC #AV4381E) | dHPC (optogenetics) | dHPC coordinates | Titer: 4e12 TU |
| rAAV2-CaMKII-EYFP (UNC #AV6650) | dHPC (control) | dHPC coordinates | Titer: 4.3e12 TU |

Titer of AAVrg-pgk-Cre: 1e13 vg/ml. Titer of DIO-mCherry: 1.1e13 vg/ml.

---

## Imaging Parameters

| Parameter | Value |
|-----------|-------|
| Imaging modality | Dual-color two-photon |
| Calcium indicator | GCaMP6s (Thy1 pan-neuronal) |
| Static label | mCherry (Cre-dependent, NAc-projecting) |
| Cranial window | 3 mm cannula |
| Region imaged | dHPC CA1/prosubiculum border |
| Signal extraction | Denoised, deconvolved, and event traces |

Fig. S2A: Sample field of view crossing putative CA1 and prosubiculum, with spectrally separate green (GCaMP6s) and red (mCherry) channels.

---

## Experiment 1: Spatial Coding in dHPC->NAc vs. dHPC- Neurons

### Place Cell Proportions

| Population | Place Cell Proportion | Comparison |
|-----------|----------------------|------------|
| dHPC->NAc | Higher (enriched) | Significantly greater than dHPC- |
| dHPC- | Lower (baseline) | Reference population |

### Spatial Information Content

| Metric | dHPC->NAc | dHPC- | Direction |
|--------|-----------|-------|-----------|
| Spatial information (bits/event) | Higher | Lower | Enhanced in projection neurons |
| Trial-to-trial reliability | Higher | Lower | More consistent spatial maps |
| In-place-field activity | Higher | Lower | Stronger firing within fields |

Fig. 2A: Excerpt from a representative session showing behavioral activity (top) and denoised neural activity of identified place cells. dHPC->NAc neurons (red traces) and dHPC- neurons (green traces) are ordered by place field location.

Fig. 2: dHPC->NAc neurons carry enhanced and more reliable spatial information overall.

---

## Experiment 2: Place Field Modulation by Cues and Reward Zone

### Reward Zone Overrepresentation

| Population | Reward Zone Overrepresentation | Significance |
|-----------|-------------------------------|-------------|
| dHPC->NAc | Increased overrepresentation | Greater than dHPC- |
| dHPC- | Present but less pronounced | Baseline level |

### Local Cue Modulation

| Population | Cue Boundary Modulation | Observation |
|-----------|------------------------|-------------|
| dHPC->NAc | Stronger modulation | Place field edges cluster near texture boundaries |
| dHPC- | Weaker modulation | Less cue-driven spatial coding |

Fig. 3A: Heatmaps of dHPC- (left) and dHPC->NAc (right) place cells showing normalized position-binned average calcium events, ordered by place field location. Texture boundaries shown as white dashed lines; yellow rectangle marks reward zone.

Fig. 3B: Example place fields with edges near belt texture boundaries. Primary place fields are indicated by color fill. The dHPC->NAc population shows stronger alignment with texture transitions.

---

## Experiment 3: Speed Modulation

### Speed-Excited Neurons

| Metric | Example Neuron (Fig. 4A-B) |
|--------|---------------------------|
| Slope | 7.43e-4 |
| Intercept | -2.097e-3 |
| Correlation (r) | 0.937 |
| p-value | 0.0 (highly significant) |

Fig. 4A-B: Representative speed-excited neuron showing increased calcium activity during high-velocity periods irrespective of position. Linear regression on average calcium events per velocity bin confirms significant positive relationship.

### Speed-Modulated Cell Proportions

| Cell Type | dHPC->NAc Proportion | dHPC- Proportion | Direction of Enrichment |
|-----------|---------------------|-----------------|------------------------|
| Speed-excited | Similar or slightly enriched | Baseline | No major difference |
| Speed-inhibited | Overrepresented | Lower proportion | Significant enrichment in dHPC->NAc |

Fig. 4: Speed-inhibited cells (those that decrease activity with increasing velocity, i.e., deceleration-related) are overrepresented among dHPC->NAc neurons. This is functionally relevant because mice must decelerate as they approach the hidden reward zone.

---

## Experiment 4: Appetitive Licking Responses

### Lick-Excited Neuron Proportions

| Population | Lick-Excited Proportion | Significance |
|-----------|------------------------|-------------|
| dHPC->NAc | Overrepresented | Significantly enriched |
| dHPC- | Lower proportion | Baseline |

Fig. 5A: Representative example showing reward dispensation and appetitive licking onsets alongside population calcium activity. The dHPC->NAc population (red) shows robust activity increase around lick onsets, while dHPC- (green) does not.

Fig. 5B: Peri-lick time histograms confirm that dHPC->NAc neurons are preferentially excited by appetitive licking.

Fig. 5C: Quantification of lick-excited proportions across populations.

---

## Experiment 5: Optogenetic Stimulation of dHPC Axons in NAc

### Orofacial Movement Tracking

| Parameter | Value |
|-----------|-------|
| Camera type | Near-infrared |
| Sampling rate | 75 Hz |
| Analysis | Motion energy (pixel-by-pixel intensity difference) |
| Mouth segmentation | Automated |

Fig. 6A: Example still image from near-infrared camera.
Fig. 6B: False-color coded motion energy overlaid on sample image. Mouth region segmented automatically.
Fig. 6C: Average motion energy in mouth region increases with licking.

### Optogenetic Effects

| Measure | ChR2 Group | EYFP Control | Effect |
|---------|-----------|-------------|--------|
| Mouth movement (motion energy) | Increased | No change | Stimulation induces oral movements |
| Running velocity | Decreased (deceleration) | No change | Stimulation slows the animal |

Fig. 6: Optogenetic activation of dHPC terminals in NAc elicits two key behaviors: mouth/jaw movements resembling appetitive licking and deceleration. These match the enriched coding properties found in dHPC->NAc neurons.

---

## Experiment 6: Conjunctive Coding Analysis

### Venn Diagram Analysis (Fig. 7A)

| Population | Place + Speed-Negative | Place + Speed-Positive | Place + Lick | Triple Conjunctive |
|-----------|----------------------|----------------------|-------------|-------------------|
| dHPC->NAc | Higher overlap | Present | Higher overlap | Enriched |
| dHPC- | Lower overlap | Present | Lower overlap | Less common |

Fig. 7A: Venn diagrams for dHPC- (left) and dHPC->NAc (right) showing overlap between place cells and speed-modulated cells.

Fig. 7B: Proportions of place cells that are also speed-modulated, split by projection type. A greater fraction of dHPC->NAc place cells are also significantly speed-modulated.

### Conjunctive Coding Summary

| Coding Type | dHPC->NAc Enrichment | Functional Implication |
|------------|---------------------|----------------------|
| Position only | Enhanced | Better spatial mapping for reward navigation |
| Position + velocity | Enhanced | Combined spatial-locomotor signal near reward |
| Position + licking | Enhanced | Reward approach coding |
| Position + velocity + licking | Enhanced | Full goal-directed state representation |

---

## Experiment 7: Generalized Linear Model (GLM)

### Model Design

| Predictor | Description |
|-----------|-------------|
| Position | Linearized belt position (360 cm) |
| Velocity | Running speed |
| Appetitive licking | Binary lick events |

The GLM predicts each neuron's calcium activity from these three predictors. Model comparison uses likelihood ratio tests between the full model and reduced models (each predictor removed in turn).

### GLM Results

| Metric | dHPC->NAc | dHPC- | Comparison |
|--------|-----------|-------|------------|
| Full model fit | Better | Lower | Enhanced in projection neurons |
| Position contribution | Larger | Smaller | Consistent with place cell enrichment |
| Velocity contribution | Larger | Smaller | Consistent with speed cell enrichment |
| Licking contribution | Larger | Smaller | Consistent with lick cell enrichment |
| Conjunctive coding (interaction terms) | Stronger | Weaker | Enhanced in projection neurons |

Fig. 8A: Schematic of GLM approach. Example modeling for a triple conjunctive neuron showing true calcium activity vs. predictions from the full model and reduced models.

Fig. 8: The GLM confirms that dHPC->NAc neurons have enhanced conjunctive coding, meaning they integrate spatial, velocity, and appetitive information more strongly than the general dHPC population. This conjunctive representation improves the ability to identify when the animal is near the reward zone.

---

## Key Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| Belt length | 360 cm |
| Reward zone width | 30 cm |
| Anticipation zone width | 30 cm |
| Number of texture zones | 6 |
| Training days | 5 |
| Imaging mice (Thy1-GCaMP6s) | 6 |
| Optogenetics mice (C57Bl/6) | 16 |
| Behavioral training mice | 18 |
| Anesthetic (surgery) | Ketamine 0.13 mg/g + xylazine 0.01 mg/g (i.p.) |
| Drill hole diameter | 0.5 mm |
| Infrared camera sampling | 75 Hz (face), 25 Hz (body) |

---

## Statistical Methods Used

| Test | Application |
|------|------------|
| Repeated-measures ANOVA | Training progression (rewarded laps, licking) |
| Greenhouse-Geisser correction | Applied when sphericity assumption violated |
| Linear regression | Speed tuning (calcium events vs. velocity bins) |
| Chi-squared / proportion tests | Comparing place cell, speed cell, lick cell proportions between populations |
| Likelihood ratio test | GLM model comparison (full vs. reduced) |
| Spatial information (bits/event) | Place cell identification criterion |

---

## Figure Summary

| Figure | Key Finding |
|--------|------------|
| Fig. 1 | Task schematic; training increases reward-directed licking over 5 days; dual-color imaging setup |
| Fig. 2 | dHPC->NAc neurons have more place cells, higher spatial information, better reliability |
| Fig. 3 | dHPC->NAc place fields are modulated by local cues and over-represent the reward zone |
| Fig. 4 | Speed-inhibited cells are overrepresented in dHPC->NAc neurons |
| Fig. 5 | dHPC->NAc neurons are excited by appetitive licking |
| Fig. 6 | Optogenetic stimulation of dHPC axons in NAc induces mouth movement and deceleration |
| Fig. 7 | Enhanced conjunctive coding of space, velocity, and licking in dHPC->NAc neurons |
| Fig. 8 | GLM confirms enhanced conjunctive coding; better reward zone identification |
| Fig. S1 | Behavioral task details, belt texture images, training metrics |
| Fig. S2 | Dual-color imaging validation, spectral separation of GCaMP6s and mCherry |

---

## Reference Count
89 references cited in the paper.
