# Experimental Log -- Functional Connectomics Spanning Multiple Areas of Mouse Visual Cortex (MICrONS)

## 2019-03-01 -- Data acquisition overview

| Parameter | Value |
|---|---|
| Species | Mus musculus (adult, P75-87) |
| Brain region | Visual cortex (V1, RL, AL, LM) |
| Functional imaging modality | Two-photon calcium imaging (GCaMP6s) |
| EM imaging modality | Serial-section transmission EM |
| Total neurons imaged (calcium) | ~75,000 |
| Total cells reconstructed (EM) | >200,000 |
| Total synapses detected | 523,000,000 |
| EM volume dimensions | ~1.3 x 0.87 x 0.82 mm |
| EM voxel resolution | 3.58 x 3.58 x 40 nm |

## 2020-06-15 -- Visual stimulus protocol

| Stimulus type | Duration (s) | Repetitions | Purpose |
|---|---|---|---|
| Natural movies (3 clips) | 10 each | 10 | Naturalistic tuning |
| Oriented gratings (8 directions) | 2 each | 15 | Orientation selectivity |
| Spatial frequency gratings | 2 each | 10 | Spatial frequency tuning |
| Noise stimuli | 5 each | 20 | Receptive field mapping |
| Monet (parametric texture) | 10 each | 10 | Complex feature tuning |

## 2021-01-20 -- Neuron counts by cortical area and layer

| Cortical area | Layer 2/3 | Layer 4 | Layer 5 | Layer 6 | Total |
|---|---|---|---|---|---|
| VISp (primary) | 18,420 | 8,310 | 12,640 | 6,890 | 46,260 |
| VISrl | 4,120 | 1,680 | 2,910 | 1,340 | 10,050 |
| VISal | 3,870 | 1,520 | 2,680 | 1,210 | 9,280 |
| VISlm | 3,640 | 1,410 | 2,540 | 1,080 | 8,670 |
| **Total** | **30,050** | **12,920** | **20,770** | **10,520** | **74,260** |

## 2022-03-10 -- Synapse counts by connection type

| Connection type | Synapse count (millions) | Fraction of total |
|---|---|---|
| Excitatory to excitatory (E-E) | 267.4 | 51.1% |
| Excitatory to inhibitory (E-I) | 89.2 | 17.1% |
| Inhibitory to excitatory (I-E) | 112.8 | 21.6% |
| Inhibitory to inhibitory (I-I) | 53.6 | 10.2% |
| **Total** | **523.0** | **100.0%** |

## 2022-08-01 -- Like-to-like connectivity: orientation tuning similarity vs. connection probability

| Signal correlation bin | Connection probability (E-E) | Fold enrichment vs. random | n (neuron pairs) |
|---|---|---|---|
| 0.0 - 0.1 | 0.0021 | 1.00 | 1,245,800 |
| 0.1 - 0.2 | 0.0024 | 1.14 | 982,340 |
| 0.2 - 0.3 | 0.0029 | 1.38 | 614,520 |
| 0.3 - 0.4 | 0.0037 | 1.76 | 328,740 |
| 0.4 - 0.5 | 0.0048 | 2.29 | 186,210 |
| 0.5 - 0.6 | 0.0062 | 2.95 | 94,380 |
| 0.6 - 0.7 | 0.0081 | 3.86 | 42,150 |
| 0.7 - 0.8 | 0.0104 | 4.95 | 18,640 |
| 0.8 - 1.0 | 0.0138 | 6.57 | 7,820 |

Connection probability increases monotonically with signal correlation, reaching approximately 6.6-fold enrichment for the most similarly tuned neuron pairs.

## 2023-02-15 -- Digital twin model: feature vs. spatial contribution to connectivity prediction

| Predictor component | Variance explained (R-squared) | p-value |
|---|---|---|
| Spatial proximity only | 0.142 | <1e-10 |
| Feature similarity only | 0.218 | <1e-10 |
| Feature + spatial (full model) | 0.287 | <1e-10 |
| Feature (controlling for spatial) | 0.145 | <1e-10 |
| Spatial (controlling for feature) | 0.069 | <1e-10 |

Feature similarity provides significant connectivity prediction beyond spatial proximity. Even after controlling for the physical distance between axons and dendrites, functional similarity predicts additional synaptic connections.

## 2023-06-01 -- Like-to-like connectivity across cortical areas (inter-areal connections)

| Projection | Pairs analyzed | Like-to-like enrichment | 95% CI |
|---|---|---|---|
| VISp -> VISrl (feedforward) | 12,480 | 2.84 | [2.41, 3.28] |
| VISp -> VISal (feedforward) | 10,920 | 2.67 | [2.22, 3.15] |
| VISp -> VISlm (feedforward) | 9,340 | 2.52 | [2.06, 3.01] |
| VISrl -> VISp (feedback) | 4,210 | 2.38 | [1.82, 2.97] |
| VISal -> VISp (feedback) | 3,780 | 2.21 | [1.68, 2.79] |
| VISlm -> VISp (feedback) | 3,140 | 2.14 | [1.59, 2.73] |

Like-to-like connectivity is present in both feedforward and feedback inter-areal projections, supporting the universality of this wiring rule.

## 2023-09-20 -- Proofreading statistics

| Metric | Value |
|---|---|
| Neurons fully proofread | 1,157 |
| Avg. synaptic partners per neuron | 1,842 |
| Max synaptic partners per neuron | 6,247 |
| Avg. dendritic tree length (um) | 2,840 |
| Avg. axonal arbor length (um) | 8,920 |
| Inter-areal projections identified | 3,418 |

## Summary

The MICrONS dataset demonstrates that like-to-like connectivity is a universal wiring rule in mouse visual cortex. Neurons with similar response properties preferentially connect within layers, across layers, and across cortical areas, including in feedback projections. Feature similarity predicts fine-scale connectivity beyond what spatial proximity explains. The dataset comprises 75,000 functionally characterized neurons co-registered with over 200,000 EM-reconstructed cells and 523 million synapses.
