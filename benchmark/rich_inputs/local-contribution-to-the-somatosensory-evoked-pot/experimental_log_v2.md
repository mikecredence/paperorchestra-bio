# Experimental Log: Local Contribution to Somatosensory Evoked Potentials in Rat Thalamus

## 1. Animals and Surgical Preparation

| Parameter | Detail |
|---|---|
| Species / strain | Wistar rats, adult males |
| Number of animals | 11 |
| Weight range | 350-560 g |
| Anesthesia | Urethane, 1.5 mg/kg i.p. (+ 10% top-ups as needed) |
| Local anesthetic (ears) | Emla 2.5% cream (AstraZeneca) |
| Local anesthetic (scalp) | Lidocaine hydrochloride 1% (Polfa Warszawa) |
| Stereotaxic apparatus | Narishige |
| Body temperature | 37-38 C (thermostatic blanket) |
| Physiological monitoring | MouseOx (heart rate, breath rate, O2 saturation) |
| Fluid support | s.c. injections of 0.9% NaCl and/or 5% glucose |
| Ethical approval | EU Directives 86/609/EEC and 2010/63/EU; 1st Warsaw Local Ethics Committee |
| Perfusion fixative | 10% formalin in PBS |
| Histological sections | 50 um coronal, freezing microtome |
| Staining methods | Cytochrome oxidase and Nissl bodies |

## 2. Recording Probe Configurations

| Setup | Probe Type | Channels | Placement (Cortex) | Placement (Thalamus) | Animals |
|---|---|---|---|---|---|
| 1 | Neuropixels 1.0 | 384 | Continuous track cortex-to-thalamus | Same probe | Subset of 11 |
| 2 | NeuroNexus 8x8 multi-shank | 64 per probe (x2) | Barrel cortex (tilted ~30 deg) | VPM/PoM (vertical) | Subset of 11 |
| 3 | NeuroNexus 32-channel linear | 32 per probe (x2) | Barrel cortex (tilted ~30 deg) | VPM/PoM (vertical) | Subset of 11 |

| Stereotaxic Coordinates | Cortex (Barrel Field) | Thalamus |
|---|---|---|
| AP range | 1.5-3.0 mm posterior to bregma | Not specified (vertical insertion) |
| ML range | 5.0-6.2 mm right of bregma | Standard VPM/PoM coordinates |
| Probe angle | ~30 deg from vertical (perpendicular to cortical surface) | Vertical |
| Reference electrode | Ag/AgCl under neck skin | Same |

## 3. Stimulation Parameters

| Parameter | Value |
|---|---|
| Stimulator type | Piezoelectric |
| Whisker group | Large vibrissae from left mystacial pad |
| Attachment point | ~10-15 mm from snout |
| Deflection amplitude | 0.1 mm horizontal (rostro-caudal axis) |
| Pulse duration | 1 or 2 ms |
| Pulse voltage | 20 V (square wave) |
| Number of stimuli | 100 per session |
| Inter-stimulus interval | 3-5 s (pseudorandom) |
| Control software | Spike2 sequencer (Cambridge Electronic Design) |

## 4. Temporal Profile of Evoked Responses

| Event | Latency Post-Stimulus | Structure | Signal Characteristic |
|---|---|---|---|
| Earliest thalamic response | ~3 ms | VPM/PoM thalamus | Single/multi-unit activity |
| Thalamic negative EP peak | ~8-12 ms | VPM/PoM thalamus | Small-amplitude negative wave |
| Cortical response onset | ~5 ms | Barrel cortex | Initial activation |
| Cortical negative EP peak | ~10 ms | Barrel cortex (layer 4/5) | Large-amplitude negative wave |
| Thalamic-cortical EP correlation > 0.5 | 10-12 ms | Both structures | Rolling 3 ms window correlation |

Fig 1B: Neuropixels recording showing simultaneous thalamic and cortical EPs. A negative deflection in the thalamic recording coincides with the strongest cortical negative wave around 10 ms.

Fig 1C: EP waveforms at selected thalamic and cortical sites; the "oo" mark indicates the time of strongest cortical negative wave where thalamic contamination is most evident.

Fig 1D: Rolling correlation (3 ms window) between thalamic and cortical EPs across 11 rats. Correlation exceeds 0.5 around 10-12 ms post-stimulus, indicating substantial shared signal component.

## 5. Volume Conduction Analysis

### 5.1 Cortical Source Contribution to Thalamic Field

| Observation | Detail |
|---|---|
| Cortical EP at layer 4/5 (10 ms) | Large negative deflection |
| Cortical EP at bottom of cortex (10 ms) | Clear positive polarity |
| Thalamic EP polarity (10 ms) | Negative (consistent with mid-cortical, not deep-cortical signal) |
| Estimated cortical field spread | Strong negative stripe from cortex through entire subcortical space |

Fig 2A: Spatiotemporal EP profile from Neuropixels probe shown as 3D color map, spanning cortex through thalamus.

Fig 2B: CSD profile estimated from the same data shows current sinks and sources in both cortical and thalamic regions.

Fig 2C: Spatiotemporal EP profile reconstructed from cortical recordings only. The purple (negative) stripe around 10 ms extends from cortical sources deep into the subcortical space, demonstrating the strength and range of passive spread (volume conduction). The polarity is only transiently reversed at the bottom of cortex before continuing as negative into the thalamic territory.

## 6. kCSD Source Decomposition Analysis

### 6.1 Analytical Configurations

| Configuration | Recordings Used | Source Space | Purpose |
|---|---|---|---|
| A (Fig 5A) | Thalamus + cortex | Thalamus only | Estimate thalamic CSD with cortical context |
| B (Fig 5B) | Thalamus only | Thalamus only | Test if cortical recordings are needed |
| C (Fig 5C) | Thalamus + cortex | Full cortico-thalamic block | Full source reconstruction |

### 6.2 Source Separation Results (Fig 3)

| Panel | Source Subset | Reconstruction Target | Finding |
|---|---|---|---|
| Fig 3 A1-A3 | All sources (full CSD) | Cortical + thalamic channels | Full reconstruction reference |
| Fig 3 B1-B3 | Cortical sources only | Cortical + thalamic channels | Cortical field dominates thalamic recording at 10 ms |
| Fig 3 C1-C3 | Thalamic sources only | Cortical + thalamic channels | Local thalamic contribution is smaller, different waveform |

Fig 3: Measured EPs overlaid with computed contributions from cortical and thalamic source subsets (example from 8x8 NeuroNexus probes). Cortical sources produce substantial field at thalamic recording sites. Thalamic sources produce local contribution with different temporal profile.

## 7. Quantitative Comparison of Measured vs. Reconstructed Thalamic EPs

### 7.1 Waveform Comparison at 10 ms

| Signal | Polarity at 10 ms | Amplitude (relative) |
|---|---|---|
| Measured thalamic EP | Negative (more negative) | Larger |
| Reconstructed EP from local thalamic sources | Less negative / different | Smaller |
| Difference | Attributable to cortical volume conduction | Significant |

Fig 4A: Overlay of measured and reconstructed potentials from central cortical and thalamic sites. Solid lines = measured potentials, dashed lines = reconstructed from local sources. Cortical channel shows close match; thalamic channel shows measured potential is more negative than locally reconstructed potential.

### 7.2 Statistical Test at 10 ms Post-Stimulus

| Test | Comparison | Result | p-value |
|---|---|---|---|
| Permutation paired-test | Measured thalamic EP vs. reconstructed local thalamic EP at 10 ms | Reconstructed values significantly less negative | p < 0.05 |

Fig 4B: Scatter plot of potential values at 10 ms in recorded thalamic EPs vs. their reconstructions from local sources. Reconstructed data points are systematically less negative than measured data points, confirming cortical contamination.

## 8. Concurrent Cortical Recording Necessity Test

### 8.1 Configuration Comparison (Fig 5)

| Configuration | CSD Estimation Quality | Key Finding |
|---|---|---|
| A: Thal+Ctx recordings, thal sources only | Good | Reference configuration |
| B: Thal recordings only, thal sources only | Good (similar to A) | Cortical recordings NOT essential |
| C: Thal+Ctx recordings, full source space | Good | Full model confirms findings |

Fig 5: Three analytical configurations compared. The critical result is that configuration B (thalamic recordings only, thalamic source space only) yields CSD profiles very similar to configuration A (which includes cortical recordings), demonstrating that concurrent cortical recordings are not necessary for reliable thalamic CSD estimation.

## 9. Probe Technology Generalization

| Probe System | Channel Count | Coverage | kCSD Result Consistency |
|---|---|---|---|
| Neuropixels 1.0 | 384 | Continuous cortex-to-thalamus | Consistent |
| NeuroNexus 8x8 multi-shank | 2 x 64 | Separate cortical and thalamic arrays | Consistent |
| NeuroNexus 32-channel linear | 2 x 32 | Separate cortical and thalamic probes | Consistent |

Results were replicated across all three recording setups, confirming generalizability of the approach.

## 10. Thalamic Nuclei Details

| Nucleus | Abbreviation | Whisker-Responsive Region | Role |
|---|---|---|---|
| Ventral Posteromedial | VPM | Upper-lateral sector | Primary thalamic relay for whisker input |
| Posterior medial | PoM | Upper-lateral sector | Higher-order thalamic nucleus for whisker processing |

Histological verification confirmed electrode placement in the representation of large mystacial vibrissae located in dorsolateral VPM.

## 11. CSD Method Details

| Parameter | Detail |
|---|---|
| CSD method | Kernel CSD (kCSD) |
| Input | Averaged evoked potential profiles (100 stimulus repetitions) |
| Basis functions | Model-based kernel approach |
| Source space | Configurable (thalamus only, cortex only, or full block) |
| Output | Current source density estimate at each spatial point |
| Advantage over traditional CSD | Works with arbitrary electrode geometries, handles missing data, model-based approach |

## 12. Histological Verification

| Step | Method |
|---|---|
| Electrode track visualization | Photographs of coronal sections |
| Atlas overlay | Brain atlas planes using GIMP v2.10 and Inkscape v1.0.1 |
| Staining | Cytochrome oxidase (barrel field visualization) and Nissl bodies |
| Verification targets | Barrel cortex electrode placement, VPM/PoM thalamic electrode placement |
| Supplementary data | Histological examples provided in Suppl. Fig 2 |

## 13. Signal Properties

| Property | Cortical EP | Thalamic EP |
|---|---|---|
| Amplitude (10 ms peak) | Large (layer 4/5 negative wave) | Small (negative deflection) |
| Polarity at bottom of cortex (10 ms) | Positive | N/A |
| Spatial extent of field | Extends through entire subcortical space | Local (after CSD correction) |
| Correlation with counterpart (10-12 ms) | > 0.5 (rolling 3 ms window, n=11 rats) | > 0.5 |
| Earliest evoked activity | ~5 ms | ~3 ms |

## 14. Implications for LFP Interpretation

| Issue | Recommendation |
|---|---|
| Thalamic LFP contains cortical contamination | Apply CSD analysis before interpreting thalamic signals |
| Volume conduction from barrel cortex | Can affect subcortical recordings including olfactory bulb (per prior literature) |
| Hippocampal oscillations | May also spread widely; similar CSD approach recommended |
| Human intracranial recordings | Same volume conduction concerns apply |
| Experimental design | Concurrent cortical recording is helpful but not required for thalamic CSD |

## 15. Software and Analysis Tools

| Software | Version | Purpose |
|---|---|---|
| Spike2 | N/A | Stimulation control |
| GIMP | 2.10 | Histological overlay |
| Inkscape | 1.0.1 | Histological overlay |
| kCSD toolbox | N/A | Kernel current source density estimation |

## 16. Key Quantitative Findings Summary

| Finding | Quantitative Detail |
|---|---|
| Rolling EP correlation (thal-ctx) | > 0.5 at 10-12 ms post-stimulus (group of 11 rats) |
| Reconstructed thalamic EP vs. measured | Significantly less negative at 10 ms (permutation test p < 0.05) |
| Earliest thalamic response | ~3 ms (confirmed local origin, preceding cortical contamination window) |
| Cortical response onset | ~5 ms post-stimulus |
| Number of stimulus repetitions | 100 per session |
| Whisker deflection | 0.1 mm, 1-2 ms duration |
| Probe channels (Neuropixels) | 384 |
