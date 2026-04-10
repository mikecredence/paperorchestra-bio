# Experimental Log -- Thiolutin and RNA Pol II

## 2024-01-10 -- Chemicogenetic screen in S. cerevisiae

Screened yeast deletion library for altered sensitivity to thiolutin (5 ug/mL). Identified mutants with increased sensitivity and resistance.

### Top sensitive mutants

| Gene deleted | Function | Growth (thiolutin/DMSO ratio) | Interpretation |
|---|---|---|---|
| TRX1 | Thioredoxin | 0.12 | Redox buffering critical |
| TRX2 | Thioredoxin | 0.15 | Confirms redox link |
| SOD1 | Superoxide dismutase | 0.22 | Oxidative stress component |
| PMR1 | Mn2+ transporter | 0.18 | Mn involvement |
| CTR1 | Cu2+ transporter | 0.25 | Cu involvement |

### Top resistant mutants

| Gene deleted | Function | Growth (thiolutin/DMSO ratio) | Interpretation |
|---|---|---|---|
| ZRT1 | Zn2+ transporter | 1.05 | Zn chelation relevant |
| FET3 | Fe/Cu oxidase | 0.95 | Metal homeostasis |

## 2024-02-05 -- Thioredoxin oxidation assay

Treated cells with thiolutin (3 ug/mL, 15 min) and measured thioredoxin redox state by AMS gel shift.

| Condition | % oxidized Trx1 | % oxidized Trx2 |
|---|---|---|
| DMSO control | 8 | 12 |
| Thiolutin 3 ug/mL | 65 | 72 |
| H2O2 positive ctrl | 78 | 81 |

Thiolutin causes strong thioredoxin oxidation in vivo, approaching H2O2 levels.

## 2024-03-01 -- Metal interaction experiments

Growth inhibition by thiolutin (3 ug/mL) with supplementation of various metals.

| Metal added (100 uM) | Growth rescue (% of untreated) | p-value vs thiolutin alone |
|---|---|---|
| None (thiolutin only) | 35 | -- |
| Zn2+ | 78 | <0.001 |
| Mn2+ | 70 | <0.001 |
| Cu2+ | 28 | ns (worsened) |
| Fe2+ | 40 | ns |
| Mg2+ | 36 | ns |

Zn2+ and Mn2+ both rescue growth, while Cu2+ actually worsens it. Thiolutin interacts functionally with multiple metals.

## 2024-04-10 -- In vitro Pol II transcription assay

Purified yeast Pol II, reconstituted transcription initiation on a model promoter template. Measured runoff transcription with radiolabeled NTPs.

### Thiolutin dose-response on Pol II transcription

| Thiolutin (uM) | Relative transcription (%) | Mn2+ (1 mM) present | DTT (5 mM) |
|---|---|---|---|
| 0 | 100 | Yes | 0.5 mM |
| 5 | 72 | Yes | 0.5 mM |
| 10 | 45 | Yes | 0.5 mM |
| 25 | 18 | Yes | 0.5 mM |
| 50 | 8 | Yes | 0.5 mM |
| 25 | 92 | No Mn2+ | 0.5 mM |
| 25 | 88 | Yes | 5 mM (excess) |

IC50 approximately 12 uM in the presence of Mn2+. Removing Mn2+ or adding excess DTT abrogates inhibition almost completely.

### Key controls

| Condition | Relative transcription (%) |
|---|---|
| No thiolutin, +Mn2+, 0.5 mM DTT | 100 |
| 25 uM thiolutin, +Mn2+, 0.5 mM DTT | 18 |
| 25 uM thiolutin, no Mn2+ | 92 |
| 25 uM thiolutin, +Mn2+, 5 mM DTT | 88 |
| 25 uM holomycin, +Mn2+, 0.5 mM DTT | 22 |

Both thiolutin and the related dithiolopyrrolone holomycin directly inhibit Pol II. Inhibition is Mn2+-dependent and redox-sensitive.
