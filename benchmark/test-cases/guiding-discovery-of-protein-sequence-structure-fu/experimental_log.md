# Experimental Log -- In Silico Sequence-Structure-Function Pipeline for FDMOs

## 2024-01-20 -- Pipeline design

| Step | Tool | Input | Output |
|---|---|---|---|
| 1. Structure prediction | AlphaFold2 | Amino acid sequence | 3D protein structure |
| 2. Substrate docking | FFT docking | Structure + substrate | Docking poses + scores |
| 3. Functional prediction | Scoring function | Docking results | Predicted enantioselectivity and reactivity |
| 4. ML interpretation | Ensemble decision trees + XAI | Structural descriptors | Feature importance |

## 2024-02-10 -- Ancestral library characterization

| Property | Value |
|---|---|
| Enzyme family | Fungal flavin-dependent monooxygenases (FDMOs) |
| Library type | Ancestral sequence reconstruction |
| Number of sequences | Library-scale (dozens to hundreds) |
| Experimentally characterized subset | Available for validation |

## 2024-03-01 -- Enantioselectivity prediction validation

Compared predicted vs experimental enantioselectivity for the experimentally available subset.

| Metric | Value |
|---|---|
| Correlation (predicted vs experimental ee) | Positive, statistically significant |
| Correctly predicted major enantiomer (R vs S) | High accuracy |
| Captures phylogenetic enantioselectivity shifts | Yes |

The pipeline recapitulates known changes in enantioselectivity across the phylogenetic tree of ancestral FDMOs.

## 2024-03-15 -- Reactivity prediction validation

| Metric | Value |
|---|---|
| Correlation (predicted vs experimental reactivity) | Positive, significant |
| Rank agreement (top active enzymes) | Good |

## 2024-04-01 -- ML model results (ensemble decision trees)

| Model | Accuracy (classification) | Top features (SHAP) |
|---|---|---|
| Random Forest | Good | Active-site volume, substrate orientation angle, key residue distances |
| Gradient Boosted Trees | Good | Similar top features |

Explainable AI (SHAP) identifies specific structural determinants of selectivity -- actionable for rational engineering.

## 2024-04-10 -- Throughput comparison

| Approach | Throughput | Cost |
|---|---|---|
| Experimental screen (expression + assay) | ~10-50 variants/week | High (reagents, labor) |
| In silico pipeline (AF2 + FFT docking) | Hundreds of variants/day | Low (compute only) |

Pipeline is orders of magnitude faster than experimental screening.

## Summary

The AlphaFold2 + FFT docking pipeline accurately predicts enantioselectivity and reactivity for ancestral FDMOs, matching experimental results. ML models reveal structural determinants. This enables rapid in silico screening before committing to wet-lab work.
