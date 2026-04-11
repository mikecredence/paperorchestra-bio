## Working title
SPEAR: Supervised Bayesian Factor Model for Multi-Omics Signature Discovery

## Core question
Can jointly modeling multi-omics assays and a response of interest through supervised dimensionality reduction produce more predictive and biologically interpretable signatures than sequential unsupervised factor extraction followed by prediction?

## Motivation / gap
- Existing factor models (MOFA, iClusterBayes) perform dimensionality reduction without considering the response variable, leading to suboptimal predictive factors
- Multi-omics integration and predictive modeling are typically done sequentially, losing signal relevant to the outcome
- Current methods require manual tuning of factor number and lack adaptive sparsity across assays
- No existing method provides both sparse regression coefficients and full projection coefficients for downstream interpretation
- Feature selection in existing methods relies on arbitrary cutoffs on loading values rather than posterior probabilities

## Core contribution (bullet form)
- Developed SPEAR, a supervised variational Bayesian factor model that jointly models multi-omics data X and response Y with adaptive weight parameter w
- In simulations with moderate SNR, SPEAR (w=1) significantly outperformed MOFA in MSE and correctly recovered all 5 simulated factors vs only 2 by MOFA
- Achieved significantly higher AUROC for predicting COVID-19 severity (Moderate class) compared to MOFA and other baselines
- Achieved significantly higher AUROC for predicting breast cancer LumB subtype from TCGA multi-omics data
- Provides automatic factor rank estimation, automatic feature selection via posterior probabilities (analogous to FDR 0.05), and assay-wise automatic relevance determination (ARD)

## Method in brief
SPEAR assumes X = U * beta^T + E, where U are latent factor scores and beta are factor loadings. The response Y is also modeled as a linear function of factors: Y = U * beta_0 + noise. A weight parameter w controls the emphasis between explaining X structure and predicting Y: the joint model maximizes P_w(X|U) * P(Y|U). When w >= 1, SPEAR emphasizes factor structure in X; when w approaches 0, it focuses purely on predicting Y. The optimal w is selected by cross-validation, favoring larger w values by default to encourage biologically meaningful factors.

SPEAR uses variational Bayes inference with automatic relevance determination (ARD) for assay-wise factor influence and spike-and-slab priors for feature sparsity. This yields posterior probabilities of each feature being non-zero, enabling automatic feature selection at a threshold of 0.95 (analogous to FDR 0.05). The method supports Gaussian, ordinal, and multinomial response types. Factor rank is estimated automatically before fitting. SPEAR outputs both sparse regression coefficients (for prediction) and full projection coefficients (for biological interpretation).

## Target venue
Bioinformatics
