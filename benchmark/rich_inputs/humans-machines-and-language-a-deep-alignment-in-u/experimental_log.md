# Experimental Log: Finding structure during incremental speech comprehension

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsWe constructed 60 sets of sentences with varying sentential structures (see Methods) and presented them to human listeners.
- In each stimulus set, there are two target sentences differing only in the transitivity of the first verb (Verb1) encountered, i.e., how likely it is that Verb1 takes a direct object [see (1) and (2) below and Figure 1]:
The dog found in the park was covered in mud.The dog walked in the park was cov
- biorxiv;2021.10.25.465687v4/FIG1F1fig1Figure 1.Example spoken sentence stimuli and plausible structured interpretations.The two target sentences in each set differ only in the transitivity of the first verb (Verb1).
- The interpretative preference hinges on the likelihood of the SN acting as an agent or a patient (i.e., its thematic role) in conjunction with the transitivity of Verb1.
- As the sentence progresses to the prepositional phrase, a combination of higher SN agenthood and greater Verb1 intransitivity (i.e., a higher Active index) generally favors an Active interpretation.
- Conversely, increased SN patienthood coupled with higher Verb1 transitivity (i.e., a higher Passive index) may lead to a Passive interpretation.
- All images were generated using Midjourney for illustrative purposes.In the first sentence, Verb1 (i.e., “found”) has high transitivity (HiTrans) and strongly prefers a direct object (e.g., ball), while in the second sentence, Verb1 (i.e., “walked”) has relatively low transitivity (LoTrans) and is o
- Critically, (a) the structural interpretation of these sentences is ambiguous at the point Verb1 is encountered and (b) the preferred human resolution of this ambiguity depends on the real-time integration of linguistic and non-linguistic constraints as more of the sentence is heard.
- In the example above, the sequence “The dog found…” could initially have either an Active interpretation – where the dog has found something, or a Passive interpretation – where the dog is found by someone (Figure 1).
- Similarly, the sequence “The dog walked…”, where walk is primarily used as an intransitive verb (without a direct object), could also bias the listener to an Active interpretation, where the dog is doing the walking, rather than the less frequent Passive interpretation where someone is taking the do
- It also depends on non-linguistic information, i.e., how likely the subject is (or is not) to adopt the Active (agent) role to perform the specified action (Dowty 1991; Marslen-Wilson et al.
- 1993), that is, “thematic role” properties of the subject noun.
- So, regardless of Verb1 transitivity, the Active interpretation should be more strongly favored in “The king found/walked…” given the higher agenthood of the “king” and thus the greater implausibility of a Passive interpretation involving a “king” relative to a “dog”.
- Hence, the word-by-word interpretation of the sentential structure – and of the real-world event structure evoked by this interpretation – is determined by the constraints jointly placed by the subject noun and Verb1, which is manifested by the interpretative coherence between non-linguistic world k
- Specifically, the Passive interpretation will become more preferred in a HiTrans sentence, given the absence of an expected direct object for the highly transitive Verb1, so Verb1 tends to be interpreted as a passive verb [i.e., the head of a reduced relative clause in “The dog (that was) found in t
- Conversely, in a LoTrans sentence, the Active interpretation of Verb1 is strengthened by the incoming prepositional phrase, which is in accord with the verb’s intransitive use and the event conjured up by the sequence of words heard so far (e.g., “The dog walked in the park…”).
- However, with the appearance of the actual main verb (e.g., “was covered” in the example sentences), the Active interpretation of Verb1 as the main verb will be completely rejected, which resolves the potential ambiguity and confirms the Passive interpretation in both HiTrans and LoTrans sentences.I
- For example, the incremental building, maintenance and update of sentential structure over time might primarily involve activity in the fronto-temporal regions (Friederici 2012), while estimating the plausibility of the event interpreted from the sentence with prior knowledge of the world may elicit

## Figure Descriptions

### Figure 1.
Example spoken sentence stimuli and plausible structured interpretations.The two target sentences in each set differ only in the transitivity of the first verb (Verb1). Each sentence has two possible structured interpretations before the actual main verb is presented: an active interpretation, where

### Figure 2.
Human incremental structural interpretations derived from continuation pre-tests.(A) An example set of target sentences differing only in the transitivity of Verb1, HiTrans: high transitivity, LoTrans: low transitivity. Det: determiner, SN: subject noun, V1: Verb1, PP1-PP3: prepositional phrase, MV:

### Figure 3.
Incremental interpretation of sentential structure by BERT.(A) Context-free dependency parse trees of two plausible structural interpretations. Left: Passive interpretation where V1 is the head of a reduced relative clause. Right: Active interpretation where V1 is the main verb. (B) Incremental inpu

### Figure 4.
Correlation between incremental BERT structural measures and explanatory variables.BERT structural measures include (A, B) BERT interpretative mismatch represented by each sentence’s distance from the two landmarks in model space (Figure 3D); (C, D) Dynamic updates of BERT interpretative mismatch re

### Figure 5.
Illustration of the pipeline for ssRSA.For each pair of sentences, we extract their BERT or corpus-based measures and calculate the dissimilarity between these measures, resulting in a model representational dissimilarity matrix (RDM). Meanwhile, we also extract the neural activity recorded while pa

### Figure 6.
Neural dynamics underpinning the emerging structure and interpretation of an unfolding sentence. (A-C)ssRSA results of BERT parse depth vector up to Verb1 (V1), the preposition (PP1) and the main verb (MV) in epochs separately time-locked to their onsets. (D-F) ssRSA results of the mismatch for the 

### Figure 7.
Neural dynamics updating the incremental structural interpretation. (A)ssRSA results of BERT Verb1 (V1) parse depth change at the main verb (MV) relative to the parse depth of V1 when it is first encountered. (B) ssRSA results of the updated BERT V1 parse depth when the input sentence reaches the MV

### Figure 8.
Neural dynamics of multifaceted probabilistic constraints underpinning incremental structural interpretations.(A, B) ssRSA results of SN agenthood and SN patienthood (i.e., plausibility of SN being the agent or the patient of V1) in PP1 and MV epochs separately. (C) ssRSA results of non- directional

## References
Total references in published paper: 71

### Key References (from published paper)
- Ambiguity in sentence processing (, 1998)
- Events as intersecting object histories: A new theory of event representation (, 2019)
- The {CELEX} lexical data base on {CD-ROM} (, 1993)
- A map of object space in primate inferotemporal cortex (, 2020)
- The MVGC multivariate Granger causality toolbox: a new approach to Granger-causal inference (, 2014)
- The WaCky wide web: a collection of very large linguistically processed web-crawled corpora (, 2009)
- Deep Learning for AI (, 2021)
- Effects of event knowledge in processing verbal arguments (, 2010)
- Using cognitive psychology to understand GPT-3 (, 2023)
- Language models are few-shot learners (, 2020)
- Deep language algorithms predict semantic comprehension from brain activity (, 2022)
- Evidence of a predictive coding hierarchy in the human brain listening to speech (, 2023)
- Brains and algorithms partially converge in natural language processing (, 2022)
- Decoding the Real-Time Neurobiological Properties of Incremental Semantic Interpretation (, 2021)
- The neuroconnectionist research programme (, 2023)
- Two Distinct Neural Timescales for Predictive Speech Processing (, 2019)
- Thematic Proto-Roles and Argument Selection (, 1991)
- The multiple-demand (MD) system of the primate brain: mental programs for intelligent behaviour (, 2010)
- Finding Structure in Time (, 1990)
- Learning and development in neural networks: the importance of starting small (, 1993)
- Structures, Not Strings: Linguistics as Part of the Cognitive Sciences (, 2015)
- Syntactic processing: evidence from Dutch (, 1987)
- Making and correcting errors during sentence comprehension: Eye movements in the analysis of structu (, 1982)
- The cortical language circuit: from auditory perception to sentence comprehension (, 2012)
- The brain differentiates human and non-human grammars: functional localization and structural connec (, 2006)
- Intermediate acoustic-to-semantic representations link behavioral and neural responses to natural so (, 2023)
- Shared computational principles for language processing in humans and deep language models (, 2022)
- Multivariate pattern analysis for MEG: A comparison of dissimilarity measures (, 2018)
- Interpreting magnetic fields of the brain: minimum norm estimates (, 1994)
- A hierarchy of linguistic predictions during natural language comprehension (, 2022)

## Ground Truth Reference
- Figures: 8
- Tables: 0
- References: 71