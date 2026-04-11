# Experimental Log

> Pre-writing data tables and observations for the antipsychotic drug / cortical layer study.

---

## Mouse Lines and Sample Sizes

| Genotype | Target Cell Type | n (mice) |
|----------|-----------------|----------|
| C57BL/6 + AAV-PHP.eB | Brain-wide | 6 |
| Emx1-Cre | Cortical excitatory | 4 |
| Cux2-CreERT2 | L2/3 and L4 excitatory | 4 |
| Scnn1a-Cre | L4 excitatory subset | 7 |
| Tlx3-Cre x Ai148 | L5 IT neurons | 25 |
| Ntsr1-Cre | L6 excitatory subset | 3 |
| PV-Cre | PV interneurons | 2 |
| VIP-Cre | VIP interneurons | 6 |
| SST-Cre | SST interneurons | 5 |

---

## Experiment 1: Closed vs Open Loop Locomotion Onsets by Cell Type

| Neuron Type | Layer | Closed vs Open Loop Distinction |
|-------------|-------|-------------------------------|
| Cux2 | L2/3-L4 | Weak |
| Scnn1a | L4 | Weak |
| Tlx3 | L5 IT | Strongest distinction |
| Ntsr1 | L6 | Similar level to Tlx3 |
| PV | Mixed | Moderate |
| VIP | Mixed | Moderate |
| SST | Mixed | Moderate |

Fig. 1: Activation patterns in deep cortical layers distinguished closed and open loop locomotion onsets more strongly than superficial layers.

---

## Experiment 2: Visuomotor Prediction Error Responses

| Stimulus | Brain-wide V1 Response | Tlx3 V1 Response |
|----------|----------------------|-------------------|
| Mismatch (negative PE) | Activation originating in V1 | Strong activation; propagation to V2am |
| Drifting grating | Activation | Net suppression (population average) |

Fig. 3A: Average mismatch and grating responses in brain-wide imaging (230 mismatch onsets, 86 grating onsets in example mouse).
Fig. 3B: Region-specific traces for 6 cortical areas.

---

## Experiment 3: Clozapine Effects on Inter-Regional Correlations

| Cell Type | n (mice) | Pre-Drug Correlations | Post-Clozapine | Effect Magnitude |
|-----------|---------|----------------------|----------------|-----------------|
| Brain-wide (C57BL/6) | 4 | Standard matrix | Reduced | Moderate |
| Tlx3 (L5 IT) | 5 | Standard matrix | Strongly reduced | Dramatic |
| Cux2 (L2/3-L4) | 4 | Standard | Minimal change | Weak |
| Scnn1a (L4) | 7 | Standard | Minimal change | Weak |

Fig. 5A-D: Correlation matrices before and after clozapine for brain-wide and L5 IT.

---

## Experiment 4: Drug Comparison -- Distance-Dependent Correlations

| Drug | Class | L5 IT Decorrelation | Mechanism |
|------|-------|--------------------|----|
| Clozapine | Atypical antipsychotic | Strong reduction | Multi-receptor |
| Aripiprazole | Atypical antipsychotic | Strong reduction (similar) | D2 partial agonist |
| Haloperidol | Typical antipsychotic | Strong reduction (similar) | D2 antagonist |
| Amphetamine | Psychostimulant | No significant decorrelation | DA/NE release |

Fig. 6: Distance-dependent density maps of correlations for clozapine in brain-wide and Tlx3 mice.
Fig. 7: Aripiprazole and haloperidol mimic clozapine decorrelation; amphetamine does not.

---

## Experiment 5: Antipsychotic Effects on Prediction Errors

| Measure | Pre-Drug (V1 Tlx3) | Post-Antipsychotic |
|---------|--------------------|--------------------|
| Mismatch response | Standard amplitude | Reduced |
| Mismatch propagation V1 to V2am | Present | Impaired |
| Grating response | Suppression | Less affected |

Fig. 8: Antipsychotic treatment preferentially reduced negative prediction error responses and propagation.

---

## Hemodynamic Control Experiments

| Preparation | Hemodynamic Artifact Magnitude | Used For |
|-------------|-------------------------------|----------|
| Crystal skull | Small | Main experiments |
| Clear skull | Larger | Comparison only |
| eGFP (no GCaMP) | Hemodynamic only | Reference calibration |
| 405 nm isosbestic | Attempted correction | Incomplete correction |

Fig. S1A-B: Crystal skull vs clear skull hemodynamic artifacts.

---

## Statistical Methods

| Method | Application |
|--------|-------------|
| Hierarchical bootstrap (90% CI) | All time course and bar comparisons |
| Multiple comparison correction | Figs. 1L and S4J |
| Bregma-lambda distance normalization | Inter-regional distance standardization |

---

## Key Experimental Parameters

| Parameter | Value |
|-----------|-------|
| Imaging wavelength (GCaMP excitation) | 470 nm LED |
| Isosbestic wavelength | 405 nm |
| Camera | sCMOS |
| Virtual corridor pattern | Vertical black and white bars |
| Cortical ROIs | 12 (6 bilateral) |
| Signal attenuation half-depth | ~100 um |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | L5 IT neurons (Tlx3) best distinguish closed vs open loop |
| Fig. 2 | L5 IT differentially activated depending on visual feedback type |
| Fig. 3 | Prediction errors originate in V1, propagate to other areas in L5 IT |
| Fig. 4 | Clozapine increases locomotion responses in V1 L5 IT |
| Fig. 5 | Clozapine reduces correlations mainly in L5 IT |
| Fig. 6 | Long-range decorrelation is distance-dependent and layer-specific |
| Fig. 7 | Three antipsychotics decorrelate L5 IT; amphetamine does not |
| Fig. 8 | Antipsychotics reduce negative prediction error responses and propagation |

---

## Reference Count
73 references cited.
