# Idea Summary: ENACT: End-to-End Analysis of Visium High Definition (HD) Data

## Working title
ENACT: End-to-End Analysis of Visium High Definition (HD) Data

## Core question
MotivationSpatial transcriptomics (ST) enables the study of gene expression within its spatial context in histopathology samples. To date, a limiting factor has been the resolution of sequencing based ST products. The introduction of the Visium High Definition (HD) technology opens the door to cell resolution ST studies. However, challenges remain in the ability to accurately map transcripts to cells and in assigning cell types based on the transcript data.ResultsWe developed ENACT, the first ti

## Motivation / gap
- IntroductionSpatial transcriptomics (ST) is a promising new technology that enables researchers to explore the spatial distribution of cells within tissues.
- ST technologies can be divided into two categories; sequencing-based (e.g.
- Visium and GeoMX) and image-based (e.g.
- Sequencing-based technologies provide several advantages including the ability to comprehensively map the entire transcriptome, identification of splice variants, and computation of RNA-velocity (1).

## Core contribution (bullet form)
Extracted from abstract:
MotivationSpatial transcriptomics (ST) enables the study of gene expression within its spatial context in histopathology samples. To date, a limiting factor has been the resolution of sequencing based ST products. The introduction of the Visium High Definition (HD) technology opens the door to cell resolution ST studies. However, challenges remain in the ability to accurately map transcripts to cells and in assigning cell types based on the transcript data.ResultsWe developed ENACT, the first tissue-agnostic pipeline that integrates advanced cell segmentation with Visium HD transcriptomics data to infer cell types across whole tissue sections. Our pipeline incorporates novel bin-to-cell assignment methods, enhancing the accuracy of single-cell transcript estimates. Validated on diverse synthetic and real datasets, our approach is both scalable and effective offering a robust solution for spatially resolved transcriptomics analysis.Availability and implementationENACT source code is available at https://github.com/Sanofi-Public/enact-pipeline. Experimental data is available at https://zenodo.org/records/13887921. Supplementary information: Supplementary data are available at BiorXiv online.

## Method in brief
Materials and MethodsCell SegmentationFig. 1 presents the key steps involved in the proposed processing and analysis pipeline. Cells in the full resolution tissue image are first segmented using Stardist, one of the most widely used UNet-based cell segmentation methods that has been shown to accurately segment images even when cells are tightly packed (4).biorxiv;2024.10.17.618905v1/FIG1F1fig1Fig. 1.Processing pipeline(1) Bin-by-gene matrix from 10X Genomics Visium HD provides mRNA transcript counts for each 2μm x 2μm bin. (2) Segmenting the full resolution tissue image using Startdist. (3) Visium HD bins that overlap with a cell are aggregated via a summing operation. This leads to a 2D cell-by-gene matrix. (4) Sargent, CellAssign, or CellTypist are used to translate the cell-wise transcript counts to a respective cell label. (5) Cell labels and their spatial locations within the tissue are wrapped in AnnData objects, which is compatible with SquidPy. This enables the application of various spatial statistical analyses, including neighborhood enrichment, Moran’s I, and co-occurrence analyses. Spatial distribution of the cells can be visualized by Tissuumaps (9) digital pathology viewer.Bin-to-Cell AssignmentTo obtain the total transcript counts for each cell in the tissue, Visium HD bins that intersect with the inferred cell boundary are aggregated. This produces a 2D cell-by-gene matrix, similar to a single-cell RNA sequencing (scRNA-Seq) experiment with an additional cell 

## Target venue
Bioinformatics
