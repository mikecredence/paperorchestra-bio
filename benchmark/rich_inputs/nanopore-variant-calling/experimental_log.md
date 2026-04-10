# Experimental Log: Benchmarking reveals superiority of deep learning variant callers on bacterial nanopore sequence data

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsGenome and variant truthsetGround truth reference assemblies were generated for each sample using ONT and Illumina reads (see Genome assembly).Creating a variant truthset for benchmarking is challenging [24, 25].
- Instead of random mutations, we used a pseudo-real approach, applying real variants from a donor genome to the sample’s reference [25, 26].
- This approach has the advantage of a simulation, in that we can be certain of the truthset of variants, but with the added benefit of the variants being real differences between two genomes.For each sample, we selected a donor genome with average nucleotide identity (ANI; a measure of similarity bet
- We identified all variants between the sample and donor using minimap2 [27] and mummer [28], inter-sected the variant sets, and removed overlaps and indels longer than 50bp.
- While incorporating structural variation would be an interesting and useful addition to the current work, we chose to focus here on small (<50bp) variants.Table 1 summarises the samples used, the number of variants, and the ANI between each sample and its donor.
- We analysed 14 samples from different species, spanning a wide range of GC content (30–66%).
- Despite the variation in SNP counts (2102–57887), the number of indels was consistent across samples (see Suppl.
- Table S2 for details).biorxiv;2024.03.15.585313v3/TBL1T1tbl1Table 1.Summary of the ANI and number of variants found between each sample and its donor genome.Data qualityWe analysed ONT data basecalled with three different accuracy models – fast, high accuracy (hac), and super-accuracy (sup) – along 
- The median, unfiltered read identities, calculated by aligning reads to their respective assembly, are shown in Figure 1.
- Duplex reads basecalled with the sup model had the highest median read identity of 99.93% (Q32).
- The Qscore is the logarithmic transformation of the read identity, Q = −10 log10 P, where P is the read identity.
- This was followed by duplex hac (99.79% [Q27]), simplex sup (99.26% [Q21]), simplex hac (98.31% [Q18]), and simplex fast (94.09% [Q12]).
- Full summary statistics of the reads can be found in Supplementary Table S1.biorxiv;2024.03.15.585313v3/FIG1F1fig1Figure 1.Median alignment-based read identity (x-axis) for each sample (points) stratified by basecalling model (colours) and read type (y-axis).
- The Qscore is the logarithmic transformation of the read identity, Q = −10 log10 P, where P is the read identity.Which method is the best?For this study, we benchmarked the performance of seven variant callers on ONT sequencing data: BCFtools (v1.19 [29]), Clair3 (v1.0.5 [15]), DeepVariant (v1.6.0 [
- In addition, we called variants from each sample’s Illumina data using Snippy [32] to act as a performance comparison.Alignments of ONT reads to each sample’s mutated reference (see Genome and variant truth-set) were generated with minimap2 and provided to each variant caller (except Medaka, which t
- Variant calls were assessed against the truthset using vcfdist (v2.3.3 [33]), classifying each variant as true positive (TP), false positive (FP), or false negative (FN).
- Precision, recall, and the F1 score were calculated for SNPs and indels at each VCF quality score increment.
- Figure 2 displays the highest F1 scores for each variant caller across samples, basecalling models, read types, and variant types.biorxiv;2024.03.15.585313v3/FIG2F2fig2Figure 2.The highest F1 score for each sample (points), stratified by basecalling model (colours), variant type (rows), and read typ
- Note, longshot does not provide indel calls.The F1 score is the harmonic mean of precision and recall and acts as a good metric for overall evaluation.
- From Figure 2 we see that Clair3 and DeepVariant produce the highest F1 scores for both SNPs and indels with both read types.
- Unsurprisingly, the sup basecalling model leads to the highest F1 scores across all variant callers, though hac is not much lower.
- SNP F1 scores of 99.99% are obtained from Clair3 and DeepVariant on sup-basecalled data.
- For indel calls, Clair3 achieves F1 scores of 99.53% and 99.20% for sup simplex and duplex, respectively, while DeepVariant scores 99.61% and 99.22%.
- The higher depth of the simplex reads likely explains why the best duplex indel F1 scores are slightly lower than simplex (see How much read depth is enough?).
- The precision and recall values at the highest F1 score can be seen in Supplementary Figures S3 and S4 (see Suppl.
- Table S3 for a summary and S4 for full details) as well as results broken down by species for Clair3 with the sup model in Suppl.
- Reads basecalled with the fast model are an order of magnitude worse than the hac and sup models.Figure 3 shows the precision-recall curves for the sup basecalling model (see Suppl.
- Figures S8 and S9 for the hac and fast model curves, respectively) for each variant and read type – aggregated across samples to produce a single curve for each variant caller.
- Due to the right-angle-like shape of the Clair3 and DeepVariant curves, filtering based on low-value variant quality improves precision considerably for variant calls, without losing much recall.
- The best Clair3 and DeepVariant F1 scores are obtained with no quality filtering on sup data, except for indels from duplex data where a quality filter of 4 provides the best F1.
- Table S5 for the full details.biorxiv;2024.03.15.585313v3/FIG3F3fig3Figure 3.Precision and recall curves for each variant caller (colours and line styles) on sequencing data basecalled with the sup model, stratified by variant type (rows) and read type (columns) and aggregated across samples.
- Note, Longshot does not provide indel calls.A striking feature of Figure 2 and Figure 3 is the comparison of deep learning-based variant callers (Clair3, DeepVariant, Medaka, and NanoCaller) to Illumina.
- For all variant and read types with hac or sup data, these deep learning methods match or surpass Illumina, with median best SNP and indel F1 scores of 99.45% and 95.76% for Illumina.
- Clair3 and DeepVariant, in particular, perform an order of magnitude better.
- Fast model ONT data has a lower F1 score than Illumina, only achieving parity in the best case for SNPs.Understanding missed and false callsConventional wisdom may leave readers surprised at finding that ONT data can provide better variant calls than Illumina.
- In order to convince ourselves (and others) of these results, we investigate the main causes for this difference.Given the ONT read-level accuracy now exceeding Q20 (Figure 1; simplex sup), read length remains the primary difference between the two technologies.
- Figure S4 shows that Illumina’s lower F1 score is mainly due to recall rather than precision (Suppl.
- We hypothesised that Illumina errors are related to alignment difficulties in repetitive or variant-dense regions due to its shorter reads.Figure 4 shows that variant density and repetitive regions account for many false negatives, lowering recall.
- We define variant density as the number of variants (missed or called) in a 100bp window around each call.
- Figure 4a reveals a bimodal distribution of variant density for Illumina FNs, with a second peak at 20 variants per 100bp, unlike the distribution for TP and FP calls.
- In contrast, Clair3, a top-performing ONT variant caller, shows no bimodal distribution and few missed or false calls at this density (Figure 4b).
- Figure S10), as 20 variants per 100bp represent a larger portion of an Illumina read than an ONT read.biorxiv;2024.03.15.585313v3/FIG4F4fig4Figure 4.Impact of variant density and repetitive regions on Illumina variant calling.
- Variant density is the number of (true or false) variants in a 100bp window centred on a call.
- Illumina calls, aggregated across all samples are shown in a, while b shows Clair3 calls from simplex sup-basecalled reads at 100x depth.
- c) impact of repetitive regions on the F1 score (y-axis) for Clair3 (100x simplex sup) and Illumina.
- The x-axis indicates whether variants that fall within repetitive regions are excluded from the calculation of the F1 score.
- Points indicate the F1 score for a single sample.We also assessed the change in F1 score when masking repetitive regions of the genome (see Identifying repetitive regions).
- Due to their shorter length, Illumina reads struggle more with alignment in these regions compared to ONT reads [34].
- Figure S11 highlights missed variants and alignment gaps in Illumina data.
- This is further quantified by the increase in Illumina’s F1 score when repetitive regions are masked (Figure 4c), rising from 99.3% to 99.7%.
- In contrast, Clair3 100x simplex sup data shows only a 0.003% increase.In terms of ONT missed calls, a variant dense repetitive region in the E.
- coli sample ATCC_25922 was the cause of the simplex sup SNP outlier from Figure 2 (see Suppl.
- In addition, the duplex sup SNP outlier was caused by very low read depth for sample KPC2_202310 (K.
- Section S2).Indels have traditionally been a systematic weakness for ONT sequencing data; primarily driven by variability in the length of homopolymeric regions as determined by basecallers [9].
- Having seen the drastic improvements in read accuracy in Figure 1, we sought to determine whether false positive indel calls are still a byproduct of homopolymer-driven errors.When analysing Clair3, the best-performing ONT caller, we found that reads basecalled with the fast model often miscalculate
- Of the eight false indel calls by Clair3 on sup data, five were homopolymers and three occurred within one or two bases of another insertion with a similar sequence.
- The hac model improved over the fast model but still produced notable false indel calls, mainly miscalculating homopolymers by 1bp.
- DeepVariant showed a similar error profile to Clair3 (Suppl.
- Figure S13), with 8/11 false indels being homopolymers.
- Figure S15) and NanoCaller (Suppl.
- Figure S16) performed similarly, while BCFtools (Suppl.
- Figure S12) exhibited a persistent bias for homopolymeric indel errors, even with sup model reads.
- This indicates that while the sup basecaller reduces bias, deep learning methods like Clair3 and DeepVariant further mitigate it by training models to account for these systematic issues.
- An honourable mention goes to FreeBayes, a traditional variant caller that handles errors without inherent bias.biorxiv;2024.03.15.585313v3/FIG5F5fig5Figure 5.Relationship between indel length (y-axis) and homopolymer length (x-axis) for false positive (FP) indel calls for Clair3 100x simplex fast (
- Figures S17–S22), especially when compared to Illumina indel error profiles.How much read depth is enough?Having established the accuracy of variant calls from ‘full depth’ ONT datasets (100x), we investigated the required ONT read depth to achieve desired precision or recall, which varies by use ca
- This is particularly relevant for ONT, where sequencing can be stopped in real-time once ‘sufficient’ data is obtained.We subsampled each ONT read set with rasusa (v0.8.0 [35]) to average depths of 5, 10, 25, 50, and 100x and called variants with these reduced sets.
- Due to limited duplex depth, 50x was the maximum used for duplex reads, while 100x was used for simplex reads.Figure 6 and Figure 7 show F1 score, precision, and recall as functions of read depth for SNPs and indels.
- Precision and recall decrease as read depth is reduced, notably below 25x.
- Remarkably, Clair3 or DeepVariant on 10x ONT sup simplex data provides F1 scores consistent with, or better than, full-depth Illumina for both SNPs and indels (see Table S1 for Illumina read depths).
- The same is true for duplex hac or sup reads.biorxiv;2024.03.15.585313v3/FIG6F6fig6Figure 6.Effect of read depth (x-axis) on the highest SNP F1 score, and precision and recall at that F1 score (y-axis), for each variant caller (colours).
- Bars on each point at each depth depict the 95% confidence interval.
- The horizontal red dashed line is the full-depth Illumina value for that metric, with the red bands indicating the 95% confidence interval.biorxiv;2024.03.15.585313v3/FIG7F7fig7Figure 7.Effect of read depth (x-axis) on the highest indel F1 score, and precision and recall at that F1 score (y-axis), f
- Bars on each point at each depth depict the 95% confidence interval.
- The horizontal red dashed line is the full-depth Illumina value for that metric, with the red bands indicating the 95% confidence interval.With 5x of ONT read depth the F1 score is lower than Illumina for almost all variant caller and basecalling models.
- However, BCFtools surprisingly produces SNP F1 scores on par with Illumina on duplex sup reads.
- Despite the inferior F1 scores across the board at 5x, SNP precision remains above Illumina with duplex reads for all methods except NanoCaller, and calls from Clair3 and DeepVariant simplex sup data.What computational resources do I need?The final consideration for variant calling is the required c
- Additionally, if working with raw (pod5) ONT data, basecalling is also a resource-intensive step.Figure 8 shows the runtime (seconds per megabase of sequencing data) and maximum memory usage for read alignment and variant calling (see Suppl.
- Figure S23 and Table S7 for basecalling GPU runtimes).
- DeepVariant was the slowest (median 5.7s/Mbp) and most memory-intensive (median 8GB), with a runtime of 38 minutes for a 4Mbp genome at 100x depth.
- FreeBayes had the largest runtime variation, with a maximum of 597s/Mbp, equating to 2.75 days for the same genome.
- In contrast, basecalling with a single GPU using the super-accuracy model required a median runtime of 0.77s/Mbp, or just over 5 minutes for a 4Mbp genome at 100x depth.
- Clair3 had a median memory usage of 1.6GB and a runtime of 0.86s/Mbp (<6 minutes for a 4Mbp 100x genome).
- Table S6.biorxiv;2024.03.15.585313v3/FIG8F8fig8Figure 8.Computational resource usage of alignment and each variant caller (y-axis and colours).

## Tables

### Table 1.
> Summary of the ANI and number of variants found between each sample and its donor genome.


## Figure Descriptions

### Figure 1.
Median alignment-based read identity (x-axis) for each sample (points) stratified by basecalling model (colours) and read type (y-axis). The Qscore is the logarithmic transformation of the read identity, Q = −10 log10 P, where P is the read identity.

### Figure 2.
The highest F1 score for each sample (points), stratified by basecalling model (colours), variant type (rows), and read type (columns). Illumina results (green) are included as a reference and do no have different basecalling models or read types. Note, longshot does not provide indel calls.

### Figure 3.
Precision and recall curves for each variant caller (colours and line styles) on sequencing data basecalled with the sup model, stratified by variant type (rows) and read type (columns) and aggregated across samples. The curves are generated by using increasing variant quality score thresholds to fi

### Figure 4.
Impact of variant density and repetitive regions on Illumina variant calling. Variant density is the number of (true or false) variants in a 100bp window centred on a call. a and b) the distribution of variant densities for true positive (TP), false positive (FP) and false negative (FN) calls. The y

### Figure 5.
Relationship between indel length (y-axis) and homopolymer length (x-axis) for false positive (FP) indel calls for Clair3 100x simplex fast (top left), hac (top right), and sup (lower left) calls. Illumina is shown in the lower right for reference. The vertical red line indicates the threshold above

### Figure 6.
Effect of read depth (x-axis) on the highest SNP F1 score, and precision and recall at that F1 score (y-axis), for each variant caller (colours). Each column is a basecall model and read type combination. The grey bars indicate the number of samples with at least that much read depth in the full rea

### Figure 7.
Effect of read depth (x-axis) on the highest indel F1 score, and precision and recall at that F1 score (y-axis), for each variant caller (colours). Each column is a basecall model and read type combination. The grey bars indicate the number of samples with at least that much read depth in the full r

### Figure 8.
Computational resource usage of alignment and each variant caller (y-axis and colours). The top panel shows the maximum memory usage (x-axis) and the lower panel shows the runtime as a function of the CPU time (seconds) divided by the number of basepairs in the readset (seconds per megabasepairs; x-

## References
Total references in published paper: 50

### Key References (from published paper)
- ‘Beyond the SNP Threshold: Identifying Outbreak Clusters Using Inferred Transmissions’ (, 2019)
- Oxford nanopore sequencing in clinical microbiology and infection diagnostics’ (, 2021)
- ‘The 2021 WHO catalogue of Mycobacterium tuberculosis complex mutations associated with drug resista (, 2022)
- ‘Automated Reconstruction of Whole-Genome Phylogenies from Short-Sequence Reads’ (, 2014)
- ‘Key parameters for genomics-based real-time detection and tracking of multidrug-resistant bacteria: (, 2021)
- ‘An ISO-certified genomics workflow for identification and surveillance of antimicrobial resistance’ (, 2023)
- ‘Mobile real-time surveillance of Zika virus in Brazil’ (, 2016)
- ‘Nanopore Sequencing as a Rapidly Deployable Ebola Outbreak Tool’ (, 2016)
- Sequencing DNA with nanopores: Troubles and biases’ (, 2021)
- ‘Comparison of R9.4.1/Kit10 and R10/Kit12 Oxford Nanopore flowcells and chemistries in bacterial gen (, 2023)
- ‘Evaluation of the accuracy of bacterial genome reconstruction with Oxford Nanopore R10.4.1 long-rea (, 2024)
- ‘Oxford Nanopore R10.4 long-read sequencing enables the generation of near-finished bacterial genome (, 2022)
- Longshot enables accurate variant calling in diploid genomes from single-molecule long read sequenci (, 2019)
- ‘Symphonizing pileup and full-alignment for deep learning-based long-read variant calling’ (, 2022)
- ‘NanoCaller for accurate detection of SNPs and indels in dificult-to-map regions from long-read sequ (, 2021)
- ‘Variant calling and benchmarking in an era of complete human genome sequences’ (, 2023)
- ‘PrecisionFDA Truth Challenge V2: Calling variants from short and long reads in dificult-to-map regi (, 2022)
- ‘Benchmarking variant callers in next-generation and third-generation sequencing analysis’ (, 2021)
- ‘A universal SNP and small-indel variant caller using deep neural networks’ (, 2018)
- ‘Discovering multiple types of DNA methylation from bacteria and microbiome using nanopore sequencin (, 2021)
- Generalizable characteristics of false-positive bacterial variant calls’ (, 2021)
- ‘Genomic diversity affects the accuracy of bacterial single-nucleotide polymorphism–calling pipeline (, 2020)
- ‘Genomic variant benchmark: if you cannot measure it, you cannot improve it’ (, 2023)
- ‘Toward better understanding of artifacts in variant calling from high-coverage samples’ (, 2014)
- ‘A synthetic-diploid benchmark for accurate variant-calling evaluation’ (, 2018)
- ‘Minimap2: pairwise alignment for nucleotide sequences’ (, 2018)
- ‘MUMmer4: A fast and versatile genome alignment system’ (, 2018)
- ‘Twelve years of SAMtools and BCFtools’ (, 2021)
- vcfdist: accurately benchmarking phased small variant calls in human genomes’ (, 2023)
- Repetitive DNA and next-generation sequencing: computational challenges and solutions’ (, 2012)

## Ground Truth Reference
- Figures: 8
- Tables: 1
- References: 50