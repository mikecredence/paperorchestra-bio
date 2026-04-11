# Experimental Log: Ketamine Multi-Dimensional Connectivity Signatures

## Study Design and Parameters

| Parameter | Value |
|-----------|-------|
| Design | Double-blind placebo-controlled crossover |
| N participants | 40 healthy adults |
| Ketamine bolus dose | 0.23 mg/kg |
| Ketamine continuous infusion rate | 0.58 mg/kg/hour |
| Imaging modality | Resting-state fMRI |
| Brain parcellation | 718 functionally-defined parcels |
| Connectivity metric | Global brain connectivity (GBC) |
| Primary analysis | PCA on delta-GBC (718 parcels x 40 subjects) |
| Behavioral assessments | PANSS (positive, negative, general), spatial working memory |
| Gene expression source | Allen Human Brain Atlas (AHBA) via GEMINI-DOT |
| Permutation test for PC significance | 5000 permutations, p < 0.05 |

## Experiment 1: PCA on Delta-GBC Neural Features

### Significant Principal Components

| PC | Variance Explained (%) | Significance | Correlation with Mean Delta-GBC |
|----|----------------------|--------------|-------------------------------|
| PC1 | >10 | p < 0.05 (permutation) | Significant (p < 0.001, Bonferroni) |
| PC2 | >10 | p < 0.05 (permutation) | Significant (p < 0.001, Bonferroni) |
| PC3 | ~5 | p < 0.05 (permutation) | Not significant |
| PC4 | ~5 | p < 0.05 (permutation) | Significant (p < 0.001, Bonferroni) |
| PC5 | ~5 | p < 0.05 (permutation) | Not significant |
| Total (PCs 1-5) | 42.1 | -- | -- |

- Fig 1A shows screeplot of % variance explained by first 31 (out of 39) delta-GBC PCs, with first 5 PCs identified as significant
- Fig 1B shows correlations between each significant PC map and the mean delta-GBC map; PC1, PC2, and PC4 are significantly correlated with the mean map
- Fig 1D shows unthresholded PC1 delta-GBC map across cortical surface

### Observations on Bi-Directionality

- All 5 PCs are bi-directional: extreme positive and negative loaders show opposite GBC change patterns
- High positive PC1 loaders show increased GBC in association networks (default mode) and decreased GBC in sensory cortices (secondary visual)
- High negative PC1 loaders show the reverse pattern
- This bi-directionality explains contradictory findings in the ketamine resting-state literature

## Experiment 2: Effective Dimensionality Comparison Across Substances

| Substance | Effective Dimensionality (mean +/- SD) | Comparison |
|-----------|---------------------------------------|------------|
| Ketamine | 12.8 +/- 0.7 | Reference |
| LSD | 8.7 +/- 0.3 | p < 0.001 vs ketamine |
| Psilocybin | 8.6 +/- 0.3 | p < 0.001 vs ketamine |
| LSD vs Psilocybin | -- | p = 0.6 (not significant) |

| Statistical Test | Result |
|-----------------|--------|
| One-way ANOVA | F(2,60) = 564, p < 0.001 |
| Post hoc: ketamine vs LSD | p < 0.001 |
| Post hoc: ketamine vs psilocybin | p < 0.001 |
| Post hoc: LSD vs psilocybin | p = 0.6 |

- Fig 1C shows bar plots of effective dimensionality across three pharmacological conditions
- Ketamine shows substantially higher dimensionality than both classical psychedelics
- No difference between LSD and psilocybin

## Experiment 3: Gene Expression Analysis (PC1 Delta-GBC Map)

### Gene Analysis Workflow

| Step | Description |
|------|-------------|
| 1 | Select neural target map (PC1 delta-GBC) |
| 2 | Obtain gene expression maps from AHBA using GEMINI-DOT |
| 3 | Map expression patterns from 6 postmortem brains onto cortical surface |
| 4 | Compute spatial correlation between PC1 map and each gene's expression pattern |
| 5 | Rank ~17,000 genes by spatial correlation |
| 6 | Perform gene set enrichment analysis |

### Key Gene Expression Correlation Results

| Gene / Gene Class | Spatial Correlation with PC1 Delta-GBC | Direction |
|-------------------|----------------------------------------|-----------|
| SST (somatostatin) | Significant positive | SST interneuron marker tracks PC1 |
| PVALB (parvalbumin) | Significant positive | PVALB interneuron marker tracks PC1 |
| Glutamate receptor genes | Varied | Some show correlation |
| GABA receptor genes | Varied | Some show correlation |

- Fig 2 shows the gene analysis workflow and the spatial match between PC1 delta-GBC and SST/PVALB expression
- SST and PVALB are markers for GABAergic interneuron subtypes that are known to preferentially express specific NMDA receptor subunits
- This finding links ketamine's NMDA antagonism to specific cell types via systems-level connectivity changes

### Interpretive Hypotheses for Multi-Dimensional PCs

| Hypothesis | PC Interpretation |
|-----------|-------------------|
| Synapse type | One PC reflects effects on excitatory-excitatory (E-E) synapses, another on excitatory-inhibitory (E-I) synapses |
| Receptor affinity | One PC reflects high-affinity actions on GluN2C/GluN2D receptors, another reflects lower-affinity actions on GluN2A/GluN2B |
| Multiple targets | Different PCs driven by ketamine's numerous downstream molecular targets beyond NMDA |

## Experiment 4: Behavioral PCA

### Behavioral Measures Under Placebo and Ketamine

| Measure | Placebo (mean) | Ketamine (mean) | Effect Size (Cohen's d) |
|---------|---------------|-----------------|------------------------|
| PANSS Positive | Lower | Higher | Reported in Fig 3A |
| PANSS Negative | Lower | Higher | Reported in Fig 3A |
| PANSS General | Lower | Higher | Reported in Fig 3A |
| Spatial Working Memory | Higher | Lower | Reported in Fig 3A |

- Fig 3A shows mean raw scores (left) and distributions of normalized scores (right) for placebo vs ketamine across all four behavioral domains
- All measures show significant ketamine effects (indicated by ** in figure)

### Behavioral PCA Results

| Behavioral PC | Variance Captured | Key Loading Pattern |
|---------------|-------------------|---------------------|
| Behavioral PC1 | Largest share | Mixed loading across PANSS and cognition |
| Behavioral PC2 | Second share | Dissociable from PC1 |
| Behavioral PC3 | Third share | Additional dimension of symptom variation |

- Fig 3 shows the multi-dimensional behavioral effect of acute ketamine
- Behavioral PCs are significant by permutation testing
- Individual variation in behavioral PC scores is substantial

## Experiment 5: Neuro-Behavioral Mapping

### Mapping Behavioral PCs onto Neural Delta-GBC

| Analysis | Method | Key Finding |
|----------|--------|-------------|
| Neuro-behavioral PC1 | Regression of behavioral PC1 score onto delta-GBC map per subject (N=40) | Distinct spatial pattern of brain-behavior relationship |
| Neuro-behavioral PC2 | Same regression approach for behavioral PC2 | Different spatial pattern from PC1 |
| Single-subject resolution | Individual behavioral PC scores predict individual delta-GBC patterns | Resolvable at single-subject level |

- Fig 4A shows the neuro-behavioral PC1 map: Z-scored regression coefficients (behavioral PC1 score vs delta-GBC) across all 40 subjects
- Red/orange parcels indicate positive relationship between GBC and behavioral PC1 score
- Blue parcels indicate negative relationship
- Fig 4 demonstrates that lower-dimensional behavioral variation reveals robust neuro-behavioral mapping

### Neuro-Behavioral Map Properties

| Property | PC1 Neuro-Behavioral Map | PC2 Neuro-Behavioral Map |
|----------|-------------------------|-------------------------|
| Association cortex involvement | Present | Different pattern |
| Sensory cortex involvement | Present (opposite direction) | Different pattern |
| Thalamic involvement | Observed | Observed |
| Spatial overlap with neural PCs | Partially overlapping | Partially overlapping |

## Experiment 6: Individual Subject-Level Analysis

### Individual Variation in Behavioral and Neuro-Behavioral Scores

| Metric | Range | Distribution |
|--------|-------|--------------|
| Behavioral PC1 score (Z) | Wide range (negative to positive) | Approximately normal |
| Neuro-behavioral PC1 score (Z) | Wide range | Approximately normal |

- Fig 5A shows a bar plot of behavioral PC1 score for each of 40 participants, ordered and color-coded
- Blue bars indicate high negative behavioral PC1 loaders; yellow bars indicate high positive loaders
- Fig 5B shows neuro-behavioral PC1 scores per individual
- Individual subject maps demonstrate that neuro-behavioral relationships are resolvable at the single-subject level

### Exemplar Individual Subject Maps

| Subject Type | PC1 Delta-GBC Pattern | Behavioral Profile |
|-------------|----------------------|-------------------|
| High positive PC1 loader | Increased GBC in association networks, decreased in sensory | Higher PANSS positive symptoms |
| High negative PC1 loader | Decreased GBC in association networks, increased in sensory | Lower PANSS positive symptoms |
| Intermediate loader | Mixed pattern | Intermediate symptom profile |

## Supplementary Results

### PCA on Separate Placebo and Ketamine GBC (Fig S2)

| Condition | PCA Result |
|-----------|-----------|
| Placebo GBC | Separate PCA performed for comparison |
| Ketamine GBC | Separate PCA performed for comparison |
| Delta-GBC | 5 significant PCs (main analysis) |

### Remaining Significant PCs (Figs S3-S5)

| PC | Spatial Pattern | Variance Explained |
|----|----------------|--------------------|
| PC3 | Reported in supplement | ~5% |
| PC4 | Reported in supplement | ~5% |
| PC5 | Reported in supplement | ~5% |

### Extreme Loader Comparison (Fig S8)

| Feature | Positive PC1 Loaders | Negative PC1 Loaders |
|---------|---------------------|---------------------|
| Default mode GBC | Increased | Decreased |
| Secondary visual GBC | Decreased | Increased |
| Somatosensory GBC | Mixed | Mixed |

## Statistical Methods Summary

| Analysis | Test | Threshold |
|----------|------|-----------|
| PC significance | Permutation test (5000 permutations) | p < 0.05 |
| PC-mean map correlation | Pearson correlation, Bonferroni corrected | p < 0.001 |
| Effective dimensionality comparison | One-way ANOVA + post hoc | F(2,60) = 564, p < 0.001 |
| Gene expression correlation | Spatial correlation + enrichment analysis | FDR corrected |
| Neuro-behavioral mapping | Regression (behavioral PC score ~ delta-GBC) per subject | Z-scored coefficients |

## Key Conclusions from Data

1. Ketamine's neural effects are irreducible to a single dimension despite acting on a single molecular target (NMDA receptor)
2. The principal neural gradient maps onto SST and PVALB interneuron gene expression, suggesting cell-type-specific downstream effects
3. Behavioral symptom variation is also multi-dimensional and maps onto distinct neural gradients
4. These mappings are resolvable at the individual subject level, supporting the feasibility of personalized pharmacological biomarkers
5. Higher effective dimensionality of ketamine compared to classical psychedelics may relate to ketamine's broader receptor pharmacology or downstream effects
