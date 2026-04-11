## Working title
sRNAfrag: A Standardized Pipeline for Analyzing Small RNA Fragmentation in Sequencing Data

## Core question
Can a standardized computational pipeline accurately detect, quantify, and analyze fragmentation patterns of non-tRNA small RNAs (snoRNAs, snRNAs, rRNAs) from small RNA sequencing data, and can multi-mapping events reveal conserved fragment patterns across species?

## Motivation / gap
- Fragments from snoRNAs and rRNAs associate with Argonaute proteins and may have functional roles in disease, but lack curated annotations like tRNA fragments (MINTbase)
- Existing tools like FlaiMapper generate annotations from BAM files, but user preprocessing decisions introduce variability
- No pipeline handles multi-mapping correction, cross-species conservation analysis, and fragment clustering in an integrated workflow
- The small RNA fragment field needs standardized tools to build toward a curated database similar to MINTbase for non-tRNA fragments
- No tool exploits multi-mapping events as a signal for identifying functionally important conserved fragment loci

## Core contribution (bullet form)
- Developed sRNAfrag, a three-module pipeline (P1, S1, P2) that processes raw fastq to fragment counts with license-plate IDs, multi-mapping correction, and clustering
- Achieved 94.7% and 86.5% accuracy for start and end loci calling within 1 bp of true miRNA positions (comparable to FlaiMapper's 92.4% and 85.2%)
- Demonstrated that multi-mapping events recover the conserved 5' seed region of miRNAs, validating the approach for other sRNA types
- Detected 1,411 snoRNA fragment conservation events shared between 2 of 4 eukaryotic species (human, mouse, C. elegans, A. thaliana)
- Provides three normalization methods (ratio with miRNAs, TPM, CPM) and outputs in standard formats for downstream analysis

## Method in brief
sRNAfrag operates in three modules. P1 processes raw reads: UMI handling and adapter removal (UMI-tools, AdapterRemoval), alignment to transcriptome with bowtie (allowing up to 3 mismatches, reporting up to 10000 alignments), extraction and sorting with SAMtools, and generation of a lookup table with license-plate IDs based on fragment sequence. S1 corrects for multi-mapping by dividing counts by number of potential source loci, applies filtering (minimum 5 adjusted counts), and generates sequence logos per fragment length. P2 merges overlapping fragments into clusters using a bipartite star graph approach with a minimum cluster size of 10 nt, compiles summary reports, and enables cross-species comparison.

For peak calling, sRNAfrag includes a smoothing function to prevent spurious peaks near dominant ones and a sandwich-zero correction that assigns sandwiched zero-count positions the count of adjacent loci. Cross-species conservation analysis compares fragment sequences across species using Hamming distance metrics and shared fragment detection.

## Target venue
Briefings in Bioinformatics
