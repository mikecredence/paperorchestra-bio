# Idea Summary: Deciphering the Genetic Code of Neuronal Type Connectivity Through Bilinear Modeling

## Working title
Deciphering the Genetic Code of Neuronal Type Connectivity Through Bilinear Modeling

## Core question
AbstractUnderstanding how different neuronal types connect and communicate is critical to interpreting brain function and behavior. However, it has remained a formidable challenge to decipher the genetic underpinnings that dictate the specific connections formed between neuronal types. To address this, we propose a novel bilinear modeling approach that leverages the architecture similar to that of recommendation systems. Our model transforms the gene expressions of presynaptic and postsynaptic n

## Motivation / gap
- 1IntroductionOne of the fundamental objectives in neuroscience is understanding how diverse neuronal cell types establish connections to form functional circuits.
- This understanding serves as a cornerstone for decoding how the nervous system processes information and coordinates responses to stimuli [1].
- Despite this, the genetic mechanisms determining the specific connections between distinct neuronal types, especially within complex brain structures, remains elusive [2, 3].Recent advances in transcr
- Single-cell transcriptomics enables high-resolution profiling of gene expressions across neuronal types [4, 5], while connectomic data offers detailed maps quantifying connections between neuronal cel
- However, the challenge of linking gene expressions derived from single-cell transcriptomics to neuronal type connectivity evident from connectomic data to uncover the genetic underpinnings has yet to 

## Core contribution (bullet form)
Extracted from abstract:
AbstractUnderstanding how different neuronal types connect and communicate is critical to interpreting brain function and behavior. However, it has remained a formidable challenge to decipher the genetic underpinnings that dictate the specific connections formed between neuronal types. To address this, we propose a novel bilinear modeling approach that leverages the architecture similar to that of recommendation systems. Our model transforms the gene expressions of presynaptic and postsynaptic neuronal types, obtained from single-cell transcriptomics, into a covariance matrix. The objective is to construct this covariance matrix that closely mirrors a connectivity matrix, derived from connectomic data, reflecting the known anatomical connections between these neuronal types. When tested on a dataset of Caenorhabditis elegans, our model achieved a performance comparable to, if slightly better than, the previously proposed spatial connectome model (SCM) in reconstructing electrical synaptic connectivity based on gene expressions. Through a comparative analysis, our model not only captured all genetic interactions identified by the SCM but also inferred additional ones. Applied to a mouse retinal neuronal dataset, the bilinear model successfully recapitulated recognized connectivity motifs between bipolar cells and retinal ganglion cells, and provided interpretable insights into genetic interactions shaping the connectivity. Specifically, it identified unique genetic signatures associated with different connectivity motifs, including genes important to cell-cell adhesion and synapse formation, highlighting their role in orchestrating specific synaptic connections between these neurons. Our work establishes an innovative computational strategy for decoding the genetic programming of neuronal type connectivity. It not only sets a new benchmark for single-cell transcriptomic analysis of synaptic connections but also paves the way for mechanistic studies of neural circuit assembly and genetic manipulation of circuit wiring.

## Method in brief
Methods not available from XML.

## Target venue
eLife
