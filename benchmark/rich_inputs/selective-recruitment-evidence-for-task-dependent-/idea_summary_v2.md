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
