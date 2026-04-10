## Working title

Deep-Learning-Based Gene Perturbation Effect Prediction Does Not Yet Outperform Simple Linear Baselines

## Core question

Do current deep learning models -- including foundation models -- actually outperform deliberately simple linear baselines when predicting the transcriptomic effects of genetic perturbations?

## Motivation / gap

- Foundation models and deep learning methods are claimed to learn rich representations of cell biology that enable in silico prediction of unseen perturbation outcomes
- The field has lacked a rigorous comparison of these sophisticated models against trivially simple baselines
- Without such comparison, it is unclear whether the complexity of deep learning approaches is justified for this task

## Core contribution

- Benchmark of 5 foundation models and 2 other deep learning models against simple linear baselines on gene perturbation prediction
- Finding: for combinatorial perturbations (two genes, only singles seen), deep learning does not beat a simple additive model
- Finding: for unseen gene perturbations, deep learning does not outperform predicting the mean of training perturbations
- Hypothesis that poor performance is partially due to observational (not interventional) pre-training data
- Demonstration that a simple linear model trained on interventional data reliably outperforms all other approaches

## Method in brief

We will take Perturb-seq datasets with single and combinatorial gene knockdowns. For the combinatorial task, we test whether models can predict double-knockdown profiles from single-knockdown training data. For the unseen-gene task, we test leave-one-gene-out prediction. Baselines: (1) additive model (sum of single perturbation effects) for combinatorial; (2) mean-of-training-perturbations for unseen genes; (3) linear model trained on interventional data. Deep learning comparisons: 5 foundation models + 2 specialized deep learning models. Evaluation by correlation and MSE on held-out perturbation profiles.

## Target venue

Nature Methods
