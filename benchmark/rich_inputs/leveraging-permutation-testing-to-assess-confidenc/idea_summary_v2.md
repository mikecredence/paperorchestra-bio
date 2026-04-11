## Working title

Permutation testing as a confidence benchmark for positive-unlabeled learning in high-dimensional biological datasets

## Core question

Can permutation testing be adapted to the positive-unlabeled (PU) learning setting to provide a statistically grounded "no-information-rate" baseline, allowing researchers to distinguish reliable from unreliable PU classification models when true negative labels are unavailable?

## Motivation / gap

- PU learning is increasingly applied to biological and biomedical datasets where definitive negative examples are absent, but validating binary predictions without ground truth negatives is a major unresolved challenge
- Most prior PU learning evaluations report binary metrics (accuracy, F1, MCC) using ground truth labels that would not be available in real-world scenarios, creating an unrealistic assessment framework
- Permutation testing is a well-established technique for assessing model robustness in fully supervised learning, but it has never been applied to the PU learning context
- High-dimensional biological datasets (p >= n) are especially vulnerable to overfitting, and existing PU methods lack a principled approach to gauge whether learned classifications exceed chance performance
- The "spy" fold technique used in two-step reliable negative PU strategies has not been combined with permutation-based null distributions to create a unified confidence assessment pipeline

## Core contribution (bullet form)

- First application of permutation testing to PU learning, providing a null-hypothesis distribution against which actual PU Bagging scores can be compared for statistical significance
- Demonstrated that z-score-based comparison of actual vs. permuted label scores is more stable than independent two-sample t-tests across varying numbers of permutation replicates (p-value from z-score remains stable regardless of permutation count)
- Validated methodology across nine synthetic datasets varying in class separation (0, 1, 2 hypercube distances) and ground truth negative proportions (10%, 30%, 50% TN)
- Tested on real-world benchmark datasets: Wisconsin Diagnostic Breast Cancer (WDBC, 30 features, 400 samples), BRCA/LUAD RNA-seq (325 PCA components, 441 samples), and a humoral immune response dataset (36 Rhesus Macaques)
- Mean Bagging Score (MBS) showed lower standard deviation than Explicit Positive Recall (EPR) for both actual and permuted labels, yielding improved ability to detect differences between true and permuted label settings
- Cliff's delta effect size and z-score p-values together can reliably identify when PU models have meaningful predictive power vs. when class separation is insufficient

## Method in brief

The pipeline combines an enhanced "spy" fold strategy with PU Bagging and label permutation. Known positive (KP) samples are systematically held out as "spies" via repeated cross-validated folds, and the class 1 probability of each spy sample is computed by the PU Bagging algorithm. These scores are aggregated using two methods: Explicit Positive Recall (EPR, the proportion of KP samples correctly classified above a threshold) and Mean Bagging Score (MBS, the average class 1 probability across spy folds). The same inference pipeline is then applied after randomly permuting the P/U labels among samples for multiple replicates, generating a null distribution of scores.

Statistical confidence is assessed by comparing the single actual-label score against the distribution of permuted-label scores using (1) a one-sample z-score with associated p-value, and (2) Cliff's delta effect size with 95% confidence intervals. The z-score approach was shown to be preferable to two-sample independent t-tests because the latter can be artificially inflated by increasing the number of permutation replicates, while z-score statistics remain stable. The methodology was evaluated on synthetic datasets (200 features, 200 samples, 30% informative / 70% redundant features), three configurations of WDBC data, the BRCA/LUAD RNA-seq dataset after PCA dimensionality reduction, and a vaccine immunology dataset, with varied proportions and numbers of KP samples to stress-test applicability.

## Target venue

BMC Bioinformatics
