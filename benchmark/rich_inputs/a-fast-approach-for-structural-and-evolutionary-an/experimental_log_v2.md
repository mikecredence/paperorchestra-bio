# Experimental Log

> Pre-writing data tables and observations for the energy profile protein comparison study.

---

## Datasets Used

| Dataset | Source | Description | Filtering Criteria |
|---------|--------|-------------|-------------------|
| Training set | PISCES (PDB) | Non-redundant protein chains | Seq identity < 50%, resolution < 1.6 A, R-factor < 0.25, length 40-1000 residues |
| ASTRAL40 | SCOPe v2.08 | Protein domains at 40% seq identity cutoff | BLAST E-value filtered |
| ASTRAL95 | SCOPe v2.08 | Protein domains at 95% seq identity cutoff | BLAST E-value filtered |
| CATH benchmark | CATH v4.2.0 | 251 protein domains from 2 families in 5 superfamilies | Residue count 44-854, average 211 |
| Ferritin-like superfamily | SCOP a.25.1 | Proteins from families a.25.1.1 and a.25.1.2 | As used by Malik et al. and Lelievre et al. |
| Coronavirus spike glycoproteins | PDB | Structures from SARS-CoV, SARS-CoV-2, MERS-CoV | All available spike structures |
| Bacteriocins | Various | 690 peptides across 3 bacteriocin classes | N/A |
| SARS-CoV-2 proteome | Various | 4,405 proteins across 28 families | Large-scale test |

---

## Baselines and Methods Compared

| Method | Type | Requires Structure? | Alignment-Free? |
|--------|------|---------------------|-----------------|
| CPE (this work) | Sequence-based energy profile | No | Yes |
| SPE (this work) | Structure-based energy profile | Yes | Yes |
| TM-Vec | Deep learning embedding | No (trained on structures) | Yes |
| TM-Score | Template modeling score | Yes | No |
| RMSD | Root mean square deviation | Yes | No |
| GR-Align | Graph-based alignment (GDS metric) | Yes | No |
| Yau-Hausdorff | Geometric set distance | Yes | Yes |

---

## Experiment 1: Correlation Between Sequence-Based and Structure-Based Energy

Fig. 2A and 2B show strong Pearson correlation between total energy from structure (y-axis) and total energy estimated from sequence (x-axis) for both ASTRAL40 and ASTRAL95 datasets. The p-value is less than 1e-16 in both cases.

Fig. 2C shows the correlation between the difference in total energy (sequence vs. structure) and protein length. The relationship is weak, indicating protein length does not substantially bias energy estimates.

Fig. 2F shows a histogram of correlation coefficients between energy differences and protein length across all 210 pairwise interaction types. 96% of interaction types display a correlation less than 0.5 with protein length.

| Dataset | Comparison | Correlation (Pearson r) | p-value |
|---------|------------|------------------------|---------|
| ASTRAL40 | Total energy: sequence vs. structure | ~1.0 (strong) | < 1e-16 |
| ASTRAL95 | Total energy: sequence vs. structure | ~1.0 (strong) | < 1e-16 |
| ASTRAL40 | CPE distance vs. SPE distance (all pairs) | ~1.0 (strong) | < 1e-16 |
| ASTRAL95 | CPE distance vs. SPE distance (all pairs) | ~1.0 (strong) | < 1e-16 |
| ASTRAL40 | Energy difference vs. protein length | Low (<0.5 for 96% of types) | Varies |

---

## Experiment 2: UMAP Visualization of Energy Profiles Across SCOP Hierarchy

Fig. 3 shows UMAP projections (n_neighbors=30, min_dist=0.1) of both CPE and SPE for protein domains from ASTRAL40 and ASTRAL95.

| SCOP Level | Example Groups Tested | Observation |
|------------|----------------------|-------------|
| Class | All-alpha vs. All-beta | Clear separation in both CPE and SPE UMAP embeddings |
| Fold | a.100 vs. a.104 (within all-alpha) | Domains cluster by fold identity |
| Superfamily | a.29.2 vs. a.29.3 (within fold a.29) | Distinct clustering by superfamily |
| Family | a.25.1.0 vs. a.25.1.2 (within superfamily a.25.1) | Family-level separation visible |

Fig. 4A-B: Intraclass distances (within all-alpha) are significantly lower than interclass distances (all-alpha vs. other classes) for both CPE and SPE. Same pattern holds at fold, superfamily, and family levels.

---

## Experiment 3: Protein Classification on CATH Benchmark (251 Domains)

| Method | Accuracy (%) | Computation Time |
|--------|-------------|-----------------|
| CPE | 100.0 | ~1 second |
| SPE | ~100.0 | Longer (requires structures) |
| TM-Vec | 100.0 | ~67 seconds |
| TM-Score | 81.5 | Hours |
| RMSD | 59.2 | Hours |
| GR-Align | 59.2-81.5 range | Hours |
| Yau-Hausdorff | 59.2-81.5 range | Hours |

Fig. 4A: Time vs. accuracy scatter plot. CPE and TM-Vec both reach 100% accuracy. CPE is far faster.
Fig. 4B: Running times scaled to 12 hours. The inset circle represents 80 seconds. CPE occupies a negligible fraction.

System used for timing: 2.4 GHz processor, 8 GB RAM.

---

## Experiment 4: Superfamily Classification (1-NN)

Table 1 from paper: Total accuracy and F1 measure for each of the five superfamilies using 1-nearest-neighbor classification.

| Superfamily | CPE Accuracy | CPE F1 | SPE Accuracy | SPE F1 | TM-Vec Accuracy | TM-Vec F1 |
|-------------|-------------|--------|-------------|--------|----------------|-----------|
| Superfamily 1 | ~100% | ~1.0 | ~100% | ~1.0 | ~100% | ~1.0 |
| Superfamily 2 | ~100% | ~1.0 | ~100% | ~1.0 | ~100% | ~1.0 |
| Superfamily 3 | ~100% | ~1.0 | ~100% | ~1.0 | ~100% | ~1.0 |
| Superfamily 4 | ~100% | ~1.0 | ~100% | ~1.0 | ~100% | ~1.0 |
| Superfamily 5 | ~100% | ~1.0 | ~100% | ~1.0 | ~100% | ~1.0 |
| **Overall** | **~100%** | **~1.0** | **~100%** | **~1.0** | **~100%** | **~1.0** |

All three methods approached near-perfect performance on this benchmark. The differentiator is speed, not accuracy on this dataset.

---

## Experiment 5: Alpha vs. Beta Globin Discrimination

Fig. 4C: UMAP projection for 21 mammalian hemoglobin structures (alpha-globins and beta-globins). All methods (CPE, SPE, TM-Vec) effectively differentiate between alpha and beta globins, despite their highly similar structures but distinct functional roles within the hemoglobin tetramer.

| Method | Alpha vs. Beta Globin Separation | Notes |
|--------|----------------------------------|-------|
| CPE | Clear separation | Captures functional divergence from sequence |
| SPE | Clear separation | Structure-based confirmation |
| TM-Vec | Clear separation | Deep learning embedding |

---

## Experiment 6: Phylogenetic Network of Ferritin-Like Superfamily

Proteins from SCOP superfamily a.25.1, split into two main families:
- a.25.1.1: Ferritins, Bacterioferritins, Dps, Rubrerythrin
- a.25.1.2: RNR R2, BMM-alpha, BMM-beta, Fatty acid desaturases

Phylogenetic networks reconstructed using NeighborNet (phangorn package, visualized with SplitTree).

Table 2: Spearman correlation between the manually curated reference network branching order and predicted branching orders.

| Method | Spearman Correlation with Manual Network |
|--------|----------------------------------------|
| SPE | Reported (see paper Table 2) |
| TM-Vec | Reported (see paper Table 2) |
| CPE | Reported (see paper Table 2) |

Fig. 5B: SPE phylogenetic network recovers two main branches matching a.25.1.1 and a.25.1.2. Subgroup structure (Ferritins, Dps, Rubrerythrin, Bacterioferritins within a.25.1.1; BMM-alpha, BMM-beta, Fatty acid desaturase, RNR R2 within a.25.1.2) is largely preserved.

Fig. 5C: Neighbor-joining tree from SPE average distances recapitulates subgroup relationships.

Fig. 5D-E: TM-Vec phylogenetic network and neighbor-joining tree show similar topology.

Fig. 5F: CPE phylogenetic network also recovers the two main branches.

---

## Experiment 7: Coronavirus Spike Glycoprotein Clustering

Spike glycoprotein structures from SARS-CoV, SARS-CoV-2, and MERS-CoV were clustered using six different methods.

| Method | Clustering Quality | Correct Virus-of-Origin Grouping |
|--------|-------------------|----------------------------------|
| Sequence alignment | Dendrograms shown (Fig. 6A) | Partial |
| CPE | Dendrograms shown (Fig. 6B) | Good separation by virus |
| TM-Vec | Dendrograms shown (Fig. 6C) | Good separation |
| SPE | Dendrograms shown (Fig. 6D) | Good separation |
| RMSD | Dendrograms shown (Fig. 6E) | Partial |
| TM-Score | Dendrograms shown (Fig. 6F) | Partial |

Fig. 6G: Displacement analysis showing structural differences between spike proteins from the three viruses.

Fig. 6: Leaves of each dendrogram are color-coded by originating virus. CPE and SPE provide clean separation comparable to TM-Vec.

---

## Experiment 8: Bacteriocin Classification

| Dataset Detail | Value |
|---------------|-------|
| Total peptides | 690 |
| Number of classes | 3 |
| Inter-class pairs | 125,869 |

Fig. 7A: UMAP projection of CPE for 690 bacteriocin peptides shows three distinct clusters corresponding to bacteriocin classes.

Fig. 7B: Comparison of CPE distances with TM-scores from TM-align on structures predicted by AlphaFold2, OmegaFold, and ESMFold, and with TM-Vec distances.

| Comparison | Pair Type | n Pairs | Observation |
|-----------|-----------|---------|-------------|
| CPE vs. TM-score (AlphaFold2) | Different classes | 125,869 | CPE distances correlate with structural distances |
| CPE vs. TM-score (OmegaFold) | Different classes | 125,869 | Similar correlation pattern |
| CPE vs. TM-score (ESMFold) | Different classes | 125,869 | Similar correlation pattern |
| CPE vs. TM-Vec | All pairs | N/A | Comparable discrimination |

---

## Experiment 9: Large-Scale SARS-CoV-2 Proteome Analysis

Table 3 from paper: Analysis across 28 protein families, encompassing 4,405 proteins.

| Metric | CPE | SPE | TM-Vec |
|--------|-----|-----|--------|
| Overall Accuracy | High (see Table 3) | High (see Table 3) | High (see Table 3) |
| F1 Score | High (see Table 3) | High (see Table 3) | High (see Table 3) |
| Computation Time | Fastest | Moderate | Slower |

The 1-NN classifier was used for family detection across 28 families. CPE maintains fast computation even at this larger scale.

---

## Experiment 10: Drug Combination Prediction (Separation Measure)

The study introduces a separation measure based on energy profile similarity as a proxy for network-based drug combination predictions.

| Comparison | Metric | Result |
|-----------|--------|--------|
| CPE separation vs. network-based separation | Correlation | Significant (p < threshold) |
| Computational requirement | CPE | Orders of magnitude faster |
| Computational requirement | Network-based | Requires full PPI network construction |

The discussion notes that energy-profile-based separation correlates significantly with network-based approach results, emphasizing utility for drug combination screening.

---

## Key Technical Parameters

| Parameter | Value |
|-----------|-------|
| Number of amino acid types | 20 |
| Number of unique pairwise interaction types | 210 |
| Number of atom types | 167 |
| Distance shells | 30 (starting at 0.75 A, width 0.5 A) |
| RT constant | 0.582 kcal/mol |
| Observation weight (sigma) | 0.02 |
| CPE/SPE vector dimensionality | 210 |
| Distance metric | Manhattan distance |
| UMAP parameters (main figures) | n_neighbors=30, min_dist=0.1 |
| UMAP parameters (CATH figures) | n_neighbors=13, min_dist=0.1 |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Schematic of the pipeline: potential function construction, predictor matrix estimation, SPE from structure, CPE from sequence |
| Fig. 2A-B | Strong linear correlation between sequence-based and structure-based total energy for both ASTRAL40 and ASTRAL95 |
| Fig. 2C | Weak correlation between energy difference and protein length |
| Fig. 2D-E | Strong correlation between CPE and SPE pairwise distances |
| Fig. 2F | 96% of interaction types show < 0.5 correlation with protein length |
| Fig. 3 | UMAP shows clear clustering at fold, superfamily, and family levels for both CPE and SPE |
| Fig. 4A | CPE and TM-Vec both achieve 100% accuracy; CPE is orders of magnitude faster |
| Fig. 4B | CPE computation time is negligible on the 12-hour scale |
| Fig. 4C | All methods separate alpha and beta globins |
| Fig. 5 | Phylogenetic networks from SPE, TM-Vec, and CPE all recover the two main ferritin-like family branches |
| Fig. 6 | CPE and SPE cluster coronavirus spike glycoproteins by virus of origin |
| Fig. 7A | UMAP of CPE for bacteriocins shows three distinct class clusters |
| Fig. 7B | CPE distances correlate with structure-based distances across multiple structure predictors |

---

## Statistical Tests Mentioned

| Test | Context | Result |
|------|---------|--------|
| Pearson correlation | Sequence vs. structure energy (ASTRAL40/95) | r near 1.0, p < 1e-16 |
| Pearson correlation | CPE distance vs. SPE distance | r near 1.0, p < 1e-16 |
| Spearman correlation | Phylogenetic branching order vs. manual reference | Values reported in Table 2 |
| 1-NN classification | Superfamily and family-level classification | Accuracy and F1 reported in Tables 1 and 3 |
| Distance comparison | Intra-class vs. inter-class | Intra-class significantly lower |

---

## Reference Count
50 references cited in the paper.
