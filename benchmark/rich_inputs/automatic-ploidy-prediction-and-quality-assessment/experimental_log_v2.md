# Experimental Log: BELA -- Embryo Ploidy Prediction from Time-Lapse Imaging

## Dataset Descriptions

### Table 1: Dataset Characteristics

| Dataset | Source | Instrument | N Embryos | EUP | SA | CxA | ANU (total) | Has BS | Has Maternal Age | Collection Period |
|---------|--------|-----------|-----------|-----|-----|-----|-------------|--------|-----------------|------------------|
| WCM-Embryoscope | Weill Cornell Medicine | Embryoscope | 1,998 | 916 | 494 | 588 | 1,082 | Yes | Yes | 2018-2019 |
| WCM-Embryoscope+ | Weill Cornell Medicine | Embryoscope+ | 841 | 410 | 170 | 261 | 431 | Yes | Yes | 2019-2020 |
| Spain (IVI Valencia) | IVI Valencia | Embryoscope | 543 | 234 | N/A | N/A | 309 | No | Yes | Not specified |
| Florida (IVF Florida) | IVF Florida | Embryoscope+ | 869 | 445 | 202 | 222 | 424 | Yes | Yes | Not specified |

### Table 2: Time-Lapse Sequence Details

| Parameter | Value |
|-----------|-------|
| Frames per sequence | 360-420 |
| Frame interval | 0.3 hours |
| Total imaging duration | ~5 days |
| BELA input window | 96-112 hpi (day 5) |

---

## Blastocyst Score Components

### Table 3: Blastocyst Score System

| Component | Description | Role |
|-----------|-------------|------|
| ICM grade | Inner cell mass morphology | Sub-component of BS |
| TE grade | Trophectoderm morphology | Sub-component of BS |
| Expansion score | Degree of blastocoel expansion | Sub-component of BS |
| Blastocyst Score (BS) | Sum of converted component scores | Range 3-14 (lower = higher quality) |
| Day of formation | Day blastocyst was formed | Contributes to BS |

---

## Model Architecture

### Table 4: BELA Pipeline Components

| Stage | Component | Details |
|-------|-----------|---------|
| 1 - Feature extraction | VGG16 (pretrained) | 512-dimensional feature vectors per frame |
| 1 - Temporal modeling | Multitask BiLSTM | Simultaneously predicts ICM, TE, expansion, BS |
| 1 - Augmentation | Horizontal + rotational | Applied to time-lapse sequences |
| 2 - Ploidy prediction | Logistic regression | Inputs: MDBS + maternal age |

### Table 5: Model Comparison Framework

| Model Type | Input | Requires Embryologist Input | Maternal Age Used |
|-----------|-------|---------------------------|------------------|
| Day-5 video model | Day-5 time-lapse video | No | Variant with/without |
| BELA | Day-5 video -> MDBS | No | Yes |
| Embryologist-annotated BS model | Embryologist-derived BS | Yes | Variant with/without |
| Maternal age only | Maternal age | No | Yes |
| BS + maternal age (logistic regression) | Manual BS + age | Yes | Yes |

---

## Performance Results

### Table 6: EUP vs. ANU -- AUC Performance on Internal Datasets

| Model | WCM-Embryoscope AUC (mean +/- SD) | WCM-Embryoscope+ AUC (mean +/- SD) |
|-------|-----------------------------------|-------------------------------------|
| Day-5 video (no maternal age) | Lower than BELA | Lower than BELA |
| BELA (no maternal age) | Improved over video-only | Improved over video-only |
| Embryologist BS (no maternal age) | Comparable to BELA | Comparable to BELA |
| Day-5 video + maternal age | Moderate | Moderate |
| BELA + maternal age | ~0.76 | Competitive |
| Embryologist BS + maternal age | ~0.76 | Competitive |

Fig 2a shows model performances without maternal age; Fig 2b shows performances with maternal age. BELA matches embryologist-annotated BS models and significantly surpasses video-only models.

### Table 7: EUP vs. CxA -- AUC Performance on Internal Datasets

| Model | WCM-Embryoscope AUC | WCM-Embryoscope+ AUC |
|-------|---------------------|----------------------|
| Day-5 video (no maternal age) | Lower | Lower |
| BELA (no maternal age) | Higher | Higher |
| Embryologist BS (no maternal age) | Comparable to BELA | Comparable to BELA |
| BELA + maternal age | Improved | Improved |
| Embryologist BS + maternal age | Comparable | Comparable |

### Table 8: External Validation -- Spain Dataset (EUP vs. ANU)

| Model | Spain AUC (mean +/- SE) |
|-------|------------------------|
| Day-5 video model | Lower |
| BELA | Higher than video model |

Fig 3 compares day-5 video model (blue bars) and BELA (orange bars) on the Spain dataset. BELA outperforms the video-only model on external data.

### Table 9: External Validation -- Florida Dataset

| Model | EUP vs. ANU AUC | EUP vs. CxA AUC |
|-------|-----------------|-----------------|
| BELA | Outperforms traditional ML | Outperforms traditional ML |
| Logistic regression (BS only) | Lower | Lower |
| Logistic regression (maternal age only) | Lower | Lower |
| Logistic regression (BS + maternal age) | Lower | Lower |

Fig 4 shows BELA outperforms traditional machine learning models trained on embryologist-derived BS and/or maternal age on the Florida dataset.

---

## Ablation Studies

### Table 10: Developmental Stage Comparison

| Time Window | Input Type | Relative Performance |
|-------------|-----------|---------------------|
| Early development (<96 hpi) | Image | Lower |
| Early development (<96 hpi) | Video | Lower |
| Day 5 (96-112 hpi) | Image | Moderate |
| Day 5 (96-112 hpi) | Video | Highest (selected for BELA) |
| Later stages (>112 hpi) | Video | Not superior to day 5 |

The ablation analysis (Supplemental Text 1) compared different embryonic development timepoints and image vs. video inputs, concluding that day-5 video (96-112 hpi) provides the optimal window.

---

## Single Aneuploid Behavior

### Table 11: SA Embryo Classification by EUP vs. CxA Model

| SA Embryo Predicted Class | Approximate Fraction |
|--------------------------|---------------------|
| Predicted as EUP | ~50% |
| Predicted as CxA | ~50% |

This even split suggests single aneuploid embryos morphologically resemble both euploid and complex aneuploid embryos, making their identification particularly challenging.

---

## Performance by Age Group

### Table 12: BELA AUC by SART Age Groups

| Age Group | WCM-Embryoscope | WCM-Embryoscope+ | Spain | Florida |
|-----------|----------------|-------------------|-------|---------|
| Younger groups | Higher AUC | Higher AUC | Variable | Variable |
| Middle groups | Lower AUC | Lower AUC | Variable | Variable |
| Older groups | Higher AUC | Higher AUC | Variable | Variable |
| Pattern | Bimodal | Bimodal | Different distribution | Different distribution |

Supplemental Table 2 shows bimodal performance pattern (best at lower and higher age groups) for WCM datasets. External datasets (Spain, Florida) do not follow same pattern, likely reflecting demographic differences across clinics.

---

## Score Prediction Quality

### Table 13: Blastocyst Score Prediction Evaluation

| Metric | Task | Value Range |
|--------|------|-------------|
| Mean Absolute Error (MAE) | BS prediction from video | Evaluated per component |
| MAE | ICM prediction | Component-level |
| MAE | TE prediction | Component-level |
| MAE | Expansion prediction | Component-level |

The multitask BiLSTM was evaluated using MAE for each blastocyst score sub-component. The model-derived blastocyst score (MDBS) serves as intermediate output providing explainability.

---

## Comparison with Prior Art

### Table 14: Published Ploidy Prediction Models

| Model | Input | AUC | Key Limitations |
|-------|-------|-----|----------------|
| ERICA | Single embryo image (1,231 images) | 0.74 | Cannot distinguish SA vs CxA; limited dataset |
| Barnes et al. | Single image at 110 hours | 0.61 | Single time point only |
| Liao et al. | Not specified | 0.70 | Required subjective morphokinetic parameters |
| BELA (this work) | Day-5 video + maternal age | 0.76 | Requires ~2,000 training sequences |

---

## PGT-A Ground Truth Details

### Table 15: Genetic Testing Protocols by Site

| Site | Biopsy Timing | Analysis Method | Technology |
|------|-------------- |----------------|-----------|
| Weill Cornell | Day 5 or Day 6 (at blastocyst) | NGS | In-house CRM |
| IVI Valencia (Spain) | Day 3 assisted hatching, blastocyst biopsy | NGS | Igenomix / Thermo Fisher |
| IVF Florida | Blastocyst stage | NGS | Igenomix / Thermo Fisher |
| Biopsy cells | 5-6 trophectoderm cells | All sites | Standard TE biopsy |

---

## Clinical Tool

### Table 16: STORK-V Web Interface Features

| Feature | Description |
|---------|-------------|
| Automation | Fully automated, no embryologist input needed |
| Output 1 | Model-derived blastocyst score |
| Output 2 | Ploidy status prediction |
| Explainability | Intermediate scores (ICM, TE, expansion) visible to embryologists |
| Input required | Time-lapse video + maternal age |

Fig 5 shows the STORK-V web interface providing comprehensive embryo assessment.

---

## Figure Observations

- **Fig 1**: Overview of BELA development pipeline. Steps 1-4 show feature extraction from time-lapse frames via VGG16. Multitask BiLSTM predicts blastocyst score components. Logistic regression predicts ploidy from MDBS and maternal age.

- **Fig 2**: Bar plots comparing mean AUC (+/- SD) across three model types (day-5 video, BELA, embryologist BS) on both WCM datasets. Panel (a) without maternal age, panel (b) with maternal age. BELA is competitive with embryologist-annotated models.

- **Fig 3**: External validation on Spain dataset. BELA (orange) outperforms day-5 video model (blue) for EUP vs. ANU classification.

- **Fig 4**: Florida dataset validation. BELA outperforms logistic regression models trained only on embryologist-derived BS and/or maternal age.

- **Fig 5**: Screenshot of STORK-V clinical web interface showing automated quality scoring and ploidy prediction.

---

## Key Limitations Noted

| Limitation | Impact |
|-----------|--------|
| Limited training data (~2,000 sequences) | Restricts experimentation with larger architectures |
| Performance drop on external datasets | Demographic and protocol differences across clinics |
| SA embryos difficult to classify | Even split between EUP and CxA predictions |
| Not a PGT-A replacement | Supplementary decision support tool |
| Single-center training | May not generalize to all clinic protocols |
