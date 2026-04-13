Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Nature Communications

## Idea Summary

# Idea Summary: AI-Accelerated Virtual Screening Platform for Drug Discovery

## Working title
An artificial intelligence accelerated virtual screening platform for drug discovery

## Core question
Can an open-source, physics-based virtual screening method with active learning achieve state-of-the-art docking accuracy and efficiently screen multi-billion compound libraries to discover novel hits for therapeutically relevant targets?

## Motivation / gap
- Structure-based virtual screening is key for early drug discovery, but screening multi-billion compound libraries is time- and cost-prohibitive for physics-based docking
- Leading docking programs (Glide, GOLD) and their VS platforms are not freely available to researchers
- AutoDock Vina is free but has slightly lower accuracy than commercial tools
- No open-source scalable platform exists that combines state-of-the-art physics-based docking with active learning for ultra-large library screens
- Deep learning docking models are better suited for blind docking (unknown binding site), but physics-based methods still outperform when the binding site is known
- Most VS methods work well only on hydrophobic, deep, and large protein pockets but struggle with polar, shallow, and small pockets

## Core contribution (bullet form)
- Developed RosettaGenFF-VS, an improved force field combining enthalpy (delta-H) with a new entropy model (delta-S) for ranking different ligands binding to the same target
- Created RosettaVS with two docking modes: VSX (express, rapid initial screening) and VSH (high-precision with full receptor flexibility for final ranking)
- Built OpenVS, an open-source scalable platform using active learning to train a target-specific neural network during docking for efficient triage of multi-billion libraries
- Achieved state-of-the-art performance on CASF2016 (285 complexes) and DUD benchmarks across scoring, docking, screening, and reverse screening powers
- Discovered 7 novel hits to KLHDC2 (14% hit rate from 50 compounds) and 4 novel hits to NaV1.7 VSD4 (44% hit rate from 9 compounds), all with single-digit micromolar binding affinities
- Validated KLHDC2-ligand binding pose with high-resolution X-ray crystallography
- Completed screening of multi-billion compound libraries in less than 7 days for each target

## Method in brief
RosettaVS builds on the Rosetta GALigandDock method with its RosettaGenFF physics-based force field. Key enhancements include new atom types and torsional potentials for modeling billions of small molecules, and a new entropy model combined with enthalpy calculations for accurate cross-compound ranking (RosettaGenFF-VS). The docking protocol has two modes: VSX for rapid initial screening and VSH incorporating full receptor side-chain and partial backbone flexibility for final-stage ranking. This receptor flexibility is a key differentiator from most other VS methods.

The OpenVS platform addresses the computational cost of docking billions of compounds through active learning. During docking runs, a target-specific neural network is simultaneously trained on completed docking results and used to predict and prioritize the most promising compounds for expensive physics-based docking. This iterative triage approach means only a fraction of the full library needs explicit docking. The platform is designed for high scalability and parallelization on HPC clusters.

For target validation, two unrelated targets were screened: KLHDC2 (a novel E3 ubiquitin ligase) and NaV1.7 VSD4 (a human voltage-gated sodium channel pain target). The KLHDC2 campaign included initial screening plus focused library expansion based on a shared substructure among initial hits. Experimental validation used AlphaLISA assays for KLHDC2 and electrophysiology (inactivated-state IC50) for NaV1.7. A crystal structure of the KLHDC2-ligand complex confirmed the predicted binding pose.

## Target venue
Nature Communications


## Experimental Log

# Experimental Log: AI-Accelerated Virtual Screening Platform for Drug Discovery

> Data tables and results extracted from full-text analysis

---

## Platform Architecture Overview

| Component | Description |
|---|---|
| Force field | RosettaGenFF-VS (improved RosettaGenFF) |
| Docking method | RosettaVS (VSX express + VSH high-precision) |
| Platform | OpenVS (open-source, scalable, active learning) |
| Active learning | Target-specific neural network trained during docking |
| Receptor flexibility | Full side-chain + partial backbone (in VSH mode) |
| Scoring | Enthalpy (delta-H) + entropy (delta-S) model |

---

## Benchmark 1: CASF2016 Dataset

### Dataset Details

| Parameter | Value |
|---|---|
| Dataset | CASF2016 (Comparative Assessment of Scoring Functions 2016) |
| Number of complexes | 285 diverse protein-ligand complexes |
| Evaluation categories | Scoring power, docking power, screening power, reverse screening power |
| Benchmark purpose | Standard evaluation for scoring functions |

### CASF2016 Scoring Power

| Method | Performance | Rank |
|---|---|---|
| RosettaGenFF-VS | Top performing | Best or among best |
| Other methods (from Ref 28) | Variable | See Fig. S2 |

- Fig. S2: Full scoring power comparison across all methods
- RosettaGenFF-VS demonstrates superior ability to rank binding affinities

### CASF2016 Docking Power (Fig. S3)

| Metric | RosettaGenFF-VS | Notes |
|---|---|---|
| Top 1 success rate (<2A RMSD) | High | Best among tested |
| Top 2 success rate (<2A RMSD) | High | Competitive |
| Top 3 success rate (<2A RMSD) | High | Competitive |

- Docking power measures ability to find correct binding pose
- Success defined as top-ranked decoy within 2 Angstrom RMSD of native structure
- Docking power independent of entropy model (reported without entropy specification)

### CASF2016 Screening Power

| Metric | RosettaGenFF-VS | Notes |
|---|---|---|
| Top 1% enrichment factor | High | Fig. S4 |
| Best binder in top 1% | High success rate | Fig. S5 |
| Best binder in top 5% | High success rate | Fig. S5 |
| Best binder in top 10% | High success rate | Fig. S5 |

- Fig. S4: Top 1% enrichment factor comparison across all methods
- Fig. S5: Success rate of including best binder in top 1/5/10% ranked molecules

### CASF2016 Reverse Screening Power (Fig. S6)

| Metric | RosettaGenFF-VS | Notes |
|---|---|---|
| Best target in top 1% | High success rate | Target identification |
| Best target in top 5% | High success rate | Target identification |
| Best target in top 10% | High success rate | Target identification |

- Given a ligand, correctly identifies the best protein target

---

## Benchmark 2: DUD Dataset (Fig. 1)

### ROC-AUC Performance (Fig. 1b)

| Method | AUC (averaged over targets, 3 runs) |
|---|---|
| RosettaVS | Highest among tested |
| Other methods (from Ref 28) | Variable |

- Results averaged over targets and from three independent runs
- Fig. 1b shows bar chart comparison of AUC values

### ROC Enrichment at Various False Positive Rates (Fig. 1c)

| False Positive Rate | Metric Type |
|---|---|
| 0.5% | Empty bar |
| 1% | Patterned bar |
| 2% | Solid bar |

- Fig. 1c shows mean ROC enrichments averaged over targets
- RosettaVS outperforms at all false positive rate thresholds

---

## Virtual Screening Campaign 1: KLHDC2

### Target Overview

| Parameter | Value |
|---|---|
| Target protein | KLHDC2 (novel E3 ubiquitin ligase) |
| Library size | Multi-billion compounds |
| Screening time | <7 days |
| Validation assay | AlphaLISA |

### Initial Screening Results (Fig. 2a)

| Metric | Value |
|---|---|
| Compounds synthesized and assayed (initial) | 29 |
| Hits from initial screen | 7 |
| Hit rate (initial) | 7/29 = 24% |
| Binding affinity range | Low micromolar |

### Focused Library Screening (Fig. 2b)

| Metric | Value |
|---|---|
| Focused library basis | Shared substructure from initial hits |
| Compounds synthesized and assayed (focused) | 21 |
| Hits from focused screen | 6 |
| Hit rate (focused) | 6/21 = 29% |

### Overall KLHDC2 Hit Summary

| Metric | Value |
|---|---|
| Total novel hits | 7 (unique compounds with low uM affinity) |
| Total compounds tested | ~50 |
| Overall hit rate | ~14% |
| Affinity range | Single-digit micromolar |

- Fig. 2c: AlphaLISA assay dose-response curves and IC50 values for the seven hit compounds
- Seven compounds show low micromolar binding affinity (highlighted in boxes)
- Shared substructure identified and used for focused library generation

### Crystal Structure Validation (Fig. 3)

| Parameter | Detail |
|---|---|
| Complex | KLHDC2-C29 |
| Method | X-ray crystallography |
| Resolution | High resolution |
| Pose validation | Predicted docking pose confirmed |

- Fig. 3a: Crystal structure showing specific residues interacting with C29 (sticks and balls); hydrogen bonds shown as yellow dashed lines
- Fig. 3b: 2D interaction diagram with hydrogen bonds as blue dashed lines
- Crystal structure validates the computational docking pose prediction

---

## Virtual Screening Campaign 2: NaV1.7

### Target Overview

| Parameter | Value |
|---|---|
| Target protein | NaV1.7 VSD4 (voltage-gated sodium channel) |
| Relevance | Pain target |
| Library size | Multi-billion compounds |
| Screening time | <7 days |
| Validation assay | Electrophysiology (inactivated-state IC50) |

### NaV1.7 Hit Results (Fig. 4)

| Metric | Value |
|---|---|
| Compounds tested | 9 |
| Novel hits | 4 |
| Hit rate | 4/9 = 44% |
| Affinity range | Single-digit micromolar |

### Top NaV1.7 Compound IC50 Values (Fig. 4b)

| Compound | Inactivated-state IC50 (uM) | 95% CI |
|---|---|---|
| Z8739902234 | 1.32 | 1.14 - 1.55 |
| Z8739905023 | 2.23 | 2.14 - 2.46 |

- Fig. 4a: 2D structures of the best two compounds
- Fig. 4b: Concentration-response curves with IC50 values and 95% confidence intervals
- Fig. 4c: Exemplary current traces showing inhibition of inactivated state of NaV1.7
- Fig. 4d: Docked structures of both compounds showing predicted binding poses

---

## Combined Hit Discovery Summary

| Target | Library Size | Hits | Compounds Tested | Hit Rate | Time |
|---|---|---|---|---|---|
| KLHDC2 | Multi-billion | 7 novel | ~50 | 14% | <7 days |
| NaV1.7 VSD4 | Multi-billion | 4 novel | 9 | 44% | <7 days |

---

## RosettaVS Docking Modes

| Mode | Name | Speed | Receptor Flexibility | Use Case |
|---|---|---|---|---|
| VSX | Virtual Screening Express | Fast | Limited | Initial screening / triage |
| VSH | Virtual Screening High-precision | Slower | Full side-chain + partial backbone | Final ranking of top candidates |

---

## Force Field Improvements (RosettaGenFF to RosettaGenFF-VS)

| Enhancement | Purpose |
|---|---|
| New atom types | Model broader chemical space (billions of compounds) |
| New torsional potentials | Improved conformational sampling |
| Improved preprocessing | Handle diverse compound libraries |
| Entropy model (delta-S) | Accurate cross-compound ranking for same target |
| Enthalpy + entropy combination | Total binding free energy estimation |

---

## Active Learning Strategy

| Step | Description |
|---|---|
| 1 | Begin physics-based docking on initial compound subset |
| 2 | Train target-specific neural network on completed docking results |
| 3 | Use neural network to predict/rank remaining compounds |
| 4 | Select most promising compounds for next round of physics-based docking |
| 5 | Iterate until convergence or library exhausted |
| Benefit | Only a fraction of library requires expensive docking |
| Scalability | Designed for HPC cluster parallelization |

- Fig. 1a: Overview of the deep learning guided virtual screening protocol
- Fig. S1: Detailed flowchart of the protocol

---

## Crystallography Data (Table 1)

| Parameter | KLHDC2-C29 Complex |
|---|---|
| Method | Molecular replacement |
| Data type | X-ray diffraction |
| Resolution | High resolution (specific value in Table 1) |
| Refinement | Standard crystallographic refinement |

- Table 1 contains full data collection and refinement statistics

---

## Method Comparison Context

| Feature | RosettaVS | AutoDock Vina | Glide/GOLD | Deep Learning Models |
|---|---|---|---|---|
| Open source | Yes | Yes | No | Varies |
| Receptor flexibility | Full (VSH mode) | Limited | Limited | N/A |
| Active learning platform | Yes (OpenVS) | No | Yes (commercial) | Some |
| Ultra-large library support | Yes | Limited | Yes (commercial) | Yes |
| Pocket type performance | Good on all types | Biased toward hydrophobic | Good | Variable |
| Known binding site | Strong | Good | Strong | Better for blind docking |
| Generalizability | Physics-based (general) | Physics-based | Physics-based | Limited on novel complexes |

---

## Key Advantages of RosettaVS

| Advantage | Explanation |
|---|---|
| Balanced energetics | Better protein-ligand vs intra-ligand molecular energy balance |
| Polar pocket performance | High accuracy on polar, shallow, small pockets |
| Open-source | Freely available to all researchers |
| Scalable | Designed for HPC parallelization |
| Active learning | Efficient chemical space exploration |
| Receptor flexibility | Unique among open-source tools at this scale |

---

## Figure Summary

| Figure | Content |
|---|---|
| Fig. 1a | VS protocol overview with active learning |
| Fig. 1b | ROC-AUC benchmark comparison (DUD dataset) |
| Fig. 1c | ROC enrichment at 0.5%, 1%, 2% FPR |
| Fig. 2a | KLHDC2 initial screening: 7/29 compounds |
| Fig. 2b | KLHDC2 focused screening: 6/21 compounds |
| Fig. 2c | AlphaLISA IC50 curves for 7 hit compounds |
| Fig. 3a | Crystal structure KLHDC2-C29 with interactions |
| Fig. 3b | 2D interaction diagram |
| Fig. 4a | 2D structures of best NaV1.7 compounds |
| Fig. 4b | Dose-response curves with IC50 values |
| Fig. 4c | Current trace electrophysiology data |
| Fig. 4d | Docked structures of NaV1.7 hits |
| Fig. S1 | Detailed VS flowchart |
| Fig. S2 | CASF2016 scoring power (all methods) |
| Fig. S3 | CASF2016 docking power (all methods) |
| Fig. S4 | CASF2016 screening power enrichment factors |
| Fig. S5 | CASF2016 screening power success rates |
| Fig. S6 | CASF2016 reverse screening power |

---

## Future Directions

| Direction | Description |
|---|---|
| GPU acceleration | Speed up ligand docking with GPU computing |
| Deep learning pose generation | Generative AI for efficient pose generation |
| Improved surrogate models | Better active learning guidance for chemical space exploration |
| Generalizable DL score function | Deep learning for improved binder discrimination |
| Non-small molecule templates | Use macrocycles or antibody loops as template structures |

