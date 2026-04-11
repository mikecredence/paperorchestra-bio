# Experimental Log: Uncovering Protein Ensembles: Automated Multiconformer Model Building for X-ray Crystallography and Cryo-EM

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsOverview of qFit protein algorithmqFit protein is a tool that automatically identifies alternative conformations based on a high-resolution density map (generally better than ∼2 Å) and a well-refined single-conformer structure (generally Rfree below 20%).
- For X-ray maps, we recommend using a composite omit map as input to minimize model bias24.
- All code and associated documentation can be found in the qFit GitHub repository (https://github.com/ExcitedStates/qfit-3.0).
- The version of qFit associated with this paper is 2024.2 and is available at SBGrid (https://sbgrid.org/)25.A - qFit residueFor each residue, qFit samples backbone conformations, side-chain dihedral angles, and B-factors(Figure 1A).
- The sampling and scoring of residues can be run in parallel using Python multiprocessing.biorxiv;2023.06.28.546963v4/FIG1F1fig1Figure 1.Programmatic flow of qFit protein algorithm.A.
- qFit residue algorithm, demonstrated by Tyr118 in the E46Q mutant structure of the photoactive yellow protein from Halorhodospira halophila (PDB: 1OTA)29.
- The 2mFo-DFc composite omit density map contoured at 1 σ is shown as a blue mesh.A.1.
- Backbone sampling: For each residue, qFit performs a collective translation of backbone atom (N, C, Cα, O) coordinates.A.2.
- Aromatic angle sampling: For aromatic residues (His, Tyr, Phe, Trp), qFit takes the conformations from the backbone step and samples the Cα-Cβ-Cγ angle.A.3.
- Dihedral angle sampling: Since Tyr has two χ angles, qFit starts by taking the output conformers from the aromatic angle sampling step and exhaustively samples the χ1 angle, scoring the best conformations based on QP/B-factor/MIQP scoring.
- Since the only angle left to be sampled is the χ2 angle, qFit rotates about the terminal ring of the Tyr and then scores the conformations that best fit the density.A.4.
- qFit segment algorithm, demonstrated by Tyr118 in PDB: 1OTA.
- After identifying all optimal conformations for each individual residue, qFit works to connect the protein back together.B.1 qFit segment: Moving linearly along the protein sequence, qFit identifies ‘segments’ of residues with multiple backbone conformations.
- Here, Ser117 (i) and Tyr118 (i+1) have multiple backbone conformations.
- The optimal combination of conformations is then determined by the QP/MIQP scoring, leading to one combination being culled.B.2 qFit relabel: qFit uses Monte Carlo optimization with a steric model to assign altloc labels to spatially coupled alternative conformers.
- In this example, Ser117 and the neighboring Gln32 initially have clashing altloc B conformers.
- However, relabeling swaps the A and B labels of Gln32 to relieve this clash.B.3 qFit refinement: We then refine the occupancies, coordinates, and B-factors of the raw qFit output file to produce a final qFit model.A.1 - Backbone samplingThe qFit process begins with sampling backbone conformations (F
- Each translation takes place in steps of 0.1 Å along each coordinate axis, extending to 0.3 Å, resulting in 9 (if isotropic) or 81 (if anisotropic) distinct backbone conformations for further analysis.
- For Gly and Ala, this is the only sampling that occurs.A.2 - Aromatic angle samplingFor aromatic residues (His, Tyr, Phe, Trp), qFit takes the conformations from the backbone step (above) and builds part of the side chain out to Cγ (start of the aromatic ring) based on the input model coordinates (F
- Then, we alter the Cα-Cβ-Cγ angle (“the aromatic angle”) in steps of +/- 3.75°, extending to +/- 7.5°, creating 5 partial side-chain conformations per backbone conformation.
- These conformers provide variability in the placement of the aromatic ring prior to dihedral angle sampling.biorxiv;2023.06.28.546963v4/FIG2F2fig2Figure 2.Multiconformer models created by qFit are better models than deposited single-conformer models.A.
- The qFit Rfree values improve in 73% of structures.B.
- qFit identifies new alternative conformations adjacent to the RNA binding motif in the Pyrococcus horikoshii fibrillarin pre-rRNA processing protein (PDB: 1G8A).
- qFit identified new rotamers for Leu58 (tp) and Met175 (ttp and mtp)36 and significantly different alternative conformations within the original rotameric well for Phe69.C.
- qFit adds at least one additional alternative conformation in 31.7% of residues (n=9,998).D.
- (Left) All residues (n=42,626).
- (Right) Only residues with alternative conformations in the deposited model (n=970).
- See main text for definitions of categories.A.3 - Dihedral angle samplingThe following steps occur for each χ dihedral angle for every residue (Figure 1A.3).
- For the first dihedral angle (χ1), the input is the sampled backbone conformations (or for aromatic residues the backbone and “aromatic angle” conformers described above).
- We sample around the χ1 dihedral angle by enumerating a conformation every 6° for for 24° on each side of an idealized rotamer angle.
- For proline, we sample the exo and endo conformations of the pyrrolidine ring, by +/- 24° in steps of 6°.
- We then eliminate conformations that clash (with other parts of the same sampled conformation of heavy atoms (based on hard spheres) or are redundant (using an all-atom RMSD threshold of 0.01 Å).biorxiv;2023.06.28.546963v4/FIG3F3fig3Figure 3.qFit improves some geometry metrics compared to deposited 
- Model MolProbity score (deposited model: 1.27 (median) [0.94-0.16] (interquartile range), qFit model: 1.09 (median) [0.90-1.30] (interquartile range)), p-value=0.006 from two-sided t-test.B.
- Model averaged RMSD (Å) of idealized versus model bond lengths (deposited model: 0.010 [0.0070-0.015], qFit model: 0.0073 [0.005-0.011]), p-value=0.002 from two-sided t-test.C.
- Model averaged RMSD (Å) of idealized versus model bond angles (deposited model: 1.30 [1.14-1.57], qFit model: 0.91 [0.77-1.13]), p-value=3.79e-16 from two-sided t-test.D.
- Model clashscore (deposited model: 2.50 [1.30-5.92], qFit model: 1.80 [1.31-3.73]), p-value=0.0028 from two-sided t-test.E.
- Meshes represent 2Fo-Fc density at 1 σ.
- Met189 from deposited structure (PDB: 1VF8; left, green) has a Sδ-Cε bond length of 1.596 Å (7.8 σ from idealized length of 1.791 Å)38.
- qFit models two alternative conformations, filling in unmodeled density, and fixing the Sδ-Cε bond length (1.790 Å for alternative conformation A and 1.794 Å for alternative conformation B).F.
- Example of qFit (right, blue and magenta) fixing a clash between Met83 and Leu81 from deposited structure (PDB: 6HEQ).
- Meshes represent density at 1 σ.
- In the deposited model (left, green), Met83 is not correctly fitted into density and is clashing with Leu81 (closest contact: 3.0 Å).
- qFit corrects this by improving the fit of Met83, leading to the closest contact being 3.8 Å.These sampled conformations are then subjected to a quadratic programming (QP) optimization26, which identifies the set of conformations whose weighted calculated density best fits the experimental electron 
- The output of QP typically yields 5 to 15 conformations that best explain the density.Next, qFit samples the B-factors of the conformers.
- The input atomic B-factors are multiplied by a factor ranging from 0.5 to 1.5 in increments of 0.2.
- The resulting 50 to 150 conformation/B-factor combinations are subjected to a mixed-integer quadratic programming (MIQP) optimization.
- The MIQP algorithm incorporates two additional constraints relative to QP: a cardinality term, which limits the maximum number of conformations to five, and a threshold term, which stipulates that no individual conformation can have an occupancy weight below 0.2.
- In qFit, MIQP then outputs up to 5 conformations.For residues with subsequent dihedral angles, the conformations selected by the MIQP procedure at the χ(n-1) angle serve as the starting conformers for sampling the χ(n) angle.
- For residues with only one dihedral angle (Ser, Cys, Thr, Val, Pro), we proceed directly to scoring χ1.A.4 - Final qFit residue ScoringUpon reaching the terminal dihedral angle, we perform the optimization steps outlined above (QP/MIQP), but instead of relying only on the optimization algorithm to d
- qFit runs the MIQP step 5 times with a cardinality term ranging from 1 to 5.
- The number of parameters (k) is defined by the following: number of conformers * number of atoms * 4 (representing the x, y, z coordinates and B-factor).
- A heuristic scaling factor of 0.95 accounts for the fact that the coordinate parameters are not independent due to chemical constraints between atoms during sampling.
- biorxiv;2023.06.28.546963v4/FIG4F4fig4Figure 4:qFit performs best at high resolution of input datasetA.
- Meshes represent density at 1 σ.
- Multiconformer match - Residue is multiconformer in qFit model with RMSD < 0.5 Å from ground truth residue.
- qFit models two distinct alternate conformations which recapitulate the ground truth residue’s alternate conformations.Multiconformer no match - Residue is multiconformer in qFit model with RMSD > 0.5 Å from ground truth residue.
- The example on the right is a single-conformation residue in ground truth but qFit models three alternate conformations.Single conformer match - Residue is single-conformer in qFit model with RMSD < 0.5 Å from ground truth residue.
- Both ground truth model and qFit model have one distinct conformation and they align well.Single conformer no match - Residue is single-conformer in qFit model with RMSD > 0.5 Å from ground truth residue.
- Proportion of all residues in the qFit models of 7KR0 that are modeled as multiconformer match (orange), single conformer match (blue), multiconformer no match(green), and single conformer no match(red) as a function of resolution of input synthetic data from the 7KR0 dataset.
- The shaded region denotes the 95% confidence interval.C.
- Glu114 in the 7KR0 dataset modeled by qFit (cyan and magenta) compared to the ground truth structure (green and yellow) at different synthetic resolutions.
- Meshes represent density at 1 σ.D.
- The fraction of residues in the qFit models of the qFit test dataset with a Q-score within 0.01 to that of the ground truth model as a function of resolution.
- Occupancies of conformers were binned into three classes – occupancy equal to 1 (blue), 1 > occupancy >= 0.5 (orange) and occupancy < 0.5 (green).qFit then outputs the set of conformations with the lowest BIC value, concluding the qFit residue routine.B.
- Second, we label the alternative conformers while being aware of clashes.B.1 - qFit segmentAfter identifying the optimal conformations for each residue in parallel, qFit reconnects the backbone atoms (Figure 1B.1).
- qFit then moves along the protein, enumerating and selecting optimal combinations of fragment conformations until reaching the end of the segment.B.2 - qFit relabelNext, qFit determines the correct altloc labeling (A, B, C, D, E) of coupled alternative conformers using Monte Carlo optimization with 
- This procedure can be especially helpful after manually adding or deleting conformations in Coot12.
- This labeling step is not parallelized.B.3 - qFit refinementThe raw output of qFit (a multiconfomer model) should then be refined.
- We provide scripts for a refinement procedure with Phenix27, where we iteratively refine the occupancy, coordinates, and B-factors, removing conformations with occupancies under 10%.
- Once the model is stable (has no conformations with occupancies less than 10%), we perform a final round of refinement which optimizes the placements of ordered water molecules (Methods).
- We then apply a mosaic bulk solvent (phenix.mosaic) to the final model, which allows for partial bulk solvent occupancy28.
- This model can then be examined and edited in Coot12 or other visualization software, and further refined using software such as phenix.refine, Refmac, or Buster as the modeler sees fit.qFit improves overall fit to data relative to deposited structuresTo evaluate the impact of qFit algorithmic and c
- We clustered these structures at a sequence identity threshold of 30% and selected the highest-resolution structure per cluster.
- Finally, we ensured that the datasets ran without error through the qFit pipeline, including refinement with Phenix, resulting in 144 diverse structures (Supplementary Figure 1).Each deposited structure was initially re-refined using phenix.refine (Methods) to eliminate differences from the original
- The qFit model has a lower (improved) Rfree value for 76% (109/144) of structures (Figure 2A; Supplementary Figure 2A; Supplementary Table 1).
- On average, there is an absolute decrease of Rfree value by 0.6% (median deposited models Rfree: 18.1%, median qFit models Rfree: 17.5%), which is in line with theoretical expectations for the increase in model complexity created by qFit31,32.
- qFit models have similar R-gap values compared to deposited models (mean: 3.0% for both models).
- Collectively, these results indicate that qFit improves the quality of most models without overfitting (Supplementary Figure 2B).Despite this general trend of improved models, 24% of the qFit models have worse Rfree than the deposited models (n=35).
- The majority of these structures had a deposited model Rfree of over 20%.
- These high Rfree values are notable because our re-refinement procedure generally improved Rfree relative to the originally deposited model, particularly for structures with higher starting Rfree (Supplementary Figure 2C).
- It further suggests that qFit is best employed at a late stage of modeling, after the single-structure model is of sufficient quality that it would be deposited in the PDB.As an example of how qFit can uncover previously unnoticed conformational heterogeneity, we examined differences in conformation
- Among these residues, qFit identified well-justified alternative conformations for residues Leu58, Phe69, and Met175, including new rotamers for Leu58 and Met175, that were not present in the deposited model (Figure 2B).
- For example, when Leu58 is in the ‘up’ position (altloc A), Phe69 is also in the ‘up’ position (altloc A).
- Only 2.9% of residues in the deposited models were multiconformers (two or more alternative conformations, n=970).
- In contrast, 40.7% (n=11,049) of residues in the qFit models were multiconformers (Figure 2C).
- The vast majority (92.5%) of multiconformer residues in the qFit models have only two alternative conformations; only 2.4% of residues have more than two alternative conformations.Alternative conformations come in a few varieties.
- This behavior is exemplified by the Tyr residue in Figure 1A.
- Third is even more subtle changes in coordinates to avoid strain because of the alternative conformations of neighboring residues34.
- This category is essentially imperceptible to visual inspection, as the atom centers are nearly superimposable, but is important to avoid outlier bond geometry because of adjacent residues having larger displacements.To quantify how often qFit models new rotameric states, we analyzed the qFit models
- We classified the agreement between the deposited and qFit models into 5 categories (Figure 2D, Supplementary Figure 3).
- Overall this category, “Consistent”, represents 93.7% of residues (n=42,626) in the dataset.The second and third categories deal with imbalance in alternative conformations that populate distinct rotamers.
- This category, Additional Rotamer(s) in qFit model, represents 2.38% of residues (n=1,082).
- In contrast, only two residues (0.06% of the dataset) are classified in the converse category, Additional Rotamer(s) in deposited model.The final two categories cover disagreements in rotamer assignments.
- This category, Consistent & Different Rotamers, represents 0.82% of residues (n=373).
- Different rotamer assignments represent 3.04% of residues (n=1,384).
- While the analyses above include all residues, focusing on residues that were modeled in as multiconformers in the deposited models (n=970) reveals a large increase in the Different and Consistent & Different Rotamers categories, to 14.88% (n=144) and 27.68% (n=268) of residues, respectively.
- On the other hand, placing additional alternative conformers may alleviate strain in the model that can result from fitting a single conformer into density that should be supported by multiple conformers11,19,37.To validate geometry, we used MolProbity to evaluate the deposited and qFit models.
- MolProbity compares input models with idealized values and then provides component scores for various geometric and steric features that are summarized in an overall “MolProbity score”38.
- In the future, we aim to explore updated metrics that consider all alternative conformations.Compared to deposited models, qFit models had improved MolProbity scores (1.27 median deposited versus 1.09 median qFit, p=0.006 from two-sided t-test; Figure 3A), which indicated that overall qFit improves 
- This included considerable improvements in bond lengths and angles in the qFit models (RMSD between idealized values for bond lengths: 0.010 Å median deposited vs.
- 0.007 Å median qFit, p=0.021 from two-sided t-test; RMSD between idealized values for bond angles: 1.30° median deposited vs.
- 0.91° median qFit, p=3.79e-16 from two-sided t-test; Figure 3B,C).
- To visualize an example of these differences, we investigated Met189 from PDB: 1V8F.
- In the deposited model this residue has Sδ-Cε bond lengths of 1.596 Å, which are significantly shorter than the idealized lengths of 1.791 +/- 0.025 Å38.
- qFit adds an additional conformation, both explaining previously unmodeled density and bringing the Sδ-Cε bond lengths much closer to the expected values: 1.790 Å (alternative conformer A) and 1.794 Å (alternative conformer B) for the two conformations (Figure 3E).
- This multiconformer residue with improved geometry is consistent with the hypothesis that qFit is alleviating strained geometry by modeling multiple conformations.Additionally, qFit models have improved clashscores (2.50 median deposited, 1.80 median qFit, p=0.0028 from two-sided t-test; Figure 3D).
- We looked at the qFit modeling differences in a cluster of Met and Leu residues in PDB: 6HEQ, which had one of the largest changes in clashscores between the deposited and qFit models.
- We observed that qFit fixes the positioning of Met83, preventing the clash with both conformers of Leu81 and improving the local fit to density (Figure 3F).We observed almost equivalent rotamer scores, favored Ramachandran values, and C-beta values (median number of rotamer outliers: 0.94 deposited 
- 0.800 qFit; percentage of Ramachandran favored: 97.7% deposited vs.
- 97.8% qFit; median value of clashscore: 2.50 deposited vs.
- 1.78 qFit) (Supplementary Figure 4).
- To address this question, we generated artificial structure factors using an ultra-high-resolution structure (0.77 Å) of the SARS-CoV-2 Nsp3 macrodomain (PDB: 7KR0)39.
- This model had a high proportion of residues (47%) manually modeled as alternative conformations and did not employ qFit during model building or refinement, making it an ideal comparison structure.
- We refer to this structure as the “ground truth 7KR0 model”, and evaluated how well its alternative conformations were recapitulated by qFit as resolution was artificially worsened across synthetic datasets.
- To create the dataset for resolution dependence, we used the ground truth 7KR0 model, including all alternative conformations, and generated artificial structure factors with a high resolution limit ranging from 0.8 to 3.0 Å (in increments of 0.1 Å).
- We then added random noise to the structure factors that increased as resolution worsened (Methods; Supplementary Figure 5A and 5B).
- Finally, we used the refined single-conformer model as input for qFit.We then turned to evaluate the fidelity of qFit in recapitulating the ground truth 7KR0 model.
- Due to many residues in both the ground truth and qFit models having alternative conformations that nearly overlap each other, we categorize residues as multiconformer only if they possess at least two alternative conformers with a side-chain heavy-atom root-mean-square deviation (RMSD) greater than
- From this cutoff, 50 out of the 169 residues (30%) in the ground truth model are classified as multiconformers.Next, we define each residue as having an agreement between the outputted qFit model and the ground truth 7KR0 model.
- If all qFit modeled conformers are within 0.5 Å of the deposited 7KR0 model, we classify it as a match.
- We did observe a drop off of detecting alternative conformations (multiconformer match) beyond resolutions of ∼1.8-2.0 Å (Figure 4B; Supplementary Figure 5C).
- This behavior is exemplified by Glu114, which is multiconformer in the ground truth model (Figure 4C).
- At high resolution (1.0 Å), qFit correctly models the alternative conformation and this residue is categorized as a multiconformer match.
- At 1.8 Å resolution, qFit still models two alternative conformations and has a good fit to density; however, the secondary conformer has an RMSD greater than 0.5 Å away from the ground truth model; consequently this residue is now categorized as a multiconformer no match.
- Finally, at 2.8 Å resolution, qFit only models a single conformer, moving the residue to the single conformer no match category.Simulated multiconformer data illustrate the convergence of qFitNext, we tested the ability of qFit to detect alternative conformations over a larger, more diverse dataset.
- We generated artificial structure factors for the qFit models with improved Rfree values over the deposited values from the previous sections (n=109).
- Although this dataset is more diverse, it has a notable weakness relative to the 7KR0 dataset test: the 7KR0 alternative conformations were modeled manually, whereas the larger dataset has alternative conformations modeled by qFit.
- Therefore, this second synthetic dataset assesses convergence of the qFit models across resolution.Using these qFit models as ground truth models, we generated structure factors, performed refinement of single-conformer models, and ran qFit over the resolution range of 1.0 to 3.0 Å (Supplementary Fi
- We observed a similar fall-off of multiconformer match residues around 2.0 Å (Supplementary Figure 5D).
- We also observe a trend of increased no match multiconformers/single conformers for longer residues that are just outside the 0.5 Å RMSD cutoff (Supplementary Figure 6).
- We did not observe a relationship between input model Rfree and the number of correctly modeled conformers, but it is difficult to tell whether our synthetic noise procedures properly capture the dependence of qFit performance on input model/data agreement (Supplementary Figure 7A/B).We then assesse
- To do this, we used the Q-score40, which compares the map profile of an atom with an ideal Gaussian distribution that would be observed if the atom perfectly fits into the density.
- Across the test dataset, residues that qFit models as single conformers have an almost equivalent Q-score to the ground truth model even at lower resolutions (Figure 4D).
- The primary alternative conformations in qFit models (occupancy between 0.5 and 1.0) and lower-occupancy alternative conformations (occupancy <0.5) display Q-scores that are very close to the equivalent “ground truth model” alternative conformations until a resolution of about 1.8 Å.
- These trends were also observed with the 7KR0 dataset (Supplementary Figure 7C).
- Overall, these analyses on both the 7KR0 and larger synthetic datasets confirm that qFit will best detect alternative conformations with high-resolution (1.8-2.0 Å or better) data.qFit models alternative conformers in cryo-EM density mapsAs single-particle cryo-EM is increasingly producing high-reso
- While a previous version of qFit introduced cryo-EM compatibility21, we had not optimized the approach to work with cryo-EM maps and models.
- qFit can now be run in ‘EM mode’ which uses electron structure factors, improves the treatment of solvent background levels, and reduces the default maximum number of alternative conformations (cardinality) (Methods).To benchmark our ability to model alternative conformations in high-resolution cryo
- However, only 8 of these structures have a resolution better than 2 Å (FSC at 0.143) when calculated by the Electron Microscopy Data Bank (EMDB)43.
- Some of the original 22 structures did not have FSC curves in EMDB (n=6) due a lack of data, and others had an EMDB calculated resolution worse than 2 Å (n=8) (Supplementary Table 2).
- The absence of standardized maps for determining cryo-EM structure resolution complicated our selection of structures for qFit analysis.We downloaded the eight models with resolution better than 2 Å from the PDB and their corresponding maps from EMDB.
- qFit was run with the ‘EM’ flag and the output model was refined using the qFit real space refinement script (Methods).Across the first asymmetric unit of the 8 models, 8.21% (n=64) of residues in the deposited model had at least two alternative conformers in the deposited structure, compared with 3
- To determine if qFit could recapitulate the modeling of alternative conformers from deposited structures, we compared the high-resolution apoferritin deposited model (PDB: 7A4M, resolution: 1.22 Å) with the qFit model using the same criteria outlined in the resolution dependence section above (RMSD 
- qFit correctly models 77% of residues in the first asymmetric unit.
- This includes Arg22, which has two alternative conformations in the deposited model.
- qFit was able to recapitulate both alternative conformations (Figure 5A), highlighting that qFit can detect manually modeled alternative conformations in cryo-EM maps.
- In addition, qFit detected several unmodeled alternative conformers that were visually confirmed (Figure 5B-D).biorxiv;2023.06.28.546963v4/FIG5F5fig5Figure 5.qFit identifies alternative conformations in high-resolution cryo-EM models.Meshes represent density at 1 σ, with blue volumes representing de
- qFit recapitulated the deposited alternative conformations of Arg22 (chain A) in apoferritin (PDB: 7A4M, resolution: 1.22 Å).B.
- qFit identified a previously unmodeled alternative conformation of Glu14 (chain A) in apoferritin (PDB: 7A4M, resolution: 1.22 Å).C.
- qFit identified a previously unmodeled alternative conformation of Lys49 (chain A) in a different structure of apoferritin (PDB: 6Z9E, resolution: 1.55 Å).
- qFit identified a previously unmodeled alternative conformation of Gln403 (chain A) in adeno-associated virus (PDB: 7KFR, resolution: 1.56 Å).As with the X-ray models, we wanted to determine how qFit changes the model geometry.
- Unlike the observations in the X-ray dataset, qFit does increase (worsen) the MolProbity score, likely coming from high clashscore of most structures, highlighting a future improvement in the algorithm(Supplementary Figure 8).While we have made significant progress in modeling alternative conformati
- Even among this select group of structures, there were varying levels of experimental and computational map details on EMDB and in manuscripts41,42,44, including information on masking, handling of bulk solvent, and local resolution.
- While there is an accepted formula for calculating resolution (FSC at 0.143), the maps to calculate these are not consistent leading to differences in resolution as we observed between the deposited versus EMDB calculated resolutions.
- New methods for cryo-EM ensemble modeling will benefit from ongoing efforts to standardize the storage of raw, meta, and processed data45.

## Figure Descriptions

### Figure 1.
Programmatic flow of qFit protein algorithm.A. qFit residue algorithm, demonstrated by Tyr118 in the E46Q mutant structure of the photoactive yellow protein from Halorhodospira halophila (PDB: 1OTA)29. The 2mFo-DFc composite omit density map contoured at 1 σ is shown as a blue mesh.A.1. Backbone sam

### Figure 2.
Multiconformer models created by qFit are better models than deposited single-conformer models.A. The distribution of Rfree value in deposited models versus qFit models. The qFit Rfree values improve in 73% of structures.B. qFit identifies new alternative conformations adjacent to the RNA binding mo

### Figure 3.
qFit improves some geometry metrics compared to deposited structures.A. Model MolProbity score (deposited model: 1.27 (median) [0.94-0.16] (interquartile range), qFit model: 1.09 (median) [0.90-1.30] (interquartile range)), p-value=0.006 from two-sided t-test.B. Model averaged RMSD (Å) of idealized 

### Figure 4:
qFit performs best at high resolution of input datasetA. Ground truth model residues are shown as green and yellow sticks; qFit model residues are shown as magenta, cyan, and gray. Meshes represent density at 1 σ.
Multiconformer match - Residue is multiconformer in qFit model with RMSD < 0.5 Å from 

### Figure 5.
qFit identifies alternative conformations in high-resolution cryo-EM models.Meshes represent density at 1 σ, with blue volumes representing density at 0.5 σ. Green and yellow sticks represent deposited conformation(s). Cyan and magenta sticks represent qFit conformations. Occupancy is labeled based 

### Supplementary Figure 1.
Flow diagram of the selection of the test set PDBs.

### Supplementary Figure 2.
Rfree and R-gap distributions.A. Distribution of difference of Rfree between deposited and qFit models. The median difference in Rfree is 0.6%. Median deposited models Rfree: 18.1%, median qFit models Rfree: 17.5%.B. Distribution of R-gap values between deposited and qFit models (median deposited mo

### Supplementary Figure 3.
Examples of rotamer state categories.Meshes represent 2Fo-Fc density at 1 σ. Green and yellow sticks represent deposited conformer(s). Blue and magenta sticks represent qFit conformer(s).A. Same: The entire set of rotamers identified in the deposited and qFit models are the same (PDB: 1BN6, His199).

### Supplementary Figure 4.
Deposited versus qFit model geometry.A. Count of number of Cβ deviation (>0.25Å) per model (deposited model: 0.0 median [interquartile range: 0.0-0.0], qFit model: 0.0 median [interquartile range: 0.0-0.0]), p-value=0.37 from two-sided t-test.B. Median count of number of rotamer outliers per model (

### Supplementary Figure 5.
A. Protocol for generating synthetic structure factors at various resolutions starting from the ground truth model. For the 7KR0 dataset, all the steps starting from random shaking of coordinates were done 10 times for each resolution. For the larger test dataset, all steps were only done once.B. A 

### Supplementary Figure 6.
A. The distribution of RMSD between qFit residues and corresponding ground truth residues (qFit test set) whenever the RMSD is higher than the 0.5 Å cutoff, resulting in the qFit residues being classified as multiconformer no match.B. The propensity of each residue type to be modeled with high RMSD 

### Supplementary Figure 7.
A. Rwork (blue) and Rfree (orange) distribution of the input model from the qFit test dataset. These correspond to the models obtained after refining against Fnoisy structure factors (see Supplementary Figure 5A). The shaded region around the lines indicates the spread (standard deviation) across th

### Supplementary Figure 8.
A. MolProbity score(deposited model: 1.49 (median) [1.40-1.61] (interquartile range), qFit model: 1.59 (median) [1.39-1.92] (interquartile range))B. Model average of RMSD of model bond length from idealized bond length(Å)(deposited model: 0.00 [0.00-0.01], qFit model: 0.00 [0.00-0.00])C. Model avera

## References
Total references in published paper: 76

### Key References (from published paper)
- Single-Particle Cryo-EM at Crystallographic Resolution (, 2015)
- Structural heterogeneity in protein crystals (, 1986)
- Achieving better-than-3-Å resolution by single-particle cryo-EM at 200 keV (, 2017)
- An expanded allosteric network in PTP1B by multitemperature crystallography, fragment screening, and (, 2018)
- Ligand binding remodels protein side-chain conformational heterogeneity (, 2022)
- Ensemble-function relationships to dissect mechanisms of enzyme catalysis (, 2022)
- Is one solution good enough? (, 2006)
- What Will Computational Modeling Approaches Have to Say in the Era of Atomistic Cryo-EM Data? (, 2020)
- E pluribus unum, no more: from one crystal, many conformations (, 2014)
- Modelling dynamics in protein crystal structures by ensemble refinement (, 2012)
- Vagabond: bond-based parametrization reduces overfitting for refinement of proteins (, 2021)
- Features and development of Coot (, 2010)
- Improving sampling of crystallographic disorder in ensemble refinement (, 2021)
- Thermal Motion and Conformational Disorder in Protein Crystal Structures: Comparison of Multi-Confor (, 1994)
- The solvent component of macromolecular crystals (, 2015)
- XDS (, 2010)
- Linking crystallographic model and data quality (, 2012)
- How Good Can Single-Particle Cryo-EM Become? What Remains Before It Approaches Its Physical Limits? (, 2019)
- FLEXR: automated multi-conformer model building using electron-density map sampling (, 2023)
- Exposing Hidden Alternative Backbone Conformations in X-ray Crystallography Using qFit (, 2015)
- qFit 3: Protein and ligand multiconformer modeling for X-ray crystallographic and single-particle cr (, 2021)
- Modeling discrete heterogeneity in X-ray diffraction data by fitting multi-conformers (, 2009)
- qFit-ligand Reveals Widespread Conformational Heterogeneity of Drug-Like Molecules in X-Ray Electron (, 2018)
- Iterative-build OMIT maps: map improvement by iterative model building and refinement without model  (, 2008)
- Collaboration gets the most out of software (, 2013)
- A rewriting system for convex optimization problems (, 2018)
- Towards automated crystallographic structure refinement with phenix.refine (, 2012)
- Accounting for nonuniformity of bulk-solvent: A mosaic model (, 2024)
- Short hydrogen bonds in photoactive yellow protein (, 2004)
- The Protein Data Bank (, 2000)

## Ground Truth Reference
- Figures: 13
- Tables: 0
- References: 76