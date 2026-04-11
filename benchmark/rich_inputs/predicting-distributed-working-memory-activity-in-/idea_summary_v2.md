# Idea Summary

## Working title
Predicting Distributed Working Memory Activity in a Large-Scale Mouse Brain: The Importance of the Cell Type-Specific Connectome

## Core question
How does a macroscopic gradient of parvalbumin-expressing (PV) interneuron density, combined with cell type-specific long-range connectivity, shape distributed working memory representations across the mouse cortex?

## Motivation / gap
- Distributed persistent neural activity during working memory delay periods has been observed across many mouse brain regions, but the circuit mechanism is poorly understood
- In macaques, cortical hierarchy and excitatory spine gradients explain persistent activity patterns; the mouse cortex lacks a comparable excitatory gradient, suggesting a fundamentally different mechanism
- Existing connectome-based models of mouse cortex have not incorporated cell type-specific targeting (excitatory vs inhibitory) of long-range projections
- It is unclear whether persistent firing in delay-dependent tasks is generated locally or depends on long-distance reverberation among multiple brain regions
- The role of thalamocortical loops in sustaining distributed working memory has not been modeled at scale in mice

## Core contribution (bullet form)
- Built the first biologically-based large-scale model of 43 mouse cortical areas with a measured PV interneuron density gradient (Pearson r = -0.35 between PV fraction and hierarchy, p < 0.05)
- Demonstrated that working memory coding is distributed yet modular: areas with low PV cell fraction sustain activity while high-PV sensory areas respond only transiently
- Introduced a counterstream inhibitory bias (CIB) rule for long-range projections where feedforward connections preferentially target excitatory neurons and feedback connections preferentially target PV interneurons
- Showed that cell type-specific graph measures (involving both connectivity strength and PV density) predict persistent activity patterns better than standard connectomic measures
- Extended the model to include 40 thalamic nuclei, demonstrating that thalamocortical interactions help maintain distributed persistent activity
- Identified multiple self-sustained internal states (each engaging a distinct subset of areas), suggesting high memory capacity in the cortical network

## Method in brief
Each cortical area is modeled as a local circuit with excitatory and inhibitory (PV) populations governed by coupled differential equations. Inter-areal connectivity is based on the Allen Institute mesoscopic connectome data (anterograde fluorescent tracers) within a 43-area parcellation. The PV cell fraction gradient is obtained from the qBrain mapping platform. The key model feature is a counterstream inhibitory bias: the fraction of long-range excitatory input targeting local inhibitory neurons scales with hierarchical distance, following the rule m_ij = m_E + (m_I - m_E) * delta_ij where delta_ij encodes the hierarchical relationship between areas.

The model operates in two dynamical regimes: one where local recurrent excitation alone cannot sustain persistent activity (requiring long-range reverberation), and one where local excitation is sufficient. In the reference regime, parameters include cortical excitatory self-coupling (gE,self = 0.4 nA), base inhibitory strength (gEI,0 = 0.192 nA), and long-range coupling (muEE = 0.1 nA). The thalamocortical extension adds 40 thalamic areas with corticothalamic and thalamocortical connection matrices. Working memory is simulated by applying a brief sensory input (500 ms) to a primary sensory area and measuring delay-period firing rates across the network.

## Target venue
eLife
