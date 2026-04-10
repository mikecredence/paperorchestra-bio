# Experimental Log -- Gene Perturbation Prediction: Deep Learning vs Linear Baselines

## 2024-02-01 -- Model inventory

| Model type | Count | Examples |
|---|---|---|
| Foundation models | 5 | scGPT, Geneformer, scFoundation, etc. |
| Other deep learning models | 2 | Specialized perturbation predictors |
| Linear baselines | 3 | Additive model, mean predictor, linear (interventional) |
| Total models evaluated | 10 | -- |

## 2024-02-20 -- Task 1: Combinatorial perturbations (double knockdown from singles)

Training: single-gene perturbation profiles. Test: predict double-gene perturbation profiles.

| Model | Correlation (mean) | MSE (relative) | Beats additive baseline? |
|---|---|---|---|
| Foundation model 1 | ~0.85 | 1.0x | No |
| Foundation model 2 | ~0.84 | 1.05x | No |
| Foundation model 3 | ~0.83 | 1.1x | No |
| Foundation model 4 | ~0.82 | 1.1x | No |
| Foundation model 5 | ~0.80 | 1.2x | No |
| Deep learning model 1 | ~0.84 | 1.0x | No |
| Deep learning model 2 | ~0.83 | 1.05x | No |
| **Additive baseline** | **~0.86** | **1.0x (ref)** | **-- (reference)** |

No deep learning model outperforms the simple additive baseline on combinatorial perturbations.

## 2024-03-10 -- Task 2: Unseen gene perturbations (leave-one-out)

Training: all perturbations except target gene. Test: predict held-out gene perturbation.

| Model | Correlation (mean) | Beats mean-of-training baseline? |
|---|---|---|
| Foundation model 1 | ~0.60 | No |
| Foundation model 2 | ~0.58 | No |
| Foundation model 3 | ~0.55 | No |
| Deep learning model 1 | ~0.59 | No |
| Deep learning model 2 | ~0.57 | No |
| **Mean-of-training baseline** | **~0.62** | **-- (reference)** |

None of the deep learning methods outperform simply predicting the average perturbation effect.

## 2024-03-25 -- Linear model on interventional data

| Model | Correlation (combinatorial) | Correlation (unseen gene) |
|---|---|---|
| Linear (interventional data) | ~0.90 | ~0.68 |
| Best foundation model | ~0.85 | ~0.60 |
| Additive baseline | ~0.86 | N/A |
| Mean baseline | N/A | ~0.62 |

A simple linear model trained on interventional (perturbation) data reliably outperforms all deep learning models and other baselines.

## 2024-04-05 -- Analysis of why deep learning underperforms

| Factor | Evidence |
|---|---|
| Pre-training data is observational (not interventional) | Models learn correlational, not causal, gene relationships |
| Perturbation effects are sparse | Most genes change little; hard to beat mean prediction |
| Combinatorial effects are roughly additive | Simple additive model captures the dominant signal |

## Summary

Current deep learning and foundation models do not outperform trivially simple baselines for gene perturbation prediction. Observational pre-training data is a likely culprit. A linear model on interventional data is the best performer.
