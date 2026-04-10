# Experimental Log: TEMPy-REFF Cryo-EM Refinement

## Benchmark dataset summary

| Property | Value |
|---|---|
| Total cryo-EM maps | 366 |
| Source | EMDB |
| Resolution range | 1.8 - 7.1 A |
| Corresponding models | PDB assembly models |

## Refinement performance vs. state-of-the-art

| Method | Avg. cross-correlation improvement | Notes |
|---|---|---|
| TEMPy-REFF (ours) | Significant improvement over baseline | B-factor + ensemble |
| State-of-the-art (Phenix/Refmac) | Baseline | Standard real-space refinement |

## Resolution bin analysis

| Resolution bin (A) | N maps | TEMPy-REFF fit quality | Baseline fit quality |
|---|---|---|---|
| 1.8 - 3.0 | ~120 | Improved | Good |
| 3.0 - 5.0 | ~160 | Markedly improved | Moderate |
| 5.0 - 7.1 | ~86 | Largest gains | Poor |

## AlphaFold-Multimer combination results

| Metric | Before AF-Multimer | After AF-Multimer + REFF |
|---|---|---|
| Modelled residues | Deposited PDB coverage | Extended into unresolved regions |
| Map-model agreement | Standard | Improved in newly modelled regions |

## Notes

- 2024-01-15: Initial benchmark run on 366 maps complete. Consistent improvement across resolution bins.
- 2024-02-03: AlphaFold-Multimer integration tested on subset with missing regions; successfully modelled new density.
- 2024-02-20: Composite map decomposition validated; components align well with known subunit boundaries.
- Key finding: the ensemble representation captures conformational heterogeneity that single-model refinement misses, especially at lower resolutions.
