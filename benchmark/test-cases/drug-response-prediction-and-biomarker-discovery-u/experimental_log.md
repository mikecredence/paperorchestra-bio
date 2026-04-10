# Experimental Log: Multi-Modal DRP and Biomarker Discovery

## Data sources

| Dataset | Cell lines | Drugs | Molecular modalities |
|---|---|---|---|
| Large-scale screening panel | Hundreds of cancer cell lines | Panels of drugs | Genomics, proteomics, transcriptomics |

## Model architecture comparison

| Model | Modalities used | Prediction metric (R2 or RMSE) | Notes |
|---|---|---|---|
| Multi-modal DL (ours) | Genomics + proteomics + drug features | Best performance | Full integration |
| Single-modal DL (genomics only) | Genomics + drug features | Lower than multi-modal | Missing proteomic signal |
| Traditional ML (random forest) | Genomics | Baseline | No deep learning |
| Existing DRP methods | Varies | Lower than ours | Published benchmarks |

## Drug response prediction results

| Metric | Multi-modal DL | Single-modal DL | Traditional ML |
|---|---|---|---|
| Pearson correlation | Highest | Moderate | Lowest |
| RMSE | Lowest | Moderate | Highest |
| Spearman correlation | Highest | Moderate | Lowest |

## Biomarker discovery

| Discovery approach | Number of biomarkers identified | Validation method |
|---|---|---|
| Attention/feature importance | Multiple per drug | Literature cross-reference |
| Pathway enrichment | Key oncogenic pathways | Gene set analysis |

## Notes

- 2024-01-18: Multi-modal data preprocessing and alignment complete.
- 2024-02-06: Multi-modal DL consistently outperforms single-modal and traditional ML baselines.
- 2024-02-22: Biomarker extraction from attention weights identifies known and novel drug-gene associations.
- 2024-03-08: Pathway analysis confirms enrichment for known oncogenic signaling pathways.
- Key insight: proteomic data provides complementary signal to genomics that meaningfully improves DRP.
