Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

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


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the cross-species brain development alignment study.

---

## Datasets Used

| Dataset | Source | Species | N Subjects | Age Range | Sex Distribution |
|---------|--------|---------|-----------|-----------|-----------------|
| HCP-Development | Human Connectome Project | Human | 370 | 8-14 years (mean 11.1 +/- 1.8) | 170 male / 200 female |
| UW-Madison Macaque MRI | University of Wisconsin-Madison | Macaca mulatta | 181 | 2-4 years (mean 2.8 +/- 0.6) | 89 male / 92 female |

---

## MRI Acquisition Parameters

| Parameter | Human (HCP-D) | Macaque (GE DISCOVERY MR750) | Macaque (GE Signa EXCITE) |
|-----------|---------------|------------------------------|--------------------------|
| Scanner | Siemens 3T Tim Trio | GE DISCOVERY MR750 3.0T | GE Signa EXCITE 3.0T |
| Head coil | 32-channel | N/A | N/A |
| T1w TR (ms) | 2500 | N/A | N/A |
| T1w TE (ms) | 2.22 | N/A | N/A |
| T1w flip angle | 8 deg | N/A | N/A |
| T1w voxel (mm) | 0.8 x 0.8 x 0.8 | N/A | N/A |
| dMRI directions | 185 (2-shell: b=1500, 3000) | 12 (b~1000) | 12 (b~1000) |
| dMRI b0 volumes | 28 | N/A | N/A |
| dMRI TR/TE (ms) | 3230/89.2 | N/A | N/A |
| dMRI voxel (mm) | 1.5 x 1.5 x 1.5 | N/A | N/A |
| Number of macaques | -- | 42 | 139 |

---

## Feature Types and Selection

| Feature Type | Description | Modality |
|-------------|-------------|----------|
| GMV | Gray matter volume per region | sMRI |
| FA | Fractional anisotropy per tract | dMRI |
| MD | Mean diffusivity per tract | dMRI |
| RD | Radial diffusivity per tract | dMRI |
| AD | Axial diffusivity per tract | dMRI |

### Feature Selection Criteria and Counts

| Selection Criterion | Macaque Features | Human Features |
|--------------------|-----------------|----------------|
| Common features (p < 0.01, 100 iterations) | 62 | 225 |
| Minimum MAE criterion (100 iterations) | 117 | 239 |
| Matched top features (same count) | 62 | 62 |

---

## Experiment 1: Intra-Species Age Prediction

Separate models trained and tested within species using selected brain features. Performance assessed via Pearson correlation (R), p-value, and mean absolute error (MAE).

### Primary analysis (common features: 62 macaque, 225 human)

| Species | R | P-value | MAE |
|---------|---|---------|-----|
| Macaque (intra-species) | 0.5729 | < 0.001 | 0.3758 years |
| Human (intra-species) | 0.6153 | < 0.001 | 1.1236 years |

### Minimum MAE features (117 macaque, 239 human)

| Species | R | P-value | MAE |
|---------|---|---------|-----|
| Macaque (intra-species) | 0.5825 | < 0.001 | 0.3675 years |
| Human (intra-species) | 0.6039 | < 0.001 | 1.1388 years |

### Matched feature count (62 macaque, 62 human)

| Species | R | P-value | MAE |
|---------|---|---------|-----|
| Macaque (intra-species) | reported | < 0.001 | reported |
| Human (intra-species) | reported | < 0.001 | reported |

Fig. 2A: Scatterplot of predicted vs. actual macaque age shows positive linear trend with 95% CI band. Each dot is one macaque.

Fig. 2D: Scatterplot of predicted vs. actual human age shows positive linear trend with 95% CI band. Each dot is one human.

---

## Experiment 2: Cross-Species (Inter-Species) Age Prediction

Models trained in one species applied to predict ages in the other species.

### Primary analysis (common features: 62 macaque, 225 human)

| Direction | R | P-value | MAE |
|-----------|---|---------|-----|
| Macaque model -> predict human ages | 0.4823 | < 0.001 | 8.3610 |
| Human model -> predict macaque ages | 0.2898 | < 0.001 | 7.6157 |

### Minimum MAE features (117 macaque, 239 human)

| Direction | R | P-value | MAE |
|-----------|---|---------|-----|
| Macaque model -> predict human ages | 0.4018 | < 0.001 | 7.7185 |
| Human model -> predict macaque ages | 0.3223 | < 0.001 | 7.9514 |

Key finding: The macaque-trained model consistently predicts human ages with higher correlation than the human-trained model predicts macaque ages, regardless of feature selection strategy. This asymmetry suggests that macaque brain development embeds a developmental program that partially maps onto the more complex human trajectory, but not vice versa.

Fig. 2B: Scatterplot of macaque-model-predicted human ages vs. actual human ages (orange dots).

Fig. 2C: Scatterplot of human-model-predicted macaque ages vs. actual macaque ages (purple dots).

---

## Experiment 3: Brain Age Gap vs. Actual Age Relationship

The absolute brain age gap (|delta brain age|) was computed for cross-species predictions and correlated with actual chronological age.

### Primary analysis (common features)

| Species (predicted by other model) | Relationship with Actual Age | R | P-value | MAE |
|------------------------------------|------------------------------|---|---------|-----|
| Human (predicted by macaque model) | Positive correlation | 0.9828* | 0.001 | 3.3545* |
| Macaque (predicted by human model) | Negative correlation | reported | reported | reported |

*Values from supplement figure 4 (117/239 features); main analysis shows same directional pattern.

### Supplementary (117 macaque, 239 human features)

| Species | R | P-value | MAE |
|---------|---|---------|-----|
| Human predicted by macaque model: |delta brain age| vs. actual age | 0.9828 | 0.001 | 3.3545 |
| Macaque predicted by human model: |delta brain age| vs. actual age | negative trend | reported | reported |

### Supplementary (62 matched features)

| Species | R | P-value | MAE |
|---------|---|---------|-----|
| Human predicted by macaque model: |delta brain age| vs. actual age | 0.9814 | < 0.001 | 2.7123 |
| Macaque predicted by human model: |delta brain age| vs. actual age | negative trend | reported | reported |

Fig. 3A: Positive association between |delta brain age| and actual age in human (predicted by macaque model). Older humans show larger gaps, suggesting accumulating evolutionary divergence through development.

Fig. 3B: Negative association between |delta brain age| and actual age in macaque (predicted by human model). The macaque model from human data becomes less accurate for older macaques.

Fig. Supplement 4: Same patterns replicated with 117/239 features.

Fig. Supplement 5: Same patterns replicated with 62/62 matched features.

---

## Experiment 4: Feature Distribution Analysis

Selected features were categorized by modality parameter (GMV, FA, MD, RD, AD) and by species specificity (human-specific, macaque-specific, common).

| Feature Category | GMV | FA | MD | RD | AD |
|-----------------|-----|----|----|----|----|
| Human-specific | present | present | present | present | present |
| Macaque-specific | present | present | absent | absent | absent |
| Common (both species) | present | present | present | present | present |

Fig. 4A: Bar chart showing the percentage breakdown of macaque-specific, human-specific, and common features across the five MRI parameters. Macaque-specific features are concentrated in FA and GMV only.

Fig. 4B: Top 5 macaque-specific features in gray matter and white matter tracts.

Fig. 4C: Top 5 human-specific features in gray matter and white matter tracts.

Fig. 4D: Top 5 common features shared between species in gray matter and white matter tracts.

---

## Experiment 5: BCAP Correlations with Behavioral Phenotypes

The Brain Cross-species Age Gap (BCAP) index was correlated with behavioral measures collected in HCP-D for human participants.

| Behavioral Test | Direction of Correlation with BCAP | Significance |
|----------------|-----------------------------------|-------------|
| Visual Sensitivity Test | Negative | Significant |
| Picture Vocabulary Test | Positive | Significant |
| BIS/BAS Scale | Not reported as significant | -- |
| Child Behavior Checklist (CBCL) | Not reported as significant | -- |

Fig. 5A: Scatterplots showing individual-level BCAP vs. Visual Sensitivity (negative slope) and BCAP vs. Picture Vocabulary (positive slope). Each dot is one human participant.

Interpretation: Higher BCAP (greater evolutionary divergence) correlates with lower visual sensitivity but higher vocabulary performance, potentially reflecting a trade-off where language-related brain evolution comes at the cost of basic sensory processing.

---

## Experiment 6: BCAP Associations with Brain Anatomy

BCAP values were correlated with individual brain features to identify which structures drive cross-species divergence.

| Feature Domain | Top Positive Associations with BCAP | Top Negative Associations with BCAP |
|---------------|-------------------------------------|-------------------------------------|
| White matter tracts | Top 3 tracts (language-related pathways including arcuate fasciculus regions) | Bottom 3 tracts |
| Gray matter regions | Top 5 regions (higher-order cognitive areas) | Bottom 5 regions |

Fig. 5B: The top 3 and bottom 3 white matter tract features associated with BCAP are displayed (left panel). These tracts are primarily language-related pathways. The top 5 and bottom 5 gray matter features are shown (right panel), highlighting higher-order cognitive regions.

Key finding: BCAP is mainly driven by language-related white matter pathways and higher-order cognitive gray matter areas, consistent with the known disproportionate expansion of these systems in human evolution.

---

## Experiment 7: Sex Effects on Prediction Performance

Models were run separately for male and female participants to check for sex-related differences.

| Sex | Intra-Species Prediction | Cross-Species Prediction | Evolutionary Difference |
|-----|-------------------------|-------------------------|------------------------|
| Male | Significant (p < 0.001) | Significant | No significant sex difference in BCAP |
| Female | Significant (p < 0.001) | Significant | No significant sex difference in BCAP |

Fig. Supplement 3A: Prediction results for males across intra- and inter-species conditions.

Fig. Supplement 3B: Prediction results for females across intra- and inter-species conditions.

Both sexes show the same asymmetric cross-species prediction pattern (macaque model better at predicting human than vice versa).

---

## Comprehensive Prediction Results Summary

| Condition | Feature Set | Direction | R | P-value | MAE |
|-----------|------------|-----------|---|---------|-----|
| Intra-species | 62 mac / 225 hum | Macaque -> Macaque | 0.5729 | < 0.001 | 0.3758 |
| Intra-species | 62 mac / 225 hum | Human -> Human | 0.6153 | < 0.001 | 1.1236 |
| Cross-species | 62 mac / 225 hum | Macaque -> Human | 0.4823 | < 0.001 | 8.3610 |
| Cross-species | 62 mac / 225 hum | Human -> Macaque | 0.2898 | < 0.001 | 7.6157 |
| Intra-species | 117 mac / 239 hum | Macaque -> Macaque | 0.5825 | < 0.001 | 0.3675 |
| Intra-species | 117 mac / 239 hum | Human -> Human | 0.6039 | < 0.001 | 1.1388 |
| Cross-species | 117 mac / 239 hum | Macaque -> Human | 0.4018 | < 0.001 | 7.7185 |
| Cross-species | 117 mac / 239 hum | Human -> Macaque | 0.3223 | < 0.001 | 7.9514 |

---

## Brain Age Gap Regression Summary

| Feature Set | Species Predicted | Relationship | R | P-value | MAE |
|------------|-------------------|-------------|---|---------|-----|
| 117 mac / 239 hum | Human by macaque model | Positive | 0.9828 | 0.001 | 3.3545 |
| 62 mac / 62 hum | Human by macaque model | Positive | 0.9814 | < 0.001 | 2.7123 |
| 117 mac / 239 hum | Macaque by human model | Negative | reported | reported | reported |
| 62 mac / 62 hum | Macaque by human model | Negative | reported | reported | reported |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Flowchart: feature selection via Pearson correlation -> model training -> intra/inter-species prediction -> BCAP computation |
| Fig. 2A | Macaque intra-species prediction scatterplot shows moderate positive correlation (R=0.5729) |
| Fig. 2B | Macaque model predicting human ages shows decent correlation (R=0.4823) |
| Fig. 2C | Human model predicting macaque ages shows weaker correlation (R=0.2898) |
| Fig. 2D | Human intra-species prediction scatterplot shows moderate positive correlation (R=0.6153) |
| Fig. 3A | |delta brain age| positively associated with actual age in humans predicted by macaque model |
| Fig. 3B | |delta brain age| negatively associated with actual age in macaques predicted by human model |
| Fig. 4A | Macaque-specific features restricted to FA and GMV; human-specific features span all five parameters |
| Fig. 5A | BCAP negatively correlated with Visual Sensitivity, positively with Picture Vocabulary |
| Fig. 5B | Language-related white matter tracts and higher-order cognitive gray matter regions most strongly associated with BCAP |
| Fig. S1 | Replicated pattern with 117/239 features |
| Fig. S2 | Replicated pattern with matched 62/62 features |
| Fig. S3 | No significant sex differences in prediction or evolutionary patterns |
| Fig. S4 | Brain age gap vs. actual age replication with 117/239 features |
| Fig. S5 | Brain age gap vs. actual age replication with 62/62 features |

---

## Metrics and Methods Summary

| Analysis Component | Method/Tool |
|-------------------|-------------|
| Feature selection | Pearson correlation (p < 0.01), 100 iterations |
| Age prediction model | SVR or similar regression (not fully specified) |
| Model evaluation | Pearson R, p-value, MAE |
| Cross-species application | Apply model trained in species A to data from species B |
| BCAP computation | Predicted age (cross-species) minus actual age |
| Behavioral correlation | Pearson correlation with HCP-D phenotypes |
| Anatomical association | Correlation of BCAP with individual brain features |
| Image processing | FreeSurfer (sMRI), FSL (dMRI) |
| Parcellation | Desikan-Killiany atlas (gray matter), JHU atlas (white matter tracts) |

---

## Reference Count
69 references cited in the paper.

