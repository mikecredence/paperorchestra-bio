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
