# Experimental Log

> Pre-writing data tables and observations for the cerebellar selective recruitment study.

---

## Motor Task Design (Table 1)

| Condition | Target Force (N) | Target Taps | Error Rate (%) |
|-----------|-----------------|-------------|---------------|
| Baseline | 2.5 | 6 | Higher (easy, completed fast) |
| Medium Force | 4.0 | 6 | Low |
| High Force | 6.0 | 6 | Low |
| Medium Speed | 2.5 | 9 | Low |
| High Speed | 2.5 | 12 | Low |

Table 1: Mean and between-subject SD of force, speed, and error rate for each condition (n=16 participants).

---

## Experiment 1: Motor Task Activation

| ROI | Condition | t-statistic | p-value | n |
|-----|-----------|-------------|---------|---|
| M1/S1 (left) | High Force vs Baseline | t15 = 9.41 | 1.10e-7 | 16 |
| M1/S1 (left) | High Speed vs Baseline | t15 = 8.29 | 5.54e-7 | 16 |
| Cerebellar motor (right) | High Force vs Baseline | t15 = 14.21 | 4.14e-10 | 16 |
| Cerebellar motor (right) | High Speed vs Baseline | t15 = 7.60 | 1.59e-6 | 16 |

Fig. 2: Activity maps for high force, baseline, and high speed conditions on cortical surface and cerebellar flatmap.

---

## Experiment 2: Motor Task -- Selective Recruitment Analysis

| Condition | Observed Cerebellar Activity | Predicted (from model) | Residual Direction |
|-----------|-----------------------------|-----------------------|-------------------|
| Baseline | Reference point (0,0) | Reference | Zero |
| Medium Force | Increased | Proportional increase | Near zero (on regression line) |
| High Force | Increased | Proportional increase | Near zero (on regression line) |
| Medium Speed | Increased | Moderate increase | Positive (above regression line) |
| High Speed | Strongly increased | Moderate increase | Strongly positive |

Fig. 3A: Connectivity weights from group-level model for cerebellar right-hand area.
Fig. 3B: Observed vs predicted cerebellar activation. Force conditions fall on the regression line; speed conditions fall above it.

---

## Connectivity Model Details

| Parameter | Value |
|-----------|-------|
| Training dataset | MDTB task set A |
| Regression method | Ridge regression |
| Alternative tested | Lasso regression; 5-dataset Ridge |
| Evaluation metric | Cosine similarity (predicted vs observed) |
| Model performance | Good prediction across novel tasks |

Supp. Fig. 1: Connectivity model evaluation with alternative models showing similar predictive accuracy.

---

## Experiment 3: Digit Span Working Memory Task

| Phase | Memory Load | Cerebellar D3R Activity | Model Prediction | Residual |
|-------|------------|------------------------|-----------------|----------|
| Encoding | Load 3 | Moderate | Moderate | Positive (above line) |
| Encoding | Load 5 | Higher | Higher | Positive (above line) |
| Encoding | Load 7 | Highest | Highest | Positive (above line) |
| Retrieval (Forward) | Load 3-7 | Present | Present | Near zero |
| Retrieval (Backward) | Load 3-7 | Present | Present | Near zero |

Fig. 4: Digit span task timeline -- cue, encoding, delay, retrieval phases.
Fig. 5A-B: Group-averaged activation during encoding shows cortical and cerebellar increases.
Fig. 5C-D: Cerebellar D3R sub-region of multi-demand network used for main analysis.

---

## Experiment 4: WM Selective Recruitment Analysis

| Task Phase | Selective Recruitment (residual > 0)? | Interpretation |
|-----------|--------------------------------------|---------------|
| Encoding | Yes -- positive residuals | Cerebellum actively recruited for encoding |
| Retrieval (Forward) | No -- residuals near zero | Activity explained by fixed connectivity |
| Retrieval (Backward) | No -- residuals near zero | No additional cerebellar engagement |

Fig. 6A: Connectivity weights for cerebellar D3R region of interest.
Fig. 6B: Observed vs predicted cerebellar activity. Encoding conditions show positive residuals; retrieval does not.

---

## Behavioral Performance (Digit Span)

| Measure | Load 3 | Load 5 | Load 7 |
|---------|--------|--------|--------|
| Accuracy (Forward) | High | Moderate | Lower |
| Accuracy (Backward) | High | Moderate | Lower |
| Go vs No-Go | Go trials: retrieval; No-go: encoding only | - | - |

Fig. 4: Behavioral accuracy and response time data.

---

## Statistical Approach

| Analysis | Method |
|----------|--------|
| ROI activation | One-sample t-tests vs baseline |
| Selective recruitment | Linear regression of observed vs predicted; analysis of residuals |
| Model comparison | Cosine similarity on held-out tasks |
| Significance threshold | Standard p < 0.05 |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Motor task timeline with force and speed manipulation |
| Fig. 2 | Both force and speed increase cortical and cerebellar activation |
| Fig. 3 | Speed conditions show positive residuals (selective recruitment); force does not |
| Fig. 4 | Digit span task design with encoding, delay, retrieval phases |
| Fig. 5 | Cortical and cerebellar activation during WM encoding and retrieval |
| Fig. 6 | Encoding shows selective recruitment; retrieval does not |
| Supp. Fig. 1 | Alternative connectivity models yield similar results |

---

## Reference Count
64 references cited.
