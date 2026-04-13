Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

## Working title

Hippocampal and striatal volume contributions to the longitudinal development of feedback-timing-dependent reinforcement learning in 6-to-7-year-old children

## Core question

Do hippocampal and striatal structural volumes differentially contribute to the development of value-based reinforcement learning over a 2-year period in middle childhood, and does feedback timing (immediate vs. delayed) modulate these brain-cognition associations as predicted by the adult memory systems literature?

## Motivation / gap

- Adult studies show that feedback timing modulates engagement of hippocampal (delayed feedback) vs. striatal (immediate feedback) memory systems during reinforcement learning, but whether similar dissociations exist in developing children is unknown
- Longitudinal developmental trajectories of reinforcement learning in middle childhood (ages 6-10) have not been examined with computational models that decompose learning rate and value-guided decision-making (inverse temperature)
- The hippocampus and striatum have different maturational timelines, yet how their structural volumes relate to RL parameter changes over time in children has not been tested
- Cross-sectional developmental studies have described age-related increases in learning accuracy and win-stay behavior, but longitudinal evidence including lose-shift behavior and computational parameters is lacking
- Whether the hippocampal and striatal memory systems operate cooperatively or competitively during value-based learning in childhood (as opposed to the more differentiated pattern in adults) is an open question

## Core contribution (bullet form)

- Two-year longitudinal study of 142 children (wave 1 age: mean 7.19, SD 0.46) showing improved reinforcement learning: increased accuracy (beta_wave2 = 0.550, p < 0.001), increased win-stay (beta = 0.586, p < 0.001), decreased lose-shift (beta = -0.252, p < 0.001), and faster reaction times (beta = -221 ms, p < 0.001)
- Feedback timing modulated reaction time (delayed feedback was faster, beta = -13.8, p = 0.038) and the inverse temperature parameter (value-guided decision-making), but not accuracy or win-stay/lose-shift
- Computational modeling identified longitudinal increases in both learning rate and inverse temperature toward more optimal parameter combinations, with children's learning rates (0.02-0.05) still far from adult optima (~0.29)
- Hippocampal volume showed more protracted maturation than striatal volume across the 2-year period
- Larger hippocampal volume was associated with better delayed model-derived learning longitudinally, consistent with adult findings
- Unexpectedly, larger striatal volume was associated with both immediate AND delayed learning, suggesting a less differentiated, more cooperative role for the striatum in middle childhood

## Method in brief

Children (n=142 at wave 1, n=127 at wave 2; 46% female) completed an adapted probabilistic reinforcement learning task with four cue-choice pairs (87.5% contingent reward probability) across immediate and delayed feedback conditions. In the immediate condition, feedback followed the choice after 1 second; in the delayed condition, a 6-second delay with an incidentally presented object was interposed before feedback. Behavioral measures included accuracy, win-stay probability, lose-shift probability, and reaction time, analyzed with generalized linear mixed models (GLMMs). Computational modeling compared multiple value-based models using Bayesian model comparison (Pseudo-BMA+ with Bayesian bootstrap, 100,000 iterations), with the winning model estimating learning rate (alpha) and inverse temperature (tau) parameters, where tau was allowed to differ by feedback timing condition.

A subgroup underwent structural MRI at both waves (73 children with longitudinal MRI data; 82 usable scans at wave 1, 99 at wave 2 after motion exclusion). Hippocampal and striatal volumes were extracted from T1-weighted scans. Brain-cognition associations were modeled using four-variate latent change score (LCS) models that simultaneously captured longitudinal change in striatal volume, hippocampal volume, immediate learning score, and delayed learning score (model-derived choice probabilities from fitted posterior parameters). This framework allowed testing whether brain volume changes predicted learning changes and whether these associations differed by feedback timing condition. Parameter and model recovery analyses confirmed the reliability of the computational modeling approach.

## Target venue

eLife


## Experimental Log

# Experimental Log: Longitudinal Development of Value-Based Learning in Middle Childhood

## 1. Participant Characteristics

### 1.1 Sample Overview

| Parameter | Wave 1 | Wave 2 |
|---|---|---|
| Total enrolled | 142 | 127 |
| Included in RL analysis | 140 | 126 |
| Excluded from RL | 2 (1 incomplete task, 1 technical issue) | 1 |
| Sex (% female) | 46% | 46% |
| Age mean (years) | 7.19 | 9.25 |
| Age SD (years) | 0.46 | 0.45 |
| Age range (years) | 6.07-7.98 | 8.30-10.20 |
| Inter-wave interval mean (years) | -- | 2.07 |
| Inter-wave interval SD (years) | -- | 0.17 |
| Inter-wave interval range (years) | -- | 1.69-2.68 |

### 1.2 MRI Subsample

| Parameter | Wave 1 | Wave 2 |
|---|---|---|
| Scanned | 90 | 104 |
| Sex (% female) | 49% | 45% |
| Handedness (% right) | 100% | 92% |
| Usable structural scans | 82 | 99 |
| Excluded (excessive motion) | 8 | 5 |
| Longitudinal MRI data (both waves) | 73 | 73 |
| Longitudinal learning data (both waves) | 126 | 126 |

### 1.3 Poor Learners (< 50% accuracy in last 20 trials)

| Wave | N Poor Learners | Total N | Percentage |
|---|---|---|---|
| Wave 1 | 13 | 140 | 9.3% |
| Wave 2 | 6 | 126 | 4.8% |

Analyses were also run with a reduced dataset excluding poor learners; results remained unchanged (Appendix 6).

## 2. Reinforcement Learning Task Design

| Parameter | Detail |
|---|---|
| Number of cues | 4 (cartoon characters) |
| Number of choices per cue | 2 (round-shaped or square-shaped lolli) |
| Reward contingency | 87.5% contingent, 12.5% non-contingent |
| Feedback timing conditions | Immediate (1 s delay) and Delayed (6 s delay) |
| Cues per condition | 2 immediate, 2 delayed |
| Inter-trial interval | 0.5 s |
| Choice window | Up to 7 s |
| Delayed condition insert | Incidentally presented object (for episodic memory test) |
| Compensation | 8 EUR per hour |
| Session duration | 150-180 minutes |
| MRI timing | Within 3 weeks of behavioral session |

## 3. Behavioral Results -- Descriptive Statistics

### 3.1 Accuracy (Probability Correct)

| Wave | Feedback | Mean ACC (approx.) | Direction of Change |
|---|---|---|---|
| 1 | Immediate | Lower | -- |
| 1 | Delayed | Lower | -- |
| 2 | Immediate | Higher | Increased |
| 2 | Delayed | Higher | Increased |

### 3.2 Win-Stay Probability

| Wave | Feedback | Mean WS (approx.) | Direction of Change |
|---|---|---|---|
| 1 | Immediate | Lower | -- |
| 1 | Delayed | Lower | -- |
| 2 | Immediate | Higher | Increased |
| 2 | Delayed | Higher | Increased |

### 3.3 Lose-Shift Probability

| Wave | Feedback | Mean LS (approx.) | Direction of Change |
|---|---|---|---|
| 1 | Immediate | Higher | -- |
| 1 | Delayed | Higher | -- |
| 2 | Immediate | Lower | Decreased |
| 2 | Delayed | Lower | Decreased |

### 3.4 Reaction Time (seconds)

| Wave | Feedback | Mean RT (approx.) | Direction of Change |
|---|---|---|---|
| 1 | Immediate | Slower | -- |
| 1 | Delayed | Slower (but faster than immediate) | -- |
| 2 | Immediate | Faster | Decreased |
| 2 | Delayed | Faster | Decreased |

## 4. GLMM Fixed Effects -- Behavioral Variables

| DV | Predictor | Beta | SE | Test Statistic | p-value |
|---|---|---|---|---|---|
| Accuracy | Wave 2 | 0.550 | 0.061 | z = 8.97 | < 0.001 |
| Accuracy | Delayed feedback | 0.013 | 0.024 | z = 0.54 | 0.590 |
| Win-Stay | Wave 2 | 0.586 | 0.071 | z = 8.22 | < 0.001 |
| Win-Stay | Delayed feedback | 0.023 | 0.033 | z = 0.69 | 0.489 |
| Lose-Shift | Wave 2 | -0.252 | 0.037 | z = -6.87 | < 0.001 |
| Lose-Shift | Delayed feedback | 0.030 | 0.022 | z = 1.37 | 0.169 |
| RT | Wave 2 | -221 | 22.8 | t(135) = -9.70 | < 0.001 |
| RT | Delayed feedback | -13.8 | 6.59 | t(136) = -2.10 | 0.038 |

Fig 2A: Accuracy increased between waves with no feedback timing difference.
Fig 2B: Win-stay increased and lose-shift decreased between waves; no feedback timing effect.
Fig 2C: RT was faster at wave 2 and faster for delayed vs. immediate feedback.
Fig 2D: Correlation matrix showing accuracy was primarily correlated with win-stay and lose-shift (within and between waves) but not with RT. Significant correlations circled; Bonferroni-corrected p-values.

## 5. Computational Modeling Results

### 5.1 Model Comparison

| Model | Description | Comparison Outcome |
|---|---|---|
| vbm1 | Basic RL (single alpha, single tau) | Not best |
| vbm2 | Separate alpha by feedback condition | Not best |
| vbm3 (winning) | Separate tau by feedback condition, shared alpha | Best fit |
| Additional models | Various combinations | Inferior to vbm3 |

Model comparison used Pseudo-BMA+ with Bayesian bootstrap (100,000 iterations) at group level and elpd_100 (summed expected log pointwise predictive density) at individual level.

### 5.2 Winning Model Parameters (vbm3)

| Parameter | Description | Wave 1 Mean (approx.) | Wave 2 Mean (approx.) | Change Direction |
|---|---|---|---|---|
| Alpha (learning rate) | How quickly values are updated | 0.02 | 0.05 | Increased |
| Tau_immediate | Inverse temperature for immediate feedback | Lower | Higher | Increased |
| Tau_delayed | Inverse temperature for delayed feedback | Lower | Higher | Increased |

Children's learning rates (0.02-0.05) are far below adult averages (0.12-0.34) and simulated optimal (~0.29).

### 5.3 Feedback Timing Effect on Parameters

| Parameter | Feedback Timing Effect | Detail |
|---|---|---|
| Alpha (learning rate) | No significant difference by feedback timing | Shared across conditions in winning model |
| Tau (inverse temperature) | Separated by feedback timing in winning model | tau_delayed vs. tau_immediate differs |
| Condition difference in tau | Individual variability present | Average difference not large, but individual differences substantial |

Fig 3A (top): Learning rate and inverse temperature both increased between waves. Inverse temperature but not learning rate was separated by feedback timing.
Fig 3A (bottom left): Condition difference in inverse temperature showed individual variability.
Fig 3B: Higher condition difference in inverse temperature correlated with faster RT for delayed vs. immediate feedback.

### 5.4 Simulation-Based Optimal Parameters

| Parameter | Optimal Value | Optimal Learning Score |
|---|---|---|
| Alpha (learning rate) | ~0.29 | 96.5% accuracy |
| Tau (inverse temperature) | Corresponding optimal | 96.5% accuracy |

Fig 4A: Parameter landscape showing simulation-based average learning scores. Cyan "X" marks the optimal parameter combination (96.5% accuracy). Cyan rectangle shows the space of fitted parameter combinations from children.
Fig 4B: Enlarged view of fitted parameter space showing mean and individual change vectors (arrows) from wave 1 to wave 2. Change direction is toward higher (more optimal) learning scores.

### 5.5 Parameter Recovery

| Parameter | Recovery Quality (Pearson r) |
|---|---|
| Alpha | Good correlation between simulated and recovered |
| Tau_immediate | Good correlation |
| Tau_delayed | Good correlation |

Appendix 1, Fig 1: Parameter recovery of winning model showing identity line and loess regression.

### 5.6 Model Recovery

| Level | Method | Result |
|---|---|---|
| Group-level | Pseudo-BMA+ (20 groups x 50 datasets, 100,000 bootstrap iterations) | vbm3 correctly identified |
| Individual-level | elpd_100 (1,000 datasets) | vbm3 correctly identified |

Appendix 1, Fig 2: Model recovery matrices at group and individual level.

## 6. Episodic Memory Results

| Measure | Delayed Feedback | Immediate Feedback | Comparison |
|---|---|---|---|
| Corrected recognition (hits - false alarms) | Slightly higher (trend only) | Baseline | Enhanced at trend level, not significant |

Fig 5A: Recognition memory for objects presented during delayed feedback was only enhanced at trend, contrary to the hypothesis based on adult literature.

## 7. Brain Volume Results

### 7.1 Longitudinal Volume Changes

| Brain Region | Wave 1 Volume | Wave 2 Volume | Change Direction | Change Magnitude (relative) |
|---|---|---|---|---|
| Hippocampus | Smaller | Larger | Increased | Larger increase |
| Striatum | Smaller | Larger | Increased | Smaller increase |

Fig 5C: Both hippocampal and striatal volumes increased between waves, with hippocampal volume showing more protracted (larger) maturation.

### 7.2 Brain Volume Comparison

| Comparison | Finding | Interpretation |
|---|---|---|
| Hippocampal vs. striatal volume change | Hippocampal change > striatal change | More protracted hippocampal maturation |
| Within-wave correlations | Volume-learning associations present | Brain-cognition links exist |
| Between-wave stability | Associations stable longitudinally | Consistent developmental pattern |

## 8. Latent Change Score (LCS) Model Results

### 8.1 Four-Variate LCS Model Structure

| Variable | Domain | Waves |
|---|---|---|
| Striatal volume | Brain | 1, 2 |
| Hippocampal volume | Brain | 1, 2 |
| Immediate learning score | Cognition | 1, 2 |
| Delayed learning score | Cognition | 1, 2 |

Fig 5D: Path diagram of the four-variate LCS model showing brain-cognition associations.

### 8.2 Key Brain-Cognition Associations

| Predictor (Volume) | Outcome (Learning) | Association | Consistent with Hypothesis? |
|---|---|---|---|
| Hippocampal volume | Delayed learning | Positive (larger volume = better delayed learning) | Yes -- matches adult literature |
| Hippocampal volume | Immediate learning | Weaker / not significant | Partially -- expected stronger dissociation |
| Striatal volume | Immediate learning | Positive (larger volume = better learning) | Yes |
| Striatal volume | Delayed learning | Positive (larger volume = better learning) | No -- expected dissociation |

### 8.3 Interpretation of Brain-Cognition Patterns

| Pattern | Adult Literature | Children (This Study) |
|---|---|---|
| Hippocampus-delayed feedback link | Strong | Present (consistent) |
| Striatum-immediate feedback link | Strong and specific | Present but NOT specific (also linked to delayed) |
| Memory system differentiation | High (competitive/specialized) | Low (cooperative, less differentiated) |

## 9. Univariate LCS Models (Appendix 5)

| Variable | Model Fit | Slope Mean | Slope Variance | Intercept-Slope Correlation |
|---|---|---|---|---|
| Immediate learning score | Reported | Positive (improvement) | Individual differences | Reported |
| Delayed learning score | Reported | Positive (improvement) | Individual differences | Reported |
| Striatal volume | Reported | Positive (growth) | Individual differences | Reported |
| Hippocampal volume | Reported | Positive (growth, larger) | Individual differences | Reported |

## 10. Sex Differences

| Variable | Finding | Notes |
|---|---|---|
| Learning performance | Lower in girls vs. boys | Possible sex difference in RL during middle childhood |
| Switching behavior | Less optimal in girls | Could reflect confounding variables |
| Prior literature | Mixed findings depending on age and task type | Both male and female advantages reported |

Appendix 2: Detailed fixed effects including age and sex predictors.

## 11. Reduced Dataset Sensitivity Analysis (Appendix 6)

| Analysis | Complete Dataset | Reduced Dataset (excluding poor learners) | Conclusion |
|---|---|---|---|
| GLMM behavioral effects | Significant wave effects | Unchanged | Robust |
| Model comparison | vbm3 wins | Unchanged | Robust |
| Overall pattern | Consistent | Consistent | Poor learners do not drive results |

## 12. Correlation Structure (Fig 2D, Appendix 3)

| Variable Pair | Within-Wave Correlation | Between-Wave Correlation |
|---|---|---|
| Accuracy - Win-Stay | Significant positive | Significant positive |
| Accuracy - Lose-Shift | Significant negative | Significant negative |
| Accuracy - RT | Not significant | Not significant |
| Win-Stay - Lose-Shift | Significant negative | Significant negative |
| Alpha - Tau | Reported in Appendix 3 | Reported |

Appendix 3, Fig 1: Full parameter correlation matrix of winning model with Bonferroni-corrected significance.

## 13. Simulated Learning Landscape (Fig 4)

| Region of Parameter Space | Average Learning Score | Characterization |
|---|---|---|
| Optimal (alpha ~0.29, tau optimal) | 96.5% | Adult-like performance |
| Children wave 1 (alpha ~0.02, tau low) | Low | Suboptimal |
| Children wave 2 (alpha ~0.05, tau higher) | Moderate improvement | Moving toward optimum |
| Low alpha, any tau | Poor | Insufficient learning rate |
| High alpha, low tau | Moderate | Fast updating but noisy decisions |

## 14. Empirical Win-Stay / Lose-Shift Trajectory (Appendix 4)

| Metric | Wave 1 | Wave 2 | Change Direction |
|---|---|---|---|
| Win-stay proportion | Lower | Higher | Toward optimum |
| Lose-shift proportion | Higher | Lower | Toward optimum |
| Combined learning score | Lower | Higher | Improvement |

Appendix 4, Fig 1: Individual and mean change arrows plotted on simulated learning score landscape. Mean change (white arrow) moves toward higher learning scores; individual trajectories (black arrows) show variability.

## 15. Study Design and Procedures

| Session | Content | Timing |
|---|---|---|
| Wave 1 Session 1 | RL task + other cognitive tasks | Weekday 2-6pm or weekend |
| Wave 1 Session 2 | Additional cognitive tasks | Within days |
| Wave 1 MRI | Structural T1-weighted scan | Within 3 weeks of behavioral |
| Wave 2 Session 1 | RL task + cognitive tasks + MRI | ~2 years later |
| Consent | Written parental consent + child verbal assent | Both waves |

## 16. Key Statistical Methods

| Method | Application |
|---|---|
| GLMM (logistic) | Accuracy, win-stay, lose-shift |
| LMM | Reaction time (Satterthwaite df) |
| Bayesian model comparison (Pseudo-BMA+) | RL model selection |
| Individual model fits (elpd_100) | Individual-level model selection |
| Latent Change Score models (4-variate) | Brain-cognition longitudinal associations |
| Univariate LCS models | Individual variable trajectories |
| Bonferroni correction | Multiple comparison adjustment for correlations |
| Parameter recovery | Simulated-and-recovered validation |
| Model recovery | Group and individual level |

