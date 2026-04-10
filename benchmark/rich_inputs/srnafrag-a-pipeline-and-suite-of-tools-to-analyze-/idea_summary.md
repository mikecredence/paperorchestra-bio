# Idea Summary: sRNAfrag: A pipeline and suite of tools to analyze fragmentation in small RNA sequencing data

## Working title
sRNAfrag: A pipeline and suite of tools to analyze fragmentation in small RNA sequencing data

## Core question
AbstractFragments derived from small RNAs such as small nucleolar RNAs hold biological relevance. However, they remain poorly understood, calling for more comprehensive methods for analysis. We developed sRNAfrag, a standardized workflow and set of scripts to quantify and analyze sRNA fragmentation of any biotype. In a benchmark, it is able to detect loci of mature microRNAs fragmented from precursors and, utilizing multi-mapping events, the conserved 5’ seed sequence of miRNAs which we believe 

## Motivation / gap
- 1IntroductionEvidence of transfer RNA (tRNA) fragmentation has been reported since at least 1969 [1].
- However, it was only recently that their functional roles in disease was revealed [2, 3].
- Fragmentation of other small RNAs (sRNAs) such as small nucleolar RNAs (snoRNAs) and ribosomal RNAs (rRNAs) have also been reported, majority of which are derived from the 3’ and 5’ ends of the primar
- While much of the sRNA fragment literature has been focused on tRNA derived fragments, there is rising evidence that fragments derived from other biotypes of sRNAs have a mechanistic role in disease a
- Reanalysis of Photoactivatable-Ribonucleoside-Enhanced Cross linking and Immunoprecipitation (PAR-CLIP) sequencing data sets have revealed that fragments derived from snoRNAs and rRNAs associate with 

## Core contribution (bullet form)
Extracted from abstract:
AbstractFragments derived from small RNAs such as small nucleolar RNAs hold biological relevance. However, they remain poorly understood, calling for more comprehensive methods for analysis. We developed sRNAfrag, a standardized workflow and set of scripts to quantify and analyze sRNA fragmentation of any biotype. In a benchmark, it is able to detect loci of mature microRNAs fragmented from precursors and, utilizing multi-mapping events, the conserved 5’ seed sequence of miRNAs which we believe may extraoplate to other small RNA fragments. The tool detected 1411 snoRNA fragment conservation events between 2/4 eukaryotic species, providing the opportunity to explore motifs and fragmentation patterns not only within species, but between. Availability: https://github.com/kenminsoo/sRNAfrag.

## Method in brief
5Methods5.1Pipeline Overview and Annotation Data SourcessRNAfrag can be broken down into three distinct parts which we have labeled as P1, S1, and P2 (Fig 5). Users specify the location of files, adapter sequences, which modules to run, etc. by modifying a YAML configuration file. YAML files are similar to JSON files. A modified annotation file in General Transfer Format (GTF), along with a folder of gzipped fastq files is used as an input.biorxiv;2023.08.19.553943v1/FIG5F5fig5Fig. 5.Pipeline WorkflowSummary of the sRNAfrag pipeline. Users first configure the pipeline by modifying an included YAML file. Users may also modify annotation files using included scripts if needed. Three modules, P1, S1, and P2, are used to processed raw gzipped fastq files to a final summary report while also generating figures.We have created and provided scripts that parse NCBI annotations. This was applied to three common model species, M. musculus, C. elegans, and A. thaliana [47]. Human annotations were derived from snoDB (snoRNA), RNAcentral (snRNA), and Integrated Transcript Annotation for small RNA (rRNA) [48–50]. All processing is documented on our public repository (https://github.com/kenminsoo/sRNAfrag). Methods for validating and combining annotations from multiple sources are discussed further in [Additional File 4] which can improve sRNAfrag’s utility. GNU Parallel accommodates for parallel processing [51].5.2P1 Module -Initial ProcessingRaw reads are processed for UMIs and adapters w

## Target venue
Briefings in Bioinformatics
