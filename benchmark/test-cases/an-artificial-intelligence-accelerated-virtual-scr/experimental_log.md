# Experimental Log: An artificial intelligence accelerated virtual screening platform for drug discovery

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsDevelopment of an AI accelerated virtual screening platformOur previously developed Rosetta GALigandDock is a ligand docking method that uses a physics-based force field, RosettaGenFF, that previously has shown superior performance in ligand docking accuracy23.
- Building upon recent works4–8, we developed an open-source virtual screening (OpenVS) platform that uses active learning techniques to simultaneously train a target-specific neural network during the docking computations to efficiently triage and select the most promising compounds for expensive doc
- This platform was also designed to be highly scalable and parallelizable for large-scale virtual screens.RosettaVS shows state-of-the-art performance on virtual screening benchmarksWe first used the Comparative Assessment of Scoring Functions 2016 (CASF2016) dataset27,28 to benchmark the performance
- The CASF2016, consisting of 285 diverse protein ligand complexes, is a standard benchmark specifically designed for scoring function evaluation.
- Recent developments of deep learning based score functions have demonstrated superior performance on these benchmarks16,29,30, however, it is not clear how generalizable these methods are to novel compounds and receptors.
- Even when a cutoff of 0.6 Tanimoto similarity for ligands and a sequence identity of 30% for proteins were used, it is likely that the contamination of these validation benchmarks still occurred.
- Because of this, our subsequent comparisons will focus on other physics-based scoring functions, including the top-performing ones from Ref28.
- S3, RosettaGenFF-VS achieves the leading performance to accurately distinguish the native binding pose from decoy structures.
- The second metric is the success rate of placing the best binder among the 1%, 5% or 10% top-ranked ligands over all target proteins in the dataset.
- S4, the top 1% enrichment factor from RosettaGenFF-VS (EF1%=16.72) outperforms the second-best method (EF1%=11.9) by a significant margin.
- S5 illustrates that RosettaGenFF-VS excels in identifying the best binding small molecule within the top 1/5/10% ranking molecules, surpassing all other methods.
- Analysis of our method on various screening power subsets28 shows significant improvements in more polar, shallower and smaller protein pockets compared to other methods (Fig.
- However, in a realistic virtual screening scenario, the docking method must accurately score the complex while also effectively sampling the conformations.To this end, we further evaluated the virtual screening performance of VSX and VSH mode from RosettaVS protocol on the Directory of Useful Decoys
- The DUD dataset consists of 40 pharmaceutical relevant protein targets with over 100,000 small molecules.
- ROC enrichment, which addresses a few deficiencies of the enrichment factor32, measures the true positive enrichment at a given X% false positive rate.
- Notably, RosettaVS outperforms the second-best method by a factor of two (0.5/1.0% ROC enrichment), achieving state-of-the-art performance in early ROC enrichment, further highlighting the effectiveness of RosettaVS.
- Furthermore, VSH mode slightly outperforms VSX mode due to the capability of modeling the conformational changes of the pocket sidechains induced by the ligand(see Methods).Discovery of a novel small molecule hit to KLHDC2 ubiquitin ligaseIn order to showcase the effectiveness of our newly developed
- As a substrate receptor subunit of CUL2-RBX1 E3 complex, KLHDC2 features a KELCH-repeat propeller domain, which can recognize the di-glycine C-end degron of its substrates with a nanomolar affinity.
- We set out to identify compounds that can anchor to the diglycine-binding site of KLHDC2, which has recently been suggested as a promising PROTACs E3 platform for targeted protein degradation.33,34We used the OpenVS platform and VSX mode in RosettaVS to screen the Enamine-REAL library against the ta
- S11, the protocol discovers better compounds with higher predicted binding affinity after each docking iteration.
- The predicted binding affinity for the top 0.1 percentile significantly improved from -6.81 kcal/mol in the first iteration to -12.43 kcal/mol in the final iteration.
- Subsequently, we re-docked the top-ranked 50,000 small molecules from the virtual screening using VSH mode in RosettaVS, allowing for flexibility in the receptor structure during docking.
- The entire computation was completed within a week on a local HPC cluster equipped with 3000 CPUs and one RTX2080 GPU.
- Approximately 6 million compounds (0.11%) from the Enamine REAL library were subjected to docking.We took the top-ranked 1000 compounds and filtered out compounds with low predicted solubility, unsatisfied hydrogen bonds in the bound conformation, and followed by similarity clustering to reduce the 
- A total of 54 molecules that passed the filtering and clustering were manually examined for favorable interactions and geometries in PyMol35.
- Finally, 37 compounds were chosen for chemical synthesis.
- Out of these, 29 compounds were successfully synthesized (Fig.
- S13) and characterized in an AlphaLISA competition assay, in which each compound was tested for its ability to compete with a diglycine-containing SelK C-end degron peptide for binding KLHDC2.
- While several compounds showed detectable activity in displacing the degron peptide, compound 29 (C29) stood out with the best IC50 of ∼ 3 μM (Fig.
- This single digit μM IC50 was further confirmed in a competition assay using BioLayer Interferometry (Fig.
- S14).biorxiv;2024.03.28.587262v1/FIG2F2fig2Fig.
- 2Deep learning accelerated virtual screening finds novel KLHDC2 binders.a, 7 out of 29 initial synthesized and assayed compounds from the initial virtual screening.
- b, 6 out of 21 synthesized and assayed compounds from the focused screening.
- c, AlphaLISA assay and the IC50 values of the seven compounds from the initial screening.
- d, AlphaLISA assay and the IC50 values of the six compounds from the focused screening.
- f, Comparison of experimentally resolved and the computationally predicted binding pose of C29.
- The high resolution X-ray crystal structure in yellow is superimposed on predicted docked pose in magenta.To reveal the binding mode of compound 29, we soaked the crystals of apo KLHDC2 with the compound and determined structure of the KLHDC2-C29 complex at 2.0 Å resolution36.
- Consistent with its activity in displacing the diglycine peptide, compound 29 binds to the degron-binding pocket with its distal carboxyl group interacting with two critical arginine residues (Arg236 and Arg241) and a serine residue (Ser269) in KLHDC2 that are involved in recognizing the extreme C-t
- The triazole moiety next to the carboxyl group of the compound is nestled among three aromatic residues (Tyr163, Trp191, and Trp270) and stabilized by a NH…N hydrogen bond.
- The interaction of the compound with the E3 is further strengthened by a hydrogen bond formed between Lys147 and the central carbonyl group of the small molecule as well as direct packing of the tert-butylphenyl group to the auxiliary chamber of the degron-binding pocket24.
- Overall, the binding mode of compound 29 is highly similar to that of the diglycine C-end degron with a binding pose closely matching the prediction (Fig.
- 2f).biorxiv;2024.03.28.587262v1/FIG3F3fig3Fig.
- 3Crystal structure of KLHDC2-C29 complex.a, Specific residues interacting with C29 are labeled and shown as sticks and balls.
- b, 2D representation of interactions between C29 and KLHDC2.
- Residues in the pocket that form hydrogen bonds with C29 are shown as sticks and balls.Following our initial hit, we broadened our exploration to the ZINC22 library37, which houses approximately 4.1 billion small molecules in ready-to-dock 3D format.
- It’s noteworthy that a substantial fraction of ZINC22 originates from the Enamine REAL library.
- We performed substructure search of the acetyl-amino-methyl-triazole-acetic acid backbone (2D structure highlighted in red in Fig.
- 2a, b) against the ZINC22 library and identified ∼381,567 compounds.
- These compounds are docked using GALigandDock flexible docking mode and 21 compounds were picked by manually examining the top 100 structures that passed all the filters mentioned above.
- S15) and their activities were tested in the AlphaLISA-based competition assay with compound C29 as a positive control.
- Remarkable, six additional hits showed single digit μM IC50, further validating the effectiveness of our method (Fig.
- We expect that the potency of these compounds can be readily improved to reach the nanomolar range with further compound optimization.Discovery of small molecule antagonists to NaV1.7 VSD4To evaluate the wider applicability of our virtual screening protocol, we examined its effectiveness on the huma
- Specifically, we targeted voltage-sensing domain IV (VSD4) which is involved in NaV channel fast inactivation38–41 and contains a receptor site for small molecules that stabilize an inactivated state of the channel26,42,43.
- We used the same virtual screening protocol to screen the target against the ZINC22 library (∼4.1 billion compounds).
- Similar to the KLHDC2 screen, new compounds with better predicted binding affinities were discovered after each iteration, and the predicted binding affinity for the top 0.1 percentile improved from -10.8 kcal/mol in the first iteration to -18.2 kcal/mol in the final iteration.
- The top-ranked 100,000 small molecules from the virtual screening were re-docked using VSH mode in RosettaVS to account for the flexibility in the receptor structure.
- Approximately 4.5 million compounds (0.11%) from the ZINC22 library were subjected to docking.We first clustered the top 100,000 ranked small molecules, then applied filters on the top 1000 cluster representative molecules.
- A total of 160 molecules that passed the clustering and filtering were examined manually.
- Finally, ten molecules were selected for synthesis, and their Tanimoto similarities to the known inhibitors of NaV1.7 from the ChEMBL database44,45 are less than 0.33.
- S16) and their activities were measured using the whole patch clamp electrophysiology assay on hNaV1.7 channel stably expressed in HEK-293 cells as described in Methods.
- Compound Z8739902234 demonstrated the highest potency with IC50 = 1.3 μM for NaV1.7 in an inactivated state-dependent manner (Fig.
- IC50 values of better than 10 μM were observed for four compounds, translating to a hit rate of 44.4% (Fig.
- Notably, compound Z8739902234 is state dependent (Fig.
- S18, left panel) and has moderate selectivity for hNaV1.7 versus hNaV1.5 and hERG channels (Fig.
- S18, right panel).biorxiv;2024.03.28.587262v1/FIG4F4fig4Fig.
- 4Deep learning accelerated virtual screening finds novel Nav1.7 binders.a, 2D structures of the best two compounds discovered from the initial virtual screening.
- b, Concentration-response curves and inactivated-state IC50 values (in µM, mean, 95% CI) for Z8739902234 (1.32, 1.14 - 1.55) and Z8739905023 (2.23, 2.14 - 2.46).
- c, Exemplary current traces showing that Z8739902234 and Z8739905023 inhibit the inactivated state of NaV1.7.
- d, Docked structure of Z8739902234 and Z8739905023.
- Ligands are shown in dark magenta and human NaV1.7 - NavAb channel chimera VSD4 is shown in gray.
- Pocket residues that are within 4Å of the ligand are shown as lines and are labeled.

## Tables

### Table 1
> Data collection and refinement statistics (molecular replacement)


## Figure Descriptions

### Fig. 1
Deep learning guided virtual screening approach and the state-of-the-art ligand docking method.a, Overview of the deep learning guided virtual screening protocol; b, Results of the area-under-curve (AUC) of the receiver operator characteristics (ROC) curve, averaged over targets and averaged from th

### Fig. 2
Deep learning accelerated virtual screening finds novel KLHDC2 binders.a, 7 out of 29 initial synthesized and assayed compounds from the initial virtual screening. b, 6 out of 21 synthesized and assayed compounds from the focused screening. Seven compounds in total show low micromolar binding affini

### Fig. 3
Crystal structure of KLHDC2-C29 complex.a, Specific residues interacting with C29 are labeled and shown as sticks and balls. Hydrogen bonds are shown as yellow dash lines. b, 2D representation of interactions between C29 and KLHDC2. Hydrogen bonds are shown as blue dash lines. Residues in the pocket

### Fig. 4
Deep learning accelerated virtual screening finds novel Nav1.7 binders.a, 2D structures of the best two compounds discovered from the initial virtual screening. b, Concentration-response curves and inactivated-state IC50 values (in µM, mean, 95% CI) for Z8739902234 (1.32, 1.14 - 1.55) and Z873990502

### Fig. S1
Flowchart of the deep learning guided virtual screening protocol.

### Fig. S2
CASF2016 scoring power results of all the methods.

### Fig. S3
CASF2016 docking power results of all the methods. Success rate of the top 1/2/3 decoys with less than 2Å rmsd to the native structure. Docking power of RosettaGenFF-VS does not depend on the entropy model so it is reported without the specification of the entropy model. Performance of other methods

### Fig. S4
CASF2016 screening power top 1% enrichment factor results of all the methods.

### Fig. S5
CASF2016 screening power results of all the methods. The success rate of including the best binder in the top 1/5/10% ranked molecules.

### Fig S6
CASF2016 reverse screening power results of all the methods. The success rate of ranking the best protein target among the top 1/5/10% of all the targets given the ligand.

### Fig. S7
CASF2016 binding funnel analysis for all methods tested. The Spearman correlation coefficients between the RMSD ranges and the computed scores are reported. Binding funnels of RosettaGenFF-VS doesn’t depend on the entropy model, so it is reported without the specification of the entropy model. Perfo

### Fig. S8
Success rate of identifying the best-affinity ligand among top 1% ranked ligands for each protein target in the CASF2016 forward screening power test on three subsets.

### Fig. S9
The receiver operating characteristic (ROC) curves of DUD targets using VSH mode.

### Fig. S10
Examples of the docked poses of DUD from VSH (orange) vs. VSX (cyan). In both cases, VSH predicted a better docking pose and ranked the ligand among top 1% due to predicted movement in receptor sidechains. The target and ligand ID is (a) fgfr1 and ZINC03815565, and (b) parp and ZINC03832197.

### Fig. S11
Distribution of the predicted binding affinities of the top 100 ranked molecules after each iteration of KLHDC2 virtual screening

### Fig. S12
Distribution of the predicted binding affinities of the top 100 ranked molecules after each iteration of NaV1.7 virtual screening

### Fig. S13
Twenty-nine compounds from the initial virtual screening of KLHDC2 binders.

### Fig. S14
BioLayer Interferometry competition assay of compound 29. Streptavidin coated optical probes were loaded with Biotin-SelK (12 aa). The binding of the analyte GST-KLHDC2 in the presence or absence of the C29, to the loaded optical probes was measured in the association buffer. The dissociation was me

### Fig. S15
Twenty-one compounds from the focused screening of KLHDC2 binders.

### Fig. S16
Nine compounds from the virtual screening for NaV1.7 VSD4.

### Fig. S17
Whole-cell patch clamp recordings of the nine compounds from the virtual screening for NaV1.7 VSD4. The compounds bind to the inactivated state of the channel.

### Fig. S18
Left, Comparison of concentration–response relationship of Z8739902234 inhibition against NaV1.7 in inactivated state (-70 mV holding potential) and resting state (-120 mV holding potential). IC50 (in µM, mean, 95% CI) for inactivated state: 1.32, 1.14 - 1.55; resting state: 13.1, 12.78 - 13.45. Rig

### 


### 


### 


### 


## References
Total references in published paper: 73

### Key References (from published paper)
- Modeling the expansion of virtual screening libraries (, 2022)
- Ultra-large library docking for discovering new chemotypes (, 2019)
- An open-source drug discovery platform enables ultra-large virtual screens (, 2020)
- Artificial intelligence–enabled virtual screening of ultra-large chemical libraries with deep dockin (, 2022)
- Deep Docking: A Deep Learning Platform for Augmentation of Structure Based Drug Discovery (, 2020)
- Efficient Exploration of Chemical Space with Docking and Deep Learning (, 2021)
- Accelerating high-throughput virtual screening through molecular pool-based active learning (, 2021)
- Synthon-based ligand discovery in virtual libraries of over 11 billion compounds (, 2021)
- Uni-Dock: GPU-Accelerated Docking Enables Ultralarge Virtual Screening (, 2023)
- Glide: A New Approach for Rapid, Accurate Docking and Scoring. 1. Method and Assessment of Docking A (, 2004)
- Glide: A New Approach for Rapid, Accurate Docking and Scoring. 2. Enrichment Factors in Database Scr (, 2004)
- Extra Precision Glide: Docking and Scoring Incorporating a Model of Hydrophobic Enclosure for Protei (, 2006)
- Development and validation of a genetic algorithm for flexible docking (, 1997)
- AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient op (, 2010)
- A geometric deep learning approach to predict binding conformations of bioactive molecules (, 2021)
- EquiBind: Geometric Deep Learning for Drug Binding Structure Prediction (, 2022)
- DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking (, 2022)
- TANKBind: Trigonometry-Aware Neural NetworKs for Drug-Protein Binding Structure Prediction (, 2022)
- Uni-Mol: A Universal 3D Molecular Representation Learning Framework (, 2023)
- Do Deep Learning Models Really Outperform Traditional Approaches in Molecular Docking? (, 2023)
- PoseBusters: AI-based docking methods fail to generate physically valid poses or generalise to novel (, 2023)
- Force Field Optimization Guided by Small Molecule Crystal Lattice Data Enables Consistent Sub-Angstr (, 2021)
- Recognition of the Diglycine C-End Degron by CRL2KLHDC2 Ubiquitin Ligase (, 2018)
- E3 ligase autoinhibition by C-degron mimicry maintains C-degron substrate fidelity (, 2023)
- Structural basis of Nav1.7 inhibition by an isoform-selective small-molecule antagonist (, 2015)
- Comparative Assessment of Scoring Functions on an Updated Benchmark: 2. Evaluation Methods and Gener (, 2014)
- Comparative Assessment of Scoring Functions: The CASF-2016 Update (, 2018)
- Boosting Protein–Ligand Binding Pose Prediction and Virtual Screening Based on Residue–Atom Distance (, 2022)
- Uni-Mol: A Universal 3D Molecular Representation Learning Framework (, 2023)
- Benchmarking Sets for Molecular Docking (, 2006)

## Ground Truth Reference
- Figures: 26
- Tables: 1
- References: 73