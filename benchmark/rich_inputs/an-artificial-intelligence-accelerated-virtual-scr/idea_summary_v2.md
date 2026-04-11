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
