# Experimental Log

> Pre-writing data tables and observations for the bilinear model study on neuronal type connectivity.

---

## Datasets Used

| Dataset | Organism | Data Type | Description |
|---------|----------|-----------|-------------|
| C. elegans neuronal dataset | C. elegans | Gene expression + connectivity | Innexin gene expression per neuron; gap junction connectivity matrix between individual neurons |
| Mouse retinal neuronal dataset | Mouse | Transcriptomic (scRNA-seq) + connectomic | BC and RGC type-level gene expression from single-cell transcriptomics; BC-RGC connectivity from serial EM connectomics |
| BC type correspondence | Mouse | Cell type mapping | Mapping of BC types across different nomenclatures (Supplementary File 1) |
| RGC type correspondence | Mouse | Cell type mapping | Mapping of RGC types across different nomenclatures (Supplementary Files 2-3) |

---

## Baselines and Methods Compared

| Method | Type | Key Feature | Approach |
|--------|------|-------------|----------|
| Bilinear model (this work) | Latent factor model | Factorizes rule matrix into A and B | Collaborative filtering analogy; learns two transformation matrices |
| Spatial Connectome Model (SCM) | Regression model | Full rule matrix O | Represents connectome as edge list; regresses on Kronecker product of gene expression |

---

## Experiment 1: C. elegans Gap Junction Connectivity Reconstruction

### Setup
- Task: Reconstruct electrical synapse (gap junction) connectivity from innexin gene expression
- Input: Innexin expression profiles for each C. elegans neuron
- Target: Observed gap junction connectivity matrix (binary/weighted)
- Spatial constraints: Physical contact between neurons incorporated into weight matrix
- Model is generalized to single-cell level by treating each neuron as a type (ni = nj = 1)

### Hyperparameter Selection (C. elegans)

| Parameter | Range Tested | Selected Value |
|-----------|-------------|----------------|
| Lambda (regularization) | 1e-8, 1e-6, 1e-4, 1e-2, 1 | Determined via cross-validation (Fig. S1) |
| Latent dimensionality | 2, 4, 6, 8, 10, 12, 14, 16 | Determined via cross-validation (Fig. S1) |

Fig. 2-Supplement 1A shows a heatmap of log10(validation loss) across the lambda-dimensionality grid. Figs. 2-Supplement 1B and 1C show marginal plots of validation loss against lambda and dimensionality respectively.

### ROC Analysis: Bilinear Model vs. SCM

| Method | ROC-AUC | Notes |
|--------|---------|-------|
| Bilinear model | Comparable to or slightly higher than SCM | See Fig. 2D |
| SCM (from prior work) | Baseline | See Fig. 2D |
| Chance level | 0.50 | Dashed line in Fig. 2D |

Fig. 2A shows the connectivity matrix predicted by the bilinear model. Fig. 2B shows the connectivity matrix from the SCM. Fig. 2C shows the observed (ground truth) gap junction connectivity matrix. Color spectrum runs from red (strong connections) to gray (weak/no connections). Fig. 2D shows the ROC curves for both methods, with the bilinear model performing comparably to, if slightly better than, the SCM.

### Rule Matrix Comparison

| Matrix | Source | Dimensions | Key Observation |
|--------|--------|------------|-----------------|
| AB^T (bilinear) | This work | Innexin-by-innexin | Captures all major entries from SCM rule matrix plus additional entries |
| O (SCM) | Prior work | Innexin-by-innexin | Established innexin interaction rules |

Fig. 3A displays the rule matrix AB^T from the bilinear model. Fig. 3B displays the rule matrix O from the SCM. Black boxes highlight entries with substantial differences between the two matrices, indicating additional genetic interactions inferred by the bilinear model that were not captured by the SCM.

### Computational Efficiency Comparison

| Model | Property | Advantage |
|-------|----------|-----------|
| Bilinear model | Factorized (A, B separate) | Lower parameter count; more computationally efficient; naturally extensible to deep learning |
| SCM | Full rule matrix O | Higher parameter count; less scalable |

---

## Experiment 2: Mouse Retinal BC-RGC Connectivity Reconstruction

### Setup
- Task: Reconstruct synaptic connectivity between bipolar cell (BC) types and retinal ganglion cell (RGC) types from gene expression
- Pre-synaptic: BC type gene expression profiles (from scRNA-seq)
- Post-synaptic: RGC type gene expression profiles (from scRNA-seq)
- Target: BC-RGC connectivity matrix (from serial EM connectomic data)
- Data alignment: Transcriptomic and connectomic data from different sources, matched at the cell-type level

### Hyperparameter Selection (Mouse Retina)

| Parameter | Range Tested | Selected Value |
|-----------|-------------|----------------|
| Lambda (regularization) | 0.1, 1, 10, 100 | Determined via cross-validation (Fig. S2) |
| Latent dimensionality | 1, 2, 3, 4, 8 | 2 (based on cross-validation; Fig. S2) |

Fig. 4-Supplement 1A shows a heatmap of log10(validation loss) across the lambda-dimensionality grid. Figs. 4-Supplement 1B and 1C show the marginal plots.

### Connectivity Reconstruction Quality

| Metric | Observation |
|--------|-------------|
| Overall pattern match | Reconstructed matrix (Fig. 4A) closely mirrors the observed connectivity matrix (Fig. 4B) |
| Color encoding | Dark red = strong connection; dark blue = weak/no connection |
| Known motifs recapitulated | ON and OFF pathway connectivity motifs between BCs and RGCs |

Fig. 4A shows the reconstructed connectivity matrix from the bilinear model. Fig. 4B shows the observed connectivity matrix from connectomic data. The model successfully recapitulates recognized connectivity patterns between BC and RGC types.

---

## Experiment 3: Latent Dimension Analysis of Connectivity Motifs

### Two-Dimensional Latent Space

| Latent Dimension | Connectivity Motif | BC Grouping |
|-----------------|-------------------|-------------|
| Dimension 1 | Captures one major connectivity pattern | Separates BC types along one axis in latent space |
| Dimension 2 | Captures a second, orthogonal connectivity pattern | Separates BC types along the other axis |

Fig. 5A shows the reconstructed connectivity using only latent dimension 1. Fig. 5B shows the reconstructed connectivity using only latent dimension 2. Each dimension captures a distinct connectivity motif.

### BC Types in Latent Feature Space

| BC Type Group | Position in Latent Space | IPL Stratification Pattern |
|--------------|------------------------|---------------------------|
| Group 1 (positive dim 1) | Upper-right quadrant | Specific IPL sublayer stratification |
| Group 2 (negative dim 1) | Lower-left quadrant | Different IPL sublayer stratification |
| Group 3 (positive dim 2) | Upper-left quadrant | Yet another IPL pattern |
| Group 4 (negative dim 2) | Lower-right quadrant | Distinct from above |

Fig. 5C plots each BC type in the 2D latent feature space, with dashed lines at zero for each dimension. Figs. 5D and 5E show the stratification profiles of BC types in the inner plexiform layer (IPL), color-coded by their position along latent dimension 1 (Fig. 5D) or dimension 2 (Fig. 5E).

---

## Experiment 4: Gene Signature Analysis

### Top Genes per Latent Dimension

| Latent Dimension | Number of Top Genes Analyzed | Cell Types Profiled | Visualization |
|-----------------|-----------------------------|--------------------|---------------|
| Dimension 1 | 50 | BCs (Fig. 6A) and RGCs (Fig. 6B) | Weight value (color: red positive, blue negative; saturation: magnitude) + expression (dot size: % expressing; color saturation: mean expression) |
| Dimension 2 | 50 | BCs and RGCs | Same as above |

Fig. 6A-B show the weight vectors of the top 50 genes for latent dimension 1, along with their expression patterns in BC types (6A) and RGC types (6B). The sign and magnitude of the weight value are encoded in color and saturation. Expression level is encoded by dot size (fraction of cells expressing) and color saturation (mean expression level).

### Gene Ontology (GO) Enrichment

| Latent Dimension | Cell Type | GO Categories Enriched | Key Functional Terms |
|-----------------|-----------|----------------------|---------------------|
| Dimension 1 | BCs | Cell adhesion, synapse formation | Cell-cell adhesion molecules, synaptic membrane proteins |
| Dimension 1 | RGCs | Synapse organization | Synaptic signaling genes |
| Dimension 2 | BCs | Cell adhesion, axon guidance | Guidance molecules, adhesion factors |
| Dimension 2 | RGCs | Synaptic transmission | Neurotransmitter receptor genes |

Supplementary File 4 contains the full list of GO terms associated with each latent dimension for both BC and RGC gene sets. The identified genes include those important for cell-cell adhesion and synapse formation, consistent with their roles in orchestrating specific synaptic connections.

---

## Experiment 5: Prediction of BC Partners for Transcriptomically Defined RGC Types

### Setup
- RGC types with known connectivity were used for training
- Transcriptomically defined RGC types (from Tran et al.) with unknown connectivity were projected into the same latent space

### Projection Results

| RGC Category | Number of Types | Projection Method |
|-------------|-----------------|-------------------|
| Known connectivity RGCs | Training set | Direct fit |
| Transcriptomically defined RGCs (unknown connectivity) | Multiple types (named per Tran et al.) | Projected into learned latent space |

Fig. 7A shows the projection of transcriptomically defined RGC types into the same latent space as RGC types with known connectivity. Fig. 7B shows the resulting predicted connectivity matrix between these RGC types and BC types.

### Prediction Validation

| Validation Approach | Result |
|--------------------|--------|
| Comparison with functional descriptions | Predictions substantially aligned with known functional properties of the RGC types from prior studies |
| Supplementary File 5 | Full list of predicted BC partners for each transcriptomically defined RGC type |

---

## Experiment 6: Model Properties and Extensions

### Relationship Between Bilinear Model and SCM

| Property | Bilinear Model | SCM |
|----------|---------------|-----|
| Rule matrix | AB^T (factorized, low-rank) | O (full rank) |
| Parameter count | Lower (determined by latent dimensionality) | Higher (full innexin-by-innexin or gene-by-gene) |
| Spatial constraints | Incorporated via weight matrix W | Incorporated via physical contact requirement |
| Scalability | More efficient; extensible to deep learning | Less scalable |
| Interpretability | Latent dimensions map to biological motifs | Rule matrix entries map to gene pairs |

### Proposed Future Extension (Fig. 8)

| Component | Description |
|-----------|-------------|
| Two-tower deep learning model | Pre- and post-synaptic gene expressions transformed via separate deep neural networks into latent embeddings |
| Connectivity prediction | Inner product of the two latent embeddings |
| Advantage | Can capture nonlinear relationships between gene expression and connectivity |

Fig. 8A illustrates the two-tower architecture: gene expression profiles of pre- and post-synaptic neurons are independently transformed into latent embedding representations via deep neural networks, and connectivity is predicted by the inner product of these embeddings.

---

## Summary of Key Figure Observations

| Figure | Key Observation |
|--------|----------------|
| Fig. 1A | In the ideal scenario, transformation matrices A and B directly relate per-cell gene expression to per-cell connectivity |
| Fig. 1B | In the practical scenario, type-averaged gene expressions and connectivity are used, with transformation matrices learned at the type level |
| Fig. 2A-C | Bilinear model prediction, SCM prediction, and ground truth connectivity matrices show high visual similarity |
| Fig. 2D | ROC curves for bilinear model and SCM are nearly overlapping, with bilinear slightly better |
| Fig. 3A-B | Rule matrices from bilinear model and SCM share most entries; black boxes mark additional interactions found only by bilinear model |
| Fig. 4A-B | Reconstructed and observed BC-RGC connectivity matrices match closely |
| Fig. 5A-B | Each latent dimension captures a distinct connectivity motif |
| Fig. 5C | BC types cluster meaningfully in the 2D latent space |
| Fig. 5D-E | IPL stratification profiles correspond to latent dimension positions |
| Fig. 6A-B | Top gene weights show distinct signatures per latent dimension with biologically relevant expression patterns |
| Fig. 7A | Transcriptomically defined RGC types project into the learned latent space |
| Fig. 7B | Predicted connectivity for RGC types with unknown connectivity shows structured BC partner preferences |

---

## Supplementary Files Summary

| File | Content |
|------|---------|
| Supplementary File 1 | BC type correspondence across nomenclatures |
| Supplementary File 2 | RGC type correspondence across nomenclatures |
| Supplementary File 3 | Additional RGC type correspondence |
| Supplementary File 4 | GO terms for latent dimension gene sets in BCs and RGCs |
| Supplementary File 5 | Predicted BC partners for transcriptomically defined RGC types |

---

## Metrics and Evaluation Criteria

| Metric | Used For | Notes |
|--------|----------|-------|
| ROC-AUC | C. elegans gap junction reconstruction | Compared bilinear model vs. SCM |
| Validation loss (log10) | Hyperparameter selection | Cross-validation on both datasets |
| Visual matrix comparison | Connectivity reconstruction quality | Heatmap comparison of predicted vs. observed matrices |
| GO enrichment analysis | Biological interpretation of gene signatures | Applied to top genes per latent dimension |
| Functional alignment | Prediction validation | Compared predicted BC partners against known functional descriptions of RGC types |

---

## Reference Count
93 references cited in the paper.
