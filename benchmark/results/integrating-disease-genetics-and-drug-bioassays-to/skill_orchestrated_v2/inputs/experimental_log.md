# Experimental Log: Draphnet

## Data sources and matrices

| Matrix | Definition | Dimensions | Source |
|---|---|---|---|
| D | Drug x endpoint | 429 compounds x 1391 endpoints (with missing entries; each drug assayed on ~100 endpoints on average) | EPA ToxCast/Tox21 Level 5 |
| P | Gene x phenotype (signed z-score of gene-phenotype association) | 10,027 genes x 197 phenotypes | PhenomeXcan (S-MultiXcan over UK Biobank GWAS) |
| Y | Drug x phenotype (binary; indication or side effect) | 429 x 197 | SIDER, matched via UMLS CUIs |
| U_D S_D | Low-rank SoftImpute projection of D | 429 x r_D | SoftImpute on D |
| W_DP | Learned interaction matrix (in factored space) | r_D x r_P | Logistic affinity regression |

Final selected ranks and regularization (picked by cross-validation on held-out drugs):

| Hyperparameter | Value |
|---|---|
| r_P (SVD rank of P) | 131 |
| r_D (SoftImpute rank of D) | 95 |
| Lasso logistic regularization | 1 |
| Drug fraction held out per CV fold (prediction evaluation) | 5% |
| Drug fraction held out per CV fold (regularization tuning) | 10% |
| Number of CV folds (prediction comparison) | 20 |
| Entries masked for SoftImpute hyperparameter tuning | 5% of non-missing |
| Permutations for drug-disease-genome null | 10,000 |
| Clique-null simulations (disease-gene overlap) | 1,000 |
| Multiple-testing correction (drug-gene p-values) | Benjamini-Yekutieli |
| Multiple-testing correction (target enrichment) | Benjamini-Hochberg |

## Experiment 1: Premise — similarity of molecular profiles aligns with phenotypic similarity

For each pair of drugs, we compute the Jaccard similarity of their binary SIDER profiles and the Spearman correlation of their ToxCast endpoint scores over shared endpoints. We relate the two at the pair level.

| Test | Statistic | p-value | Note |
|---|---|---|---|
| Spearman of Jaccard index vs ToxCast endpoint correlation across drug pairs | not reported | p=1e-22 | accounting implicit via test |
| Linear model of Jaccard index vs endpoint correlation adjusting for number of shared endpoints | not reported | p=1.7e-43 | adjusts for number of endpoints a pair has in common |
| Analogous test for phenotypes: Jaccard over drug overlap vs PhenomeXcan gene-profile similarity | not reported | p=4e-81 | Fig 1C; all tissues show high correlation |
| Spearman correlation between D-space similarity and U_D S_D-space similarity of drug pairs | 0.21 | n/a | similarity preserved under dimensionality reduction |
| Spearman correlation between Jaccard distance and PhenomeXcan-profile correlation of disease pairs | -0.11 | n/a | Fig 1C |

## Experiment 2: Predictive performance on held-out drugs

20-fold cross-validation; within each fold 5% of drugs held out. Side-effect profiles predicted by Draphnet vs by nearest-neighbor in D.

| Comparison | Metric | Test | p-value |
|---|---|---|---|
| Draphnet vs nearest-neighbor baseline (held-out drugs) | Jaccard distance (predicted vs actual side-effect profile) | rank-sum | p=3e-8 |

Direction: Draphnet achieves lower Jaccard distance than nearest neighbor for a majority of drugs (Fig 2A).

Qualitative prediction highlights (from ranked off-label predictions):
- fludrocortisone ranked top non-indicated predicted treatment for eczema (an oral corticosteroid; eczema is typically treated by topical steroids).
- methyclothiazide ranked top non-indicated predicted treatment for glaucoma (a diuretic; glaucoma's main cause is fluid retention in the eye).
- dasatinib's top predicted indications were cancers despite its primary indication (leukemias) not being in training matrix P.

## Experiment 3: Drug-target enrichment of ToxCast profile similarity

For each DrugBank target, compare Spearman correlations between pairs of drugs sharing that target vs pairs that do not.

| Test | p-value |
|---|---|
| Aggregate rank-sum: drugs sharing >=1 target have more similar ToxCast endpoint effects than those that do not | p=1e-28 |

## Experiment 4: Drug phenome-effect matrix vs permutation null (by target)

We project D via U_D S_D W_DP and compare drugs sharing targets against those projected using permuted interaction matrices.

- For most drug targets, the true projection distinguishes drugs sharing targets from those that do not better than the null (Fig 2B; each point is a target; axes compare -log10 p-values).
- Among pairs of drugs that share a target, phenome-effect Spearman correlation is systematically higher in the true projection than in the null projection (Fig 2C; stars indicate significance thresholds; "*****+" denotes p<10^-5).
- A small number of target classes do not show improvement, consistent with polypharmacology (example: CHRM1 is annotated as a target for 14 drugs including anticholinergics, neuroleptics, migraine treatments, and ophthalmological preparations; these 14 drugs have a median of 19 other targets).

## Experiment 5: Drug-disease-genome matrix and target-level disease-gene enrichment

Projection onto the 10,027-gene disease-genome space using inverse SVD of P; empirical permutation p-values (10,000 permutations), Benjamini-Yekutieli adjustment.

| Quantity | Value |
|---|---|
| Median number of disease genes associated per drug | 7 |
| DrugBank targets tested (shared by >=3 drugs) | 132 |
| Targets with >=1 significantly associated disease gene (adj. p<0.01) | 28 |

Fig 3A: empirical -log10 p-value calibration plot shows true drug-target association significance is much higher than that of permuted targets.

Representative associations (Fig 3B-C):
- Fig 3B: t-SNE shows drugs in the same ATC therapeutic category cluster together; calcium channel blockers cluster; anti-inflammatories/analgesics cluster.
- PPM1M: associated with several HTR2C-targeting neuroleptics (serotonin signaling). PPM1M is the top PhenomeXcan gene for bipolar disorder; a recent schizophrenia GWAS reported a locus in this gene; another study linked the locus to rare mental illness.
- CETP: associated with fenofibrate and other drugs targeting lipid metabolism; PhenomeXcan links CETP to high cholesterol; prior experimental work supports CETP as an effector of fenofibrate and PPARalpha agonism.

## Experiment 6: Novel drug categorization via disease-gene cliques

Construct a drug-drug graph by connecting pairs of drugs with more shared significant disease genes than expected under a weighted random null (1,000 simulations, sampling disease genes in proportion to the number of drugs they are significantly associated with). Identify fully connected cliques with >=3 drugs; visualize with igraph (Fig 4).

Observed cliques (selected):
- anti-inflammatories (ketoprofen, ibuprofen, indomethacin) cluster together and connect to PPARalpha-agonists (fenofibrate, bezafibrate); pyridoxine (vitamin B-6) is also connected.
- calcium channel blockers (bepridil, verapamil) are connected to pimozide (a psychiatric drug known to cause arrhythmia as a side effect).
- mecamylamine (largely discontinued antihypertensive) connected to pindolol (antihypertensive beta blocker) and gabapentin (CNS drug for seizures and nerve pain). Mecamylamine was discontinued in part due to CNS effects and has been investigated for seizure and behavioral disorders.

Visualization filters for Fig 4:
- Disease genes kept only if associated with >=1 gene target AND associated with fewer than 15 total drugs.
- Drugs kept only if in a fully connected clique of size >=3.
- Only selected cliques (e.g., verapamil, bepridil, pimozide) shown as filled polygons.

## Methods parameters (verbatim)

| Parameter / step | Value |
|---|---|
| ToxCast data level | Level 5 (public; fraction of models calling a compound a "hit" per endpoint) |
| Number of compounds in D | 429 |
| Number of endpoints in D | 1391 |
| Average endpoints assayed per drug | ~100 |
| Number of genes in P after variance filtering (top half of most-variable genes) | 10,027 |
| Number of UK Biobank phenotypes matched to SIDER | 197 |
| Gene-phenotype score | \|Phi^-1(multiXcan_p)\| * sign (consensus S-PrediXcan sign across tissues) |
| Phenotype matching method | UMLS concept unique identifiers (CUIs) |
| SoftImpute hyperparameter selection | CV-like: mask 5% of non-missing entries, minimize imputation MSE |
| Dimensionality reduction of P | standard SVD; V_P used as input to Kronecker formulation |
| Affinity regression reformulation | (V_P (x) (U_D S_D)) * stack(W_DP) = logit(p(Y)) |
| Regularization tuning split | 10% of drugs held out per fold |
| Prediction comparison split | 20-fold CV over drugs, 5% held out per fold |
| Final r_P | 131 |
| Final r_D | 95 |
| Final lasso regularization | 1 |
| Null distribution size | 10,000 permutations of Y |
| Multiple-testing correction (drug-gene) | Benjamini-Yekutieli (nonindependent) |
| Multiple-testing correction (target enrichment) | Benjamini-Hochberg |
| Target databases | DrugBank; Therapeutic Targets Database |
| Therapeutic categorization | ATC codes (for visualization) |
| Clique detection | networkx; all fully connected cliques |
| Graph visualization | igraph (bipartite drug-gene) |

## Statistics (tests used)

- Spearman correlation (pairwise correlations and their cross-comparisons)
- Jaccard index / Jaccard distance (set-overlap measures on binary drug-phenotype and drug-disease-gene sets)
- Rank-sum test (Wilcoxon/Mann-Whitney; used to compare correlation distributions between drugs sharing vs not sharing targets, and to compare Jaccard distances for Draphnet vs nearest-neighbor predictions)
- Linear model (adjusting for the number of shared endpoints when relating endpoint correlation to Jaccard index)
- Hypergeometric test (target-level enrichment of disease genes)
- Empirical permutation test (10,000 Y permutations; 1,000 for clique-null)
- Benjamini-Yekutieli correction (drug-gene significance under dependence)
- Benjamini-Hochberg correction (target enrichment)
- Logistic regression with L1 (lasso) regularization (Draphnet fit)

## Figure observations summary

- Fig 1A: schematic — drug endpoint effects (pink) propagate through disease genes (green) to phenotypes (yellow), with the drug-phenotype relationship (dashed blue) explained by the learned green network shared across all drug-phenotype pairs.
- Fig 1B: Draphnet as affinity regression integrating D (ToxCast), P (PhenomeXcan), Y (SIDER).
- Fig 1C: disease-disease pair plot; x = Jaccard distance over drug overlap, y = Spearman correlation of PhenomeXcan profiles; Spearman = -0.11; p=4e-81 overall.
- Fig 2A: Jaccard distance between predicted and actual side-effect profiles — Draphnet lower than nearest-neighbor for majority of drugs (p=3e-8, rank-sum).
- Fig 2B: per-target -log10 p-values; true projection shifts targets toward larger -log10 p compared with null.
- Fig 2C: distributions of pairwise Spearman correlations among drugs sharing specific targets, comparing true vs null projections; stars mark significance thresholds.
- Fig 3A: empirical -log10 p-value calibration curve — true drug-target enrichments for disease-gene associations are systematically stronger than permuted null.
- Fig 3B: t-SNE of drug target-significance profiles with ATC annotations.
- Fig 3C: heatmap of drug-target-gene significance for selected drugs (green scale) with target annotations.
- Fig 4: bipartite drug-gene graph with colored cliques.
