## Working title
PEPerMINT: Graph Neural Network-Based Peptide-Level Imputation for Mass Spectrometry Proteomics

## Core question
Can a graph neural network that leverages peptide-to-protein relationships and amino acid sequence embeddings outperform existing imputation methods for missing peptide abundance values in mass spectrometry proteomics?

## Motivation / gap
- Missing peptide abundance values are extremely common in label-free MS proteomics (22-69% of values), propagating to protein-level analyses
- Existing imputation methods (KNN, RF, PCA, BPCA, etc.) do not exploit the structural relationship between peptides belonging to the same protein
- No existing method uses amino acid sequence information to inform imputation
- Deep learning approaches (DAE, VAE) have not been tailored to the peptide graph structure
- No existing imputation method provides uncertainty estimates for imputed values
- Imputation is typically done at protein level; peptide-level imputation could be more informative

## Core contribution (bullet form)
- Developed PEPerMINT, a GNN model operating on peptide-peptide graphs with ProtT5 sequence embeddings, achieving best RMSE across all six benchmark datasets
- Outperformed the second-best method (BPCA) by up to 20% RMSE on the breast cancer dataset
- Maintained superior performance across varying degrees of missingness per peptide, with the largest advantage at high missingness fractions
- Achieved the best differential expression (DE) prediction (highest AUC on HeLa-E.coli dataset at 5% FDR)
- Provided meaningful uncertainty estimates that correlate with imputation error, enabling filtering of unreliable imputed values
- Demonstrated that uncertainty-based filtering further improves downstream DE prediction performance

## Method in brief
PEPerMINT takes as input a peptide abundance matrix A (n peptides x s samples) with missing values, plus sequence embeddings S (n x 1024) generated from amino acid sequences using the ProtT5 language model. Peptide-to-protein relationships are encoded as a peptide-peptide graph G where peptides sharing a protein are fully connected. The architecture applies a learnable transformation to scale down sequence embeddings, concatenates them with abundance vectors, applies a non-linear transformation to create latent representations, and uses graph attention layers (GAT) to propagate information across the peptide graph. The model is trained via self-supervised learning by masking known abundance values and predicting them.

Benchmarking was performed against 11 imputation methods (Median, KNN, ISVD, PCA, RF, BPCA, MICE, CF, MinDet, MinProb, DAE, VAE) across six diverse datasets spanning cell lines, tissue, and plasma samples. Evaluation used sample-wise RMSE with artificially introduced missing values for four datasets and DDA/DIA ground truth for two datasets. Wilcoxon signed-rank tests were used for pairwise statistical comparisons. Differential expression analysis used ROC curves with FDR thresholds.

## Target venue
Bioinformatics
