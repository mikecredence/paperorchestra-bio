# Experimental Log -- Benchmarking ST Clustering, Alignment, and Integration

## 2024-01-10 -- Dataset collection

| Dataset type | Source | Count |
|---|---|---|
| Real datasets | Various ST platforms | Multiple |
| Simulated datasets | Custom simulation | Multiple |
| Technologies covered | 10x Visium, MERFISH, Slide-seq, STARmap, etc. | 4+ |
| Species | Human, Mouse | 2 |

## 2024-02-01 -- Method inventory

| Task | Number of methods benchmarked | Example methods |
|---|---|---|
| Spatial clustering | Multiple | SpaGCN, BayesSpace, STAGATE, stLearn, Louvain+spatial |
| Slice alignment | Multiple | PASTE, STalign, GPSA |
| Multi-slice integration | Multiple | STAligner, SPIRAL, Harmony+spatial |

## 2024-03-01 -- Clustering benchmark results (representative)

| Method | Mean ARI (real data) | Spatial Coherence Score (SCS) | Scalability |
|---|---|---|---|
| BayesSpace | 0.45-0.65 | High | Moderate |
| SpaGCN | 0.40-0.55 | Moderate-High | Good |
| STAGATE | 0.50-0.70 | High | Good |
| Louvain (no spatial) | 0.30-0.45 | Low | Excellent |

Methods leveraging spatial information consistently outperform non-spatial baselines on SCS.

## 2024-03-15 -- Alignment benchmark results

| Method | Layer-wise accuracy | Spot-to-spot accuracy | Runtime |
|---|---|---|---|
| PASTE | High | Moderate | Fast |
| STalign | Moderate-High | High | Moderate |
| GPSA | Moderate | Moderate | Slow |

## 2024-04-01 -- Integration benchmark results

| Method | Batch mixing (kBET) | Biological conservation (ARI) | 3D reconstruction quality |
|---|---|---|---|
| STAligner | Good | High | Good |
| Harmony+spatial | Moderate | Moderate | Moderate |
| SPIRAL | Good | Moderate-High | Good |

## 2024-04-10 -- Effect of dataset characteristics

| Factor | Impact on clustering | Impact on alignment |
|---|---|---|
| Dataset size (spots) | Large datasets favor scalable methods | Minimal impact |
| Technology (seq-based vs imaging) | Imaging-based favors graph methods | Affects feature overlap |
| Species | Minimal systematic effect | Minimal |
| Tissue complexity | High complexity reduces all ARI scores | More landmarks help alignment |

## Summary

No single method dominates across all tasks and datasets. Spatial-aware methods consistently outperform non-spatial baselines. Method choice should be guided by task, dataset size, and technology platform.
