# Idea Summary

## Working title
Multi-day Neuron Tracking in High Density Electrophysiology Recordings Using Earth Mover's Distance

## Core question
Can we reliably track the same neurons across multiple recording days (up to ~7 weeks) in high-density extracellular electrophysiology data without relying on firing statistics or functional response properties?

## Motivation / gap
- Longitudinal tracking of single neurons is critical for studying learning, adaptation, and motor stability, but no robust automated method exists for high-density probes
- Existing approaches rely on firing statistics or functional tuning properties, which can change over the timescales of interest (learning, plasticity)
- Brain tissue drifts relative to the chronically implanted probe, causing non-rigid movement that shifts waveform positions and causes neurons to appear/disappear across sessions
- Spike sorting (e.g., Kilosort) is optimized for single sessions; multi-session matching is largely unaddressed
- Template-matching spike sorters involve randomness in initialization, producing inconsistent cluster labels across sessions
- Calcium imaging provides spatial cues for tracking but lacks the temporal resolution of electrophysiology

## Core contribution (bullet form)
- Developed an EMD-based neuron tracking algorithm that matches neurons across days using only physical location and waveform shape, independent of firing statistics
- Achieved 84% average recovery rate across all dataset pairs spanning 1 to 47 days
- Demonstrated ~90% recovery rate for sessions up to one week apart and ~78% for sessions five to seven weeks apart
- Reached 99% accuracy up to one week and 95% accuracy five to seven weeks apart using a 10 um z-distance threshold
- Validated matches using visual receptive field similarity as ground truth in mouse V1 recordings
- Retrieved 552 total tracked neurons with partial or no receptive field information (~12 per dataset pair on average), demonstrating generalization beyond visually responsive units

## Method in brief
The method operates on spike-sorted output from Kilosort 2.5, requiring no manual curation. Only units labeled "good" by Kilosort (KSgood) are considered. The core algorithm uses the Earth Mover's Distance (EMD) optimization, which minimizes total transport cost to match units from one recording session to another. The distance metric between unit i in session 1 and unit k in session 2 is d_ik = d_loc + omega * d_wf, where d_loc is the 3D physical distance between estimated unit positions and d_wf is a waveform dissimilarity score. The weight omega was tuned to maximize recovery rate of reference units.

The procedure has two stages. First, the EMD is applied to estimate rigid (homogeneous vertical) drift between sessions, using the full KSgood population. This drift estimate is subtracted from unit positions to correct for between-day tissue movement. Second, the EMD is applied again on drift-corrected units to produce final unit-to-unit assignments. A z-distance threshold (10 um) is applied post hoc to select physically plausible matches and reject false positives.

Validation relies on "reference units" -- the subset of KSgood units with strong, distinguishable visual responses in both datasets. The visual receptive field similarity (combining peri-stimulus time histogram correlation and visual fingerprint correlation) provides ground truth for assessing matching accuracy. Two tracking strategies are supported: match all sessions to a single anchor session, or match consecutive session pairs and trace units through chains spanning three or more sessions.

## Target venue
eLife
