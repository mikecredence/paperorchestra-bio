# Experimental Log: Leveraging Permutation Testing to Assess Confidence in Positive-Unlabeled Learning Applied to High-Dimensional Biological Datasets

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 1A), we score the class 1 probability of each “spy fold” with the PU Bagging algorithm (Fig.
- The class 1 probability of each positive sample when modeled as a “spy” is further aggregated by two different scoring methods and pooled under a repeated cross-validated spy fold strategy [10].
- 1B).biorxiv;2023.07.06.548028v1/FIG1F1fig1Figure 1:Graphical representation of the application of permutation and “spy” techniques in PU learning.A.
- Proposed by Liu et al [1], the spy method randomly samples a small percentage of the definitively labeled positive (P) class and mixes them into the unlabeled (U) set as “spies”.
- Here, we generated nine high dimensional (p≥n) synthetic datasets with different hypercube distances (high (class separation = 2), medium(class separation = 1), and a negative control (class separation = 0) and varied ground truth label class ratios (10%, 30%, 50% True Negative).
- 2A).biorxiv;2023.07.06.548028v1/FIG2F2fig2Figure 2:Permutation testing to evaluate model robustness across varying class separations and with extreme class imbalance.A.
- Data visualization (30% True Negative) using first three components from PCA, labeled by both ground truth class labels (left, black and red)) and P/U labels (right, purple and yellow) in the simulation settings for synthetic data with 3 different degrees of class separation (top) and Wisconsin Diag
- Violin plots comparing the Positive Set score under actual and permuted P/U labels for varying portions (50-10%, left to right) of True Negatives among the U set.
- Area under the curve for classification of unlabeled samples (U-AUC) is reported in below each test condition.We calculated area under the receiver operator characteristic curve (ROC-AUC) between the modeled class 1 probability for known positive examples and the ground truth label for the unlabeled
- As expected, the unlabeled set AUC (U-AUC) values varied from excellent (1.00) to close to random (0.64) in association with class separation when a high proportion of true negative samples were included in the unlabeled set.
- When the proportion of true negative samples within the unlabeled set was decreased to 10%, the U-AUC values for each condition showed a consistent reduction and exhibited the expected variation based on the level of class separation, ranging from 0.88 (excellent) to 0.54 (low to no discrimination) 
- To thoroughly evaluate the performance the samples labeled as positive, both Explicit Positive Recall (EPR) and Mean Bagging Scores (MBS) were calculated [7].
- When classes were well separated (class separation = 2), distributions for actual and permuted positive samples were distinct based on tail probabilities (not shown), by Welch’s t test, Cliff’s delta estimate, which is a measure of effect size, and p-value from z-score (Fig.
- Even with moderate class separation (class-separation = 1), a low proportion (10%) of true negatives yielded EPR and MBS values for actual positives that were not significantly different than those observed when labels were permuted (Fig.
- Importantly, when positive and negative classes were not distinct (class separation = 0), statistically significant differences between actual and permuted EPR or MBS were generally not observed.
- To this end, EPR appeared somewhat less susceptible to false positive observations, suggesting that this approach is a reliable means to evaluate the level of confidence in modeling results in the absence of any true negative examples.biorxiv;2023.07.06.548028v1/FIG3F3fig3Figure 3.Statistical method
- Mean and standard deviation of the scores in actual group obtained from 30-time repetition.
- Error bars represented the 95% confidence interval of the estimate.
- Dashed line indicates p-value = 0.05.
- 2C), we observed confident differences between actual known positive and permuted positive samples for all proportions of true negatives (Fig.
- In this dataset, even when EPR and MBS scores approached 0.5, the U-AUC values consistently surpassed 0.9.
- In this extension, we also varied the percentage of randomly selected known positive samples ranging from as few as 10% to as many as 40% (Fig.
- study datasets.biorxiv;2023.07.06.548028v1/FIG4F4fig4Figure 4:Statistical methods to evaluate scores between actual and permuted label group in real world biological datasets.A.
- Statistical significance between actual and permuted scores was defined by Welch T test (****: p value < 0.0001).
- AUC of U set samples calculated between class 1 probability using PU bagging SVM compared and ground truth label.
- 4A-B), and actual known positive subject EPR and MBS values were statistically significantly different than observed for permuted positive subjects, regardless of the number of known positives (Fig.
- 4A), though the distributions remained quite distinct (Fig.
- 4A, C) and a large effect size was observed (Fig.
- Concordantly, high U-AUC values, significant p-value from z-score, and large effect sizes (Cliff’s delta) provided further evidence that comparisons between actual and permuted positive class samples can provide confidence to model results in the absence of underlying ground truth label for validati
- We evaluated three different levels of permutation repetitions (30, 100, 500) and four different numbers of known positive examples to interrogate the changes in statistical significance between scores from actual labels and permuted labels (Fig.
- Compared to scores using the MBS value, a larger 95% confidence interval of Cliff’s Delta was observed under a lower number of permutations; however, the group difference level remained stable over the boundary of “large” (Cliff’s Delta estimate > 0.474), and a substantial change in p-value was not 
- Second row: Cliff’s delta estimates with a 95% confidence interval.
- Dashed line: p-value = 0.05.In contrast to this case, in which a significant difference was obtained between scores under the actual label and permuted labels with all methods, we also investigated estimates from statistical comparison methods in a dataset where only moderate to low statistical sign
- For this analysis, we generated a high dimensional synthetic dataset with a similar number of instances and attributes, but only a moderate level of hypercube distance (n:100, p:200, (%) TN:30) and poor to acceptable discrimination achieved in AUC of the unlabeled set based on the randomly selected 
- With a 95% confidence interval of falling into the range from “negligible” to “medium” Cliff’s Delta, varying the number of permutations from low to high did not positively or negatively impact the estimate from this non-parametric test (Fig.

## Tables

### Table 1.
> Description of the datasets and positive-unlabeled settings evaluated.


## Figure Descriptions

### Figure 1:
Graphical representation of the application of permutation and “spy” techniques in PU learning.A. Proposed by Liu et al [1], the spy method randomly samples a small percentage of the definitively labeled positive (P) class and mixes them into the unlabeled (U) set as “spies”. A classifier is then tr

### Figure 2:
Permutation testing to evaluate model robustness across varying class separations and with extreme class imbalance.A. Data visualization (30% True Negative) using first three components from PCA, labeled by both ground truth class labels (left, black and red)) and P/U labels (right, purple and yello

### Figure 3.
Statistical methods to evaluate scores between actual and permuted label group in the PU simulations from synthetic datasets.Explicit Positive Recall (EPR, left) and Mean Bagging Scores (MBS, right) for varying classification difficulties. Lines are colored according to class separation distance bet

### Figure 4:
Statistical methods to evaluate scores between actual and permuted label group in real world biological datasets.A. Scores obtained from actual (yellow) and permuted (orange) P/U labels with two different scoring methods (EPR, left and MBS, right) under varied numbers of KP (NKP) samples for WDBC (t

### Figure 5:
P value from the z-score remains stable regardless of the number of permutations.Statistical comparisons between scores from actual and permuted labels in Lakhashe et al. dataset and a dimension-matched synthetic dataset with varied numbers of permutation repetitions. First row: sample mean and stan

## References
Total references in published paper: 12

### Key References (from published paper)
- Permutation tests for studying classifier performance (, 2010)
- Positive-unlabeled learning in bioinformatics and computational biology: a brief review (, 2022)
- A bagging SVM to learn from positive and unlabeled examples (, 2014)
- Genome-wide sequence-based prediction of peripheral proteins using a novel semi-supervised learning  (, 2010)
- Computationally predicting protein-RNA interactions using only positive and unlabeled examples (, 2015)
- Learning from positive and unlabeled data: a survey (, 2020)
- Scikit-learn: Machine Learning in Python (, 2011)
- The cancer genome atlas pancancer analysis project (, 2013)
- Cooperation Between Systemic and Mucosal Antibodies Induced by Virosomal Vaccines Targeting HIV-1 En (, 2022)
- Array programming with NumPy (, 2020)
- Building text classifiers using positive and unlabeled examples (, 2003. IEEE)
- Package ‘ggpubr’ (, 2020)

## Ground Truth Reference
- Figures: 5
- Tables: 1
- References: 12