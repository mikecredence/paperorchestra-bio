## Working title
Draphnet: Integrating drug bioassays and disease genetics to map drug impacts on the human phenome

## Core question
Can a supervised linear model integrating in vitro drug bioassay profiles (ToxCast) with phenome-wide disease genetic profiles (PhenomeXcan) learn an interpretable network that both predicts drug-disease effects and reveals which disease driver genes each drug likely impacts?

## Motivation / gap
- Unintended drug effects (both harmful side effects and beneficial repurposing opportunities) are common but poorly understood mechanistically.
- Prior computational methods (connectivity score, matrix completion, gene-expression contrast methods such as So et al.'s S-PrediXcan-based approach) focus on prediction alone and do not learn how drug molecular effects propagate to disease biology.
- Rich systematic data are now available — EPA ToxCast/Tox21 assays, PhenomeXcan gene-based GWAS associations across ~197 UK Biobank phenotypes, and SIDER drug-phenotype annotations — but have not been jointly integrated into a single interpretable model.
- No prior method learns a shared drug-endpoint-to-disease-gene network that can be shared across thousands of drug-phenotype pairs.
- A method that is simultaneously predictive and interpretable could generate testable mechanistic hypotheses for drug repurposing and personalized medicine.

## Core contribution (bullet form)
- We introduce Draphnet, a supervised bilinear (affinity-regression) model trained by regularized logistic regression to predict the SIDER drug-phenotype matrix Y from the ToxCast drug-endpoint matrix D (429 compounds, 1391 endpoints) and the PhenomeXcan gene-phenotype matrix P (10,027 genes, 197 phenotypes).
- We establish the premise of the approach by showing that drugs with similar ToxCast profiles share more phenotypes (Spearman p=1e-22; linear model adjusted for shared-endpoint count p=1.7e-43) and that diseases with more similar PhenomeXcan profiles share more drugs (p=4e-81).
- In 20-fold cross-validation over held-out drugs, Draphnet's side-effect predictions significantly beat a nearest-neighbor baseline (lower Jaccard distance, rank-sum p=3e-8).
- The learned interaction matrix W_DP allows us to project each drug into a phenome-effect space and further into a drug-disease-genome matrix; drugs sharing known targets have significantly more correlated phenome-effect vectors than in a permutation null (target-level rank-sum tests, e.g., p=1e-28 for the aggregate test).
- Across 132 DrugBank targets shared by >=3 drugs, 28 targets show disease genes significantly associated with drug-target membership (adjusted p<0.01; Supplementary Table 2); representative associations include PPM1M with HTR2C-targeting neuroleptics and CETP with fenofibrate and other PPARalpha-targeting drugs.
- From the drug-disease-genome matrix we construct a novel drug categorization via fully connected cliques on significant disease-gene overlaps (Supplementary Table 3), recovering expected therapeutic groupings (e.g., calcium channel blockers) and surfacing unexpected ones (e.g., anti-inflammatories connected to PPARalpha-agonists; mecamylamine connected to pindolol and gabapentin).

## Method in brief
Draphnet implements affinity regression for a binary outcome. We model DWP^T = logit(p(Y)), where D is the drug-by-endpoint matrix (429 compounds x 1391 endpoints, with many missing entries) and P is the gene-by-phenotype matrix (10,027 genes x 197 phenotypes). D is imputed and dimensionality-reduced using SoftImpute, yielding the projection U_D S_D; hyperparameters (rank, regularization) were selected by a cross-validation procedure that masks 5% of non-missing entries and minimizes imputation MSE. P is factorized by SVD: P = U_P S_P V_P^T. Substituting these factorizations transforms the bilinear problem into a standard Kronecker-product regression: (V_P (x) (U_D S_D)) * stack(W_DP) = logit(p(Y)), which we solve with L1-regularized logistic regression. Final hyperparameters selected by cross-validation on held-out drugs: r_P = 131, r_D = 95, lasso regularization = 1. The regularization parameter is tuned by holding out 10% of drugs per fold.

After training, we multiply U_D S_D by W_DP to obtain a drug phenome-effect matrix, and further apply the inverse SVD transforms (using that U_P S_P has an orthogonal-like structure from equation 1) to project each drug onto the full 10,027-gene disease-genome space (equation 2). Significance of each drug-gene entry is assessed by a permutation null: Y is permuted 10,000 times, the full pipeline is rerun, and empirical p-values are computed and adjusted by Benjamini-Yekutieli. We then test drug-target gene enrichments by hypergeometric tests (Benjamini-Hochberg corrected) and construct drug-drug cliques on significant disease-gene overlap using the networkx package.

Predictions are evaluated by 20-fold cross-validation over drugs (5% held out per fold), comparing Jaccard distance between predicted and actual SIDER side-effect profiles against a nearest-neighbor baseline in D. Drug target annotations come from DrugBank and the Therapeutic Targets Database; ATC categories are used to color drugs in t-SNE visualizations of the disease-genome projections.

## Target venue
Nature Genetics
