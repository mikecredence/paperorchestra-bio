# Experimental Log -- ACE2 Transcriptional Regulation by Sp1

## 2024-01-18 -- Luciferase reporter screen

Screened 45 different TF luciferase reporters in HPAEpiC cells to identify regulators of ACE2 expression. Correlated TF activity with ACE2 mRNA levels.

### Top hits from TF reporter screen

| Transcription factor | Reporter activity (fold vs control) | Correlation with ACE2 mRNA | Direction |
|---|---|---|---|
| Sp1 | 3.8 | r = 0.82 | Positive regulator |
| HNF4 | 0.35 | r = -0.75 | Negative regulator |
| AP-1 | 1.6 | r = 0.41 | Weak positive |
| NF-kB | 1.4 | r = 0.32 | Weak positive |
| STAT3 | 1.2 | r = 0.18 | Not significant |

Sp1 and HNF4 are the strongest regulators in opposing directions.

## 2024-02-12 -- Sp1/HNF4 validation

### Knockdown and overexpression effects on ACE2

| Condition | ACE2 mRNA (fold vs control) | ACE2 protein (fold vs control) | p-value |
|---|---|---|---|
| siControl | 1.0 | 1.0 | -- |
| siSp1 | 0.28 | 0.32 | <0.001 |
| Sp1 overexpression | 4.2 | 3.5 | <0.001 |
| siHNF4 | 3.1 | 2.8 | <0.001 |
| HNF4 overexpression | 0.35 | 0.40 | <0.001 |

Clean reciprocal regulation confirmed: Sp1 drives ACE2 up, HNF4 drives it down.

## 2024-03-05 -- SARS-CoV-2 infection effects on TF activity

Infected HPAEpiC cells with SARS-CoV-2 (MOI=0.1), measured TF activity at 24h and 48h.

| Parameter | Mock 24h | Infected 24h | Mock 48h | Infected 48h |
|---|---|---|---|---|
| Sp1 reporter activity (RLU) | 1.0 | 2.4 | 1.0 | 3.8 |
| HNF4 reporter activity (RLU) | 1.0 | 0.55 | 1.0 | 0.30 |
| Sp1 phosphorylation (p-Sp1/total) | 1.0 | 2.1 | 1.0 | 3.2 |
| HNF4 nuclear fraction (%) | 68 | 42 | 65 | 25 |
| ACE2 mRNA (fold) | 1.0 | 2.8 | 1.0 | 5.2 |

Infection progressively activates Sp1 (via phosphorylation) and excludes HNF4 from nucleus.

## 2024-03-25 -- PI3K/AKT pathway dissection

| Treatment | p-AKT (fold) | p-Sp1 (fold) | HNF4 nuclear (%) | ACE2 mRNA (fold) |
|---|---|---|---|---|
| Mock | 1.0 | 1.0 | 68 | 1.0 |
| SARS-CoV-2 | 3.5 | 3.2 | 25 | 5.2 |
| SARS-CoV-2 + LY294002 (PI3Ki) | 1.2 | 1.3 | 60 | 1.4 |
| SARS-CoV-2 + MK-2206 (AKTi) | 1.1 | 1.1 | 62 | 1.2 |

PI3K/AKT inhibition completely blocks virus-induced Sp1 activation, HNF4 nuclear exclusion, and ACE2 upregulation.

## 2024-04-15 -- Colchicine therapeutic potential

| Condition | ACE2 mRNA (fold) | p-AKT (fold) | Viral load (copies/mL) | Cell viability (%) |
|---|---|---|---|---|
| Mock | 1.0 | 1.0 | -- | 100 |
| SARS-CoV-2 | 5.2 | 3.5 | 2.4e6 | 72 |
| SARS-CoV-2 + colchicine 0.1 uM | 3.1 | 2.2 | 8.5e5 | 78 |
| SARS-CoV-2 + colchicine 1 uM | 1.8 | 1.4 | 2.1e5 | 82 |
| SARS-CoV-2 + colchicine 5 uM | 1.3 | 1.1 | 5.8e4 | 80 |
| Colchicine 5 uM alone | 0.9 | 0.95 | -- | 95 |

Colchicine dose-dependently inhibits PI3K/AKT, reduces ACE2 expression, and decreases viral load by ~1.5 log at 5 uM without major cytotoxicity.
