# Experimental Log -- osl-dynamics: Toolbox for Modeling Fast Dynamic Brain Activity

## 2024-01-10 -- Toolbox architecture and supported modalities

| Component | Description |
|-----------|-------------|
| Language | Python (PyTorch backend) |
| Supported modalities | MEG, EEG, fMRI, LFP, ECoG |
| Core models | TDE-HMM, DyNeMo |
| Preprocessing | Source reconstruction, parcellation, sign-flipping |
| Post-hoc analysis | Multitaper spectral estimation, power/coherence maps |
| Package name | osl-dynamics (pip installable) |
| License | Open source |

## 2024-02-01 -- TDE-HMM resting-state MEG analysis (CTF dataset)

Three-state TDE-HMM applied to resting-state MEG data for data-driven oscillatory burst detection.

| Parameter | Value |
|-----------|-------|
| Dataset | CTF resting-state MEG |
| Number of subjects | 51 |
| Sampling rate (Hz) | 250 |
| Number of parcels | 38 (Glasser parcellation) |
| Time-delay embedding lags | 15 |
| Number of HMM states | 3 |
| Training method | Expectation-maximization (Baum-Welch) |
| State lifetime range (ms) | 50 - 400 |
| Mean state lifetime (ms) | 150 |

### Burst detection results (TDE-HMM state properties)

| State | Dominant frequency (Hz) | Peak brain region | Mean fractional occupancy | Mean lifetime (ms) |
|-------|------------------------|-------------------|--------------------------|-------------------|
| State 1 (alpha) | 8 - 12 | Occipital cortex | 0.38 | 180 |
| State 2 (beta) | 15 - 25 | Sensorimotor cortex | 0.32 | 140 |
| State 3 (broadband) | 2 - 40 | Distributed | 0.30 | 120 |

The HMM automatically detects alpha and beta oscillatory bursts without specifying target frequencies, amplitude thresholds, or burst duration criteria a priori.

## 2024-03-01 -- DyNeMo resting-state MEG analysis

Dynamic Network Modes model applied to same CTF resting-state dataset.

| Parameter | Value |
|-----------|-------|
| Number of modes | 6 |
| RNN hidden units | 64 |
| Inference method | Stochastic variational inference |
| Learning rate | 0.001 |
| Training epochs | 40 |
| Batch size | 64 sequences |
| KL annealing epochs | 10 |

### DyNeMo mode properties

| Mode | Dominant frequency band | Key brain regions | Mean mixing coefficient |
|------|------------------------|-------------------|------------------------|
| Mode 1 | Alpha (8-12 Hz) | Visual cortex | 0.22 |
| Mode 2 | Beta (15-25 Hz) | Motor cortex | 0.18 |
| Mode 3 | Theta (4-8 Hz) | Frontal, temporal | 0.16 |
| Mode 4 | Alpha-beta | Parietal | 0.15 |
| Mode 5 | Gamma (30-45 Hz) | Somatosensory | 0.14 |
| Mode 6 | Low-frequency (1-4 Hz) | Default mode | 0.15 |

DyNeMo allows multiple modes to be simultaneously active, capturing richer dynamics than the mutually exclusive HMM states.

## 2024-03-20 -- Task MEG analysis (Elekta dataset, motor task)

| Parameter | Value |
|-----------|-------|
| Dataset | Elekta task MEG (motor execution) |
| Number of subjects | 10 |
| Task | Button press (left/right hand) |
| HMM states | 4 |
| Temporal resolution | 4 ms (250 Hz) |

### Task-evoked state dynamics

| State | Pre-movement occupancy | Post-movement occupancy | Laterality index | Frequency |
|-------|----------------------|------------------------|-------------------|-----------|
| Beta desync (contra) | 0.42 | 0.15 | 0.68 | 15-25 Hz |
| Beta rebound (contra) | 0.18 | 0.48 | 0.72 | 18-28 Hz |
| Alpha state | 0.25 | 0.22 | 0.12 | 8-12 Hz |
| Broadband | 0.15 | 0.15 | 0.08 | 2-40 Hz |

The TDE-HMM captures the classic beta desynchronization before movement and post-movement beta rebound in contralateral sensorimotor cortex on a single-trial basis.

## 2024-04-10 -- Computational benchmarks

| Metric | TDE-HMM | DyNeMo |
|--------|---------|--------|
| Training time (51 subjects, 3 states/modes) | 12 min | 45 min |
| Memory usage (GB) | 2.1 | 4.8 |
| GPU acceleration supported | No | Yes |
| Inference per subject (ms) | 200 | 800 |
| Log-likelihood convergence epochs | 25 | 35 |

## Ground Truth Reference

- bioRxiv DOI: 10.1101/2023.08.07.549346
- Published DOI: 10.7554/eLife.91949
- Venue: eLife
- Year: 2024
