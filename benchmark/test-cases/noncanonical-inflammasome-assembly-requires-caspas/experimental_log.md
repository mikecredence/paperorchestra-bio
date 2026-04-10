# Experimental Log -- Noncanonical Inflammasome Assembly and Caspase-11

## 2024-01-15 -- Construct design

| Construct | Tag | Catalytic activity | Autoprocessing |
|---|---|---|---|
| Casp11-WT-GFP | GFP | Active | Yes |
| Casp11-C254A-GFP | GFP | Dead (catalytic mutant) | No |
| Casp11-D285A-GFP | GFP | Active | Impaired (autoprocessing mutant) |

## 2024-02-01 -- LPS-induced speck formation (live-cell imaging)

Transfected LPS into macrophages expressing fluorescent Casp11 constructs.

| Construct | Speck formation after LPS | % Cells with specks | Timeframe |
|---|---|---|---|
| Casp11-WT-GFP | Yes | ~30-50% | 2-6 hours post-LPS |
| Casp11-C254A-GFP (catalytic dead) | No / severely reduced | <5% | Up to 8 hours |
| Casp11-D285A-GFP (autoprocessing mutant) | No / severely reduced | <5% | Up to 8 hours |
| GFP only (control) | No | 0% | -- |

Key finding: Catalytic activity is required for Casp11 speck formation. This was unexpected -- the prevailing model assumed specks form first, then activate the enzyme.

## 2024-02-20 -- Pyroptosis readouts

| Construct | Gasdermin D cleavage | LDH release (% cytotoxicity) | PI uptake |
|---|---|---|---|
| Casp11-WT | Yes (strong) | ~60-80% | High |
| Casp11-C254A | No | <10% | Minimal |
| Casp11-D285A | No / minimal | <15% | Minimal |
| Untransfected + LPS | No (LPS cannot enter cytosol) | <5% | Minimal |

Both catalytic activity and autoprocessing are required for downstream pyroptosis.

## 2024-03-10 -- Biochemical characterization (size-exclusion chromatography)

| Construct | LPS treatment | Oligomeric state |
|---|---|---|
| Casp11-WT | + LPS | High molecular weight complex (SMOC) |
| Casp11-WT | - LPS | Monomeric |
| Casp11-C254A | + LPS | Remains monomeric / low MW |
| Casp11-D285A | + LPS | Remains monomeric / low MW |

Catalytic-dead and autoprocessing-deficient Casp11 fail to form high MW complexes even in the presence of LPS.

## 2024-03-25 -- Model revision

| Previous model | Revised model (this work) |
|---|---|
| LPS binds Casp11 -> passive oligomerization into SMOC -> proximity activates catalytic activity -> GSDMD cleavage | LPS binds Casp11 -> catalytic activity and autoprocessing are actively required for SMOC assembly -> GSDMD cleavage and pyroptosis |

## Summary

Casp11 forms LPS-induced specks in macrophages, providing direct evidence for a noncanonical inflammasome SMOC. Unexpectedly, catalytic activity and intra-molecular autoprocessing are required for speck/SMOC formation itself, not just for downstream signaling. This revises the standard model of inflammasome assembly.
