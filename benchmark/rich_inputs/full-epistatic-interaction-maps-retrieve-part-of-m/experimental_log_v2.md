# Experimental Log

> Pre-writing data tables and observations for the Next-Gen GWAS epistatic interaction study.

---

## Datasets Used

| Dataset | Source | SNPs (raw) | SNPs (after MAF filter) | Ecotypes | Phenotypes |
|---------|--------|-----------|------------------------|----------|-----------|
| 1001 Genomes Arabidopsis | Genotype matrix from 1001 Genome Project | 9,124,892 | 346,094 (Campos) / 341,067-371,956 (Atwell) | 1,135 | Multiple |
| Atwell et al. (2010) | Published Arabidopsis GWAS data | 9,124,892 | 341,067-371,956 | 1,135 | Flowering time + others |
| Campos et al. (2021) | Arabidopsis ionomics | 9,124,892 | 346,094 | 1,135 | 18 elemental concentrations (ICP-MS) |

---

## Computational Resources

| Component | Specification |
|-----------|--------------|
| Server | PowerEdge T640 DELL |
| RAM | 377 GB |
| GPUs | 4x NVIDIA Quadro RTX 6000 (24 GB each) |
| Software | R (simulations), custom GPU code |
| Code repository | https://github.com/CarluerJB |
| Computation time | Hours (vs. years for conventional approaches) |

---

## MAF Filtering Parameters

| Parameter | Value |
|-----------|-------|
| MAF threshold | > 0.3 |
| SNPs retained (Campos 2021) | 346,094 |
| SNPs retained (Atwell 2010, range) | 341,067 - 371,956 |
| Total pairwise combinations | ~61.2 billion |

---

## Experiment 1: Simulation Validation of NGG

Fig. 1: Simulated genotype and phenotype data with specific modulable parameters. 100 SNPs on each axis (Var1, Var2). The z-axis reports estimated theta of simple SNPs (diagonal) and pairwise combinations (off-diagonal triangle). Random noise added.

| Simulation Component | Details |
|---------------------|---------|
| Number of SNPs simulated | 100 x 100 |
| Simulated signals | 5 epistatic interactions |
| Noise | Random noise added |
| Recovery | NGG retrieves all 5 simulated signals (panels A and B) |
| False positives | Minimal under simulation conditions |

Fig. 1A-B: NGG correctly recovers the 5 planted epistatic signals from the noisy simulated data, demonstrating the method works as intended before application to real data.

---

## Experiment 2: 1D-GWAS Benchmarking - NGG vs. EMMA

Fig. 2A: Comparison of NGG and EMMA algorithms on Atwell et al. (2010) data. Both methods retrieve largely similar 1D signals.

| Method | Type | Key Signal Retrieved | Concordance |
|--------|------|---------------------|-------------|
| NGG (diagonal of 2D map) | Novel GPU-accelerated | FLC locus for flowering | High |
| EMMA (mixed model) | Standard of practice | FLC locus for flowering | Reference |

Fig. 2B: Phenotype 48 (days to flowering trait, 8W vernalization) NGG results. SNPs near the FLC locus (major flowering time gene) are prominently detected.

| Phenotype | ID | Method | FLC Locus Detected |
|-----------|----|---------|--------------------|
| Days to flowering (8W) | 48 | NGG | Yes, SNPs in close vicinity |
| Days to flowering (8W) | 48 | EMMA | Yes |
| Flowering time (FT10) | 31 | NGG | Yes |
| Flowering time (FT10) | 31 | EMMA | Yes |

---

## Experiment 3: Direct SNP Effect Estimation

Fig. 3: NGG provides a direct estimation of each SNP's effect (theta) on the phenotype, with Col-0 as the reference genome.

| Plot | Content | Key Feature |
|------|---------|-------------|
| Upper plot | NGG signal: support x absolute value of estimated effect | Combined metric |
| Lower plot | Estimated effect of each SNP (signed theta) | Direction of effect visible |
| Colored points | Signals emerging from noise in bootstrap procedure | Robust signals only |

---

## Experiment 4: Full 2D Epistatic Maps

Fig. 4: 2D-NGG results providing estimation of 61.2 billion SNP combination effects.

| Panel | Phenotype | Dataset | Presentation |
|-------|-----------|---------|-------------|
| A | Days to flowering (FT10, phenotype ID 31) | Atwell et al. (2010) | Heatmap + histogram |
| B | Phosphorus content (ICP-MS) | Campos et al. (2021) | Heatmap + histogram |

| Phenotype | Total Pairwise Interactions Evaluated | Map Resolution |
|-----------|--------------------------------------|----------------|
| FT10 (flowering time) | ~61.2 billion | Gene-level |
| Phosphorus content | ~61.2 billion | Gene-level |

The heatmaps display epistatic interaction strength between SNP pairs. Histograms show the distribution of interaction effect sizes.

---

## Experiment 5: Heritability Estimation - 1D vs. 1D+2D

Fig. 5A: Analysis scheme. Blue diagonal = 1D-GWAS signals. Orange triangle = 2D-NGG epistatic interactions representing 61 billion combinations.

Fig. 5B: Heritability (h2, measured as adjusted R-squared) plotted against increasing number of PCA components.

| Signal Source | Label | h2 Trend |
|--------------|-------|----------|
| 1D-GWAS only (diagonal) | V data points | Increases then plateaus at lower h2 |
| 1D-GWAS + 2D-NGG (diagonal + triangle) | W data points | Increases further, higher plateau |

| Comparison | Observation |
|-----------|-------------|
| 1D-only vs. 1D+2D at same PCA count | 2D signals substantially increase explained variance |
| Marginal gain from epistasis | Large for most phenotypes tested |
| Interpretation | Missing heritability partly recovered through epistatic interactions |

---

## Experiment 6: Machine Learning Phenotype Prediction

Fig. 6A: Each dot represents a given ML model trying to predict a given phenotype using different learning data inputs.

| ML Model | Type |
|----------|------|
| SVM | Support Vector Machine |
| RF | Random Forest |
| DNN | Deep Neural Network |
| GP | Gaussian Processes |
| LASSO | L1-regularized regression |
| Elastic-Net | Combined L1/L2 regularization |

| Input Configuration | Number of Classes | Number of SNPs | Signal Source |
|--------------------|------------------|----------------|--------------|
| Config 1 | 3 | 50 | 1D only |
| Config 2 | 3 | 100 | 1D only |
| Config 3 | 3 | 500 | 1D only |
| Config 4 | 3 | 1000 | 1D only |
| Config 5 | 5 | 50 | 1D only |
| Config 6 | 5 | 100 | 1D only |
| Config 7 | 5 | 500 | 1D only |
| Config 8 | 5 | 1000 | 1D only |
| Config 9 | 3 | 50 | 1D + 2D |
| Config 10 | 3 | 100 | 1D + 2D |
| Config 11 | 3 | 500 | 1D + 2D |
| Config 12 | 3 | 1000 | 1D + 2D |
| Config 13 | 5 | 50 | 1D + 2D |
| Config 14 | 5 | 100 | 1D + 2D |
| Config 15 | 5 | 500 | 1D + 2D |
| Config 16 | 5 | 1000 | 1D + 2D |

| Phenotype Category | Number of Phenotypes | Measurement Method |
|-------------------|---------------------|-------------------|
| Elemental concentrations | 18 | ICP-MS on Arabidopsis leaves |

---

## Experiment 6 (continued): ML Prediction Results Summary

| Comparison | Observation |
|-----------|-------------|
| 1D-only SNPs vs. 1D+2D SNPs | Epistatic signal markers improve prediction accuracy |
| Across all 6 ML models | Consistent improvement with 2D inputs |
| Across 18 phenotypes | Improvement seen across most elemental concentrations |
| Effect of number of SNPs | More SNPs generally improve prediction, but 2D markers add value even at low SNP counts |
| Effect of class count | 3-class prediction easier than 5-class, but relative improvement from 2D similar |

Fig. 6A: Dot plot shows that including 2D-NGG epistatic markers shifts prediction accuracy upward across all model-phenotype-configuration combinations.

---

## Phenotype Details

| Phenotype | Source | Measurement |
|-----------|--------|-------------|
| Days to flowering (FT10) | Atwell et al. 2010, phenotype ID 31 | Days from planting to flowering at 10C |
| Days to flowering (8W) | Atwell et al. 2010, phenotype ID 48 | Days from planting to flowering after 8 weeks vernalization |
| Phosphorus (P) | Campos et al. 2021 | ICP-MS leaf elemental concentration |
| 17 additional elements | Campos et al. 2021 | ICP-MS leaf elemental concentrations |

---

## Key Known Loci Recovered

| Locus | Gene | Phenotype | Method |
|-------|------|-----------|--------|
| FLC | FLOWERING LOCUS C | Flowering time | Both NGG and EMMA |

Fig. 2B confirms that NGG 1D signal peaks near FLC, validating the method against known biology.

---

## Bootstrap Procedure

| Parameter | Description |
|-----------|-------------|
| Purpose | Distinguish real signals from noise |
| Output | Colored data points in Fig. 3 represent robust signals |
| Application | Applied to both 1D and 2D analyses |
| Details | Described in Supplementary Material 1 |

---

## Scalability Comparison

| Approach | Pairwise Evaluation Time | Scalability |
|----------|------------------------|-------------|
| Standard GWAS + HPC | Years for full combinatorial space | Poor |
| NGG (GPU-accelerated) | Hours | Practical on single server |
| EMMA (mixed model) | Feasible for 1D only | Not scalable to 2D |

---

## Overall Conclusions from Data

1. NGG can evaluate over 60 billion pairwise SNP interactions within hours on a single multi-GPU server, making full epistatic mapping practical.
2. 1D-GWAS results from NGG are concordant with the standard EMMA mixed model approach, validating the method.
3. 2D epistatic maps at gene resolution reveal substantial interaction structure beyond single-locus signals.
4. A large proportion of missing heritability is recovered when epistatic interactions are included (higher adjusted R-squared with 1D+2D vs. 1D alone).
5. Machine learning phenotype prediction improves consistently when epistatic markers are added to the input features, across six ML model types and 18 ionomic phenotypes.
6. The method generalizes across different phenotype types (flowering time, elemental concentrations) and datasets.
