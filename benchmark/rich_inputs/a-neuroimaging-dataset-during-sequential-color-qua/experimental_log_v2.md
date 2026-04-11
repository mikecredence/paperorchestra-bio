# Experimental Log: Color Qualia fMRI Dataset

## Overview

Dataset capturing fMRI responses during sequential pairwise color similarity judgments in 35 healthy adults with both report and no-report conditions. Includes outside-scanner color vision assessments (Ishihara test, ND-100 Hue test) and psychological questionnaires.

---

## Participant Demographics

### Table 1: Participant Summary Statistics

| Metric | Value |
|--------|-------|
| Total participants | 35 |
| Male / Female | 17 / 18 |
| Age range (years) | 21-59 |
| Mean age (years) | 40.6 |
| SD age (years) | 12.5 |
| Excluded (head motion) | 4 |
| Final sample | 31 |

### Table 2: Questionnaire and Assessment Results (Grand Averages)

| Assessment | Mean | SD |
|------------|------|-----|
| Ishihara test score | 1.3 | 1.3 |
| ND-100 Hue test total | 119.1 | 85.1 |
| STAI Trait score | 43.1 | 10.5 |
| BDI-II score | 7.9 | 6.8 |

Note: All participants scored below the color blindness threshold of 5 on the Ishihara test. Demographics per participant described in Table 1 of the paper.

---

## Color Vision Assessment Details

### Table 3: ND-100 Hue Test Parameters

| Parameter | Value |
|-----------|-------|
| Number of hues | 100 |
| Color space | CIE 1964 |
| Brightness level | 6 |
| Hues per sorting row | 25 |
| Number of rows | 4 |
| Time limit per row | 2 minutes |
| Color difference unit | NBS unit (1 per hue step) |
| Discrimination score formula | abs(left neighbor - right neighbor) - 2 |
| Perfect score per hue | 0 |

---

## fMRI Task Design

### Table 4: Task Parameters

| Parameter | Value |
|-----------|-------|
| Number of colors | 9 |
| Unique color pairs | 45 |
| Trial types | Report, No-report |
| Response window | 4000 ms |
| Number of functional runs | 4 |
| Number of sessions | 4 |
| Report trial validity criterion | Cursor move + button click within 4000 ms |
| No-report trial validity criterion | No button click within 4000 ms |

### Table 5: Valid/Invalid Trial Counts Per Condition

| Condition | Valid Trials (Mean) | Invalid Trials (Mean) | Notes |
|-----------|--------------------|-----------------------|-------|
| Report | Majority valid | Small number invalid | First trial of each run omitted |
| No-report | Majority valid | Small number invalid | First trial of each run omitted |

Note: Detailed per-participant trial counts are in Table 2 of the paper. Validity was assessed based on whether participants clicked (report) or withheld clicking (no-report) within the 4000 ms window.

---

## Behavioral Consistency Analysis

### Table 6: Dissimilarity Score Consistency (Run 1-2 vs Run 3-4)

| Color Pair ID | Mean Dissimilarity (Run 1-2) | Mean Dissimilarity (Run 3-4) | Corrected p-value | Significant? |
|--------------|-----------------------------|-----------------------------|-------------------|-------------|
| Pairs 1-45 | Reported per pair | Reported per pair | All n.s. after correction | No |

Summary: Wilcoxon signed-rank tests with multiple comparison corrections showed no significant differences between first-half and second-half similarity judgments for any of the 45 color pairs. This confirms that participant responses were consistent across the four functional runs.

### Table 7: Grand Average Dissimilarity Scores (Selected Color Pairs)

| Color Pair | Mean Dissimilarity (Run 1-2) | Mean Dissimilarity (Run 3-4) | Corrected p-value | Min N Available |
|------------|-----------------------------|-----------------------------|-------------------|-----------------|
| All 45 pairs | Values per pair in Table 3 | Values per pair in Table 3 | All > 0.05 | Varies by pair |

Note: Table 3 of the paper provides the full 45-pair breakdown with corrected p-values and minimum participant counts.

---

## Intra- and Inter-Participant Consistency

### Table 8: Double-Pass Correlation Summary

| Analysis Type | Comparison | Result |
|--------------|------------|--------|
| Intra-participant | Run 1-2 vs Run 3-4 (same person) | High correlation coefficients (Fig 3a diagonal) |
| Inter-participant | Person i vs Person j (45 color pairs) | Moderate-to-high correlations (Fig 3a off-diagonal) |

Fig 3a shows the full correlation matrix (r_ij) quantifying consistency between each pair of participants for ratings of 45 color pairs. The diagonal (intra-participant) values are generally higher than off-diagonal (inter-participant) values.

Fig 3d displays the histogram of intra-participant correlation coefficients, showing substantial coherence between the first and second halves of the task.

---

## fMRI Data Quality Metrics

### Table 9: Framewise Displacement (FD) Summary

| Metric | Value |
|--------|-------|
| Measure | Average FD per run |
| Runs per participant | 4 |
| Grand average FD (all participants, all runs) | Shown as gray dotted line in Fig 4a |
| Exclusion criterion | Excessive head motion (4 participants excluded) |

Fig 4a shows individual FD data per run and the overall average across all four runs. The gray dotted line indicates the grand average.

### Table 10: Temporal Signal-to-Noise Ratio (tSNR) Summary

| Metric | Value |
|--------|-------|
| Measure | tSNR per run |
| Runs per participant | 4 |
| Grand average tSNR | Shown as gray dotted line in Fig 4b |

Fig 4b displays individual tSNR data with per-run and per-participant averages. The gray dotted line represents the grand average across all participants and runs.

---

## Brain Activation Results

### Table 11: Color Observation-Related Activation

| Analysis | Key Finding |
|----------|------------|
| Task-related activation | Fig 4 shows visualization of brain activation during color observation |
| Expected regions | Ventral occipitotemporal cortex (V4/V8 areas) |
| Report vs No-report | Dataset enables comparison but detailed results not reported in data descriptor |

---

## Data Structure and Format

### Table 12: Dataset Organization

| Component | Format/Standard |
|-----------|----------------|
| Overall format | BIDS v1.9.0 |
| Repository | OpenNeuro (OSF: https://osf.io/sqd7n/) |
| Top-level directory | ColorSimilarity_fMRI_exp |
| Participant directories | sub-01 through sub-35 |
| Sessions per participant | 4 |
| Session contents | anat (anatomical), func (functional) |
| Functional data | Task-related fMRI + event timing files |
| Behavior files | Color comparison results + questionnaire results |
| Personally identifiable info | Removed |
| Original format | DICOM (converted to BIDS) |

### Table 13: Data Modalities Per Participant

| Modality | Description | Sessions |
|----------|-------------|----------|
| Anatomical MRI | T1-weighted structural scan | Available |
| Functional MRI | Task-related BOLD data | 4 runs across sessions |
| Behavioral logs | Trial-by-trial similarity ratings | Per run |
| Event files | Stimulus onset/offset timing | Per run |
| Questionnaires | STAI, BDI-II, Edinburgh Handedness | Once |
| Ishihara test | Color vision deficiency screening | Once |
| ND-100 Hue test | Color discrimination profile | Once |

---

## Color Stimuli Specifications

### Table 14: Stimulus Set

| Parameter | Value |
|-----------|-------|
| Number of colors | 9 |
| Color space | CIE 1964 |
| Presentation | Sequential (2 colors per trial) |
| Total unique pairs | C(9,2) = 45 |
| Stimulus display | Inside MRI scanner |

Fig 1c shows the 9 colors used in the fMRI task. Fig 1d illustrates the trial procedure.

---

## Experimental Workflow

### Table 15: Session Sequence

| Step | Description | Location |
|------|-------------|----------|
| 1 | ND-100 Hue test | Outside scanner |
| 2 | Ishihara test (38 plates) | Outside scanner |
| 3 | Edinburgh Handedness Inventory | Outside scanner |
| 4 | STAI questionnaire | Outside scanner |
| 5 | BDI-II questionnaire | Outside scanner |
| 6 | Practice color similarity task | Outside scanner |
| 7 | Practice color similarity task | Inside scanner |
| 8 | MRI scanning (4 functional runs) | Inside scanner |

Fig 1a provides an overview of this experimental workflow.

---

## Key Figure Observations

- Fig 1b: The 100 ND-100 hue test colors are arranged on a chromaticity grid based on CIE 1964 color space, each separated by one NBS color difference unit.
- Fig 2: Folder structure follows BIDS format with hierarchical participant/session/modality organization.
- Fig 3: Correlation matrices show that intra-participant consistency (diagonal) is generally higher than inter-participant consistency (off-diagonal). The histogram of intra-participant correlations clusters at high r values.
- Fig 4a: FD values vary across participants and runs; four participants with excessive motion were excluded.
- Fig 4b: tSNR values are generally stable across runs within participants.
- Fig 4: Brain activation maps during color observation show expected patterns in visual cortex.

---

## Datasets and Metrics Used

### Table 16: External References

| Resource | Purpose |
|----------|---------|
| OpenNeuro / OSF | Data repository |
| BIDS v1.9.0 | Data format standard |
| CIE 1964 color space | Color specification |
| ND-100 Hue test (Japan Color Research Institute) | Color discrimination assessment |
| Ishihara 38-plate test | Color deficiency screening |
| Edinburgh Handedness Inventory | Handedness assessment |
| STAI | Anxiety measurement |
| BDI-II | Depression measurement |

### Table 17: Statistical Methods

| Method | Application |
|--------|------------|
| Wilcoxon signed-rank test | Comparing first-half vs second-half similarity ratings |
| Multiple comparison correction | Applied to 45 color-pair comparisons |
| Pearson correlation (double-pass) | Intra- and inter-participant consistency |
| Framewise displacement | Head motion quantification |
| tSNR | Signal quality assessment |
