## Working title
An fMRI Dataset for Studying Color Qualia Similarity Judgments With and Without Overt Reports

## Core question
Can we build a publicly available fMRI dataset that captures neural activity during pairwise color qualia similarity judgments -- including a no-report condition -- to enable investigation of the neural substrates of subjective color experience?

## Motivation / gap
- The relationship between subjective qualitative experience (qualia) and specific brain regions/networks remains poorly understood
- Traditional neuroimaging studies of color perception rely on verbal descriptions, which introduce biases and are difficult to quantify structurally
- The "qualia structure" paradigm (leveraging exhaustive relational comparisons among qualia rather than verbal reports) has been proposed but no fMRI dataset existed that captures these relational similarity judgments for color
- No-report paradigms are critical for dissociating genuine neural correlates of consciousness from report-related confounds, yet no color qualia fMRI dataset included such a condition
- Prior fMRI work on color (V4/V8 region studies, multi-voxel pattern analyses) focused on neural responses to individual colors rather than relational similarity structure
- No open dataset existed combining color similarity fMRI with individual-level color discriminability assessments (hue tests)

## Core contribution (bullet form)
- First fMRI dataset capturing pairwise similarity judgments among 9 color qualia from 35 participants (ages 21-59, M = 40.6, SD = 12.5)
- Dataset includes both report and no-report conditions (half of trials each), enabling analysis of overt reporting effects on color qualia processing
- Each participant completed ND-100 Hue test outside the scanner, providing individual color discriminability profiles
- Behavioral validation shows consistent similarity ratings: Wilcoxon signed-rank tests across all 45 color pairs revealed no significant differences between first and second halves
- Intra-participant double-pass correlations demonstrate high coherence of individual ratings
- Data organized in BIDS format (v1.9.0) and freely available on OpenNeuro, including 4 fMRI sessions per participant

## Method in brief
Thirty-five adults (17 male, 18 female) with normal color vision (confirmed via 38-plate Ishihara test) performed a sequential color similarity judgment task in the MRI scanner. Nine colors were selected, yielding 45 unique pairwise combinations. On each trial, participants viewed two colors sequentially and judged their similarity. Half the trials were "report" trials (participants moved a cursor and clicked a decision button within 4000 ms) and half were "no-report" trials (no button press required within the same window). Participants completed 4 functional runs across sessions.

Outside the scanner, each participant completed the ND-100 Hue test, which uses 100 equally spaced hues on a CIE 1964 color space circumference. Participants sorted 25 randomly arranged hues into correct gradient order (4 rows, 2-min time limit each). Discrimination scores were computed for each hue based on the absolute differences between assigned numbers of neighboring hues. Additionally, participants completed the Edinburgh Handedness Inventory, STAI, and BDI-II questionnaires.

All data were converted to BIDS format (v1.9.0) and deposited on OpenNeuro. Quality metrics including framewise displacement and temporal signal-to-noise ratio (tSNR) were computed per run. Four participants were excluded due to excessive head motion.

## Target venue
Scientific Data
