## Working title

Multi-dimensional neural and behavioral signatures of acute ketamine: linking inter-individual variability to cortical gene expression patterns of SST and PVALB interneurons

## Core question

Are the acute neural and behavioral effects of ketamine uni-dimensional (reflecting a single mechanism acting uniformly) or multi-dimensional (reflecting multiple axes of variation with substantial inter-individual differences), and can these dimensions be linked to downstream molecular mechanisms involving specific interneuron subtypes?

## Motivation / gap

- Ketamine is one of the most promising therapies for treatment-resistant depression, yet only ~65% of patients respond to a single infusion -- understanding individual variability is critical for precision medicine
- Most prior resting-state studies of ketamine used seed-based approaches requiring a priori region selection, potentially missing distributed system-level effects
- Inconsistent findings in the literature (e.g., contradictory thalamo-cortical connectivity results) may stem from unexamined inter-individual variability rather than true population-level disagreement
- The gap between ketamine's molecular mechanisms (NMDA receptor antagonism) and its systems-level neural and behavioral effects remains largely unbridged
- No existing framework connects behavioral symptom variation to distinct neural connectivity gradients at the single-subject level

## Core contribution (bullet form)

- Identified 5 significant principal components of ketamine-induced change in global brain connectivity (delta-GBC) in 40 healthy participants, collectively capturing 42.1% of total variance, demonstrating the multi-dimensional nature of ketamine's neural effects
- Showed that ketamine produces higher effective dimensionality (12.8 +/- 0.7) compared to LSD (8.7 +/- 0.3) and psilocybin (8.6 +/- 0.3), as measured by one-way ANOVA (F(2,60) = 564, p < 0.001)
- Demonstrated that the principal neural gradient (PC1 delta-GBC map) matches cortical gene expression patterns of somatostatin (SST) and parvalbumin (PVALB) interneurons, implicating these cell types in ketamine's acute effects
- Found that behavioral symptoms of ketamine are also multi-dimensional (3 significant behavioral PCs capturing variation across PANSS and cognition), and these behavioral dimensions map onto distinct neural connectivity gradients
- Resolved neuro-behavioral relationships at the single-subject level, showing that individual behavioral PC scores predict unique delta-GBC spatial patterns

## Method in brief

A double-blind placebo-controlled crossover study was conducted with 40 healthy participants who received acute ketamine (initial bolus 0.23 mg/kg, continuous infusion 0.58 mg/kg/hour). Resting-state fMRI data were collected under both placebo and ketamine conditions. Brain data were parcellated into 718 functionally-defined parcels, global brain connectivity (GBC) was computed for each parcel, and a delta-GBC map (ketamine minus placebo) was created per participant. PCA was then performed on this 718 x 40 matrix to identify the principal axes of neural variation.

Behavioral effects were assessed using the PANSS (positive, negative, general symptom subscales) and a spatial working memory task. A separate PCA was performed on normalized behavioral measures to identify the principal axes of symptom variation. Neuro-behavioral mapping was accomplished by regressing each participant's behavioral PC score onto their delta-GBC map. Gene expression analyses used the Allen Human Brain Atlas (AHBA) mapped via GEMINI-DOT to cortical parcels, with spatial correlations computed between neural PC maps and gene expression topographies across ~17,000 genes, followed by gene set enrichment analysis. Effective dimensionality was compared across ketamine, LSD, and psilocybin using previously published datasets.

## Target venue

eLife
