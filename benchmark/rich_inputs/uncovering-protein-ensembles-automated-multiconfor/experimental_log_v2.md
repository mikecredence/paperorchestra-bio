# Experimental Log: qFit Multiconformer Model Building

## Test Set Characteristics (Supplementary Table 1)

| Parameter | Value |
|-----------|-------|
| Total structures | 144 |
| Resolution range | 1.2-1.5 A |
| Max sequence identity between any two | 30% |
| CATH folds represented | 72 |
| Space groups | 24 |
| Chain requirement | Single-chain (ASU and biological assembly) |
| Ligands | None |
| Mutations | None |

## Initial Refinement Protocol

| Step | Tool | Parameters |
|------|------|-----------|
| Re-refinement | phenix.refine | Standard parameters |
| Input for qFit | Re-refined models (not raw PDB depositions) |
| Map for X-ray | Composite omit map (2mFo-DFc) |
| Map for cryo-EM | Sharpened map |

## qFit Algorithm Components

### qFit Residue (Fig 1A)

| Step | Description |
|------|-------------|
| A.1 Backbone sampling | Collective translation of N, C, Ca, O coordinates |
| A.2 Aromatic angle sampling | Ca-Cb-Cg angle for His, Tyr, Phe, Trp |
| A.3 Dihedral angle sampling | Exhaustive chi1 sampling, then remaining chi angles |
| A.4 Final scoring | QP + B-factor sampling + MIQP with BIC selection |

### B-Factor Sampling

| Multiplier Range | Increment |
|-----------------|-----------|
| 0.5 - 1.5 | 0.2 |
| Applied after | QP reduction of conformations |
| Combined with | Coordinate conformations for MIQP |

### BIC Formulation

| Component | Formula |
|-----------|---------|
| BIC | RSCC penalty + k |
| k (residue) | 3 * n_atoms * n_conformers + n_conformers |
| k (segment) | n_torsion_angles |
| Cardinality tested | 1 to 5 conformations |
| Selection | Lowest BIC wins |

## Rfree Results (Fig 2A, Supplementary Fig 2)

### Overall Rfree Improvement

| Metric | Deposited Models | qFit Models |
|--------|-----------------|-------------|
| Median Rfree | 18.1% | 17.5% |
| Median improvement | -- | 0.6% |
| % structures with improved Rfree | -- | 73% |

### R-gap (Supplementary Fig 2B)

| Metric | Deposited | qFit |
|--------|-----------|------|
| Median R-gap | 3.0% | 3.0% |

Fig 2A: Distribution of Rfree shows qFit models shifted left (better) compared to deposited.
Supplementary Fig 2A: Distribution of Rfree difference shows median 0.6% improvement.

## Geometry Metrics (Fig 3, Supplementary Fig 4)

### MolProbity Score (Fig 3A)

| Model | Median | IQR | p-value (two-sided t-test) |
|-------|--------|-----|---------------------------|
| Deposited | 1.27 | 0.94-0.16 | -- |
| qFit | 1.09 | 0.90-1.30 | 0.006 |

### Bond Length RMSD (Fig 3B)

| Model | Median (A) | IQR | p-value |
|-------|-----------|-----|---------|
| Deposited | 0.010 | 0.007-0.015 | -- |
| qFit | 0.0073 | 0.005-0.011 | 0.002 |

### Bond Angle RMSD (Fig 3C)

| Model | Median (degrees) | IQR | p-value |
|-------|-----------------|-----|---------|
| Deposited | 1.31 | 0.96-1.83 | -- |
| qFit | 1.12 | 0.86-1.52 | 0.002 |

### Additional Geometry (Supplementary Fig 4)

| Metric | Deposited (median [IQR]) | qFit (median [IQR]) | p-value |
|--------|--------------------------|---------------------|---------|
| Cb deviations (>0.25A) per model | 0.0 [0.0-0.0] | 0.0 [0.0-0.0] | 0.37 |
| Rotamer outliers per model | 0.94 [0.00-2.12] | 0.81 [0.35-1.60] | 0.73 |
| % Ramachandran favored | 97.70 [96.90-98.93] | 98.0+ | -- |

## Alternative Conformation Recapitulation (Fig 4)

### Ground Truth Comparison Categories

| Category | Definition |
|----------|-----------|
| Multiconformer match | qFit multiconformer with RMSD < 0.5A from ground truth |
| Multiconformer no match | qFit multiconformer but wrong conformations |
| Single-conformer match | qFit single conformer matching ground truth |
| Single-conformer no match | qFit single but ground truth has alternatives |

### Resolution Dependence (Fig 4, Supplementary Fig 5)

| Resolution (A) | Multiconformer Match Rate | Single Match Rate |
|----------------|--------------------------|-------------------|
| 1.2-1.3 | Highest | Good |
| 1.3-1.5 | Good | Good |
| 1.5-1.8 | Decreasing | Moderate |
| 1.8-2.0 | Low | Moderate |
| >2.0 | Poor | -- |

qFit performs best at high resolution where signal-to-noise allows reliable detection of alternative conformations.

### Rotamer State Analysis (Supplementary Fig 3)

| Category | Description | Example PDB |
|----------|-------------|-------------|
| Same | Identical rotamers in deposited and qFit | 1BN6, His199 |
| Additional in qFit | qFit finds extra rotamer(s) | 3CX2, Glu165 |
| Additional in deposited | Deposited has rotamers qFit misses | -- |
| Different | No shared rotamers | -- |

## Cryo-EM Application (Fig 5)

### Structures Tested

| PDB | Protein | Resolution (A) | Key Finding |
|-----|---------|---------------|-------------|
| 7A4M | Apoferritin | 1.22 | Recapitulated deposited alternative conformations (e.g., Arg22) |
| 7K7B | SARS-CoV-2 RNA polymerase | 2.0 | Identified previously unmodeled alternative conformations |

### Apoferritin (7A4M, Fig 5A)

| Residue | Deposited Conformers | qFit Conformers | Match |
|---------|---------------------|-----------------|-------|
| Arg22 (chain A) | 2 conformers | 2 conformers | Recapitulated |

### SARS-CoV-2 RNA Polymerase (Fig 5B)

| Finding | Detail |
|---------|--------|
| Novel alternative conformations | Previously unmodeled conformations identified |
| Density support | Shown at 0.5 and 1.0 sigma contours |

## Synthetic Resolution Study (Supplementary Fig 5)

| Starting Model | PDB 7KR0 |
|----------------|-----------|
| Procedure | Generate synthetic structure factors at varying resolutions |
| Repetitions | 10 per resolution (7KR0), 1 per resolution (larger set) |
| Finding | qFit multiconformer detection decreases with worsening resolution |

## Software and Versions

| Component | Detail |
|-----------|--------|
| qFit version | 2024.2 (paper), 2023.1 (analysis) |
| Repository | https://github.com/ExcitedStates/qfit-3.0 |
| Distribution | SBGrid |
| Refinement | Phenix, Refmac, Buster (all compatible) |
| Model building | Coot (compatible) |
| Optimization | MIQP solver |
| Parallelization | Python multiprocessing |
| Map handling | Chunked for large cryo-EM maps |

## qFit Command Lines

| Application | Command |
|-------------|---------|
| X-ray | qfit_protein composite_omit_map.mtz -l 2FOFCWT,PH2FOFCWT rerefine_pdb.pdb |
| Cryo-EM | qfit_protein sharpened_map.ccp4 rerefine_cryo-EM.pdb -r RESOLUTION -em -n 10 -s 5 |

## New Features in This Version

| Feature | Description |
|---------|-------------|
| B-factor sampling | Multiplier range 0.5-1.5 in 0.2 steps |
| BIC selection | Bayesian information criterion for parsimony |
| Large map parallelization | Map chunking for cryo-EM |
| Iterative MIQP | Handles non-convex optimization failures |
| Post-qFit refinement | Standardized protocol |

## Key Figure Observations

- Fig 1: Algorithmic flow showing residue sampling (backbone, aromatic, dihedral, scoring) and segment combination
- Fig 2A: Rfree distribution shifted left for qFit models; 73% improved
- Fig 2B: Example of qFit finding new alternative conformations near RNA binding motif (PDB 1G8A)
- Fig 3A-C: MolProbity, bond length, and bond angle metrics all significantly improved
- Fig 4: Ground truth comparison at varying resolutions shows resolution dependence
- Fig 5A: Cryo-EM apoferritin - qFit recapitulates deposited alternates
- Fig 5B: Cryo-EM SARS-CoV-2 - qFit identifies novel alternates
- Supplementary Fig 1: PDB selection flow diagram
- Supplementary Fig 2: Rfree difference and R-gap distributions
- Supplementary Fig 5: Synthetic resolution study confirms resolution requirements
