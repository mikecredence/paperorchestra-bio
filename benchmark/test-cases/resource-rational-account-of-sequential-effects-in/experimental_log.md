# Experimental Log: Resource-Rational Sequential Effects

## Experiment 1: Model comparison on human prediction data

Fit different models to human behavioral data from stochastic prediction tasks.

| Model | Log-Likelihood | BIC | AIC | Parameters |
|---|---|---|---|---|
| Optimal Bayesian | -1842 | 3698 | 3690 | 3 |
| Nonstationarity (leaky integration) | -1605 | 3232 | 3218 | 4 |
| Resource-Rational: Precision Cost | -1588 | 3200 | 3184 | 4 |
| Resource-Rational: Predictive Power | -1592 | 3210 | 3192 | 4 |

Key finding: Resource-rational models fit as well or better than the nonstationarity model.

## Experiment 2: Sequential effect signatures

Proportion of responses matching classic sequential effect patterns.

| Effect Pattern | Human Data | Optimal Bayesian | Nonstationarity Model | Precision Cost Model | Predictive Power Model |
|---|---|---|---|---|---|
| Positive recency (short lag) | 0.62 | 0.50 | 0.60 | 0.61 | 0.59 |
| Negative recency (long lag) | 0.43 | 0.50 | 0.44 | 0.43 | 0.44 |
| Alternation bias (after repetitions) | 0.57 | 0.50 | 0.55 | 0.56 | 0.56 |
| Repetition bias (after alternations) | 0.54 | 0.50 | 0.53 | 0.54 | 0.53 |

## Experiment 3: Forgetting timescale (Precision Cost model)

| Effective Memory (trials) | Fitted lambda | MSE to Human Data |
|---|---|---|
| 2 | 0.50 | 0.042 |
| 5 | 0.82 | 0.018 |
| 8 | 0.88 | 0.015 |
| 12 | 0.92 | 0.021 |
| Infinite (Bayesian) | 1.00 | 0.058 |

Best fit: effective memory of ~8 trials with exponential forgetting (lambda ~ 0.88).

## Notes

- The resource-rational framework produces sequential effects without assuming the participant believes the environment is nonstationary.
- Exponential forgetting from precision costs is the simplest mechanism and fits well.
- The predictive power model captures similar patterns through a different mechanism (favoring informative beliefs).
- Both approaches are more parsimonious in interpretation than nonstationarity, as they derive from general cognitive constraints.
