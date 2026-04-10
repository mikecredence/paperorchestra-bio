# Experimental Log: Bacterial Essential Interactome Assembly

## Experiment 1: AlphaFold2 prediction summary

| Metric | Value |
|---|---|
| Total essential protein pairs modeled | 1,089 |
| High-accuracy models (ipTM > 0.7) | 115 |
| Medium-confidence models (ipTM 0.5-0.7) | 203 |
| Low-confidence / no interaction | 771 |
| Success rate (high-accuracy) | 10.6% |

## Experiment 2: Model quality metrics for high-accuracy set

| Quality Metric | Mean | Median | Range |
|---|---|---|---|
| ipTM score | 0.82 | 0.81 | 0.70 - 0.95 |
| pLDDT (interface) | 78.5 | 79.2 | 65.0 - 92.1 |
| PAE (interface, A) | 4.2 | 3.8 | 1.5 - 8.0 |
| Interface area (A^2) | 1,450 | 1,280 | 520 - 4,100 |

## Experiment 3: Comparison to known structures

| Category | Count | % of High-Accuracy Set |
|---|---|---|
| Known complex (PDB match) | 42 | 36.5 |
| Known interaction, no structure | 31 | 27.0 |
| Novel interaction (not in databases) | 28 | 24.3 |
| Conflicting with literature | 14 | 12.2 |

## Experiment 4: Interface feature analysis

| Feature | Known Complexes (mean) | Novel Complexes (mean) | p-value |
|---|---|---|---|
| Hydrogen bonds at interface | 12.4 | 10.8 | 0.18 |
| Salt bridges | 4.2 | 3.8 | 0.42 |
| Hydrophobic contacts | 28.5 | 24.1 | 0.09 |
| Interface buried surface area (A^2) | 1,520 | 1,340 | 0.12 |

Novel interactions have comparable interface features to known complexes.

## Experiment 5: Druggability assessment of novel targets

| Novel Interaction | Interface Druggability Score | Hot-Spot Residues | Pocket Detected? |
|---|---|---|---|
| DnaA-DnaN | 0.72 | 5 | Yes |
| FtsZ-ZapA | 0.68 | 4 | Yes |
| MurA-MurB | 0.81 | 6 | Yes |
| RpoB-RpoC (novel interface) | 0.55 | 3 | Partial |

## Notes

- 115 high-confidence models out of 1,089 tested pairs is a strong yield for systematic prediction.
- 28 novel interactions are the most exciting finding; these are new drug target candidates.
- Framework is generalizable: same pipeline can be applied to any bacterial species with annotated essential genes.
- Validation of known complexes (36.5% match PDB) supports the reliability of the approach.
