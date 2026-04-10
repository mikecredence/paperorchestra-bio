# Experimental Log: sRNAfrag: A pipeline and suite of tools to analyze fragmentation in small RNA sequencing data

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 2Results2.1sRNAfrag Effectively Calls Peaks and CountssRNAfrag extracts both counts and potential start/end loci for users.
- sRNAfrag had 597 pre-miRNAs with supporting fragments after filtering compared to the 642 that FlaiMapper obtained.
- Of these pre-miRNAs, sRNAfrag called 94.7% and 86.5% of start and end loci within 1 bp of their true position (Fig 1A).
- This is comparable to FlaiMapper which called 92.4% and 85.2% of start and end loci in our dataset with default settings [16].
- Rather, count peaks exist at positions that do not exactly match loci in miRbase as can be seen in [Additional Figure 1].biorxiv;2023.08.19.553943v1/FIG1F1fig1Fig.
- 1.Peak and Count Calling PerformanceA) Proportion of detected peaks vs.
- C) Merged counts after P2 Module vs.
- AASRA generated counts.Comparing the counts used to call peaks to that of AASRA shows that sRNAfrag utilizes counts that are comparable to more standard small RNA-seq workflows during peak calling, affirming that, in our pipeline, loci-count relationships are properly preserved and used (Fig 1B).
- A benchmark of the AASRA method was conducted on a synthetic dataset presented in [Additional Figure 2].
- Thus, we show that when counts are merged (fragments that are clustered together), results are closer to that of AASRA (Fig 1C).
- We infer that the underestimation of slope (0.983) and negative intercept is partially due to the AASRA pipeline’s behavior to assign alignments that have a 1 n.t.
- Because of this, starting positions prior to the first loci of the annotation are counted as being apart of that transcript whereas sRNAfrag does not as a sequence preceding a transcript is not considered when generating the lookup table.2.2Multi-Mapping Events Reveal Potentially Important Conserved
- The 5’ seed sequence of miRNAs represent the functionally important portion of the molecule [24].
- Furthermore, miRNA families, arising from duplications events, likely are subject to evolutionary pressures to retain the same seed sequence [25].
- The mir-30 family had four (3 are depicted, with the final being 1 n.t.
- longer) fragments that were shared amongst all potential sources (Fig 2A).
- Each were aligned at their 5’ ends, representing the beginning of the 5’ derived mature miRNA (hsamiR-30c-5p).
- We investigate all clusters of fragments with more than one potential source transcript and found that the 5’ end of the most counted fragment match the most commonly shared fragment 65.9% of the time (Fig 2B).biorxiv;2023.08.19.553943v1/FIG2F2fig2Fig.
- 2.Comparative Analysis of Fragments Involved in Multi-Mapping EventsA-B) Black triangles depict the most highly expressed fragment of the source transcript.
- Three clustered fragments shared between has-miR-30b/30c and one fragment shared between 12 isoforms of snoRD115 whose 5’ end is the same as the most conserved fragment is depicted.
- C-D) Piechart depicting the proportion of merged fragments (with more than one possible source transcript) whose most commonly shared fragment between sources has a the same 3’ or 5’ loci as the most counted transcript.
- Greater than 0 represents occurrences when the most found and counted transcript do not match.We attempted to apply the same logic to a fragment derived from snoRD115.
- The fragment in question was shared between 12 source transcripts that had slight differences in sequence (Fig 2B).
- Exploring the location of these fragmentation events showed that 40% of conservation events were at terminal portion of the source transcript compared to just 1.5% for miRNAs (Fig 2D).
- In the future, similar assignments could allow for better understanding of fragment biogenesis in other biotypes of small RNAs.2.3License Plating Allows Conserved Fragments to be DetectedGiven that orthologous snoRNA genes are fairly common, we decided to investigate if fragments of similar sequence
- Using this method, 1411 conservation events between two species were found with a hamming distance at most of 3, majority of which were fragments shared between M.
- sapiens (Fig 3A).biorxiv;2023.08.19.553943v1/FIG3F3fig3Fig.
- 3.Shared snoRNA Fragments between SpeciesSource transcripts are depicted with fragment source cluster loci highlighted in red.
- Derived from unassigned transcript 14429.
- sapiens snoRNA derived fragment, with hamming distance of 0 relative to M.
- Derived from NR 002172.1 (SNORD15A).Out of the 1411, we chose to investigate one shared fragment derived from the 3’ ends of primary transcripts in 3/4 of our chosen species.
- RNAfold and RNAplot was used to generate minimum free energy structures of source transcripts [27].
- The cluster start and end are highlighted on the secondary structure, as opposed to the fragment start and end (Fig 3B-D).
- elegans snoRNA was the most different out of the three, with a hamming distance of two (Fig 3B).
- musculus shared the same sequence (Fig 3C-D).
- Fragments were derived from SNORD15A which is annotated for M.
- This is a proof of concept that attempting to explore fragmentation between species may not only be fruitful, but is also made easier with sRNAfrag as its outputs can be joined and used in scripts such as the one used in this section.2.4sRNAfrag Run Time Scales Linearly for Multiple Biotypes and Spe
- The amount of time that sRNAfrag takes exhibits a linear relationship with the number of fragmnts discovered in a manner that is mostly independent of the number of sequenced reads (Fig 4A).
- For every 1000 additional unique fragments discovered, users can expect an additional 23 seconds of run time.
- This is slower than reported times in SURFr, taking an average of 4.5 minutes to complete jobs [22].
- However, our pipeline realigns fragments back to the reference genome which takes significant amount of time.biorxiv;2023.08.19.553943v1/FIG4F4fig4Fig.
- 4.sRNAfrag Run Time and Human Outside Map CompositionA) Overall run time in minutes.
- B-D) The composition of out of space maps for rRNA, snRNA, and snoRNA fragments in humans.Especially large run times were observed for rRNA fragments, which is unsurprising given that the pipeline processed 20,000-200,000 fragments.
- This is because when the number of fragments surpasses 8000, sampling of the smallest fragments is conducted, which is slow.
- We found that most reads from fragments map to piRNAs (Fig 4B-D).
- Interesting, snRNA U1 has been found to be similar to that of tandem repeat tRNA which may explain why snRNA fragment alignments were annotated as tRNAs [28].
- However, this led to memory issues, especially as possible fragments would range in the tens of millions (Table 1).
- Furthermore, fragments that exist typically represent only a small fraction of possible sequences in nearly every species tested.biorxiv;2023.08.19.553943v1/TBL1T1tbl1Table 1.Possible maximum number of fragments generated by provided annotation files and percentage found in test databiorxiv;2023.08.
- The start locations are standardized to fall between 0-1 and averaged if more than one position exists.
- Additional columns not shown contain information about 5’ and 3’ flanking sequences.
- If a fragment can originate from more than one source in the provided annotation, all information is delimited with a special character in the sources column.The upper maximum number of fragments that could be generated in the lookup table can be calculated with equation 1 when m is maximum length, 
- reported that transcript length peaks at 2,065 bp over 92,696 transcripts and genes [30].
- Analyzing fragmentation over 20000 protein coding genes would yield a theoretical number of 1.3 billion possible fragments.
- Assuming that fragmentation of protein-coding gene follows the trend of snRNAs (0.06% of fragments out of all possible) for a total of 780,000 detected fragments, this would take about 5 hours to run.
- We previously found that lookup table generation occurs at a rate of 11,000 fragments / second.
- Ignoring memory limitations, lookup table generation alone would take 32 hours and would take up 252 GB of space.

## Tables

### Table 1.
> Possible maximum number of fragments generated by provided annotation files and percentage found in test data


### Table 2.
> Entries in the lookup table contain information regarding source transcript and the position from which it originates from. The start locations are standardized to fall between 0-1 and averaged if mor


### Table 3.
> Sample Information


## Figure Descriptions

### Fig. 1.
Peak and Count Calling PerformanceA) Proportion of detected peaks vs. Offset from truth for end and start loci. B) Peak calling counts vs. AASRA generated counts. Counts are unmerged and represent the unadjusted counts for that loci. C) Merged counts after P2 Module vs. AASRA generated counts.

### Fig. 2.
Comparative Analysis of Fragments Involved in Multi-Mapping EventsA-B) Black triangles depict the most highly expressed fragment of the source transcript. The red line depicts the most shared fragment between potential sources. Three clustered fragments shared between has-miR-30b/30c and one fragmen

### Fig. 3.
Shared snoRNA Fragments between SpeciesSource transcripts are depicted with fragment source cluster loci highlighted in red. A) Heatmap depicting number of shared fragments between four species, M. musculus (mm), H. sapiens (hs), A. thaliana (at), and C. elegans (ce). Diagonals are set to 0. B) Shar

### Fig. 4.
sRNAfrag Run Time and Human Outside Map CompositionA) Overall run time in minutes. B-D) The composition of out of space maps for rRNA, snRNA, and snoRNA fragments in humans.

### Fig. 5.
Pipeline WorkflowSummary of the sRNAfrag pipeline. Users first configure the pipeline by modifying an included YAML file. Users may also modify annotation files using included scripts if needed. Three modules, P1, S1, and P2, are used to processed raw gzipped fastq files to a final summary report wh

### Fig. 6.
Addressing The Smoothing and Sandwich ProblemA) Depiction of the adjustment with the smoothing function which prevents peaks from being called if large peaks exist close by. B) Sandwiched zeros are assigned to the same number of counts as the next loci under the assumption that sandwiched zeros tend

### Fig. 7.
Clustering AlgorithmAn example transcript is depicted with start and end loci labeled onto the sequence with detected peaks. Clusters are assigned using logic. Clusters must be at least 10 n.t. long before the id counter increases.

### 


## References
Total references in published paper: 61

### Key References (from published paper)
- RECONSTITU-TION OF ALANINE ACCEPTOR ACTIVITY FROM FRAGMENTS PRO-DUCED BY SPECIFIC CLEAVAGE OF tRNA A (, 1969)
- Mechanisms of tRNA-derived fragments and tRNA halves in cancer treatment resistance (, 2020)
- Comprehensive land-scape of tRNA-derived fragments in lung cancer (, 2022)
- Extensive terminal and asymmetric processing of small RNAs from rRNAs, snoRNAs, snRNAs, and tRNAs (, 2012)
- The snoRNA MBII-52 (SNORD 115) is processed into smaller RNAs and regulates alternative splicing (, 2010)
- Human snoRNA-93 is processed into a microRNA-like RNA that promotes breast cancer cell invasion (, 2017)
- MicroRNA-like snoRNA-Derived RNAs (sdRNAs) Promote Castration-Resistant Prostate Cancer (, 2022)
- Computational meta-analysis of ribosomal RNA frag-ments: potential targets and interaction mechanism (, 2021)
- The human box C/D snoRNA U3 is a miRNA source and miR-U3 regulates expression of sortin nexin 27 (, 2020)
- Argonaute Proteins: From Structure to Function in Development and Pathological Cell Fate Determinati (, 2020)
- Small RNAs derived from snoRNAs (, 2009)
- Multisite Evaluation of Next-Generation Methods for Small RNA Quantification (, 2020)
- AASRA: an anchor alignment-based small RNA annotation pipeline† (, 2021)
- MINTbase v2.0: a comprehensive database for tRNA-derived fragments that includes nuclear and mitocho (, 2018)
- MINTmap: fast and exhaustive profiling of nuclear and mitochondrial tRNA fragments from short RNA-se (, 2017)
- FlaiMapper: computational annotation of small ncRNA-derived fragments using RNA-seq high-throughput  (, 2015)
- MGcount: a total RNA-seq quantification tool to address multi-mapping and multi-overlapping alignmen (, 2022)
- Eukaryotic snoRNAs: A paradigm for gene expression flexibility (, 2009)
- Direct Sequencing of tRNA by 2D-HELS-AA MS Seq Reveals Its Different Isoforms and Dynamic Base Modif (, 2020)
- Primer extension coupled with fragment analysis for rapid and quantitative evaluation of 5.8S rRNA i (, 2021)
- Developmental Analysis of Spliceosomal snRNA Isoform Expression (, 2015)
- CCA addition by tRNA nucleotidyltransferase: polymerization without translocation? (, 1998)
- Stability of miRNA 5terminal and seed regions is correlated with experimentally observed miRNA-media (, 2012)
- Novel microRNA families expanded in the human genome (, 2013)
- snOPY: a small nucleolar RNA orthological gene database (, 2013)
- ViennaRNA Package 2.0 (, 2011)
- U1 snRNA: The evolution of its primary and secondary structure (, 1985)
- Identification of protein-protected mRNA fragments and structured excised intron RNAs in human plasm (, 2020)
- Gene Size Matters: An Analysis of Gene Length in the Human Genome (, 2021)
- An esti-mate of the total number of true human miRNAs (, 2019)

## Ground Truth Reference
- Figures: 8
- Tables: 3
- References: 61