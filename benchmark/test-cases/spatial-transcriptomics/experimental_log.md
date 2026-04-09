# Experimental Log: Subcellular Spatial Transcriptomics Benchmarking

## Platforms Under Test

| Platform | Type | Resolution | Gene Panel | Tissue Prep |
|----------|------|------------|------------|-------------|
| Stereo-seq v1.3 | sST (sequencing) | 0.5 um | ~17,134 (whole-transcriptome) | FFPE |
| Visium HD FFPE | sST (sequencing) | 2 um | 18,085 (whole-transcriptome) | FFPE |
| Visium HD FF | sST (sequencing) | 2 um | 18,085 (whole-transcriptome) | Fresh-frozen (OCT) |
| CosMx 6K | iST (imaging) | Single-molecule | 6,175 (targeted panel) | FFPE |
| Xenium 5K | iST (imaging) | Single-molecule | 5,001 (targeted panel) | FFPE |

## Reference / Ground Truth Platforms

| Platform | Purpose | Processing |
|----------|---------|------------|
| scRNA-seq (10x Chromium) | Gene expression ground truth | cellranger v7.0.0 |
| CODEX | Protein spatial ground truth | Adjacent tissue sections |

## Tissue Samples

| Cancer Type | Abbreviation | Tissue Prep |
|-------------|-------------|-------------|
| Colon adenocarcinoma | COAD | FFPE + FF serial sections |
| Hepatocellular carcinoma | HCC | FFPE + FF serial sections |
| Ovarian cancer | OV | FFPE + FF serial sections |

- Serial sections cut from same tissue blocks for all platforms
- FFPE-embedded sections for Stereo-seq, Visium HD FFPE, CosMx 6K, Xenium 5K
- Fresh-frozen OCT-embedded sections for Visium HD FF
- Single-cell suspensions prepared from same samples for scRNA-seq
- Adjacent sections profiled with CODEX for protein ground truth

## Dataset Scale
- Total cells profiled across all platforms and samples: 8.13 million
- Manual nuclear segmentation reference: 72,405 cells annotated across five 500x500 um regions

## Data Processing Pipelines

| Platform | Pipeline | Version |
|----------|----------|---------|
| Stereo-seq v1.3 | SAW | v8.0 |
| Visium HD (FFPE & FF) | Space Ranger | v3.0.0 |
| CosMx 6K | Atomx (decoding) | v1.3.2 |
| Xenium 5K | Xenium Onboard Analysis | v3.1.0 |
| scRNA-seq | cellranger | v7.0.0 |

## Computational Analysis Tools

| Tool | Version | Purpose |
|------|---------|---------|
| scanpy | v1.10.3 | Clustering, UMAP, general analysis |
| StarDist | v0.5.0 | Nuclear segmentation |
| CellCharter | -- | Spatial clustering |
| SimpleITK | v2.4.0 | Image registration |
| scikit-learn | v1.5.2 | Nearest neighbor analysis |
| SELINA | -- | Cell type annotation (tool 1) |
| Celltypist | -- | Cell type annotation (tool 2) |
| Spoint | -- | Cell type annotation (tool 3) |
| Tangram | -- | Cell type annotation (tool 4) |
| TACCO | -- | Cell type annotation (tool 5) |

---

## Results: Capture Sensitivity

### Per 8-um bin analysis (sST platforms matched to comparable resolution)
- Visium HD FFPE showed enhanced transcript and gene detection per bin compared to Stereo-seq v1.3 across HCC and OV samples
- Stereo-seq v1.3 had a higher proportion of reads passing UMI quality control compared to Visium HD FFPE and scRNA-seq, indicating improved retention of valid transcript information
- Visium HD FFPE exhibited lower sequencing saturation at comparable sequencing depths

### iST platform comparison (common gene set)
- Xenium 5K detected higher numbers of transcripts and genes per bin compared to CosMx 6K in HCC
- CosMx 6K detected higher total transcripts than Xenium 5K overall (driven by larger panel)
- When restricting to the 2,522 shared genes between the two iST panels, Xenium 5K showed higher per-gene sensitivity

### Cross-platform gene detection breadth
- sST platforms (Stereo-seq, Visium HD) detected far more unique genes due to whole-transcriptome capture
- iST platforms limited to their panel sizes (6,175 for CosMx, 5,001 for Xenium)
- At single-cell-scale binning, sST platforms detected only a few hundred to ~1,000 genes per cell

---

## Results: Specificity (Background Noise)

### Negative control probe analysis (iST platforms)
- CosMx 6K showed elevated negative control signal proportions across all QC thresholds
- Xenium 5K maintained consistently lower negative control signals
- Primary background source identified as nonspecific probe binding in CosMx 6K

### Spatial autocorrelation of background (Moran's I)
- CosMx 6K exhibited stronger spatial aggregation of negative control signals (higher Moran's I), indicating spatially structured noise
- Xenium 5K showed reduced spatial variation in background signal

---

## Results: Diffusion Control (sST Platforms)

### Extra-tissue transcript leakage
- Stereo-seq v1.3 demonstrated substantially greater transcript diffusion beyond tissue boundaries in all samples
- Visium HD FFPE showed more effective diffusion control
- Extra-tissue/intra-tissue transcript count ratios significantly favored Visium HD FFPE
- This diffusion artifact in Stereo-seq likely relates to the capture bead array design and RNA migration during permeabilization

---

## Results: Cell Segmentation

### Manual annotation benchmark
- 72,405 cells manually annotated across five 500x500 um regions from multiple tissue types
- Manual annotations served as segmentation ground truth

### Platform-specific segmentation performance
- CosMx 6K and Xenium 5K default segmentation closely matched manual cell counts
- Stereo-seq v1.3 exhibited reduced segmentation accuracy relative to manual annotations

### Cell morphology metrics
- CosMx 6K produced larger, more convex, more circular cell boundaries
- Xenium 5K captured more irregular (realistic) cell morphologies matching tissue architecture
- StarDist nuclear segmentation applied to Xenium 5K: identified nuclei with higher gene and transcript counts per nucleus compared to other platforms

---

## Results: Gene Expression Correlation with scRNA-seq

### Gene-wise Pearson correlation (ST vs matched scRNA-seq)
- Stereo-seq v1.3: high correlation with scRNA-seq
- Visium HD FFPE: high correlation with scRNA-seq
- Xenium 5K: high correlation with scRNA-seq
- CosMx 6K: substantial deviation from scRNA-seq reference (lower correlation)
- Correlation pattern held when restricting to 2,522 genes shared across Xenium 5K panel

---

## Results: Cell Type Annotation

### Annotation robustness (5-tool consensus)
- Xenium 5K: highest proportion of cells consistently annotated across all five annotation tools
- iST platforms (CosMx 6K and Xenium 5K) recovered a greater number of distinct cell types compared to sST platforms
- Xenium 5K showed highest overall annotation robustness

### T cell subtype recovery
- CosMx 6K and Xenium 5K recovered the highest number of T cell subtypes
- Xenium 5K demonstrated superior annotation reliability for immune cell subtypes across tools

### Platform ranking for annotation consistency
1. Xenium 5K (best)
2. CosMx 6K
3. Visium HD FFPE
4. Visium HD FF
5. Stereo-seq v1.3

---

## Results: Spatial Clustering

### Silhouette score (cluster separation quality)
- scRNA-seq provided the most effective cell population separation (highest silhouette scores)
- iST platforms (CosMx 6K, Xenium 5K) achieved better cluster resolution than sST platforms (Stereo-seq, Visium HD)

### Spatial clustering concordance with CODEX
- Comparable clustering concordance across most platforms when aligned to CODEX protein spatial domains
- Stereo-seq v1.3 showed notably low concordance in HCC tissue specifically
- CellCharter used for all spatial domain identification

---

## Results: Transcript-Protein Spatial Concordance (CODEX Alignment)

### Gene signature spatial correlations (immune and stromal cell types)
- Visium HD FFPE and Xenium 5K showed the highest concordance with CODEX protein spatial patterns
- Xenium 5K exhibited the strongest overall concordance across cell types

### Cell type-specific concordance
- Xenium 5K: highest concordance, particularly for immune cell populations (T cells, macrophages, B cells)
- All platforms performed comparably for detecting epithelial cell populations
- Stromal cell concordance varied more across platforms

### Overall CODEX concordance ranking
1. Xenium 5K (best overall)
2. Visium HD FFPE
3. CosMx 6K
4. Visium HD FF
5. Stereo-seq v1.3

---

## Summary of Platform Strengths and Weaknesses

| Metric | Best Platform | Worst Platform |
|--------|--------------|----------------|
| Gene detection breadth | Visium HD FFPE (18,085 genes) | Xenium 5K (5,001 genes) |
| UMI quality retention | Stereo-seq v1.3 | Visium HD FFPE |
| Specificity (low background) | Xenium 5K | CosMx 6K |
| Diffusion control | Visium HD FFPE | Stereo-seq v1.3 |
| Cell segmentation accuracy | CosMx 6K / Xenium 5K (tied) | Stereo-seq v1.3 |
| scRNA-seq correlation | Stereo-seq / Visium HD / Xenium (tied) | CosMx 6K |
| Annotation robustness | Xenium 5K | Stereo-seq v1.3 |
| Immune cell type recovery | Xenium 5K / CosMx 6K | sST platforms |
| Spatial clustering quality | iST platforms | sST platforms |
| CODEX concordance | Xenium 5K | Stereo-seq v1.3 |

---

## Data Availability
- All data available via SPATCH portal for visualization and download
- Uniformly processed and annotated multi-omics dataset released for community use
- Portal supports interactive exploration across all platforms and tissue types

## Ground Truth Reference
- bioRxiv DOI: 10.1101/2024.12.23.630033
- Published: Nature Communications, DOI 10.1038/s41467-025-64292-3
