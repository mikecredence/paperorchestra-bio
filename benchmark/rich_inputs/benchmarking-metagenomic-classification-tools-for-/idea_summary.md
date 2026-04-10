# Idea Summary: Comprehensive benchmarking of metagenomic classification tools for long-read sequencing data

## Working title
Comprehensive benchmarking of metagenomic classification tools for long-read sequencing data

## Core question
AbstractBackgroundLong reads have gained popularity in the analysis of metagenomics data. Therefore, we comprehensively assessed metagenomics classification tools on the species taxonomic level. We analysed kmer-based tools, mapping-based tools and two general-purpose long reads mappers. We evaluated more than 20 pipelines which use either nucleotide or protein databases and selected 13 for an extensive benchmark. We prepared seven synthetic datasets to test various scenarios, including the pres

## Motivation / gap


## Core contribution (bullet form)
Extracted from abstract:
AbstractBackgroundLong reads have gained popularity in the analysis of metagenomics data. Therefore, we comprehensively assessed metagenomics classification tools on the species taxonomic level. We analysed kmer-based tools, mapping-based tools and two general-purpose long reads mappers. We evaluated more than 20 pipelines which use either nucleotide or protein databases and selected 13 for an extensive benchmark. We prepared seven synthetic datasets to test various scenarios, including the presence of a host, unknown species and related species. Moreover, we used available sequencing data from three well-defined mock communities, including a dataset with abundance varying from 0.0001% to 20% and six real gut microbiomes.ResultsGeneral-purpose mappers Minimap2 and Ram achieved similar or better accuracy on most testing metrics than best-performing classification tools. They were up to ten times slower than the fastest kmer-based tools requiring up to four times less RAM. All tested tools were prone to report organisms not present in datasets, except CLARK-S, and they underperformed in the case of the high presence of the host’s genetic material. Tools which use a protein database performed worse than those based on a nucleotide database. Longer read lengths made classification easier, but due to the difference in read length distributions among species, the usage of only the longest reads reduced the accuracy.The comparison of real gut microbiome datasets shows a similar abundance profiles for the same type of tools but discordance in the number of reported organisms and abundances between types. Most assessments showed the influence of database completeness on the reports.ConclusionThe findings indicate that kmer-based tools are well-suited for rapid analysis of long reads data. However, when heightened accuracy is essential, off-the-shelf mappers demonstrate slightly superior performance, albeit at a considerably slower pace. Nevertheless, a combination of diverse categories of tools and databases will likely be necessary to analyse complex samples. Discrepancies observed among tools when applied to real gut datasets, as well as a reduced performance in cases where unknown species or a significant proportion of the host genome is present in the sample, highlight the need for continuous improvement of existing tools. Additionally, regular updates and curation of databases are important to ensure their effectiveness.

## Method in brief
MethodsThis chapter describes the tools and assessment measures used and how we constructed the test datasets and databases.


## Target venue
BMC Bioinformatics
