## Working title

Competitive interactions shape brain dynamics and computation across species

## Core question

Are competitive (inhibitory) interactions between brain regions, alongside cooperative (excitatory) interactions, essential for faithfully reproducing empirical brain dynamics and enabling computational capacity in the mammalian connectome?

## Motivation / gap

- Whole-brain computational models traditionally rely on cooperative (excitatory) coupling between brain regions via structural connectivity, ignoring the role of competitive (inhibitory) long-range interactions
- It is unclear whether competitive interactions are dynamically and computationally relevant at the macroscale connectome level, despite their well-established importance at the circuit level
- Existing models fail to simultaneously capture both the spatial structure and temporal dynamics of empirical functional connectivity
- The contribution of competitive interactions to information-theoretic properties (synergy, redundancy) and computational capacity of brain networks has not been systematically investigated across species

## Core contribution (bullet form)

- Demonstrate using whole-brain computational modeling that the architecture of models which most faithfully reproduce empirical brain activity consistently combines modular cooperative interactions with diffuse, long-range competitive interactions across human, macaque, and mouse
- Show that models with competitive interactions achieve up to two-fold improvement in fitting empirical functional connectivity compared to cooperative-only models
- Reveal that competitive interactions spontaneously give rise to greater synergistic information, hierarchical information flow, and realistic metastability without explicit optimization for these properties
- Demonstrate superior computational performance of connectome-based neuromorphic reservoir computing networks when competitive interactions are included
- Provide a cross-species validation framework establishing the evolutionary conservation of competitive interaction architecture

## Method in brief

Whole-brain computational modeling using coupled neural mass models (Hopf bifurcation oscillators) with connectivity derived from species-specific structural connectomes. Two model variants compared: cooperative-only (positive coupling via structural connectivity) versus cooperative-competitive (positive modular coupling plus negative long-range coupling). Models fitted to species-specific resting-state fMRI data at the single-subject level (human: N=100 from HCP; macaque: N=19; mouse: N=10). Model evaluation via spatial correlation between simulated and empirical functional connectivity, functional connectivity dynamics (FCD), metastability, and information-theoretic measures (synergy, redundancy via partial information decomposition). Reservoir computing framework applied to assess computational capacity of the resulting network dynamics. Cross-species analysis to test evolutionary conservation.

## Target venue

Nature Neuroscience
