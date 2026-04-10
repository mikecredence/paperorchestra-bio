# Experimental Log: AFProfile -- MSA Denoising for AlphaFold-Multimer

## Experiment 1: CASP15 difficult targets evaluation

Evaluated AFProfile on seven difficult targets from CASP15 where standard AlphaFold-multimer (AFM) struggled.

| Target   | AFM MMscore | AFProfile MMscore | Delta  |
|----------|-------------|-------------------|--------|
| T1173    | 0.49        | 1.00              | +0.51  |
| H1144    | 0.60        | 0.84              | +0.24  |
| T1123    | 0.55        | 0.77              | +0.22  |
| T1124    | 0.68        | 0.72              | +0.04  |
| T1170    | 0.71        | 0.78              | +0.07  |
| T1152    | 0.62        | 0.69              | +0.07  |
| T1187    | 0.80        | 0.82              | +0.02  |
| **Mean** | **0.63**    | **0.76**          | **+0.13** |

## Experiment 2: Large-scale benchmark on 487 difficult complexes

Applied AFProfile to 487 protein complexes where standard AFM predictions fail (MMscore < 0.75).

| Metric                           | AFM baseline | AFProfile |
|----------------------------------|-------------|-----------|
| Total complexes evaluated        | 487         | 487       |
| Success rate (MMscore > 0.75)    | 0%          | 33%       |
| Number of complexes improved     | --          | 161       |
| Mean MMscore                     | 0.48        | 0.59      |

## Experiment 3: MMscore-DockQ correlation

Validated that MMscore is a reliable optimization proxy for structural quality.

| Complex type | Spearman r (MMscore vs DockQ) |
|-------------|-------------------------------|
| Heteromers  | > 0.80                        |
| Homomers    | > 0.90                        |
| All         | > 0.85                        |

## Experiment 4: Comparison with sampling-based approach (AFsample)

| Method     | Avg MMscore (CASP15) | Approach                  | Relative cost |
|-----------|----------------------|---------------------------|--------------|
| AFM       | 0.63                 | Standard inference        | 1x           |
| AFProfile | 0.76                 | MSA gradient optimization | ~2-3x        |
| AFsample  | 0.97                 | Massive random sampling   | ~100x        |
