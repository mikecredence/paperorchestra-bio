## Working title

Lateral entorhinal cortex neurons encode distinct experiential epochs around reward during goal-directed navigation in mice

## Core question

Does the lateral entorhinal cortex (LEC) provide the non-spatial "what" information about reward experience epochs (approach, consumption, departure) that the hippocampus needs to contextualize spatial maps during goal-directed navigation?

## Motivation / gap

- The hippocampus integrates "where" (spatial) and "what" (experiential) information to form episodic memories and guide navigation, but the source of the "what" signal is unknown
- The medial entorhinal cortex (MEC) is known to carry spatial information (grid cells, border cells, head direction cells), but the role of the LEC in reward-guided behavior is poorly understood
- Place cells in the hippocampus show context-dependent and reward-dependent firing (overrepresentation near reward locations, distinct goal approach vs departure signals), implying upstream non-spatial input
- Previous LEC studies have been limited by inability to perform two-photon calcium imaging in this anatomically challenging lateral structure during behavior
- No study has dissociated object coding from reward experience coding in LEC, or shown how LEC representations respond when reward location changes

## Core contribution (bullet form)

- Developed a novel two-photon imaging method using a microprism implant to access the LEC in head-fixed behaving mice, recording ~500 active neurons per imaging field (range 150-843 across 47 imaging fields)
- Discovered three functionally distinct neuronal populations in LEC: pre-reward (goal approach), reward consumption active (RCA), and post-reward (goal departure) populations
- Demonstrated that when reward location is moved, pre-reward and post-reward populations immediately shift their representations to track the new reward location, while maintaining their functional identity
- Showed that these populations are largely invariant to spatial location and environment, unlike MEC spatial cells
- Found via optogenetic inhibition of LEC that silencing LEC disrupts learning of a new reward location but does not impair behavior at an already-learned reward location
- Identified that pre-reward population activation can be modeled as a state transition (hidden Markov model) rather than a gradual ramp, with transition points variable across laps

## Method in brief

The key technical innovation was a surgical preparation for two-photon calcium imaging of the LEC in behaving mice. Because the LEC is situated ventral to the rhinal fissure as a lateralized structure, direct optical access requires approaching at >90 degrees to horizontal. A cranial window (3 mm round coverslip) with an attached 2.0 mm square microprism was implanted to rotate the imaging plane 90 degrees. GCaMP6s transgenic mice were used, and imaging was performed with a conventional upright two-photon microscope accessing depths >250 um. Fields of view were approximately 700 x 700 um.

Mice were head-fixed on a treadmill traversing a 3.1 m linear virtual reality track with water reward delivered at a specific location (e.g., 2.3 m). The track was visually cue-rich but the reward location was not marked by any visual feature. Movies were motion corrected and cells segmented using Suite2p. A novel iterative algorithm was used for neuropil correction, baseline adjustment, and deconvolution of calcium transients. Spatial cells were identified by comparing firing peak distributions to shuffled data. Pre-reward and post-reward populations were classified based on the location of their firing peaks relative to reward. Reward relocation experiments moved reward to a new position mid-session. Optogenetic experiments used Arch-expressing mice with bilateral fiber placement over LEC. A hidden Markov model was fit to pre-reward population activity to distinguish recruitment vs state-change models of ramping activity.

## Target venue

Nature Neuroscience
