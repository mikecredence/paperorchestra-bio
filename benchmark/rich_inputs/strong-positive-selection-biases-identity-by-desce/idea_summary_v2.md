## Working title
Strong Positive Selection Biases IBD-Based Inferences of Demography and Population Structure in Plasmodium falciparum

## Core question
How does strong positive selection from antimalarial drug resistance bias identity-by-descent (IBD)-based estimates of effective population size and population structure in P. falciparum, and can removing IBD peak regions correct this bias?

## Motivation / gap
- IBD is widely used for malaria genomic surveillance to estimate Ne and population structure, but selection bias is largely ignored
- P. falciparum has undergone multiple strong selective sweeps from antimalarial drug resistance
- Selection increases local IBD sharing and generates longer haplotype blocks, violating assumptions of IBD-based demographic estimators
- The interplay between high background relatedness (from declining Ne), positive selection, and low SNP density (high recombination) makes it difficult to disentangle selection effects
- No systematic evaluation of how selection affects IBD distributions in Pf populations had been conducted
- No correction strategy for selection bias in IBD-based analyses had been proposed

## Core contribution (bullet form)
- Analyzed WGS data from 2,055 P. falciparum isolates from eastern SEA (including 640 new genomes) plus West African validation dataset
- Demonstrated via simulation and empirical data that positive selection distorts IBD segment length distributions, shifting them toward longer segments
- Showed that selection-biased IBD leads to underestimated effective population size and blurred population structure
- Developed an IBD peak removal strategy that partially restores accuracy, with effectiveness dependent on background relatedness level
- Found that correction is most beneficial in high-transmission settings (West Africa) with low background relatedness, but less necessary in low-transmission/high-relatedness settings (SEA)
- 80% of SEA isolates were monoclonal (Fws > 0.95); 50.7% of WAF isolates were monoclonal

## Method in brief
WGS data from 2,055 eastern SEA P. falciparum isolates (751 sequenced in-house including 640 new, 1,304 from MalariaGEN Pf6) spanning 14 years and 18 provinces across Cambodia, Thailand, Laos, and Vietnam were analyzed. Population genetic simulations using simplified models with strong positive selection, decreasing Ne, and high recombination were designed as single-population (Ne estimation) and multi-population (structure inference) models. A five-deme stepping-stone model was used to test selection effects on IBD-based population structure inference.

IBD was inferred using both true IBD from simulations and empirical haplotype-based methods. An IBD peak removal strategy identified genomic regions with excess IBD sharing (corresponding to known drug resistance loci) and excluded those segments before downstream analyses. IBD-based Ne was estimated using IBDNe. Population structure was assessed via IBD network community detection. Validation was performed on a West African dataset from MalariaGEN Pf6.

## Target venue
Nature Communications
