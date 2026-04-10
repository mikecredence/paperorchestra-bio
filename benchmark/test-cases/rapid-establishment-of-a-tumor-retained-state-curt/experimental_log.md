# Experimental Log: NK Cell Fate in Solid Tumors

## Experiment 1: Kinetics of NK cell phenotypic conversion after tumor entry

Photo-labeled NK cells tracked at timepoints after tumor infiltration.

| Time Post-Entry | % Expressing IFN-gamma | % Expressing Granzyme B | % Tissue-Residency Markers | n (mice) |
|---|---|---|---|---|
| 0 h (pre-entry, blood) | 68 | 72 | 5 | 8 |
| 24 h | 42 | 48 | 28 | 8 |
| 48 h | 12 | 15 | 65 | 8 |
| 72 h | 3 | 5 | 88 | 8 |
| 7 days | 2 | 3 | 94 | 6 |

Key finding: Near-complete loss of effector function within 48-72 hours.

## Experiment 2: Tumor growth after NK cell depletion in established tumors

| Condition | Tumor Volume Day 14 (mm3) | Tumor Volume Day 21 (mm3) | p-value (vs control) |
|---|---|---|---|
| Isotype control | 285 | 810 | -- |
| NK depletion (established tumor) | 298 | 835 | 0.72 |
| NK depletion (early, day 0) | 420 | 1250 | <0.01 |

## Experiment 3: Transcriptomic shift -- top DEGs (tumor-retained vs blood NK)

| Gene | Log2 Fold Change | Adjusted p-value | Function |
|---|---|---|---|
| Itga1 (CD49a) | +4.2 | <0.001 | Tissue residency |
| Cd69 | +3.8 | <0.001 | Tissue retention |
| Ifng | -5.1 | <0.001 | Cytokine (effector) |
| Gzmb | -4.5 | <0.001 | Cytotoxicity |
| Ccl5 | -3.9 | <0.001 | Chemokine |
| Prf1 | -3.2 | <0.001 | Cytotoxicity |

## Experiment 4: Cross-model validation

| Tumor Model | Conversion by 72h? | Depletion Affects Growth? |
|---|---|---|
| B16-F10 (melanoma) | Yes | No |
| MC38 (colon) | Yes | No |
| LLC (lung) | Yes | No |

## Notes

- Continuous recruitment + rapid conversion = the tumor always has NK cells, but they are functionally dead.
- This explains why NK-based immunotherapies struggle in established solid tumors.
- Targeting the conversion program (rather than just boosting NK recruitment) may be the key therapeutic angle.
