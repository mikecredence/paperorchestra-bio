# Experimental Log -- Toolkits for Detailed and High-Throughput Interrogation of Synapses in C. elegans

## 2023-03-01 -- Transgenic reporter strain resource

| Reporter category | Marker protein | Synapse type | Number of strains |
|---|---|---|---|
| Pre-synaptic active zone | CLA-1::GFP | Chemical (pre) | 10 |
| Synaptic vesicle | RAB-3::mCherry | Chemical (pre) | 8 |
| Trans-synaptic contact | split-GFP GRASP | Chemical (pre+post) | 7 |
| Gap junction | INX::GFP | Electrical | 5 |
| **Total** | | | **30** |

All strains express reporters under neuron-type-specific promoters targeting defined circuits across the nervous system.

## 2023-04-15 -- WormPsyQi pipeline architecture

| Pipeline step | Method | Purpose |
|---|---|---|
| 1. Neurite segmentation | U-Net (trained on 200 annotated images) | Define region of interest |
| 2. Synapse segmentation | Adaptive threshold + watershed | Identify individual puncta |
| 3. Validation/correction | Rule-based biological constraints | Remove artifacts |
| 4. Re-labeling (optional) | Active learning loop | Adapt to new reporters |
| 5. Feature extraction | Morphometric quantification | Measure punctum properties |

## 2023-05-20 -- Pipeline validation: WormPsyQi vs. manual expert annotation

| Reporter strain | Neuron class | Manual count (mean +/- SD) | WormPsyQi count (mean +/- SD) | Pearson r | n (animals) |
|---|---|---|---|---|---|
| CLA-1::GFP (olaIs67) | DA9 motor neuron | 22.4 +/- 3.1 | 23.1 +/- 2.8 | 0.94 | 48 |
| CLA-1::GFP (olaIs68) | AIY interneuron | 14.8 +/- 2.6 | 15.2 +/- 2.4 | 0.92 | 52 |
| RAB-3::mCherry (olaIs35) | DD motor neurons | 31.6 +/- 4.2 | 32.4 +/- 3.9 | 0.91 | 45 |
| GRASP (olaIs71) | PHB->AVA | 8.2 +/- 1.8 | 8.5 +/- 1.6 | 0.89 | 40 |
| INX-19::GFP (olaIs73) | AIY-RIA gap junction | 5.4 +/- 1.2 | 5.7 +/- 1.1 | 0.87 | 38 |

WormPsyQi counts correlate strongly (r > 0.87) with manual expert annotation across all tested reporter types.

## 2023-06-10 -- Synapse number across developmental stages (DA9 motor neuron, CLA-1::GFP)

| Developmental stage | Synapse count (mean) | SD | n (animals) | p vs. adult |
|---|---|---|---|---|
| L1 larva | 6.2 | 1.4 | 35 | <0.001 |
| L2 larva | 11.8 | 2.1 | 32 | <0.001 |
| L3 larva | 16.4 | 2.8 | 38 | <0.001 |
| L4 larva | 20.1 | 3.0 | 41 | 0.012 |
| Young adult | 22.4 | 3.1 | 48 | -- |
| Day 3 adult | 21.8 | 3.4 | 36 | 0.58 |

Synapse number increases progressively during larval development and plateaus at the young adult stage.

## 2023-07-05 -- Synapse punctum morphometric features (young adult, DA9 motor neuron)

| Feature | Mean | SD | Min | Max | Unit |
|---|---|---|---|---|---|
| Punctum count | 22.4 | 3.1 | 14 | 31 | count |
| Punctum area | 0.42 | 0.12 | 0.18 | 0.89 | um^2 |
| Peak intensity (a.u.) | 2,840 | 620 | 1,180 | 4,920 | a.u. |
| Integrated intensity | 1,194 | 348 | 412 | 2,680 | a.u. * um^2 |
| Inter-punctum distance | 1.86 | 0.54 | 0.72 | 3.41 | um |
| Neurite length | 42.8 | 6.2 | 28.4 | 58.1 | um |
| Synapse density | 0.52 | 0.08 | 0.34 | 0.74 | puncta/um |

## 2023-07-20 -- Sex-specific differences in synaptic properties (PHB sensory neuron)

| Property | Hermaphrodite (mean +/- SD) | Male (mean +/- SD) | Fold change (M/H) | p-value |
|---|---|---|---|---|
| Synapse count (PHB->AVA) | 8.2 +/- 1.8 | 12.6 +/- 2.4 | 1.54 | <0.001 |
| Synapse count (PHB->PVC) | 5.1 +/- 1.3 | 4.8 +/- 1.2 | 0.94 | 0.42 |
| Mean punctum area (PHB->AVA) | 0.38 +/- 0.09 | 0.46 +/- 0.11 | 1.21 | 0.003 |
| Mean peak intensity (PHB->AVA) | 2,510 +/- 480 | 3,120 +/- 560 | 1.24 | <0.001 |

Males exhibit significantly more and larger PHB->AVA synapses compared to hermaphrodites, consistent with sex-specific circuit remodeling for mating behavior.

## 2023-08-15 -- Cross-neuron comparison of synaptic properties (young adult hermaphrodite)

| Neuron class | Reporter | Synapse count | Punctum area (um^2) | Density (puncta/um) | Neurite length (um) |
|---|---|---|---|---|---|
| DA9 motor neuron | CLA-1::GFP | 22.4 | 0.42 | 0.52 | 42.8 |
| AIY interneuron | CLA-1::GFP | 14.8 | 0.36 | 0.38 | 38.9 |
| DD motor neurons | RAB-3::mCherry | 31.6 | 0.48 | 0.28 | 112.4 |
| ASE sensory neuron | CLA-1::GFP | 9.4 | 0.31 | 0.42 | 22.6 |
| RIA interneuron | CLA-1::GFP | 18.2 | 0.39 | 0.45 | 40.4 |
| VD motor neurons | RAB-3::mCherry | 28.4 | 0.44 | 0.26 | 108.8 |

Synapse count and density vary systematically across neuron classes, with motor neurons in the ventral cord having the highest absolute counts but lower linear density than compact interneurons.

## 2023-09-01 -- Pipeline throughput and efficiency

| Metric | Manual | WormPsyQi | Improvement |
|---|---|---|---|
| Animals analyzed per hour | 8-12 | 180-240 | ~20x |
| Intra-observer variability (CV) | 12.4% | 3.2% | 3.9x reduction |
| Inter-observer variability (CV) | 18.7% | 0% (deterministic) | Eliminated |
| Features extracted per animal | 2-3 | 7+ | >2x |

## Summary

WormPsyQi enables automated, high-throughput quantification of synaptic properties in C. elegans with accuracy comparable to manual expert annotation (r > 0.87) and approximately 20-fold higher throughput. Combined with 30 transgenic reporter strains, this toolkit enables systematic characterization of synapse number, size, intensity, and distribution across the nervous system, revealing developmental trajectories, sex-specific differences, and neuron-class-specific synaptic architectures.
