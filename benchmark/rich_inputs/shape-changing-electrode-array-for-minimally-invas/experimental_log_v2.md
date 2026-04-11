# Experimental Log

> Pre-writing data tables and observations for the shape-changing electrode array study.

---

## SCEA Design Specifications

| Parameter | Value |
|-----------|-------|
| Substrate material | Parylene-C |
| Substrate thickness | 4 um |
| Insulation layers | SU8 |
| Conductive layer | CNT/Au (web-like SWCNT by CVD) |
| Active site size | 100 x 100 um2 |
| Compressed strip width | 3 mm |
| Deployed array size (rat) | 20 mm x 15 mm |
| Channel count (rat) | 64 |
| Channel count (canine) | 256 |
| Canine array size | 20 mm x 10 mm |
| Shape actuator | Nitinol (NiTi shape-memory alloy) |
| Actuator transition temperature | 37 degrees C (body temperature) |
| Bonding adhesive | Polyethylene oxide (PEO), water-soluble |

---

## Experiment 1: Impedance Characterization

| Measurement | Before Shape Transform | After Shape Transform |
|-------------|----------------------|---------------------|
| Mean impedance at 1 kHz | ~50 kOhm | ~50 kOhm (stable) |
| Channel-to-channel variation | Low (see impedance map) | Low |
| Functional channels | 64/64 | 64/64 |

Fig. 1g: In vitro impedance map of 64-channel SCEA before and after one compression/expansion cycle.
Fig. 1h: Box plots showing impedance distribution stability.

---

## Experiment 2: MRI Studies on Rats

### Structural MRI (T2-weighted)

| Timepoint | Brain Structure Change | Notes |
|-----------|----------------------|-------|
| 1 week | No change | SCEA position visible |
| 2 weeks | No change | Stable |
| 3 weeks | No change | Stable |
| 4 weeks | No change | Stable |
| 8 weeks | No change | Stable |

### DCE-MRI (BBB Assessment)

| Timepoint | Cortical BBB Breach | Meningeal Enhancement |
|-----------|--------------------|--------------------|
| 1 week | No obvious breach | Segments of convexity enhancement present |
| 2 weeks | No obvious breach | Diminishing |
| 4 weeks | No obvious breach | Completely resolved |
| 8 weeks | No obvious breach | Absent |

| Control Comparison | Meningeal Enhancement |
|-------------------|---------------------|
| SCEA via minimally invasive surgery | Present at 1 week, resolved by 4 weeks |
| Same electrode via craniotomy (no shape transform) | Similar enhancement level |

Fig. 2a: Schematic of MRI measurement plan.
Fig. 2b: T2-weighted images across timepoints showing no structural changes.
Fig. 2c: DCE-MRI images and quantification of cortical signal enhancement.

---

## Experiment 3: Immunohistochemistry (IHC) in Rats

| Marker | Target | 1 Week | 4 Weeks | 8 Weeks | Contralateral Control |
|--------|--------|--------|---------|---------|---------------------|
| GFAP | Astrocyte reactivity | Mild increase | Minimal | Baseline-like | Baseline |
| Iba1 | Microglial activation | Mild increase | Minimal | Baseline-like | Baseline |
| NeuN | Neuronal density | No change | No change | No change | Reference |

Cortex divided into L1, upper layers (UL), and lower layers (LL) for quantification.

Fig. 3a: IHC assessment schematic with ROI definitions.
Fig. 3b: Example immunofluorescence images under SCEA vs contralateral control.

---

## Experiment 4: Rat Seizure Recording (4-AP Model)

| Parameter | Value |
|-----------|-------|
| Seizure induction | Topical 4-AP through cranial hole |
| Recording type | Epidural micro-ECoG |
| Bandwidth captured | 0.5-500 Hz |
| Seizure types observed | Short electrographic seizures |
| Spatial resolution | Individual channels (64) |

| Signal Feature | Observed? | Frequency Range |
|---------------|-----------|----------------|
| Low-frequency oscillations | Yes | 0.5-50 Hz |
| Ripples | Yes | 80-250 Hz |
| Fast ripples | Yes | 250-500 Hz |
| Spatiotemporal propagation | Yes | Mapped across array |

Fig. 4a: Illustration of SCEA recording setup in rat.
Fig. 4b: Micro-ECoG signal and spectrogram from channel #17 during seizure.

---

## Experiment 5: Canine Subdural Implantation

| Parameter | Value |
|-----------|-------|
| Animal model | Beagle dog |
| Implantation type | Subdural through dura slit |
| Array | 256-channel, 20 mm x 10 mm |
| Recording condition | Emergence from anesthesia |
| Dura slit size | Small (marked by white dotted line) |

| Observation | Details |
|-------------|---------|
| Deployment | Successful transformation from strip to sheet subdurally |
| Vascular integrity | No vessel disruption during deployment |
| Conformal contact | Array conformed to brain surface curvature |
| Signal quality | High-quality ECoG recorded |

Fig. 5a: Schematic of minimally invasive subdural implantation.
Fig. 5b: Optical images before and after actuator withdrawal.

---

## Experiment 6: Canine Brain State Mapping

| Brain State | Cortical Activity Pattern | Spatial Organization |
|-------------|--------------------------|---------------------|
| Deep anesthesia | Suppressed, burst-suppression | Globally synchronized |
| Light anesthesia | Increasing activity | Regional differences emerging |
| Emergence | Active cortical patterns | Spatiotemporally organized |

Fig. 5: High-quality recordings capturing emergence-period dynamics with full spatial coverage.

---

## Experiment 7: Post-Operative SCEA Localization

| Method | Application | Tool |
|--------|------------|------|
| T1-weighted MRI | Ni-SCEA localization | Standard MRI |
| 3D reconstruction | Brain + SCEA visualization | MIPAV software |
| Serial sectioning | Channel position mapping | MRI image analysis |

Fig. 6a-d: MRI-based localization workflow for 256-channel Ni-SCEA in beagle brain.

---

## Comparison with Existing Brain Mapping Techniques

| Technique | Spatial Resolution | Temporal Resolution | Bandwidth | Invasiveness |
|-----------|-------------------|--------------------|-----------|----|
| Scalp EEG | cm | ms | 0.5-50 Hz (routine) | Non-invasive |
| MEG | mm | ms | Up to 250 Hz (specialized) | Non-invasive |
| fMRI | mm | s | Hemodynamic (indirect) | Non-invasive |
| fNIR | mm-cm | s | Hemodynamic (indirect) | Non-invasive |
| Standard ECoG | um-mm | ms | Up to 500 Hz | Highly invasive (craniotomy) |
| SCEA (this work) | um-mm | ms | Up to 500 Hz | Minimally invasive |

---

## Material Properties

| Component | Property | Value |
|-----------|----------|-------|
| CNT film | Conductivity under strain | Maintained after large deformation |
| Gold layer | Conductivity under strain | Fails (nm-thick, cracks) |
| CNT/Au hybrid | Combined function | CNT preserves conductivity; Au for initial performance |
| Nitinol | Phase transition | Martensite (low T) to austenite (body T) |
| PEO adhesive | Dissolution | Water-soluble; dissolves after deployment |
| Parylene-C | Flexibility | Highly flexible at 4 um thickness |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | SCEA design, fabrication, compression/deployment, impedance stability |
| Fig. 2 | MRI: no structural brain changes; meningeal enhancement resolves by 4 weeks |
| Fig. 3 | IHC: minimal inflammatory response, comparable to standard epidural implant |
| Fig. 4 | Rat seizure recording with high-bandwidth micro-ECoG through SCEA |
| Fig. 5 | Canine subdural implantation and emergence-period recording |
| Fig. 6 | MRI-based post-operative SCEA localization |

---

## Reference Count
43 references cited.
