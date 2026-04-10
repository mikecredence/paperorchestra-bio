# Experimental Log: Disseminating EMT CSCs in Oral Cancer

## Cohort summary

| Property | Value |
|---|---|
| Cancer type | Human oral cancer |
| Total specimens | 84 |
| Imaging fields analyzed | >12,000 |
| Markers used | EpCAM, CD24, Vimentin |

## Disseminating cell enrichment

| Cell phenotype | Metastatic specimens | Non-metastatic specimens | Enrichment |
|---|---|---|---|
| EpCAM+/CD24+/Vimentin+ (triple+) | Significantly enriched | Low frequency | p < 0.05 |
| Single disseminating cells beyond tumour body | High count | Low count | Significant |

## Neural network metastasis prediction

| Metric | Value |
|---|---|
| Cross-validated accuracy | 87-89% |
| Input features | Disseminating cell counts and marker co-expression |
| Model type | Artificial neural network |
| Validation | Cross-validation on 84 specimens |

## Marker co-expression analysis

| Marker combination | Association with dissemination | Association with metastasis |
|---|---|---|
| EpCAM+ only | Epithelial, non-disseminating | Weak |
| Vimentin+ only | Mesenchymal stromal | Not predictive |
| EpCAM+/Vimentin+ | Partial EMT | Moderate |
| EpCAM+/CD24+/Vimentin+ | EMT CSC phenotype | Strong predictor |

## Notes

- 2024-01-05: Staining protocol optimized for triple immunofluorescence on FFPE oral cancer sections.
- 2024-01-28: Imaging of 84 specimens complete; >12,000 fields catalogued.
- 2024-02-12: Triple-positive disseminating cells significantly enriched at invasive front of metastatic cases.
- 2024-03-01: Neural network achieves 87-89% cross-validated accuracy for metastasis prediction.
- Key finding: first direct observation of EMT CSCs disseminating in human tumour tissue with clinical predictive value.
