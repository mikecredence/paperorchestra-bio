Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Bioinformatics

## Idea Summary

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


## Experimental Log

# Experimental Log: PEPerMINT Peptide Imputation

## Benchmark Datasets Overview (Table 2)

| Dataset | Ground Truth Type | Samples | Biological Samples | Tech Reps per BS | Proteins | Peptides | % Missing |
|---------|------------------|---------|-------------------|-----------------|----------|----------|-----------|
| Prostate cancer (A1) | Masked | -- | -- | -- | -- | -- | ~30-40% |
| Breast cancer | Masked | -- | -- | 0 | -- | -- | ~50-60% |
| HeLa-E.coli | DDA/DIA | -- | -- | -- | -- | -- | ~22-40% |
| HIV blood | DDA/DIA | -- | -- | -- | -- | -- | ~60-69% |
| Dataset 5 | Masked | -- | -- | -- | -- | -- | ~30% |
| Dataset 6 | Masked | -- | -- | -- | -- | -- | ~40% |

Note: Missing value percentages across the six datasets ranged from 22.1% to 68.8%.

## Imputation Methods Benchmarked (Table 1)

| Method | Category | Description |
|--------|----------|-------------|
| Median | Basic | Peptide-wise median imputation |
| KNN | Basic | k-nearest neighbors |
| ISVD | Basic | Iterative singular value decomposition |
| PCA | Basic | Principal component analysis |
| RF | Basic | Random forest |
| BPCA | Complex | Bayesian PCA |
| MICE | Complex | Multiple imputation by chained equations |
| CF | Complex | Collaborative filtering / matrix factorization |
| MinDet | Simple | Minimum value detection limit |
| MinProb | Simple | Minimum probability-based |
| DAE | Deep learning | Denoising autoencoder |
| VAE | Deep learning | Variational autoencoder |
| PEPerMINT | Deep learning (GNN) | Our proposed method |

## Abundance-Based Evaluation: Sample-Wise RMSE (Fig 3A)

| Method | Prostate (A1) | Breast Cancer | HeLa-E.coli | HIV Blood | Dataset 5 | Dataset 6 |
|--------|--------------|---------------|-------------|-----------|-----------|-----------|
| PEPerMINT | Best | Best | Best | Best | Best | Best |
| BPCA | 2nd-3rd | 2nd (up to 20% worse) | 2nd-3rd | mid | 2nd-3rd | 2nd-3rd |
| RF | 2nd-3rd | 3rd-4th | 2nd-3rd | mid | 2nd-3rd | 2nd-3rd |
| MICE | mid | mid | mid | mid | mid | mid |
| CF | mid | mid | mid | mid | mid | mid |
| Median | mid | mid | mid | mid | mid | mid |
| KNN | worse | worse | worse | worse | worse | worse |
| DAE | worse | worse | worse | worse | worse | worse |
| VAE | worse | worse | worse | worse | worse | worse |
| ISVD | worst | worst | worst | mid | worst | worst |
| MinDet | worst | worst | worst | good | worst | worst |
| MinProb | worst | worst | worst | good | worst | worst |

Key finding: PEPerMINT outperformed the second-best method (BPCA) by up to 20% RMSE on the breast cancer dataset. Similar results were obtained with mean absolute error.

## Performance by Fraction of Missing Values (Fig 3B, Prostate Cancer)

| Missingness Fraction | PEPerMINT Rank | Observation |
|---------------------|----------------|-------------|
| 0-20% | 1st | Advantage over competitors moderate |
| 20-40% | 1st | Growing advantage |
| 40-60% | 1st | Large advantage |
| 60-80% | 1st | Largest advantage over competitors |
| 80-100% | 1st | Biggest margin over other methods |

Key observations:
- PEPerMINT, RF, BPCA, CF, DAE, and especially ISVD improve when missingness decreases
- MinProb and MinDet perform better with higher fractions of missing values
- PEPerMINT's largest advantage is for peptides with high fraction of missing values

## Statistical Comparison (Wilcoxon Signed-Rank Test, Fig 4)

| Comparison | Datasets Where PEPerMINT Significantly Better | Datasets Where Tie | Datasets Where Significantly Worse |
|-----------|----------------------------------------------|-------------------|-----------------------------------|
| PEPerMINT vs Median | Majority (4-6/6) | 0-2 | 0 |
| PEPerMINT vs KNN | Majority (5-6/6) | 0-1 | 0 |
| PEPerMINT vs ISVD | Majority (5-6/6) | 0-1 | 0 |
| PEPerMINT vs RF | Majority (4-5/6) | 1-2 | 0 |
| PEPerMINT vs BPCA | Majority (4-5/6) | 1-2 | 0 |
| PEPerMINT vs MICE | Majority (4-5/6) | 1-2 | 0 |
| PEPerMINT vs CF | Majority (4-5/6) | 1-2 | 0 |
| PEPerMINT vs MinDet | Majority (4-6/6) | 0-2 | 0 |
| PEPerMINT vs MinProb | Majority (4-6/6) | 0-2 | 0 |
| PEPerMINT vs DAE | Majority (5-6/6) | 0-1 | 0 |
| PEPerMINT vs VAE | Majority (5-6/6) | 0-1 | 0 |

PEPerMINT performed significantly better than all other methods on the majority of benchmark datasets (5% significance level).

## Differential Expression Analysis (Fig 5)

| Method | AUC (HeLa-E.coli) | FDR 5% Performance |
|--------|-------------------|-------------------|
| PEPerMINT | Highest | Best true positive rate at 5% FDR |
| RF | High | Good |
| BPCA | High | Good |
| MICE | Moderate | Moderate |
| Others | Lower | Worse |

Fig 5 shows ROC curves for DE prediction on the HeLa-E.coli dataset. PEPerMINT (yellow line) has the largest AUC and best performance at the 5% FDR threshold.

## Uncertainty Estimation (Fig 6)

| Analysis | Result |
|----------|--------|
| Correlation of predicted uncertainty with actual error | High positive correlation |
| Low uncertainty imputed values | Low RMSE |
| High uncertainty imputed values | High RMSE |
| Uncertainty quantile filtering | Progressive RMSE improvement as high-uncertainty values removed |

### Uncertainty-Filtered DE Analysis (Fig 6C)

| Uncertainty Threshold | Effect on DE Prediction |
|----------------------|------------------------|
| No filtering | Baseline PEPerMINT performance |
| Remove top 10% uncertainty | Improved precision at low FDR |
| Remove top 25% uncertainty | Further improvement |
| Remove top 50% uncertainty | Best precision at low FDR |

Fig 6A: Scatter of imputed vs ground truth values colored by predicted uncertainty shows high-uncertainty predictions tend to be further from the diagonal.
Fig 6B: RMSE computed over different uncertainty quantiles shows monotonic improvement as unreliable values are excluded.
Fig 6C: ROC curve zoomed at low FDR shows progressively better DE detection when filtering by uncertainty.

## Ablation Studies

| Component Removed | Effect on Performance |
|-------------------|---------------------|
| Sequence embeddings (ProtT5) | Performance decreases |
| Graph structure (peptide-peptide edges) | Performance decreases |
| Both sequence + graph | Largest decrease |
| Full PEPerMINT | Best performance |

The ablation confirms that both amino acid sequence information and peptide-peptide graph structure contribute to PEPerMINT's superior performance. Sequence embeddings allow PEPerMINT to capture biophysical properties; graph structure enables information sharing across peptides from the same protein.

## Architecture Details

| Component | Specification |
|-----------|--------------|
| Sequence embedding model | ProtT5 (1024-dimensional) |
| Sequence embedding transformation | Learnable linear projection (downscaling) |
| Abundance transformation | Non-linear MLP |
| Graph layer | Graph Attention Network (GAT) |
| Training scheme | Self-supervised (random masking) |
| Loss function | MSE on masked values |
| Input normalization | Log-transformed, zero-mean, unit-variance |

## Runtime Comparison (Fig S8)

| Method | Relative Runtime |
|--------|-----------------|
| Median | Fastest |
| KNN | Fast |
| MinDet | Fast |
| MinProb | Fast |
| ISVD | Moderate |
| PCA | Moderate |
| MICE | Moderate |
| RF | Moderate-Slow |
| BPCA | Moderate-Slow |
| CF | Moderate |
| DAE | Slow |
| VAE | Slow |
| PEPerMINT | Slow (but comparable to DAE/VAE) |

## Key Figure Observations

- Fig 1A: Architecture overview showing abundance matrix + ProtT5 embeddings fed into GNN operating on peptide graph
- Fig 1B: Comparison of 11 published methods from three categories (basic, complex, deep learning)
- Fig 1C-D: Evaluation framework with six datasets and two ground truth approaches (masked and DDA/DIA)
- Fig 2: Simplified neural network diagram showing sequence scaling, concatenation, latent representation, and graph attention
- Fig 3A: Bar charts of sample-wise RMSE across all six datasets with 95% CI error bars; PEPerMINT consistently lowest
- Fig 3B: Stratified results by missingness fraction; PEPerMINT advantage grows with more missing values
- Fig 4: Heatmap of pairwise statistical comparisons; PEPerMINT row is predominantly blue (significantly better)
- Fig 5: ROC curves for DE analysis; PEPerMINT curve dominates others
- Fig 6: Uncertainty analysis showing correlation with error and utility for downstream filtering

## Discussion Notes

- PEPerMINT's advantage is largest on the breast cancer dataset which lacks technical replicates, suggesting the model learns biological patterns rather than just averaging replicates
- Performance on the HIV blood dataset (high MNAR fraction) explains why MinDet/MinProb perform relatively well there
- Self-supervised training aligns with MCAR missing mechanism; still works well for mixed MCAR/MNAR
- Sequence embeddings and graph structure provide context even for peptides with very few observed values
- Novel uncertainty estimation feature distinguishes PEPerMINT from all other benchmarked methods

