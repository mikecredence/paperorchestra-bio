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
