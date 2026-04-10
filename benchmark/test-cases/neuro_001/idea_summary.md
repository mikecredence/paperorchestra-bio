## Working title

Multimodal Precision Neuroimaging of the Individual Human Brain at Ultra-High Fields (7T)

## Core question

Can we build a comprehensive, publicly available multimodal 7T MRI dataset with sufficient depth per individual to enable precision mapping of brain structure, function, and connectivity at the single-subject level?

## Motivation / gap

- Multimodal MRI allows non-invasive examination of brain structure and function, but most datasets average across many subjects, obscuring individual-level detail
- Precision neuroimaging aims to map individual brains with high fidelity, but few datasets provide the depth of acquisition needed
- 7T (ultra-high field) MRI offers higher SNR and spatial resolution, but comprehensive multimodal 7T datasets are scarce
- No existing resource combines T1 relaxometry, MT imaging, T2*-weighted imaging, diffusion MRI, and multi-state fMRI at 7T with per-subject connectomes and gradients

## Core contribution

- A multimodal Precision Neuroimaging and Connectomics (PNI) 7T MRI dataset
- 10 healthy individuals scanned across 3 sessions each with a comprehensive protocol
- Modalities: T1 relaxometry, magnetization transfer imaging, T2*-weighted imaging, diffusion MRI, multi-state functional MRI
- Release of cortex-wide connectomes from different modalities at multiple parcellation scales
- Release of connectivity "gradients" for dimensionality-reduced connectome representations
- Anonymized raw data plus processed derivatives

## Method in brief

Ten healthy participants will undergo three 7T MRI sessions each. Each session includes: (1) T1 relaxometry (MP2RAGE), (2) magnetization transfer imaging, (3) T2*-weighted imaging, (4) high-resolution diffusion MRI, and (5) multi-state fMRI (resting-state plus task paradigms). Data will be processed with standard pipelines (FreeSurfer, FSL, MRtrix3). Cortex-wide connectomes will be computed per modality at multiple parcellation scales (e.g., Schaefer 100-1000). Gradient decomposition (diffusion map embedding) will be applied to connectomes.

## Target venue

Unknown (data descriptor)
