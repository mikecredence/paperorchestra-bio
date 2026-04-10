## Working title

sRNAfrag: A Pipeline and Suite of Tools to Analyze Fragmentation in Small RNA Sequencing Data

## Core question

Can we build a standardized tool to systematically quantify and analyze fragmentation patterns across any small RNA biotype, and use it to uncover conserved fragmentation events?

## Motivation / gap

- Fragments derived from small RNAs (e.g., snoRNA-derived fragments) have biological relevance, but they remain poorly understood.
- Existing analysis methods are ad hoc and biotype-specific; there is no standardized workflow for analyzing sRNA fragmentation across all biotypes.
- Multi-mapping reads, which are common in sRNA-seq, are typically discarded but contain useful information (e.g., conserved seed sequences).

## Core contribution

- Develop sRNAfrag, a standardized pipeline and script suite for quantifying and analyzing sRNA fragmentation of any biotype
- Benchmark showing the tool detects mature miRNA loci fragmented from precursors and, using multi-mapping events, recovers the conserved 5' seed sequence of miRNAs
- Detect 1411 snoRNA fragment conservation events between 2 of 4 eukaryotic species
- Enable cross-species fragmentation pattern analysis and motif discovery

## Method in brief

- Standardized workflow for mapping, quantifying, and classifying sRNA fragments from sequencing data
- Multi-mapping event analysis to capture conserved sequence features (e.g., 5' seed)
- Benchmarking against known miRNA precursor-to-mature fragmentation loci
- Cross-species conservation analysis across 4 eukaryotic species for snoRNA fragments
- Motif and fragmentation pattern discovery tools
- Open-source: https://github.com/kenminsoo/sRNAfrag

## Target venue

Briefings in Bioinformatics
