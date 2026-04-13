Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

# Idea Summary

## Working title
Selective Recruitment: Evidence for Task-Dependent Gating of Inputs to the Cerebellum

## Core question
Does the cerebellum receive task-dependent gating of neocortical inputs -- upregulated when cerebellar processing is functionally required -- rather than simply reflecting fixed transmission of neocortical activity?

## Motivation / gap
- Cerebellar BOLD signal reflects mossy fiber input, not Purkinje cell output, so activation could merely mirror neocortical activity through fixed anatomical connections
- fMRI studies show cerebellar activation across nearly all task domains, but this does not prove functional involvement
- Clinical evidence shows cerebellar lesions impair rapid alternating movements but not force generation, yet both produce cerebellar BOLD increases
- No null model has been applied to distinguish task-invariant transmission from selective recruitment of cerebellar processing
- The cerebellar contribution to cognitive functions like working memory cannot be inferred from activation alone

## Core contribution (bullet form)
- Used a cortico-cerebellar connectivity model (Ridge regression, trained on MDTB task set A) as a null model to predict cerebellar activity from neocortical patterns
- In a motor task, found that speed-related cerebellar activity exceeded model predictions (positive residuals for high speed: t15 significant), while force-related activity did not, consistent with clinical evidence
- In a digit span working memory task, found enhanced gating specifically during memory encoding (positive residuals), but not during retrieval or manipulation
- Motor task: M1/S1 ROI showed significant activation increases for high-force (t15 = 9.41, p = 1.10e-7) and high-speed (t15 = 8.29, p = 5.54e-7) conditions
- Cerebellar motor ROI increased for both force (t15 = 14.21, p = 4.14e-10) and speed (t15 = 7.60, p = 1.59e-6), but only speed showed selective recruitment

## Method in brief
Two fMRI experiments were conducted. Experiment 1 used an alternating finger tapping task with parametric manipulation of force (2.5N, 4N, 6N) and speed (1Hz, 2Hz, 3Hz baseline to high). A cortico-cerebellar connectivity model (Ridge regression on MDTB dataset) predicted cerebellar activity from neocortical patterns. Systematic positive residuals (observed > predicted) indicate selective recruitment. Experiment 2 used a digit span task with forward/backward recall at loads of 3-7 digits, separating encoding, delay, and retrieval phases.

The connectivity model was trained to predict each cerebellar voxel's activity from neocortical activity across diverse tasks, then evaluated on novel tasks. Residuals between observed and predicted cerebellar activity were analyzed: positive residuals indicate upregulated input (selective recruitment), negative residuals indicate downregulated input. ROI analyses focused on right cerebellar motor areas and D3R region of the multi-demand network.

## Target venue
eLife


## Experimental Log

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

