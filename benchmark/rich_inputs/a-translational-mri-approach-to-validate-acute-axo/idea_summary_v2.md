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
