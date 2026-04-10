# Experimental Log -- Tumour mRegDC Heterogeneity

## 2024-01-25 -- Photoconversion tracking of DC migration

Used photoconvertible mouse model (Kaede). Tumours photoconverted at day 10 post-implantation. Tracked converted DCs in tumour and dLN over time.

### DC migration kinetics post-photoconversion

| Time post-conversion | % converted DCs in tumour | % converted DCs in dLN | % mRegDC among converted in dLN |
|---|---|---|---|
| 6 h | 85 | 5 | 78 |
| 24 h | 52 | 28 | 82 |
| 48 h | 30 | 42 | 85 |
| 72 h | 18 | 38 | 80 |

mRegDCs are the dominant population arriving in dLN (78-85% of migrated DCs). A substantial fraction remains tumour-resident even at 72 h.

## 2024-02-20 -- Phenotypic comparison: tumour vs dLN mRegDCs

Flow cytometry panel on mRegDCs sorted from tumour vs dLN at 48 h post-photoconversion.

| Marker (MFI) | Tumour mRegDC | dLN mRegDC | Fold difference | p-value |
|---|---|---|---|---|
| CCR7 | 2,800 | 4,500 | 0.62x | <0.01 |
| PD-L1 | 6,200 | 3,100 | 2.0x | <0.001 |
| MHC-II | 3,400 | 5,800 | 0.59x | <0.001 |
| CD80 | 1,200 | 2,900 | 0.41x | <0.001 |
| CD86 | 1,800 | 3,500 | 0.51x | <0.01 |
| IL-12 (intracellular) | 450 | 1,100 | 0.41x | <0.01 |

Tumour-retained mRegDCs have higher PD-L1 but lower MHC-II, costimulatory molecules, and IL-12 compared to dLN migrants.

## 2024-03-15 -- Temporal evolution of tumour mRegDCs

scRNA-seq on tumour mRegDCs binned by dwell-time using photoconversion timestamps.

### Expression changes by dwell-time (log2FC vs freshly arrived)

| Gene module | Short dwell (<24h) | Medium dwell (24-48h) | Long dwell (>48h) |
|---|---|---|---|
| Antigen presentation (H2-Aa, H2-Ab1) | 0 (ref) | -0.8 | -1.6 |
| Pro-inflammatory (Il12b, Tnf) | 0 (ref) | -1.1 | -2.3 |
| Regulatory (Cd274/PD-L1, Socs2) | 0 (ref) | +0.5 | +1.2 |
| Migration (Ccr7, Fscn1) | 0 (ref) | -0.3 | -0.9 |

Progressive loss of antigen presentation and pro-inflammatory capacity with increased dwell-time. Regulatory program intensifies.

## 2024-04-02 -- Spatial co-localization analysis

Multiplexed IHC on murine and human tumour sections.

| Species | mRegDC-PD1+CD8+ proximity (<30um) | Random expectation | Enrichment fold |
|---|---|---|---|
| Mouse (MC38) | 38% of mRegDCs | 11% | 3.5x |
| Mouse (B16) | 32% of mRegDCs | 9% | 3.6x |
| Human (melanoma) | 41% of mRegDCs | 13% | 3.2x |
| Human (NSCLC) | 35% of mRegDCs | 10% | 3.5x |

Significant spatial co-localization in both species and tumour types.

## 2024-04-18 -- Anti-PD-L1 treatment effects

Treated MC38 tumour-bearing mice with anti-PD-L1 vs isotype control. Profiled tumour mRegDCs at day 5 post-treatment.

| Parameter | Isotype control | Anti-PD-L1 | p-value |
|---|---|---|---|
| Tumour mRegDC frequency (% of CD45+) | 4.2 | 6.8 | <0.01 |
| MHC-II MFI on tumour mRegDC | 3,200 | 4,900 | <0.01 |
| IL-12+ tumour mRegDC (%) | 12 | 28 | <0.001 |
| PD-L1 MFI | 6,100 | 2,800 | <0.001 |
| CD8+ T cell infiltration (cells/mm^2) | 180 | 420 | <0.001 |

Anti-PD-L1 treatment partially reverses the regulatory phenotype of tumour mRegDCs and boosts CD8+ T cell infiltration.
