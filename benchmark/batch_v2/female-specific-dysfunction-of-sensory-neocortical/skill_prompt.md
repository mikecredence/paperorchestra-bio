Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Cell Reports

## Idea Summary

## Working title

Female-specific cortical circuit hyperexcitability driven by mGluR5-ERalpha signaling in a Pten deletion model of autism

## Core question

How does deletion of the ASD-risk gene Pten produce sex-specific effects on neocortical circuit function, and what molecular signaling pathway mediates the female-selective hyperexcitability?

## Motivation / gap

- ASD is diagnosed 4x more in males than females, but growing evidence suggests it manifests differently in females and may be underdetected
- Some ASD symptoms (sensory processing deficits, epilepsy) are more severe or prevalent in females
- PTEN mutations cause variable phenotypes including macrocephaly, ASD, intellectual disability, and epilepsy (PTEN Hamartoma syndromes)
- PTEN loss-of-function in breast cancer interacts with estrogen receptor alpha (ERalpha) to drive tumor growth via PI3K/Akt/mTOR, but whether similar sex-dependent mechanisms operate in the brain is unknown
- Germline Pten heterozygous deletion mice show female-specific social behavior deficits, yet the underlying brain physiology is unexplored
- No prior work has identified a molecular mechanism for sex-specific effects of an ASD-risk gene on neural circuit function

## Core contribution (bullet form)

- Pten deletion in neocortical pyramidal neurons (NSEPten KO) causes a 56% increase in UP state duration selectively in female mice (L4 somatosensory cortex), with significant sex x genotype interaction in L2/3 (F(1,73)=5.555, p<0.05) and L5 (F(1,71)=7.332, p<0.01)
- Female-specific circuit hyperexcitability depends on mGluR5: the negative allosteric modulator MTEP corrects prolonged UP states only in females; mGluR5 protein levels are elevated in female L5-enriched cortical lysates
- ERalpha is required: two selective ERalpha antagonists (MPP, GNE) rescue UP state duration in female Cre(+) mice; genetic reduction of ERalpha (Esr1fl/+) in Pten KO neurons rescues circuit excitability, protein synthesis, and soma size selectively in females
- Enhanced mGluR5-ERalpha complexes are found in female cortex; signaling through ERK and de novo protein synthesis drives the female-specific phenotype (corrected by U0126, anisomycin, cycloheximide)
- Female NSEPten KO mice show deficits in temporal processing of sensory stimuli (gap-ASSR), reduced social interaction, hyperactivity, enhanced fear learning, and mGluR5-dependent seizures
- Female-specific cortical hyperexcitability and mGluR5-dependent seizure severity are replicated in the clinically relevant germline Pten+/- model

## Method in brief

The primary electrophysiology approach uses extracellular multiunit recordings of spontaneous UP states in acute thalamocortical slices of somatosensory barrel cortex from P18-25 or P42-60 NSEPten KO and Pten+/- mice. UP states provide a readout of intact recurrent excitatory/inhibitory circuit function. Pharmacological manipulations (MTEP for mGluR5, MPP/GNE for ERalpha, U0126 for ERK, anisomycin/cycloheximide for protein synthesis) are applied in the bath to identify signaling pathways driving prolonged UP states. Genetic approaches include conditional reduction of ERalpha (Esr1 floxed allele crossed to NSE-Cre/Pten floxed).

Molecular and biochemical analyses include western blots for mGluR5 protein levels in L5-enriched cortical lysates, co-immunoprecipitation for mGluR5-ERalpha complexes, puromycin incorporation assays (SUnSET) for de novo protein synthesis in individual L5 neurons, and Nissl staining for soma size measurements. In vivo auditory steady-state responses (gap-ASSR) measure temporal processing in P21 pups using EEG. Behavioral testing in young adults includes social interaction (3-chamber), open field locomotion, and fear conditioning. Seizure susceptibility is assessed via flurothyl exposure with survival analysis.

## Target venue

Cell Reports


## Experimental Log

# Experimental Log: Female-Specific Cortical Dysfunction in Pten Deletion ASD Model

## Animal Models and Genotypes

| Model | Genotype | Abbreviation | Background |
|-------|----------|-------------|------------|
| Conditional Pten KO | NSE-Cre(+)/Pten fl/fl | Cre(+) or NSEPten KO | C57BL6 |
| Control | NSE-Cre(-)/Pten fl/fl or Pten fl/+ | Cre(-) | C57BL6 |
| ERalpha reduction | NSE-Cre/Pten fl/fl/Esr1 fl/+ | Cre(+)/Esr1 fl/+ | C57BL6 |
| Germline heterozygous | Pten+/- (CMV-Cre x Pten fl) | Pten+/- | C57BL/6J |
| Cre reporter | Ai14 | tdTomato reporter | C57BL6 |

- NSE-Cre is expressed postnatally (~P2) in layers III-V neurons and CA3/dentate gyrus
- In cortex, NSE-Cre expression is most abundant in sensory areas; >99% of targeted neurons are excitatory (GABA staining)
- Diet: Teklad Global 16% Protein Rodent Diet (no alfalfa or soybean meal to minimize phytoestrogens)

## Experiment 1: UP State Recordings in NSEPten KO Mice (P18-25)

### Slice Preparation

| Parameter | Value |
|-----------|-------|
| Age range | P18-25 |
| Slice type | Thalamocortical |
| Slice thickness | 400 um |
| Recording site | Somatosensory barrel cortex |
| Recovery ACSF | 126 NaCl, 3 KCl, 1.25 NaH2PO4, 26 NaHCO3, 2 MgCl2, 2 CaCl2, 25 d-glucose (mM) |
| High-activity ACSF | 126 NaCl, 5 KCl, 1.25 NaH2PO4, 26 NaHCO3, 1 MgCl2, 1 CaCl2, 25 d-glucose (mM) |
| Temperature | 32 C |
| Electrode type | 0.5 MOhm tungsten (FHC) |
| Amplification | 10,000-fold |
| Sampling rate | 2.5 kHz |
| Filter band | 500 Hz - 3 kHz |
| UP state threshold | 15x RMS noise |
| Minimum UP state duration | 200 ms |
| Minimum inter-UP interval | 600 ms |

### UP State Duration Results (Fig 1C)

| Layer | Sex | Genotype | UP State Duration (relative to Cre- control) | N (slices) | N (mice/sex/genotype) |
|-------|-----|----------|----------------------------------------------|------------|----------------------|
| L4 | Female | Cre(+) | +56% vs Cre(-) | 25-45 | 4-6 |
| L4 | Male | Cre(+) | No change vs Cre(-) | 25-45 | 4-6 |
| L4 | Female | Cre(-) | Baseline | 25-45 | 4-6 |
| L4 | Male | Cre(-) | Baseline (no sex difference) | 25-45 | 4-6 |
| L2/3 | Female | Cre(+) | Increased vs Cre(-) | varies | 4-6 |
| L2/3 | Male | Cre(+) | No change vs Cre(-) | varies | 4-6 |
| L5 | Female | Cre(+) | Increased vs Cre(-) | varies | 4-6 |
| L5 | Male | Cre(+) | No change vs Cre(-) | varies | 4-6 |

### Sex x Genotype Interaction Statistics

| Layer | Test | F statistic | df | p-value |
|-------|------|-------------|-----|---------|
| L2/3 | 2-way ANOVA (sex x genotype) | 5.555 | (1, 73) | < 0.05 |
| L5 | 2-way ANOVA (sex x genotype) | 7.332 | (1, 71) | < 0.01 |

- No effect of sex or genotype on UP state amplitude or frequency in any layer (Supplementary Table 1)
- Fig 1B shows representative UP state traces from L4; prolonged states visible in female Cre(+) but not male Cre(+)

## Experiment 2: mGluR5 Pharmacology on UP States (Fig 2)

### MTEP (mGluR5 NAM) Treatment

| Condition | Sex | Genotype | MTEP Effect on UP State Duration | N (slices) | N (mice/genotype/sex) |
|-----------|-----|----------|----------------------------------|------------|----------------------|
| MTEP 3 uM, 2 hrs | Female | Cre(+) | Corrected (rescued to Cre- level) | 25-45 | 4-8 |
| MTEP 3 uM, 2 hrs | Female | Cre(-) | No effect | 25-45 | 4-8 |
| MTEP 3 uM, 2 hrs | Male | Cre(+) | No effect | 25-45 | 4-8 |
| MTEP 3 uM, 2 hrs | Male | Cre(-) | No effect | 25-45 | 4-8 |

- Fig 2A: Representative UP states from female Cre(-) and Cre(+) slices before and after MTEP
- Fig 2B: Group data showing MTEP selectively rescues female Cre(+) UP state duration

### mGluR5 Protein Levels in Cortex (Fig 2C-D)

| Measure | Sex | Genotype | Result |
|---------|-----|----------|--------|
| mGluR5 protein (L5-enriched lysate) | Female | Cre(+) | Increased vs Cre(-) |
| mGluR5 protein (L5-enriched lysate) | Male | Cre(+) | No change vs Cre(-) |

- Fig 2C: Representative western blots for mGluR5
- Fig 2D: Quantified group data showing female-specific increase in mGluR5 protein

## Experiment 3: ERalpha Pharmacology and Genetics (Fig 3)

### ERalpha Antagonist Treatment

| Drug | Concentration | Duration | Sex | Genotype | Effect on UP States | N (slices) | N (mice/genotype) |
|------|--------------|----------|-----|----------|--------------------|-----------|--------------------|
| MPP | 1 uM | 1.5-2 hrs | Female | Cre(+) | Reduced duration | 16-32 | 4-8 |
| GNE | 1 uM | 1.5-2 hrs | Female | Cre(+) | Reduced duration | 16-32 | 4-8 |
| MPP | 1 uM | 1.5-2 hrs | Male | Cre(+) | No effect | 16-32 | 4-8 |

- Fig 3A-B: Representative UP states and group data for ERalpha antagonists in female Cre(+)

### Genetic Reduction of ERalpha

| Genotype | Sex | UP State Duration | Protein Synthesis | Soma Size |
|----------|-----|-------------------|-------------------|-----------|
| NSE-Cre/Pten fl/fl (Cre+) | Female | Prolonged | Elevated | Enlarged |
| NSE-Cre/Pten fl/fl/Esr1 fl/+ | Female | Rescued to control | Rescued | Rescued |
| NSE-Cre/Pten fl/fl (Cre+) | Male | Normal | Normal | Normal |
| NSE-Cre/Pten fl/fl/Esr1 fl/+ | Male | No change | No change | No change |

- Fig 3C: Representative UP states from female Cre(+) vs Cre(+)/Esr1 fl/+
- Genetic reduction of ERalpha corrects circuit excitability, protein synthesis, and soma size only in females

### mGluR5-ERalpha Complex Levels

| Measure | Sex | Result |
|---------|-----|--------|
| mGluR5-ERalpha co-IP | Female cortex | Elevated vs male |
| mGluR5-ERalpha co-IP | Male cortex | Baseline |

- Fig 3 shows elevated mGluR5-ERalpha complexes selectively in female cortex

## Experiment 4: ERK and Protein Synthesis Inhibitors (Fig 4)

### Pharmacological Rescue of UP States in Females

| Drug | Concentration | Duration | Target | Effect in Female Cre(+) | Effect in Female Cre(-) | N (slices) | N (mice/genotype/condition) |
|------|--------------|----------|--------|------------------------|------------------------|------------|---------------------------|
| U0126 | 20 uM | 2 hrs | ERK (MEK inhibitor) | Corrected UP state duration | No effect | 12-30 | 3-6 |
| Anisomycin | 20 uM | 1 hr | Protein synthesis | Corrected UP state duration | No effect | 12-30 | 3-6 |
| Cycloheximide | 60 uM | 1 hr | Protein synthesis | Corrected UP state duration | No effect | 12-30 | 3-6 |

- Fig 4A: Representative UP states for each drug condition in female Cre(-) and Cre(+)
- Fig 4B-D: Group averages confirming ERK and protein synthesis blockade rescues female Cre(+) phenotype

### Protein Synthesis Measurement (SUnSET Assay, Fig 4E)

| Measure | Sex | Genotype | Result | N (sections) | N (mice) |
|---------|-----|----------|--------|-------------|----------|
| Puromycin incorporation (L5, PTEN KO neurons) | Female | Cre(+) | Increased vs neighboring PTEN+ neurons | 17 | 3 |
| Puromycin incorporation (L5, PTEN KO neurons) | Male | Cre(+) | No change vs neighboring PTEN+ neurons | 17 | 3 |

- mGluR5-driven protein synthesis is selectively elevated in female Pten KO L5 neurons

## Experiment 5: ERalpha Controls Protein Synthesis and Soma Size (Fig 5)

### Protein Synthesis with ERalpha Reduction

| Genotype | Measure | Normalized to PTEN+ neighbors | N (sections) | N (mice) | Test |
|----------|---------|-------------------------------|-------------|----------|------|
| NSE-Cre/Pten fl/fl | Puromycin in PTEN KO L5 neurons | Elevated | 17 | 3 | t-test |
| NSE-Cre/Pten fl/fl/Esr1 fl/+ | Puromycin in PTEN KO L5 neurons | Rescued to control | 17 | 3 | t-test |

- Fig 5A-B: Representative puromycin immunolabeling and group data

### Soma Size with ERalpha Reduction

| Genotype | Sex | Soma Size | N (sections) | N (mice) |
|----------|-----|-----------|-------------|----------|
| NSE-Cre/Pten fl/fl (Cre+) | Female | Enlarged vs Cre(-) | varies | 3 |
| NSE-Cre/Pten fl/fl/Esr1 fl/+ | Female | Rescued | varies | 3 |
| NSE-Cre/Pten fl/fl (Cre+) | Male | Enlarged vs Cre(-) | varies | 3 |
| NSE-Cre/Pten fl/fl/Esr1 fl/+ | Male | Not rescued (still enlarged) | varies | 3 |

- Fig 5C-F: Nissl staining images and quantification of L5 soma size
- ERalpha reduction rescues soma enlargement only in female Pten KO neurons, establishing cell-autonomous role

## Experiment 6: Sensory Processing and Behavior (Fig 6)

### Gap-ASSR (Temporal Processing, P21 Pups)

| Measure | Sex | Genotype | Result |
|---------|-----|----------|--------|
| ITPC during gap-ASSR (auditory cortex) | Female | Cre(+) | Deficit (not greater than baseline) |
| ITPC during gap-ASSR (auditory cortex) | Male | Cre(+) | Deficit |
| ITPC during gap-ASSR (frontal cortex) | Female | Cre(+) | Deficit (not greater than baseline) |
| ITPC during gap-ASSR (frontal cortex) | Male | Cre(+) | Deficit |

- Fig 6A-B: Average ITPC heatmaps for P21 mice from auditory and frontal cortex
- Both sexes show ITPC deficits with the gap stimulus, but female Cre(+) ITPC was not significantly above baseline (more severe)

### Seizure Susceptibility (Flurothyl, Fig 6)

| Measure | Sex | Genotype | Result | Statistical Test |
|---------|-----|----------|--------|-----------------|
| Seizure severity (flurothyl) | Female | Cre(+) | mGluR5-dependent increase | Survival analysis |
| Seizure severity (flurothyl) | Male | Cre(+) | Not mGluR5-dependent | Survival analysis |

- Female NSEPten KO mice show mGluR5-dependent seizures; males do not

## Experiment 7: Germline Pten+/- Model (Fig 7)

### UP State Recordings (6-8 Weeks Old)

| Measure | Sex | Genotype | Result | N (slices) | N (mice/sex/genotype) |
|---------|-----|----------|--------|------------|----------------------|
| UP state duration | Female | Pten+/- | Increased vs WT | 43-58 | 8-12 |
| UP state duration | Male | Pten+/- | No change vs WT | 43-58 | 8-12 |
| UP state frequency | Female | Pten+/- | Reported | 43-58 | 8-12 |
| Total time in UP state | Female | Pten+/- | Increased vs WT | 43-58 | 8-12 |

- Fig 7A: Representative UP states from 6-8 week old male and female Pten+/- mice
- Fig 7B: Group averages showing female-selective increase in UP state duration and total UP time

### Seizure Susceptibility in Pten+/- Mice (P90-100)

| Measure | Sex | Result | Statistical Test |
|---------|-----|--------|-----------------|
| Survival (repeated daily flurothyl) | Female Pten+/- | Decreased survival | Mantel-Cox test |
| Survival (repeated daily flurothyl) | Male Pten+/- | Less affected | Mantel-Cox test |

- Fig 7C: Survival curves showing female-specific seizure vulnerability in Pten+/- mice
- Confirms the female-specific hyperexcitability phenotype in a human disease-relevant model

## Summary of Signaling Pathway

| Component | Role in Female Pten KO | Evidence |
|-----------|----------------------|----------|
| Pten deletion | Hyperactivates PI3K/Akt/mTOR | Genetic model |
| mGluR5 | Elevated protein; drives UP states and seizures | Western blot; MTEP rescue |
| ERalpha | Required for hyperexcitability; forms complexes with mGluR5 | Antagonist rescue; genetic rescue; co-IP |
| ERK | Mediates signaling to protein synthesis | U0126 rescue |
| De novo protein synthesis | Effector of circuit hyperexcitability | Anisomycin/cycloheximide rescue; SUnSET assay |

## Key Metrics and Definitions

| Metric | Definition |
|--------|-----------|
| UP state | Spontaneous persistent activity state, 0.5-1 Hz oscillation, driven by recurrent excitatory/inhibitory synaptic circuits |
| UP state duration | Time amplitude remains above 15x RMS noise threshold (minimum 200 ms) |
| ITPC | Inter-trial phase coherence, measure of temporal consistency of neural responses |
| gap-ASSR | Gap-modulated auditory steady-state response, tests temporal processing of sensory stimuli |
| SUnSET | Surface sensing of translation; puromycin incorporation assay for measuring de novo protein synthesis |
| co-IP | Co-immunoprecipitation for measuring protein-protein interactions |

## Datasets and Baselines

| Dataset/Baseline | Description |
|-----------------|-------------|
| Cre(-) controls | Pten fl/fl or Pten fl/+ without NSE-Cre; baseline for all comparisons |
| Vehicle treatment | Within-genotype drug-free condition for pharmacology experiments |
| PTEN+ neighboring neurons | Internal control for SUnSET assay (protein synthesis) and soma size within same sections |
| WT littermates | Control for Pten+/- experiments |

## Reference Count

- Total references cited: 110

