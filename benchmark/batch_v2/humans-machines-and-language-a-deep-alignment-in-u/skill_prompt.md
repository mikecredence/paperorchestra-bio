Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

## Working title

Neural dynamics of incremental sentence structure building revealed by BERT parse depth and EMEG source imaging

## Core question

How does the brain incrementally construct structured interpretations of spoken sentences, integrating multiple types of probabilistic constraints (syntactic, semantic, world knowledge) in real time, and can deep language model representations capture this process?

## Motivation / gap

- Previous neuroimaging studies of sentence structure focused narrowly on syntax (grammatical vs. ungrammatical, syntactic complexity manipulations, artificial grammars), ignoring the broader constraint landscape
- The constraint-based approach to sentence processing posits that multiple probabilistic constraints (syntax, semantics, world knowledge) jointly drive interpretation, but modeling their dynamic interplay has been challenging
- Deep language models like BERT implicitly learn these multifaceted constraints from data, but their utility as computational tools for probing neural dynamics of structured interpretation is underexplored
- It remains unclear where and when in the brain coherent structured interpretations emerge from the evaluation and integration of diverse constraints
- Prior work lacked spatiotemporal resolution needed to track incremental structure building at the word-by-word level

## Core contribution (bullet form)

- Designed 60 sentence sets with controlled structural ambiguity (high-transitivity vs. low-transitivity Verb1), validated by behavioral pre-tests showing probabilistic human interpretive preferences
- Extracted incremental BERT parse depth vectors that capture context-sensitive structural representations, showing they correlate with corpus-based transitivity/agenthood measures (Spearman rho significant at PFDR < 0.05)
- Used searchlight representational similarity analysis (ssRSA) on EMEG source-space data (16 participants) to reveal spatiotemporal dynamics of structure building
- Found a shift from bilateral frontal-temporal regions to left-lateralized regions as sentence structure is established
- Identified sequential left lateral temporal activations that update structural interpretation when syntactic ambiguity is resolved at the main verb
- Demonstrated right-hemisphere influence of lexical interpretive coherence over left-hemisphere structural representations

## Method in brief

The study constructed 60 sets of spoken sentences (360 total across 6 conditions) where two target sentences per set differed only in Verb1 transitivity (high vs. low). Behavioral pre-tests at two gating points (after Verb1 and after the prepositional phrase) confirmed that listeners form probabilistic structural interpretations modulated by verb transitivity and subject noun agenthood. Corpus-based measures (Active index, Passive index) were derived from subcategorization frame probabilities and thematic role plausibility.

BERT (base, uncased) was used as a structural probing model: sentences were input incrementally word-by-word, and a trained probe extracted parse depth vectors at each position. These BERT parse depths captured context-sensitive structural preferences that correlated with both corpus-based lexical constraints and human behavioral data. The parse depth trajectories in model space showed systematic movement toward passive or active interpretation landmarks depending on sentence type.

Brain activity was recorded using combined electro/magnetoencephalography (EMEG) from 16 participants listening to the sentences. Source-space searchlight RSA (ssRSA) compared model representational dissimilarity matrices (from BERT parse depths and corpus-based measures) against neural RDMs computed from spatiotemporal searchlights across the cortex. Cluster-based permutation testing (vertex-wise P < 0.01, cluster-wise P < 0.05) identified significant spatiotemporal clusters.

## Target venue

eLife


## Experimental Log

# Experimental Log: Incremental Sentence Structure Building with BERT and EMEG

## Study Design and Participants

| Parameter | Value |
|-----------|-------|
| Participants enrolled | 17 |
| Participants analyzed | 16 (1 excluded for sleepiness) |
| Age range | 19-38 years |
| Mean age | 26.5 years |
| Female participants | 7 |
| Handedness | All right-handed |
| Native language | British English |
| Neurological conditions | None |
| Recording modality | Combined EEG/MEG (EMEG) |

## Stimulus Design

| Parameter | Value |
|-----------|-------|
| Number of sentence sets | 60 |
| Sentences per set | 6 |
| Total sentences | 360 |
| Sentence types | UNA, HiTrans, LoTrans, PAS, DO1, DO2 |
| Key manipulation | Verb1 transitivity (high vs. low) |
| Subject noun phrase | Single-word determiner + noun |
| Critical positions | Det, SN, V1, PP1-PP3, MV, END |

### Sentence Conditions

| Condition | Abbreviation | Key Feature |
|-----------|-------------|-------------|
| Unambiguous | UNA | Verb1 unambiguously heads relative clause |
| High transitivity | HiTrans | Verb1 strongly prefers direct object |
| Low transitivity | LoTrans | Verb1 is optionally transitive |
| Passive | PAS | Contains passive construction |
| Direct object 1 | DO1 | Contains direct object (variant 1) |
| Direct object 2 | DO2 | Contains direct object (variant 2) |

### Verb1 Transitivity Properties

| Property | HiTrans | LoTrans | Statistical Test |
|----------|---------|---------|-----------------|
| SCF probability for direct object (VALEX) | 0.71 +/- 0.16 | 0.44 +/- 0.19 | t(117) = 8.45, p = 9.3e-14 |
| Structural ambiguity at Verb1 | Yes | Yes | -- |
| Expected initial interpretation bias | Passive (relative clause head) | Active (main verb) | -- |

## Behavioral Pre-test Results

Two gating pre-tests were conducted: (1) continuation after Verb1, and (2) continuation after the prepositional phrase.

### Pre-test 1: Continuations After Verb1

| Measure | HiTrans Pattern | LoTrans Pattern |
|---------|----------------|-----------------|
| Probability of direct object continuation | Higher | Lower |
| Probability of PP continuation | Lower | Higher |
| Interpretation | Transitive use of Verb1 preferred | Intransitive use of Verb1 preferred |

### Pre-test 2: Continuations After Prepositional Phrase

| Measure | HiTrans Pattern | LoTrans Pattern |
|---------|----------------|-----------------|
| Probability of main verb continuation | Higher | Lower |
| Preferred interpretation | Passive (Verb1 = relative clause head) | Active (Verb1 = main verb) |
| Distribution separation | Overlapping (probabilistic) | Overlapping (probabilistic) |

- Fig 2B shows direct object continuations are more likely for HiTrans after Verb1, while PP continuations show the opposite pattern
- Fig 2C shows lower main verb probability in LoTrans continuations after the PP, indicating Active interpretation preference
- Neither pre-test achieved complete separation between HiTrans and LoTrans -- both characterized by overlapping probabilistic distributions

### Corpus-Based Measures and Behavioral Correlations

| Corpus Measure | Description | Correlation with Pre-test |
|---------------|-------------|--------------------------|
| SN agenthood | Likelihood of subject noun being interpreted as agent | Significant (PFDR < 0.05) |
| SN patienthood | Likelihood of subject noun being interpreted as patient | Significant (PFDR < 0.05) |
| Verb1 transitivity | SCF probability for direct object from VALEX/CELEX | Significant (PFDR < 0.05) |
| Active index | Coherence for active interpretation (SN agenthood x V1 intransitivity) | Significant (PFDR < 0.05) |
| Passive index | Coherence for passive interpretation (SN patienthood x V1 transitivity) | Significant (PFDR < 0.05) |

- Fig 2D: Spearman rank correlations between corpus-based lexical constraints and probabilistic interpretations in both pre-tests. Black dots indicate significance by 10,000 permutations (PFDR < 0.05 corrected).

## BERT Structural Probing

| Parameter | Value |
|-----------|-------|
| Model | BERT (base, uncased) |
| Input mode | Incremental (word-by-word) |
| Output | Parse depth vectors at each word position |
| Training task | Structural probing (predict dependency parse depths) |
| Parse tree type | Dependency parse tree (de Marneffe et al. 2006) |
| Number of BERT layers tested | 12 (layer selection per analysis) |

### BERT Parse Depth Properties

| Property | Context-Free Parse | BERT Parse |
|----------|-------------------|------------|
| Sensitivity to lexical content | No (same for same position/structure) | Yes (varies with specific words) |
| Sensitivity to transitivity | No | Yes (reflects probabilistic bias) |
| Incremental updates | No (fixed tree) | Yes (updates as words are added) |
| Captures constraint interplay | No | Yes (trained on distributional data) |

### BERT Structural Measures Extracted

| Measure | Description |
|---------|-------------|
| Parse depth vector | Depths of all words at each incremental position |
| Interpretive mismatch (Passive) | Distance from passive landmark in model space |
| Interpretive mismatch (Active) | Distance from active landmark in model space |
| Dynamic update (Passive) | Movement toward passive landmark |
| Dynamic update (Active) | Movement toward active landmark |
| PC1, PC2 of parse depth | First two principal components of parse depth vectors |
| V1 parse depth change at MV | Change in Verb1 parse depth when main verb is encountered |

### BERT Measure Correlations with Explanatory Variables

| BERT Measure | Correlates with | Direction |
|-------------|----------------|-----------|
| Passive mismatch at V1 | V1 transitivity | Decreases with higher transitivity |
| Active mismatch at V1 | V1 transitivity | Increases with higher transitivity |
| Passive mismatch at PP | PP fit + transitivity | Further modulated by PP content |
| Active mismatch at PP | PP fit + transitivity | Further modulated by PP content |
| V1 parse depth change at MV | Transitivity + agenthood | Larger change for HiTrans |

- Fig 3D: Incremental trajectories in model space (Det, SN, V1 parse depths) show systematic separation between HiTrans and LoTrans by the PP
- Fig 3E: Distance from Passive and Active landmarks changes as the sentence unfolds, with separation emerging at PP and consolidating at MV
- Fig 4: Correlations between BERT structural measures and corpus-based explanatory variables confirm BERT captures the constraint-based dynamics

## EMEG Recording and Analysis Parameters

| Parameter | Value |
|-----------|-------|
| Recording system | Combined EEG/MEG (EMEG) |
| Source reconstruction method | Source-space analysis |
| Analysis method | Searchlight representational similarity analysis (ssRSA) |
| Searchlight type | Spatiotemporal in EMEG source space |
| Statistical test | Cluster-based permutation test |
| Vertex-wise threshold | P < 0.01 |
| Cluster-wise threshold | P < 0.05 |
| Time-locking epochs | V1 onset, PP1 onset, MV onset |

## Neural Dynamics Results

### Emerging Structure at Verb1 (Fig 6A)

| Finding | Details |
|---------|---------|
| BERT parse depth at V1 | Bilateral frontal-temporal activation |
| Hemispheric pattern | Bi-hemispheric (both left and right) |
| Temporal window | Shortly after V1 onset |
| Brain regions | Lateral frontal and temporal cortex bilaterally |

### Emerging Structure at Prepositional Phrase (Fig 6B)

| Finding | Details |
|---------|---------|
| BERT parse depth at PP1 | Activation extends in temporal cortex |
| Hemispheric shift | Beginning shift toward left lateralization |
| Interpretive mismatch | Right hemisphere shows sensitivity to lexical coherence |
| Temporal window | After PP1 onset |

### Structure at Main Verb (Fig 6C)

| Finding | Details |
|---------|---------|
| BERT parse depth at MV | Left-lateralized temporal and frontal regions |
| Hemispheric pattern | Predominantly left hemisphere |
| Interpretive resolution | Structure disambiguation occurs here |
| Brain regions | Left lateral temporal cortex dominant |

### Interpretive Mismatch Neural Correlates (Fig 6D-F)

| Epoch | Preferred Interpretation Mismatch | Brain Regions |
|-------|----------------------------------|---------------|
| V1 | Passive mismatch (BERT layer in parentheses) | Bilateral frontal-temporal |
| PP1 | Updated mismatch reflecting PP constraints | Bilateral with right hemisphere emphasis |
| MV | Resolved mismatch | Left-lateralized |

### Structural Update at Main Verb (Fig 7)

| Analysis | Significant Clusters | Brain Regions |
|----------|---------------------|---------------|
| V1 parse depth change at MV | Yes (cluster-based permutation, P < 0.05) | Left lateral temporal cortex |
| Updated V1 parse depth at MV | Yes | Left lateral temporal, overlapping with change effect |
| Spatiotemporal overlap (Fig 7C) | Sequential activations identified | Left temporal regions show sequential processing |

- Fig 7A: V1 parse depth change at MV is represented in left lateral temporal regions
- Fig 7B: Updated V1 parse depth at MV engages overlapping but extended left temporal regions
- Fig 7C: Overlap between the two effects confirms sequential update process

### Corpus-Based Constraint Neural Correlates (Fig 8)

| Measure | Epoch | Significant Effect | Brain Region |
|---------|-------|--------------------|-------------|
| SN agenthood | PP1 | Yes | Right hemisphere |
| SN patienthood | PP1 | Yes | Right hemisphere |
| SN agenthood | MV | Yes | Right hemisphere |
| SN patienthood | MV | Yes | Right hemisphere |
| Non-directional index | MV | Yes | Right hemisphere |
| Passive index | MV | Yes | Right hemisphere + left hemisphere |
| Active index | MV | Yes | Left hemisphere |

- Fig 8A-B: SN agenthood and patienthood are represented in right hemisphere regions at both PP1 and MV epochs
- Fig 8C: Non-directional interpretive coherence (regardless of preferred structure) activates right hemisphere at MV
- Fig 8D: Passive index (coherence for passive interpretation) engages both hemispheres at MV
- Fig 8E: Active index representation is left-lateralized

## Summary of Key Spatiotemporal Patterns

| Time Course | Hemispheric Pattern | Process |
|------------|-------------------|---------|
| V1 onset | Bilateral frontal-temporal | Initial structural representation |
| PP1 onset | Bilateral, beginning left shift | Structure refinement with PP constraints |
| MV onset | Left-lateralized temporal | Structural disambiguation and resolution |
| V1 to MV (lexical coherence) | Right hemisphere | Evaluation of interpretive coherence from lexical constraints |
| V1 to MV (structural update) | Left lateral temporal | Sequential update of structural interpretation |

## Key Statistical Methods

| Method | Application |
|--------|-------------|
| Representational similarity analysis (RSA) | Compare model RDMs to neural RDMs |
| Searchlight approach | Spatiotemporal scanning across cortex |
| Cluster-based permutation test | Correct for multiple comparisons |
| Spearman rank correlation | Corpus-behavioral measure correlations |
| 10,000 permutations | Significance testing for correlations |
| FDR correction | Multiple comparison correction (PFDR < 0.05) |
| Principal component analysis | Dimensionality reduction of BERT parse depths |

## Datasets and Resources

| Resource | Usage |
|----------|-------|
| CELEX database | Verb transitivity classification |
| Google n-gram corpus | Verb transitivity frequency |
| VALEX | Subcategorization frame probabilities |
| BERT (base, uncased) | Structural probing model |
| De Marneffe dependency parser | Parse tree ground truth for BERT training |
| EMEG source-space data | Neural activity recordings |

## Model Validation Summary

| Validation Step | Result |
|----------------|--------|
| BERT parse depths vs. corpus measures | Significant correlations (PFDR < 0.05) |
| BERT parse depths vs. human behavioral pre-tests | Consistent with probabilistic interpretations |
| BERT model space trajectories | Systematic HiTrans/LoTrans separation |
| Context-free vs. BERT parse | BERT captures lexical sensitivity absent in context-free |
| ssRSA neural effects | Multiple significant spatiotemporal clusters |
| Hemispheric lateralization pattern | Consistent with known language network organization |

