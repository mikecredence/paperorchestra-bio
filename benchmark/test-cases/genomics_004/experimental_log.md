# Experimental Log -- Benchmarking Single-Cell Multi-Modal Integration

## 2024-01-15 -- Scope definition

| Dimension | Coverage |
|---|---|
| Total algorithms benchmarked | 40 |
| Modalities | DNA (scATAC), RNA (scRNA), Protein (CITE-seq), Spatial |
| Dataset types | Paired, Unpaired, Mosaic |
| Evaluation axes | Usability, Accuracy, Robustness |

## 2024-02-10 -- Dataset assembly

| Dataset type | Modality combination | Example datasets |
|---|---|---|
| Paired | RNA + Protein (CITE-seq) | PBMC CITE-seq |
| Paired | RNA + DNA (10x Multiome) | PBMC Multiome |
| Unpaired | RNA + ATAC (separate) | Brain scRNA + scATAC |
| Mosaic | Mixed paired + unpaired | Custom assemblies |
| Spatial | RNA + spatial coordinates | MERFISH, Visium |

## 2024-03-01 -- Accuracy results (paired datasets)

| Method category | Mean ARI | Mean NMI | Label transfer accuracy |
|---|---|---|---|
| Top-performing (e.g., Cobolt, MultiVI) | 0.70-0.85 | 0.75-0.85 | High |
| Mid-tier | 0.50-0.70 | 0.55-0.70 | Moderate |
| Low-performing | <0.50 | <0.55 | Low |

## 2024-03-15 -- Accuracy results (unpaired datasets)

| Method category | Mean ARI | Batch correction (kBET) | Bio conservation |
|---|---|---|---|
| Top-performing (e.g., GLUE, bindSC) | 0.55-0.70 | Good | High |
| Mid-tier | 0.40-0.55 | Moderate | Moderate |
| Low-performing | <0.40 | Poor | Low |

Unpaired integration is harder than paired across the board.

## 2024-04-01 -- Mosaic dataset results

| Method | Handles mosaic? | ARI on mosaic data | Notes |
|---|---|---|---|
| StabMap | Yes | 0.60-0.70 | Designed for mosaic |
| MultiVI | Partial | 0.50-0.60 | Requires adaptation |
| Most methods | No | N/A | Cannot handle mosaic input |

Few methods natively support mosaic data -- a clear gap.

## 2024-04-10 -- Robustness to dataset size and noise

| Condition | Effect on top methods | Effect on low-tier methods |
|---|---|---|
| Small dataset (< 1k cells) | Moderate degradation | Large degradation |
| High noise / low quality | Mild degradation | Severe degradation |
| Large dataset (> 100k cells) | Scalability limits for some | Many fail to run |

## 2024-04-15 -- Usability assessment

| Criterion | Range across 40 tools |
|---|---|
| Installation difficulty | Easy to very difficult |
| Documentation quality | Excellent to poor |
| Runtime (typical dataset) | Seconds to hours |
| GPU requirement | 12 tools require GPU |

## Summary

Of 40 methods, a small subset consistently performs well across paired and unpaired settings. Mosaic integration remains underserved. Usability varies dramatically. Guidance tables provided for method selection by dataset type and modality.
