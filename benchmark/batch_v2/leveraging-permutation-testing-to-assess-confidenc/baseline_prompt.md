Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: BMC Bioinformatics

## Idea Summary

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


## Experimental Log

# Experimental Log: Permutation Testing for Confidence in PU Learning

## 1. Dataset Summary

### 1.1 Synthetic Datasets

| Dataset ID | Samples (n) | Features (p) | Informative Features | Redundant Features | TN Proportion | Class Separation | Notes |
|---|---|---|---|---|---|---|---|
| Table 1a | 200 | 200 | 30% (60) | 70% (140) | 10% | High (dist=2) | p >= n setting |
| Table 1a | 200 | 200 | 30% (60) | 70% (140) | 30% | High (dist=2) | p >= n setting |
| Table 1a | 200 | 200 | 30% (60) | 70% (140) | 50% | High (dist=2) | p >= n setting |
| Table 1b | 200 | 200 | 30% (60) | 70% (140) | 10% | Medium (dist=1) | p >= n setting |
| Table 1b | 200 | 200 | 30% (60) | 70% (140) | 30% | Medium (dist=1) | p >= n setting |
| Table 1b | 200 | 200 | 30% (60) | 70% (140) | 50% | Medium (dist=1) | p >= n setting |
| Table 1c | 200 | 200 | 30% (60) | 70% (140) | 10% | None (dist=0) | Negative control |
| Table 1c | 200 | 200 | 30% (60) | 70% (140) | 30% | None (dist=0) | Negative control |
| Table 1c | 200 | 200 | 30% (60) | 70% (140) | 50% | None (dist=0) | Negative control |
| Table 1g | 100 | 200 | 30% (60) | 70% (140) | Moderate | Medium | For permutation count stability test |

### 1.2 Real-World Benchmark Datasets

| Dataset | Total Samples | Features | TN Proportions Tested | Feature Type | Source |
|---|---|---|---|---|---|
| WDBC (Table 1d) | 400 (sampled from 569) | 30 | 10.8%, 30%, 50% | Cell nuclei measurements | UCI Repository |
| BRCA/LUAD (Table 1e) | 441 (300 BRCA + 141 LUAD) | 325 PCs (95% variance retained) | Fixed (LUAD as TN) | RNA-Seq gene expression (PCA-reduced) | PANCAN dataset |
| Lakhashe (Table 1f) | 36 Rhesus Macaques | Multiplex immunoassay features | Fixed (group L as TN, n=36) | Humoral immune profiles | Vaccine immunology study |

### 1.3 PU Label Simulation Settings

| Parameter | Detail |
|---|---|
| TP label assignment | Ground truth positive samples |
| TN label assignment | Ground truth negative samples |
| KP (Known Positive) selection | Random subset of TP, varied proportions |
| Unlabeled set composition | Remaining TP + all TN |
| WDBC class mapping | Malignant -> Class 0 (TN), Benign -> Class 1 (TP) |
| BRCA/LUAD class mapping | BRCA -> TP (n=300), LUAD -> TN (n=141) |
| Lakhashe class mapping | Groups M,K -> TP; Group L (efficacious) -> TN (n=36) |

## 2. Pipeline Architecture

| Stage | Component | Detail |
|---|---|---|
| 1 | Spy fold creation | Randomly sample KP samples into U set as "spies" (repeated cross-validation) |
| 2 | PU Bagging | Train classifier on remaining P vs. expanded U; score spy class 1 probability |
| 3 | Score aggregation (EPR) | Proportion of KP classified above threshold |
| 4 | Score aggregation (MBS) | Mean class 1 probability across spy folds |
| 5 | Label permutation | Randomly shuffle P/U labels among all samples |
| 6 | Repeat steps 1-4 | Generate null distribution of scores under permuted labels |
| 7 | Statistical comparison | Z-score, Cliff's delta, (optional) t-test |

## 3. Scoring Methods Comparison

| Scoring Method | Abbreviation | Definition | Observed Behavior |
|---|---|---|---|
| Explicit Positive Recall | EPR | Fraction of spy KP samples with class 1 probability above threshold | Higher standard deviation in both actual and permuted label scores |
| Mean Bagging Score | MBS | Average class 1 probability of spy KP samples across folds | Lower standard deviation; improved sensitivity to actual vs. permuted differences |

Fig 3: EPR (left panels) and MBS (right panels) compared across synthetic datasets with varying class separation and TN proportion. MBS generally shows tighter distributions and better separation between actual and permuted scores.

## 4. Synthetic Dataset Results -- Score Distributions

### 4.1 Actual Label Scores (30-time repetition)

| Class Separation | TN% | EPR Mean (approx.) | EPR SD (approx.) | MBS Mean (approx.) | MBS SD (approx.) |
|---|---|---|---|---|---|
| High (dist=2) | 10% | High | Moderate | High | Low |
| High (dist=2) | 30% | High | Moderate | High | Low |
| High (dist=2) | 50% | High | Moderate | High | Low |
| Medium (dist=1) | 10% | Moderate-High | Moderate | Moderate-High | Low |
| Medium (dist=1) | 30% | Moderate | Moderate | Moderate | Low |
| Medium (dist=1) | 50% | Moderate | Moderate | Moderate | Low |
| None (dist=0) | 10% | Low | High | Low | Low-Moderate |
| None (dist=0) | 30% | Low | High | Low | Low-Moderate |
| None (dist=0) | 50% | Low | High | Low | Low-Moderate |

### 4.2 Permuted Label Scores

| Class Separation | TN% | EPR Permuted Mean | MBS Permuted Mean | Score Separation (Actual - Permuted) |
|---|---|---|---|---|
| High (dist=2) | 10-50% | Baseline-level | Baseline-level | Large |
| Medium (dist=1) | 10-50% | Baseline-level | Baseline-level | Moderate |
| None (dist=0) | 10-50% | Similar to actual | Similar to actual | Near zero (as expected) |

Fig 2B: Violin plots comparing PU Bagging score distributions between actual and permuted labels across synthetic datasets (30% TN shown) and WDBC. Clear separation visible for high and medium class separation; overlap for zero separation (negative control).

## 5. Statistical Comparison Methods

### 5.1 Z-Score vs. T-Test Stability

| Metric | Behavior with Increasing Permutations | Preferred? |
|---|---|---|
| Z-score p-value | Stable (remains approximately constant) | Yes |
| Two-sample t-test p-value | Can be arbitrarily deflated (inflated significance) | No |
| Cliff's delta | Stable effect size estimate | Yes (complementary) |

Fig 5: P-value from z-score remains stable regardless of the number of permutation replicates. Demonstrated on Lakhashe dataset and a dimension-matched synthetic dataset. First row: sample mean and SD of permuted score distribution. Second row: Cliff's delta with 95% CI. Third row: z-score p-value showing stability.

### 5.2 Statistical Framework

| Test | Input | Output | Use Case |
|---|---|---|---|
| One-sample z-score | Actual label score vs. permuted distribution (mean, SD) | p-value | Primary significance test |
| Cliff's delta | Actual scores vs. permuted scores | Effect size + 95% CI | Magnitude of difference |
| Two-sample t-test | Actual vs. permuted score groups | p-value | NOT recommended (inflated by permutation count) |

## 6. Real-World Dataset Results

### 6.1 WDBC Dataset

| TN Proportion | NKP (varied) | EPR Actual vs. Permuted | MBS Actual vs. Permuted | Statistical Significance |
|---|---|---|---|---|
| 50% | Multiple levels tested | Actual > Permuted | Actual > Permuted | Significant (high separation in WDBC) |
| 30% | Multiple levels tested | Actual > Permuted | Actual > Permuted | Significant |
| 10.8% | Multiple levels tested | Actual > Permuted | Actual > Permuted | Significant |

Fig 4 (top row): WDBC scores from actual (yellow) and permuted (orange) labels with EPR and MBS, showing clear separation across varied NKP values. Boxplots show median, mean, IQR, and error bars.

### 6.2 BRCA/LUAD RNA-Seq Dataset

| Setting | NKP (varied) | EPR Separation | MBS Separation | Significance |
|---|---|---|---|---|
| 325 PCs, 95% variance | Multiple levels tested | Clear separation | Clear separation | Significant |

Fig 4 (middle row): BRCA/LUAD dataset shows robust actual vs. permuted score separation for both EPR and MBS, confirming applicability to high-dimensional genomic data after PCA reduction.

### 6.3 Lakhashe Vaccine Immunology Dataset

| Setting | NKP (varied) | EPR Separation | MBS Separation | Significance |
|---|---|---|---|---|
| 36 Rhesus Macaques, 3 vaccine regimens | Multiple levels tested | Moderate separation | Moderate separation | Variable depending on NKP |

Fig 4 (bottom row): Lakhashe dataset results show the methodology works with small sample immunological data, though power is reduced with very few KP samples.

## 7. Impact of KP Proportion on Performance

| Factor | Effect on Model Confidence |
|---|---|
| Very low KP proportion | Reduced statistical power; harder to distinguish actual from permuted |
| Moderate KP proportion | Adequate power for most datasets |
| High KP proportion | Strong separation between actual and permuted distributions |
| Low class separation | Reduces confidence regardless of KP proportion |
| High dimensionality (p >> n) | Successfully handled after appropriate dimensionality reduction |

## 8. PCA Visualization of Datasets

| Dataset | First 3 PCs Show | Ground Truth Labels | PU Labels |
|---|---|---|---|
| Synthetic (high separation) | Clear cluster separation | Two distinct groups | P concentrated, U mixed |
| Synthetic (medium separation) | Partial overlap | Overlapping groups | P concentrated, U mixed |
| Synthetic (no separation) | Complete overlap | No visible structure | Random assignment appearance |
| WDBC | Moderate separation | Benign vs. malignant clusters | P concentrated, U mixed |

Fig 2A: PCA visualization (first 3 components) for ground truth and PU labels across synthetic data with 3 separation levels and WDBC dataset. Confirms experimental difficulty gradient.

## 9. Negative Control Results (Class Separation = 0)

| Metric | Actual Label | Permuted Label | Interpretation |
|---|---|---|---|
| EPR score | Low / near baseline | Low / near baseline | No information in labels |
| MBS score | Low / near baseline | Low / near baseline | No information in labels |
| Z-score p-value | Not significant | N/A | Correctly identifies no signal |
| Cliff's delta | Near zero | N/A | No meaningful effect |

These negative control results confirm that the methodology does not produce false positive confidence when there is genuinely no class structure in the data.

## 10. Key Methodological Considerations

| Consideration | Detail |
|---|---|
| Dimensionality reduction | PCA used for BRCA/LUAD to retain 95% variance (325 components from full RNA-seq feature space) |
| Cross-validation | Repeated cross-validated spy fold strategy |
| Repetition count | 30 repetitions for score distribution estimation |
| Permutation replicates | Varied (tested stability across different counts) |
| Classifier in PU Bagging | Algorithm insensitive to classifier choice (from prior work) |
| Feature composition | Synthetic data: 30% informative, 70% redundant (linear combinations of informative features) |

## 11. Comparison with Prior PU Learning Approaches

| Approach | Validation Strategy | Limitations |
|---|---|---|
| Standard PU Bagging | Uses ground truth for evaluation | Not available in real scenarios |
| Biased SVM | Single classifier | Underperforms PU Bagging, especially with small KP |
| This work (permutation PU) | No ground truth needed; uses null distribution | Requires sufficient KP and class separation for power |

## 12. Software and Implementation

| Component | Tool/Library |
|---|---|
| Synthetic data generation | scikit-learn (Python) |
| PCA dimensionality reduction | scikit-learn |
| PU Bagging implementation | Custom pipeline |
| Statistical testing | Z-score, Cliff's delta, t-test |
| Visualization | Violin plots, boxplots, PCA scatter plots |

## 13. Summary of Main Conclusions

| Conclusion | Evidence |
|---|---|
| Permutation testing provides a valid no-information-rate benchmark for PU learning | Negative controls show no false positives; positive cases show significant separation |
| Z-score is preferred over t-test for permutation comparison | Z-score p-value stable across permutation counts; t-test is inflated |
| MBS outperforms EPR as a scoring method | Lower variance, better sensitivity to actual vs. permuted differences |
| Methodology works across synthetic and real biological datasets | Validated on WDBC, BRCA/LUAD, vaccine immunology data |
| Low class separation and/or very few KP samples reduce confidence | Expected behavior; methodology correctly identifies unreliable models in these settings |

