## Working title
qFit: Automated Multiconformer Model Building for X-ray Crystallography and Cryo-EM

## Core question
Can an automated computational method reliably identify and model protein conformational heterogeneity (alternative conformations) from high-resolution density maps, producing multiconformer models that improve upon single-conformer deposited structures?

## Motivation / gap
- X-ray and cryo-EM density maps contain information about conformational ensembles, but most PDB depositions model only a single ground-state conformation
- Manual creation of multiconformer models is difficult, time-consuming, and complicated by noise
- Existing ensemble methods (phenix.ensemble_refinement) produce multiple complete copies that are hard to interpret and modify in software like Coot
- No automated tool reliably produces multiconformer models that improve standard quality metrics (Rfree) across diverse proteins
- Advances in high-throughput data collection and ligand-soaking campaigns create growing demand for automated heterogeneity detection
- Cryo-EM maps at high resolution also show conformational heterogeneity that current classification approaches cannot resolve at the side-chain level

## Core contribution (bullet form)
- Enhanced qFit algorithm with BIC-based model selection, B-factor sampling, and improved parallelization, validated on 144 high-resolution (1.2-1.5 A) X-ray structures representing 72 folds
- qFit models improve Rfree in 73% of structures (median deposited: 18.1%, median qFit: 17.5%, median improvement: 0.6%)
- Improved MolProbity score (deposited: 1.27 median, qFit: 1.09 median; p = 0.006), bond length RMSD (deposited: 0.010, qFit: 0.0073; p = 0.002), and bond angle RMSD (deposited: 1.31, qFit: 1.12; p = 0.002)
- qFit reliably recapitulates manually modeled alternative conformations from deposited structures
- Demonstrated applicability to high-resolution cryo-EM maps (e.g., apoferritin at 1.22 A, SARS-CoV-2 RNA polymerase at 2.0 A)
- Multiconformer models are compatible with standard refinement pipelines (Phenix, Refmac, Buster) and model building software (Coot)

## Method in brief
qFit protein takes a high-resolution density map (better than ~2 A) and a well-refined single-conformer structure as input. For each residue, it samples backbone conformations (collective N/C/Ca/O translation), aromatic angles, and side-chain dihedral angles exhaustively in a hierarchical scheme. B-factors are sampled by multiplying input values by 0.5-1.5 in 0.2 increments. Candidate conformations are scored using quadratic programming (QP) followed by mixed integer quadratic programming (MIQP) with Bayesian Information Criterion (BIC) selection to choose a parsimonious multiconformer. BIC penalizes model complexity: BIC = RSCC_penalty + k, where k counts parameters (3 per atom per conformation plus 1 B-factor per conformation for residues; number of torsion angles for segments).

After residue-level fitting, qFit segment combines conformations of consecutive residues into contiguous backbone segments using a similar QP/MIQP/BIC framework. The final model undergoes post-qFit refinement using standard pipelines. For cryo-EM, sharpened maps are used directly with resolution specified. The test set of 144 structures was selected with max 30% sequence identity, single-chain proteins without ligands or mutations, representing 72 CATH folds and 24 space groups.

## Target venue
eLife
