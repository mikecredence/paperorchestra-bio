# Idea Summary: Benchmarking Subcellular Spatial Transcriptomics Platforms

## Working title
Systematic Benchmarking of High-Throughput Subcellular Spatial Transcriptomics
Platforms Across Human Tumors

## Core question
How do the latest high-throughput subcellular spatial transcriptomics platforms
compare in sensitivity, specificity, cell segmentation, spatial clustering, and
concordance with orthogonal multi-omics data when applied to the same tumor
tissue sections?

## Motivation / gap
- Multiple subcellular-resolution spatial transcriptomics (ST) platforms are now
  commercially available, but no study has systematically compared them on
  identical tissue samples with unified processing and annotation
- Existing comparisons use different tissues, different processing pipelines,
  and different metrics -- making head-to-head assessment impossible
- Two major technology classes (sequencing-based sST and imaging-based iST)
  have fundamentally different trade-offs (whole-transcriptome vs targeted
  panels, diffusion artifacts vs optical crowding) that are poorly quantified
- Practitioners and core facilities need objective guidance on platform
  selection for tumor biology studies
- No public resource exists that provides uniformly processed multi-platform
  multi-omics spatial data for computational method development

## Core contribution (bullet form)
- First unified benchmark of 5 subcellular ST platforms (Stereo-seq v1.3,
  Visium HD FFPE, Visium HD FF, CosMx 6K, Xenium 5K) on serial sections from
  3 human tumor types (colon adenocarcinoma, hepatocellular carcinoma, ovarian
  cancer)
- Multi-metric evaluation framework covering 7 dimensions: capture sensitivity,
  specificity, diffusion control, cell segmentation accuracy, cell type
  annotation robustness, spatial clustering concordance, and transcript-protein
  spatial alignment
- Orthogonal ground truth using adjacent-section CODEX protein profiling and
  matched scRNA-seq from the same tumors
- Finding that imaging-based platforms (especially Xenium 5K) achieve superior
  cell segmentation fidelity, annotation robustness, and CODEX concordance,
  while sequencing-based platforms (especially Visium HD FFPE) offer higher
  gene detection breadth
- Discovery that CosMx 6K has elevated negative control signal and spatial
  background aggregation compared to Xenium 5K
- Finding that Stereo-seq v1.3 exhibits substantially greater transcript
  diffusion beyond tissue boundaries compared to Visium HD
- Public release of uniformly processed 8.13 million cell multi-omics dataset
  via the SPATCH portal

## Method in brief
- Collect serial tissue sections from 3 cancer types (COAD, HCC, OV)
- Process identical sections on each platform using manufacturer protocols
- Generate matched scRNA-seq (10x Chromium, cellranger v7.0.0) and CODEX
  protein data on adjacent sections
- Unify analysis using scanpy v1.10.3 for clustering, StarDist v0.5.0 for
  nuclear segmentation, CellCharter for spatial clustering
- Evaluate sensitivity at matched bin sizes (8 um), specificity via negative
  control probes, diffusion via extra-tissue transcript ratios
- Cell segmentation validated against 72,405 manually annotated cells across
  five 500x500 um regions
- Cell annotation assessed with 5 independent tools (SELINA, Celltypist,
  Spoint, Tangram, TACCO) for robustness
- Spatial concordance with CODEX measured via gene signature correlations for
  immune and stromal cell types

## Target venue
Nature Communications
