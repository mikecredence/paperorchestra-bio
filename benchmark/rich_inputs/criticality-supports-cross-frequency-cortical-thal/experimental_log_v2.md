# Experimental Log: Criticality and Cross-Frequency Cortical-Thalamic Information Transfer

## Overview

Multi-species study examining spectrally-resolved directed information transfer between cortex and thalamus during waking, anesthesia, seizure, and psychedelic states. Combines empirical electrophysiology with mean-field computational modeling to link edge-of-chaos criticality to cross-frequency communication.

---

## Species and Recording Sites

### Table 1: Electrophysiology Recording Details

| Species / Strain | Thalamic Nucleus | Cortical Region | Connection Type | Brain States Recorded |
|-----------------|-----------------|-----------------|-----------------|----------------------|
| Human (ET patients) | Ventral intermediate (Vim) | Ipsilateral sensorimotor cortex | Direct reciprocal | Waking, Propofol anesthesia |
| Long-Evans rats | Ventral posterior | Ipsilateral somatosensory cortex | Direct reciprocal | Waking, Propofol anesthesia |
| C57/BL6 mice | Mediodorsal | Medial prefrontal cortex | Direct reciprocal | Waking, 5-MeO-DMT |
| GAERS rats | Ventral posterior | Contralateral somatosensory cortex | Indirect (via ipsilateral S1) | Waking, Spike-and-wave seizures |

---

## Spectral Analysis Parameters

### Table 2: Frequency Bands of Interest

| Band Label | Frequency Range (Hz) | Role in Analysis |
|-----------|---------------------|------------------|
| Delta/Theta/Alpha (low-frequency sender) | 1.625-13 | Source frequency for cross-frequency transfer |
| High Gamma (receiver) | 52-104 | Target frequency for cross-frequency transfer |
| Full exploratory sweep | All possible pairs | Initial sweep across all frequency combinations |

### Table 3: Information Transfer Measurement Parameters

| Parameter | Value |
|-----------|-------|
| Method | Spectrally resolved directed transfer entropy |
| Window length | 10 seconds per trial |
| Significance testing | Surrogate time-series based |
| Surrogate approach | Randomization of dynamics within specific frequency ranges |
| Metric unit | Bits of transfer entropy lost |
| Statistical test for state comparisons | One-tailed Wilcoxon signed-rank test |

---

## Initial Exploratory Sweep (Fig 2)

### Table 4: Exploratory Sweep Design

| Parameter | Value |
|-----------|-------|
| Frequency pairs evaluated | All possible spectral combinations |
| Z-scoring | Applied per trial, per subject |
| Averaging | Across all 10-s windows per subject, then across subjects |
| Species pooled | All four (humans, Long-Evans rats, C57/BL6 mice, GAERS rats) |
| Direction | Both cortex-to-thalamus and thalamus-to-cortex |
| Note on surrogate testing | Insufficient surrogates for significance at this stage (computational cost) |

Fig 2 shows the z-scored information transfer strength across all frequency-band pairs during waking states. A prominent motif of low-to-high frequency bidirectional communication was visible in nearly all subjects and species.

---

## Surrogate-Tested Cross-Frequency Information Transfer (Table 1 in paper)

### Table 5: Significance of Cross-Frequency Transfer (Low ~1.5-13 Hz to High ~52-104 Hz)

| Species | Direction | Condition | Surrogate Test Result | Notes |
|---------|-----------|-----------|----------------------|-------|
| Human ET patients | Cortex -> Thalamus | Waking | Significant | Per 10-s window p-values |
| Human ET patients | Thalamus -> Cortex | Waking | Significant | Per 10-s window p-values |
| Long-Evans rats | Cortex -> Thalamus | Waking | Significant | Direct connections |
| Long-Evans rats | Thalamus -> Cortex | Waking | Significant | Direct connections |
| C57/BL6 mice | Cortex -> Thalamus | Waking | Significant | MD thalamus / mPFC |
| C57/BL6 mice | Thalamus -> Cortex | Waking | Significant | MD thalamus / mPFC |
| GAERS rats | Cortex -> Thalamus | Waking | Significant | Indirect connection |
| GAERS rats | Thalamus -> Cortex | Waking | Significant | Indirect connection |

---

## Effect of Brain State on Cross-Frequency Information Transfer

### Table 6: Cortex-to-Thalamus Cross-Frequency Transfer Across Brain States

| Comparison | Species | Direction | Effect | Statistical Test | Significance |
|-----------|---------|-----------|--------|-----------------|-------------|
| Waking vs Propofol | Human ET patients | Ctx -> Thal | Reduced | Wilcoxon signed-rank (one-tailed) | Significant |
| Waking vs Propofol | Long-Evans rats | Ctx -> Thal | Reduced | Wilcoxon signed-rank (one-tailed) | Significant |
| Waking vs Seizure | GAERS rats | Ctx -> Thal | Reduced | Wilcoxon signed-rank (one-tailed) | Significant |
| Waking vs 5-MeO-DMT | C57/BL6 mice | Ctx -> Thal | Enhanced | Wilcoxon signed-rank (one-tailed) | Significant |

Fig 3A-B: Propofol anesthesia significantly reduced cortex-to-thalamus low-to-high frequency information transfer in both humans and rats.
Fig 3C: Generalized spike-and-wave seizures significantly reduced cortex-to-thalamus cross-frequency transfer in GAERS rats.
Fig 3D: 5-MeO-DMT significantly enhanced cortex-to-thalamus cross-frequency transfer in mice.

### Table 7: Thalamus-to-Cortex Cross-Frequency Transfer Across Brain States

| Comparison | Species | Direction | Effect | Statistical Test | Significance |
|-----------|---------|-----------|--------|-----------------|-------------|
| Waking vs Propofol | Human ET patients | Thal -> Ctx | Reduced | Wilcoxon signed-rank (one-tailed) | Significant |
| Waking vs Propofol | Long-Evans rats | Thal -> Ctx | Reduced | Wilcoxon signed-rank (one-tailed) | Significant |
| Waking vs Seizure | GAERS rats | Thal -> Ctx | Reduced | Wilcoxon signed-rank (one-tailed) | Significant |
| Waking vs 5-MeO-DMT | C57/BL6 mice | Thal -> Ctx | Not significantly enhanced | Wilcoxon signed-rank (one-tailed) | Not significant |

Fig 5A-B: Thalamus-to-cortex low-to-high frequency transfer was reduced during propofol anesthesia.
Fig 5C: Thalamus-to-cortex transfer reduced during seizures.
Note: Unlike cortex-to-thalamus, the psychedelic condition did not significantly increase thalamus-to-cortex transfer (n=5 animals, possibly underpowered).

---

## Control Analyses

### Table 8: Non-Spectrally-Resolved Transfer Entropy Results

| Comparison | Species | Direction | Consistent with Consciousness? | Significance |
|-----------|---------|-----------|-------------------------------|-------------|
| Waking vs Propofol | Human ET | Ctx -> Thal | No consistent relationship | Varied |
| Waking vs Propofol | Long-Evans rats | Ctx -> Thal | No consistent relationship | Varied |
| Waking vs Seizure | GAERS rats | Ctx -> Thal | No consistent relationship | Varied |
| Waking vs 5-MeO-DMT | C57/BL6 mice | Ctx -> Thal | No consistent relationship | Varied |

Fig 3-supplement 1: Broadband (non-spectrally resolved) transfer entropy from cortex to thalamus showed no consistent pattern across brain states. Used JIDT implementation of Kraskov et al. kernel estimation with Kozachenko-Leonenko log-probability estimators, K nearest neighbors, bias correction, embedded Schreiber history length k=1.

### Table 9: Phase-Amplitude Coupling (Modulation Index) Results

| Comparison | Species | Direction | Consistent with Consciousness? | Significance |
|-----------|---------|-----------|-------------------------------|-------------|
| Waking vs Propofol | Human ET | Ctx -> Thal | No consistent relationship | Varied |
| Waking vs Propofol | Long-Evans rats | Ctx -> Thal | No consistent relationship | Varied |
| Waking vs Seizure | GAERS rats | Ctx -> Thal | No consistent relationship | Varied |
| Waking vs 5-MeO-DMT | C57/BL6 mice | Ctx -> Thal | No consistent relationship | Varied |

Fig 3-supplement 2: Cross-frequency phase-amplitude coupling (PAC) from cortex to thalamus using the modulation index (MI) between phase of 1.625-13 Hz activity and amplitude of 52-104 Hz activity. MI is a bivariate measure calculated between pairs of univariate channels. No consistent relationship with consciousness was observed.

Fig 5-supplement 1: Broadband transfer entropy (thalamus-to-cortex) also showed no consistent consciousness-related pattern.
Fig 5-supplement 2: PAC (thalamus-to-cortex) also showed no consistent consciousness-related pattern.

---

## Power Spectral Density Analysis (Fig 4)

### Table 10: Spectral Power Changes Across Brain States

| Brain State Manipulation | Slow/Delta Power (<=4 Hz) | High-Frequency Power (>80 Hz) | Cross-Freq Transfer |
|-------------------------|--------------------------|------------------------------|---------------------|
| Propofol (vs waking) | Increased | Decreased | Decreased |
| 5-MeO-DMT (vs waking) | Increased | Decreased | Increased (Ctx->Thal) |
| Seizure (vs waking) | Altered | Altered | Decreased |

Fig 4 shows median power spectral densities (Welch's method) for all brain states. Key observation: both propofol and 5-MeO-DMT increased slow/delta power and decreased high-frequency power (>80 Hz) in both cortex and thalamus, yet had OPPOSING effects on cross-frequency information transfer. This dissociation rules out simple spectral power explanations.

---

## Computational Model

### Table 11: Mean-Field Model Components

| Component | Description |
|-----------|-------------|
| Model type | Modified van Albada-Robinson mean-field model |
| System modeled | Basal ganglia-thalamocortical system |
| Populations | Multiple neural populations (cortical, thalamic, basal ganglia) |
| Firing rate function | Sigmoidal: Q_a = Q_max / (1 + exp(-(V_a - theta)/sigma')) |
| Q_max | Maximum possible firing rate per population |
| sigma' | Standard deviation of cell body potentials relative to threshold |
| Membrane potential dynamics | dV_a/dt depends on synaptic weights v_ab, incoming pulse rates phi_b, delays tau_ab |
| Synaptic response kernel | Modified to decouple duration from peak amplitude |
| Anesthesia simulation | Modulation of synaptic decay rate alpha (prolonged inhibition duration without changing peak chloride current) |
| Optimization | Bayesian-genetic optimization to match empirical waking electrodynamics |

### Table 12: Key Model Equations and Parameters

| Equation | Description | Key Variables |
|----------|-------------|---------------|
| Q_a(r,t) = Q_max * S(V_a - theta) | Population firing rate | Q_max, V_a, theta, sigma' |
| dV_a/dt = sum_b(v_ab * phi_b(t - tau_ab)) | Membrane potential dynamics | v_ab (synaptic weight), phi_b (pulse rate), tau_ab (delay) |
| D_alpha_beta = (1/alpha*beta) * d^2/dt^2 + (1/alpha + 1/beta) * d/dt + 1 | Differential operator | alpha (decay rate), beta (rise rate) |
| h (modified) | Synaptic response decoupled from peak | Alpha modulation for anesthesia |

### Table 13: Model Validation and Optimization

| Aspect | Details |
|--------|---------|
| Optimization method | Bayesian-genetic |
| Target | Match diverse aspects of real waking-state neural electrodynamics |
| Biological realism | Biologically realistic parameters |
| Criticality measure | Lyapunov exponent (edge-of-chaos = transition from stability to chaos) |
| Anesthesia simulation | GABAergic modulation of synaptic decay |
| Seizure simulation | Parameter adjustments to generate spike-and-wave patterns |

Fig 6-supplement 1 depicts the Bayesian-genetic optimization workflow for deriving awake-state model parameters.

---

## Edge-of-Chaos Criticality Results

### Table 14: Criticality and Cross-Frequency Transfer Relationship

| Brain State | Proximity to Edge-of-Chaos | Cross-Frequency Transfer | Direction from Critical Point |
|------------|---------------------------|-------------------------|------------------------------|
| Waking | Near critical point | High | Normal operating regime (slightly chaotic side) |
| Propofol anesthesia | Diverged from critical point | Reduced | Away from edge |
| Seizure | Diverged from critical point | Reduced | Away from edge (periodic side) |
| 5-MeO-DMT (psychedelic) | Tuned closer to critical point | Enhanced (Ctx->Thal) | Approaches from chaotic side |

The model predicts that slow thalamocortical electrodynamics near the edge-of-chaos phase transition maximize cross-frequency information transfer. Unconsciousness shifts dynamics away from this critical point (either toward periodic or deeply chaotic regimes), reducing transfer. Psychedelics tune dynamics closer to criticality from the chaotic side.

---

## Summary of Key Statistical Tests

### Table 15: Statistical Framework

| Test | Application | Threshold |
|------|------------|-----------|
| Surrogate time-series testing | Significance of spectral information transfer per window | p-value per 10-s window |
| One-tailed Wilcoxon signed-rank test | Cross-state comparisons within species | *p<0.05, **p<0.01, ***p<0.001 |

### Table 16: Significance Summary Across All Comparisons

| Analysis | Ctx->Thal (Unconscious) | Thal->Ctx (Unconscious) | Ctx->Thal (Psychedelic) | Thal->Ctx (Psychedelic) |
|----------|------------------------|------------------------|------------------------|------------------------|
| Cross-freq spectral TE | Significant decrease | Significant decrease | Significant increase | Not significant |
| Broadband TE | No consistent pattern | No consistent pattern | No consistent pattern | No consistent pattern |
| Phase-amplitude coupling | No consistent pattern | No consistent pattern | No consistent pattern | No consistent pattern |

---

## Datasets and External Tools

### Table 17: Software and Analysis Tools

| Tool / Resource | Purpose |
|----------------|---------|
| Java Information Dynamics Toolkit (JIDT) | Broadband transfer entropy estimation |
| Kraskov et al. method | Kernel-based probability distribution estimation |
| Kozachenko-Leonenko estimator | Log-probability estimation via nearest-neighbor counting |
| Welch's method | Power spectral density estimation |
| Modulation index (MI) | Phase-amplitude coupling quantification |
| Bayesian-genetic optimization | Model parameter fitting |
| Lyapunov exponent | Edge-of-chaos criticality quantification |

---

## Reference Count
112 references cited in the paper.
