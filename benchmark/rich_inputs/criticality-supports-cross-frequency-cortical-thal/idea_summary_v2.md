## Working title
Edge-of-Chaos Criticality Mediates Cross-Frequency Cortical-Thalamic Information Transfer During Consciousness

## Core question
Does bidirectional information transfer between cortex and thalamus rely on a specific cross-frequency spectral channel, and is this channel mediated by the proximity of slow thalamocortical dynamics to edge-of-chaos criticality -- explaining why it breaks down during unconsciousness and is enhanced during psychedelic states?

## Motivation / gap
- Consciousness is thought to require preserved bidirectional cortical-thalamic communication, but the spectral mechanisms of this communication are poorly characterized
- Unconsciousness (anesthesia, seizures) consistently coincides with disrupted cortical-thalamic communication, yet the mechanistic link is unknown
- Criticality (the phase transition between order and chaos) has been separately linked to both information processing capacity and waking brain states, but never directly to cortical-thalamic communication
- No study had systematically profiled frequency-specific directed information transfer between thalamus and cortex across multiple species and multiple states of consciousness
- The relationship between edge-of-chaos dynamics and cross-frequency neural communication had not been formalized or tested empirically
- Existing measures of cortical-thalamic coupling (e.g., phase-amplitude coupling, broadband transfer entropy) lack the spectral resolution needed to identify frequency-specific communication channels

## Core contribution (bullet form)
- Identified a highly conserved spectral channel across humans, mice, and rats: information sent via delta/theta/alpha waves (~1.5-13 Hz) from one structure is encoded by high gamma (~50-100 Hz) in the other
- Demonstrated this cross-frequency cortical-thalamic transfer is significantly reduced during propofol anesthesia and generalized spike-and-wave seizures (unconscious states)
- Showed that the psychedelic 5-MeO-DMT enhances low-to-high frequency corticothalamic information transfer (cortex-to-thalamus direction)
- Established via numerical simulations (mean-field basal ganglia-thalamocortical model with Bayesian-genetic optimization) that edge-of-chaos criticality of slow thalamocortical dynamics mediates these changes
- Demonstrated that non-spectrally-resolved transfer entropy and phase-amplitude coupling do NOT show consistent relationships with consciousness, highlighting the importance of spectral resolution

## Method in brief
Spectrally resolved directed information transfer was measured using a recently developed surrogate-based method that quantifies how many bits of transfer entropy are lost when dynamics within specific frequency ranges are randomized. This was applied to simultaneous thalamic-cortical electrophysiology recordings from: (1) human essential tremor patients (Vim thalamus / sensorimotor cortex), (2) Long-Evans rats (ventral posterior thalamus / somatosensory cortex), (3) C57/BL6 mice (mediodorsal thalamus / medial prefrontal cortex), and (4) GAERS rats (ventral posterior thalamus / contralateral somatosensory cortex). After an initial exploratory sweep across all frequency-pair combinations, a candidate channel was identified (low-frequency ~1.5-13 Hz to high gamma ~52-104 Hz) and subjected to rigorous surrogate testing.

Brain state manipulations included propofol anesthesia (humans and rats), generalized spike-and-wave seizures (GAERS rats), and 5-MeO-DMT psychedelic administration (mice). Statistical significance was evaluated using one-tailed Wilcoxon signed-rank tests across conditions within each species.

A modified mean-field model of the basal ganglia-thalamocortical system was developed based on prior work, with parameters optimized via Bayesian-genetic methods to match empirical waking-state electrodynamics. The model uses sigmoidal firing rate functions (Q_a as a function of membrane potential relative to threshold), synaptic response kernels parameterized by decay rate alpha and rise rate beta, and was specifically modified to simulate GABAergic anesthesia by modulating synaptic decay without altering maximal postsynaptic current. Proximity to edge-of-chaos criticality was quantified via the Lyapunov exponent of the system, and its relationship to cross-frequency information transfer was examined in silico.

## Target venue
eLife
