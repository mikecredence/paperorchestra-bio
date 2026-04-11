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
