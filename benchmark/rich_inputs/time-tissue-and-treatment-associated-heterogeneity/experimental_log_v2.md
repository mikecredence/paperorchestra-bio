# Experimental Log: mRegDC Heterogeneity in Tumours

## Human Cancer Survival Analysis (Extended Data Fig 1)

### TCGA Cohorts

| Cancer Type | n | mRegDC Signature vs Survival |
|------------|---|------------------------------|
| Skin cutaneous melanoma (SKCM) | 473 | Improved (Kaplan-Meier, log-rank) |
| Colorectal adenocarcinoma (COAD) | 521 | Improved |
| Breast invasive carcinoma (BRCA) | 1,226 | Improved |
| Lung adenocarcinoma (LUAD) | 598 | Improved |
| Total analysed | 4,045 | -- |

### METABRIC Breast Cancer Subtypes (Extended Data Fig 1H)

| Subtype | n | mRegDC Association |
|---------|---|-------------------|
| HR+ (ER or PR) | 1,369 | Subtype-specific |
| HER2+ | 185 | Subtype-specific |
| Triple-negative (TNBC) | 299 | Subtype-specific |
| Total | 1,853 | -- |

## Human scRNA-seq Datasets Analyzed

| Cancer Type | GEO/Accession | Patients | Key Finding |
|------------|---------------|----------|-------------|
| Colorectal cancer | GSE178341 | 62 | CCR7+ mRegDCs express PD-L1, PD-L2 |
| Breast cancer | EGAS00001004809 | 29 | mRegDC cluster identified |
| Melanoma | GSE123139 | 25 | mRegDC cluster identified |

## Mouse Tumour Models

| Parameter | Value |
|-----------|-------|
| Cell lines | MC38, MC38-Ova, CT26 |
| Mouse strains | C57BL/6 Kaede, BALB/c Kaede |
| Injection | 2.5e5 cells subcutaneous, left flank |
| Anti-PD-L1 | Clone 80, 200 ug IP, days 7, 10, 13 |
| Isotype control | NIP228 mouse IgG1, same schedule |
| Harvest day | 13, 14, 15, or 16 (5h, 24h, 48h, 72h post-photoconversion) |
| Volume formula | V = 0.5 * a * b^2 |
| Housing | 21C, 55% humidity, 12h light-dark |

## Photoconversion Tracking Results

### mRegDC Migration to dLN (Fig 2)

| Time Post-Conversion | Kaede-Red mRegDCs in dLN | Interpretation |
|---------------------|-------------------------|----------------|
| 5h | Detectable | Early emigrants |
| 24h | Increased | Active migration |
| 48h | Peak | -- |
| 72h | Maintained/declining | -- |

### Tumour-Retained mRegDCs

| Observation | Detail |
|-------------|--------|
| CCR7+ mRegDCs in tumour | Present at all time points |
| Key finding | A subset of mRegDCs remains in tumour despite CCR7 expression |
| Cannot be labeled "migratory DC" | Not all CCR7+ DCs migrate |

### mRegDC to cDC Ratio Over Time (Extended Data Fig 3C)

| Model | Time Course | Statistical Test |
|-------|-------------|-----------------|
| MC38 | Ratio increases with time | One-way ANOVA with Sidak's |
| CT26 | Similar trend | One-way ANOVA with Sidak's |

## Transcriptional Heterogeneity of mRegDCs (Fig 1, 3)

### scRNA-seq Clusters

| Cluster | Location | Characteristics |
|---------|----------|-----------------|
| mRegDC_1 | Tumour (recent arrivals) | High antigen presentation, pro-inflammatory |
| mRegDC_2 | Tumour (intermediate) | Intermediate phenotype |
| mRegDC_3 | Tumour (prolonged residence) | Reduced MHC-II, Cd74, cytokine transcripts |
| mRegDC (dLN) | Draining lymph node | Distinct from all tumour clusters |

### Temporal Trajectory (Fig 3A-C)

| Gene Category | Trend with Tumour Dwell-Time |
|--------------|------------------------------|
| MHC-II transcripts | Progressive reduction |
| Cd74 | Progressive reduction |
| Antigen processing/presentation (GO:0002468) | Reduced in mRegDC_3 vs mRegDC_1 |
| Pro-inflammatory cytokines | Progressive reduction |
| Co-inhibitory molecules (PD-L1) | Maintained/increased |

Wilcoxon rank-sum test used for gene signature score comparisons between clusters.

### Tumour vs dLN mRegDC Comparison (Extended Data Fig 4)

| Feature | Tumour mRegDCs | dLN mRegDCs |
|---------|---------------|-------------|
| Lymphocyte co-stimulation (GO:0031294) | Lower | Higher (GSEA enriched) |
| MHC-II expression | Variable by cluster | Higher |
| Phenotype | Heterogeneous, time-dependent | More uniform |

## Anti-PD-L1 Treatment Effects (Fig 3, Extended Data Fig 6)

### Tumour Growth

| Treatment | Effect | n per group |
|-----------|--------|-------------|
| Anti-PD-L1 | Reduced tumour growth | 5 mice (scRNA-seq experiment) |
| Isotype | Normal growth | 5 mice |

### mRegDC Transcriptional Changes After Anti-PD-L1

| Pathway (GSEA) | Direction | Significance |
|----------------|-----------|-------------|
| Hallmark IFN-gamma response | Upregulated | P-adj < 0.05 |
| Hallmark inflammatory response | Upregulated | P-adj < 0.05 |
| KEGG antigen processing/presentation | Upregulated | P-adj < 0.05 |

### Key Molecules Upregulated by Anti-PD-L1

| Molecule | Function | Change |
|----------|----------|--------|
| OX40L (Tnfsf4) | T cell co-stimulation | Increased |
| CD80 | Co-stimulation | Maintained high |
| PVR | TIGIT ligand | Increased |
| Lymphocyte stimulatory molecules | Multiple | Enriched state |

### RNA Velocity (Extended Data Fig 6C)

| Treatment | Trajectory |
|-----------|-----------|
| Isotype | mRegDCs progress toward exhausted state |
| Anti-PD-L1 | Trajectory skewed toward stimulatory state |

## mRegDC-CD8+ T Cell Interaction (Fig 4)

### Cell Proportion Correlations (TCGA, Fig 4A)

| Cancer | mRegDC-CD8+ T Cell Correlation | Significance |
|--------|-------------------------------|-------------|
| Colorectal (COAD, n=521) | High positive Pearson r | p < 0.05 |
| Breast (BRCA) | Positive | p < 0.05 |
| Melanoma (SKCM) | Positive | p < 0.05 |

### mRegDC Signature vs CD8+ Effector Signature (Fig 4B)

| Cancer | Pearson Correlation | Significance |
|--------|-------------------|-------------|
| COAD | Positive | Significant |
| BRCA | Positive | Significant |
| SKCM | Positive | Significant |

### Spatial Co-Localization

| Species | Tissue | Finding |
|---------|--------|---------|
| Human | Solid tumours | mRegDCs co-localize with PD-1+CD8+ T cells |
| Mouse | MC38-Ova tumours | mRegDCs co-localize with PD-1+CD8+ T cells |

## OX40L Functional Studies

| Experiment | Result |
|-----------|--------|
| OX40L reporter mice | mRegDCs express OX40L in tumours |
| CD11c-Cre OX40L-fl/fl | DC-specific OX40L deletion |
| OX40L+ mRegDC + CD8+ T cells | Augmented cytolytic activity |
| Anti-PD-L1 + OX40L | Potential synergistic mechanism |

## Additional Mouse Strains Used

| Strain | Purpose |
|--------|---------|
| C57BL/6 Kaede | Photoconversion tracking |
| BALB/c Kaede | CT26 tumour model |
| OX40L+/Human-CD4 reporter | OX40L expression tracking |
| OX40Lfl/fl | Conditional deletion |
| CD11c-Cre OX40Lfl/fl | DC-specific OX40L knockout |

## Key Figure Observations

- Extended Data Fig 1A: Kaplan-Meier curves show improved survival with high mRegDC signature across 4 cancer types
- Extended Data Fig 1B-G: UMAPs of myeloid cells from human cancer scRNA-seq showing mRegDC clusters
- Fig 1B: UMAP of tumour myeloid cells from scRNA-seq at 48h post-photoconversion
- Fig 1C-D: DC cluster identification with canonical markers
- Fig 1E: Kernel density embedding by Kaede color and time shows mRegDC temporal dynamics
- Extended Data Fig 3: PAGA and RNA velocity show maturation trajectory in tumour DCs
- Fig 2A: Flow cytometry of tumour-dLN showing Kaede-red DC emigrants
- Fig 2B: Time course of Kaede-red mRegDC proportion in dLN
- Fig 3A: MHC-II and Cd74 expression decrease over pseudotime in tumour DCs
- Fig 3B-C: Gene signature scores show progressive functional decline with tumour residence
- Extended Data Fig 6: GSEA shows IFN-gamma, inflammatory, and antigen presentation pathways upregulated by anti-PD-L1
- Fig 4A: Correlation matrix from TCGA deconvolution highlights mRegDC-CD8+ T cell axis
- Fig 4B: mRegDC and CD8+ effector signatures positively correlated across cancers

## Datasets and Methods Summary

| Resource | Detail |
|----------|--------|
| TCGA | 4,045 bulk transcriptomes |
| METABRIC | 1,853 breast tumours |
| scRNA-seq (mouse) | MC38-Ova tumours, Kaede-green/red sorted |
| scRNA-seq (human) | CRC, breast, melanoma published datasets |
| Flow cytometry | Multi-parameter panel for DC subsets |
| Multiplex IF | Spatial co-localization |
| Photoconversion | 405 nm light exposure to tumour |
| Statistical tests | Wilcoxon rank-sum, one-way ANOVA with Sidak's, log-rank, Pearson correlation |
