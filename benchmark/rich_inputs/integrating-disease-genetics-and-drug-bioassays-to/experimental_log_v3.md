# Experimental Log: Mapping Drug Biology to Disease Genetics (Draphnet)

## Data Sources and Dimensions

| Matrix | Description | Dimensions | Source |
|--------|-------------|------------|--------|
| D | Drug endpoint profiles | 429 drugs x 1391 endpoints | EPA ToxCast/Tox21 |
| P | Disease gene associations | 10,027 genes x 197 phenotypes | PhenomeXcan (S-MultiXcan) |
| Y (side effects) | Drug-phenotype associations | 429 drugs x 197 phenotypes | SIDER |
| Y (indications) | Drug-phenotype associations | 429 drugs x 197 phenotypes | SIDER |
| UDSD | Reduced drug representation | Lower-rank decomposition of D | SoftImpute |

### Drug data characteristics
- Average endpoints assayed per drug: ~100 (of 1391 total)
- Drug-phenotype associations: binary (present or unrecorded)
- Drug endpoint data: Level 5 (fraction of models calling compound as "hit")

### Disease gene data
- Gene-based scores: |Phi^-1(multiXanP_gene,phenotype)| x sign_gene,phenotype
- Genes retained: top half most variably associated with phenotype (highest standard deviation)
- Final gene count: 10,027

---

## Initial Data Assessment (Figure 1)

### Drug similarity vs phenotype overlap

| Test | Metric | p-value |
|------|--------|---------|
| ToxCast similarity vs phenotype Jaccard index | Spearman correlation | p = 1e-22 |
| ToxCast similarity vs phenotype Jaccard (accounting for shared endpoints) | Linear model | p = 1.7e-43 |
| Drug pairwise similarity before vs after dimensionality reduction | Spearman correlation | 0.21 |

### Disease similarity vs drug overlap

| Test | Metric | p-value |
|------|--------|---------|
| PhenomeXcan similarity vs drug Jaccard index | Spearman correlation | p = 4e-81 |

Phenotype pairs with higher PhenomeXcan similarity have lower Jaccard distance (Spearman correlation = -0.11).

---

## Model Hyperparameters

| Parameter | Value |
|-----------|-------|
| Rank of P decomposition (rP) | 131 |
| Rank of D decomposition (rD) | 95 |
| Regularization (lasso logistic regression lambda) | 1 |
| Cross-validation drug holdout | 10% per fold |
| SoftImpute cross-validation holdout | 5% of non-missing values |
| Total cross-validation folds (prediction assessment) | 20 |
| Held-out drugs per fold (prediction) | 5% |

---

## Predictive Performance (Figure 2A)

### Side effect prediction

| Comparison | Metric | p-value | Test |
|------------|--------|---------|------|
| Draphnet vs nearest-neighbor baseline | Jaccard distance (predicted vs actual side effect profile) | p = 3e-8 | Wilcoxon rank sum test |

Draphnet outperforms baseline for a majority of drugs.

### Notable predictions (not in SIDER training data)
- Fludrocortisone: most strongly predicted non-indicated drug for eczema (oral corticosteroid; eczema typically treated by topical steroids)
- Methyclothiazide: highest ranked non-indicated drug for glaucoma (diuretic; glaucoma caused by fluid retention)
- Dasatinib: top predicted indications were cancers (despite primary indication leukemias not available in training matrix P)

---

## Drug Phenome Effect Matrix Analysis (Figure 2B-C)

### Drug target validation

| Test | p-value | Test type |
|------|---------|-----------|
| Drugs sharing targets vs not sharing: ToxCast similarity | p = 1e-28 | Wilcoxon rank sum test |

### True vs null phenome effect matrix
- For most drug targets: true projection improves ability to distinguish drugs sharing targets compared to null projection (Figure 2B)
- Null model: UDSD projected onto permuted interaction matrix
- Pairwise Spearman correlation of projections of drugs sharing targets: systematically higher in true vs null projection (Figure 2C)
- Significance indicated as "*****+" for p-value < 10^-5

---

## Drug-Disease Genome Matrix (Figure 3)

### Permutation-based significance assessment
- 10,000 permutations of Y
- For each permutation: retrain model and obtain null drug-disease genome matrix
- P-values adjusted using Benjamini-Yekutieli method (appropriate for non-independent hypotheses)
- Median disease genes per drug: 7

### Drug target enrichment for disease genes

| Parameter | Value |
|-----------|-------|
| DrugBank targets tested | 132 (shared by >=3 drugs) |
| Targets with significant disease gene associations | 28 (at adjusted p < 0.01) |
| Significance vs permuted targets | Figure 3A calibration plot |

### Selected drug-disease gene associations (Figure 3C)

| Disease gene | Associated drugs | Drug target | Biological rationale |
|-------------|-----------------|-------------|---------------------|
| PPM1M | Neuroleptic drugs | HTR2C (serotonin signaling) | Top PhenomeXcan gene for bipolar disorder; loci associated with schizophrenia; linked to rare mental illness |
| CETP | Fenofibrate, lipid metabolism drugs | PPARalpha agonists | Associated with high cholesterol in PhenomeXcan; experimentally supported as effector of fenofibrate and PPARalpha agonism |

### tSNE visualization (Figure 3B)
- Drugs in same therapeutic category cluster together
- Calcium channel blockers cluster in one area
- Anti-inflammatories and analgesics in another cluster

---

## Drug Categorization by Disease Genome (Figure 4)

### Network construction
- Drug pairs connected if sharing more disease genes than expected by chance
- Null distribution: 1000 simulations sampling random disease genes proportional to drug association frequency
- Fully connected cliques of >=3 drugs identified
- Disease genes filtered: associated with >=1 gene target and <15 total drugs

### Selected drug cliques

| Clique | Drugs | Shared biology |
|--------|-------|---------------|
| Anti-inflammatory cluster | Ketoprofen, ibuprofen, indomethacin + fenofibrate, bezafibrate | PPARalpha-agonists modulate inflammation |
| Anti-inflammatory extended | Above + pyridoxine (vitamin B-6) | Nutrient with anti-inflammatory effects |
| Calcium channel blocker cluster | Bepridil, verapamil + pimozide | Pimozide (psychiatric drug) known to cause arrhythmia |
| CNS/cardiovascular cluster | Mecamylamine, pindolol, gabapentin | Mecamylamine: discontinued antihypertensive with CNS effects; investigated for seizures |

---

## Model Formulation

### Core equation
DWPt = logit(p(Y))

### Reformulated with dimensionality reduction
(Vp x UDSD) x stack(WDP) = logit(p(Y))

### Drug phenome effect matrix
UDSD * WDP (maps each drug to compressed summary of effect across phenotypes)

### Drug-disease genome matrix
UDSD * WDP projected to gene space using inverses of SVD decomposition of P

---

## Methods Parameters

### PhenomeXcan processing
- GWAS source: UK Biobank
- Gene-based associations: S-PrediXcan combined across tissues via S-MultiXcan
- P-values converted to z-scores using inverse normal cumulative distribution
- Signs: consensus (majority) S-PrediXcan sign across tissues
- Phenotype matching: UMLS concept unique identifiers (CUIs)

### ToxCast processing
- Data level: Level 5 (fraction of models calling "hit")
- Dimensionality reduction: SoftImpute (SVD-based matrix completion)
- Hyperparameter selection: cross-validation setting 5% non-missing to missing

### Drug-drug network for categorization
- Pairwise significance: simulation-based (1000 iterations)
- Disease genes sampled proportional to drug association frequency
- Network library: networkx
- Clique detection: fully connected cliques
- Visualization: igraph (bipartite graph)

---

## Statistics Summary

1. **Spearman correlation** - Drug ToxCast similarity vs phenotype Jaccard index (p = 1e-22); PhenomeXcan similarity vs drug Jaccard (p = 4e-81); pairwise drug similarity before/after dimensionality reduction (r = 0.21; r = -0.11 for phenotype pairs)
2. **Linear model** - ToxCast similarity vs phenotype Jaccard accounting for shared endpoints (p = 1.7e-43)
3. **Wilcoxon rank sum test** - Draphnet vs baseline prediction (p = 3e-8); drugs sharing targets vs not sharing ToxCast similarity (p = 1e-28)
4. **Regularized logistic regression (lasso)** - Model training with lambda = 1
5. **SoftImpute** - Dimensionality reduction and matrix completion for sparse ToxCast data
6. **Singular value decomposition (SVD)** - Decomposition of PhenomeXcan matrix P
7. **Permutation test (10,000 permutations)** - Significance of drug-disease gene connections
8. **Benjamini-Yekutieli correction** - Multiple testing adjustment for non-independent drug-gene hypotheses
9. **Benjamini-Hochberg correction** - Multiple testing adjustment for target-gene enrichment
10. **Hypergeometric test** - Drug target enrichment for disease genes
11. **20-fold cross-validation** - Prediction performance assessment
12. **Simulation-based null distribution (1000 iterations)** - Drug-drug disease gene overlap significance
