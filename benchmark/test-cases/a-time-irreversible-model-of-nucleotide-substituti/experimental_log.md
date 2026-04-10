# Experimental Log -- Time-irreversible substitution model for SARS-CoV-2

## 2024-01-20 -- Observed substitution counts in real SARS-CoV-2 data

Pairwise comparison of early Wuhan reference vs. sampled genomes (~29.9 kb).

| Substitution type | Observed count | Proportion (%) |
|-------------------|---------------|----------------|
| C -> U | 4812 | 42.3 |
| U -> C | 485 | 4.3 |
| A -> G | 1420 | 12.5 |
| G -> A | 1105 | 9.7 |
| A -> C | 312 | 2.7 |
| A -> U | 498 | 4.4 |
| G -> U | 620 | 5.5 |
| G -> C | 195 | 1.7 |
| U -> A | 410 | 3.6 |
| U -> G | 380 | 3.3 |
| C -> A | 520 | 4.6 |
| C -> G | 615 | 5.4 |

C->U dominates at ~42%, roughly 10x the reverse U->C rate. Traditional reversible models cannot capture this.

## 2024-02-08 -- Simulation study: estimation accuracy

Simulated 1000 replicates under the irreversible model (true C->U rate = 0.050 subs/site/year, other rates ~0.005).

| Parameter | True value | Mean estimate | Std dev | Bias |
|-----------|-----------|--------------|---------|------|
| r(C->U) | 0.0500 | 0.0498 | 0.0032 | -0.0002 |
| r(U->C) | 0.0050 | 0.0051 | 0.0018 | +0.0001 |
| r(A->G) | 0.0055 | 0.0054 | 0.0015 | -0.0001 |
| r(G->A) | 0.0045 | 0.0046 | 0.0014 | +0.0001 |

The new method recovers true parameters with low bias and reasonable variance.

## 2024-02-25 -- Comparison: reversible vs irreversible model fit

Fitted GTR (reversible) and new irreversible model to real SARS-CoV-2 alignment (n=500 genomes).

| Model | Log-likelihood | AIC | BIC | Parameters |
|-------|---------------|-----|-----|-----------|
| GTR (reversible) | -125430 | 250880 | 250950 | 10 |
| Irreversible model | -124210 | 248444 | 248550 | 12 |

Irreversible model provides substantially better fit (delta-AIC > 2000).

## 2024-03-10 -- Estimated substitution rates from real data

| Substitution | Rate (subs/site/year) | Ratio to mean |
|-------------|----------------------|--------------|
| C -> U | 0.048 | 9.6x |
| U -> C | 0.005 | 1.0x |
| A -> G | 0.006 | 1.2x |
| G -> A | 0.005 | 1.0x |
| Others (avg) | 0.003 | 0.6x |

The C->U substitution rate is approximately 10 times higher than other substitution types, consistent with APOBEC-mediated deamination.
