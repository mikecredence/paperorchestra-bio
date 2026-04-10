## Working title

Functional Connectomics Spanning Multiple Areas of Mouse Visual Cortex

## Core question

Do neurons with similar visual response properties preferentially form synaptic connections, and does this "like-to-like" connectivity principle hold across cortical layers and visual areas, including feedback connections?

## Motivation / gap

- Excitatory neurons in primary visual cortex (V1) with similar orientation tuning are known to be preferentially connected, but it was unclear whether this like-to-like wiring principle extends across cortical layers and higher visual areas
- Previous functional connectomics studies were limited to small volumes in a single cortical area, preventing analysis of inter-areal synaptic connectivity
- No existing dataset combined calcium imaging of tens of thousands of neurons with electron microscopy reconstruction at a scale spanning multiple cortical areas
- The relative contributions of spatial proximity versus functional similarity in predicting fine-scale synaptic connectivity were unresolved

## Core contribution

- A millimeter-scale open-access dataset combining dense calcium imaging of ~75,000 neurons with petascale electron microscopy reconstruction containing >200,000 cells and 523 million synapses across four visual cortical areas (VISp, VISrl, VISal, VISlm)
- Demonstration that like-to-like connectivity is a universal wiring rule that operates within and across cortical layers and visual areas, including in feedback projections
- A digital twin model separating neuronal tuning into feature (stimulus selectivity) and spatial (receptive field location) components, showing that the feature component predicts fine-scale synaptic connections beyond what spatial proximity alone can explain
- Proofreading of a subset of neurons yielding complete dendritic trees and local plus inter-areal axonal projections mapping up to thousands of connections per neuron

## Method in brief

An adult mouse is presented with natural movies and parametric visual stimuli while two-photon calcium imaging records activity from approximately 75,000 neurons across primary visual cortex (VISp) and three higher visual areas (VISrl, VISal, VISlm). After functional imaging, the same tissue volume (approximately 1 cubic millimeter) is sectioned and imaged by serial-section electron microscopy at synaptic resolution. Automated segmentation and synapse detection identify over 200,000 cells and 523 million synapses. A subset of neurons is proofread to obtain complete morphological reconstructions. A digital twin neural network model is trained to predict neural responses, then decomposed into feature and spatial components. Synaptic connectivity is correlated with functional similarity metrics derived from both direct calcium imaging responses and digital twin predictions to test like-to-like connectivity across layers and areas.

## Target venue

Nature
