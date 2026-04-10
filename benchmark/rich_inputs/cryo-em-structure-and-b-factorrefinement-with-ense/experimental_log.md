# Experimental Log: Cryo-EM structure and B-factor refinement with ensemble representation

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 1): fitting an atomic model to the map, segmenting the map into several parts, each representing a distinct entity (for example, a distinct subunit in a protein complex), or combining focused maps into a single overall composite map, with optimal weights of the focused maps.Although Gaussian Mixture
- We performed such tests using our extended benchmark of 388 protein complexes (CERES+), which is based on the recently-released CERES29 database and additional cases (see Methods).
- The results are presented in Table S1.The B-factor converges quite rapidly (Extended Data Fig.
- S1, S2), usually in 10-11 iterations or less, with minimal changes observed afterwards.
- The latter can be seen in the examples of Faba bean necrotic stunt virus (FBNSV) (EMD-10097) and the SARS-Cov-2 RNA-dependent RNA polymerase (EMD-30127) (Extended Data Fig.
- S1).The B-factor assignment is highly robust, and the recovered B-factors are near-identical, after a few iterations (Extended Data Fig.
- Overall, they deviate by ±0.87 Å2 over 366 cases in our dataset.
- S5).Ensemble generation based on B-factorsTo more accurately represent the variety of conformations that are compatible with the map, we generate a structural ensemble, based on the model we have obtained.
- We first generate models by randomly perturbing the positions of atoms, based on their B-factors, we then run a local l-BFGS30 minimisation (with openMM31), to locate close-by structures that are compatible with the data32.
- 2 for the refinement of rotavirus VP6 (EMD-6272) at 2.6 Å.
- 2c).biorxiv;2022.06.08.495259v1/FIG2F2fig2Fig.
- 2Ensemble representation illustrated on rotavirus VP6 (EMD-6272).a, Depiction of structure ensemble (orange), along with the map (transparent grey); a plot of the CCC of each individual model in the ensemble is shown (blue), as well as the ensemble map (orange); b, depiction of a single model map (g
- d, Differences in the ensemble for different residues: for residue arg 107 (left) is more widespread, and the side-chain density is more spread out, only visible at a higher contour level, on the right side, for arg 217, the ensemble is highly constrained, and the side-chain density is well defined.
- S7).Benchmarking structure refinementTo assess the quality of improvement in the model using a large dataset, we look at the changes in average SMOCf33, CCC, MolProbity34, and CaBLAM35 scores between the initial conformation and after refinement.
- We benchmarked our method against the CERES dataset29 (see Methods), which is an automated Phenix27 re-refinement of 366 complexes in their cryo-EM maps at resolution <= 5 Å.
- 3 and Extended Data Table 2.biorxiv;2022.06.08.495259v1/FIG3F3fig3Fig.
- 3Refinement of the CERES benchmark and the example of the glutamate dehydrogenase refinement.a, Benchmark comparison using CCC, between the initial (PDB-deposited) models (blue), the CERES re-refined models (green), and TEMPy-REFF refinementbased model ensemble (orange), separated by resolution band
- b, SMOCf plot calculated along the chain for the glutamate dehydrogenase deposited map and model (EMD-8194, 1.8Å, PDB ID: 5K12, blue), CERES-refined model (green) and the TEMPy-REFF model ensemble (orange): a higher score indicates a better local fit to the density for the corresponding residue.
- c, The deposited (blue), CERES-refined (green) and TEMPy-REFF ensemble (orange) models are shown in the map (grey mesh); insets of specific regions with improved quality-of-fit (around residues H195, Y76, L78) are shown.Generally, with TEMPy-REFF we obtain very large improvements in CCC scores even 
- 3a), while they become lower for the deposited and the CERES models.
- These improvements are statistically significant compared with results obtained for the deposited and the CERES models using paired-sample T-tests, the average improvements are 0.197 with a p-value of 0.0006 compared to EMDB models and 0.150 with a p-value of 0.003 compared to CERES models.
- This trend also holds true for CaBLAM scores (Extended Data Table 2).Overall local measures of fit quality (SMOC) show improvements with TEMPy-REFF models.
- In the example of glutamate dehydrogenase (PDB ID 5K12, EMD-8194), this is apparent in most regions of the modelled structure (Fig 3b).
- A visual comparison between the initial (PDB-deposited) model, CERES-refined model, and TEMPy-REFF refinement-based model ensemble is shown in Fig 3c: while all structures are well fit to the map overall, insets of residue fit show the source of improvements: a histidine (H195) that is present in th
- We demonstrate this on the 2.8 Å resolution map of glycoprotein B-neutralizing antibody Complex from Herpes Simplex Virus 1 (EMD-2124736) (Fig.
- 4b on RNA polymerase II super elongation complex (EMD-12966 to EMD-1296937).biorxiv;2022.06.08.495259v1/FIG4F4fig4Fig.
- 4Using TEMPy-REFF for map segmentation and composition.a, Segmentation of maps (glycoprotein B-Neutralizing Antibody Complex from Herpes Simplex Virus 1, EMD-2124736) into 9 submaps corresponding to single chains.
- b, Composition of 3 focused maps into a composite map, using EMD-12966 (cyan), EMD-12967 (purple), and EMD-12968 (pink).
- Top: Map-model FSC between the deposited model and the deposited composite map, EMD-1296937 (blue) and between the deposited model and TEMPy-REFF composite map (orange).
- Bottom: TEMPy-REFF composite map (orange) superposed on the deposited composite map (EMD-12969, blue).In both examples, this approach has several advantages: because the responsibility decays smoothly, there are no “seams” between segmented maps, or within composite maps, as evidenced in the FSC cur
- Additionally, areas where the assignment would be uncertain are treated as such, and the density will not be arbitrarily assigned to a specific model or submap.Case study 1: yeast RNA polymerase III elongation complexWe explore the effectiveness of the TEMPy-REFF approach in more detail by refining 
- The corresponding cryo-EM map (EMD-3178) was resolved at a global resolution of 3.9 Å38.
- A brief observation of the deposited model (which is hitherto referred to as the “deposited model”) suggests that it is well fitted to the cryo-EM map: we computed a position-optimised correlation using the ChimeraX39 fitmap utility, which gave a model-map correlation score of 0.82.
- The validation statistics presented in the PDB are reasonable; clash score of 14, Ramachandran outliers 1.1% and sidechain outliers 2.1%, with an overall MolProbity score of 2.8.
- Altogether, these observations make PDB ID 5FJ8 an interesting test case for the automated refinement using the TEMPy-REFF procedure as it allows us to measure our automated algorithm against a manually optimised model-building pipeline that produced a good quality model for a map with heterogeneous
- The ensemble models resulting from TEMPy-REFF refinement show a significant improvement in the correlation to the map, with a final CCC of 0.94.
- (the final model CCC, without the ensemble, is 0.83).
- 5.biorxiv;2022.06.08.495259v1/FIG5F5fig5Fig.
- 5Case study of RNA polymerase III elongation complex.a, The deposited model of the RNA polymerase III elongation complex (PDB ID 5FJ8, left) and the TEMPY-REFF refined model (right) coloured according to the B-factors (calculated with RELION (left) and TEMPy-REFF (right), and the 3.9 Å resolution cr
- For comparison purposes, the B-factors are normalised between 0-1.
- Insets show several regions before and after refinement (residues 192-210, 745-759) colored as in b,) and the ensemble of models (lighter orange).
- We visualise the LoQFit score at each residue in both models using 2D plots (Fig.
- The average LoQFit score for the deposited model was 10.1 Å, and model agreement was particularly high in chains A and B at the central regions of the model and map, where the average LoQFit score was 5.4 and 5.6 Å, respectively.
- However, even in these regions we observe peaks in the LoQFit score, consistent with poorer model fit, such as those seen around residues 192-210 and 745-759 in chain A (Fig.
- 5c), as reflected in the higher B-factors in this region (Fig.
- In these chains the average LoQFit score was 7.4 and 7.0Å, respectively, reflecting the lower map resolution (and correlating with high B-factors), as well as poorer model fit in the deposited model.
- Refinement with TEMPy-REFF resolved many of these poorer fitting regions: the average LoQFit score for the refined model improved to 9.0 Å, and we observed significantly better model fit at lower resolution regions of the map.
- The average LoQFit score for chain O improved to 5.9 Å in the refined model (from 7.3 Å, data not shown), and in chains M and N the average LoQFit score improved to 6.0 and 5.7 Å after refinement.Case study II: Nucleosome-CHD4 complex structureThe nucleosome is a large nucleoprotein present in the n
- We apply TEMPy-REFF to refine the model associated with map EMD-1005840 (PDB ID 6RYR) (Fig.
- The deposited cryo-EM map clearly suffers from very variable resolution (range: 3-10 Å, see Extended Data Fig.
- S8) which affected the quality-of-fit of the deposited model (Fig 6a).
- S8).biorxiv;2022.06.08.495259v1/FIG6F6fig6Fig.
- 6Case studies of Nucleosome-CHD4 complex and SARS-CoV-2 RNA polymerase (AlphaFold model refinement).a, A nucleosome structure in complex with chromatin remodelling enzyme CHD4 (EMD-10058, PDB ID: 6RYR) is shown (worm representation), with the width proportional to the B-factor, and color based on lo
- d, Zoom-in on some of the DNA basepairs (chain I/J, basepair 54) fitted in the map (mesh representation).
- e, AlphaFold2 predicted structure, with the colouring indicating the plDDT confidence measure (blue means higher confidence, red means lower confidence), fitted in the deposited map (EMD-30127, grey) f, SMOCf plot of the deposited and refined model (blue before refinement and orange after).
- 6h) contain residues which are not present in the deposited model but are present in the AlphaFold2 model and are well fitted to the map.
- g, Deposited model for the SARS-CoV-2 RNA polymerase (PDB ID 6M71, blue) fitted in the deposited map (transparent grey).
- h, TEMPy-REFF model (orange) obtained by refining the AlphaFold2 prediction in the deposited map (transparent grey).
- 6h) are shown with coloured squares.
- 6a), is also more variable (higher RMSFe) in our ensemble map (Fig.
- 6b-c).Case study III: SARS-CoV2 RNA polymerase and AlphaFold2To refine a model into an experimental cryo-EM map, an initial model is needed.
- For systems with limited structural homologs or none, an initial model may be obtained by deep-learning based ab initio tools, such as AlphaFold241 or RosettaFold42.
- Nowadays, such programs are able to create very high-quality protein models43.
- The predicted lDDT score41,44 (plDDT) is also an excellent tool to decide which part of the model can be reliably kept, and which may not be correctly predicted, due to flexibility or lack of known homologous sequences and structures.To assess the capability of our method to refine such a model, we 
- We used the polymerase sequence (UNIPROT ID: P0DTD1, residues 4393-5324) and only considered templates present in the PDB at least a year earlier than the deposition date of the deposited model (PDB ID 6M71)45.
- The predicted model was refined into the SARS-Cov-2 polymerase cryo-EM map at 2.9 Å resolution (EMD-30127) (Fig 6e-f).
- 6h) is highly similar to the deposited model (Fig.
- 6g) at most residue positions, which was calculated using Chimera46, Coot14, and Phenix27.
- However, more intriguingly, using a SMOCf plot, we show that some residues that were not present in the deposited structure45 can actually be placed into the map, with fitting scores much greater than chance (Fig.

## Tables

### Extended Data Table S1
> Change in CCC upon B-factor refinement in TEMPy-REFF.Initial values are listed for a uniform B-factor of 10, final are listed after 5 B-factor refinement steps. Atomic coordinates are not changed duri


### Extended Data Table S2
> Change in scores upon refinement, comparison against CERES


### Extended Data Table S3
> Speed benchmark.time for a run, for a given system


### Extended Data Table S4
> Forcefield comparison: change in CCC after refinement using either AMBER orCHARMM.To confirm that no significant bias is introduced by the choice of forcefield, we tested both AMBER and CHARMM36 force


## Figure Descriptions

### Fig. 1
Flow chart summarising the steps in the TEMPy-REFF algorithm.a, The EM (Expectation-Maximisation) algorithm. Responsibility is an estimation of the part of the data that is represented by a given component in the mixture. New parameters (the mean and variance of each component corresponding to the p

### Fig. 2
Ensemble representation illustrated on rotavirus VP6 (EMD-6272).a, Depiction of structure ensemble (orange), along with the map (transparent grey); a plot of the CCC of each individual model in the ensemble is shown (blue), as well as the ensemble map (orange); b, depiction of a single model map (gr

### Fig. 3
Refinement of the CERES benchmark and the example of the glutamate dehydrogenase refinement.a, Benchmark comparison using CCC, between the initial (PDB-deposited) models (blue), the CERES re-refined models (green), and TEMPy-REFF refinementbased model ensemble (orange), separated by resolution bands

### Fig. 4
Using TEMPy-REFF for map segmentation and composition.a, Segmentation of maps (glycoprotein B-Neutralizing Antibody Complex from Herpes Simplex Virus 1, EMD-2124736) into 9 submaps corresponding to single chains. b, Composition of 3 focused maps into a composite map, using EMD-12966 (cyan), EMD-1296

### Fig. 5
Case study of RNA polymerase III elongation complex.a, The deposited model of the RNA polymerase III elongation complex (PDB ID 5FJ8, left) and the TEMPY-REFF refined model (right) coloured according to the B-factors (calculated with RELION (left) and TEMPy-REFF (right), and the 3.9 Å resolution cry

### Fig. 6
Case studies of Nucleosome-CHD4 complex and SARS-CoV-2 RNA polymerase (AlphaFold model refinement).a, A nucleosome structure in complex with chromatin remodelling enzyme CHD4 (EMD-10058, PDB ID: 6RYR) is shown (worm representation), with the width proportional to the B-factor, and color based on loc

### Extended Data Fig. S1
Change in CCC and B-factor during the TEMPy-REFF refinement procedurea, CCC and B-factor changes illustrated on EMD-10097; b, and EMD-30127. The B-factor converges in around 10-12 iterations, thereby improving the CCC, i.e. the quality of fit to the data (left column). Significant changes in B-facto

### Extended Data Fig. S2
The change in B-factors during the TEMPy-REFF refinement process.Starting from an initial assignment, the B-factor converges to their final value, with an accompanying improvement in CCC.

### Extended Data Fig. S3
The convergence of B-factor values during the TEMPy-REFF refinement process, using multiple initial B-factor assignments:Unit B-factors to all atoms (all B = 1); All B = 1000; Random uniform B-factors between 1 and 1000 (B = U(1, 1000)); Random normal B-factors, with mean and variance according to t

### Extended Data Fig. S4
The values of the final B-factor after TEMPY-REFF refinement, for an initial uniform B-factor of 1 vs uniformly distributed between 1 and 1000.The B-factors are largely independent from the initial value.

### Extended Data Fig. S5
The change in Bfactor, before and after position refinement for two assemblies.a, EMD-0407; PDB ID 6NBC b, EMD-30127; PDB ID 6M71

### Extended Data Fig. S6
Ensemble generation.a, depiction of an ensemble of structures for SARS-Cov-2 RNA-dependent RNA polymerase at 2.9 Å resolution (EMD-30127, initial model PDB ID: 6M71). The CCC with respect to the map is shown on the right, with the single refinement shown in red, the ensemble in blue, and the ensembl

### Extended Data Fig. S7
Change in CCC as a function of ensemble size, for the otopetrin proton channel Otop3 at 3.22 Å (EMD-9361, initial model PDB ID: 6NF6).Bootstrap estimates at each size are computed by resampling from the full ensemble.

### Extended Data Fig. S8
Comparison of LoQFit and ResMap local resolution for the nucleosome-CHD4 complex.Both follow very similar trends, with regions of locally higher and lower resolutions in agreement between the methods. (To obtain a local resolution along the chain for ResMap, we compute the average local resolution o

### Extended Data Fig. S9
Ramachandran plotfor a, CHARMM and b, AMBER: although similar, both forcefields exhibit slightly different preferences regarding dihedral combinations; the centers are slightly offset (most visible in c,), and differently populated.

### Extended Data Fig. S10
Schematics of map composition with responsibilities.We use two Gaussians to illustrate the map composition process (blue and yellow). Each Gaussian is an idealised representation of a focused map. Three protocols for combining those maps into a single composed map are shown, with the resulting map i

## References
Total references in published paper: 56

### Key References (from published paper)
- Bijvoet Center for Biomolecular Research, Faculty of Science-Chemistry, Utrecht University, Utrecht, (, 2015)
- Current approaches for the fitting and refinement of atomic models into cryo-EM maps using CCP-EM (, 2018)
- Consensus among flexible fitting approaches improves the interpretation of cryo-EM data (, 2012)
- Molecular dynamics-based refinement and validation for sub-5 Å cryoelectron microscopy maps (, 2016)
- Low-resolution structure refinement in electron microscopy (, 2003)
- Protein structure fitting and refinement guided by cryo-EM density (, 2008)
- Multiple subunit fitting into a low-resolution density map of a macromolecular complex using a gauss (, 2008)
- Gaussian-input Gaussian mixture model for representing density maps and atomic models (, 2018)
- Automated cryo-EM structure refinement using correlation-driven molecular dynamics (, 2019)
- Real-space refinement in PHENIX for cryo-EM and crystallography (, 2018)
- iMODFIT: efficient and robust flexible fitting based on vibrational analysis in internal coordinates (, 2013)
- Normal mode based flexible fitting of high-resolution structure into low-resolution experimental dat (, 2004)
- Automated structure refinement of macromolecular assemblies from cryo-EM maps using Rosetta (, 2016)
- Features and development of Coot (, 2010)
- ISOLDE: a physically realistic environment for model building into low-resolution electron-density m (, 2018)
- Optimization of the additive CHARMM all-atom protein force field targeting improved sampling of the  (, 2012)
- ff14SB: Improving the Accuracy of Protein Side Chain and Backbone Parameters from ff99SB (, 2015)
- Deriving and refining atomic models in crystallography and cryo-EM: the latest Phenix tools to facil (, 2019)
- Characterisation of molecular motions in cryo-EM single-particle data by multi-body refinement in RE (, 2018)
- Deep learning enables the atomic structure determination of the Fanconi Anemia core complex from cry (, 2020)
- Conformational Changes during Pore Formation by the Perforin-Related Protein Pleurotolysin (, 2015)
- TEMPy: a Python library for assessment of three-dimensional electron microscopy density fits (, 2015)
- High-resolution electron microscopy of helical specimens: a fresh look at tobacco mosaic virus (, 2007)
- Assessing the quality of single particle reconstructions by atomic model building (, 2018)
- A Multi-model Approach to Assessing Local and Global Cryo-EM Map Quality (, 2019)
- Molecular Dynamics to Predict Cryo-EM: Capturing Transitions and Short-Lived Conformational States o (, 2021)
- Macromolecular structure determination using X-rays, neutrons and electrons: recent developments in  (, 2019)
- Bayesian Weighing of Electron Cryo-Microscopy Data for Integrative Structural Modeling (, 2019)
- CERES: a cryo-EM re-refinement system for continuous improvement of deposited models (, 2021)
- On the limited memory BFGS method for large scale optimization (, 1989)

## Ground Truth Reference
- Figures: 16
- Tables: 4
- References: 56