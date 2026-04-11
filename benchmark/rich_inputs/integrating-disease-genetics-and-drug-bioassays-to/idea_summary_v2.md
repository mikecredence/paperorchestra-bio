## Working title

Draphnet: learning a network connecting drug biological effects to disease genetics for predicting and interpreting drug-phenotype associations

## Core question

Can a supervised linear model that integrates in vitro drug bioassay data (ToxCast) with genome-wide disease gene associations (PhenomeXcan) learn an interpretable network explaining how drug molecular effects propagate to disease phenotypes, and can this network predict drug side effects and repurposing opportunities?

## Motivation / gap

- Drugs frequently have unexpected effects on diverse diseases (both harmful side effects and beneficial repurposing), but the biological basis connecting drug molecular action to disease phenotypes is poorly understood
- Existing computational methods (connectivity scores, expression-based approaches) focus on prediction rather than learning interpretable drug-disease biology
- ToxCast/Tox21 in vitro bioassay data and PhenomeXcan GWAS-derived gene-disease associations are rich but untapped resources for systematic drug-phenotype modeling
- No prior method has integrated ToxCast endpoint data across hundreds of drugs with PhenomeXcan gene-disease profiles across nearly 200 phenotypes in a unified framework
- Matrix completion and other prediction-focused methods lack biological interpretability -- they cannot explain why a drug affects a phenotype

## Core contribution (bullet form)

- Developed Draphnet, a supervised affinity regression model integrating 429 drugs (ToxCast endpoints, 1391 assays) and ~200 UK Biobank phenotypes (PhenomeXcan gene associations) with SIDER drug-phenotype labels
- Prediction performance (Jaccard distance) substantially outperforms a baseline model that uses only drug-drug and phenotype-phenotype similarity
- Demonstrated that drugs sharing Draphnet-predicted biological effects also share known gene targets (validated against DrugBank), supporting biological plausibility
- Identified disease genes impacted by drug targets (e.g., anti-inflammatories and PPARa-agonists share downstream effects on CETP, experimentally supported as a fenofibrate effector)
- Proposed new drug groupings based on shared effects on the disease genome, revealing cliques of drugs with overlapping disease gene associations
- Showed that ToxCast endpoint similarity correlates with shared SIDER phenotypes (p = 1e-22) and PhenomeXcan genomic profile similarity correlates with phenotype co-occurrence (Spearman rho = -0.11)

## Method in brief

The core model is an affinity regression: Y ~ D * W * P^T, where Y is the binary drug-phenotype association matrix from SIDER, D encodes drug similarity based on ToxCast endpoint profiles (dimensionality-reduced via SoftImpute), P encodes phenotype similarity based on PhenomeXcan S-MultiXcan gene-disease z-scores, and W is the learned interaction matrix connecting drug biological endpoints to disease genes. The model is trained with L2 regularization to predict held-out drug-phenotype pairs.

ToxCast Level 5 data (hit-call fractions across 1391 endpoints for 429 compounds) were preprocessed using SoftImpute for dimensionality reduction and missing value imputation, projecting each drug to a lower-dimensional space U_D * S_D. PhenomeXcan gene-phenotype associations were derived from S-MultiXcan p-values converted to signed z-scores, keeping the top half of most variably associated genes. SIDER drug-phenotype associations (side effects and indications) were matched to UK Biobank phenotypes via UMLS concept identifiers.

After training, the learned matrix W can be used to project each drug into "disease gene space," revealing which disease driver genes are predicted to be downstream of that drug's molecular effects. Drug target significance was assessed by comparing the pairwise similarity of drugs sharing a target (from DrugBank) against null distributions. Drugs were clustered based on shared disease gene associations to identify biologically meaningful drug groupings.

## Target venue

Bioinformatics Advances
