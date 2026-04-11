# Experimental Log

> Pre-writing data tables and observations for the TEMPy-REFF cryo-EM refinement study.

---

## Datasets Used

| Dataset | Source | Description | Size |
|---------|--------|-------------|------|
| CERES benchmark | EMDB + PDB | Cryo-EM maps with deposited atomic models | 366 maps |
| Resolution range | EMDB | Maps spanning near-atomic to medium resolution | 1.8-7.1 A |
| AlphaFold-Multimer models | AlphaFold DB | Predicted structures for unmodelled regions | Case studies |
| Focused maps (RNA Pol III) | EMDB | EMD-3178 (3.9 A) with PDB 5FJ8 | 1 complex |
| Nucleosome-CHD4 complex | EMDB | EMD-10058 with PDB 6RYR | 1 complex |
| SARS-CoV-2 RNA polymerase | EMDB | Case study for AlphaFold model refinement | 1 complex |
| Rotavirus VP6 | EMDB | EMD-6272, used for ensemble illustration | 1 complex |
| Glycoprotein B complex | EMDB | EMD-21247, 9-chain segmentation example | 1 complex |
| Composite map test | EMDB | EMD-12966, EMD-12967, EMD-12968 (3 focused maps) | 3 maps |

---

## Baselines and Methods Compared

| Method | Type | Key Feature |
|--------|------|------------|
| TEMPy-REFF (single model) | This work | Mixture model with B-factor refinement |
| TEMPy-REFF (ensemble) | This work | Ensemble of refined models |
| CERES | Benchmark standard | Re-refinement protocol for EMDB |
| PDB-deposited models | Reference | Original deposited structures |
| Phenix | Comparison | Standard cryo-EM refinement tool |
| RELION B-factors | Comparison | B-factor estimation from RELION |

---

## Metrics Used

| Metric | Description | Higher/Lower Better |
|--------|-------------|-------------------|
| CCC | Cross-correlation coefficient (map-model fit) | Higher |
| SMOCf | Local fit quality score per residue | Higher |
| RMSFe | Root mean square fluctuation across ensemble | Lower = more consistent |
| MolProbity | Stereochemical quality assessment | Lower clashscore = better |
| Map-model FSC | Fourier shell correlation between map and model | Higher |
| ResMap | Local resolution estimation | N/A (diagnostic) |

---

## Experiment 1: B-Factor Refinement (Position Fixed)

B-factors were optimized while keeping atomic positions fixed, to isolate the effect of B-factor estimation on fit quality.

| System | Initial B-factor | B-factor After 5 Steps | CCC Change |
|--------|-----------------|----------------------|------------|
| Uniform B = 10 | 10 (all atoms) | Converged (variable) | Improved |
| Multiple test cases | Uniform initial | Heterogeneous final | Positive delta CCC |

Extended Data Table S1 reports the change in CCC upon B-factor refinement for multiple systems. In all cases, B-factor optimization alone improves the map-model fit.

Fig. S1a: CCC and B-factor changes during refinement for EMD-10097. B-factor converges in approximately 10-12 iterations with accompanying CCC improvement.

Fig. S1b: Same convergence pattern demonstrated on EMD-30127.

---

## Experiment 2: B-Factor Convergence from Different Initial Values

Starting from various initial B-factor assignments, the method converges to similar final B-factor distributions.

| Initial B-factor Assignment | Convergence | Final B-factor Distribution |
|----------------------------|------------|---------------------------|
| All B = 1 (unit) | Converges | Similar to other initializations |
| All B = 1000 | Converges | Similar to other initializations |
| B = U(1, 1000) (random uniform) | Converges | Similar to other initializations |
| B = N(mu_exp, sigma_exp) (experimental) | Converges | Similar to other initializations |

Fig. S3: All four initialization strategies converge to essentially the same final B-factor distribution, demonstrating self-consistency.

Fig. S4: Final B-factor values are largely independent of initial assignment (B=1 vs. U(1,1000) comparison shows near-identity).

---

## Experiment 3: CERES Benchmark -- 366 Maps

The full benchmark compares TEMPy-REFF against CERES re-refined and original PDB-deposited models.

| Method | Avg CCC (overall) | CCC Trend at Low Resolution |
|--------|-------------------|---------------------------|
| PDB-deposited (initial) | Baseline | Decreases with lower resolution |
| CERES re-refined | Higher than deposited | Decreases with lower resolution |
| TEMPy-REFF single model | Comparable or higher than CERES | Decreases with lower resolution |
| TEMPy-REFF ensemble | Highest | Near-constant across resolutions |

### CCC by Resolution Band

| Resolution Band (A) | PDB-Deposited CCC | CERES CCC | TEMPy-REFF Single CCC | TEMPy-REFF Ensemble CCC |
|---------------------|-------------------|-----------|----------------------|------------------------|
| 1.8-2.8 | Baseline | Improved | Comparable/higher | Highest |
| 2.8-3.8 | Baseline | Improved | Comparable/higher | Highest |
| 3.8-4.8 | Baseline | Improved | Comparable/higher | Highest |
| 4.8-5.8 | Baseline | Moderate improvement | Comparable/higher | Near-constant (highest) |
| 5.8-7.1 | Baseline | Modest improvement | Comparable/higher | Near-constant (highest) |

Fig. 3a: Bar chart comparing CCC across resolution bands for deposited (blue), CERES (green), and TEMPy-REFF ensemble (orange). The ensemble method maintains high CCC even at lower resolution bands where CERES performance drops.

Extended Data Table S2: Detailed score changes upon refinement compared against CERES for all metrics.

---

## Experiment 4: Ensemble Size Optimization

The number of models in the ensemble was varied to determine the optimal ensemble size.

| Ensemble Size | CCC (individual models) | CCC (ensemble map) | Observation |
|--------------|------------------------|--------------------|----|
| 1 | Single model CCC | N/A | Baseline |
| 2-5 | Individual CCCs stable | Increasing | Rapid improvement |
| 5-10 | Individual CCCs stable | Plateau region | Diminishing returns |
| 10+ | Individual CCCs stable | Plateau | Marginal improvement |

Fig. 2a: Plot of CCC for individual ensemble members (blue line, roughly constant) and ensemble map CCC (orange line, rises then plateaus). The ensemble map consistently outperforms any individual member.

Fig. S7: Extended analysis showing the plateau behavior as more models are added, consistent with prior work in NMR ensemble methods and X-ray crystallographic ensembles.

---

## Experiment 5: Local Fit Quality and Ensemble Variability

The relationship between local fit quality (SMOCf) and ensemble variability (RMSFe) was assessed at the residue level.

| Metric Pair | Correlation | Direction |
|------------|------------|-----------|
| SMOCf vs. RMSFe | Anticorrelated | Higher local fit = lower variability |
| SMOCf vs. Local resolution (ResMap) | Correlated | Better local resolution = better local fit |

Fig. 2c: SMOCf score and RMSFe plotted along the protein chain for rotavirus VP6 (EMD-6272). Clear anticorrelation: residues with good local fit show low ensemble variability, and vice versa.

Fig. 2d: Comparison showing differences among ensemble members at various residue positions.

---

## Experiment 6: Case Study -- Glutamate Dehydrogenase (EMD-8194, 1.8 A)

| Model | SMOCf Pattern | Fit Quality |
|-------|--------------|-------------|
| PDB-deposited (5K12) | Baseline | Good (high resolution) |
| CERES-refined | Improved in some regions | Better |
| TEMPy-REFF ensemble | Best overall | Best local fit at most positions |

Fig. 3b: SMOCf plot along chain showing deposited (blue), CERES (green), and TEMPy-REFF ensemble (orange). The ensemble provides the best fit profile.

Fig. 3c: A double-occupancy histidine site requires more than one model to be correctly represented -- the ensemble naturally handles this.

---

## Experiment 7: Map Segmentation

The responsibility calculation naturally segments maps into contributions from individual chains.

| Test System | Chains | Segmentation Quality |
|------------|--------|---------------------|
| Glycoprotein B-Neutralizing Antibody Complex (EMD-21247) | 9 | Clean separation into 9 submaps |

Fig. 4a: Visualization of the 9-chain segmentation, each submap colored differently, showing clean assignment of density to individual protein chains.

---

## Experiment 8: Composite Map Construction

Three focused maps were combined into a single composite map using optimal mixture-model weights.

| Map Component | EMDB ID | Role |
|--------------|---------|------|
| Focused map 1 | EMD-12966 | Cyan region |
| Focused map 2 | EMD-12967 | Purple region |
| Focused map 3 | EMD-12968 | Pink region |
| Deposited composite | EMD-12969 | Reference |
| TEMPy-REFF composite | Computed | Optimally weighted combination |

Fig. 4b: Visual comparison of the three input focused maps and resulting composite.

Fig. 4c: Map-model FSC comparison: the TEMPy-REFF composite (orange) achieves higher FSC than the deposited composite (blue) across most spatial frequencies.

---

## Experiment 9: RNA Polymerase III Case Study (EMD-3178, 3.9 A)

| Feature | Deposited (PDB 5FJ8) | TEMPy-REFF Refined |
|---------|----------------------|-------------------|
| B-factor source | RELION | TEMPy-REFF |
| B-factor normalization | 0-1 range | 0-1 range |
| Missing regions | Some unmodelled | Modelled with AlphaFold |

Fig. 5a: Side-by-side comparison of B-factors from deposited structure (RELION B-factors, left) and TEMPy-REFF refined (right). Both colored on 0-1 normalized scale.

Fig. 5b: Chain A in complex with RNA chains (R, S, T). Deposited structure (blue, top) vs. TEMPy-REFF refined (orange, bottom) showing improved fit.

---

## Experiment 10: Nucleosome-CHD4 Complex (EMD-10058, PDB 6RYR)

| Observation | Detail |
|-------------|--------|
| B-factor vs. local resolution | B-factor width (worm representation) correlates with local resolution from ResMap |
| Flexible regions | Higher B-factors and lower local resolution in flexible loops |
| Ensemble improvement | Ensemble captures flexibility that single model misses |

Fig. 6a: Structure in worm representation with width proportional to B-factor and color based on local resolution.

Fig. 6b: Deposited model (blue, left) vs. ensemble of TEMPy-REFF models (orange, right) shown inside the cryo-EM map. The ensemble fills more density, especially in lower-resolution regions.

---

## Experiment 11: SARS-CoV-2 RNA Polymerase (AlphaFold Model Refinement)

| Feature | Before Refinement | After TEMPy-REFF |
|---------|-------------------|------------------|
| Model source | AlphaFold-Multimer prediction | Refined into cryo-EM map |
| Previously unmodelled regions | Present | Newly modelled |

Fig. 6c: Demonstration that AlphaFold-Multimer models can be refined into cryo-EM maps using TEMPy-REFF to provide newly-modelled regions in deposited EMDB maps.

---

## Experiment 12: Forcefield Comparison

| Forcefield | Avg CCC After Refinement | Preferred Dihedrals |
|-----------|-------------------------|-------------------|
| AMBER | Slightly higher on average | Slight backbone preference differences |
| CHARMM36 | Comparable | Slight backbone preference differences |

Extended Data Table S4: No significant bias from forcefield choice. AMBER runs yielded slightly higher CCC on average. Green highlighting marks the forcefield with higher CCC for each system.

Fig. S9: Small differences in preferred backbone dihedrals between AMBER and CHARMM36, but these do not materially affect refinement quality.

---

## Experiment 13: Computational Speed

| System | Map Size | Time per Run |
|--------|---------|-------------|
| Various (Extended Data Table S3) | Variable | Minutes to low hours |

Extended Data Table S3: Speed benchmark across multiple systems. The method is described as computationally quick, especially relative to the sampling needed for the ensemble.

---

## Key Algorithm Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| K (force constant) | 400 | Fictitious map-derived force constant |
| kappa (implicit solvent) | 3 | GB-Neck2 implicit solvent parameter |
| B-factor convergence | ~10-12 iterations | Empirically determined |
| Forcefield | AMBER (default) | Via OpenMM |
| Solvent model | GB-Neck2 | Implicit solvent |
| Occupancy | Set to 1 (fixed) | Not refined |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Flowchart of TEMPy-REFF: EM algorithm for responsibility -> parameter re-estimation -> ensemble generation -> map segmentation/composition |
| Fig. 2a | Ensemble map CCC exceeds individual model CCC; plateau reached after ~5-10 models |
| Fig. 2b | Visual comparison of single-model map vs. ensemble map at contour level 0.02 |
| Fig. 2c | SMOCf and RMSFe are clearly anticorrelated along the chain |
| Fig. 3a | Ensemble CCC remains near-constant at lower resolutions while CERES CCC declines |
| Fig. 3c | Double-occupancy histidine requires ensemble representation |
| Fig. 4a | Clean 9-chain segmentation via responsibilities |
| Fig. 4c | TEMPy-REFF composite map achieves higher FSC than deposited composite |
| Fig. 5a | TEMPy-REFF B-factors show different spatial distribution than RELION B-factors |
| Fig. 6a | B-factor correlates with local resolution in nucleosome-CHD4 complex |
| Fig. 6c | AlphaFold models refined into cryo-EM maps capture previously unmodelled regions |
| Fig. S1 | B-factor converges in 10-12 iterations with accompanying CCC improvement |
| Fig. S3 | Four different B-factor initializations converge to same final values |
| Fig. S4 | Final B-factors independent of initial assignment |
| Fig. S7 | Ensemble CCC plateaus with increasing ensemble size |
| Fig. S9 | AMBER and CHARMM36 show minor dihedral preference differences |

---

## Statistical Summary

| Test/Comparison | Context | Observation |
|----------------|---------|-------------|
| CCC improvement (B-factor only) | All tested systems | Positive improvement in every case |
| CCC improvement (full refinement) | 366 CERES benchmark | TEMPy-REFF >= CERES on average |
| Ensemble vs. single model CCC | All tested systems | Ensemble consistently higher |
| SMOCf vs. RMSFe correlation | Residue level | Strong anticorrelation |
| SMOCf vs. local resolution | Residue level | Positive correlation |
| AMBER vs. CHARMM CCC | Benchmark subset | No significant difference; AMBER slightly higher |

---

## Reference Count
56 references cited in the paper.
