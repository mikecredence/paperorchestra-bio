## Working title

Comprehensive benchmarking of metagenomic classification tools for long-read sequencing data

## Core question

How do different categories of metagenomic classification tools (kmer-based, mapping-based, general-purpose mappers, and protein-database tools) compare in accuracy, species detection, abundance estimation, and computational cost when applied to long-read sequencing data from PacBio and ONT platforms?

## Motivation / gap

- Most existing metagenomic classification tools were originally designed for short, accurate Illumina reads; long-read technologies (ONT and PacBio HiFi) are gaining traction but lack thorough benchmarks
- Previous benchmarking studies on long reads did not include PacBio HiFi reads or general-purpose long-read mappers (Minimap2, Ram) as classification alternatives
- No prior work systematically assessed how database composition, read length distributions, host contamination levels, and abundance measure definitions jointly affect tool performance
- The influence of unknown species (absent from reference databases) on false-positive reporting has not been rigorously tested across tool categories
- Real gut microbiome datasets reveal discordance among tools, but there is no comprehensive cross-category comparison documenting these differences
- Protein-database tools have not been directly compared to nucleotide-database tools on the same long-read datasets under controlled conditions

## Core contribution (bullet form)

- Evaluated 13 pipelines across four tool categories on 7 synthetic datasets, 3 mock community datasets, and 6 real gut microbiome samples, making this one of the most comprehensive long-read metagenomics benchmarks to date
- Demonstrated that general-purpose mappers (Minimap2 alignment mode, Ram) match or exceed the best classification tools in accuracy while requiring up to 4x less RAM, though they are up to 10x slower than the fastest kmer-based tools
- Showed that all tested tools except CLARK-S tend to overreport organisms not in the sample, and that high host DNA contamination (e.g., 99% human reads in PB3) substantially degrades performance
- Found that protein-database tools (Kaiju, MEGAN-P) consistently underperformed compared to nucleotide-database tools across nearly all metrics
- Established that longer reads improve classification accuracy, but filtering to only the longest reads paradoxically reduces accuracy due to uneven read-length distributions across species
- Quantified abundance estimation errors across three definitions (relative read count, relative genome length, relative genome count) on mock community datasets, showing that the choice of abundance metric matters

## Method in brief

The study constructed seven synthetic datasets by mixing real sequenced reads from isolated species (ONT and PacBio), preserving natural error profiles and length distributions while maintaining ground-truth labels. These ranged from simple bacterial communities (3-10 species, even distributions) to complex scenarios with eukaryotic hosts (up to 99% human reads), unknown species, related strains, and staggered abundances down to 0.005% of reads. Three sequenced mock communities (ONT_Zymo, PB_ATCC, PB_Zymo) and six real gut microbiome samples complemented the synthetic benchmarks.

All tools were tested against custom-built databases derived from the same NCBI RefSeq sequences (complete genomes and chromosomes for bacteria, archaea, and human) to eliminate database-content bias. The nucleotide database contained 9,044 tax IDs and the protein database 11,435 tax IDs. Evaluation metrics included read-level classification accuracy at species and genus levels, abundance estimation error (L1 distance between predicted and true abundance vectors), true/false positive organism detection at varying read-count thresholds (1, 10, 50 reads), and computational resource usage (wall-clock time and peak RAM).

The 13 pipelines spanned four categories: kmer-based (Kraken2, Bracken, Centrifuge, CLARK, CLARK-S), mapping-based (MetaMaps, MEGAN-N, deSAMBA), general-purpose long-read mappers (Minimap2 in alignment and mapping modes, Ram in mapping mode), and protein-database tools (Kaiju, MEGAN-P). Abundance was calculated using three definitions: relative read count, relative genome length, and relative genome count. Resource benchmarks normalized all datasets to approximately 1 Gbp for fair comparison, with additional scalability tests at half and full original sizes for mock community datasets.

## Target venue

BMC Bioinformatics
