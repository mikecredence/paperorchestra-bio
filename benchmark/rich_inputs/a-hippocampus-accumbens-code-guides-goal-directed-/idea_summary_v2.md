# Idea Summary

## Working title
A hippocampus-accumbens code guides goal-directed appetitive behavior

## Core question
What specific spatial and behavioral information do dorsal hippocampal neurons projecting to the nucleus accumbens (dHPC->NAc) carry, and how does this projection-specific coding support goal-directed navigation toward hidden rewards?

## Motivation / gap
- The hippocampus encodes rich spatial and non-spatial task features, but which information is routed to specific downstream targets remains largely unknown
- The nucleus accumbens is proposed to transform hippocampal spatial codes into motivation-driven motor commands, yet direct evidence for this transformation is sparse
- Previous studies showed that disabling HPC->NAc projections diminishes conditioned place preference, but the actual coding content of this projection during behavior has not been characterized at scale
- Most prior work used electrophysiology, limiting the number of simultaneously recorded projection-identified neurons
- It is unknown whether NAc-projecting hippocampal neurons carry enriched reward zone representations, speed coding, or licking-related signals compared to the general population

## Core contribution (bullet form)
- Used dual-color two-photon imaging to simultaneously record from large populations of hippocampal neurons, distinguishing NAc-projecting (dHPC->NAc) from non-projecting (dHPC-) neurons during goal-directed navigation in head-fixed mice
- Found that dHPC->NAc neurons have a larger proportion of place cells with enhanced spatial information, greater trial-to-trial reliability, and stronger in-place-field activity
- Demonstrated that dHPC->NAc place fields over-represent the reward zone and are more strongly modulated by local belt cues
- Showed that speed-inhibited (deceleration) cells are overrepresented among dHPC->NAc neurons, while lick-excited neurons are also enriched in this projection
- Optogenetic stimulation of dHPC terminals in NAc induced mouth movements and deceleration, confirming functional relevance
- A generalized linear model (GLM) revealed enhanced conjunctive coding of position, velocity, and licking in dHPC->NAc neurons, improving reward zone identification

## Method in brief
Food-restricted mice were trained on a head-fixed spatial reward learning task using a 360 cm self-propelled treadmill belt with six textured zones and one hidden 30 cm reward zone. Mice learned across five training days to lick a spout in the reward zone to receive liquid reward. Behavioral metrics included licking in an anticipation zone (30 cm before reward) and the reward zone itself, tracked via infrared cameras for orofacial movements.

For neural recordings, Thy1-GCaMP6s mice received retrograde AAVrg-Cre injections in the medial NAc and DIO-mCherry in dHPC (CA1/subiculum border). This enabled dual-color two-photon imaging: dynamic GCaMP6s calcium signals from all neurons plus static mCherry labeling of NAc-projecting neurons. Place cells were identified using spatial information criteria, speed modulation was assessed via linear regression on calcium events vs. velocity bins, and lick-related activity was quantified around appetitive lick onsets.

For optogenetics, separate C57Bl/6 mice received CaMKII-ChR2 or control EYFP in dHPC, with fiber optic cannulae targeting NAc. Stimulation was delivered during treadmill running to assess effects on mouth movement and velocity. A GLM was used to model each neuron's calcium activity as a function of position, velocity, and appetitive licking, with conjunctive coding quantified by comparing full vs. reduced models using likelihood ratio tests.

## Target venue
Nature Communications
