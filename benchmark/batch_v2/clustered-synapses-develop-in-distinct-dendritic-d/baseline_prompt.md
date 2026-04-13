Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title

Clustered synapses emerge in distinct dendritic domains of visual cortex pyramidal neurons before eye opening

## Core question

How do functionally clustered synaptic inputs assemble onto layer 2/3 pyramidal cell dendrites during early postnatal development in mouse visual cortex, and what role does local co-activity play in synaptic organization before the onset of visual experience?

## Motivation / gap

- Adult cortical neurons exhibit synaptic clustering (neighboring synapses share similar activity/tuning), which is essential for dendritic computation, but when and how this organization emerges during development is unknown
- Electron microscopy has shown that excitatory synapses appear during the first postnatal week and peak near P14 (eye opening), but these structural data do not reveal functional organization at the single-synapse level in vivo
- Previous in vivo calcium imaging studies mapped synaptic inputs in adult cortex, but no study has done so in neonatal cortex where many synapses form directly on the dendritic shaft (not on spines)
- It is unclear whether synaptic clustering requires visual experience or whether it is established by spontaneous network activity before eye opening
- The relationship between local synaptic co-activity and synapse stabilization/potentiation during early development has not been examined

## Core contribution (bullet form)

- Mapped 354 functional synapses producing 3,440 transmission events across 12 dendritic areas from 11 mice aged P8-P13 using concurrent in vivo two-photon calcium imaging and whole-cell patch clamp
- Demonstrated that functional synapse density increased several-fold during the second postnatal week (P8-P13), with both spine and shaft synapses contributing
- Found that at P8-P10 synapses assembled in confined dendritic segments while other segments remained devoid of inputs; by P12-P13 dendrites were nearly entirely covered by domains of co-active synapses
- Identified distinct dendritic domains of clustered, co-active synapses that expand and increase in synapse number during development
- Showed that local co-activity with neighboring synapses correlates with synaptic stabilization and potentiation, suggesting a plasticity mechanism for domain formation
- Approximately 20% of synapses were highly active while most showed rare transmission, indicating release probability differences rather than firing rate differences drive the observed distribution

## Method in brief

The study used in utero electroporation at E16.5 to express GCaMP6s and DsRed in layer 2/3 pyramidal neurons of mouse primary visual cortex. Between P8 and P13, concurrent in vivo two-photon calcium imaging and somatic whole-cell voltage-clamp recording were performed under light isoflurane anesthesia. Neurons were held at -30 mV to enhance NMDA receptor-mediated calcium transients at synapses, while action potentials were blocked with intracellular QX-314, allowing unambiguous detection of individual synaptic transmission events at both spine and shaft synapses without contamination from back-propagating action potentials.

Resonant scanning combined with piezo-driven z-positioning enabled imaging of large dendritic areas. Individual synaptic calcium transients were detected and mapped to precise dendritic locations. Synapses were classified as spine or shaft based on morphology in the DsRed channel. Synaptic domains were identified as contiguous dendritic segments containing co-active synapses. Co-activity scores quantified the degree to which each synapse fired synchronously with its neighbors within a domain. Changes in transmission frequency over the recording period were used to assess synaptic potentiation and depression, and these changes were correlated with the co-activity score to test whether local synchrony promotes synaptic stabilization.

## Target venue

eLife


## Experimental Log

# Experimental Log: Clustered Synapses Develop in Distinct Dendritic Domains in Visual Cortex Before Eye Opening

## 1. Animal and Experimental Overview

| Parameter | Value |
|---|---|
| Species/strain | C57BL/6J mouse |
| Number of animals | 11 |
| Age range | P8 to P13 |
| Brain region | Primary visual cortex (V1), layer 2/3 |
| Number of dendritic areas imaged | 12 |
| Total functional synapses mapped | 354 |
| Total synaptic transmission events | 3,440 |
| Anesthesia | Isoflurane (2% induction, 0.7-1% maintenance) |

## 2. Molecular Tools and Electrophysiology Parameters

| Component | Detail |
|---|---|
| Calcium indicator | GCaMP6s (in pCAGGS) |
| Structural marker | DsRed Express (in pCAGGS) |
| Transfection method | In utero electroporation at E16.5 |
| GCaMP6s concentration | 2 mg/ml |
| DsRed concentration | 0.5-2 mg/ml |
| Electroporation | 5 square wave pulses, 30 V, 50 ms duration, 950 ms interval |
| Patch pipette resistance | 4.5-6 MOhm |
| Pipette coating | BSA-Alexa 594 (for visualization) |
| Recording mode | Voltage clamp |
| Holding potential | -30 mV (to enhance NMDA receptor activation) |
| Action potential blocker | QX-314 (intracellular) |
| Current recording | 10 kHz sampling, 3 kHz filter (Multiclamp 700b) |

### Intracellular Solution Composition

| Component | Concentration |
|---|---|
| CsMeSO3 | 120 mM |
| NaCl | 8 mM |
| CsCl2 | 15 mM |
| TEA-Cl | 10 mM |
| HEPES | 10 mM |
| QX-314 bromide | 5 mM |
| MgATP | 4 mM |
| Na-GTP | 0.3 mM |

## 3. Imaging Setup

| Parameter | Value |
|---|---|
| Microscopy | Two-photon with resonant scanning |
| Z-positioning | Piezo-driven (multi-plane imaging) |
| Purpose of DsRed channel | Somatic targeting and structural identification of spines vs shaft |
| Purpose of GCaMP6s channel | Detection of synaptic calcium transients |

## 4. Synapse Classification

| Synapse Type | Identification Criterion | Calcium Signal Characteristics |
|---|---|---|
| Spine synapse | Located on morphologically identified spine in DsRed channel | Clear, isolated calcium transient on spine head |
| Shaft synapse | Located directly on dendritic shaft (no spine structure) | Calcium transient detectable only when APs are blocked (QX-314) |

Fig 2A: Example of synaptic transmission at a spine synapse with clearly detectable calcium increase.
Fig 2B: Example of synaptic transmission at two neighboring shaft synapses.
Fig 2C: Schematic of all functional synapses on an example neuron; yellow discs = spine synapses, blue discs = shaft synapses; disc diameter indicates transmission frequency.

## 5. Developmental Changes in Synapse Density and Transmission (Figure 3)

### 5.1 Synapse Density Over Development

| Age Group | Approximate Synapse Density (per 100 um dendrite) | Trend |
|---|---|---|
| P8-P9 | Low (sparse) | Few functional synapses, large gaps between inputs |
| P10-P11 | Intermediate | Increasing density |
| P12-P13 | High (approaching adult-like coverage) | Dendrites nearly entirely covered |

Fig 3A: Dendrite plots at P9 and P12 showing dramatic increase in functional synapse density.
Fig 3B: Scatter plot showing synapse density (per 100 um) increases significantly with age from P8 to P13. Each dot represents one experiment.

### 5.2 Transmission Frequency

| Age Group | Transmission Event Frequency | Notes |
|---|---|---|
| P8-P10 | Lower | Fewer total events per synapse |
| P11-P13 | Higher (several fold increase) | Both spine and shaft synapses increase in activity |

Fig 3: The frequency of transmission events increased several fold across the P8-P13 developmental window.

### 5.3 Distribution of Transmission Frequencies

| Category | Fraction of Synapses | Activity Level |
|---|---|---|
| Low-activity synapses | ~80% | Rare transmission events |
| High-activity synapses | ~20% | Frequent transmission events |

The distribution of synaptic transmission frequencies is very long-tailed: most synapses fire rarely, while roughly 20% are highly active. This skewed distribution likely reflects release probability differences between presynaptic terminals rather than differential firing rates of presynaptic neurons.

## 6. Synaptic Transmission at Synapse and Soma Level (Figure 4)

Fig 4A: Simultaneous recording of synaptic transmission events (calcium imaging) and synaptic currents (somatic voltage clamp) at P10. Most transmission events occurred during barrages of spontaneous network activity.

| Observation | Detail |
|---|---|
| Barrage structure | Synaptic transmission events clustered in time during network barrages |
| Individual synapse resolution | Different synapses on the same dendrite could be distinguished during a single barrage |
| Somatic current correlation | Barrages visible as compound synaptic currents at soma correspond to multiple individual synapse activations along the dendrite |

Fig 4: Colors represent amplitude of individual synaptic transmission events. Grey dots show inactive synapses during each barrage. The somatic whole-cell recording confirmed that imaging-detected events corresponded to actual synaptic currents.

## 7. Spatial Organization of Synapses (Figure 5)

### 7.1 Inter-Synapse Distance Analysis

| Age Group | Median Inter-Synapse Distance (um) | Distribution Shape |
|---|---|---|
| P8-P10 (younger) | Larger | Shifted rightward (more spacing) |
| P11-P13 (older) | Smaller | Shifted leftward (denser packing) |

Fig 5A: Dendrite plot at P8 showing several dendritic segments carrying high synapse density while other segments are devoid of functional inputs.
Fig 5B: Cumulative distribution of inter-synapse distances shows younger dendrites (P8-10) have larger spacing between neighboring synapses compared to older dendrites (P11-13).

### 7.2 Spatial Clustering Assessment

| Feature | P8-P10 | P12-P13 |
|---|---|---|
| Segments with synapses | Confined, patchy distribution | Nearly continuous coverage |
| Segments devoid of synapses | Many | Few |
| Clustering pattern | Synapses assemble in specific confined segments | Domains of co-active synapses cover most of the dendrite |

## 8. Dendritic Domains of Clustered Synapses (Figure 6)

### 8.1 Domain Properties Over Development

| Property | Early (P8-P10) | Late (P12-P13) | Trend |
|---|---|---|---|
| Domain extent (length in um) | Smaller | Larger | Increases with age |
| Number of synapses per domain | Fewer | More | Increases with age |
| Number of domains per dendrite | Few | More | Increases with age |
| Fraction of dendrite covered by domains | Low | High (nearly entire dendrite) | Dramatic increase |

Fig 6A: Dendrite plots at P9 and P12 with individual domains shown in different colors; synapses outside domains in grey. Disc size indicates transmission frequency; high-activity synapses outlined in black.
Fig 6B-C: Domain extent and synapse count per domain increase during development.

### 8.2 Domain Definition

| Parameter | Description |
|---|---|
| Domain identification | Contiguous dendritic segments containing co-active synapses |
| Co-activity criterion | Synapses within a domain fire synchronously above chance levels |
| High-activity synapse labeling | Black outlines on disc representations |

## 9. Co-Activity and Synaptic Plasticity (Figure 7)

### 9.1 Co-Activity Score and Synaptic Fate

| Co-Activity Level | Synaptic Fate | Example |
|---|---|---|
| Low co-activity with neighbors | Synapse depression / elimination (stops transmitting) | Synapse (1) in Fig 7A: very active initially, stopped transmitting by end of recording |
| High co-activity with neighbors | Synapse potentiation / stabilization (increases in activity) | Synapse (2) in Fig 7A: inactive initially, increased transmission and became co-active with neighbors |

Fig 7A: Two example dendrites at P12. Synapse (1) had low co-activity score and was depressed. Synapse (2) had high co-activity score and was potentiated.

### 9.2 Correlation Analysis

| Analysis | Result | Direction |
|---|---|---|
| Co-activity score vs. change in transmission frequency | Positive correlation | Higher co-activity predicts potentiation |
| Co-activity score vs. synaptic stabilization | Positive correlation | Co-active synapses are more likely to persist |

Fig 7D: Model diagram summarizing that synapses are sorted into distinct functional dendritic domains through plasticity mechanisms driven by spontaneous network activity. Co-activity within domains promotes potentiation; out-of-sync activity leads to depression.

## 10. Summary of Key Quantitative Findings

| Metric | Value |
|---|---|
| Total animals | 11 |
| Total dendritic areas | 12 |
| Total functional synapses | 354 |
| Total transmission events | 3,440 |
| Age range | P8-P13 |
| Fraction of highly active synapses | ~20% |
| Developmental trend in synapse density | Several-fold increase P8 to P13 |
| Developmental trend in transmission frequency | Several-fold increase P8 to P13 |
| Domain coverage at P12-P13 | Nearly entire dendrite |
| Eye opening | P14 (all recordings before this milestone) |

## 11. Key Controls and Methodological Considerations

| Issue | Solution |
|---|---|
| Back-propagating APs mask shaft synapse signals | QX-314 in intracellular solution blocks APs |
| Need to detect NMDA-dependent calcium at synapses | Holding potential at -30 mV enhances NMDA receptor activation |
| Anesthesia effects on spontaneous activity | Low isoflurane (0.7-1%) preserves basic spontaneous network activity patterns; prior validation showed participation rates and event amplitudes are maintained |
| Distinguishing spine vs. shaft synapses | DsRed structural channel used for morphological classification |
| Identifying patched neuron among labeled cells | Depolarization to -30 mV triggers transient calcium increase that uniquely labels the patched neuron in GCaMP6s channel |

## 12. Supplementary Figures

- Fig S1: Overview of all 12 imaged dendrites (D1-D12) with each synapse represented as a disc; size indicates transmission frequency, color indicates local co-activity
- Fig S2: All recorded synaptic transmission events across all dendrites; y-axis shows position along dendrite, each event is a disc (yellow = spine, blue = shaft), disc size indicates relative amplitude
- Fig S3: Composite image of DsRed (grey) and GCaMP6s (green) channels after depolarization to -30 mV, demonstrating identification of patched neuron dendrites

## 13. Statistical Methods

| Analysis Type | Method | Notes |
|---|---|---|
| Age-dependent changes in density | Linear regression / correlation | Each dot = one experiment |
| Inter-synapse distance distributions | Cumulative distribution comparison | Younger vs older dendrites |
| Co-activity vs. plasticity correlation | Correlation analysis | Co-activity score correlated with change in transmission frequency |
| Domain identification | Spatial clustering algorithm | Based on co-activity thresholds along dendritic segments |

## 14. References and Context

| Detail | Value |
|---|---|
| Total references cited | 63 |
| Key prior finding | Synaptic inputs organized similarly in vivo under light anesthesia and in slice cultures |
| Key prior mechanism | Push-pull mechanism between mature BDNF and proBDNF regulates transmission frequency |
| Developmental context | Second postnatal week is the peak period for synapse addition in mouse visual cortex |
| Eye opening | P14 in mouse; all recordings conducted P8-P13 (before visual experience) |

