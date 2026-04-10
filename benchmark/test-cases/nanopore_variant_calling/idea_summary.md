## Working title

Benchmarking Reveals Superiority of Deep Learning Variant Callers on Bacterial Nanopore Sequence Data

## Core question

How do SNP and indel variant calling methods compare in accuracy across diverse bacterial species when using Oxford Nanopore Technologies (ONT) sequencing versus Illumina, and do deep-learning-based callers outperform traditional approaches?

## Motivation / gap

- Variant calling is fundamental to bacterial genomics (transmission tracking, phylogenetics, AMR prediction), yet systematic benchmarking on ONT data across diverse species is lacking
- ONT has historically struggled with homopolymer-induced indel errors, but newer high-accuracy chemistries may have resolved this
- It is unclear whether deep-learning-based variant callers (e.g., Clair3) surpass traditional methods and whether ONT can now match or exceed Illumina accuracy

## Core contribution

- Comprehensive benchmark of SNP and indel variant calling across 14 diverse bacterial species
- Comparison of ONT vs Illumina sequencing for variant calling accuracy
- Demonstration that deep-learning-based ONT callers (especially Clair3) deliver higher accuracy than traditional methods and Illumina
- Investigation of missed and false calls revealing limitations of short reads
- Evidence that high-accuracy ONT chemistry eliminates traditional homopolymer-induced indel errors
- Biologically realistic benchmarking using gold-standard references with projected variations from closely related strains

## Method in brief

We will generate gold-standard reference genomes for 14 bacterial species. Variations from closely related strains will be projected onto these references to create biologically realistic SNP and indel distributions. Both ONT and Illumina sequencing will be performed. Multiple variant callers -- traditional (FreeBayes, bcftools, GATK) and deep-learning-based (Clair3, DeepVariant, Medaka) -- will be benchmarked. Accuracy will be evaluated by precision, recall, and F1 for both SNPs and indels.

## Target venue

eLife
