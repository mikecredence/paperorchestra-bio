# Experimental Log: A regression based approach to phylogenetic reconstruction from multi-sample bulk DNA sequencing of tumors

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 5Results5.1Runtime comparison to linear programming solversWe compared an implementation of our structured regression algorithm for the 𝓁1-VAFRP to a linear programming (LP) approach on simulated data.
- In particular, we implemented the natural primal LP formulation solving the 𝓁1-VAFRP (Section 3.2) using two commercial LP solvers: Gurobi v9.0.3 [43] and CPLEX v22.1.0 [44].
- We generated 264 pairs of frequency matrices F and clonal matrices B as described in Supplementary Section C.1, and measured the wall-clock runtime of our algorithm and the LP solvers on these simulated instances.
- Excluding the time required to construct the LP – which would unfairly penalize the LP solvers – we found that our algorithm was a mean of 95.6 times faster than Gurobi and 105.1 times faster than CPLEX (Supplementary Figures 1, 2).Next, we tested the warm start capability of our structured regressi
- For each of the 264 instances constructed above, we measured the time to solve the 𝓁1-VAFRP for 25,000 trees obtained by applying a single random SPR operation to the input clonal tree.
- We performed this measurement both in the setting where we employ our regression algorithm as a black-box (the cold start setting) and the setting where we used the recomputation procedure outlined in Corollary 1 (the warm start setting).
- We found that our algorithm was a mean of 6.2 times faster in the warm start as opposed to cold start settings (Supplementary Figures 3, 4).
- This implies that our regression algorithm possesses another advantage over naïve LP approaches, which do not provide any warm starting capabilities.5.2Evaluation of fastBE on simulated dataWe evaluated our factorization algorithm, fastBE, on simulated data, and compared it to four other state-of-th
- To construct each simulated instance, we generated a clone tree 𝒯 and usage matrix U, computed the frequency matrix F = UB, and sampled both variant and non-variant reads from F at 40× coverage.
- Complete details describing the simulations, parameters, and evaluation metrics are provided in Supplementary Sections C.1, C.2, C.3.On simulated instances with few clones (n = 3, 5, 10) and samples (m = 5, 10, 25), all algorithms terminated in under 24 hours on the majority of the 108 simulated ins
- fastBE, Pairtree, and Orchard accurately recovered pairwise relationships in this setting (Figure 3; Supplementary Figure 5), with fastBE, Pairtree, and Orchard performing nearly identically for the n = 10 clone setting in terms of mean F1-score (fastBE: 0.965, Pairtree: 0.972, Orchard: 0.965).
- In contrast, CITUP and CALDER struggled to accurately reconstruct pairwise relationships (Figure 3; Supplementary Figure 5) when there were 5 or more clones.
- In terms of recovering the ground truth usage matrix U and frequency matrix F, fastBE significantly outperformed CITUP and CALDER, while performing similarly to Pairtree and Orchard (Supplementary Figure 6).biorxiv;2024.04.23.590844v1/FIG3F3fig3Figure 3:The accuracy of reconstructing pairwise relati
- (Left) The F1-score versus the number of clones.
- (Right) The wall-clock runtime on instances with ≥100 clones versus the number of samples.
- Methods that did not scale to instances with many clones are excluded from the plot.On simulated instances with a modest number of clones (n = 20, 30, 50) and samples (m = 25, 50), CITUP and CALDER were unable to terminate on the majority of the simulated instances within 24 hours – consistent with 
- On instances with n = 20, 30 clones, fastBE, Pairtree, and Orchard performed similarly in terms of reconstructing pairwise relationships (Figure 3; Supplementary Figure 7).
- However, on instances with n = 50 clones, fastBE and Orchard outperformed Pairtree (mean F1 fastBE: 0.825, Pairtree: 0.749, Orchard: 0.805) in reconstructing pairwise relationships (Supplementary Figure 13).
- In terms of recovering the ground truth usage matrix U and frequency matrix F, all methods performed quite well in recovering F, but Pairtree was less accurate in recovering U and F when the number of clones was large (Supplementary Figure 8).
- Finally, fastBE was an order of magnitude faster than Pairtree and Orchard, running for an average of 1.21 seconds on instances with n = 50 clones (Supplementary Figure 13).In the regime with a large number of clones (n = 100, 250, 500, 1000) and samples (m = 50, 100), only fastBE and Orchard were a
- On these instances, fastBE and Orchard perform nearly identically in terms of recovering ground truth pairwise relationships (mean F1 fastBE: 0.773, Orchard: 0.783).
- The methods also had similar performance in recovering the ground truth usage matrix U and frequency matrix F (Supplementary Figure 8).
- In terms of runtime, however, fastBE was several orders of magnitude faster than Orchard (Figure 3; Supplementary Figure 13).
- For example, fastBE took a mean of 1229.8 seconds to run on instances with n = 1000 clones and terminated on all such instances, whereas Orchard took a mean of 71749.1 seconds and terminated on 19/24 such instances when allotted 48 hours and a dedicated 32-core processor.We also found that fastBE wa
- In particular, the pairwise reconstruction accuracy strictly improved for fastBE, Pairtree, and Orchard as the number of samples increased (Figure 3; Supplementary Figure 12), while this was not necessarily the case for CALDER and CITUP (Supplementary Figures 9, 10).
- However, the reconstruction accuracy improved for fastBE more quickly than Pairtree and Orchard (Figure 3; Supplementary Figure 12) as the number of samples increased, and fastBE obtained near perfect recovery (median F1: 0.987) with the number of samples m ≥ 50 and the number of clones n < 100.
- Interestingly, we observed a sharp transition in pairwise reconstruction accuracy for fastBE as the ratio of samples to clones approached one (Supplementary Figure 11).5.3Analysis of B progenitor acute lymphoblastic leukemia patient samplesWe applied fastBE to infer phylogenetic trees from multi-sam
- This dataset was sequenced at greater than 200× coverage using targeted sequencing, containing a median of 42 (min: 13, max 90) samples per patient.
- Originally, mutation clusters and phylogenetic trees were inferred from this dataset using Pairtree [11].
- To perform a fair comparison of fastBE against Pairtree, we applied fastBE to the (median: 8, min: 3, max: 17) mutation clusters inferred by Pairtree for each patient, obtaining phylogenetic trees on the exact same mutation clusters.
- We found that on all of the 14 of the patients, both fastBE and Pairtree inferred distinct trees, having a median of at least 8 distinct edges (Supplementary Figures 14).
- For both methods, the normalized frequency matrix estimation error was less than 1% in all but one case (Supplementary Figures 15), though the trees inferred by fastBE had modestly lower frequency matrix estimation error.We quantified the differences between the phylogenetic trees inferred by fastBE
- Importantly, all of the methods benchmarked [7, 10–12] make the perfect phylogeny assumption, and thus if the frequency matrix is correctly measured, the inferred trees should satisfy the sum condition.
- For a sample i and mutation j, we define the violation Vi,j = max {∑k ∈C(j) Fi,k − Fi j, 0} of the sum condition.
- We found that the phylogenies inferred by fastBE had a lower total violation V (mean V of 1.44 over 14 patients) compared to Pairtree (mean of V of 2.40) (Figure 4a) across all 14 patients.biorxiv;2024.04.23.590844v1/FIG4F4fig4Figure 4:a) The total violation  of the sum condition for the phylogenies
- b) The per-sample violation  of the sum condition for the phylogenies inferred by fastBE and Pairtree from the multi-sample bulk DNA sequencing data of the POP66 colorectal cancer model [45].
- The phylogenies inferred by c) fastBE and d) Pairtree for the CSC28 colorectal cancer model.
- Entries marked as ‘−’ correspond to usage values of 0.0.5.4Analysis of patient-derived colorectal cancer modelsFinally, we compared fastBE and Pairtree on two patient-derived xenograft models of colorectal cancer, POP66 and CSC28 from [45], from which multiple bulk samples underwent whole-exome sequ
- The POP66 model contained eight samples collected in the parent tumor (P0), first generation xenograft (G0), and regrowth xenografts, and 25 clones were inferred across these samples in [45].
- The CSC28 model consisted of four samples collected in the first generation (G0) and regrowth xenografts, and contained 11 clones were inferred in these samples in [45].
- When applying fastBE to the CSC28 and POP66 models, we fixed the root clone to contain all mutations with VAF near 0.5 across all samples.We found that the phylogenetic trees inferred by fastBE were quite different from those inferred by Pairtree in terms of both their implied pairwise relationships
- For example, while both CSC28 phylogenies had the same clone 1 as a child of the normal clone, the mutation ORG13G was a child of the normal clone in the Pairtree phylogeny, implying a polyclonal tumor origin.
- Further, while clone 4 is a child of clone 7 in the fastBE phylogeny, clone 4 is on a separate branch from clone 7 in the Pairtree phylogeny.
- A similar story appears for the POP66 phylogenies, where the differences are even further exaggerated due to the large number of clones.Next, we quantified violations of the sum condition in the phylogenetic trees inferred by fastBE and Pairtree.
- We found that fastBE had substantially lower total violation than Pairtree on both the CSC28 (fastBE: 0.273, Pairtree: 0.473) and POP66 (fastBE: 3.280, Pairtree: 4.770) phylogenies.
- This trend held separately across all samples (Figure 4b), and was most pronounced for the “CPT-11 Resistant” samples [45] in POP66.Finally, we compared the inferred clonal proportions in each sample, a measure of the heterogeneity within the tumor samples.
- We define the heterogeneity  of a sample i as the Shannon diversity index, a commonly used measure of species diversity in the ecology literature [46].
- (Note that 0 log 0 = 0.) For CSC28, we found similar sample heterogeneity estimates for both fastBE and Pairtree.
- For POP66, we found similar heterogeneity estimates for most samples, but fastBE found an increased amount of heterogeneity in the parent tumor and “CPT-11 Resistant” samples (Supplementary Figure 16).

## Tables

### Table 1:
> Summary of several variants of the variant allele frequency factorization problem studied in the literature. The loss functions L(F, U, B) and additional constraints beyond U ≥ 0, U 𝟙 ≤ 1 are noted fo


## Figure Descriptions

### Figure 1:
Analogous structured regression problems for a fixed tree topology T in the: (top) ℓ1-VAFFP framework for cancer evolution and the (bottom) minimum evolution framework for distance based phylogenetics. The usage matrix U describes the fraction of each clone across all samples, and the clonal matrix 

### Figure 2:
(Left) The primal LP and (right) the dual LP for the ℓ1-VAFRP

### Figure 3:
The accuracy of reconstructing pairwise relationships for the phylogenetic trees inferred by fastBE, Pairtree [11], Orchard [12], CALDER [10], and CITUP [7] on simulated data. (Left) The F1-score versus the number of clones. (Right) The wall-clock runtime on instances with ≥100 clones versus the num

### Figure 4:
a) The total violation  of the sum condition for the phylogenies inferred by fastBE and Pairtree [11] on data from fourteen patients with B progenitor acute lymphoblastic leukemia. b) The per-sample violation  of the sum condition for the phylogenies inferred by fastBE and Pairtree from the multi-sa

### Supplementary Figure 1:
Relative wall-clock runtime comparison of our algorithm to that of two commercial linear programming solvers, Gurobi and CPLEX. Only the time required to solve the model is reported.

### Supplementary Figure 2:
Absolute wall-clock runtime comparison of our algorithm to that of two commercial linear programming solvers, Gurobi and CPLEX for a varying numbers of clones n = 250, 500, 750, 1000 and samples m = 50, 100, 200, 500. Only the time required to solve the model is reported.

### Supplementary Figure 3:
Relative wall-clock runtime comparison of warm versus cold starting our regression algorithm across 264 instances with varying numbers of clones n = 250, 500, 750, 100 and samples m = 50, 100, 200, 500.

### Supplementary Figure 4:
Absolute wall-clock runtime comparison of warm and cold starting our regression algorithm across 264 instances with varying numbers of clones n = 250, 500, 750, 100 and samples m = 50, 100, 200, 500.

### Supplementary Figure 5:
The (left) false positive rate and (right) false negative rate of reconstructing pairwise relationships for fastBE, Pairtree [11], Orchard [12], CALDER [10], and CITUP [7] on simulated data for small instances with ≤ 10 clones and ≤ 25 samples.

### Supplementary Figure 6:
The normalized 𝓁1 matrix error (left) ∥U − Û ∥1 and (right)  for fastBE, Pairtree [11], Orchard [12], CALDER [10], and CITUP [7] on simulated data for small instances with ≤ 10 clones and ≤ 25 samples.

### Supplementary Figure 7:
The (left) false positive rate and (right) false negative rate of reconstructing pairwise relationships for fastBE, Pairtree [11], and Orchard [12] on simulated data with ≥20 clones. Pairtree did not scale to the ≥100 clone setting and was excluded.

### Supplementary Figure 8:
The normalized 𝓁1 matrix error (left) ∥U − Û ∥1 and (right)  for fastBE, Pairtree [11], and Orchard [12] on simulated data with ≥ 20 clones. Pairtree did not scale to the ≥ 100 clone setting and was excluded.

### Supplementary Figure 9:
The (left) false positive rate and (right) false negative rate of reconstructing pairwise relationships for fastBE, Pairtree [11], Orchard [12], CALDER [10], and CITUP [7] on simulated data with ≤10 clones and ≤25 samples versus the ratio of samples to clones.

### Supplementary Figure 10:
The (left) false positive rate and (right) false negative rate of reconstructing pairwise relationships for fastBE, Pairtree [11], Orchard [12], CALDER [10], and CITUP [7] for simulated data with ≤10 clones versus the number of samples.

### Supplementary Figure 11:
The (left) false positive rate and (right) false negative rate of reconstructing pairwise relationships for fastBE, Pairtree [11], and Orchard [12] on simulated data with ≥20 and ≤100 clones versus the ratio of samples to clones. When the ratio of samples to clones exceeded 2, all methods correctly 

### Supplementary Figure 12:
The (left) false positive rate and (right) false negative rate of reconstructing pairwise relationships for fastBE, Pairtree [11], and Orchard [12] on simulated data with ≥ 20 and ≤ 100 clones versus the number of samples.

### Supplementary Figure 13:
Absolute wall-clock runtime comparison of fastBE, Pairtree [11], and Orchard [12] with varying numbers of clones and samples. Pairtree did not scale to the ≥ 100 clone setting and was excluded.

### Supplementary Figure 14:
The size of the symmetric difference in the edge sets for the phylogenies inferred by fastBE and Pairtree [11] on data from fourteen patients with B progenitor acute lymphoblastic leukemia.

### Supplementary Figure 15:
The normalized 𝓁1 matrix error for the phylogenies inferred by fastBE and Pairtree [11] on data from fourteen patients with B progenitor acute lymphoblastic leukemia.

### Supplementary Figure 16:
The Shannon diversity index estimates for phylogenies inferred by fastBE and Pairtree [11] on multi-sample bulk DNA sequencing performed on patient-derived colorectal cancer models (top) POP66 and (bottom) CSC28.

### Supplementary Figure 17:
fastBE inferred phylogeny for the multi-sample bulk DNA sequencing performed on the CSC28 colorectal cancer model. Each vertex corresponds to a distinct clone and is labeled by the set of mutations which occur on the edge directed into the clone.

### Supplementary Figure 18:
Pairtree inferred phylogeny for the multi-sample bulk DNA sequencing performed on the CSC28 colorectal cancer model. Each vertex corresponds to a distinct clone and is labeled by the set of mutations which occur on the edge directed into the clone.

## References
Total references in published paper: 44

### Key References (from published paper)
- The evolutionary history of lethal metastatic prostate cancer (, 2015)
- Tracking the Evolution of Non–Small-Cell Lung Cancer (, 2017)
- TrAp: a tree approach for fingerprinting subclonal tumor composition (, 2013)
- Reconstruction of clonal trees and tumor composition from multi-sample sequencing data (, 2015)
- Fast and scalable inference of multi-sample cancer lineages (, 2015)
- Clonality inference in multiple tumor samples using phylogeny (, 2015)
- PhyloWGS: Reconstructing subclonal composition and evolution from whole-genome sequencing of tumors (, 2015)
- Tumor phylogeny inference using tree-constrained importance sampling (, 2017)
- CALDER: Inferring Phylogenetic Trees from Longitudinal Tumor Samples (, 2019)
- Reconstructing Complex Cancer Evolutionary Histories from Multiple Bulk DNA Samples Using Pairtree (, 2022)
- Orchard: building large cancer phylogenies using stochastic combinatorial search (, 2023)
- A practical guide to cancer subclonal reconstruction from DNA sequencing (, 2021)
- Computational analysis of cancer genome sequencing data (, 2022)
- Intratumor heterogeneity: the rosetta stone of therapy resistance (, 2020)
- Relapse-Fated Latent Diagnosis Subclones in Acute B Lineage Leukemia Are Drug Tolerant and Possess D (, 2020)
- Inferring the mutational history of a tumor using multi-state perfect phylogeny mixtures (, 2016)
- A simple method for estimating and testing minimum-evolution trees (, 1992)
- Theoretical foundation of the minimum-evolution method of phylogenetic inference (, 1993)
- Computational complexity of inferring phylogenies from dissimilarity matrices (, 1987)
- The minimum evolution problem is hard: a link between tree inference and graph clustering problems (, 2016)
- Subtree transfer operations and their induced metrics on evolutionary trees (, 2001)
- Inferring clonal evolution of tumors from single nucleotide somatic mutations (, 2014)
- PyClone: statistical inference of clonal population structure in cancer (, 2014)
- PyClone-VI: scalable inference of clonal population structures using whole genome data (, 2020)
- SciClone: inferring clonal architecture and tracking the spatial and temporal patterns of tumor evol (, 2014)
- Efficient algorithms for inferring evolutionary trees (, 1991)
- Implications of non-uniqueness in phylogenetic deconvolution of bulk DNA samples of tumors (, 2019)
- FastME 2.0: a comprehensive, accurate, and fast distance-based phylogeny inference program (, 2015)
- FastTree: computing large minimum evolution trees with profiles instead of a distance matrix (, 2009)
- FastTree 2–approximately maximum-likelihood trees for large alignments (, 2010)

## Ground Truth Reference
- Figures: 22
- Tables: 1
- References: 44