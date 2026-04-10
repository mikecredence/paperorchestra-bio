## Working title

Comprehensive benchmarking of metagenomic classification tools for long-read sequencing data

## Core question

Which metagenomic classification tools perform best for species-level taxonomic classification of long-read sequencing data across diverse scenarios?

## Motivation / gap

- Long-read sequencing (ONT, PacBio) is increasingly used for metagenomics, but most classification tools were designed for short reads
- No comprehensive benchmark exists that systematically compares kmer-based, mapping-based, and general-purpose long-read mappers on standardized datasets
- Real-world complications (host contamination, unknown species, closely related species, extreme abundance variation) are rarely tested together

## Core contribution

- Evaluate >20 classification pipelines (nucleotide and protein databases), selecting 13 for extensive benchmarking
- Test on seven synthetic datasets plus three well-defined mock communities and six real gut microbiomes
- Show that general-purpose mappers (Minimap2, Ram) achieve similar or better accuracy than specialized tools, though up to 10x slower than fastest kmer-based tools but requiring up to 4x less RAM
- Find that all tools struggle with species not represented in reference databases

## Method in brief

- Prepare seven synthetic long-read datasets simulating host presence, unknown species, related species, and varying abundances (0.0001% to 20%)
- Use three sequenced mock communities as ground truth
- Benchmark 13 pipelines across metrics: precision, recall, F1, L1 distance, runtime, RAM usage
- Compare kmer-based tools (Kraken2, Centrifuge, etc.), mapping-based classifiers, and general mappers (Minimap2, Ram)

## Target venue

BMC Bioinformatics
