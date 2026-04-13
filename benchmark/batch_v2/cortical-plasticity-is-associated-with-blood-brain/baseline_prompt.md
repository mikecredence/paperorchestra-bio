Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title

Activity-dependent blood-brain barrier modulation underlies synaptic plasticity in the healthy somatosensory cortex

## Core question

Does physiological neuronal activity induce focal modulation of blood-brain barrier permeability in the healthy brain, and if so, does this BBB modulation play a mechanistic role in synaptic plasticity?

## Motivation / gap

- BBB dysfunction and serum albumin leakage are well-characterized in brain injury models, where they induce pathological plasticity, hyper-excitability, and seizures, but whether physiological neuronal activity modulates BBB permeability in the healthy brain is unknown
- Emerging evidence from whisker stimulation and circadian rhythm studies hints at activity-dependent BBB changes, but the mechanisms and functional consequences have not been investigated
- TGF-beta signaling has been linked to both pathological BBB changes and synaptic plasticity, yet whether it mediates activity-dependent BBB modulation in normal conditions is untested
- The role of caveolae-mediated transcytosis in physiological (as opposed to pathological) BBB modulation has not been examined
- No study has demonstrated physiological BBB modulation in humans in response to a motor/sensory task

## Core contribution (bullet form)

- Prolonged limb stimulation (30 min, 6 Hz) in rats induces focal BBB permeability increase in the contralateral somatosensory cortex, demonstrated by extravasation of NaFlu, Evans blue, and Alexa488-conjugated albumin
- ELISA confirmed higher albumin concentration in stimulated cortex at 30 min post-stimulation, declining at 4 and 24 hours; albumin levels were significantly lower than in photothrombosis injury controls
- Stimulation-induced BBB opening is associated with long-term potentiation (LTP) of somatosensory evoked potentials (SEPs), and direct cortical perfusion of albumin alone also induces LTP
- BBB modulation and LTP depend on AMPA/NMDA neurotransmission, caveolae-mediated transcytosis (blocked by methyl-beta-cyclodextrin), and TGF-beta receptor signaling (blocked by SJN)
- RNA-seq of stimulated cortex revealed differentially expressed genes enriched for BBB transport and synaptic plasticity ontologies, with upregulation of caveolae and vesicle trafficking genes
- First evidence in humans: 30 min of hand squeezing a stress ball increased BBB permeability in the activated motor cortex region as measured by DCE-MRI, co-localized with fMRI activation

## Method in brief

In rats, the experimental paradigm involved 30 minutes of forelimb or hindlimb electrical stimulation (6 Hz, 2-3 mA, 0.1 ms pulses) delivered via subdermal needle electrodes. BBB permeability was assessed using intravital fluorescence microscopy (wide-field and two-photon) with sodium fluorescein (NaFlu) and Evans blue tracers injected intravenously, histological analysis of tracer extravasation, and ELISA quantification of albumin in cortical tissue at multiple time points (30 min, 4 h, 24 h post-stimulation). Synaptic plasticity was evaluated by comparing somatosensory evoked potentials (SEPs) from 1-min test stimulations delivered before and after the 30-min conditioning stimulation. Pharmacological blockers (CNQX/AP5 for glutamate receptors, methyl-beta-cyclodextrin for caveolae, SJN for TGF-beta receptors) were applied via cortical perfusion to dissect mechanisms.

In humans, subjects performed a 30-minute stress-ball squeezing task. Functional MRI localized the activated cortical area, and dynamic contrast-enhanced (DCE) MRI assessed BBB permeability before and after the motor task. Permeability maps were compared within the fMRI-defined activation region. Additionally, RNA-sequencing was performed on rat cortical tissue at 1 h and 24 h post-stimulation, with differential gene expression analysis and Gene Ontology enrichment to identify molecular pathways involved in the activity-dependent BBB and plasticity response.

## Target venue

eLife


## Experimental Log

# Experimental Log: Cortical Plasticity is Associated with Blood-Brain Barrier Modulation

## 1. Animal Model and Surgical Parameters

| Parameter | Value |
|---|---|
| Species/strain | Adult Sprague Dawley male rats |
| Weight | 300-350 g |
| Supplier | Harlan Laboratories |
| Anesthesia | Ketamine (100 mg/ml, 0.08 ml/100 g) + Xylazine (20 mg/ml, 0.06 ml/100 g), IP |
| Body temperature | 37 +/- 0.5 C (feedback-controlled heating pad) |
| Monitoring | Heart rate, breath rate, O2 saturation (MouseOx) |
| Craniotomy location | 4 mm caudal, 2 mm frontal, 5 mm lateral to bregma (right sensorimotor cortex) |
| Cortical perfusion | aCSF continuously applied to exposed cortex |

### Artificial CSF Composition

| Component | Concentration (mM) |
|---|---|
| NaCl | 124 |
| NaHCO3 | 26 |
| NaH2PO4 | 1.25 |
| MgSO4 | 2 |
| CaCl2 | 2 |
| KCl | 3 |
| Glucose | 10 |
| pH | 7.4 |

## 2. Stimulation Protocol

| Parameter | Value |
|---|---|
| Stimulation target | Left forelimb or hindlimb |
| Electrode type | Two subdermal needle electrodes |
| Pulse shape | 0.1 ms square pulses |
| Current | 2-3 mA |
| Frequency | 6 Hz |
| Test stimulation | 360 pulses (60 s, 1 min) |
| Conditioning stimulation | 30 min at 6 Hz |
| Test stimulation timing | Before (baseline) and after conditioning stimulation |

## 3. BBB Permeability Assessment -- Tracers and Methods (Figure 1)

### 3.1 Tracer Summary

| Tracer | Molecular Weight Class | Route | Detection Method |
|---|---|---|---|
| Sodium fluorescein (NaFlu) | Low MW (~376 Da) | Intravenous | Intravital fluorescence microscopy |
| Evans blue (EB) | High MW (binds albumin, ~67 kDa complex) | Intravenous | Histological fluorescence |
| Alexa Fluor 488-conjugated albumin | High MW (~67 kDa) | Intravenous | Histological fluorescence |

### 3.2 NaFlu Extravasation Results

| Condition | Extravasation Observed? | Location |
|---|---|---|
| Control (no 30-min stim) | No | -- |
| 30-min stimulation | Yes | Contralateral somatosensory cortex (around responding blood vessels) |
| Ipsilateral to stimulated limb | No | -- |

Fig 1f-g: Fluorescent angiography before and immediately after 30-min stimulation showed local NaFlu extravasation around responding blood vessels.
Fig 1m-n: Histological confirmation of NaFlu in extravascular space around small vessels in contralateral somatosensory cortex; not in ipsilateral cortex.

### 3.3 Evans Blue and Alexa488-Albumin (Separate Cohort, No Craniotomy)

| Tracer | Extravasation in Contralateral Hemisphere | Interpretation |
|---|---|---|
| Evans blue | Yes | Albumin-bound dye present in neuropil |
| Alexa488-conjugated albumin | Yes | Confirms serum albumin crosses BBB after stimulation |

Fig 1h-k: Brain sections showing EB and Alexa488-Alb extravasation in contralateral hemisphere.

### 3.4 Albumin ELISA Time Course (Figure 1l)

| Time Post-Stimulation | Albumin Concentration (Stimulated Cortex vs. Sham) | Significance |
|---|---|---|
| 30 min | Higher in stimulated cortex | Significant vs. sham |
| 4 hours | Declining | Reduced compared to 30 min |
| 24 hours | Near baseline | Reduced compared to 30 min |
| Photothrombosis (24 h, positive control) | Significantly higher than all stimulation timepoints | Significantly higher than sham and all stim groups |

Fig 1l: ELISA bar plot showing albumin concentration peaks at 30 min post-stimulation and declines over 4 and 24 hours. Photothrombosis-induced albumin levels were substantially higher than physiological stimulation at all time points.
Fig S1d: Positive control photothrombosis data confirming the assay sensitivity.

## 4. Electrophysiology and Synaptic Plasticity (Figure 2)

### 4.1 Somatosensory Evoked Potential (SEP) Recording

| Parameter | Value |
|---|---|
| Recording location | L2/3 sensorimotor cortex |
| Recording type | Local field potential (LFP) |
| Test stimulation | 1 min, 6 Hz, 2 mA |
| Measurement | SEP amplitude before vs. after 30-min stimulation |

### 4.2 LTP Induction by Stimulation

| Condition | SEP Amplitude Change | Interpretation |
|---|---|---|
| Before 30-min stim | Baseline | -- |
| After 30-min stim | Increased (potentiated) | LTP of somatosensory evoked responses |
| Sham (no 30-min stim) | No change | Confirms potentiation requires prolonged stimulation |

Fig 2a: LFP traces showing SEP before and after conditioning stimulation; amplitude increased post-stimulation.
Fig 2b: SEP amplitude quantification showing significant potentiation.

### 4.3 Albumin Perfusion Induces LTP

| Condition | SEP Change | Significance |
|---|---|---|
| aCSF control perfusion | No change | -- |
| Albumin cortical perfusion | Increased (LTP) | Direct application of albumin to cortex is sufficient for potentiation |

Fig 2: Direct cortical perfusion of serum albumin (without peripheral stimulation) replicated the LTP effect, supporting the hypothesis that albumin extravasation mediates activity-dependent plasticity.

## 5. Pharmacological Blocker Experiments (Figure 3)

### 5.1 Blockers Used

| Blocker | Target | Concentration | Purpose |
|---|---|---|---|
| CNQX/AP5 | AMPA/NMDA glutamate receptors | 50 uM | Block excitatory neurotransmission |
| Methyl-beta-cyclodextrin (mBCD) | Caveolae / lipid rafts | 10 uM | Inhibit caveolae-mediated transcytosis |
| SJN | TGF-beta receptor | 0.3 mM | Block TGF-beta signaling |

### 5.2 Effect of Blockers on BBB Permeability (PI = Permeability Index)

| Condition | BBB Permeability (NaFlu extravasation) | Compared to 30-min Stim Alone |
|---|---|---|
| 30-min stimulation alone | Increased (reference) | -- |
| CNQX/AP5 + 30-min stim | Blocked (no increase) | Significantly reduced |
| mBCD + 30-min stim | Blocked (no increase) | Significantly reduced |
| SJN + 30-min stim | Blocked (no increase) | Significantly reduced |

Fig 3b: NaFlu permeability maps showing tracer accumulation after stimulation alone (visible) vs. after blocker + stimulation (absent).
Fig 3c: Permeability index (PI) quantification confirming all three blockers prevented stimulation-induced BBB opening.

### 5.3 Effect of Blockers on Synaptic Plasticity (LTP)

| Condition | SEP Potentiation | Compared to 30-min Stim Alone |
|---|---|---|
| 30-min stimulation alone | Present (LTP) | -- |
| CNQX/AP5 + 30-min stim | Blocked (no LTP) | Significantly reduced |
| mBCD + 30-min stim | Blocked (no LTP) | Significantly reduced |
| SJN + 30-min stim | Blocked (no LTP) | Significantly reduced |

### 5.4 Effect on Hemodynamic Response

| Condition | Hemodynamic Response (HbT) | Notes |
|---|---|---|
| 30-min stimulation alone | Present | Normal neurovascular coupling |
| CNQX/AP5 + 30-min stim | Blocked | Expected, since neural activity is blocked |
| mBCD + 30-min stim | Not significantly affected | Caveolae inhibition did not disrupt vasodilation |
| SJN + 30-min stim | Not significantly affected | TGF-beta blockade did not disrupt vasodilation |

Key finding: mBCD and SJN block BBB modulation and LTP without significantly disrupting the hemodynamic response, indicating that the BBB-plasticity pathway is separable from the vasodilatory component of neurovascular coupling.

## 6. Transcriptomic Analysis (Figure 4)

### 6.1 RNA-Seq Design

| Parameter | Value |
|---|---|
| Tissue | Contralateral somatosensory cortex |
| Timepoints | 1 hour and 24 hours post-stimulation |
| Comparison | 24 h vs. 1 h post-stimulation |
| Sample size | n = 8 rats per group |
| Statistical test for DEGs | Wald Test |
| Visualization | Scatter plot of log fold change vs. mean expression |

### 6.2 Differentially Expressed Genes (DEGs)

| Category | Direction (24h vs 1h) | Key Genes / Pathways |
|---|---|---|
| BBB transport genes | Upregulated at 24 h | Caveolae-related, vesicle trafficking |
| Synaptic plasticity genes | Upregulated at 24 h | Postsynaptic density, long-term potentiation |
| Immune/inflammatory | Transiently upregulated at 1 h | Declining by 24 h |

Fig 4a: Volcano/scatter plot showing significant DEGs (blue dots) between 24 h and 1 h timepoints.

### 6.3 Gene Ontology Enrichment

| GO Category | Enrichment Direction | Key Terms |
|---|---|---|
| BBB transport | Enriched in 24 h | Vesicle-mediated transport, transcytosis |
| Synaptic plasticity | Enriched in 24 h | Postsynaptic density, synapse organization |
| Neuronal activity response | Enriched in 1 h | Immediate early genes, activity-dependent transcription |

Fig 4b: Top Gene Ontologies enriched in the 24 h vs 1 h comparison, highlighting convergence of BBB transport and synaptic plasticity pathways.

## 7. Human Experiments (Figure 5)

### 7.1 Protocol

| Parameter | Value |
|---|---|
| Task | Squeeze elastic stress ball continuously for 30 min |
| Hand | One hand (lateralized task) |
| MRI sequences | T1-weighted, fMRI (task localization), DCE-MRI (BBB permeability) |
| DCE-MRI timing | Before and after 30-min task |

### 7.2 Results

| Measure | Finding |
|---|---|
| fMRI activation | Contralateral motor/somatosensory cortex activated during task |
| DCE-MRI BBB permeability | Increased in the fMRI-defined activation region after 30-min task |
| Spatial co-localization | BBB permeability increase co-localized with fMRI activation map |

Fig 5a: Schematic of stress-ball squeezing task.
Fig 5b: Timeline of MRI acquisition protocol.
Fig 5c: Activation map (t-statistic) from fMRI overlaid on anatomical image showing contralateral motor cortex activation.
Fig 5: DCE-MRI permeability maps showing increased BBB permeability in the region corresponding to fMRI activation after the 30-min motor task.

## 8. Positive Control: Photothrombosis Model

| Parameter | Value |
|---|---|
| Model | Photothrombosis (PT)-induced ischemia |
| Timepoint | 24 hours post-PT |
| Albumin concentration | Significantly higher than sham and all stimulation timepoints |
| Purpose | Validates ELISA sensitivity and distinguishes physiological from pathological BBB opening |

## 9. Summary of Mechanistic Pathway

| Step | Component | Evidence |
|---|---|---|
| 1 | Neuronal activity (30-min stimulation) | LFP recordings confirm sustained cortical activation |
| 2 | Glutamate release and AMPA/NMDA activation | CNQX/AP5 blocks both BBB opening and LTP |
| 3 | Caveolae-mediated albumin transcytosis | mBCD blocks BBB opening and LTP; histology shows transcytosis |
| 4 | Albumin enters neuropil | ELISA, EB, Alexa488-Alb confirm albumin extravasation |
| 5 | TGF-beta receptor signaling | SJN blocks BBB opening and LTP |
| 6 | Synaptic potentiation (LTP) | SEP amplitude increase; direct albumin perfusion sufficient |
| 7 | Gene expression changes | RNA-seq shows upregulation of BBB transport and plasticity genes |

## 10. Key Experimental Comparisons

| Comparison | BBB Permeability | LTP | Hemodynamic Response |
|---|---|---|---|
| Stim vs. sham | Increased | Present | Present |
| CNQX/AP5 + stim vs. stim | Blocked | Blocked | Blocked |
| mBCD + stim vs. stim | Blocked | Blocked | Not significantly affected |
| SJN + stim vs. stim | Blocked | Blocked | Not significantly affected |
| Albumin perfusion vs. aCSF | N/A (direct application) | Present | N/A |
| Human task vs. baseline | Increased (DCE-MRI) | Not measured | Not measured |

## 11. Imaging Modalities Used

| Modality | Species | Purpose |
|---|---|---|
| Wide-field intravital microscopy | Rat | Arterial diameter, HbT signal, NaFlu extravasation |
| Two-photon microscopy | Rat | High-resolution vascular imaging |
| Histological fluorescence | Rat | EB, Alexa488-Alb, NaFlu in tissue sections |
| ELISA | Rat | Quantitative albumin concentration in cortical tissue |
| fMRI (BOLD) | Human | Localize cortical activation during motor task |
| DCE-MRI | Human | Quantify BBB permeability before and after task |
| RNA-sequencing | Rat | Transcriptomic profiling of stimulated cortex |

## 12. Statistical and Design Notes

| Feature | Detail |
|---|---|
| Blinding | All experiments and data analysis performed blinded to treatment group |
| Positive control | Photothrombosis model for ELISA validation |
| Lateralization control | Contralateral vs. ipsilateral cortex comparison |
| Sham controls | Electrode placement without 30-min stimulation |
| Human sample | Subjects performed task with one hand; contralateral cortex analyzed |
| Reference count | 71 |

## 13. Figure Summary

- Fig 1: Stimulation-induced BBB permeability increase demonstrated by NaFlu, EB, Alexa488-albumin extravasation, and ELISA time course
- Fig 2: LTP of somatosensory evoked potentials after stimulation; albumin perfusion alone also induces LTP
- Fig 3: Pharmacological blockers (CNQX/AP5, mBCD, SJN) prevent both BBB opening and LTP without disrupting hemodynamic responses (mBCD, SJN)
- Fig 4: RNA-seq reveals DEGs enriched for BBB transport and synaptic plasticity Gene Ontologies
- Fig 5: Human DCE-MRI shows BBB permeability increase co-localized with fMRI activation after 30-min motor task

