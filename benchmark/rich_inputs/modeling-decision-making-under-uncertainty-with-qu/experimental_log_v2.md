# Experimental Log: Decision-Making Under Uncertainty with Qualitative Outcomes

## 1. Participant Demographics

### 1.1 In-Person Sample (Study 1)

| Parameter | Value |
|---|---|
| Screened | 101 adults |
| Did not complete study | 10 (4 task failure, 6 did not return) |
| Completed | 91 |
| Excluded (MoCA < 26) | 25 |
| Final analyzed sample | 66 (reported in Table 1); 71 cognitively healthy before further exclusion |
| Sex (female) | 32 of 71 cognitively healthy |
| Age range | 18-88 years |
| Age mean | 49.68 |
| Age SD | 22.3 |
| Cognitive screen | Montreal Cognitive Assessment (MoCA) |
| MoCA cutoff | >= 26 |

### 1.2 Online Sample (Study 2)

| Parameter | Value |
|---|---|
| Analyzed sample | 332 participants |
| Purpose | Independent replication |
| Task | Same decision-making task (online version) |

### 1.3 Combined Demographics (Table 1)

| Characteristic | In-Person Sample | Online Sample |
|---|---|---|
| N analyzed | 66 | 332 |
| Age range | 18-89 | Reported in Table 1 |
| Sex distribution | ~45% female | Reported in Table 1 |
| Screening | MoCA >= 26 | Online attention checks |

## 2. Task Design -- Monetary Domain

### 2.1 Risky Monetary Decisions

| Parameter | Values |
|---|---|
| Certain option | $5 |
| Lottery amounts | $5, $8, $12, $25 |
| Risk levels (known probability) | 25%, 50%, 75% |
| Visual representation | Bags with red/blue chips; percentage shown as colored rectangle |
| Repetitions per combination | 4 |
| Total risky monetary trials | 4 amounts x 3 risk levels x 4 reps = 48 |

### 2.2 Ambiguous Monetary Decisions

| Parameter | Values |
|---|---|
| Certain option | $5 |
| Lottery amounts | $5, $8, $12, $25 |
| Ambiguity levels (occlusion %) | 24%, 50%, 74% |
| Visual representation | Bags with occluder hiding portion of chip distribution |
| Repetitions per combination | 4 |
| Total ambiguous monetary trials | 4 amounts x 3 ambiguity levels x 4 reps = 48 |

### 2.3 Catch Trials

| Detail | Value |
|---|---|
| Number of catch trials | 12 (out of 84 total monetary) |
| Purpose | Attention verification |

## 3. Task Design -- Medical Domain

### 3.1 Risky Medical Decisions

| Parameter | Values |
|---|---|
| Certain option | No change in condition |
| Lottery outcomes | Slight improvement, moderate improvement, major improvement, complete recovery |
| Risk levels | 25%, 50%, 75% |
| Visual representation | Same chip-bag format with medical outcome labels |
| Repetitions per combination | 4 |

### 3.2 Ambiguous Medical Decisions

| Parameter | Values |
|---|---|
| Certain option | No change in condition |
| Lottery outcomes | Slight improvement, moderate improvement, significant improvement, complete recovery |
| Ambiguity levels | 24%, 50%, 74% |
| Repetitions per combination | 4 |

## 4. Computational Models Compared

### 4.1 Model Specifications

| Model | Equation | Value Estimation | Domain Applied | Key Feature |
|---|---|---|---|---|
| Estimated Value | Eq. 4 | Free parameters for each outcome level | Medical + Monetary | Extracts subjective values without objective amounts |
| No-Subjective Parameters | Eq. 5 | Raw category distances / fixed | Medical + Monetary | Baseline without value estimation |
| Classical Utility | Eq. 1 | Power-law transformation of objective amount | Monetary only | Standard approach with known dollar values |
| Hybrid models | Various | Combinations of above | Monetary | Alternative specifications |

### 4.2 Model Comparison Results (Table 2)

| Comparison | Domain | Winning Model | Comparison Metric |
|---|---|---|---|
| Estimated Value vs. No-Subjective Parameters | Medical (in-person) | Estimated Value | Superior fit |
| Estimated Value vs. No-Subjective Parameters | Medical (online) | Estimated Value | Superior fit |
| Estimated Value vs. Classical Utility | Monetary (in-person) | Estimated Value | Superior fit |
| Estimated Value vs. Classical Utility | Monetary (online) | Estimated Value | Superior fit |
| Estimated Value vs. No-Subjective Parameters | Monetary (in-person) | Estimated Value | Superior fit |
| Estimated Value vs. Hybrid models | Monetary | Estimated Value | Superior or equivalent |

Key finding: The Estimated Value model outperformed the Classical Utility model even in the monetary domain where objective dollar amounts are available. This indicates that subjective value estimation captures individual variation better than applying a standard power-law transformation to known quantities.

## 5. Extracted Subjective Values -- Medical Domain

### 5.1 In-Person Sample (Fig 2A)

| Medical Outcome Category | Mean Added Value | SD | Cumulative Value (approx.) |
|---|---|---|---|
| No change (certain) | 0 (reference) | -- | 0 |
| Slight improvement | 6.93 | 1.79 | 6.93 |
| Moderate improvement | +9.00 | 2.62 | 15.93 |
| Major improvement | +7.04 | 2.89 | 22.97 |
| Complete recovery | +4.18 | 2.41 | 27.15 |

### 5.2 Online Sample (Fig 2C)

| Medical Outcome Category | Mean Added Value | SD | Cumulative Value (approx.) |
|---|---|---|---|
| No change (certain) | 0 (reference) | -- | 0 |
| Slight improvement | 8.63 | 2.54 | 8.63 |
| Moderate improvement | +12.62 | 4.25 | 21.25 |
| Significant improvement | +4.66 | 2.56 | 25.91 |
| Complete recovery | +2.37 | 1.61 | 28.28 |

### 5.3 Cross-Sample Comparison of Medical Values

| Category | In-Person Mean | Online Mean | Pattern |
|---|---|---|---|
| Slight improvement | 6.93 | 8.63 | Online slightly higher |
| Moderate improvement increment | 9.00 | 12.62 | Online higher |
| Major/significant increment | 7.04 | 4.66 | In-person higher |
| Complete recovery increment | 4.18 | 2.37 | In-person higher |

The pattern of diminishing marginal value for the highest categories is consistent across samples, though the distribution of value across levels differs.

Fig 2A: In-person medical domain -- individual dots (colored) per participant with black mean dot per category. Values increase monotonically but with decreasing increments at the highest level.

Fig 2C: Online medical domain -- similar pattern of monotonic increase with diminishing returns at the top.

## 6. Extracted Subjective Values -- Monetary Domain

### 6.1 In-Person Sample (Fig 2B)

| Monetary Amount | Estimated Subjective Value (approx.) | Objective Value |
|---|---|---|
| $5 (reference/certain) | Reference | $5 |
| $8 | Estimated via model | $8 |
| $12 | Estimated via model | $12 |
| $25 | Estimated via model | $25 |

### 6.2 Online Sample (Fig 2D)

| Monetary Amount | Estimated Subjective Value (approx.) | Objective Value |
|---|---|---|
| $5 (reference/certain) | Reference | $5 |
| $8 | Estimated via model | $8 |
| $12 | Estimated via model | $12 |
| $25 | Estimated via model | $25 |

Fig 2B: In-person monetary domain -- estimated values track objective amounts but with individual variation captured by the model.
Fig 2D: Online monetary domain -- similar pattern.

## 7. Ambiguity Attitudes

### 7.1 Cross-Domain Association (Fig 3)

| Sample | Regression | Slope Direction | 89% HDPi | Interpretation |
|---|---|---|---|---|
| In-person (Fig 3A) | Medical beta vs. monetary beta | Positive | Does not cross zero | Consistent ambiguity attitudes across domains |
| Online (Fig 3B) | Medical beta vs. monetary beta | Positive | Does not cross zero | Replicated cross-domain consistency |

Fig 3A: Scatter plot of ambiguity aversion (beta) in monetary (x-axis) vs. medical (y-axis) domains for in-person sample. Positive slope with 89% HDPi shown.
Fig 3B: Same for online sample, replicating the positive association.

### 7.2 Risk vs. Ambiguity Attitude Properties

| Property | Detail |
|---|---|
| Risk attitudes in Estimated Value model | Integrated into estimated values (not separately quantified) |
| Ambiguity attitudes (beta) | Separately estimated per domain |
| Cross-domain comparability | Ambiguity attitudes can be compared across domains because they measure within-domain modulation |
| Risk attitude cross-domain comparison | Not directly possible without equating outcomes across domains |

## 8. Model Estimation Approach

| Component | Method |
|---|---|
| Estimation framework | Hierarchical Bayesian modeling |
| Value parameters | Individualized (participant-level) within hierarchical structure |
| Risk parameters | Embedded in value estimates (Eq. 4) |
| Ambiguity parameter (beta) | Separate per domain |
| Posterior intervals | 89% highest density posterior interval (HDPi) |
| Cross-domain regression | Robust regression |
| Model comparison | Information criteria (reported in Table 2) |

## 9. Experimental Procedures

### 9.1 In-Person Study Timeline

| Session | Content | Duration |
|---|---|---|
| Session 1 | Decision-making task + reversal RL task (not reported) | Standard |
| Session 2 | fMRI task | Standard |
| Session 3 | MoCA + cognitive questionnaires + general IQ | Standard |
| Payment | Per-session + completion bonus | -- |

### 9.2 Screening and Exclusion Pipeline

| Stage | N | Reason for Exclusion |
|---|---|---|
| Initial screening | 101 | Phone screen for major medical/psychiatric conditions |
| Failed to complete | 10 | 4 task failure, 6 no-show |
| Completed | 91 | -- |
| MoCA < 26 excluded | 20 | Cognitive impairment screen |
| Final cognitively healthy | 71 | 32 females; age 18-88 |
| Further task-level exclusions | 5 | To reach n=66 for analysis |

## 10. Key Design Choices

| Design Choice | Rationale |
|---|---|
| Qualitative medical outcomes (not quantified) | Preserve natural qualitative framing of health decisions |
| Same risk/ambiguity structure across domains | Enable cross-domain comparison |
| Hierarchical Bayesian estimation | Capture individual differences while borrowing strength across group |
| MoCA screening (in-person) | Ensure cognitive competence for complex decision task |
| Independent online replication | Address generalizability and sample size concerns |
| Catch trials (12/84 monetary) | Verify task engagement |

## 11. Theoretical Framework

| Concept | Definition | Application |
|---|---|---|
| Risk | Known outcome probabilities | 25%, 50%, 75% probability levels |
| Ambiguity | Unknown/partially unknown probabilities | 24%, 50%, 74% occlusion levels |
| Subjective value | Individual's internal valuation of an outcome | Estimated as free parameters in the model |
| Ambiguity aversion (beta) | Tendency to prefer known over unknown probabilities | Compared across monetary and medical domains |
| Classical utility | Power-law transformation of objective value | Benchmark comparison model |

## 12. Replication Summary

| Finding | In-Person (n=66) | Online (n=332) | Replicated? |
|---|---|---|---|
| Estimated Value model fits medical data | Yes | Yes | Yes |
| Estimated Value outperforms utility in monetary | Yes | Yes | Yes |
| Monotonic increase in medical subjective values | Yes | Yes | Yes |
| Diminishing increments at highest medical level | Yes | Yes | Yes |
| Cross-domain ambiguity attitude association | Positive (89% HDPi) | Positive (89% HDPi) | Yes |
| Individual variability in estimated values | Substantial | Substantial | Yes |

## 13. Comparison with Prior Approaches

| Approach | Outcome Handling | Limitation Addressed by This Work |
|---|---|---|
| Standard monetary risk/ambiguity tasks | Objective dollar amounts | Cannot handle qualitative outcomes |
| Quantified medical outcomes (months of life) | Force quantification | Imposes metric assumptions |
| Fixed-distance categories | Equal spacing assumed | Ignores individual differences in value assignment |
| This work (Estimated Value model) | Free estimation per category per participant | No metric assumptions; captures individual heterogeneity |

## 14. Limitations and Notes

| Limitation | Detail |
|---|---|
| Risk attitudes not separately estimated | Embedded in value parameters in Estimated Value model |
| In-person sample age range | Very wide (18-89); potential age confounds |
| Medical scenario is hypothetical | Not based on actual patient conditions |
| Cross-domain comparison restricted to ambiguity | Risk comparison requires outcome equating |
| Online sample differences | Slightly different value distributions vs. in-person |

## 15. Software and Statistical Tools

| Tool | Purpose |
|---|---|
| Hierarchical Bayesian estimation | Model fitting |
| Robust regression | Cross-domain ambiguity attitude association |
| 89% HDPi | Posterior interval reporting |
| Model comparison metrics | WAIC / LOO-CV (reported in Table 2) |
| Task software | Computerized decision-making paradigm |
