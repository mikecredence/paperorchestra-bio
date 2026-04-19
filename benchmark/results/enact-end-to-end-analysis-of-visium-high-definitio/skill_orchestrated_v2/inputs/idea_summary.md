{
  "statistical_sentences": [
    "However, this approach results in significant information loss, as 25% of the bins overlap with more than one cell, leading to a low recall.When focusing solely on cell nuclei, we observe a smaller difference in performance between the \u2018Naive\u2019 and weighted methods (Fig. S3).",
    "Indeed, only about 5% of bins overlapped more than one cell for this dataset."
  ],
  "methods_sentences": [
    "Specifically, spots (also referred to as bins) in Visium HD are 2\u03bcm x 2\u03bcm.",
    "To enable cell-based analysis, Visium HD allows the user to aggregate bins resulting in an 8\u03bcm x 8\u03bcm dimension for each spot, which roughly covers the size of a cell.",
    "However, accurately get-ting single-cell transcript estimates from the aggregated 8\u03bcm x 8\u03bcm is not trivial.",
    "In many cases, each such aggregated spot overlaps 2 or more cells and vice versa, each cell overlaps more than 1 spot (often more than 2 given the 3D placement) especially in cases where cells are smaller than 8\u03bcm in diameter, or where cells overlap or are tightly spaced.To address this problem, instead of using the 8\u03bcm x 8\u03bcm bins for downstream analysis, previous work such as Bin2cell (3) proposes a method that combines morphology and gene expression information to obtain accurate single-cell transcript counts.",
    "These outlines are then expanded, and the 2\u03bcm x 2\u03bcm bins with centroids within each cell outline are aggregated to obtain single-cell transcript counts.While such integrated imaging plus sequencing method obtains good results in some cases, as we show it can be less effective when cells are tightly spaced.",
    "Cells in the full resolution tissue image are first segmented using Stardist, one of the most widely used UNet-based cell segmentation methods that has been shown to accurately segment images even when cells are tightly packed (4).biorxiv;2024.10.17.618905v1/FIG1F1fig1Fig. 1.Processing pipeline(1) Bin-by-gene matrix from 10X Genomics Visium HD provides mRNA transcript counts for each 2\u03bcm x 2\u03bcm bin. (2) Segmenting the full resolution tissue image using Startdist. (3) Visium HD bins that overlap with a cell are aggregated via a summing operation.",
    "Fig. 1.: Processing pipeline(1) Bin-by-gene matrix from 10X Genomics Visium HD provides mRNA transcript counts for each 2\u03bcm x 2\u03bcm bin. (2) Segmenting the full resolution tissue image using Startdist. (3) Visium HD bins that overlap with a cell are aggregated via a summing operation."
  ],
  "table_count": 0
}