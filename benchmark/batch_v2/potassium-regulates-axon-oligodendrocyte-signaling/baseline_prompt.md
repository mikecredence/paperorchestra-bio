Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Nature Neuroscience

## Idea Summary

# Idea Summary

## Working title
Potassium Regulates Axon-Oligodendrocyte Signaling and Metabolic Coupling in White Matter

## Core question
How do oligodendrocytes detect axonal spiking activity and regulate metabolic coupling with myelinated axons, and what role does the inwardly rectifying potassium channel Kir4.1 play in this process?

## Motivation / gap
- Oligodendrocytes provide metabolic support to axons via lactate/pyruvate through monocarboxylate transporters, but the signaling mechanisms governing this support are poorly understood
- How OLs detect axonal activity and rapidly adjust metabolic coupling is largely unknown
- GLUT1 surface expression in OLs responds to glutamatergic signaling, but whether potassium-based signaling plays a role in metabolic regulation has not been tested
- Kir4.1 channels in OLs are known for K+ clearance, but their role in regulating axonal energy metabolism has not been explored
- Axonal pathology in aging and neurodegeneration may result from homeostatic dysfunction in the axon-OL unit, yet the molecular mechanisms are poorly characterized

## Core contribution (bullet form)
- Demonstrated that high-frequency axonal firing (10, 25, 50 Hz) triggers a biphasic Ca2+ response in mature OL somas, with larger responses at higher frequencies (p < 0.0001 for 5 vs 30 mM K+)
- Showed that stimulus-evoked Ca2+ surges in OLs depend on barium-sensitive Kir channels and extracellular Ca2+ influx, with reverse-mode NCX contributing to the response
- Generated OL-specific Kir4.1 knockout mice (Kir4.1 cKO) and demonstrated they develop axonal pathology around 7-8 months of age
- Found reduced GLUT1 and MCT1 expression in myelin from 2-3 month old Kir4.1 cKO mice before onset of axonopathy, via TMT-labeled LC-MS/MS proteomics
- Detected lower resting lactate levels and reduced activity-induced lactate surges in optic nerve axons of young Kir4.1 cKO mice using the Laconic FRET sensor
- Revealed for the first time that OLs regulate axonal glucose metabolism: glucose uptake and consumption rates were reduced in Kir4.1 cKO axons (glucose consumption rate 2.7 +/- 0.6%/min in ctrl vs 0.1 +/- 0.2%/min in cKO, p = 0.0002)

## Method in brief
The study uses an ex vivo optic nerve preparation that combines electrophysiology (compound action potential recordings) with two-photon imaging of genetically encoded sensors. PLP-CreERT;RCL-GCaMP6s mice enable Ca2+ imaging specifically in mature OLs. Optic nerves are stimulated at various frequencies (0.4 Hz baseline; 10, 25, 50 Hz trains for 30 s) while simultaneously recording CAPs and OL Ca2+ dynamics. Pharmacological tools include TTX (sodium channel blocker), barium (Kir channel blocker), NBQX (AMPA/kainate antagonist), PPADS (P2 receptor antagonist), KB-R7943 (NCX inhibitor), and removal of extracellular Ca2+.

OL-specific Kir4.1 knockout mice (Kir4.1fl/fl;MOGiCre) are used for loss-of-function studies. Myelin proteomics is performed using TMT-labeled LC-MS/MS on optic nerves from 2.5-month-old mice. Axonal metabolite dynamics are measured using AAV-delivered FRET sensors: ATeam1.03 for ATP, Laconic for lactate, and FLIIP for glucose, expressed in optic nerve axons via intravitreal AAV injection. Metabolite responses are assessed under glucose deprivation, mitochondrial inhibition (NaN3), exogenous lactate application, and high-frequency stimulation protocols.

## Target venue
Nature Neuroscience


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the K+/oligodendrocyte metabolic coupling study.

---

## Mouse Lines and Genetic Tools

| Tool | Purpose | Details |
|------|---------|---------|
| PLP-CreERT;RCL-GCaMP6s | OL-specific Ca2+ imaging | Tamoxifen at 6-8 weeks; experiments 4-12 weeks post-injection |
| Kir4.1fl/fl;MOGiCre (cKO) | OL-specific Kir4.1 knockout | Compared to Kir4.1fl/fl littermate controls |
| AAV-ATeam1.03 | Axonal ATP FRET sensor | Intravitreal delivery to optic nerve axons |
| AAV-Laconic | Axonal lactate FRET sensor | Intravitreal delivery to optic nerve axons |
| AAV-FLIIP | Axonal glucose FRET sensor | Intravitreal delivery to optic nerve axons |
| RCL-GCaMP6s + AAV-Cre | Axonal Ca2+ imaging | Intravitreal AAV-Cre in reporter mice |

---

## Experiment 1: Frequency-Dependent Ca2+ Responses in OLs

Optic nerves stimulated for 30 s at different frequencies. Ca2+ responses measured as area under the curve (AUC) during stimulation.

| Stimulation Frequency | OL Ca2+ Response (AUC) | CAP Amplitude Change | n (cells/nerves) |
|----------------------|----------------------|---------------------|-----------------|
| 10 Hz | Moderate increase | Moderate decrease | 108 cells / 8 nerves |
| 25 Hz | Larger increase | Larger decrease | 108 cells / 8 nerves |
| 50 Hz | Largest increase | Largest decrease | 108 cells / 8 nerves |

Fig. 1e: The Ca2+ response was biphasic -- initial rise during stimulation followed by a transient undershoot after stimulation. Higher frequencies produced proportionally larger responses.

Fig. 1d: CAP peak 2 amplitude decreased during high-frequency stimulation, consistent with prior findings.

---

## Experiment 2: TTX and Ca2+ Removal Controls

| Condition | Effect on OL Ca2+ Response | Interpretation |
|-----------|---------------------------|----------------|
| TTX (1 uM) | Abrogated stimulus-induced Ca2+ surge | Action potentials required |
| 0 mM extracellular Ca2+ | Strongly diminished response | Ca2+ influx mechanism |

Fig. 1f: TTX completely blocked the OL Ca2+ response to 50 Hz stimulation.
Fig. 1g: Removal of extracellular Ca2+ strongly diminished the elicited response.

---

## Experiment 3: K+-Evoked Ca2+ Responses in OLs

Bath application of elevated [K+] for 30 s to mimic activity-dependent K+ elevations.

| K+ Elevation (delta mM) | Ca2+ Amplitude | Statistical Comparison | p-value |
|--------------------------|---------------|----------------------|---------|
| 5 mM | Small response | 5 vs 10 mM | 0.0048 |
| 10 mM | Moderate response | 5 vs 30 mM | < 0.0001 |
| 30 mM | Large response | 10 vs 30 mM | < 0.0001 |

n = 35-57 cells, N = 4-5 optic nerves; one-way ANOVA with Tukey's multiple comparisons test.

Fig. 2a: Ca2+ levels in OLs increased in a dose-dependent manner with extracellular K+ elevation.

---

## Experiment 4: Pharmacological Dissection of OL Ca2+ Response

| Pharmacological Agent | Target | Effect on OL Ca2+ | Effect on Axonal Ca2+ |
|----------------------|--------|-------------------|----------------------|
| Barium (Ba2+) | Kir channels (esp. Kir4.1) | Diminished stimulus-evoked and K+-evoked Ca2+ | No effect |
| NBQX (50 uM) | AMPA/kainate receptors | No significant effect (p = 0.7277) | Not tested |
| PPADS (100 uM) | P2 purinergic receptors | No significant effect | Not tested |
| KB-R7943 | Reverse-mode NCX | Reduced Ca2+ response partially | Not tested |
| Ba2+ alone (no stimulation) | Kir channels | No change in basal Ca2+ | N/A |

Extended Data Fig. 1a-b: NBQX had no effect on stimulus-evoked Ca2+ increase (n = 45 cells, N = 3 nerves, paired t-test).
Extended Data Fig. 1c-d: PPADS similarly did not significantly alter the OL Ca2+ response.
Extended Data Fig. 2: Stimulus-evoked axonal Ca2+ surges were not sensitive to barium, confirming OL-specificity.

---

## Experiment 5: Kir4.1 cKO -- CAP Recovery and K+ Clearance

| Measure | ctrl (Kir4.1fl/fl) | cKO (Kir4.1fl/fl;MOGiCre) | p-value |
|---------|--------------------|-----------------------------|---------|
| CAP peak latencies (peak 1) | Normal | No difference | 0.7637 |
| CAP peak latencies (peak 2) | Normal | No difference | 0.9958 |
| CAP peak latencies (peak 3) | Normal | No difference | 0.9265 |
| CAP amplitude recovery after stimulation | Normal recovery | Delayed recovery | Significant |

One-way ANOVA with Holm-Sidak's multiple comparisons test for latencies.

Fig. 3b: Average CAP responses of optic nerves from ctrl (n = 8) and cKO (n = 9).
Fig. 3c: No genotype differences in baseline CAP peak latencies.
Fig. 3d: CAP recovery kinetics after high-frequency stimulation impaired in cKO, equivalent to Ba2+ effects.

---

## Experiment 6: Axonal Pathology in Aged Kir4.1 cKO Mice

| Timepoint | Observation |
|-----------|-------------|
| 2-3 months | No overt axonal damage; reduced GLUT1/MCT1 in myelin |
| 7-8 months | Axonal pathology manifest |

---

## Experiment 7: Myelin Proteomics (TMT-labeled LC-MS/MS)

Optic nerves dissected from 2.5-month-old cKO (n = 4) and ctrl (n = 4) mice.

| Protein | Direction in cKO | Significance | Category |
|---------|-----------------|-------------|----------|
| GLUT1 (Slc2a1) | Downregulated | Significant | Glucose transporter |
| MCT1 (Slc16a1) | Downregulated | Significant | Monocarboxylate transporter |
| Various myelin proteins | Mixed changes | See heatmap | Structural/metabolic |

Fig. 4a: Experimental scheme for TMT-labeled LC-MS/MS.
Fig. 4b: Heatmap of relative protein changes ranked by log2 fold change between cKO and ctrl.

---

## Experiment 8: Axonal ATP Dynamics (ATeam1.03 FRET Sensor)

| Condition | ctrl Response | cKO Response | Difference |
|-----------|--------------|-------------|------------|
| 10 mM glucose baseline | Normal FRET ratio | Slightly altered | Minor |
| Glucose deprivation (GD) | ATP drop | ATP drop | Slight difference |
| GD + mitochondrial inhibition (NaN3) | Maximal ATP depletion | Maximal ATP depletion | Similar endpoint |

Fig. 5a: Color-coded ratio images from ctrl and cKO nerves during glucose and GD+MI conditions.
Fig. 5: ATP dynamics were slightly altered in young Kir4.1 cKO mice, but the differences were modest compared to lactate and glucose measures.

---

## Experiment 9: Axonal Lactate Dynamics (Laconic FRET Sensor)

| Measure | ctrl | cKO | p-value |
|---------|------|-----|---------|
| Resting lactate level (in 10 mM glucose) | Higher baseline ratio | Lower baseline ratio | Significant |
| Response to 20 mM exogenous lactate | Normal increase | Reduced increase | Significant |
| Activity-induced lactate surge (50 Hz) | Present | Reduced | Significant |
| Lactate removal (0 glucose, 0 lactate) | Normal decrease | Decreased from lower baseline | Consistent |

Fig. 6a: Representative color-coded ratio images showing lactate levels under various conditions.
Fig. 6b: Quantification of Laconic ratios across conditions for ctrl and cKO.

---

## Experiment 10: Axonal Glucose Dynamics (FLIIP FRET Sensor)

| Measure | ctrl | cKO | p-value |
|---------|------|-----|---------|
| Resting glucose level (10 mM glucose) | Normal | Reduced | Significant |
| Glucose deprivation response | Normal drop | Attenuated drop | Significant |
| Glucose uptake rate | Normal | Reduced | Significant |

Fig. 7a: Color-coded ratio images from ctrl (top) and cKO (bottom) in glucose and glucose-free conditions.
Fig. 7b: Time course of axonal glucose levels; 3-month-old cKO and ctrl mice.

---

## Experiment 11: Activity-Induced Glucose Consumption

| Measure | ctrl (n = 11) | cKO (n = 16) | p-value |
|---------|--------------|-------------|---------|
| Glucose consumption rate during 50 Hz stimulation | 2.7 +/- 0.6 %/min | 0.1 +/- 0.2 %/min | 0.0002 |
| Post-stimulation glucose rebound | Above initial baseline | Above initial baseline | Both genotypes |
| Steady-state glucose after recovery | Similar | Similar | Not significant |

Unpaired t-test for consumption rate comparison.

Fig. 8a-c: Time course of 50 Hz stimulation-evoked axonal glucose dynamics.
Fig. 8b: During stimulation, glucose levels decreased in ctrl but remained stable in cKO.
Fig. 8c: After stimulation, glucose levels increased above initial baseline values in both genotypes.

---

## Key Pharmacological Parameters

| Agent | Concentration | Target |
|-------|--------------|--------|
| TTX | 1 uM | Voltage-gated Na+ channels |
| Barium chloride | Varies | Kir channels (esp. Kir4.1) |
| NBQX | 50 uM | AMPA/kainate receptors |
| PPADS | 100 uM | P2 purinergic receptors |
| KB-R7943 | Not specified | Reverse-mode NCX |
| Sodium azide (NaN3) | 5 mM | Mitochondrial complex IV |

---

## Statistical Tests Used

| Test | Context | Key Results |
|------|---------|-------------|
| One-way ANOVA + Tukey's | K+ dose-response Ca2+ | 5 vs 10 mM: p=0.0048; 5 vs 30 mM: p<0.0001 |
| Paired t-test | NBQX effect on Ca2+ | p = 0.7277 (no effect) |
| One-way ANOVA + Holm-Sidak | CAP peak latencies (ctrl vs cKO) | p = 0.76, 0.99, 0.93 for peaks 1-3 |
| Unpaired t-test | Glucose consumption rate | p = 0.0002 |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | High-frequency axonal firing drives biphasic Ca2+ response in OLs; frequency-dependent amplitude |
| Fig. 2 | K+ elevations mimic stimulus-evoked Ca2+ response; barium blocks both stimulus and K+ effects on OLs selectively |
| Fig. 3 | Kir4.1 cKO nerves show delayed CAP recovery; OL-specific Kir4.1 is critical for K+ clearance |
| Fig. 4 | GLUT1 and MCT1 reduced in myelin of young cKO mice before axonopathy onset |
| Fig. 5 | Modest alterations in axonal ATP dynamics in young cKO |
| Fig. 6 | Lower resting lactate and reduced activity-induced lactate surges in cKO axons |
| Fig. 7 | Reduced axonal glucose uptake and resting glucose in cKO |
| Fig. 8 | Activity-induced glucose consumption rate drastically reduced in cKO axons |

---

## Proposed Working Model (Fig. 8h)

K+ released during axonal spiking activates Kir4.1 channels on OLs, causing membrane depolarization and Ca2+ influx (partly via reverse-mode NCX). This Ca2+ signal adjusts OL metabolic support: GLUT1 and MCT1 expression, lactate supply, and glucose regulation are all modulated through this pathway. Loss of Kir4.1 disrupts this signaling, leading to early metabolic deficits and eventual axonal degeneration.

---

## Antibodies Used (Table 1)

| Antibody | Application | Purpose |
|----------|------------|---------|
| CC1 | IHC | Mature OL marker |
| alpha-GFP | IHC | GCaMP6s detection |
| Various (see Table 1) | IHC / IB | Multiple targets for validation |

---

## Reference Count
117 references cited.

