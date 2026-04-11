# Idea Summary: Deep learning variant callers on bacterial nanopore data

## Working title
Benchmarking deep learning variant callers for bacterial SNP and indel detection using Oxford Nanopore R10.4.1 sequencing

## Core question
Can deep learning-based variant callers on the latest ONT R10.4.1 nanopore data match or exceed Illumina short-read accuracy for bacterial SNP and indel calling, and how do basecalling models and read depth affect performance?

## Motivation / gap
- Bacterial variant calling is critical for outbreak tracking, AMR prediction, and phylogenetics, yet benchmarks for ONT in bacteria are essentially nonexistent -- existing bacterial benchmarks only cover Illumina
- ONT has historically been limited by basecalling errors, especially homopolymer-driven indel artifacts, which made it unreliable for precise variant detection
- Deep learning variant callers (Clair3, DeepVariant) were trained exclusively on human genomes; whether they generalize to bacterial genomes (very different k-mer distributions, DNA modifications, GC content ranges) is an open question
- The new R10.4.1 pore chemistry with duplex capability and improved basecallers (fast/hac/sup models) has not been systematically evaluated for bacterial variant calling
- No study has examined how low ONT read depth can go while still matching Illumina accuracy -- important for resource-limited and real-time field sequencing

## Core contribution (bullet form)
- Comprehensive benchmark across 14 diverse bacterial species (GC 30-66%) comparing 7 ONT variant callers plus Illumina/Snippy, using biologically realistic variant truthsets derived from closely related donor genomes (~99.5% ANI)
- Clair3 achieves median SNP F1 of 99.99% and indel F1 of 99.53% on sup-basecalled simplex data, surpassing Illumina (SNP F1 99.45%, indel F1 95.76%) by roughly an order of magnitude in error rate
- Homopolymer-driven false indel calls, the historical weakness of ONT, are effectively eliminated with sup basecalling combined with deep learning variant callers (only 8 false indel calls for Clair3 on sup data across all 14 species)
- ONT at just 10x read depth with sup basecalling matches or exceeds full-depth Illumina accuracy for both SNPs and indels; 5x duplex sup achieves SNP accuracy comparable to Illumina
- Illumina's lower recall is driven by alignment difficulties in variant-dense and repetitive regions (bimodal FN density distribution peaking at ~20 variants per 100bp window), a problem that ONT long reads largely avoid

## Method in brief
We sequenced 14 bacterial species (Gram-positive and Gram-negative, spanning 30-66% GC content) using both ONT R10.4.1 MinION flowcells and Illumina NextSeq platforms from the same DNA extractions. ONT data was basecalled with Dorado v0.5.0 using three accuracy models (fast, hac, sup) for both simplex and duplex read types. Ground truth assemblies were generated via Trycycler (24 sub-assemblies per sample) polished with both long and short reads.

For the variant truthset, we selected a donor genome at approximately 99.5% ANI to each sample, identified shared variants via minimap2 and MUMmer intersection, then applied these real variants to the sample reference to create a mutated reference. This pseudo-real approach ensures biologically realistic variant distributions while maintaining a known truthset. SNP counts ranged from 2,102 to 57,887 across samples, with indel counts relatively consistent.

Seven ONT variant callers (BCFtools, Clair3, DeepVariant, FreeBayes, Longshot, Medaka, NanoCaller) were benchmarked against Illumina/Snippy. Variant calls were evaluated using vcfdist, computing precision, recall, and F1 at each quality score threshold. We further investigated error sources (variant density, repetitive regions, homopolymer length) and the impact of subsampled read depths (5x, 10x, 25x, 50x, 100x) on calling accuracy.

## Target venue
eLife
