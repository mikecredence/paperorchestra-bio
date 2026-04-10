## Working title

Toolkits for Detailed and High-Throughput Interrogation of Synapses in C. elegans

## Core question

Can we develop an automated, unbiased pipeline for quantifying synaptic properties in C. elegans at scale, and use it alongside a comprehensive set of transgenic synaptic reporter strains to systematically characterize synapse number, size, intensity, and spatial distribution across the nervous system?

## Motivation / gap

- The C. elegans connectome provides a complete wiring diagram, but systematic measurement of synapse-level properties (size, intensity, spatial distribution) across neuron types requires high-throughput quantitative tools
- Manual quantification of fluorescent synaptic puncta is labor-intensive, low-throughput, and prone to human bias, limiting reproducibility and statistical power
- Existing transgenic synaptic reporters cover only a fraction of the nervous system, and a comprehensive resource of validated reporters for both chemical and electrical synapses was lacking
- Quantitative comparison of synaptic properties across developmental stages, sexes, and genetic backgrounds requires standardized automated analysis

## Core contribution

- WormPsyQi: a machine-learning-based image analysis pipeline that automatically segments, validates, and quantifies synaptically localized fluorescent signals with reduced human bias
- A resource of 30 transgenic C. elegans strains expressing fluorescent reporters at chemical synapses (CLA-1, RAB-3, GRASP markers) and electrical synapses (innexin reporters) throughout the nervous system
- Systematic quantification of synapse number, punctum size, fluorescence intensity, and spatial distribution across multiple neuron classes, developmental stages (L1 through adult), and between hermaphrodites and males
- Demonstration that WormPsyQi reproduces manual expert quantification while enabling analysis of large datasets with hundreds of animals

## Method in brief

Thirty transgenic C. elegans strains are generated, each expressing a fluorescent reporter (GFP or mCherry) fused to a synaptic protein (CLA-1 for active zones, RAB-3 for synaptic vesicles, split-GFP GRASP for trans-synaptic contacts, or innexins for gap junctions) under neuron-specific promoters. Animals are imaged on a high-content fluorescence microscope. WormPsyQi processes images through five steps: (1) optional neurite mask segmentation using a trained U-Net model, (2) synapse punctum segmentation via adaptive thresholding and watershed, (3) automated validation and correction against known biological constraints, (4) optional re-labeling and model retraining for novel reporters, and (5) extraction of quantitative features including punctum count, area, peak intensity, integrated intensity, inter-punctum distance, and spatial distribution along the neurite axis. Pipeline accuracy is validated against manual expert annotation across multiple reporter strains and imaging conditions.

## Target venue

eLife
