# Experimental Log: Mapping drug biology to disease genetics to discover drug impacts on the human phenome

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsData curation and initial assessmentWe explore the premise that the effects of drugs on key biological processes propagate to their effects on disease genes, explaining the effect of drug on phenotype (Fig 1A).
- To implement and test this hypothesis, we aim to learn a model linking the biological processes altered by each drug (summarized in the matrix D) to the gene drivers of phenotype risk (in the matrix P), where the model is trained to predict the (incomplete) matrix Y of drug-phenotype association fro
- We obtain the drug-phenotype association matrices Y (drug side effects and drug indications) as binary (present or unrecorded) from SIDER.biorxiv;2023.01.22.525094v2/FIG1F1fig1Fig 1Design and support for the method.
- Translating the proposed model into an affinity regression integrating 1) similarity of a drug to all other drugs (ToxCast, D), 2) similarity of a disease to all other diseases (PhenomeXcan, Pt), and 3) known drug-disease relationships (SIDER, Y).
- The x-axis shows the Jaccard distance (1-Jaccard similarity index) and the y-axis shows the Spearman correlation of the disease pairs in terms of PhenomeXcan genomic profile.
- Phenotype pairs with higher PhenomeXcan similarity have lower Jaccard distance (Spearman correlation=-0.11).To represent the molecular profile of each drug in the matrix D, we compile EPA ToxCast assays recording a range of 1391 endpoints for hundreds of common medications.
- It is important to note that drugs are not assayed for all endpoints–on average, each drug is assayed for around 100 endpoints.
- Despite this, we found that drugs with more similar ToxCast endpoint profiles were more likely to be associated with the same phenotypes (p=1e-22, see Method for details), even when accounting for the number of endpoints assayed.
- To this end, we use SoftImpute(20), a method for dimensionality reduction and matrix completion (see Method).
- Although we doubtless lose some information about each drug’s biological effects, we find a strong correlation between the pairwise similarity of drugs before dimensionality reduction and as projected on the UDSD (Spearman correlation=0.21 comparing similarity of pairs of drugs from the matrix D ver
- GWAS of this data has associated loci with risk of thousands of phenotypes (including all common diseases as well as many health traits such as smoking)(21).
- The PhenomeXcan project integrates these GWAS results with expression quantitative trait locus results linking the same risk loci to expression of each gene(22).Therefore, the matrix P contains estimated association of regulation of each gene with presence of disease.
- Keeping only the genes that vary most highly across phenotypes, we obtain 10,027 genes for 197 phenotypes that can be matched to SIDER (either as indications or side effects).
- We found a strong relationship (p=4e-81, Fig 1C).Therefore, we conclude that drugs with more similar molecular profiles are associated with more similar side effects and indications.
- To exploit this signal, we adapt the affinity regression method(23,24).
- While affinity regression has previously been applied to predict continuous (normally distributed) data, here we model a binary outcome (drug-disease relation) in the model: DWPt = logit(p(Y)) (Fig 1B, see Methods).
- Matrices are summarized in Table 1.biorxiv;2023.01.22.525094v2/TBL1T1tbl1Table 1:Summary of matricesAssessment of the model’s predictive performanceAs an initial assessment of Draphnet, we test its ability to predict drug side effects.
- Predicting the drug side effects for held out drugs, we find that for a majority of drugs, our predictive model outperforms a nearest neighbor model as baseline (lower Jaccard distance between the predictions and the actual side effect profile, as compared to the nearest neighbor method, p=3e-8, ran
- This shows that Draphnet’s phenotype predictions can generalize to new drugs.biorxiv;2023.01.22.525094v2/FIG2F2fig2Fig 2A.
- Each point is one drug target, axes compare similarity of drugs that share that target versus the similarity of those drugs to other drugs (-log10 p-value of rank sum test).
- Significance is indicated by the stars (“*****+” indicates p-value < 10−5).
- Next, we investigate whether the drug phenome effect matrix reflects known characteristics of drugs.First, we confirm that drugs that share one or more known gene targets have more similar ToxCast endpoint effects (p=1e-28, rank sum test comparing distribution of Spearman correlation of pairs of dru
- However, for most drug targets, the true projection improves our ability to distinguish drugs sharing targets from those that do not, as compared to the null matrix (Fig 2B).While some drug target classes do not follow this pattern, this may be due to polypharmacology, which describes the complex na
- For example DrugBank annotates 14 drugs as targeting CHRM1, and this list include anticholinergics, neuroleptics, migraine treatments, and ophthalmological preparations.
- These 14 drugs have a median of 19 other targets.
- Comparing pairs of drugs that share targets, their phenome effect similarity is systematically higher in the true drug phenome effect matrix as compared to the same pairs of drugs in the null projection (Fig 2C).
- As a result, we create a matrix estimating for each drug the importance of its effect on each disease gene, which we call the drug-disease genome matrix (Supplementary Table 1).
- Because we compare the strength of each drug-gene connection to projections using the same input data (D and P) but with null models , these connections cannot be due only to the prior data on drug molecular effects: the drug-gene relations must be due to the learned interaction matrix that estimate
- In principle, we could estimate the chance a drug affects a particular disease by taking the dot product of the drug’s disease genome vector with the disease’s PhenomeXcan profile:



We obtain a median of 7 disease genes associated with each drug.
- Across 132 DrugBank targets shared by at least three drugs, we find 28 targets that have one or more significantly associated disease genes at adjusted p < 0.01 (Methods, Supplementary Table 2).
- Figure 3A shows that this level of association of drug disease genetics and drug targets is not likely to happen by chance.
- Therefore, we conclude that drugs sharing targets are more likely to impact the same disease genes, supporting the biological relevance of the drug-disease genome matrix.biorxiv;2023.01.22.525094v2/FIG3F3fig3Fig 3A.
- Empirical -log10 p-value calibration plot showing distribution of significance for drug target groups versus permuted drug targets.
- To the right, selected DrugBank targets of these drugs are shown.We visualize the variation in drug-gene associations across drugs in these target groups in Figure 3B, where each drug is labeled by its ATC therapeutic subgroup.
- We investigate some of the drug-disease gene relationships in Figure 3C.
- For example PPM1M is associated with a number of neuroleptic drugs that target HTR2C, involved in serotonin signaling.
- It is plausible that PPM1M could be a key driver of the effect of these drugs: it is the top PhenomeXcan gene for bipolar disorder; a recent study found loci in this gene to be associated with schizophrenia(25); and another study linked the locus to rare mental illness(26).
- Supporting a true effect of drugs on this driver, this gene has been associated with the effects of fenofibrate and PPARα agonism in experimental work(27,28).Learning a new categorization of drugsDiscovering biological effects of drugs is an open area of research.
- We focus on the disease genes linked to one or more targets, and we create a novel categorization of drugs based on overlap of these disease gene associations (Supplementary Table 3).
- Then, we identify fully connected cliques of drugs, containing at least 3 drugs that are all connected with each other.As expected, this categorization overlaps with known drug targets and drug effects.
- PPARα-agonists are known to modulate inflammation(29).
- Another connected drug is pyridoxine (vitamin B-6), a nutrient with diverse effects including anti-inflammation(30).
- Mecamylamine was discontinued as an antihypertensive in part because of its unintended diverse central nervous system effects, but more recently has been investigated for seizure and behavioral disorders(31).

## Tables

### Table 1:
> Summary of matrices


## Figure Descriptions

### Fig 1
Design and support for the method. A. Proposed model where a particular drug’s effects on endpoints (pink) can be propagated to impact on disease genes (green), genes in turn are associated with a phenotype (yellow), explaining drug effect on phenotype (dashed blue line). The same endpoint to diseas

### Fig 2
A. Prediction performance (Jaccard distance between predicted versus held-out drug effects) is substantially improved as compared to baseline predictive model. B. Each point is one drug target, axes compare similarity of drugs that share that target versus the similarity of those drugs to other drug

### Fig 3
A. Empirical -log10 p-value calibration plot showing distribution of significance for drug target groups versus permuted drug targets. B. tSNE visualization showing similarity of drugs according to their target significance, with ATC therapeutic groups highlighted. C. Drug significance for selected 

### Fig 4
Categorizing drugs based on association with disease genes.. Drugs are connected to their significant disease genes with gray lines. Drugs that share a significant overlap in disease genes are connected to each other with colored lines representing the cliques, where each color represents one unique

## References
Total references in published paper: 40

### Key References (from published paper)
- Evidence for benefit of statins to modify cognitive decline and risk in Alzheimer’s disease (, 2017)
- Beyond aspirin—cancer prevention with statins, metformin and bisphosphonates (, 2013)
- The SIDER database of drugs and side effects (, 2016)
- DrugBank 4.0: Shedding new light on drug metabolism (, 2014)
- The Drug Repurposing Hub: a next-generation drug library and information resource (, 2017)
- A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles (, 2017)
- ToxCast Chemical Landscape: Paving the Road to 21st Century Toxicology (, 2016)
- Computational repositioning of the anticonvulsant topiramate for inflammatory bowel disease (, 2011)
- Reversal of cancer gene expression correlates with drug efficacy and reveals therapeutic targets (, 2017)
- Discovery and preclinical validation of drug indications using compendia of public gene expression d (, 2011)
- Analysis of genome-wide association data highlights candidates for drug repositioning in psychiatry (, 2017)
- A gene-based association method for mapping traits using reference transcriptome data (, 2015)
- Exploring the phenotypic consequences of tissue specific gene expression variation inferred from GWA (, 2018)
- PREDICT: a method for inferring novel drug indications with application to personalized medicine (, 2011)
- Non-Negative Matrix Factorization for Drug Repositioning: Experiments with the repoDB Dataset (, 2020)
- DRIMC: an improved drug repositioning approach using Bayesian inductive matrix completion (, 2020)
- Improved anticancer drug response prediction in cell lines using matrix factorization with similarit (, 2017)
- Predicting the frequencies of drug side effects (, 2020)
- Turning genome-wide association study findings into opportunities for drug repositioning (, 2020)
- Matrix Completion and Low-Rank SVD via Fast Alternating Least Squares [Internet] (, 2014)
- PhenomeXcan: Mapping the genome to the phenome through the transcriptome (, 2020)
- Linking signaling pathways to transcriptional programs in breast cancer (, 2014)
- Affinity regression predicts the recognition code of nucleic acid–binding proteins (, 2015)
- Genome-wide association study of schizophrenia in Ashkenazi Jews (, 2015)
- Multivariate GWAS of psychiatric disorders and their cardinal symptoms reveal two dimensions of cros (, 2022)
- Selective CETP Inhibition and PPARα Agonism Increase HDL Cholesterol and Reduce LDL Cholesterol in H (, 2010)
- Cholesteryl Ester Transfer Protein Inhibition for Preventing Cardiovascular Events (, 2019)
- PPARα in atherosclerosis and inflammation (, 2007)
- Inflammation, vitamin B6 and related pathways (, 2017)
- Potential Therapeutic Uses of Mecamylamine and its Stereoisomers (, 2013)

## Ground Truth Reference
- Figures: 4
- Tables: 1
- References: 40