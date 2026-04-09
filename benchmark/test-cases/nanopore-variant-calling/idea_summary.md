# Idea Summary: Benchmarking Nanopore Variant Callers on Bacterial Genomes

## Working title
Benchmarking Reveals Superiority of Deep Learning Variant Callers on Bacterial
Nanopore Sequence Data

## Core question
How do deep learning-based variant callers compare to traditional methods for
SNP and indel detection from Oxford Nanopore bacterial sequencing data, across
different basecalling models, read types, sequencing depths, and bacterial
species?

## Motivation / gap
- Oxford Nanopore Technologies (ONT) sequencing increasingly used for bacterial
  genomics in clinical microbiology and public health surveillance
- ONT now offers multiple basecalling accuracy tiers (fast, hac, sup) and
  duplex sequencing, but no systematic evaluation of how these affect variant
  calling accuracy
- Deep learning variant callers (Clair3, DeepVariant, Medaka, NanoCaller) were
  designed primarily for human genomes -- unclear how they perform on diverse
  bacterial genomes with varying GC content and genome complexity
- Traditional variant callers (BCFtools, FreeBayes, Longshot) remain widely
  used but may be suboptimal for nanopore error profiles
- No comprehensive benchmark comparing all major variant callers across the
  full matrix of ONT basecalling models x read types x bacterial species
- Illumina is the de facto gold standard for bacterial variant calling, but it
  may itself have systematic biases (e.g., in repetitive regions) that are not
  well characterized

## Core contribution (bullet form)
- Comprehensive benchmark of 7 variant callers across 14 bacterial species
  (30-66% GC content), 3 ONT basecalling models (fast, hac, sup), and 2 read
  types (simplex, duplex)
- Key finding: deep learning callers Clair3 and DeepVariant achieve SNP F1
  99.99% and indel F1 99.53-99.61% on sup simplex data, surpassing Illumina
  (SNP F1 99.45%, indel F1 95.76%)
- Discovery that ONT superiority over Illumina is driven by better performance
  in repetitive and variant-dense genomic regions where Illumina short reads
  struggle with alignment
- Depth analysis showing 10x ONT sup simplex depth matches or exceeds full-depth
  Illumina accuracy for both SNPs and indels
- Runtime analysis: Clair3 achieves top accuracy at 0.86 s/Mbp with 1.6 GB RAM,
  making it practical for laptop-based clinical use
- Finding that the fast basecalling model produces variant calls worse than
  Illumina, establishing hac as the minimum acceptable model

## Method in brief
- Select 14 bacterial species spanning 30-66% GC content with ~99.5% ANI pairs
- Generate variant truthsets using high-confidence Illumina variant calls between
  closely related strain pairs, projected to reference genomes
- Sequence all samples with ONT (simplex and duplex) and Illumina
- Basecall ONT data with Dorado using fast, hac, and sup models
- Run 7 variant callers on all ONT conditions; run Snippy on Illumina as baseline
- Evaluate precision, recall, F1 for SNPs and indels separately
- Subsample reads to 5x, 10x, 25x, 50x, 100x depth for depth-accuracy analysis
- Analyze error modes: homopolymer errors, variant-dense region performance,
  repetitive region masking impact

## Target venue
eLife
