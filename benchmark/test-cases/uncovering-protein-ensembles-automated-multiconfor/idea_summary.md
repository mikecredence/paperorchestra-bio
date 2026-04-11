# Idea Summary: Uncovering Protein Ensembles: Automated Multiconformer Model Building for X-ray Crystallography and Cryo-EM

## Working title
Uncovering Protein Ensembles: Automated Multiconformer Model Building for X-ray Crystallography and Cryo-EM

## Core question
AbstractIn their folded state, biomolecules exchange between multiple conformational states that are crucial for their function. Traditional structural biology methods, such as X-ray crystallography and cryogenic electron microscopy (cryo-EM), produce density maps that are ensemble averages, reflecting molecules in various conformations. Yet, most models derived from these maps explicitly represent only a single conformation, overlooking the complexity of biomolecular structures. To accurately r

## Motivation / gap
- IntroductionMacromolecular X-ray crystallography and single-particle electron microscopy (cryo-EM) can provide valuable information on macromolecular conformational ensembles.
- These experiments cannot capture all conformations present in solution, as many would disrupt the ability to obtain crystals or align classifiable particles1.
- However, careful modeling from high-resolution X-ray crystallography and cryo-EM data can reveal widespread conformational heterogeneity, particularly for protein side chains and local backbone region
- Such discrete, local conformational heterogeneity is significant for many biological functions, including macromolecular binding, catalysis, and allostery4–6.While the underlying data from X-ray diffr
- Most depositions in the Protein Data Bank reflect only an averaged, single ground state set of atomic coordinates7, ignoring weak but potentially biologically rich signals encoding alternative conform

## Core contribution (bullet form)
Extracted from abstract:
AbstractIn their folded state, biomolecules exchange between multiple conformational states that are crucial for their function. Traditional structural biology methods, such as X-ray crystallography and cryogenic electron microscopy (cryo-EM), produce density maps that are ensemble averages, reflecting molecules in various conformations. Yet, most models derived from these maps explicitly represent only a single conformation, overlooking the complexity of biomolecular structures. To accurately reflect the diversity of biomolecular forms, there is a pressing need to shift towards modeling structural ensembles that mirror the experimental data. However, the challenge of distinguishing signal from noise complicates manual efforts to create these models. In response, we introduce the latest enhancements to qFit, an automated computational strategy designed to incorporate protein conformational heterogeneity into models built into density maps. These algorithmic improvements in qFit are substantiated by superior Rfree and geometry metrics across a wide range of proteins. Importantly, unlike more complex multicopy ensemble models, the multiconformer models produced by qFit can be manually modified in most major model building software (e.g. Coot) and fit can be further improved by refinement using standard pipelines (e.g. Phenix, Refmac, Buster). By reducing the barrier of creating multiconformer models, qFit can foster the development of new hypotheses about the relationship between macromolecular conformational dynamics and function.

## Method in brief
MethodsGenerating and running the qFit test setTo test the impact of algorithmic changes in qFit, we created a dataset of 144 high-resolution (1.2-1.5 Å) X-ray crystallography structures deposited in the PDB (Supplementary Table 1). These were single-chain protein structures (in the asymmetric unit and at the level of biological assembly) and contained no ligands or mutations. The maximum sequence identity between any two structures was set as 30%. Based on CATH classification35, the resultant entries represented 72 folds (Supplementary Table 1). The structures represented 24 space groups. All these structures were re-refined as described in “Initial refinement protocol”. These re-refined models are referred to as deposited models. To create multiconformer models, we input the re-refined structures in qFit protein, followed by the post qFit refinement protocol. These multiconformer models are referred to as qFit models.Initial refinement protocolAll structures from the PDB were re-refined using phenix.refine with the following parameters:



The re-refined models were used as the input for subsequent qFit models.Running qFitFor this analysis qFit was run using the following command from qFit version 2023.1:X-rayqfit_protein composite_omit_map.mtz -l 2FOFCWT,PH2FOFCWT rerefine_pdb.pdbCryo-EMqfit_protein sharpened_map.ccp4 rerefine_cryo-EM.pdb -r <RESOLUTION> -em -n 10 -s 5qFit New FeaturesParallelization of large mapsOften, cryo-EM maps are very large and reach memory limits u

## Target venue
eLife
