Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Bioinformatics

## Idea Summary

# Idea Summary

## Working title
ENACT: End-to-end analysis of Visium High Definition (HD) data

## Core question
How can we accurately assign sub-cellular resolution Visium HD transcripts to individual cells and infer cell types across whole tissue sections, overcoming the mismatch between fixed-grid sequencing bins and irregular cell boundaries?

## Motivation / gap
- Visium HD provides transcript counts at 2um x 2um sub-cellular resolution, a major advance over multi-cell resolution Visium spots, but converting bin-level data to accurate single-cell expression profiles is non-trivial
- The default 8um x 8um aggregated bins rarely align with individual cells -- each bin often overlaps 2+ cells, and each cell overlaps multiple bins, especially when cells are small or tightly packed
- Existing methods like Bin2Cell use a naive approach that assigns bins to cells based on centroid overlap, discarding ~25% of bins that overlap multiple cells
- No tissue-agnostic end-to-end pipeline existed that integrates cell segmentation, robust bin-to-cell assignment, and cell type annotation for Visium HD data
- Weighted transcript assignment strategies that account for partial bin-cell overlap had not been systematically evaluated

## Core contribution (bullet form)
- Developed ENACT, the first tissue-agnostic end-to-end pipeline for Visium HD that integrates Stardist cell segmentation with novel bin-to-cell assignment strategies and cell type annotation
- Introduced three weighted bin-to-cell assignment methods (Weight-By-Area, Weight-By-Gene, Weight-By-Cell) that outperform the naive centroid-based approach, especially when cells are tightly packed
- Demonstrated that Weight-By-Area combined with Sargent cell annotation achieves the best overall performance against pathologist annotations for 20,991 cells
- Validated on two synthetic datasets (Xenium-based and seqFISH+-based) showing that weighted methods achieve higher F1 scores when ~25% of bins overlap multiple cells
- Showed that for sparse tissues with large cells (e.g., NIH-3T3), the naive method performs comparably with shorter computation time
- Pipeline outputs are compatible with AnnData/SquidPy for downstream spatial statistical analyses including neighborhood enrichment, Moran's I, and co-occurrence

## Method in brief
ENACT processes Visium HD data through five steps. First, the full-resolution tissue image is segmented using Stardist, a UNet-based model that handles tightly packed cells. Second, Visium HD 2um x 2um bins are represented as Shapely polygons and spatially joined with predicted cell outlines. Bins not overlapping any cell are discarded. Four bin-to-cell assignment strategies are implemented: (1) Naive -- assigns each bin to the cell whose centroid it contains (similar to Bin2Cell, discards multi-cell bins), (2) Weight-By-Area -- distributes transcript counts proportionally based on the intersection area between each bin and overlapping cells, (3) Weight-By-Gene -- weights by expression similarity between the bin and candidate cells, and (4) Weight-By-Cell -- weights by overall cell expression profiles. This produces a 2D cell-by-gene matrix analogous to scRNA-seq data.

For cell type annotation, ENACT supports three methods: Sargent (score-based inference using cell-type marker genes, well-suited for low transcript counts), CellAssign (probabilistic assignment based on marker genes), and CellTypist (logistic regression model). Gene marker lists were curated from expert input and PanglaoDB (top 10 genes by sensitivity and specificity). The pipeline outputs AnnData objects compatible with SquidPy for spatial statistics and can be visualized using TissUUmaps. Evaluation used two synthetic datasets (constructed from Xenium and seqFISH+ data) for transcript assignment accuracy, plus pathologist annotations of 20,991 cells (Epithelial, Stromal, Immune) for end-to-end cell type classification.

## Target venue
Bioinformatics


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the ENACT Visium HD pipeline study.

---

## Pipeline Overview

| Step | Component | Method/Tool |
|------|-----------|-------------|
| 1 | Bin-by-gene matrix input | 10X Genomics Visium HD (2um x 2um bins) |
| 2 | Cell segmentation | Stardist (UNet-based) |
| 3 | Bin-to-cell assignment | Naive, Weight-By-Area, Weight-By-Gene, Weight-By-Cell |
| 4 | Cell type annotation | Sargent, CellAssign, or CellTypist |
| 5 | Spatial analysis output | AnnData objects compatible with SquidPy |

Fig. 1: Processing pipeline showing all five steps from Visium HD input to spatial analysis output. Visualization via TissUUmaps digital pathology viewer.

---

## Visium HD Data Specifications

| Parameter | Value |
|-----------|-------|
| Bin resolution | 2um x 2um |
| Aggregated bin size | 8um x 8um |
| Approximate cell size | ~8um diameter |
| Bin representation | Shapely polygons |
| Geometric operations | Intersection area, spatial joins |

---

## Bin-to-Cell Assignment Methods

| Method | Strategy | Shared Bin Handling | Computation Cost |
|--------|----------|--------------------|-----------------| 
| Naive | Assign bin to cell whose boundary contains the bin centroid | Discards bins overlapping multiple cells | Lowest |
| Weight-By-Area | Distribute transcripts proportionally by intersection area | Weighted split | Moderate |
| Weight-By-Gene | Weight by expression similarity between bin and candidate cells | Weighted split | Higher |
| Weight-By-Cell | Weight by overall cell expression profiles | Weighted split | Higher |

---

## Cell Type Annotation Methods

| Method | Approach | Input | Suitability for Visium HD |
|--------|----------|-------|---------------------------|
| Sargent | Score-based, marker gene inference | Cell-type specific gene markers | Well-suited (handles low transcript counts) |
| CellAssign | Probabilistic assignment | Cell-type specific gene markers | Good |
| CellTypist | Logistic regression model | Pre-trained model | Good for standard cell types |

---

## Evaluation Datasets

| Dataset | Source | Type | Cells/Bins | Tissue | Purpose |
|---------|--------|------|-----------|--------|---------|
| Xenium-based synthetic | Xenium platform data | Synthetic Visium HD-like | Variable | Various | Transcript assignment accuracy |
| seqFISH+ synthetic | seqFISH+ data | Synthetic Visium HD-like | Variable (NIH-3T3 cells) | Cell culture | Transcript assignment accuracy |
| Pathologist-annotated | Real Visium HD | Real tissue | 20,991 cells annotated | Various | End-to-end cell type evaluation |

---

## Experiment 1: Bin-to-Cell Assignment on Xenium Synthetic Data (Whole Cell Boundaries)

### Performance Metrics (Table ST3)

| Method | Precision | Recall | F1 Score | Notes |
|--------|-----------|--------|----------|-------|
| Naive | Highest | Low | Lower | Only considers unique bins; 25% information loss |
| Weight-By-Area | High | Highest | Highest | Best overall for whole-cell boundaries |
| Weight-By-Gene | High | High | High | Competitive |
| Weight-By-Cell | High | High | High | Competitive |

Key finding: ~25% of bins overlap with more than one cell in the Xenium synthetic dataset. The Naive method achieves highest precision by only using unambiguous bins, but this causes significant information loss leading to low recall.

Fig. S2: Detailed performance visualization for all methods on Xenium whole-cell boundaries.

---

## Experiment 2: Bin-to-Cell Assignment on Xenium Synthetic Data (Nuclei Only)

### Performance Metrics

| Method | Precision | Recall | F1 Score | Notes |
|--------|-----------|--------|----------|-------|
| Naive | Lower than whole-cell | Similar to weighted | Close to weighted | Fewer bins overlap multiple nuclei |
| Weight-By-Area | Lower than whole-cell | Similar | Close to Naive | Smaller advantage over Naive |
| Weight-By-Gene | Lower than whole-cell | Similar | Close to Naive | Smaller advantage over Naive |
| Weight-By-Cell | Lower than whole-cell | Similar | Close to Naive | Smaller advantage over Naive |

Key finding: All methods show lower precision on nuclei vs. whole cells due to non-overlapping bins at nuclei boundaries containing cytoplasmic transcripts. The difference between Naive and weighted methods is smaller because fewer bins overlap multiple nuclei.

Fig. S3: Performance on nuclei-only segmentation.

---

## Experiment 3: Bin-to-Cell Assignment on seqFISH+ Synthetic Data

### Performance Metrics

| Method | Precision | Recall | F1 Score | Bins Overlapping >1 Cell |
|--------|-----------|--------|----------|-------------------------|
| Naive | ~1.0 | ~0.99 | ~0.99 | ~5% |
| Weight-By-Area | ~1.0 | ~0.99 | ~0.99 | ~5% |
| Weight-By-Gene | ~1.0 | ~0.99 | ~0.99 | ~5% |
| Weight-By-Cell | ~1.0 | ~0.99 | ~0.99 | ~5% |

Key finding: NIH-3T3 cells are large and sparse, intersecting 200-700 bins each. With only ~5% of bins overlapping multiple cells, all methods perform nearly identically. The Naive method is recommended for such sparse tissues given its shorter computation time.

Fig. S4: Performance on seqFISH+ synthetic data.

---

## Experiment 4: Computation Time Comparison

### Run Times (Table ST4)

| Method | Relative Run Time | Recommended When |
|--------|-------------------|-----------------|
| Naive | Fastest (baseline) | Sparse tissues, large cells, few multi-cell bin overlaps |
| Weight-By-Area | Moderate | Dense tissues, tightly packed cells |
| Weight-By-Gene | Longer | When expression-based weighting is critical |
| Weight-By-Cell | Longer | When cell-level expression context matters |

Fig. S5: Run time comparison across methods and datasets.

---

## Experiment 5: Cell Type Annotation Evaluation Against Pathologist Labels

### Gene Marker Sources

| Source | Usage |
|--------|-------|
| Expert-provided markers | Curated by pathologists |
| PanglaoDB | Top 10 genes by sensitivity and specificity in humans |
| Tables ST7, ST8 | Specific markers used by Sargent and CellAssign |

### Cell Type Label Mapping (Table ST5)

| Annotation Method Label | Pathologist Label |
|------------------------|-------------------|
| Various epithelial subtypes | Epithelial |
| Various stromal subtypes | Stromal |
| Various immune subtypes | Immune cells |

### Evaluation Metrics

| Metric | Description |
|--------|-------------|
| Accuracy | Overall correct classification rate |
| Precision | Per-class positive predictive value |
| Recall | Per-class sensitivity |
| F1-score | Harmonic mean of precision and recall |

Evaluation framed as multi-class classification: Epithelial vs. Stromal vs. Immune.

---

## Experiment 6: End-to-End Pipeline Performance (Table ST6)

### Bin-to-Cell x Annotation Method Combinations

| Bin-to-Cell Method | Annotation Method | Accuracy | Precision | Recall | F1 Score |
|-------------------|-------------------|----------|-----------|--------|----------|
| Naive | Sargent | Moderate | Moderate | Moderate | Moderate |
| Naive | CellAssign | Moderate | Moderate | Moderate | Moderate |
| Naive | CellTypist | Moderate | Moderate | Moderate | Moderate |
| Weight-By-Area | Sargent | Best | Best | Best | Best |
| Weight-By-Area | CellAssign | High | High | High | High |
| Weight-By-Area | CellTypist | High | High | High | High |
| Weight-By-Gene | Sargent | High | High | High | High |
| Weight-By-Gene | CellAssign | High | High | High | High |
| Weight-By-Gene | CellTypist | High | High | High | High |
| Weight-By-Cell | Sargent | High | High | High | High |
| Weight-By-Cell | CellAssign | High | High | High | High |
| Weight-By-Cell | CellTypist | High | High | High | High |

Key finding: Weight-By-Area combined with Sargent annotation achieves the best overall performance across all metrics when validated against 20,991 pathologist-annotated cells.

Fig. S6: Visual summary of all 12 pipeline configuration experiments.

---

## Downstream Spatial Analysis Capabilities

| Analysis | Tool | Description |
|----------|------|-------------|
| Neighborhood enrichment | SquidPy | Identifies cell type co-localization patterns |
| Moran's I | SquidPy | Measures spatial autocorrelation of gene expression |
| Co-occurrence analysis | SquidPy | Quantifies frequency of cell type co-occurrence |
| Spatial visualization | TissUUmaps | Digital pathology viewer for spatial cell type maps |

---

## Segmentation Details

| Parameter | Value |
|-----------|-------|
| Model | Stardist |
| Architecture | UNet-based |
| Input | Full-resolution tissue H&E image |
| Output | Cell boundary polygons |
| Strength | Handles tightly packed cells |
| Post-processing | Shapely polygon representation |

---

## Data Availability and Reproducibility

| Resource | Location |
|----------|----------|
| ENACT source code | https://github.com/Sanofi-Public/enact-pipeline |
| Experimental data | https://zenodo.org/records/13887921 |
| Supplementary information | BioRxiv |
| Python package | Available from GitHub |

---

## Key Technical Challenges Addressed

| Challenge | ENACT Solution |
|-----------|---------------|
| Bins overlapping multiple cells | Weighted assignment strategies distribute transcripts proportionally |
| Cells smaller than 8um aggregated bins | Uses 2um native resolution + segmentation rather than pre-aggregated bins |
| Tightly packed cells | Stardist segmentation designed for dense cell packing |
| Low transcript counts per cell | Sargent score-based annotation robust to low counts |
| Tissue-specificity | Pipeline is tissue-agnostic, validated on diverse datasets |
| Scalability | Processes whole tissue sections efficiently |

---

## Comparison with Prior Work (Bin2Cell)

| Feature | Bin2Cell | ENACT |
|---------|---------|-------|
| Segmentation | Stardist | Stardist (same) |
| Outline expansion | Yes | Not needed (weighted methods) |
| Multi-cell bin handling | Discards | Weighted distribution |
| Bin assignment methods | 1 (centroid-based) | 4 (Naive + 3 weighted) |
| Cell type annotation | Not integrated | 3 methods (Sargent, CellAssign, CellTypist) |
| Spatial analysis output | Not specified | AnnData/SquidPy compatible |
| Performance on dense tissue | Limited by information loss | Better recall with weighted methods |

---

## Summary of Recommendations

| Tissue Type | Recommended Bin-to-Cell Method | Recommended Annotation | Rationale |
|------------|-------------------------------|----------------------|-----------|
| Dense tissue (tightly packed cells) | Weight-By-Area | Sargent | Best F1, handles multi-cell bin overlaps |
| Sparse tissue (large, separated cells) | Naive | Any | Comparable accuracy, fastest computation |
| Low transcript counts | Weight-By-Area | Sargent | Score-based method robust to low counts |
| Standard cell types | Weight-By-Area | CellTypist | Pre-trained model, good default |

---

## Figure Summary

| Figure | Key Finding |
|--------|------------|
| Fig. 1 | Pipeline overview: 5-step end-to-end processing from Visium HD bins to spatial cell type maps |
| Fig. S2 | Xenium synthetic: Weight-By-Area achieves highest F1 on whole-cell boundaries |
| Fig. S3 | Nuclei-only: smaller performance gap between methods |
| Fig. S4 | seqFISH+: all methods nearly identical for large sparse cells |
| Fig. S5 | Run time comparison across methods |
| Fig. S6 | Full experimental matrix: 4 bin methods x 3 annotation methods against pathologist labels |

---

## Reference Count
12 references cited in the paper.

