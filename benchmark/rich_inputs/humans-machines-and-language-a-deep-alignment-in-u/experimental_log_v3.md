# Experimental Log: Finding Structure During Incremental Speech Comprehension

## Participants

| Experiment | n | Age range | Mean age | Females | Notes |
|-----------|---|-----------|----------|---------|-------|
| EMEG main experiment | 16 (1 excluded) | 19-38 years | 26.5 years | 7 | 1 excluded for sleepiness |
| Continuation pre-test 1 | 30 | 18-34 years | N/A | N/A | Native British English speakers |
| Continuation pre-test 2 | 18 | 18-34 years | N/A | N/A | Native British English speakers |

Pre-test participants did not participate in the main experiment.

---

## Stimulus Design

| Parameter | Value |
|-----------|-------|
| Sentence sets | 60 |
| Sentences per set | 2 (HiTrans + LoTrans) |
| Total sentences | 120 |
| Manipulation | Transitivity of first verb (Verb1) |
| HiTrans SCF probability for direct object | 0.71 +/- 0.16 |
| LoTrans SCF probability for direct object | 0.44 +/- 0.19 |
| HiTrans vs LoTrans transitivity difference | two-tailed two-sample t-test, t(117) = 8.45, p = 9.3 x 10^-14 |
| SCF source | VALEX |

### Example stimuli
- HiTrans: "The dog found in the park was covered in mud."
- LoTrans: "The dog walked in the park was covered in mud."

### Critical sentence positions
- Det: determiner
- SN: subject noun
- V1: Verb1
- PP1-PP3: prepositional phrase
- MV: main verb
- END: last word

---

## Pre-test Results (Figure 2)

### Continuation patterns after Verb1
- Direct object continuations: more likely in HiTrans (indicating transitive use)
- PP continuations: more likely in LoTrans (indicating intransitive use)

### Continuation patterns after prepositional phrase
- Main verb probability: lower in LoTrans sentences (listeners preferred Active interpretation in LoTrans)
- Neither pre-test resulted in complete separation between HiTrans and LoTrans; characterized by two overlapping probabilistic distributions

### Correlation with corpus-based measures (Figure 2D)
- Spearman rank correlation between lexical constraints and probabilistic interpretations
- Significance determined by 10,000 permutations
- PFDR < 0.05 corrected
- Human interpretative preference significantly correlated with constraints placed by subject noun and Verb1

---

## BERT Structural Probing (Figure 3)

| Parameter | Value |
|-----------|-------|
| BERT model | BERT-large |
| Total layers | 24 |
| Layers used | 12-16 |
| Best performing layer | 14 |
| Structural probing method | Hewitt and Manning (2019) |
| Context-free Verb1 parse depth (Passive) | 2 |
| Context-free Verb1 parse depth (Active) | 0 |

### BERT interpretative trajectory results (Figure 3D-E)
- HiTrans sentences: continuously moved toward Passive interpretation landmark after Verb1; significant distance change at main verb
- LoTrans sentences: initially approached Active landmark, reoriented to Passive at main verb; significant distance changes at both Verb1 and main verb
- Two-tailed two-sample t-test for distance changes: *: P < 0.05, **: P < 0.001 (error bars represent SEM)

### BERT correlation with constraints (Figure 4)
- From PP to MV: sentences closer to Passive landmark have higher Verb1 transitivity, higher Passive index, lower Active index
- Sentences closer to Active landmark: higher Active index, lower Passive index
- Spearman correlation, permutation test, PFDR < 0.05 (corrected for all BERT layers)
- Results shown from layer 14 (see Appendix 1 figures 4-6 for all layers)
- BERT structural interpretations correlated with main verb probability from continuation pre-test

---

## EMEG Acquisition and Processing

### MEG Parameters

| Parameter | Value |
|-----------|-------|
| System | Neuromag Vector View (Elekta, Helsinki) |
| Magnetometers | 102 |
| Planar gradiometers | 204 |
| Sampling rate | 1 kHz |

### EEG Parameters

| Parameter | Value |
|-----------|-------|
| Electrodes | 70 Ag-AgCl (ESACYCAP GmbH) |
| Sampling rate | 1 kHz |

### Structural MRI

| Parameter | Value |
|-----------|-------|
| Scanner | Siemens Prisma 3T |
| Sequence | T1-weighted MPRAGE |
| Resolution | 1 mm isotropic |

### EMEG Preprocessing

| Parameter | Value |
|-----------|-------|
| Low-pass filter | 40 Hz |
| High-pass filter | 0.5 Hz |
| Filter type | 5th order bidirectional Butterworth |
| Software | SPM12 |
| Downsampled rate | 200 Hz |

### Trial Structure

| Parameter | Value |
|-----------|-------|
| Fixation cross duration | 750-1250 ms (mean 1000 ms) |
| Sound delivery delay | 26 ms +/- 2 ms |
| Post-sentence silence | 1000 ms |
| Blink cue duration | 1400 ms |
| Hearing test | Conducted before main experiment |
| Block/trial order | Pseudorandomized across participants |

---

## ssRSA Analysis (Figures 5-6)

### Searchlight parameters

| Parameter | Value |
|-----------|-------|
| Spatial radius | 10 mm |
| Temporal radius | 30 ms (60 ms sliding window) |
| Epoch length | 600 ms each |
| Baseline correction | -200 to 0 ms relative to sentence onset |
| Data RDM | 120 x 120 (60 HiTrans + 60 LoTrans) |
| Distance metric | Pearson correlation distance (1 - Pearson's r) |

### Cluster-based permutation test thresholds

| Parameter | Value |
|-----------|-------|
| Permutations | 5,000 nonparametric |
| Vertex-wise threshold | P < 0.01 |
| Cluster-wise threshold | P < 0.05 |

---

## ssRSA Results: Neural Dynamics (Figure 6)

### BERT parse depth vector effects

| Epoch | Brain regions | Timing |
|-------|---------------|--------|
| Verb1 | Bilateral frontal, anterior-to-middle temporal | From V1 onset to uniqueness point |
| Preposition (PP1) | Left fronto-temporal | After preposition recognition |
| Main verb (MV) | Left fronto-temporal + left prefrontal + left inferior parietal | After main verb recognition |

### Interpretative mismatch effects

| Epoch | Preferred interpretation | Regions | Cluster-wise P |
|-------|------------------------|---------|----------------|
| Verb1 | Active | Bilateral | < 0.05 |
| Preposition | Passive | Left fronto-temporal | < 0.05 |
| Main verb | Passive | Left fronto-temporal | 0.06 (marginal) |

Most sustained effects: left inferior frontal gyrus (IFG) and anterior temporal lobe (ATL).

---

## Structural Ambiguity Resolution (Figure 7)

### BERT Verb1 parse depth change at main verb

| Measure | Brain regions | Timing | Cluster-wise P |
|---------|---------------|--------|----------------|
| V1 parse depth change | Left posterior temporal, inferior parietal | After MV uniqueness point, extending anteriorly | < 0.05 |
| Updated V1 parse depth | Left anterior temporal, extending right posterior temporal/parietal | After MV offset | < 0.05 |
| Overlap between change and updated | Left temporal | Seamless transition from posterior to anterior | < 0.05 |

Left hippocampus activated for both V1 parse depth measures after main verb recognition.

---

## Multifaceted Constraints (Figure 8)

### Subject noun thematic role effects

| Measure | Epoch | Brain regions | Timing relative to BERT effects |
|---------|-------|---------------|--------------------------------|
| SN agenthood | Preposition (PP1) | Bilateral | Preceded BERT parse depth effects |
| SN patienthood | Main verb (MV) | Bilateral | Preceded BERT parse depth effects |

### Non-directional interpretive coherence (Figure 8C)
- Effects after MV onset in both hemispheres until MV offset
- Most sustained regions: left ATL, angular gyrus (AG), precuneus (default mode network regions)
- Cluster-based permutation test: vertex-wise P < 0.01, cluster-wise P < 0.05

### Passive index (Figure 8D)
- Right anterior fronto-temporal regions after MV recognition
- Cluster-based permutation test: vertex-wise P < 0.01, cluster-wise P < 0.05

### Granger causality analysis (Figure 8E)
- NMF decomposition of whole-brain ssRSA results
- Directed connections found only from Passive index components to BERT parse depth vector components
- Information flow: right hemisphere Passive index to left hemisphere BERT parse depth
- Permutation test: PFDR < 0.05

---

## Comparisons: BERT vs Corpus/Behavioral Measures

| Epoch | Corpus/behavioral measure tested | Result |
|-------|----------------------------------|--------|
| Verb1 | Verb1 transitivity (corpus + human continuations) | No significant model fits |
| PP1 | PP continuation probability (behavioral) | No significant model fits |
| MV | MV continuation probability (behavioral) | No significant model fits |
| All epochs | BERT parse depth after controlling for behavioral variance | Effects largely unchanged |

BERT structural measures outperformed corpus-based and behavioral measures in fitting neural activity across all epochs.

---

## Methods Parameters

### Corpus-based measures

| Measure | Description |
|---------|-------------|
| Subject noun agenthood | Likelihood of SN being interpreted as agent |
| Subject noun patienthood | Likelihood of SN being interpreted as patient |
| Verb1 transitivity | Likelihood of Verb1 taking direct object (from VALEX) |
| Active index | Coherence between high SN agenthood and low V1 transitivity |
| Passive index | Coherence between high SN patienthood and high V1 transitivity |
| Non-directional index | Degree of interpretative coherence regardless of structure preferred |

### BERT structural probing

| Parameter | Value |
|-----------|-------|
| Model | BERT-large (24 layers) |
| Input method | Word-by-word incremental |
| Probing technique | Structural probing (Hewitt and Manning 2019) |
| Selected layers | 12-16 (best at 14) |
| Output | Parse depth vector per incremental input |

### Granger Causality Analysis

| Parameter | Value |
|-----------|-------|
| Decomposition method | Non-negative matrix factorization (NMF) |
| Input | Whole-brain ssRSA model fits |
| Epoch | Main verb |
| Statistical test | Multivariate Granger causality with permutation test |
| Correction | PFDR < 0.05 |

---

## Statistics Summary

1. **Two-tailed two-sample t-test** - Verb transitivity comparison (t(117) = 8.45, p = 9.3 x 10^-14); BERT distance changes between landmarks (*: P < 0.05, **: P < 0.001)
2. **Spearman rank correlation** - Correlations between BERT measures, corpus measures, and behavioral data (permutation test, PFDR < 0.05)
3. **Cluster-based permutation test** - ssRSA neural results (5,000 permutations, vertex-wise P < 0.01, cluster-wise P < 0.05)
4. **Permutation test (10,000 permutations)** - Pre-test correlations (PFDR < 0.05)
5. **Multivariate Granger causality analysis** - Directed information flow between NMF components (permutation test, PFDR < 0.05)
6. **Non-negative matrix factorization (NMF)** - Decomposition of whole-brain ssRSA fits
7. **Representational similarity analysis (RSA)** - Correlation between model RDMs and data RDMs (Pearson correlation distance)
