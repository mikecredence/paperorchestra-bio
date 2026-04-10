# Experimental Log -- Network Statistics of the Whole-Brain Connectome of Drosophila

## 2023-06-01 -- Connectome dataset overview

| Parameter | Value |
|---|---|
| Dataset version | FlyWire v630 |
| Species | Drosophila melanogaster (adult female) |
| Total neurons | 127,978 |
| Total synapses (raw) | ~54,500,000 |
| Synapse threshold applied | 5 synapses per connection |
| Thresholded connections | 2,613,129 |
| Imaging modality | Serial-section electron microscopy |
| Segmentation method | Automated + community proofreading |

## 2023-07-10 -- Degree distribution analysis

| Degree metric | Mean | Median | Max | Std. dev. |
|---|---|---|---|---|
| In-degree | 20.4 | 12 | 2,247 | 38.6 |
| Out-degree | 20.4 | 13 | 1,893 | 35.2 |
| Total degree | 40.8 | 25 | 3,841 | 68.4 |

The degree distribution is heavy-tailed, with most neurons having relatively few connections but a long tail of highly connected hub neurons.

## 2023-07-20 -- Global network statistics

| Metric | Fly brain | ER null model | CFG null model |
|---|---|---|---|
| Clustering coefficient | 0.0477 | 0.00032 | 0.0083 |
| Global reciprocity | 0.125 | 0.00032 | 0.0056 |
| Avg. shortest path length | 3.68 | 4.12 | 3.95 |
| Small-world index (sigma) | 5.42 | 1.0 | 1.0 |
| Strong connected component (% neurons) | 93.8 | 99.7 | 98.2 |
| Weak connected component (% neurons) | 99.6 | 100.0 | 100.0 |

The fly brain clustering coefficient is roughly 150x higher than the ER model and 5.7x higher than the CFG model, indicating strong local connectivity beyond what degree distribution alone would predict.

## 2023-08-05 -- Rich-club analysis

| Rich-club parameter | Value |
|---|---|
| Rich-club degree threshold | Total degree > 37 |
| Neurons in rich club | ~38,400 (~30% of connectome) |
| Rich-club coefficient (normalized) | 1.82 |
| Integrator neurons (high in-degree bias) | ~12,500 |
| Broadcaster neurons (high out-degree bias) | ~11,200 |
| Balanced hub neurons | ~14,700 |

Rich-club neurons are disproportionately interneurons and projection neurons spanning multiple brain regions.

## 2023-08-15 -- Motif census (two-node and three-node)

| Motif type | Observed count | Z-score vs. ER | Z-score vs. CFG |
|---|---|---|---|
| Reciprocal pair (bidirectional) | 163,448 | +42.3 | +18.7 |
| Three-node chain (A->B->C) | 4,215,890 | +8.2 | +3.1 |
| Three-node convergent (A->C, B->C) | 3,987,124 | +6.4 | +2.8 |
| Three-node divergent (A->B, A->C) | 4,102,337 | +7.1 | +3.0 |
| Three-node cycle (A->B->C->A) | 892,156 | +38.5 | +22.4 |
| Fully connected triad | 248,791 | +51.2 | +28.9 |

Highly recurrent motifs (cycles, fully connected triads) are dramatically overrepresented, while simple feed-forward motifs show modest enrichment.

## 2023-09-01 -- Network statistics by neurotransmitter type

| Neurotransmitter | Neuron count | Mean degree | Clustering coeff. | Reciprocity |
|---|---|---|---|---|
| Acetylcholine (excitatory) | 52,340 | 47.2 | 0.052 | 0.138 |
| GABA (inhibitory) | 28,916 | 38.5 | 0.044 | 0.119 |
| Glutamate (mixed) | 21,784 | 35.1 | 0.041 | 0.108 |
| Dopamine | 1,245 | 62.8 | 0.038 | 0.092 |
| Serotonin | 892 | 58.4 | 0.035 | 0.087 |
| Octopamine | 634 | 44.1 | 0.029 | 0.076 |

Cholinergic neurons form the largest and most densely connected subnetwork with the highest clustering and reciprocity.

## 2023-09-15 -- Comparison with other connectomes

| Organism | Neurons | Connections | Clustering coeff. | Small-world index |
|---|---|---|---|---|
| Drosophila (adult, this study) | 127,978 | 2,613,129 | 0.0477 | 5.42 |
| C. elegans (hermaphrodite) | 302 | 6,394 | 0.340 | 5.60 |
| Drosophila larva | 3,016 | 548,000 | 0.062 | 4.18 |
| Mouse (partial cortical) | ~1,000 | ~3,500 | 0.150 | 3.80 |

Despite vast differences in scale, both Drosophila and C. elegans connectomes display small-world properties, though the clustering coefficient decreases with network size.

## 2023-10-01 -- Edge percolation and robustness

| Fraction of edges removed | Largest component size (% of network) |
|---|---|
| 0% | 93.8% |
| 10% | 91.2% |
| 20% | 87.6% |
| 30% | 80.1% |
| 40% | 65.4% |
| 50% | 42.8% |
| 60% | 18.3% |

The network shows gradual degradation under random edge removal, consistent with a robust architecture lacking a sharp percolation threshold.

## Summary

The adult Drosophila whole-brain connectome exhibits rich-club organization, high clustering, strong reciprocity, and small-world properties. Recurrent motifs are dramatically overrepresented relative to null models. Approximately 30% of neurons form a rich club of highly connected hubs. Network properties vary systematically with neurotransmitter identity and cell type.
