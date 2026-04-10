## Working title

Benchmarking Single-Cell Multi-Modal Data Integration Methods

## Core question

How do the 40 available single-cell multi-modal integration algorithms compare in terms of usability, accuracy, and robustness across different dataset types (paired, unpaired, mosaic), modality combinations (DNA, RNA, protein, spatial), and data quality conditions?

## Motivation / gap

- Single-cell multi-modal omics was "Method of the Year 2019" and has since exploded in both data generation and tool development
- Both unpaired (separate profiling) and paired (simultaneous measurement) multi-modal datasets are now common, plus "mosaic" datasets mixing both
- No comprehensive benchmark covers the full landscape of 40 integration tools across all these axes

## Core contribution

- Largest benchmark to date: 40 single-cell multi-modal integration algorithms
- Coverage of DNA, RNA, protein, and spatial omics modalities
- Evaluation across paired, unpaired, and mosaic dataset types
- Assessment of usability, accuracy, and robustness
- Practical guidance for method selection tailored to specific datasets and applications

## Method in brief

We will collect representative paired, unpaired, and mosaic multi-modal datasets spanning DNA (scATAC-seq), RNA (scRNA-seq), protein (CITE-seq), and spatial modalities. All 40 algorithms will be run with documented parameters. Evaluation will include clustering accuracy (ARI, NMI), batch correction (kBET, silhouette), biological conservation (cell type separation), label transfer accuracy, scalability, and usability scoring. Robustness will be tested by varying dataset sizes and introducing noise.

## Target venue

Nature Methods
