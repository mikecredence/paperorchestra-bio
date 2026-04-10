# Experimental Log: Comprehensive benchmarking of metagenomic classification tools for long-read sequencing data

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsTested metagenomics classification pipelines could be roughly divided into four groups:
(1)kmer-based (Kraken2 [11], Bracken [12], Centrifuge [13], CLARK [14], CLARK-S [15]),(2)mapping-based (MetaMaps [16], MEGAN-LR with a nucleotide database [17], deSAMBA [18]) tailored for long reads,(3)gen
- Bracken [12] is a statistical method that computes species abundance using taxonomy labels assigned by Kraken/Kraken2.
- We adapted Minimap2 and Ram for metagenomics classifications.
- We assessed Minimap2 in both modes and Ram only in mapping mode.We also have reviewed k-SLAM [22], MetaPhlAn [23], ConStrains [24], PathoScope [25], KrakenUniq [26], Sigma [27], CCMetagen [28], and Gotcha [29], but they either crashed during the database creation or performed poorly on long-read dat
- MEGAN-LR using the DIAMOND [30] aligner and a protein database achieved worse results than MEGAN-LR with the LAST aligner (MEGAN-P), so we omitted it from the analysis.
- We did not evaluate web-based tools such as BugSeq [31].There are two main requirements for classification algorithms: identifying present organisms using a taxonomic rank (species in this work) and evaluating their abundances.
- Therefore, using existing PacBio and ONT reads, we synthesised several simple to more complex communities containing 3 to 50 species, varying from highly abundant to very sparse.
- –Datasets ONT1, PB1, and PB4 reflect a community of bacteria without eukaryotic species.–Datasets ONT2 and PB2 reflect metagenomics datasets with one or more eukaryotic species and many bacterial species, respectively.–Dataset PB3 reflects a community with predominantly human reads (99 %) and two lo
- For the PB1+NEG dataset, we created randomized reads from the human genome.
- For the PB2 dataset, we added reads from D.
- It is important to notice that while we used reads sequenced with older PacBio technologies for synthesised communities, mock communities were sequenced using Sequel 2 HiFi technology.
- Three datasets are sequenced by ONT technologies (SRR15489009, SRR15489011 and SRR15489017) and three by PacBio HiFi (Sample10, Sample20 and Sample21).The tools were tested in four areas:
Read level classification – how accurately can they classify each read.Abundance estimation – how well can they 
- Figure 1 shows that off-the-shelf mappers and mapping-based tools outperformed others on almost all datasets and both levels.
- Differences between them and kmer-based tools varied up to 10 % at species levels.
- Pipelines which use a protein database underperformed significantly.biorxiv;2020.11.25.397729v3/FIG1F1fig1Figure 1.Read level classification accuracy, comparison between species and genus level classification.Kmer-based are represented in red, mapping-based tools are represented in blue and protein 
- Results for MEGAN-N are unavailable for the PB3 dataset.Minimap2 with alignment outperformed other tools, followed by mapping-based tools (deSAMBA, Metamaps) and Ram.
- Interesting cases were ONT1 and ONT2 datasets which contain reads of two species of the Vibrio genus that were not in databases.
- Since there were other similar species of the Vibrio genus in the database, some tools, such as MEGAN-N and Minimap2 in both modes, tended to assign those reads to them.
- Therefore, the results on the ONT1 and ONT2 datasets for these four tools were almost reversed when analysing genus and species levels.
- CLARK-S and Ram had the highest accuracy when inspecting the ONT1 and ONT2 datasets at the species level and among the lowest when examining the dataset at the genus level.
- In contrast, Minimap2 and MEGAN-N had the highest accuracy at the genus level but performed worse at the species level.Since there is an imbalance in the number of reads per species, we additionally calculated the F1 score for each class (organism in the sample) separately and averaged them (F1 macr
- Using F1 macro average instead of accuracy shows a similar pattern for most datasets with Minimap2 (both modes) surpassing others and a narrower distance between mapping-based and kmer-based tools (Supplementary Figure 1).We further investigate the influence of read length on classification.
- We only present analysis for Minimap2 with alignment, the most accurate tool at the read level.
- As evident from Figure 2, increasing the read length led to a higher classification level.
- Additional analysis on how using 30% of longest reads impacted the results is provided in Supplementary Table 1.biorxiv;2020.11.25.397729v3/FIG2F2fig2Figure 2.Comparison between classification accuracy and read length.The figure shows Q1, median and Q3 read length for true positive and false positiv
- The results shown in the figure were obtained using Minimap2 with alignment and Kraken.Abundance estimationAbundance estimation is arguably the most important assessment.
- However, long-read sequencing technologies produce reads whose length might vary greatly, especially for ONT technology.In the analysis, we compared L1 distances between reported and declared abundances using relative read count, genome length and genome count.
- Supplementary Table 5 shows the theoretical composition of Zymo and ATCC datasets.Table 1 shows that the results are mostly consistent, considering different ways of abundance calculation.
- While it is narrow for PacBio HiFi reads, it is wide and skewed for ONT reads.biorxiv;2020.11.25.397729v3/TBL1T1tbl1Table 1.Comparison of the total abundance estimation error between relative read count, relative genome length and relative genome count abundances.The table shows the total abundance 
- The total error was calculated as the L1 distance between specific types of abundances reported by tools and the abundances declared by vendors and summed up across all organisms (all present and all reported).
- The comparison of the abundance estimation error is given in Table 2.biorxiv;2020.11.25.397729v3/TBL2T2tbl2Table 2.Comparing abundance estimation error for the database with the human genome and the database without the human genome.The table shows the total abundance estimation error for datasets P
- The error was calculated as the L1 distance between abundances calculated for each tool and true abundances.
- Each dataset name is followed by the percentage of human reads in that dataset in parentheses.Table 2 shows that when the human reads’ percentage is lower, tools such as CLARK-S, Ram, Metamaps, Kaiju, and MEGAN-P were unaffected by the presence of the human genome in the database.
- However, as the human genome reads’ percentage approaches 100 %, the accuracy of most tools significantly declines.
- Metamaps performed best on ONT2, Ram on PB2, and CLARK-S on PB4.
- It is important to note that Bracken significantly improved Kraken2 results for PacBio datasets.To analyse abundance error in more detail, we separately calculated the error for species present in the sample and for species not present in the sample but incorrectly reported by tools.
- We calculated the L1 distance between reported and expected abundance in percentages.
- Figure 3 and Supplementary Figure 2 show the results.biorxiv;2020.11.25.397729v3/FIG3F3fig3Figure 3.Abundance estimation error on species level – heatmap.Abundance estimation error was calculated by comparing the abundances calculated for each tool to the ground truth.
- It is important to note that in the case of the PB_Zymo dataset, species Veillonella rogosae (taxId: 423477) and Prevotella corporis (taxId: 28128), which represent 19.94 % and 6.26 %, respectively, were not present in the database.Minimap2 align outperformed other tools in absolute differences betw
- In most of the datasets, its mean difference was below 2%, yet, other tools were not far away.
- One of the reasons is the lack of two species in databases, Veillonella rogosae and Prevotella corporis, which represent more than 26 % of the dataset.
- However, even if we did not consider these two species, distributions of errors for this dataset were much wider than in another PacBio mock community dataset, PB_ATCC (Supplementary Figure 2).Regarding species not present in the dataset, CLARK-S surpassed others, followed by MetaMaps, Ram and MEGAN
- Minimap2 was more prone to reporting organisms not present in the sample.
- Table 3 shows how the number of true and false positive organism detections is related to a threshold – a minimal number of assigned reads required to consider an organism as detected.
- The table shows that kmer-based tools, Kraken2 and Centrifuge, often reported a huge number of species, usually an order of magnitude more than mapping-based tools and mappers, except the Minimap2 map.
- In the case of very low abundance species, such as in datasets PB4 (lowest proportion of reads – 0.005 %) and ONT1 (lowest proportion of reads – 0.01 %), PB_Zymo (lowest proportion of reads – 0.0001%) and PB_ATCC (lowest proportion of reads – 0.02%) increasing the threshold lowered the number of tru
- Results for MEGAN-N are unavailable for datasets PB3, PB_Zyme and PB_ATCC.Additionally, we analysed abundances and the number of correctly identified organisms for those species with abundances lower than 1 %.
- Results, presented in Supplementary Table 9, show that there is no clear winner in the abundance estimation accuracy.
- Yet, Minimap2 align outperformed others in two out of four datasets.
- Furthermore, Kraken2 and Minimap2 recognised the most present organisms in all samples except PB_Zymo, where Kraken2 correctly predicted one more.
- The results of both analyses for datasets Sample10, Sample20, Sample21, SRR15489009, SRR15489011 and SRR15489017 are shown in Figure 4.biorxiv;2020.11.25.397729v3/FIG4F4fig4Figure 4.2D PCA and dendrograms for real datasets.Abundance estimation data for each tool is viewed as a vector, with component
- The Figure displays 2D PCA plots and hierarchical clustering dendrograms for all real datasets.
- Data for MEGAN-P is unavailable on datasets SRR15489009 and SRR15489017.From Figure 4, it can be seen that kmer-based tools such as Kraken2, Bracken and Centrifuge performed similarly.
- While for PacBio HiFi datasets, mappers Minimap2 and Ram, and Metamaps performed similarly, for ONT datasets Ram and Metamaps performed differently than Minimap2 tools.
- CLARK-S, Kaiju and MEGAN-P were far from other tools.We analysed the ten most abundant species for each pipeline for the SRR15489009 (PacBio) dataset to better understand the differences between pipelines.
- Results are presented in Supplementary Table 11.
- Although belonging to the core [32] of the human gut, Lachnospiraceae bacterium species are not found in the protein database.
- Protein database does not contain another prevalent [33] human gut bacteria – Eubacterium rectale.
- Furthermore, while mappers and all mapping-based tools recognised it (average abundance of 5 %), none of the kmer-based tools did the same.
- Other important human gut species, such as Prevottela copri [34] and Ruminococcus torques [35], were not present in the NCBI-NT database.During the analysis of the SRR15489009 (PacBio) dataset’s results, we noticed significant discordance in abundances for Faecalibacterium prausnitzii [36] between t
- While kmer-based tools’ abundances were 12%-14% (CLARK-S with 25% is an outlier), most mappers and mapping base tools’ abundances were 17%-18%.
- Kaiju and MEGAN-P report 11% and 19%, respectively.A further interesting question for real gut datasets is the actual number of species present in the sample.
- Supplementary Table 3 shows the percentage of reads classified for all datasets and tools.
- The least number of classified reads were for three ONT gut samples, where best-performing tools rarely classified above 50% of reads.
- The numbers for PacBio samples were even above 80% for some tools.
- The remaining 20 % of unclassified reads might be explained by missing species in databases (Supplementary Table 10).While Supplementary Table 4 shows the number of detected species for each real dataset and each tool, Table 4 shows a more detailed analysis of real gut samples.
- Since they performed better for real mock community datasets PB_Zymo and PB_ATCC, we hypothesise the number of species possible to detect for selected sequencing depth was closer to the numbers they reported and probably even smaller.biorxiv;2020.11.25.397729v3/TBL4T4tbl4Table 4.The number of detect
- Results for MEGAN-P are unavailable on datasets SRR15489009 and SRR15489017.Computational resource usageResults for running time and memory usage are presented in Table 5.
- Compared to mappers Minimap2 and especially Ram, the difference between the best kmer-based tools and mappers was below one order of magnitude.
- Kraken2, Centrifuge, Minimap2, MEGAN-P and MEGAN-N, for most datasets, used 2-3 times more memory.
- deSAMBA, CLARK, CLARK-S and MetaMaps used 10-15 times more memory.biorxiv;2020.11.25.397729v3/TBL5T5tbl5Table 5.Resource usage.The table shows running time (in seconds) and memory usage (in GB) for all tools and datasets.
- The table shows the minimum and maximum values for both measures for all synthetic and real datasets, which are about 1Gbp in size.biorxiv;2020.11.25.397729v3/TBL6T6tbl6Table 6.Execution time for datasets of different sizes.Tools were run on three mock community datasets (ONT_Zymo, PB_ATCC and PB_Zy
- All datasets used in the main part of the paper were subsampled to 1Gbp (file size is about 2GB) to make the testing viable even for slower tools.
- However, all three datasets were used in their original size, subsampled to half of the original dataset and subsampled to 1Gbp.
- The table shows execution time in seconds.We additionally tested Ram and Minimap2 execution times by mapping only one sequence to the whole database file.
- The execution time for both was around 1000 seconds, suggesting that the database parsing and indexing took that much time.
- The results are presented in Table 5.
- Even for the largest datasets, Ram was still, at most, around 10x slower than Kraken2, the fastest kmer-based tool.
- Although Centrifuge was the fastest tool when analysing execution times presented in Table 5, Kraken2 had the lowest execution times when tested on larger datasets.
- On larger datasets, where the actual sequence classification took a greater part of the execution time, Kraken2 outperformed Centrifuge.All resource usage measurements were performed on a machine with sufficient disk space, 775 GB RAM and 256 virtual CPUs (2 x AMD EPYC 7662 64-Core Processor).
- Measurements were performed using 12 threads for 7 synthetic and 3 mock datasets and using 32 threads for 6 gut datasets.

## Tables

### Table 1.
> Comparison of the total abundance estimation error between relative read count, relative genome length and relative genome count abundances.The table shows the total abundance estimation error for moc


### Table 2.
> Comparing abundance estimation error for the database with the human genome and the database without the human genome.The table shows the total abundance estimation error for datasets PB2, PB3 and ONT


### Table 3.
> True positive and false positive organism detection.The table shows true and false positive organism detections for three different thresholds: 1, 10 and 50. A threshold represents the number of reads


### Table 4.
> The number of detected species for real gut microbiome datasets.The table shows the number of detected species on real datasets for three different thresholds: 1, 10, and 50. A threshold represents th


### Table 5.
> Resource usage.The table shows running time (in seconds) and memory usage (in GB) for all tools and datasets. The table shows the minimum and maximum values for both measures for all synthetic and rea


### Table 6.
> Execution time for datasets of different sizes.Tools were run on three mock community datasets (ONT_Zymo, PB_ATCC and PB_Zymo) subsampled to three different sizes to test their scalability. All datase


## Figure Descriptions

### Figure 1.
Read level classification accuracy, comparison between species and genus level classification.Kmer-based are represented in red, mapping-based tools are represented in blue and protein tools are represented in green. Plot a) shows species-level classification for which reads are considered correctly

### Figure 2.
Comparison between classification accuracy and read length.The figure shows Q1, median and Q3 read length for true positive and false positive read classifications for each dataset. False positive read lengths are considered only for organisms in the database. The results shown in the figure were ob

### Figure 3.
Abundance estimation error on species level – heatmap.Abundance estimation error was calculated by comparing the abundances calculated for each tool to the ground truth. Errors were calculated separately within the dataset and outside the dataset. The total abundance estimation error is represented 

### Figure 4.
2D PCA and dendrograms for real datasets.Abundance estimation data for each tool is viewed as a vector, with components being abundance estimations for each organism (in and out of the sample). The data was transformed using PCA, and the two most significant components were plotted. Hierarchical clu

### Figure 5.
Read alignment.Read alignment consists of three steps (1) Indexing and kmer search, (2) Chaining and scoring (3) Alignment. Kmer-based tools use only the first step, and usually, they do not care about the position in the genome. Mapping-based tools use the first and second steps, which increase acc

## References
Total references in published paper: 45

### Key References (from published paper)
- Shotgun metagenomics, from sampling to analysis (, 2017)
- Animals in a bacterial world, a new imperative for the life sciences (, 2013)
- Microbial community profiling for human microbiome projects: Tools, techniques, and challenges (, 2009)
- Hybrid metagenomic assembly enables high-resolution analysis of resistance determinants and mobile e (, 2019)
- Short– and long-read metagenomics expand individualized structural variations in gut microbiomes (, 2022)
- Finding the right fit: evaluation of short-read and long-read sequencing approaches to maximize the  (, 2022)
- Testing the advantages and disadvantages of short– and long-read eukaryotic metagenomics using simul (, 2020)
- Ultra-deep, long-read nanopore sequencing of mock microbial community standards (, 2019)
- Benchmarking the MinION: Evaluating long reads for microbial profiling (, 2020)
- Evaluation of taxonomic classification and profiling methods for long-read shotgun metagenomic seque (, 2022)
- Improved metagenomic analysis with Kraken 2 (, 2019)
- Bracken: estimating species abundance in metagenomics data. PeerJ Comput Sci (, 2017)
- Centrifuge: rapid and sensitive classification of metagenomic sequences (, 2016)
- CLARK: fast and accurate classification of metagenomic and genomic sequences using discriminative k- (, 2015)
- Higher classification sensitivity of short metagenomic reads with CLARK-S (, 2016)
- Strain-level metagenomic assignment and compositional estimation for long reads with MetaMaps (, 2019)
- MEGAN-LR: new algorithms allow accurate binning and easy interactive exploration of metagenomic long (, 2018)
- Fast and Accurate Classification of Meta-Genomics Long Reads With deSAMBA (, 2021)
- Minimap2: pairwise alignment for nucleotide sequences (, 2018)
- Time– and memory-efficient genome assembly with Raven. Nature Computational Science (, 2021)
- Fast and sensitive taxonomic classification for metagenomics with Kaiju. Nat Commun (, 2016)
- k-SLAM: accurate and ultra-fast taxonomic classification and gene identification for large metagenom (, 2017)
- MetaPhlAn2 for enhanced metagenomic taxonomic profiling (, 2015)
- ConStrains identifies microbial strains in metagenomic datasets (, 2015)
- PathoScope 2.0: a complete computational framework for strain identification in environmental or cli (, 2014)
- KrakenUniq: confident and fast metagenomics classification using unique k-mer counts (, 2018)
- Sigma: strain-level inference of genomes from metagenomic analysis for biosurveillance (, 2015)
- CCMetagen: comprehensive and accurate identification of eukaryotes and prokaryotes in metagenomic da (, 2020)
- GOtcha: a new method for prediction of protein function assessed by the annotation of seven genomes (, 2004)
- Fast and sensitive protein alignment using DIAMOND (, 2014)

## Ground Truth Reference
- Figures: 5
- Tables: 6
- References: 45