{
  "statistical_sentences": [
    "This approach has the advantage of a simulation, in that we can be certain of the truthset of variants, but with the added benefit of the variants being real differences between two genomes.For each sample, we selected a donor genome with average nucleotide identity (ANI; a measure of similarity between two genomes) closest to 99.5% (see Truthset and reference generation).",
    "We analysed 14 samples from different species, spanning a wide range of GC content (30\u201366%).",
    "Duplex reads basecalled with the sup model had the highest median read identity of 99.93% (Q32).",
    "This was followed by duplex hac (99.79% [Q27]), simplex sup (99.26% [Q21]), simplex hac (98.31% [Q18]), and simplex fast (94.09% [Q12]).",
    "SNP F1 scores of 99.99% are obtained from Clair3 and DeepVariant on sup-basecalled data.",
    "For indel calls, Clair3 achieves F1 scores of 99.53% and 99.20% for sup simplex and duplex, respectively, while DeepVariant scores 99.61% and 99.22%.",
    "For all variant and read types with hac or sup data, these deep learning methods match or surpass Illumina, with median best SNP and indel F1 scores of 99.45% and 95.76% for Illumina.",
    "This is further quantified by the increase in Illumina\u2019s F1 score when repetitive regions are masked (Figure 4c), rising from 99.3% to 99.7%.",
    "In contrast, Clair3 100x simplex sup data shows only a 0.003% increase.In terms of ONT missed calls, a variant dense repetitive region in the E. coli sample ATCC_25922 was the cause of the simplex sup SNP outlier from Figure 2 (see Suppl.",
    "Bars on each point at each depth depict the 95% confidence interval.",
    "The horizontal red dashed line is the full-depth Illumina value for that metric, with the red bands indicating the 95% confidence interval.biorxiv;2024.03.15.585313v3/FIG7F7fig7Figure 7.Effect of read depth (x-axis) on the highest indel F1 score, and precision and recall at that F1 score (y-axis), for each variant caller (colours).",
    "Our findings show that deep learning approaches, specifically Clair3 and DeepVariant, deliver high accuracy in SNP and indel calls from the latest high-accuracy basecalled ONT data, outperforming Illumina-based methods, with Clair3 achieving median F1 scores of 99.99% for SNPs and 99.53% for indels.Our dataset comprised deep sequencing of 14 bacterial species using the latest ONT R10.4.1 flowcells, with a 5 kHz sampling rate, and complementary deep Illumina sequencing.",
    "Consistent with previous studies [11\u201313], we observed read accuracies greater than 99.0% (Q20) and 99.9% for simplex and duplex reads, respectively (Figure 1).The high-quality sequencing data enabled the creation of near-perfect reference genomes, crucial for evaluating variant calling accuracy.",
    "Briefly, the unfiltered ONT simplex sup reads were filtered with Filtlong (v0.2.1 [45]) to keep the best 90% (-p 90) and fastp (default settings) was used to process the raw Illumina reads.",
    "We only kept genomes with an ANI, a, such that 98.40% \u2264 a <= 99.80%.",
    "In addition, we excluded any genomes with CheckM[52] completeness less than 98% and contamination greater than 5%.",
    "We then selected the genome with the ANI closest to 99.50%.",
    "Our reasoning for this range exclusion is that genomes with a < 99.80% are almost always members of the same sequence type (ST)[53, 54], and we found very little variation between them (data not shown).We then identified variants between the reference and donor genomes using both minimap2 (v2.26 [27]) and mummer (v4.0.0rc1 [28]).",
    "We then passed the output into show-coords -rTH -I 60 to obtain the coordinates for all alignments with an identity of 60% or greater."
  ],
  "methods_sentences": [
    "Variant calling is used extensively in public health laboratories to inform decisions on managing bacterial outbreaks [5] and in molecular diagnostic laboratories as the basis for clinical decisions on how to best treat patients with disease [6].Over the last 15 years, short-read sequencing technologies, such as Illumina, have been the mainstay of variant calling in bacterial genomes, largely due to their relatively high level of base-calling accuracy.",
    "FreeBayes had the largest runtime variation, with a maximum of 597s/Mbp, equating to 2.75 days for the same genome.",
    "Our findings show that deep learning approaches, specifically Clair3 and DeepVariant, deliver high accuracy in SNP and indel calls from the latest high-accuracy basecalled ONT data, outperforming Illumina-based methods, with Clair3 achieving median F1 scores of 99.99% for SNPs and 99.53% for indels.Our dataset comprised deep sequencing of 14 bacterial species using the latest ONT R10.4.1 flowcells, with a 5 kHz sampling rate, and complementary deep Illumina sequencing.",
    "Bacteria were lysed with appropriate enzymatic treatment except for Mycobacterium and Streptococcus, which were lysed by bead beating (PowerBead, 0.5mm glass beads [13116-50] or Lysing Matrix Y [116960050-CF] and Precellys or Tissue lyser [Qiagen])."
  ],
  "table_count": 0
}