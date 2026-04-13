Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Bioinformatics Advances

## Idea Summary

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


## Experimental Log

# Experimental Log: Draphnet -- Drug-Phenotype Network via Bioassay-Genetics Integration

## Data Sources and Matrix Definitions

| Matrix | Description | Rows | Columns | Source |
|--------|-------------|------|---------|--------|
| Y | Drug-phenotype associations (binary: present/unrecorded) | 429 drugs | ~200 phenotypes | SIDER |
| D | Drug molecular endpoint profiles | 429 drugs | 1391 endpoints (sparse) | EPA ToxCast/Tox21 Level 5 |
| P | Gene-phenotype association z-scores | Top variable genes | ~200 phenotypes | PhenomeXcan (S-MultiXcan) |
| W | Learned interaction matrix (endpoints to disease genes) | Reduced drug dims | Reduced phenotype dims | Trained by Draphnet |

### Data Preprocessing Summary

| Step | Details |
|------|---------|
| ToxCast data level | Level 5 (hit-call fractions) |
| Number of endpoints | 1391 |
| Number of drugs | 429 |
| Average endpoints assayed per drug | ~100 |
| Dimensionality reduction method | SoftImpute (SVD with missing value imputation) |
| SoftImpute hyperparameter selection | Cross-validation (5% held out non-missing values, MSE metric) |
| Drug projection | U_D * S_D (lower-dimensional drug representation) |
| PhenomeXcan gene score | abs(inverse_normal(S-MultiXcan p)) * sign(consensus S-PrediXcan direction) |
| Gene filtering | Top half most variably associated with phenotype (highest SD) |
| Phenotype matching | UMLS concept unique identifiers (CUIs) to link UK Biobank to SIDER |

## Premise Validation: Molecular Similarity Predicts Phenotypic Similarity

### Drug-Drug Similarity Analysis

| Comparison | Metric | Result | P-value |
|-----------|--------|--------|---------|
| ToxCast endpoint similarity vs. shared SIDER phenotypes | Correlation/enrichment | More similar endpoints = more shared phenotypes | p = 1e-22 |
| Accounting for number of endpoints assayed | Adjusted analysis | Relationship holds after adjustment | Significant |

### Phenotype-Phenotype Similarity Analysis

| Comparison | Metric | Result |
|-----------|--------|--------|
| PhenomeXcan genomic profile similarity vs. Jaccard similarity of drug associations | Spearman correlation | rho = -0.11 (higher genomic similarity = lower Jaccard distance) |

- Fig 1C: Scatter plot showing each point as one disease pair; x-axis = Jaccard distance, y-axis = Spearman correlation of PhenomeXcan profiles

## Model Architecture

### Affinity Regression Framework

| Component | Mathematical Role | Data Source |
|-----------|------------------|-------------|
| Drug similarity (D) | Kernel over drug space | ToxCast (SoftImpute-reduced) |
| Phenotype similarity (P^T) | Kernel over phenotype space | PhenomeXcan z-scores |
| Interaction matrix (W) | Learned endpoint-to-gene network | Trained on SIDER labels |
| Prediction | Y_hat = D * W * P^T | -- |
| Regularization | L2 (ridge) | Addresses limited training data |

### Training Details

| Parameter | Value |
|-----------|-------|
| Training labels | SIDER binary (side effect present / unrecorded) |
| Separate models | Side effects and indications |
| Evaluation | Cross-validation |
| Baseline model | Drug-drug and phenotype-phenotype similarity only (no learned W) |
| Prediction metric | Jaccard distance (predicted vs. held-out drug effects) |

## Prediction Performance (Fig 2A)

| Model | Jaccard Distance (predicted vs. held-out) | Comparison |
|-------|------------------------------------------|------------|
| Draphnet | Substantially lower (better) | -- |
| Baseline (similarity only) | Higher (worse) | Draphnet significantly outperforms |

- Fig 2A: Draphnet prediction performance substantially improved compared to baseline

## Drug Target Validation (Fig 2B-C)

### Drug Target Similarity Analysis

| Analysis | Description | Result |
|---------|-------------|--------|
| Rank sum test per drug target | Compare Draphnet projection similarity of drugs sharing that target vs. drugs not sharing it | Most targets show significant enrichment |
| Null comparison | Same analysis with permuted drug projections | Null shows no enrichment |

- Fig 2B: Each point is one drug target; axes compare similarity of drugs sharing that target vs. other drugs (-log10 p-value of rank sum test)
- Fig 2C: Distributions of pairwise Spearman correlation for drugs sharing various targets in real projection vs. null projection

### Drug Target Significance

| Target Group | Real Projection Correlation | Null Projection Correlation | Significance |
|-------------|---------------------------|---------------------------|-------------|
| Shared targets (various) | Higher than null | Near zero | Indicated by asterisks in Fig 2C |

- Drugs sharing known gene targets (from DrugBank) have more similar Draphnet projections, supporting biological interpretability

## Calibration and Target Analysis (Fig 3)

### Empirical P-value Calibration (Fig 3A)

| Analysis | Result |
|---------|--------|
| Distribution of significance for drug target groups vs. permuted | Real targets show enrichment of significant associations compared to permuted |

- Fig 3A: Calibration plot confirms that drug target significance is well above permutation null

### tSNE Drug Clustering by Target Significance (Fig 3B)

| Observation | Details |
|------------|---------|
| ATC therapeutic groups highlighted | Drugs cluster by therapeutic class in tSNE space |
| Clustering basis | Target significance patterns from Draphnet |

- Fig 3B: tSNE visualization shows drugs group by ATC class when embedded using Draphnet target significance

### Selected Drug-Target-Disease Gene Associations (Fig 3C)

| Drug Category | Example Drugs | Significant Targets (DrugBank) | Disease Gene Associations |
|--------------|---------------|-------------------------------|--------------------------|
| Anti-inflammatories | Various NSAIDs | COX targets | Downstream effects on disease genes |
| PPARa-agonists | Fenofibrate, others | PPARa | CETP (experimentally supported effector) |
| PPARg-agonists | Thiazolidinediones | PPARg | RP11-54O7.17 (adjacent to PERM1, known PPARg effector) |

- Fig 3C: Green scale shows significance of drug association with disease genome for selected drugs and their DrugBank targets

### CETP Discovery

| Finding | Details |
|---------|---------|
| Anti-inflammatories downstream effect | Shared effect on CETP |
| PPARa-agonists downstream effect | Shared effect on CETP |
| Experimental support | CETP previously experimentally validated as fenofibrate effector |

## Drug Grouping by Disease Gene Effects (Fig 4)

### Drug Clique Analysis

| Analysis Step | Description |
|-------------|-------------|
| Connect drugs to significant disease genes | Gray lines in network |
| Identify drugs with significant overlap in disease genes | Colored lines connecting drug pairs |
| Clique detection | Fully connected subgraphs of 3+ drugs |
| Filtering | Show only disease genes associated with 1+ gene targets and <15 drugs |

- Fig 4: Network visualization showing drug-disease gene connections and drug cliques
- Each color represents a unique clique of drugs sharing disease gene associations
- Provides new drug groupings based on shared downstream genomic effects rather than traditional pharmacological classification

## Limitations and Parameters

| Limitation | Mitigation |
|-----------|-----------|
| Incomplete Y matrix (unrecorded != absent) | Regularization, cross-validation |
| Low training data relative to parameter count | Reduced feature space, L2 regularization |
| ToxCast sparsity (~100 endpoints per drug of 1391) | SoftImpute dimensionality reduction |
| Ambiguity in GWAS-to-gene assignment | PhenomeXcan uses S-MultiXcan consensus across tissues |
| eQTL-based gene mapping may miss some genes | Alternative resources could be explored |

### SoftImpute Cross-Validation for ToxCast

| Parameter | Selection Method |
|-----------|-----------------|
| Rank of decomposition | CV (5% held-out non-missing values) |
| Regularization parameter | CV (MSE of imputed held-out values) |

## Key Statistical Tests

| Test | Application | Result |
|------|------------|--------|
| Jaccard distance comparison | Draphnet vs. baseline prediction | Draphnet substantially better |
| Rank sum test | Drug target similarity in projection space | Most targets significant |
| Permutation test | Null distribution for target significance | Real enrichment exceeds null |
| Spearman correlation | PhenomeXcan similarity vs. Jaccard distance | rho = -0.11 |
| P-value for ToxCast-phenotype correlation | Endpoint similarity predicts shared phenotypes | p = 1e-22 |

## External Data Resources Used

| Resource | Content | Usage |
|----------|---------|-------|
| SIDER | Drug side effects and indications with CUIs | Training labels (Y matrix) |
| EPA ToxCast/Tox21 | In vitro bioassay endpoints for compounds | Drug molecular profiles (D matrix) |
| PhenomeXcan | Gene-phenotype associations from UK Biobank GWAS | Disease gene profiles (P matrix) |
| DrugBank | Known drug gene targets | Validation of learned projections |
| UMLS | Medical concept identifiers | Phenotype name matching |
| UK Biobank | GWAS results for common phenotypes | Input to PhenomeXcan |
| S-PrediXcan / S-MultiXcan | Gene-level association methods | Convert GWAS to gene associations |

## Potential Applications

| Application | Description |
|-------------|-------------|
| Drug repurposing | Predict new drug-phenotype associations |
| Side effect prediction | Anticipate adverse effects from molecular profiles |
| Disease gene discovery | Identify disease genes impacted by drug targets |
| Drug mechanism elucidation | Explain why a drug affects a phenotype via endpoint-gene network |
| Drug classification | Group drugs by shared disease genome effects rather than targets |
| Personalized medicine | Adapt model to predict individual drug effects based on risk allele profiles |

## Summary of Matrices Dimensions

| Matrix | Dimensions | Completeness |
|--------|-----------|-------------|
| Y (side effects) | 429 drugs x ~200 phenotypes | Sparse (binary, incomplete) |
| Y (indications) | 429 drugs x ~200 phenotypes | Sparse (binary, incomplete) |
| D (ToxCast raw) | 429 drugs x 1391 endpoints | Many missing entries |
| D (SoftImpute reduced) | 429 drugs x k (reduced rank) | Complete after imputation |
| P (PhenomeXcan) | ~N genes x ~200 phenotypes | Complete (z-scores) |
| W (learned) | k x N_genes (reduced) | Complete (trained) |

