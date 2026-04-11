# Experimental Log: Strong Positive Selection Biases Identity-By-Descent-Based Inferences of Recent Demography and Population Structure in Plasmodium falciparum

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsParasite isolates and WGS data summaryTo investigate the impact of positive selection on the inference of Ne and population structure, we mainly focused on eastern SEA, as it has been a hotspot for drug resistance emergence 3,47.
- We analyzed WGS data from 2,055 Pf isolates that passed quality control and data processing filters (see Online Methods), including 751 (640 new) isolates from Cambodia and Thailand that were sequenced in-house and 1,304 eastern SEA isolates from the publicly available MalariaGEN Catalogue of Geneti
- The included isolates are distributed across 14 years and 18 provinces in four countries (Cambodia, Thailand, Laos, and Vietnam) (Fig.
- Among these isolates, 79.3%, 68.0%, and 46.1% isolates had at least 5x, 10x, and 25x coverage in >80% of the Pf genome, respectively (Fig.
- The Fws statistic was estimated for each isolate to identify monoclonal versus polyclonal isolates, with 80% being classified as monoclonal isolates (Fws > 0.95) (Fig.
- Among the polyclonal isolates, 44.3% harbored a predominant clone (defined in Online Methods), and the predominant haploid genome (Fig.
- 1d, with ratio<1.0) was included in the analyzable dataset.
- Isolates from West Africa (WAF) were also obtained from the MalariaGEN Pf6 database for validation of results in a high transmission setting (Fig.
- Among WAF isolates that passed quality control, 50.7% were monoclonal, consistent with the higher multiplicity of infection (MOI) expected in a high malaria transmission setting 28.biorxiv;2023.07.14.549114v1/FIG1F1fig1Figure 1.Summary of Pf parasite isolates and WGS data for Pf from SEA.a, Distribu
- b, Distribution of genome fractions covered by at least 5, 10, and 25 sequence reads of all parasite genomes from SEA.
- d, Distribution of ratios of predominant genomes in sequenced isolates that passed quality control (determined by dEploid 49,50).Effects of positive selection on IBD distribution and IBD-based Ne inferenceEmpirical datasets sampled from a real Pf population often deviate from an ideal population due
- We designed two categories of models: (1) a single-population model to test the effects of selection on the IBD distribution and the estimation of effective population size, and (2) a multi-population model to test the effects of positive selection on IBD-based population structure inference.To prev
- The algorithm directly utilizes ancestral information from simulated (true) genealogical trees in tree sequence format 52,53 and avoids phased genotype-based IBD inference (Fig.
- We verified the quality of true IBD by comparing IBD-based Ne estimates (via IBDNe 12) with the true population size in neutral simulations under different demographic scenarios (Fig.
- S2b).Different aspects of the IBD distribution represent distinct types of information about evolutionary histories, such as the time to most recent common ancestor (TMRCA, inferred based on IBD segment length) 22,24, genetic relatedness or population structure (inferred based on pairwise genome-wid
- S3a) and other selection scenarios for Pf (Fig.
- S3b-d) consistent with realistic evolutionary parameters for Pf (see Online Methods).
- 2a) and isolate-pairs sharing larger genome-wide total IBD (Fig.
- 2b) and enriching IBD around selected sites (Fig.
- More importantly, we found that Ne (via IBDNe 12) is underestimated in recent generations in cases with selection compared to neutral cases (Fig.
- 2d), likely due to the increase in longer IBD segments (thus smaller Ne in more recent times).biorxiv;2023.07.14.549114v1/FIG2F2fig2Figure 2.Effects of positive selection on IBD distribution and Ne inference.a-c, Positive selection affects various aspects of the IBD distribution, including IBD segme
- Note that x-axis in a uses a custom scale for IBD length l (bottom) so that the estimated TMRCA (50/l, top) is in a linear scale.
- Shorter IBD segments (0.2-2 cM) were included to cover the more distant past (>25 generations ago).
- The representative results were generated using a selection coefficient, s, of 0.3, a selection starting time 80 generations ago, and a single origin of the favored allele introduced at the position of 33.3 cM of each chromosome.
- The difference between selection (s = 0.3) and neutral scenarios can be partially mitigated by removing IBD segments located within IBD peak regions.
- S3.We evaluated IBD peak region identification and removal strategies to test whether positive selection-induced bias can be corrected (Fig.
- Simply put, peaks were identified on each chromosome using a threshold method, then validated through IBD-based selection statistics XiR,s 9.
- 2d).We further evaluated the impact of varying selection parameters, including selection coefficients, selection starting times (Fig.
- S3e-g), and the number of origins of the favored alleles (Fig.
- S3h-j), on IBD distribution and Ne estimates.
- S3d), intermediate selection duration time (Fig.
- S3f), and a small number of origins (such as a hard sweep) (Fig.
- S3i) allow the establishment of the selective sweeps (the favored allele is not lost during the sweep) (Fig.
- S3 first column) and thus result in selection bias.
- Signed rank tests based on replicated simulations suggested the effects of positive selection on Ne estimates are statistically significant (Bonferroni-adjusted p values< 0.05) (Fig.
- S5).Effects of positive selection on population structure inferenceGiven the pronounced effects of positive selection on IBD distribution and Ne inference, it is vital to understand its impact on the inference of population structure.
- 3a) that simulates a pattern of allele frequency gradients across subpopulations (Fig.
- 3b), mimicking selective sweep in a structured parasite population 55.biorxiv;2023.07.14.549114v1/FIG3F3fig3Figure 3.Effects of positive selection on the IBD-based population structure inference.a, Schematic of the one-dimensional stepping-stone model.
- b, Average frequency trajectory of favored alleles (on each chromosome) in different subpopulations (p1 -p5).
- c, Heatmap of pairwise genome-wide total IBD under neutral, selection (s = 0.3), and selection with peaks removed.
- S6.Under the neutral scenario with a moderate migration rate (such as 0.01, corresponding to 1% of individuals in a subpopulation being migrants from adjacent subpopulations in each generation), within-population IBD sharing dominates the pairwise sharing heatmap (Fig.
- 3c [left panel], and d [black line]), the total population is highly modular 56,57 with respect to the true subpopulation labels (Fig.
- 3e [left bar]), and community-detection using the InfoMap clustering algorithm 57,58 captures the true population structure with high consistency (Fig.
- 3f [left panel]).However, with strong selection, both within- and between-population IBD sharing increases (Fig.
- 3 d [blue line]), reduced network modularity, and collapsed community groups (Fig.
- 3e [middle bar] and f [middle panel], making it difficult to distinguish one population from adjacent populations.
- S6) and repeated simulations (Table S1), suggesting the blurring effect is selection strength-dependent.The effect of selection on structure inference can be partially mitigated by removing IBD segments located within the genomic regions with IBD peaks (Fig.
- 3c [right panel], d [dashed red line], and e [right bar]), and the collapsed communities become distinguishable and consistent with the true population labels (Fig.
- 3f [right panel]).Genome-wide IBD sharing and selection signals in SEA Pf isolatesTo evaluate the effects of positive selection on IBD-based inferences in empirical Pf datasets, we first identified genomic regions that are under positive selection using similar methods as for simulated data, and the
- S4 and Online Methods) and correlated them with known drug-resistance genes.
- For empirical data (without genealogical trees from simulations), we chose to use the haploid-genome-oriented HMM-based IBD caller (hmmIBD) for IBD inference 59.
- The IBD coverage profiles called by hmmIBD show peaks surrounding: (1) known drug resistance genes and genes associated with the genetic architecture of resistant parasites, such as pfmdr1 60, pfaat1 41,61, pfcrt 62,63, dhps 64, pph (PF3D7_1012700) 65, gch1 66, kelch13 67–69, and arps10 65; (2) gene
- 4a).biorxiv;2023.07.14.549114v1/FIG4F4fig4Figure 4.IBD coverage profile of all and unrelated Pf isolates in SEA.a.
- 4a) compared to other geographic regions, such as WAF (Fig.
- S7), which is consistent with declines in malaria transmission owing to intensive elimination efforts in SEA 9.
- The low baseline IBD sharing is less noisy and more readily allows the identification of IBD peaks, including those surrounding pfcrt and arps10.
- 4a), we focused on the unrelated isolates (n = 701).
- The Ne estimates based on IBD before removing the peaks via IBDNe suggest a decreasing pattern of Ne in SEA, from around 104 to around 103 in the most recent 60–80 generations (Fig.
- 5a, blue), consistent with a rapid decrease in malaria incidence in the last decades owing to malaria elimination efforts in this geographic region 1.biorxiv;2023.07.14.549114v1/FIG5F5fig5Figure 5.Ne and population structure inference in an empirical dataset from SEA.a, Ne estimates for SEA before a
- Only the largest 5 communities are plotted.
- Among the 701 unrelated isolates from SEA, we identified five communities (defined via IBD network structure analysis instead of geopolitical boundaries) with sizes >20 isolates.
- The community of the largest size, labeled as C0 (Fig.
- 5b) was enriched for parasites sampled from Western Cambodia (Battambang, Kratie, Oddar Meanchey, and Pursat) (Fig.
- In contrast, the second-largest community (C1) was comprised of isolates from a wider geographic area, including Northeastern Cambodia (Ratanakiri), Laos, and Vietnam (Fig.
- Isolates within C1 were distantly related given the low-average within-community IBD sharing (Fig.
- 5b, top left bock) compared with other communities.
- Hierarchical clustering of the community-level average IBD sharing matrix revealed other major communities such as C2/3/4 are closer to C0 rather than C1.
- For instance, in recent years, parasites from Pursat converged into a main community including parasites from other communities; a similar pattern occurred in Oddar Meanchey 2–3–years later relative to Pursat (Fig.
- The group clustered with C0 – C0/2/3/4 – demonstrates relatively high frequencies of several resistance alleles, including those associated with artemisinin-resistance or its associated genetic background, e.g., PF3D7_0720700 C1484F, Apicoplast ribosomal protein S10 (ARPS10) V127M, PfCRT I356T, Ferr
- In contrast, the C1 communities had relatively low frequency or no mutations (including Kelch13 mutations) at these loci.
- The mutation landscapes for the largest 5 communities show distinct Kelch13 resistance mutation patterns, consistent with the presence of multiple artemisinin-resistant founder populations and an artemisinin susceptible population previously observed in this geographic region 8.
- These results suggest that the population structure of Pf in SEA is heavily influenced by drug resistance and positive selection and confirms that different founder populations harbor distinct combinations of resistant mutations 8.Finally, we compared these IBD-based inferences before and after peak
- 5a, blue) and post-segment removal (Fig.
- 5a, red) located within each other’s 95% confidence intervals.
- Although there are some minor changes in population structure inference, the size of main communities and the community comparison metrics adjusted rand index 72 are largely unchanged (Table S2).
- The hierarchical clustering of communities shows similar grouping patterns, such as the presence of C0/2/3/4 and C1 groups (data not shown).Effects of removing IBD peaks on IBD-based inferences in a high transmission setting with low background parasite genetic relatednessThe effects of positive sel
- S10), despite having pruned highly-related isolates (the equivalent of first-degree relatives) (Fig.
- To test this hypothesis, we took two approaches: (1) we incorporated high relatedness into simulations; and (2) we evaluated an empirical dataset from a high transmission setting, WAF, where parasite relatedness is known to be lower than in SEA 9.First, to incorporate high relatedness in our simulat
- S11a) than in high-relatedness simulations (Fig.
- S11c-d), but fails to do so in simulations under a scenario of high relatedness (Fig.
- Using the same criterion for unrelated isolates as in the SEA dataset, we found that removing IBD peaks in the WAF dataset, resulted in larger estimates of Ne for the most recent generations with non-overlapping confidence intervals around 20 generations ago (Fig.
- The difference in population structure inference before and after IBD peak removal is statistically significant based on Jackknife resampling (Table S2).biorxiv;2023.07.14.549114v1/FIG6F6fig6Figure 6.Removing IBD peaks changes the inference of Ne and population structure in the West African dataset.
- Only communities with at least 20 isolates are shown.

## Figure Descriptions

### Figure 1.
Summary of Pf parasite isolates and WGS data for Pf from SEA.a, Distribution of sampling location and collection year for the 2,055 analyzable samples. b, Distribution of genome fractions covered by at least 5, 10, and 25 sequence reads of all parasite genomes from SEA. c, Distribution of Fws in seq

### Figure 2.
Effects of positive selection on IBD distribution and Ne inference.a-c, Positive selection affects various aspects of the IBD distribution, including IBD segment length (a), total IBD shared by a pair of isolates (b), and IBD location along the chromosome (c). Note that x-axis in a uses a custom sca

### Figure 3.
Effects of positive selection on the IBD-based population structure inference.a, Schematic of the one-dimensional stepping-stone model. Five subpopulations were split from an ancestral population. There is symmetrical migration between adjacent subpopulations. A favored allele was introduced into th

### Figure 4.
IBD coverage profile of all and unrelated Pf isolates in SEA.a. IBD coverage of all parasite genomes in SEA. Labels on the top indicate the center of known or putative drug resistance genes or genes that are under selection for sexual commitment (*). b. IBD coverage of unrelated genomes in SEA. Anno

### Figure 5.
Ne and population structure inference in an empirical dataset from SEA.a, Ne estimates for SEA before and after removing IBD peaks. b, IBD network analysis of SEA data (before removing IBD peaks), including community-level IBD sharing matrix (heatmap), community size (blue circles below), and dendro

### Figure 6.
Removing IBD peaks changes the inference of Ne and population structure in the West African dataset.a, Ne estimates of Pf population in a WAF dataset before (blue) and after (red, dotted) removing peaks. b-c, IBD network community detection using WAF dataset before (b) and after (c) removing IBD pea

## References
Total references in published paper: 94

### Key References (from published paper)
- Spread of Artemisinin Resistance in Plasmodium falciparum Malaria (, 2014)
- Evolution and expansion of multidrug-resistant malaria in southeast Asia: A genomic epidemiology stu (, 2019)
- The origins of antimalarial-drug resistance (, 2014)
- The spread of artemisinin-resistant Plasmodium falciparum in the Greater Mekong subregion: A molecul (, 2017)
- Genomic structure and diversity of Plasmodium falciparum in Southeast Asia reveal recent parasite mi (, 2019)
- Plasmodium falciparum parasite population structure and gene flow associated to anti-malarial drugs  (, 2016)
- Multiple populations of artemisinin-resistant Plasmodium falciparum in Cambodia (, 2013)
- Identity-by-descent analyses for measuring population dynamics and selection in recombining pathogen (, 2018)
- Length Distributions of Identity by Descent Reveal Fine-Scale Demographic History (, 2012)
- Accurate Non-parametric Estimation of Recent Effective Population Size from Segments of Identity by  (, 2015)
- Haplotype-based inference of recent effective population size in modern and ancient DNA samples. Rom (, 2022)
- Clustering of 770,000 genomes reveals post-colonial population structure of North America (, 2017)
- Quantifying connectivity between local Plasmodium falciparum malaria parasite populations using iden (, 2017)
- Identity-by-descent detection across 487,409 British samples reveals fine scale population structure (, 2020)
- Toward a fine-scale population health monitoring system (, 2021)
- Identity by Descent Between Distant Relatives: Detection and Applications (, 2012)
- The Geography of Recent Genetic Ancestry across Europe (, 2013)
- A Fast and Simple Method for Detecting Identity-by-Descent Segments in Large-Scale Data (, 2020)
- Falciparum malaria from coastal Tanzania and Zanzibar remains highly connected despite effective con (, 2020)
- Estimating recent migration and population-size surfaces (, 2019)
- A Fast, Powerful Method for Detecting Identity by Descent (, 2011)
- The Great Migration and African-American Genomic Diversity (, 2016)
- Estimating relatedness between malaria parasites (, 2019)
- Identity-by-descent with uncertainty characterises connectivity of Plasmodium falciparum populations (, 2020)
- Population Parameters Underlying an Ongoing Soft Sweep in Southeast Asian Malaria Parasites (, 2017)
- Measurably recombining malaria parasites (, 2022)
- Genetic diversity and chloroquine selective sweeps in Plasmodium falciparum (, 2002)
- Antimalarial drug resistance (, 2004)
- Anti-malarial drugs and the prevention of malaria in the population of malaria endemic areas (, 2010)
- Accelerated evolution and spread of multidrug-resistant Plasmodium falciparum takes down the latest  (, 2019)

## Ground Truth Reference
- Figures: 6
- Tables: 0
- References: 94