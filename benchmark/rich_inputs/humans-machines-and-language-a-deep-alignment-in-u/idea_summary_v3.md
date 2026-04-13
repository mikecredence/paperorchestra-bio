## Working title
Finding structure during incremental speech comprehension

## Core question
How does the brain incrementally construct structured interpretations from spoken sentences under multifaceted probabilistic constraints, and can deep language model (BERT) structural representations reveal the spatiotemporal neural dynamics of this process?

## Motivation / gap
- Previous neuroimaging studies of language structure primarily focused on syntax in isolation, contrasting grammatical vs ungrammatical sentences or manipulating syntactic complexity, rather than studying the real-time construction of coherent interpretations
- The constraint-based approach to sentence processing proposes that comprehension is governed by multiple concurrent probabilistic constraints (syntax, semantics, world knowledge), but modeling the dynamic interplay among these constraints at the sentence level has been challenging
- While deep language models show overall congruence with brain language representations, moving beyond comparing entire model hidden states to brain activity requires probing specific contents from DLMs
- The neural dynamics underpinning incremental construction of structured interpretation from spoken sentences, including when and where coherent interpretations emerge through evaluation and integration of multifaceted constraints, remain unclear
- It is unknown how linguistic constraints (verb transitivity) and non-linguistic world knowledge (thematic role preferences) jointly drive structural interpretation in the brain

## Core contribution (bullet form)
- Designed 60 sets of sentences contrasting verb transitivity (HiTrans: SCF probability for direct object 0.71 +/- 0.16 vs LoTrans: 0.44 +/- 0.19; two-tailed two-sample t-test, t(117) = 8.45, p = 9.3 x 10^-14) and used BERT structural probing (layers 12-16, best at layer 14) to extract word-by-word parse depths
- ssRSA revealed incremental BERT parse depth vectors fit brain activity in all three critical epochs (Verb1, preposition, main verb), with cluster-based permutation tests at vertex-wise P < 0.01 and cluster-wise P < 0.05
- Demonstrated a shift from bilateral fronto-temporal regions to left-lateralized regions as sentences unfold, with most sustained effects in left inferior frontal gyrus (IFG) and anterior temporal lobe (ATL)
- Identified sequential activations in left lateral temporal regions updating structured interpretation during syntactic ambiguity resolution (Figure 7; cluster-wise P < 0.05)
- Granger causality analysis revealed directed information flow from right hemisphere Passive index components to left hemisphere BERT parse depth components (permutation test, PFDR < 0.05), suggesting world knowledge influences structural interpretation
- BERT structural measures outperformed corpus-based and behavioral measures in fitting neural activity; marginal significance for Passive interpretation mismatch in main verb epoch (cluster-wise P = 0.06)

## Method in brief
We constructed 60 sets of sentences with contrasting linguistic structures, each containing a HiTrans and LoTrans version differing only in verb transitivity. Two continuation pre-tests (30 and 18 participants, aged 18-34 years) established human interpretative preferences. The main EMEG experiment included 16 participants (aged 19-38, mean 26.5 years; 7 females; 1 excluded for sleepiness). MEG data were collected using a Neuromag Vector View system (102 magnetometers, 204 planar gradiometers) at 1 kHz sampling rate. Simultaneous EEG used 70 Ag-AgCl electrodes at 1 kHz. Structural MRI (T1-weighted MPRAGE, 1 mm isotropic) was acquired on a Siemens Prisma 3T scanner for source localization. EMEG data were filtered (0.5-40 Hz, 5th order bidirectional Butterworth), downsampled to 200 Hz, and source-localized. Each trial included a fixation cross (750-1250 ms, mean 1000 ms), spoken sentence (26 ms +/- 2 ms delay in sound delivery), 1000 ms silence, and 1400 ms blink cue. Three 600-ms epochs were time-locked to Verb1 onset, preposition onset, and main verb onset, with baseline correction using -200 to 0 ms relative to sentence onset.

BERT structural measures were extracted using a structural probing technique trained on BERT-large (24 layers), selecting layers 12-16 with best performance at layer 14. Spatiotemporal searchlight RSA (ssRSA) used a 10-mm spatial radius and 30-ms temporal radius (60-ms sliding window) across source-localized EMEG. Model RDMs from BERT parse depths and corpus-based measures were correlated with 120 x 120 data RDMs (Pearson correlation distance). Cluster permutation tests used 5,000 nonparametric permutations with vertex-wise P < 0.01 and cluster-wise P < 0.05. Granger causality analysis based on non-negative matrix factorization (NMF) components of whole-brain ssRSA results investigated directed connections between interpretative coherence and structural representations.

## Target venue
eLife
