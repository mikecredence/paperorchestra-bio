## Working title
CryoTEN: A Transformer-Based U-Net for Fast and Effective Cryo-EM Density Map Enhancement

## Core question
Can a 3D U-Net style transformer with efficient attention mechanisms substantially improve cryo-EM density map quality while being an order of magnitude faster and less memory-intensive than existing deep learning approaches?

## Motivation / gap
- Cryo-EM density maps suffer from noise and missing density values due to low contrast and conformational heterogeneity, limiting the quality of protein structures built from them
- Global sharpening (single B-factor correction) cannot adapt to local variations, leading to over/under-sharpened regions
- Local sharpening methods (LocalDeblur, LocSpiral, LocScale) improve on global approaches but remain limited in handling complex local noise patterns
- Existing deep learning methods for map enhancement (DeepEMhancer, EMReady) achieve good quality improvements but are very slow and consume large amounts of GPU memory, limiting practical usability
- No method had combined transformer-based attention with 3D U-Net architecture specifically for cryo-EM map enhancement
- The trade-off between map enhancement quality and computational efficiency had not been adequately addressed

## Core contribution (bullet form)
- CryoTEN achieves average FSC@0.143 resolution of 2.45 Angstroms on 150 test maps, a 30.99% improvement over 3.55 Angstroms for deposited primary maps; 100% of maps improved at this threshold
- FSC@0.5 resolution improved to 3.73 Angstroms from 6.38 Angstroms (41.54% improvement), with 96% of maps showing improvement
- Protein structures built from CryoTEN-processed maps show substantially better quality than those from original maps (700 chains from 124 maps evaluated via residue coverage and sequence match scores)
- CryoTEN runs >10x faster than existing deep learning methods (DeepEMhancer, EMReady) and requires much less GPU memory, while ranking second in map quality improvement
- Trained on 1,295 cryo-EM maps with corresponding simulated maps from known structures; validated on 76 maps; independently tested on 150 maps
- Also effective on half maps (70 half maps tested), demonstrating generalization

## Method in brief
CryoTEN uses a 3D U-Net architecture equipped with EPA (Efficient Pair-wise Attention) attention mechanisms. The model takes deposited experimental cryo-EM primary maps as input and is trained to predict high-quality simulated maps generated from corresponding known PDB structures. The simulated target maps are computed using a reference Gaussian function where the density at each grid point depends on its distance to every atom in the PDB structure, with parameters derived from the FSC@0.143 resolution. Training used 1,295 non-redundant map-structure pairs (filtered for CC mask > 0.7 and CC box > 0.6, clustered at 30% sequence identity via MMseqs2), with 76 for validation and 150 for independent testing.

During data processing, all maps were resampled to a standardized 1 Angstrom grid size. Deposited maps were normalized to 0-1 range using the 99.999th percentile density value. Maps were split into overlapping 64x64x64 blocks with stride 50, randomly cropped to 48x48x48 during training for regularization. At inference, 48x48x48 blocks are processed in batches and reassembled into the full enhanced map.

Evaluation used multiple map-model validation metrics computed via phenix tools: FSC@0.143 and FSC@0.5 (unmasked map-model resolution), CC box, CC mask, CC peaks (cross-correlation scores), and Q-score (atom resolvability). De novo structure modeling quality was assessed by building protein structures from enhanced maps and measuring residue coverage and sequence match scores across 700 protein chains from 124 maps.

## Target venue
Bioinformatics
