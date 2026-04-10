# Experimental Log -- Precision Neuroimaging and Connectomics (PNI) 7T Dataset

## 2024-01-10 -- Study design

| Parameter | Value |
|---|---|
| Participants | 10 healthy individuals |
| Scanner field strength | 7 Tesla (ultra-high field) |
| Sessions per participant | 3 |
| Total scanning sessions | 30 |

## 2024-02-01 -- MRI protocol per session

| Modality | Sequence | Purpose |
|---|---|---|
| T1 relaxometry | MP2RAGE | Quantitative T1 mapping, cortical segmentation |
| Magnetization transfer (MT) imaging | MT-prepared GRE | Myelin-sensitive contrast |
| T2*-weighted imaging | Multi-echo GRE | Iron/susceptibility mapping |
| Diffusion MRI | High-resolution multi-shell | White matter tractography, structural connectivity |
| Functional MRI (resting state) | Multi-band EPI | Resting-state functional connectivity |
| Functional MRI (task) | Multi-band EPI | Task-evoked functional connectivity |

## 2024-03-01 -- Data acquisition summary

| Metric | Value |
|---|---|
| Total participants completed | 10 |
| Total sessions completed | 30 |
| Average session duration | ~2-3 hours |
| Data quality (% usable runs) | >95% |

## 2024-03-15 -- Connectome derivation

| Parcellation | Scales | Modalities |
|---|---|---|
| Schaefer atlas | 100, 200, 400, 1000 parcels | All |
| Connectome types | Structural (dMRI tractography), Functional (rs-fMRI correlation), Task-functional | -- |

| Derivative | Description |
|---|---|
| Cortex-wide connectomes | Per-subject, per-modality, per-parcellation |
| Gradients | Diffusion map embedding of connectomes |

## 2024-04-01 -- Data release contents

| Component | Format | Anonymized |
|---|---|---|
| Raw MRI data | NIfTI (BIDS format) | Yes (defaced) |
| Processed connectomes | CSV / .mat | Yes |
| Gradient maps | Surface files (GIFTI) | Yes |
| Code / pipelines | GitHub repository | -- |

## 2024-04-05 -- Quality metrics (representative)

| Modality | SNR improvement vs 3T | Spatial resolution achieved |
|---|---|---|
| T1 relaxometry | ~1.5-2x | Sub-millimeter (0.7 mm iso) |
| Diffusion MRI | ~1.5x | 1.05 mm iso |
| Functional MRI | ~1.5x | 1.2 mm iso |

7T provides clear SNR and resolution gains enabling precision individual-level mapping.

## Summary

The PNI dataset provides a comprehensive 7T multimodal resource for 10 individuals (3 sessions each), with raw data and derived connectomes/gradients across multiple parcellation scales. Enables precision neuroimaging research at the single-subject level.
