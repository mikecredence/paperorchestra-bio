# Experimental Log: Local contribution to the somatosensory evoked potentials in rat’s thalamus

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 3RESULTS3.1LFP in the barrel cortex and thalamic areaWe recorded whisker-evoked field potentials in the primary somatosensory cortex and in the somatosensory thalamus of the rat’s right hemisphere (Fig.
- 1A) and repeated this paradigm with three different experimental setups (see Methods).
- Example results for simultaneous thalamo-cortical recordings done with a 384 channel Neuropixels probe are presented in Fig.
- Note that during the strongest negative wave recorded in the cortex, around 10 ms poststimulus (see ‘oo’ mark in Fig.
- 1C), a negative deflection of the potential recorded in the thalamus occurs.
- To quantify similarity of thalamic and cortical EPs, in each rat we computed their correlation in a 3 ms window rolling along EP waveforms (Fig.
- For a group of 11 rats, the correlation value above 0.5 was observed around 10–12 ms after the stimulus.Similarity of the cortical and thalamic negative waves around 10 ms suggests that they may reflect partly the same currents, which — observed from different distances — result in waves of larger (
- The largest wave around 10 ms post stimulus is the negative deflection in the cortical middle layers; but at the same latency, the potentials at the bottom of the cortex have a clear positive polarity (Fig.
- 2C, the strong negative cortical field has a very long range.
- The purple stripe around 10 ms is only transiently reversed at the bottom of the cortex, and it is evident in a whole sub-cortical space below.
- volume conduction) from cortical currents and their possible impact on distal (thalamic) potential values.biorxiv;2023.05.25.541803v2/FIG2F2fig2Figure 2.A: Example spatiotemporal EP profile from Neuropixels probe (same data as in Fig.
- 1B) presented as a 3D color map.
- Note a stripe of negative (purple) potential around 10 ms spreading from cortical sources to deep subcortical levels, which may modify thalamic waveforms.
- In all panels, horizontal axis shows the time with respect to the stimulus (applied at t=0); left vertical axis shows recording depth; colorbars on the right of each panel show the magnitude of potential (A and C, [mV]) and current source density (B, [µA/mm3]).
- Vertical dotted lines at time 0 mark the stimulus onset and related artefact in the data.We thus stated a hypothesis that a strong activity from middle cortical layers can be seen even 3 mm from the source and can overshadow subcortical signals, and we propose a general CSD-based pipeline to recover
- This analytical pipeline is of general validity even if here it is illustrated with examples from the primary somatosensory pathway.3.2CSD reconstruction and forward modelingGenerally used approach to extract local activity from LFP is the CSD method.
- 2A) is plotted as a spatio-temporal profile along electrode track (Fig.
- 3).biorxiv;2023.05.25.541803v2/FIG3F3fig3Figure 3.Comparison of measured EPs with their counterparts computed from subsets of current sources (example from an experiment using 8x8 Neuronexus probes).
- Panels in the first row (A1, B1 and C1) show schematic representations of sources reconstruction space (black dots: electrode positions; blue dots: subset of CSD used for computation of cortical (B) and thalamic (C) contributions to the EPs.
- Note a lateral gradient of EP amplitude in the cortex — NeuroNexus A8x8 silicon probe was inserted on the edge of barrel field (see Suppl.
- In the thalamus (A3, B3, C3) we can spot two clusters of early evoked responses — one (middle-right area) around the main whisker representation in VPM/PoM complex, the other (lower edge) corresponding to zona incerta nucleus.
- (A) All the cortical and thalamic sources were used for computed EPs shown in A2, A3 panels.
- (B) Cortical contributions to the measured EPs (B2, B3).
- Estimated potentials fit well cortical measurements (B2) and show similarities with thalamic recordings (B3).
- (C) Thalamic contributions to the measured EPs (C2, C3).
- On the other hand, the truly local part of the thalamic LFP, which is that estimated from thalamic sources (dashed orange line), is different from the measured EPs, which are contaminated by passively propagated strong cortical signal (dashed blue line in B3).3.3LFP reconstruction from subset of sou
- 3 with an example from one of 2D EP profiles obtained with A8x8 NeuroNexus probe.
- 3A1–A3; as required by self-consistent properties of kCSD).
- 3B2) which indicates that cortical potential has indeed mainly local origin.
- 3C2).This is not the case in the thalamus.
- 3C3, dashed orange) is much closer to the measured potentials than the cortex based estimation (Fig.
- 3B3, dashed blue) but on average more positive.
- Clearly, the LFP recorded in the thalamus contains a mix of thalamic and cortical contributions each of which must be recovered with the help of CSD methods.3.4Estimating overall effect of cortical LFP volume conductionFig.
- 4A shows enlarged overlay of exemplary measured and estimated, cortical and thalamic, EPs (examples from Fig.
- Real EP trace tended to be more negative, in particular from around 6 to 14 ms, than the reconstructed ones (see Fig.
- 4B and C for a group summary of EP amplitute at 10 ms post stimulus, B: permutation paired-test, p-value=0.002, n=11, C thalamic channels: 1 sample ttest, p-value=0.013, C cortical channels: 1 sample ttest, p-value=0.44).
- We argue this is a consequence of the strong negative wave conducted from the cortex.biorxiv;2023.05.25.541803v2/FIG4F4fig4Figure 4.A: Examples of measured and reconstructed potential from central cortical (cyan and dotted-blue, left Y axis) and thalamic sites (orange and red-dashed, right Y axis) f
- B: Potential values at 10 ms after whisker stimulation in recorded thalamic EPs and their reconstructions.
- Note significantly less negative values in reconstructed data (permutation paired-test, p-value=0.002, n=11.
- C: Absolute reconstructed-minus-measured values for thalamic (red) and cortical (blue) potential wave at 10 ms post-stimulus.
- There is a significant difference from 0 in the thalamic area, (1 sample ttest, t=3.03, p-value=0.013, n=11) but not in the cortex (1 sample ttest, t=0.8, p-value=0.44, n=11) D: Average correlation score in cortical channels between measured EPs and EPs reconstructed from cortical (blue) or thalamic
- Shaded corridor along line-plots in B and C represent SEM (n=11 rats).To quantify the similarities and differences between the waveforms of measured EPs and reconstructed contributions from thalamic and cortical sources we calculated their correlations in a 3 ms window running along the EP traces.
- Group averaged results (n=11 rats) are presented in Fig.
- 4D) was close to one throughout the analyzed time (25 ms) when reconstructed from cortical sources and it was close to zero or negative when comparing measurements with contributions to cortical potentials from thalamic sources.Correlation coefficient for thalamic waveforms measured and reconstructe
- 4E, red line) was the highest (0.87±0.05) in the early post stimulus window, fell down after 5 ms and was close to zero (0.21±0.14) at 14 ms (Fig.
- Correlation was close to zero in an early window up to 5 ms post stimulus but then increased reaching a maximum up to 0.59±0.18 around 11 ms and then dropped again.This group analysis confirmed that strong cortical currents indeed may strongly affect the field potentials recorded in the thalamus.
- This influence was maximal in a time window between 10 and 15 ms, when LFP recorded from thalamus was defined predominantly by cortical sources.3.5Detecting weak thalamic activity in the CSD spaceOur analyses showed that thalamic LFP can be substantially contaminated by passive contributions from st
- How to optimally choose CSD reconstruction space in a model-based reconstruction method such as kCSD?To address these issues we considered four analytical setups using data from an experiment with two independent A8x8 silicon probes (Fig.
- In consecutive analyses we assumed that either (1) only the thalamic electrode was used, probing relatively weak thalamic responses, or (2) both electrodes were used, one in thalamus and the other in the cortex, probing the stronger cortical activity.
- 5, top row).biorxiv;2023.05.25.541803v2/FIG5F5fig5Figure 5.The first row shows the analytical setup used in the analysis in a given column.
- Rows A1–A3 show CSD reconstructions snapshots at 5, 10 and 20 ms after stimulus that were analyzed assuming setups indicated in the first row.
- Coronal plane corresponds to ∼ 3 mm posterior from bregma point.
- 5B–D), the other was erroneous (Fig.
- 5A)c— where we tried to explain simultaneously strong cortical and weak thalamic recordings with sources placed only in the thalamus.
- 5B, where the reconstruction space is a region in the thalamus containing the electrodes with a 0.5 mm margin to accommodate possible artifacts from remote sources, and in Fig.
- 5C, where the information is taken from both thalamic and cortical electrodes and reconstruction space covers all electrode positions.
- 5C with a strong non-physiological dipolar halo surrounding the thalamic electrodes (Fig.
- 5A), which could not be aligned with the anatomy of thalamic nuclei, and which is a clear artifact.The results shown in Fig.
- 5B–D provide similar patterns of detailed thalamic currents, clearly and reasonably aligned with the histology.
- Clusters of earliest sinks and sources (5 ms, Fig.
- 5A1–D1) were localized precisely in the regions receiving direct peripheral input — the dorsal sector of VPM and PoM, and zona incerta.
- 5, rows 2–3), which in the LFP picture would be overflown by the strong cortical negative wave.
- 5B to D was a reduction in magnitude of thalamic currents (compare colour intensity between B and C–D in Fig.
- 5), however the source pattern was the same.
- 5D) did not significantly affect the pattern of reconstructed CSD in the thalamus, i.e.
- This is what we expect from traditional approaches to CSD estimation using three-point second derivative Pitts (1952) and it is also true here for this model-based analysis.

## Figure Descriptions

### Figure 1.
A: Schematic picture of the sensory pathway from the whisker pad to the thalamus (PoM and VPM) and somatosensory barrel cortex (BCx, both clearly visible on cytochrome oxidase stained coronal slice of a rat brain). Blue arrows indicate information flow from periphery to the cortex and a recurrent co

### Figure 2.
A: Example spatiotemporal EP profile from Neuropixels probe (same data as in Fig. 1B) presented as a 3D color map. B: Spatiotemporal CSD profile estimated from data in A. Note evident current sinks and sources in the thalamic region. C: Spatiotemporal profile of EPs estimated in the whole cortico-th

### Figure 3.
Comparison of measured EPs with their counterparts computed from subsets of current sources (example from an experiment using 8x8 Neuronexus probes). Panels in the first row (A1, B1 and C1) show schematic representations of sources reconstruction space (black dots: electrode positions; blue dots: su

### Figure 4.
A: Examples of measured and reconstructed potential from central cortical (cyan and dotted-blue, left Y axis) and thalamic sites (orange and red-dashed, right Y axis) from Figure 3 B2 and C3 panels. Solid lines represent measured potentials, dashed lines represent reconstructed potential from local 

### Figure 5.
The first row shows the analytical setup used in the analysis in a given column. The dots represent the electrodes taken into consideration. The frame indicates area where sources were assumed (basis sources were placed). A: Recordings from the thalamus and cortex considered; sources assumed only in

## References
Total references in published paper: 72

### Key References (from published paper)
- Voltage imaging to understand connections and functions of neuronal circuits (, 2016)
- Thalamo-cortical processing of vibrissal information in the rat. II. spatiotemporal convergence in t (, 1991)
- Comparing the feature selectivity of the gamma-band of the local fi eld potential and the underlying (, 2008)
- Volume-Conducted origin of the field potential at the lateral habenula (, 2020)
- The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes (, 2012)
- What we can and what we cannot see with extracellular multielectrodes (, 2021)
- kCSD-python, a tool for reliable current source density estimation (, 2019)
- Local field potential (, 2013)
- Somatic sensory responses in the rostral sector of the posterior group (pom) and in the ventral post (, 1992a)
- Somatic sensory responses in the rostral sector of the posterior group (POm) and in the ventral post (, 1992b)
- Modelling and analysis of local field potentials for studying the function of cortical circuits (, 2013)
- How the barrel cortex became a working model for developmental plasticity: A historical perspective (, 2020)
- A review of organic and inorganic biomaterials for neural interfaces (, 2014)
- Neo: an object model for handling electrophysiology data in multiple formats (, 2014)
- An evaluation of the conductivity profile in the somatosensory barrel cortex of Wistar rats (, 2010)
- Interactions between the lateral habenula and the hippocampus: implication for spatial memory proces (, 2013)
- Collection of Simulated Data from a Thalamocortical Network Model (, 2017)
- Independent components of neural activity carry information on individual populations (, 2014)
- Generalized laminar population analysis (gLPA) for interpretation of multielectrode data from cortex (, 2016)
- Lemniscal and Extralemniscal Compartments in the VPM of the Rat (, 2008)
- Array programming with NumPy (, 2020)
- Local field potentials: Myths and misunderstandings (, 2016)
- Differential effects produced by ketamine on oscillatory activity recorded in the rat hippocampus, d (, 2011)
- Decoding local field potentials for neural interfaces (, 2017)
- Fully integrated silicon probes for high-density recording of neural activity (, 2017)
- Modular data acquisition system for recording activity and electrical stimulation of brain tissue us (, 2021)
- How local is the local field potential? (, 2011)
- A new method of the description of the information flow in the brain structures (, 1991)
- Local origin of field potentials in visual cortex (, 2009)
- Cross-population coupling of neural activity based on gaussian process current source densities (, 2021)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 72