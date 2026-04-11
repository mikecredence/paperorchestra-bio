# Experimental Log

> Pre-writing data tables and observations for the disseminating EMT CSC study in human oral tumours.

---

## Datasets and Specimens

| Dataset | N | Description | Stratification |
|---------|---|-------------|---------------|
| CA1 OSCC cell line | N/A | Parental oral squamous cell carcinoma line | Epithelial phenotype |
| EMT-stem CA1 sub-line | N/A | Derivative of CA1 with EMT CSC properties | Mesenchymal + retained plasticity |
| Normal keratinocytes | N/A | Non-cancer epithelial control | Negative control |
| Cancer-associated fibroblasts | N/A | Stromal cell control | Negative control |
| Tumour batch 1 | Variable | Human OSCC specimens | Metastatic vs. non-metastatic |
| Tumour batch 2 | Variable | Human OSCC specimens (independent) | Metastatic vs. non-metastatic |
| Total tumour specimens | 84 | Human oral cancer | Stratified on metastatic status |
| Total imaging fields | >12,000 | Automated whole-slide imaging | Across all 84 specimens |

---

## Markers and Staining Panels

| Panel | Marker 1 (Yellow) | Marker 2 (Red) | Marker 3 (Green) | Nuclear Stain (Blue) |
|-------|-------------------|----------------|-------------------|---------------------|
| Primary panel | EpCAM | Vimentin | CD24 | DAPI |
| Control panel | Pan-keratin | Vimentin | CD24 | DAPI |

---

## Experiment 1: Validation in Cell Lines - EpCAM+Vim+CD24+ Identifies EMT CSCs

Fig. 1A-B: Immunofluorescent staining for EpCAM, Vimentin, and CD24 in CA1 cell line (A) and EMT-stem sub-line (B).

Fig. 1C-D: Immunofluorescent staining replacing EpCAM with pan-keratin in CA1 (C) and EMT-stem sub-line (D).

| Cell Population | EpCAM+Vim+CD24+ (%) | Pan-keratin+Vim+CD24+ (%) |
|----------------|---------------------|--------------------------|
| CA1 parental line | 2.1 | Very low |
| EMT-stem sub-line | 41.0 | Very low (no enrichment) |
| Normal keratinocytes | 0 (absent) | 0 (absent) |
| Cancer-associated fibroblasts | 0 (absent) | 0 (absent) |

Fig. 1E: Quantification confirms a significant enrichment of EpCAM+Vim+CD24+ cells in the EMT-stem sub-line compared to CA1. Significance by two-tailed Student t-test. Mean +/- 95% confidence intervals reported.

Key finding: EpCAM is retained during EMT while pan-keratins are lost. The triple-positive staining profile specifically marks EMT CSCs.

---

## Experiment 2: Disseminating Cells in Human Tumour Specimens

Fig. 2A-C: Representative imaging fields from normal epithelial region (A), non-metastatic tumour (B), and metastatic tumour (C). 4-colour staining: EpCAM (yellow), Vimentin (red), CD24 (green), DAPI (blue).

Fig. 2D: Staining of a metastatic tumour using the pan-keratin control panel.

Fig. 2E: Image segmentation approach. An EpCAM density map separates the tumour body from surrounding stroma.

| Region | Definition | Purpose |
|--------|-----------|---------|
| Tumour body | High EpCAM density region | Main tumour mass |
| Stroma | Low EpCAM density surrounding tumour | Where disseminating cells are detected |
| Disseminating cells | Single EpCAM+ cells in stroma | Cells that have left the tumour |

---

## Experiment 3: Enrichment of EpCAM+Vim+CD24+ Cells in Metastatic Tumour Stroma

| Tumour Status | EpCAM+Vim+CD24+ in Stroma | Significance |
|---------------|---------------------------|-------------|
| Non-metastatic | Lower frequency | Reference |
| Metastatic | Significantly enriched | p < 0.05 (specific p-value in figures) |

| Marker Combination | Enrichment in Metastatic Stroma | Clinical Relevance |
|-------------------|--------------------------------|-------------------|
| EpCAM+Vim+CD24+ | Significant enrichment | Correlates with metastasis |
| EpCAM+Vim+CD24- | No significant enrichment | Not predictive |
| Pan-keratin+Vim+CD24+ | No enrichment | Not useful |

Key finding: The CD24+ marker is specifically required alongside EpCAM and Vimentin to identify disseminating EMT CSCs that correlate with metastasis. EpCAM+CD24-Vim+ stromal cells do NOT correlate with metastatic disease.

---

## Experiment 4: Machine Learning Classification - Tumour Batch 1

Fig. 3A: Pipeline for supervised learning based on grey-level intensities of three markers in imaging tiles. Training tiles classified as coming from metastatic or non-metastatic tumour.

### EpCAM + Vimentin + CD24 Panel (Fig. 3B)

| Metric | Value |
|--------|-------|
| Cross-validation method | 10-fold |
| Cross-validated accuracy | 87-89% |
| Model type | Artificial neural network |
| Input features | Grey-level intensities for EpCAM, Vimentin, CD24 per tile |

### Pan-keratin + Vimentin + CD24 Panel (Fig. 3C)

| Metric | Value |
|--------|-------|
| Cross-validation method | 10-fold |
| Cross-validated accuracy | Lower than EpCAM panel |
| Model type | Artificial neural network |
| Input features | Grey-level intensities for pan-keratin, Vimentin, CD24 per tile |

---

## Experiment 5: Independent Validation on Tumour Batch 2

Fig. 3 shows that the model trained on batch 1 was applied to batch 2 as an independent test set.

| Evaluation | Training Set | Test Set | Accuracy |
|-----------|-------------|----------|----------|
| Within-batch (10-fold CV) | Batch 1 | Batch 1 (held-out folds) | 87-89% |
| Cross-batch validation | Batch 1 | Batch 2 (independent) | High accuracy maintained |

---

## Experiment 6: Detailed Staining Quantification Across Specimen Types

| Specimen Type | EpCAM+ in Stroma | Vim+ in Stroma | CD24+ in Stroma | Triple-positive in Stroma |
|--------------|-----------------|---------------|----------------|--------------------------|
| Normal epithelium | Minimal | High (stromal cells) | Variable | Absent/rare |
| Non-metastatic OSCC | Low | High | Variable | Low frequency |
| Metastatic OSCC | Elevated (disseminating cells) | High | Variable | Significantly enriched |

---

## Image Analysis Parameters

| Parameter | Value |
|-----------|-------|
| Imaging mode | Automated 4-colour immunofluorescence |
| Coverage | Entire histopathological slides |
| Total imaging fields | >12,000 |
| Total specimens | 84 |
| Segmentation output | Per-cell marker intensities |
| EpCAM density map | Used to delineate tumour body vs. stroma |
| Cell identification | Individual cell level across each specimen |

---

## Statistical Tests Used

| Test | Application | Figures |
|------|------------|---------|
| Two-tailed Student t-test | Cell line marker quantification | Fig. 1E |
| Significance testing | Enrichment of triple-positive cells in metastatic vs. non-metastatic stroma | Fig. 2 |
| 10-fold cross-validation | ML model performance | Fig. 3B, 3C |
| Independent test set validation | Cross-batch generalization | Fig. 3 |

---

## Key Cell Line Observations

| Observation | Figure | Details |
|-------------|--------|---------|
| EpCAM retained in EMT | Fig. 1A-B | EMT-stem cells keep EpCAM surface expression |
| Pan-keratin lost in EMT | Fig. 1C-D | Epithelial keratins are downregulated |
| CD24 marks plasticity | Fig. 1E | Required for marking cells with MET capability |
| Triple-positive absent in non-tumour | Fig. S1 | Normal keratinocytes and fibroblasts lack this profile |

---

## Comparison with Prior Work

| Study Type | EMT Detection | Limitation |
|-----------|--------------|-----------|
| Previous in vivo studies | Cells at tumour margin (attached) | Cannot track cells that have left the tumour |
| scRNAseq (partial EMT) | Gene expression signatures | Correlated with metastasis but no spatial resolution |
| Mouse models | Lineage tracing | Species-specific, may not translate to human |
| This study | Single disseminating cells in stroma | First demonstration in human tumour specimens |

---

## Marker Biology Summary

| Marker | Role | Expression in EMT CSCs | Expression in Stroma |
|--------|------|----------------------|---------------------|
| EpCAM | Epithelial cell adhesion molecule | Retained in plastic EMT subset | Absent (epithelial-specific) |
| CD24 | EMT CSC plasticity marker | Retained in MET-competent subset | Variable |
| Vimentin | Mesenchymal marker | Upregulated during EMT | High in stromal fibroblasts |
| Pan-keratin | Epithelial intermediate filaments | Lost during EMT | Absent in stroma |
| CD44 | CSC marker (flow cytometry) | Cannot use in tissue (requires trypsin) | Not applicable here |

---

## Machine Learning Model Details

| Component | Specification |
|-----------|--------------|
| Architecture | Artificial neural network |
| Input | Grey-level intensities per tile (3 channels) |
| Labels | Metastatic vs. non-metastatic tumour origin |
| Validation | 10-fold cross-validation on batch 1 |
| External validation | Independent batch 2 |
| Best accuracy | 87-89% (cross-validated) |
| EpCAM panel performance | Superior |
| Pan-keratin panel performance | Inferior |

---

## Overall Conclusions from Data

1. EpCAM+Vim+CD24+ triple staining identifies EMT CSCs with retained plasticity, enriched to 41% in EMT-stem sub-line vs. 2.1% in parental CA1.
2. Single disseminating EpCAM+Vim+CD24+ cells are significantly enriched in the stroma of metastatic oral tumour specimens.
3. The CD24 marker is specifically required; EpCAM+Vim+CD24- cells do not correlate with metastasis.
4. Pan-keratin cannot substitute for EpCAM in this application because keratins are lost during EMT.
5. An artificial neural network trained on the three-marker profile predicts metastasis with 87-89% cross-validated accuracy.
6. These findings provide the first direct observation of EMT CSCs disseminating from human tumours in vivo and link this process to metastatic outcome.
