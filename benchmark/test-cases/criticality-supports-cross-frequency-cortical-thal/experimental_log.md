# Experimental Log -- Criticality and corticothalamic cross-frequency communication

## 2024-01-18 -- Cross-frequency transfer entropy: cortex -> thalamus (conscious baseline)

Transfer entropy (TE) from cortical delta/theta (1.5-13 Hz) to thalamic high-gamma (50-100 Hz), measured across species.

| Species | n | TE (bits, mean +/- SEM) | Significance (p) |
|---------|---|------------------------|-----------------|
| Human (awake) | 12 | 0.045 +/- 0.006 | <0.001 |
| Mouse (awake) | 18 | 0.038 +/- 0.004 | <0.001 |
| Rat (awake) | 15 | 0.041 +/- 0.005 | <0.001 |

Consistent cross-frequency cortex-to-thalamus information transfer across all three species.

## 2024-02-05 -- Thalamus -> cortex (reverse direction)

Transfer entropy from thalamic delta/theta to cortical high-gamma.

| Species | n | TE (bits, mean +/- SEM) | Significance (p) |
|---------|---|------------------------|-----------------|
| Human (awake) | 12 | 0.039 +/- 0.005 | <0.001 |
| Mouse (awake) | 18 | 0.032 +/- 0.004 | <0.001 |
| Rat (awake) | 15 | 0.035 +/- 0.005 | <0.001 |

Bidirectional cross-frequency communication confirmed in all species.

## 2024-02-22 -- Effect of propofol anesthesia (mice)

| Condition | Cortex->Thalamus TE (bits) | Thalamus->Cortex TE (bits) | % reduction vs awake |
|-----------|--------------------------|--------------------------|---------------------|
| Awake | 0.038 | 0.032 | -- |
| Light propofol | 0.025 | 0.020 | ~35% |
| Deep propofol (LOC) | 0.012 | 0.009 | ~70% |
| Recovery | 0.034 | 0.028 | ~12% |

Cross-frequency communication is dose-dependently diminished by propofol, with ~70% reduction at loss of consciousness.

## 2024-03-10 -- Effect of generalized spike-and-wave seizures (rats)

| Condition | Cortex->Thalamus TE (bits) | Thalamus->Cortex TE (bits) |
|-----------|--------------------------|--------------------------|
| Pre-ictal baseline | 0.041 | 0.035 |
| During spike-wave seizure | 0.010 | 0.008 |
| Post-ictal | 0.030 | 0.025 |

Seizure-associated unconsciousness also disrupts corticothalamic cross-frequency transfer.

## 2024-03-28 -- Psychedelic state: 5-MeO-DMT (rats)

| Condition | Cortex->Thalamus TE (bits) | Thalamus->Cortex TE (bits) | % change vs baseline |
|-----------|--------------------------|--------------------------|---------------------|
| Baseline | 0.041 | 0.035 | -- |
| 5-MeO-DMT (peak) | 0.062 | 0.055 | +50-55% |
| Post-drug (2 h) | 0.044 | 0.037 | ~baseline |

Psychedelic state enhances cross-frequency corticothalamic transfer by ~50%.

## 2024-04-12 -- Criticality measures across states

Branching ratio (sigma) near 1.0 indicates criticality; deviation indicates sub/supercriticality.

| Condition | Branching ratio (sigma) | Power-law exponent (alpha) | State |
|-----------|------------------------|---------------------------|-------|
| Awake | 0.98 | 1.52 | Near-critical |
| Propofol (deep) | 0.82 | 1.85 | Subcritical |
| Spike-wave seizure | 1.25 | 1.20 | Supercritical |
| 5-MeO-DMT | 1.02 | 1.48 | Slightly supercritical |

Conscious states cluster near criticality; unconsciousness deviates in both directions. Cross-frequency transfer correlates with proximity to critical point (r = 0.85, p < 0.001).
