# Idea Summary

## Working title
Factorized visual representations in the primate visual system and deep neural networks

## Core question
Is factorization -- encoding different scene parameters (object identity, pose, viewpoint, background, lighting) in orthogonal subspaces of population activity -- a normative principle of biological visual representations, and do deep neural network models that factorize scene parameters better predict primate neural and behavioral data?

## Motivation / gap
- Object classification has been proposed as the principal objective of the ventral visual stream, but beyond a performance threshold, better classification does not yield better neural predictions -- motivating the search for additional normative principles
- Visual cortical neurons encode many types of information simultaneously (identity, pose, viewpoint), but how these different information types are geometrically organized in population activity space is poorly characterized
- Prior work has focused on invariance (discarding non-class information) as the strategy for supporting classification, but high-level cortical neurons clearly retain non-class information -- suggesting an alternative strategy
- The concept of disentanglement in machine learning typically requires independent factors to be encoded by distinct individual neurons, which is overly restrictive for neural populations; a subspace-level measure of factorization is needed
- No systematic study has tested whether factorization of individual scene parameters (lighting, background, viewpoint, pose) in DNN models predicts their similarity to primate neural and behavioral data across multiple independent datasets

## Core contribution (bullet form)
- Introduced formal measures of factorization and invariance for neural population codes, quantifying whether variance driven by different scene parameters occupies orthogonal subspaces
- Showed that factorization of object pose and background from identity increases from macaque V4 to IT and strongly contributes to improved identity decoding performance
- Conducted a large-scale analysis across a diverse library of DNN models, finding that models with higher factorization of scene parameters (especially object pose) are consistently more predictive of neural and behavioral data across 12 datasets from monkeys and humans
- Demonstrated that invariance to scene parameters was not as consistently associated with neural/behavioral prediction as factorization, suggesting that retaining non-class information in factorized subspaces is preferred over discarding it
- Showed that combining factorization with classification performance in a regression model significantly improved prediction of the most brainlike models, addressing the saturating relationship between classification and neural predictivity
- Controlled for confounds including model architecture (ResNet-50 subset analysis), dimensionality, and classification performance

## Method in brief
Factorization was measured using a PCA-based approach. For a given scene parameter (e.g., object pose), the fraction of parameter-induced variance that avoids the subspace spanned by all other parameters was computed. Specifically, the variance driven by one parameter was projected onto the subspace containing the majority of variance for all other parameters -- factorization is the fraction of variance that does NOT fall within this other-parameter subspace. Invariance was computed by comparing overall parameter-induced variance to the variance induced by other parameters. Both measures were applied to neural population responses (single-unit and multi-unit) and DNN layer activations.

For neural data, three macaque datasets (V4 and IT single-units; IT multi-units from chronic arrays; object recognition behavior) and three human datasets (two fMRI studies, one behavioral) were used -- 12 datasets total (Table S1). The DNN model library included supervised models (AlexNet, ResNet), self-supervised contrastive models (MoCo, SimCLR), and other unsupervised models, predominantly using ResNet-50 architecture (Table S2). For each model, factorization and invariance were computed for four scene parameters (lighting, background, camera viewpoint, object pose) using rendered 3D object stimuli with n=10 parameter levels each. Model "brainlikeness" was assessed as predictive power for neural responses (encoding model fits) or behavioral patterns across all 12 datasets. Regression analyses tested whether factorization improved prediction of brainlike models beyond classification performance or dimensionality alone.

## Target venue
eLife
