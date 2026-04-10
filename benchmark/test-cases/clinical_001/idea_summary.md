## Working title

Benchmarking bacterial taxonomic classification using nanopore metagenomics data of several mock communities

## Core question

How do different taxonomic classification tools perform when applied to Oxford Nanopore long-read metagenomic sequencing data from well-characterized mock bacterial communities, and how does the transition from R9 to R10 chemistry affect classifier accuracy?

## Motivation / gap

- Metagenomic shotgun sequencing with Oxford Nanopore Technologies (ONT) is increasingly used for microbial community profiling, but systematic benchmarking on ONT data is limited
- Most existing benchmarks rely on Illumina short-read data, which have different error profiles
- ONT is phasing out R9 chemistry in favor of R10, yet the impact of this transition on taxonomic classification accuracy has not been thoroughly assessed
- Mock communities with known composition provide ground truth for rigorous tool evaluation

## Core contribution

- Provide a systematic benchmark of multiple taxonomic classification tools on nanopore metagenomics data from several mock communities with known compositions
- Evaluate the impact of the R9-to-R10 chemistry transition on classifier performance
- Show divergent tool responses to chemistry change: Kraken2 performance increases with R10 while Centrifuge declines; Kaiju improves while MMseqs2 decreases
- Release a comprehensive benchmarking dataset as a community resource

## Method in brief

Several well-characterized mock bacterial communities were sequenced using Oxford Nanopore R9 and R10 chemistries. Multiple taxonomic classification tools spanning k-mer matching (Kraken2, Centrifuge), translated search (Kaiju, MMseqs2), and alignment-based approaches were applied. Performance was evaluated using precision, recall, F1 score, and abundance estimation accuracy against known community compositions.

## Target venue

Scientific Data (Nature)
