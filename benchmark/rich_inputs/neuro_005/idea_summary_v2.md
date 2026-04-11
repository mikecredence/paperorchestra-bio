## Working title

Competitive long-range interactions in the mammalian connectome shape brain dynamics, hierarchy, and computational capacity across species

## Core question

Do competitive (inhibitory/negative-signed) interactions between brain regions at the macroscale play a meaningful role in shaping brain dynamics and computation, and if so, how do they complement the traditionally assumed cooperative (excitatory/positive-signed) interactions in the structural connectome?

## Motivation / gap

- Connectome-based generative models of brain activity universally assume that anatomical connections represent cooperative (positive) interactions, because tract-tracing and diffusion tractography only produce positive weights
- Yet competitive interactions are a ubiquitous organizational principle across dynamical systems and are fundamental at the microscale (inhibitory synapses), raising the question of whether they also matter at the macroscale
- Spontaneous brain activity shows systematic anti-correlated patterns, but their mechanistic origin from structural connectivity is unclear
- No existing whole-brain model has systematically tested whether allowing negative effective connectivity improves model fit to empirical functional dynamics
- The computational consequences of competitive interactions for information processing and neuromorphic computing have not been examined

## Core contribution (bullet form)

- Developed species-specific whole-brain generative models (human N=100, macaque N=19, mouse N=10) using Stuart-Landau oscillators near the Hopf bifurcation, allowing both cooperative and competitive effective connectivity to emerge from fitting
- Models with competitive interactions consistently outperformed cooperative-only models across all three species, achieving up to 0.95 correlation between real and simulated functional connectivity
- Competitive interactions spontaneously produced better fit to un-optimized dynamical properties: metastability closer to empirical levels, greater synergistic information, and enhanced local-global hierarchy
- The architecture of competitive interactions was diffuse and long-range, contrasting with modular cooperative interactions, consistent across species
- Competitive effective connectivity produced greater differential identifiability (subject-specificity) of functional connectomes
- Neuromorphic reservoir computing with competitive generative connectivity showed superior computational performance on memory tasks compared to cooperative-only connectivity

## Method in brief

The core model couples nonlinear Stuart-Landau oscillators (one per brain region) poised just below the critical Hopf bifurcation. Each oscillator's dynamics are governed by a parameter controlling its distance from bifurcation and its intrinsic frequency. Regions are interconnected via species-specific structural connectivity: diffusion tractography for humans (100 HCP subjects, Schaefer-100 parcellation), tract-tracing augmented with CoCoMac for macaque (19 subjects), and Allen Institute tract-tracing for mouse (10 subjects). Structural connectomes for macaque and mouse were symmetrized for cross-species comparison.

Connection weights are iteratively updated at the single-subject level to minimize the difference between empirical and simulated functional connectivity (both zero-lag and lagged). In the competitive model, the sign of each connection is also allowed to vary -- negative-signed (competitive) effective connectivity is allowed but not imposed. After convergence, the recovered signed weights represent the generative effective connectivity. Two model variants are compared: cooperative-only (all weights positive) and cooperative+competitive (signs allowed to flip).

The resulting models are evaluated on explicitly optimized metrics (FC correlation) and emergent properties not used during fitting: metastability (temporal variability of Kuramoto order parameter), synergy (using partial information decomposition), local-global hierarchy (intrinsic-driven ignition), and cognitive matching (correlation with 123 NeuroSynth meta-analytic maps). Computational capacity was assessed using reservoir computing, where the effective connectivity served as the reservoir's recurrent weight matrix in a memory task.

## Target venue

Nature Neuroscience
