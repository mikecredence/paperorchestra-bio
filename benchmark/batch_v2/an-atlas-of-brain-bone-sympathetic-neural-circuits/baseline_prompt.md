Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title
Mapping the Central Sympathetic Nervous System Outflow to Bone Using Pseudorabies Viral Tracing

## Core question
Which brain regions send sympathetic nervous system (SNS) efferent signals to bone, and how is this central outflow distributed across the neuroaxis?

## Motivation / gap
- Prior work established that SNS tone regulates bone metabolism (formation and resorption), but the specific brain sites driving this outflow were unknown
- Histological studies confirmed rich SNS innervation of periosteum and bone marrow (TH+, DBH+, NPY+ fibers), but lacked circuit-level mapping back to the brain
- Leptin's anti-osteogenic actions are known to route through VMH via SNS, yet the full landscape of central nodes was uncharted
- Only one prior study (rat femoral bone marrow) attempted hierarchical circuit tracing, and it covered a limited set of brain sites
- Understanding central bone pain mechanisms requires knowing which brain regions participate in bone-directed SNS circuits
- PDE5A-containing neurons were recently linked to bone via specific brain nuclei, but a comprehensive atlas was still missing

## Core contribution (bullet form)
- First comprehensive atlas identifying 87 brain nuclei/sub-nuclei/regions across 6 brain divisions (midbrain/pons, hypothalamus, medulla, forebrain, cerebral cortex, thalamus) that send SNS outflow to bone
- Demonstrated site-specific variation in infection levels: raphe magnus (RMg) of medulla and periaqueductal gray (PAG) of midbrain showed highest PRV152 labeling
- Validated methodology with negative control (PRV152 placed on bone surface produced no EGFP signal) vs. positive injection into periosteum/metaphysis
- Confirmed bilateral brain labeling from unilateral right femur injection, consistent with prior SNS tracing literature
- Identified PRV152-infected neurons in IML of spinal cord at T13-L2 levels, confirming the bone-SNS ganglia-IML-brain route
- Established overlapping but distinct circuits to femur vs. femoral bone marrow, with key shared nodes including PAG, somatosensory cortex, MPOM, periventricular thalamic nucleus, PVH, LA, and RPa

## Method in brief
Adult male mice (3-4 months old, N=6) received unilateral PRV152 microinjections into the right femur-tibia joint. PRV152 (expressing EGFP, titer 4.7x10^9 pfu/mL) was injected into five loci (150 nL per locus) distributed across the bone metaphysis and periosteum, regions enriched with SNS innervation. The virus travels exclusively in retrograde fashion, enabling mapping of the complete periphery-to-brain neuroaxis. Animals were sacrificed 6 days post-injection based on pilot timing studies.

Brains were perfusion-fixed, cryoprotected, and sectioned at 25 um on a freezing microtome. Immunofluorescence was performed using chicken anti-GFP primary antibody followed by Alexa 488-conjugated secondary antibody. Sections were examined using a Nikon Eclipse Ni-E fluorescence microscope and brain regions identified using the Allen Mouse Brain Atlas.

Four of six mice were included in analysis (two excluded due to over-infection evidenced by widespread cloudy plaques). PRV152-labeled neurons were quantified across all brain divisions. A negative control confirmed no EGFP signal when virus was placed on the bone surface rather than injected. IML labeling at T13-L2 spinal cord levels validated the expected SNS route of infection.

## Target venue
eLife


## Experimental Log

# Experimental Log: Brain-Bone SNS Circuit Atlas

## Experiment Overview
- **Model**: Adult male mice, 3-4 months old
- **Sample size**: N=6 injected, N=4 included in analysis
- **Viral tracer**: PRV152 (EGFP-expressing pseudorabies virus)
- **Titer**: 4.7 x 10^9 pfu/mL
- **Injection target**: Right femur-tibia joint (metaphysis and periosteum)
- **Injection protocol**: 5 loci, 150 nL per locus
- **Survival time**: 6 days post-injection
- **Sectioning**: 25 um, freezing stage sliding microtome
- **Exclusion criteria**: Over-infection (widespread cloudy plaques) -- 2 of 6 mice excluded

---

## Validation Experiments

### Table 1: Control vs. Injection Validation

| Condition | PRV152 Placement | PVH EGFP Signal | RPa EGFP Signal | IML Labeling (T13-L2) |
|-----------|-----------------|-----------------|-----------------|----------------------|
| Negative control | On bone surface | None detected | None detected | Not assessed |
| Experimental | Injected into periosteum/metaphysis | Positive | Positive | Positive |

### Table 2: Animal Inclusion Summary

| Mouse ID | PRV152 Status | Infection Quality | Included in Analysis |
|----------|--------------|-------------------|---------------------|
| 1 | Infected | Even infection across neuroaxis | Yes |
| 2 | Infected | Even infection across neuroaxis | Yes |
| 3 | Infected | Even infection across neuroaxis | Yes |
| 4 | Infected | Even infection across neuroaxis | Yes |
| 5 | Over-infected | Widespread cloudy plaques | No |
| 6 | Over-infected | Widespread cloudy plaques | No |

---

## PRV152-Labeled Brain Regions by Division

### Table 3: Summary of Brain Divisions Containing PRV152-Labeled Neurons

| Brain Division | Number of Nuclei/Sub-nuclei/Regions Identified |
|---------------|------------------------------------------------|
| Midbrain and Pons | Multiple nuclei identified |
| Hypothalamus | Multiple nuclei identified |
| Hindbrain Medulla | Multiple nuclei identified |
| Forebrain | Multiple nuclei identified |
| Cerebral Cortex | Multiple nuclei identified |
| Thalamus | Multiple nuclei identified |
| **Total** | **87** |

### Table 4: Key Brain Sites with High PRV152 Infection Levels

| Brain Region | Abbreviation | Brain Division | Relative PRV152 Infection Level |
|-------------|-------------|----------------|-------------------------------|
| Periaqueductal gray | PAG | Midbrain | High |
| Raphe magnus | RMg | Medulla | High |
| Lateral hypothalamus | LH | Hypothalamus | High |
| Raphe pallidus | RPa | Medulla | High |
| Medial preoptic nucleus, medial part | MPOM | Forebrain | High |
| Primary somatosensory cortex, hindlimb | S1HL | Cerebral Cortex | High |
| Periventricular nucleus | pv | Thalamus | High |
| Paraventricular hypothalamic nucleus | PVH | Hypothalamus | Moderate-High |

---

## Laterality Analysis

### Table 5: Bilateral Labeling Pattern

| Injection Side | Brain Labeling Pattern | Hemispheric Dominance |
|---------------|----------------------|----------------------|
| Right femur (unilateral) | Bilateral | No noticeable dominance |

This bilateral pattern is consistent with prior PRV tracing studies of SNS and sensory innervation of fat depots.

---

## Spinal Cord Findings

### Table 6: Spinal Cord IML Labeling

| Spinal Level | PRV152 Labeling in IML | Interpretation |
|-------------|----------------------|----------------|
| T13 | Positive | Confirms bone-SNS ganglia-IML-brain route |
| L1 | Positive | Consistent with prior studies |
| L2 | Positive | Classic SNS spinal cord neuron territory |

---

## Comparison with Prior Studies

### Table 7: Shared SNS Circuits -- Femur vs. Bone Marrow

| Brain Region | Present in Femur (this study) | Present in Bone Marrow (prior rat study) | Shared Circuit |
|-------------|------------------------------|----------------------------------------|----------------|
| PAG (midbrain) | Yes | Yes | Yes |
| Somatosensory cortex | Yes | Yes | Yes |
| MPOM (forebrain) | Yes | Yes | Yes |
| Periventricular nucleus (thalamus) | Yes | Yes | Yes |
| PVH (hypothalamus) | Yes | Yes | Yes |
| Lateral hypothalamic nucleus (LA) | Yes | Yes | Yes |
| RPa (medulla) | Yes | Yes | Yes |

The overlapping but not identical patterns suggest separate site-specific SNS circuits may project to the femur and femoral bone marrow.

---

## SNS Marker Context

### Table 8: Known SNS Markers in Bone Innervation

| Marker | Fiber Type | Primary Location |
|--------|-----------|-----------------|
| Tyrosine hydroxylase (TH) | Noradrenergic | Vasculature-associated |
| Dopamine beta hydroxylase (DBH) | Noradrenergic | Vasculature-associated |
| Neuropeptide Y (NPY) | Noradrenergic | Vasculature-associated |
| Vesicular acetylcholine transporter (VAChT) | Cholinergic | Vasculature-associated |
| Vasoactive intestinal polypeptide (VIP) | Peptidergic | Parenchymal |

---

## Pain Circuit Relevance

### Table 9: Key Nodes in the Brain-Bone Pain Neuroaxis

| Node | Role in Pain Circuit | Connection |
|------|---------------------|-----------|
| PVH | SNS pre-autonomic neurons | Projects to PAG |
| PAG | SNS relay, pain modulation | Receives from PVH, projects to RPa-RMg |
| RPa-RMg | Terminal relay | Projects to dorsal horn of spinal cord |
| Dorsal horn | Enkephalin release regulation | Receives from RPa-RMg |

Fig 3 shows the diagrammatic outline of the SNS brain-bone neuroaxis relevant to pain, illustrating a pathway from PVH through PAG to RPa-RMg and then to the dorsal horn where enkephalin release is regulated.

---

## Experimental Parameters

### Table 10: Detailed Experimental Protocol Parameters

| Parameter | Value |
|-----------|-------|
| Light cycle | 12h:12h light:dark |
| Housing temperature | 22 +/- 2 C |
| Anesthesia | Isoflurane 2-3% in oxygen |
| Injection volume per locus | 150 nL |
| Number of injection loci | 5 |
| Viral titer | 4.7 x 10^9 pfu/mL |
| Post-injection hold time | 60 seconds per injection |
| Post-fixation time | 3-4 hours at 4 C |
| Cryoprotection | 30% sucrose in 0.1 M PBS |
| Section thickness | 25 um |
| Primary antibody | Chicken anti-GFP (1:500) |
| Secondary antibody | Alexa Fluor 488 goat anti-chicken (1:200) |
| Blocking serum | 10% normal goat serum |
| Incubation (primary) | Overnight at 4 C |
| Incubation (secondary) | 2 hours at room temperature |

---

## Figure Observations

- **Fig 1**: Demonstrates validation of PRV152 tracing. No EGFP signal in PVH or RPa when PRV152 was placed on bone surface (negative control). Positive EGFP immunoreactivity in PVH when PRV152 was injected into periosteum or metaphysis. PRV152-infected neurons visible in IML at T13-L2 spinal cord levels.

- **Fig 2**: Quantifies PRV152-labeled neurons across all brain regions, sub-regions, and nuclei. Shows distribution across six brain divisions: hypothalamus, midbrain and pons, medulla, forebrain, cerebral cortex, and thalamus. Reveals site-specific variation in infection density.

- **Fig 3**: Provides diagrammatic outline of the SNS brain-bone neuroaxis relevant to pain processing. Illustrates the circuit from PVH to PAG to RPa-RMg to dorsal horn of spinal cord, where enkephalin release is modulated.

---

## Key Quantitative Findings

### Table 11: Summary Statistics

| Metric | Value |
|--------|-------|
| Total brain nuclei/sub-nuclei/regions identified | 87 |
| Brain divisions with PRV152+ neurons | 6 |
| Animals injected | 6 |
| Animals included in analysis | 4 |
| Animals excluded (over-infection) | 2 |
| Injection loci per animal | 5 |
| Volume per injection locus | 150 nL |
| Days post-injection to sacrifice | 6 |
| Spinal cord levels with IML labeling | T13-L2 |

---

## Datasets and Resources Used
- Allen Mouse Brain Atlas (for region identification)
- Prior PRV152 tracing data from fat depot studies (for validation comparison)
- Prior rat femoral bone marrow tracing data (for cross-species comparison)

## Metrics
- EGFP immunofluorescence signal (qualitative: present/absent, and relative intensity)
- Number of PRV152-labeled neurons per brain region
- Bilateral vs. ipsilateral labeling pattern assessment

