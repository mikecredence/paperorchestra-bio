## Working title
Mapping drug biology to disease genetics to discover drug impacts on the human phenome

## Core question
Can a supervised linear model that integrates in vitro drug bioassay data with phenome-wide genetic studies learn an interpretable network connecting drug molecular effects to disease gene drivers, thereby explaining and predicting drug effects on disease phenotypes?

## Motivation / gap
- Unintended drug effects (both harmful side effects and beneficial repurposing opportunities) are widespread, but discovering how biological effects of drugs relate to disease biology remains challenging
- Existing computational methods (connectivity scores, matrix completion) focus on predicting drug effects rather than learning how drug molecular effects relate to disease biology
- Rich data now profiles both drug impacts on biological processes (EPA ToxCast) and known drug-phenotype associations (SIDER), but no method has systematically integrated ToxCast with phenome-wide genetic data for drug effect discovery
- The PhenomeXcan resource links phenotypes to disease driver genes, but has only been used to suggest drugs for a few individual diseases rather than integrated across hundreds of phenotypes
- There is a need for interpretable models that provide biological rationale for drug effect predictions, not just predictions themselves

## Core contribution (bullet form)
- Developed Draphnet, a supervised linear model integrating in vitro data on 429 drugs (1391 ToxCast endpoints) and gene associations of nearly 200 common phenotypes (10,027 genes) to learn a network connecting molecular signals to drug effects on disease
- Drugs with more similar ToxCast endpoint profiles are more likely associated with same phenotypes (Spearman correlation, p = 1e-22; linear model accounting for shared endpoints, p = 1.7e-43); diseases with more similar PhenomeXcan profiles impacted by more similar drug sets (p = 4e-81)
- Draphnet outperforms nearest-neighbor baseline for predicting drug side effects on held-out drugs (Wilcoxon rank sum test, p = 3e-8)
- Drugs sharing known gene targets have more similar ToxCast endpoint effects (rank sum test, p = 1e-28) and the learned drug phenome effect matrix further distinguishes shared-target drugs beyond input data similarity
- Across 132 DrugBank targets shared by at least 3 drugs, 28 targets have one or more significantly associated disease genes at adjusted p < 0.01
- Drug-disease genome matrix reveals biologically plausible connections: PPM1M associated with neuroleptics targeting HTR2C; CETP associated with fenofibrate and lipid metabolism drugs

## Method in brief
Draphnet learns a bilinear model DWPt = logit(p(Y)), where D is a drug endpoint matrix from EPA ToxCast (1391 endpoints for 429 drugs, ~100 endpoints assayed per drug on average), P is a disease gene matrix from PhenomeXcan (10,027 genes for 197 phenotypes matched to SIDER), and Y is a binary drug-phenotype association matrix from SIDER. Drug endpoint profiles are reduced via SoftImpute dimensionality reduction to create UDSD (handling sparse/missing values). Disease gene profiles are decomposed via standard SVD. The model is reformulated as (Vp x UDSD) x stack(WDP) = logit(p(Y)), learning the smaller matrix WDP via regularized logistic regression (lasso, lambda = 1). Cross-validation holds out 10% of drugs per fold; ranks are rP = 131 and rD = 95. Phenotype matching uses UMLS concept unique identifiers (CUIs). Gene-based scores use signed |Phi^-1(multiXanP_gene,phenotype)| from S-MultiXcan. The drug phenome effect matrix UDSD*WDP maps each drug to its compressed effect across phenotypes. Further projection to disease genome space yields per-drug significance of effect on each disease gene, assessed against 10,000 permutation-based null models with Benjamini-Yekutieli correction.

Drug categorization uses a drug-drug network based on significant overlap in disease gene associations. Fully connected cliques of at least 3 drugs are identified. Assessment of drug-target group enrichment for disease genes uses hypergeometric test with Benjamini-Hochberg correction.

## Target venue
Bioinformatics Advances
