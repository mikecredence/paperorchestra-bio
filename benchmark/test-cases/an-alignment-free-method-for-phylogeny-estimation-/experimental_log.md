# Experimental Log: An Alignment-free Method for Phylogeny Estimation using Maximum Likelihood

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 3.Results3.1.Datasets and benchmarkingWe assess the performance of our method using seven real datasets.
- First, we analyze a 7 Primates dataset [8] and a Drosophila dataset from [25].
- The 7 Primates dataset contains full mitochondrial genome sequences of 7 primates, and the Drosophila dataset consists of real genome skims of 14 Drosophila species subsampled to 100 Mb.
- We selected these datasets as the reference trees for these species are well established.Next, we analyzed datasets from the AFproject [9] that have been widely used for benchmarking alignment-free methods.
- They include assembled sequences of 29 E.coli/Shigella strains [10], assembled mitochondrial genomes of 25 fish species of the suborder Labroidei [26], full genome sequences of 14 plant species [27], full genome sequences of 27 E.coli/Shigella strains [28], and full genome sequences of 8 Yersinia st
- For the primates and Drosophila datasets, sequences and the benchmark tree are obtained from [8] and [25], respectively.
- The primary performance metric used throughout this paper is the Robinson Foulds (RF) [29] distance.
- The nRF distance between this tree and the reference tree is compared to those achieved by state-of-the-art methods from the AFproject [9].
- The bench-marked methods include FFP [30, 31], co-phylog [10], mash [12], Skmer [25] FSWM/Read-SpaM [32, 33] andi [11], phylonium [34], Multi-SpaM [13], and CAFE-cvtree [35].
- It has been observed that no single method benchmarked by AFproject [9] achieves the best scores across all datasets.
- Therefore, for the 7 primates and Drosophila datasets, we apply neighbor-joining and UPGMA implementation of MEGA-X [36] on the distance matrix to get the estimated trees, and find the RF distances using PHYLIP [37].
- We limit the scope of our work to phylogenetic trees upto a maximum of 30 species.3.2.Selection of k-mer lengthsWe first explore how the estimated trees vary with different k-mer lengths.
- The variation of nRF and entropy with change in k-mer size for the 7 Primates and Drosophila datasets are illustrated in Figure 3.
- Similar plots for the remaining datasets are shown in Supplementary Figures (S1 Figure - S5 Figure).
- We observe that, for the 7 Primates dataset, the minimum nRF distance of 0 and the maximum entropy is obtained when k equals 9.
- We observe that in Figure 3(a) there is a drop in nRF at k=23.
- In the subsequent sections, we only report nRF distances corresponding to the tree obtained using kentropy.biorxiv;2019.12.13.875526v2/FIG3F4fig3Figure 3:nRF and entropy vs.
- k-mer.Variation of normalized Robinson Foulds distance and entropy with change in k-mer length for (a) the 7-Primates dataset and (b) the Drosophila dataset.
- Diamond shaped markers represent values corresponding to kentropy.3.3.7 Primates and Drosophila DatasetsThe nRF distances for Peafowl and other methods for the 7 Primates and Drosophila datasets are demonstrated in Figure 4.
- 5(a)).biorxiv;2019.12.13.875526v2/FIG4F5fig4Figure 4:Comparison of nRF distances.nRF distance comparison among Peafowl and state-of-the-art methods on the 7 Primates and Drosophila datasets.biorxiv;2019.12.13.875526v2/FIG5F6fig5Figure 5:Analysis of the Primate and Drosophila phylogenies.The internal
- (a) The trees estimated by Peafowl (which is identical to the reference tree [8]), Skmer, and Mash.
- (b) The trees estimated by Peafowl and Skmer in comparison to the reference tree.For the Drosophila dataset, the trees with the lowest nRF distances were obtained by Peafowl, Skmer and phylonium (Figure 4).
- Skmer and Peafowl reconstructed the sister relationship of Drosophila mauritiana and Drosophila simulans which contradicts the reference tree supporting the (Drosophila mauritiana, (Drosophila simulans, Drosophila sechellia)) relationship.3.4.Genome-based phylogenyThe Genome-based Phylogeny group of
- A comparison of the nRF distances achieved by various methods is shown in Figure 6.
- Peafowl attains nRF values of 0.23, 0.05, and 0.36 on these datasets, respectively.biorxiv;2019.12.13.875526v2/FIG6F7fig6Figure 6:Comparison of nRF distances on the AFproject datasets.nRF distance comparison among Peafowl and several different methods on real datasets from AFproject.
- Exact values can be found in supplementary materials.On the 25 Fish dataset, our method is one of the best performing tools, achieving the lowest nRF distance of 0.05 along with mash and FSWM.
- Estimated and reference trees for fish genome are shown in S6 Figure.However, on the 29 E.coli/Shigella and the 14 plant datasets, Peafowl is outperformed by other methods.
- The best performing method on the 29 E.coli/Shigella dataset is phylonium whereas co-phylog, mash and Multi-SpaM generate the most accurate trees on the 14 plant dataset.Estimated and reference trees for the 29 E.coli and 14 plant datasets are available in the supplementary material (S7 Figure, S11 
- It is worth noting that the reference tree for the 29 E.coli dataset was constructed using an alignment-based approach from the assembled genomes [10] and has not been thoroughly validated subsequently.
- For the plant dataset, the kentropy value in Peafowl was calculated based on running the method over a k-mer range of 9 to 17 instead of 9 to 31 to avoid resource exhaustion.
- Results are not included in the entropy variation plot for k equals 9 and 17 due to the presence of all 1’s in the binary matrix, resulting in zero entropy and computational limitation, respectively.3.5.Horizontal gene transfer (HGT)This category of data from the AFproject [9] includes full genome s
- These two datasets are known to have undergone extensive genome rearrangements [9].
- They exhibit horizontal gene transfer properties that may cause distant species to show sibling-like properties (such as similar k-mers).The performance of various alignment-free tools on the Yersinia dataset is shown in Figure 6.
- An observation was made previously [9] that whole-genome analysis tools tend to construct trees relatively discordant to the reference tree on Yersinia sequences than traditional approaches.
- This seems true for Peafowl as well, with an nRF of 1 on this dataset.
- However, most tools perform poorly in this case, with only two having an nRF value below 0.8.
- It has been conjectured that the complex nature of the genus and substantial rearrangement events may promote this discrepancy [9].We further explored this issue and noted that the eight Yersinia genomes are very similar in sequence but share genome rearrangements, and the reference tree was constru
- 7).biorxiv;2019.12.13.875526v2/FIG7F8fig7Figure 7:Analysis of the Yersinia phylogenies.(a) The tree estimated by PEAFOWL with non-canonical counting mode, which is identical to the reference tree.
- The branches in the estimated tree that differ from the reference tree are shown in red.Supplementary S2 Table and S3 Table report the entropy and nRF values (corresponding to the highest entropy) achieved by Peafowl in the canonical and non-canonical settings, respectively.
- We observe that the entropy values in the non-canonical mode are substantially higher than those in the canonical mode for the Yersinia dataset.On the 27 E.coli/Shigella dataset, our method achieves nRF distance of 0.17, but the best performers include co-phylog, andi and phylonium with an nRF of 0.
- Estimated and reference trees for E.coli/Shigella are shown in the supplementary material (S8 Figure).3.6.Runtime and Memory UsageAll the datasets are run in an Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz machine with 8 processors and 32 GB RAM.
- Table 1 summarizes the unzipped size of the datasets used, corresponding runtime, and peak memory usage by Peafowl.
- Values for both Plant and Drosophila data are corresponding to a k-mer range of 9 to 17.biorxiv;2019.12.13.875526v2/TBL1T1tbl1Table 1:Runtime and peak memory usage of Peafowl.

## Tables

### Table 1:
> Runtime and peak memory usage of Peafowl.


## Figure Descriptions

### Figure 1:
Overview of phylogenetic tree estimation using Peafowl.At the beginning, k-mers of various sizes are listed from the input sequences. Then separate binary matrices are produced using these k-mers. From the binary matrices of different k-mer sizes, an appropriate k-mer length (kentropy) is chosen bas

### Figure 2:
Choosing k-mer lengths.Existence of k-mers depends on the length. In this figure, the k-mer AT of length 2 is found in all 3 taxa. However, the k-mer ATAGCGC of length 7 is found only in the source taxon (T1).

### 


### Figure 3:
nRF and entropy vs. k-mer.Variation of normalized Robinson Foulds distance and entropy with change in k-mer length for (a) the 7-Primates dataset and (b) the Drosophila dataset. Diamond shaped markers represent values corresponding to kentropy.

### Figure 4:
Comparison of nRF distances.nRF distance comparison among Peafowl and state-of-the-art methods on the 7 Primates and Drosophila datasets.

### Figure 5:
Analysis of the Primate and Drosophila phylogenies.The internal branches in the estimated trees that are not found in the reference trees are shown in red. (a) The trees estimated by Peafowl (which is identical to the reference tree [8]), Skmer, and Mash. (b) The trees estimated by Peafowl and Skmer

### Figure 6:
Comparison of nRF distances on the AFproject datasets.nRF distance comparison among Peafowl and several different methods on real datasets from AFproject. Exact values can be found in supplementary materials.

### Figure 7:
Analysis of the Yersinia phylogenies.(a) The tree estimated by PEAFOWL with non-canonical counting mode, which is identical to the reference tree. (b) PEAFOWL-estimated tree with canonical mode of counting. The branches in the estimated tree that differ from the reference tree are shown in red.

## References
Total references in published paper: 35

### Key References (from published paper)
- A statistical method for evaluating systematic relationships (, 1958)
- The neighbor-joining method: a new method for reconstructing phylogenetic trees (, 1987)
- Maximum parsimony method for phylogenetic prediction (, 2008)
- The robustness of two phylogenetic methods: four-taxon simulations reveal a slight superiority of ma (, 1995)
- Statistical properties of the maximum likelihood method of phylogenetic estimation and comparison wi (, 1994)
- Alignment-free sequence comparison: benefits, applications, and tools (, 2017)
- Alignment-free phylogenetics and population genetics (, 2013)
- Benchmarking of alignment-free sequence comparison methods (, 2019)
- Co-phylog: an assembly-free phylogenomic approach for closely related organisms (, 2013)
- andi: Fast and accurate estimation of evolutionary distances between closely related genomes (, 2014)
- Mash: fast genome and metagenome distance estimation using minhash (, 2016)
- ‘multi-spam’: a maximum-likelihood approach to phylogeny reconstruction using multiple spaced-word m (, 2020)
- Fast alignment-free sequence comparison using spaced-word frequencies (, 2014)
- Is multiple-sequence alignment required for accurate inference of phylogeny? (, 2007)
- A fast, lock-free approach for efficient parallel counting of occurrences of k-mers (, 2011)
- A survey and evaluations of histogram-based statistics in alignment-free sequence comparison (, 2017)
- The number of k-mer matches between two dna sequences as a function of k and applications to estimat (, 2020)
- Entropy and information approaches to genetic diversity and its expression: genomic geography (, 2010)
- Optimal choice of k-mer in composition vector method for genome sequence comparison (, 2018)
- An information-entropy position-weighted k-mer relative measure for whole genome phylogeny reconstru (, 2021)
- Fast gapped k-mer counting with subdivided multi-way bucketed cuckoo hash tables (, 2022)
- Raxml version 8: a tool for phylogenetic analysis and post-analysis of large phylogenies (, 2014)
- These are not the k-mers you are looking for: efficient online k-mer counting using a probabilistic  (, 2014)
- Skmer: assembly-free and alignment-free sample identification using genome skims (, 2019)
- Complete mitochondrial dna sequences of the threadfin cichlid (petrochromis trewavasae) and the blun (, 2013)
- A phylogenetic analysis of the brassicales clade based on an alignment-free sequence comparison meth (, 2012)
- Alignment-free microbial phylogenomics under scenarios of sequence divergence (, 2016)
- Comparison of phylogenetic trees (, 1981)
- Alignment-free genome comparison with feature frequency profiles (ffp) and optimal resolutions (, 2009)
- A genome tree of life for the fungi kingdom (, 2017)

## Ground Truth Reference
- Figures: 8
- Tables: 1
- References: 35