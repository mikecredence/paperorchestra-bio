Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

# Idea Summary: Translational MRI Validation of Acute Axonal Damage Detection

## Working title
A translational MRI approach to validate acute axonal damage detection using AxCaliber modeling

## Core question
Can MRI-based axonal diameter estimation (AxCaliber) be validated as a sensitive and specific biomarker for acute axonal damage, and does it reveal diffuse axonal pathology in the normal-appearing white matter of multiple sclerosis patients?

## Motivation / gap
- Axonal degeneration is a central pathological feature driving irreversible disability in neurodegenerative diseases like MS, yet current noninvasive detection methods lack specificity
- Conventional diffusion MRI cannot distinguish axonal damage from other microstructural changes (e.g., demyelination)
- Prior AxCaliber studies in MS (e.g., corpus callosum measurements) lacked independent histological validation
- The original AxCaliber formulation only works in single-fiber-orientation voxels (like corpus callosum), but ~70% of brain voxels have two or more dominant fiber orientations
- Quantitative comparison between MRI and histology is severely hampered by fixation artifacts and other limitations, so a controlled preclinical model is needed
- No existing animal model specifically focuses on isolated axonal damage without confounding demyelination

## Core contribution (bullet form)
- Validated AxCaliber sensitivity to axonal damage using a rat model with ibotenic acid injection: significant increase in mean axonal diameter in injected vs. control fimbria (paired t-test, p=0.003)
- Demonstrated histological correlation: neurofilament fluorescence intensity significantly correlated with MRI-estimated axonal diameter (r=0.54, p=0.029)
- Confirmed axonal specificity: no differences found in myelin content (MBP staining), showing damage was selective to axons while myelin was preserved
- Mapped whole-brain axonal diameter in MS patients using modified AxCaliber, revealing diffuse increases in mean axonal diameter across most NAWM regions
- Showed axonal damage in MS lesions: significantly higher normalized index of asymmetry in MS lesions compared to healthy tissue mapped to the same anatomical regions
- Found negative association between axonal diameter and disease duration, suggesting early swelling followed by axonal loss

## Method in brief
The preclinical arm used n=9 rats receiving unilateral stereotaxic injection of ibotenic acid (2.5 ug/uL, 1 uL) into the right dorsal hippocampus, with saline injection in the contralateral hemisphere as internal control. Ibotenic acid is a selective NMDA receptor agonist causing neurotoxic death of neuronal somas, which translates to Wallerian-like axonal degeneration in the fimbria (the hippocampus's major output bundle). Fourteen days post-surgery, rats underwent AxCaliber MRI protocol followed by perfusion and immunohistochemical analysis using NeuN (neuronal somas), neurofilament (axonal integrity), and MBP (myelination) staining.

The clinical arm applied the same AxCaliber protocol to 10 relapsing-remitting MS patients (age 27-59, 7 females) and 6 age-matched healthy controls (age 23-53, 3 females). Whole-brain axonal diameter mapping was performed using a modified AxCaliber model capable of handling crossing-fiber voxels. Tract-based spatial statistics (TBSS) compared NAWM axonal diameter between groups. For lesion analysis, a normalized index of asymmetry (NIA) was computed between lesion voxels and contralateral NAWM in MS patients, and compared to the same anatomical regions in healthy controls.

AxCaliber is a multicompartment diffusion MRI model that estimates axonal diameter distributions from the diffusion-weighted signal acquired at multiple b-values and diffusion times. The model separates intra-axonal from extra-axonal water compartments, enabling estimation of mean axonal caliber. The whole-brain extension overcomes the single-fiber-orientation limitation by incorporating fiber orientation distributions.

## Target venue
eLife


## Experimental Log

# Experimental Log: Translational MRI Validation of Acute Axonal Damage Detection

> Data tables and results extracted from full-text analysis

---

## Study Design Overview

| Parameter | Preclinical Arm | Clinical Arm |
|---|---|---|
| Subjects | n=9 rats | 10 MS patients, 6 healthy controls |
| Model/Pathology | Ibotenic acid injection (hippocampus) | Relapsing-remitting MS |
| Target structure | Fimbria (axonal output of hippocampus) | Whole-brain white matter |
| MRI protocol | AxCaliber | AxCaliber (clinical version) |
| Control | Contralateral saline injection | Age-matched healthy volunteers |
| Post-processing | DTI tractography of fimbria | TBSS, lesion ROI analysis |
| Histological validation | NeuN, neurofilament, MBP staining | N/A |

---

## Experiment 1: Preclinical Rat Model of Acute Axonal Damage

### Injection Parameters

| Parameter | Value |
|---|---|
| Neurotoxin | Ibotenic acid (NMDA receptor agonist) |
| Concentration | 2.5 ug/uL |
| Volume | 1 uL |
| Injection site | Right dorsal hippocampus |
| Coordinates | Bregma -3.8 mm, sup-inf 3.0 mm, 2 mm from midline |
| Control injection | Saline (contralateral hemisphere) |
| Survival time post-injection | 14 days |
| Sample size | n=9 rats |

### MRI Results: Mean Axonal Diameter (Fimbria)

| Measure | Injected Hemisphere | Control Hemisphere | p-value | Test |
|---|---|---|---|---|
| Mean axonal diameter | Significantly increased | Baseline | 0.003 | Paired t-test |

### Repeated-Measures ANOVA Along Fimbria Tract

| Factor | F-statistic | df | p-value |
|---|---|---|---|
| Injection (injected vs control) | F=19.5 | 1,7 | 0.003 |
| Position along tract | F=219.5 | 98,686 | <0.001 |
| Injection x Position interaction | F=11.2 | 98,686 | 0.012 |

- The tract was divided into 100 steps along the antero-posterior axis
- Significant differences in mean axonal diameter between injected and control tracts were primarily localized posterior to the injection site (Fig. 1d)
- Fig. 1b shows tractography of the fimbria with axonal diameter color-coded along the tract
- Fig. 1c shows a significant increase in mean axonal diameter for the ibotenic acid-injected fimbria compared to control

### Immunohistochemistry Results

| Stain | Target | Injected vs Control | p-value | Test |
|---|---|---|---|---|
| NeuN | Neuronal somas (hippocampus) | Lower intensity (neuronal loss) | 0.026 | Paired t-test |
| Neurofilament | Axonal integrity (fimbria) | Higher intensity (axonal damage) | 0.047 | Paired t-test |
| MBP | Myelin basic protein (fimbria) | No significant difference | NS | Paired t-test |

- Fig. 2a-b: NeuN staining confirmed neuronal loss in injected hippocampi
- Fig. 2c-d: Neurofilament staining confirmed axonal damage in injected fimbria
- Fig. S1: No significant differences in myelination (MBP staining), indicating axonal damage occurred before myelin breakdown at this time point

### MRI-Histology Correlation

| Comparison | Correlation coefficient (r) | p-value |
|---|---|---|
| Neurofilament intensity vs. MRI axonal diameter | 0.54 | 0.029 |

- Fig. 3 shows a significant positive correlation between neurofilament fluorescence intensity and AxCaliber-estimated axonal diameter across both injected (ibotenic acid) and control (saline) fimbrias
- This correlation validates that MRI-based axonal diameter estimation reflects actual underlying axonal morphological changes

---

## Experiment 2: Clinical MS Study

### Cohort Demographics

| Characteristic | MS Patients | Healthy Controls | p-value |
|---|---|---|---|
| N | 10 | 6 | - |
| Age range | 27-59 years | 23-53 years | 0.093 (Mann-Whitney) |
| Sex (female) | 7/10 | 3/6 | - |

### TBSS Analysis: NAWM Axonal Diameter

| Comparison | Finding | Significance |
|---|---|---|
| MS NAWM vs Control WM | Higher axonal diameter in MS | p<0.05 (corrected) |
| Control WM vs MS NAWM | Not significant | NS |

- Fig. 4 shows TBSS results with widespread, mostly symmetrical increases in axonal diameter in MS NAWM
- Affected tracts include: corpus callosum, internal capsule, corona radiata, thalamic radiation, inferior longitudinal fasciculus, cingulum, fornix, superior longitudinal fasciculus, inferior fronto-occipital fasciculus, uncinate fasciculus, and tapetum

### White Matter Tracts with Elevated Axonal Diameter in MS

| Tract | Elevated in MS NAWM |
|---|---|
| Corpus callosum | Yes |
| Internal capsule | Yes |
| Corona radiata | Yes |
| Thalamic radiation | Yes |
| Inferior longitudinal fasciculus | Yes |
| Cingulum | Yes |
| Fornix | Yes |
| Superior longitudinal fasciculus | Yes |
| Inferior fronto-occipital fasciculus | Yes |
| Uncinate fasciculus | Yes |
| Tapetum | Yes |

### Lesion Analysis: Normalized Index of Asymmetry (NIA)

| Group | NIA (Lesion vs Contralateral) | Significance |
|---|---|---|
| MS patients | Significantly elevated | p < significance threshold |
| Healthy controls (same anatomical region) | Not elevated | Reference |

- Fig. 5a: Example of lesion and contralateral masks overlaid on FA map
- Fig. 5b: Lesion mask in MNI space used to extract mean axonal diameter in healthy cohort for same anatomical region
- Fig. 5c: NIA for mean axonal diameter shows significant elevation in MS lesions vs contralateral tissue

### Disease Duration Association

| Measure | Association with Disease Duration | Direction |
|---|---|---|
| Axonal diameter (TBSS) | Negative | Higher diameter early, decreasing over time |
| Axonal diameter (ROI-based) | Negative | Same pattern |

- Fig. S2a: TBSS analysis showing negative correlation between axonal diameter and disease duration
- Fig. S2b-c: ROI-based analyses confirming the same negative association
- Interpretation: early axonal swelling (varicosities/spheroids) followed by progressive loss of swollen axons

---

## Key Methodological Notes

### AxCaliber MRI Protocol Parameters

| Parameter | Detail |
|---|---|
| Model type | Multicompartment diffusion model |
| Key output | Mean axonal diameter (caliber) |
| Advantage over DTI | Specific to intra-axonal compartment |
| Whole-brain capability | Modified model handles crossing-fiber voxels |
| Prior limitation | Original only worked for single-fiber voxels (~30% of brain) |

### Preclinical MRI and Histology Workflow

| Step | Timing |
|---|---|
| Stereotaxic injection | Day 0 |
| MRI scan (AxCaliber protocol) | Day 14 |
| Perfusion and tissue collection | Immediately after MRI |
| Histological staining | Post-perfusion |
| Stains applied | NeuN, neurofilament, MBP |

---

## Statistical Methods Summary

| Analysis | Test Used | Context |
|---|---|---|
| Injected vs control axonal diameter | Paired t-test | Preclinical fimbria comparison |
| Along-tract analysis | Repeated-measures ANOVA with post-hoc t-tests | Position x injection interaction |
| Multiple comparisons correction | Post-hoc correction | Tract location comparisons |
| NeuN intensity comparison | Paired t-test | Hippocampal neuronal loss |
| Neurofilament intensity comparison | Paired t-test | Fimbria axonal damage |
| MRI-histology correlation | Pearson correlation | Neurofilament vs axonal diameter |
| Age comparison (MS vs control) | Mann-Whitney test | Cohort matching |
| TBSS group comparison | Nonparametric permutation | Whole-brain NAWM |
| Disease duration association | Correlation/regression | TBSS and ROI-based |

---

## Neuropathological Context

| Feature | Observation |
|---|---|
| Varicosities/spheroids | Enlarge axonal diameter, impair transport |
| Small axon vulnerability | Smaller axons lost earlier, biasing mean diameter upward |
| Myelin preservation | At 14 days post-injection, myelin still intact despite axonal damage |
| NAWM changes | Histological alterations in axonal morphology observed even without myelin/inflammatory abnormalities |
| Axon-myelin imbalance | May be a primary event in MS pathogenesis |

---

## Figure Summary

| Figure | Content |
|---|---|
| Fig. 1a | Experimental scheme of stereotaxic injections |
| Fig. 1b | Tractography of fimbria with axonal diameter color coding |
| Fig. 1c | Mean axonal diameter: injected vs control fimbria (p<0.01) |
| Fig. 1d | Along-tract axonal diameter profiles with injection site marked |
| Fig. 2a-b | NeuN staining and quantification in hippocampi |
| Fig. 2c-d | Neurofilament staining and quantification in fimbria |
| Fig. 3 | Correlation plot: neurofilament vs MRI axonal diameter (r=0.54) |
| Fig. 4 | TBSS map of increased axonal diameter in MS NAWM |
| Fig. 5 | Lesion NIA analysis for axonal diameter |
| Fig. S1 | MBP staining: no myelin differences |
| Fig. S2 | Negative association between axonal diameter and disease duration |

---

## Datasets and Metrics

| Dataset/Metric | Description |
|---|---|
| Preclinical MRI | AxCaliber protocol on n=9 rats, bilateral fimbria |
| Clinical MRI | AxCaliber protocol on 10 MS + 6 controls |
| NeuN intensity | Quantification of neuronal somas in hippocampus |
| Neurofilament intensity | Quantification of axonal integrity in fimbria |
| MBP intensity | Quantification of myelination in fimbria |
| Mean axonal diameter | Primary MRI output from AxCaliber model |
| TBSS skeleton | White matter skeleton for voxelwise group comparison |
| NIA | Normalized index of asymmetry between lesion and contralateral tissue |
| Robinson-Foulds distance | Not applicable to this study |
| EDSS | Expanded Disability Status Scale (MS clinical measure, Table 1) |
| SDMT | Symbol Digit Modalities Test (cognitive measure, Table 1) |

