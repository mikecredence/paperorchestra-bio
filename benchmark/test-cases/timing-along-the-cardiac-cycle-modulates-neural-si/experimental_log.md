# Experimental Log: Timing along the cardiac cycle modulates neural signals of reward-based learning

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsStatistics of the reward environment predict learningParticipants carried out a reward-guided decision task inspired by previous credit assignment tasks 28,29.
- While participants performed the task, we recorded neural responses to heartbeats with EEG and ECG (Fig.1A) during the outcome which included a four-second period to ensure that multiple heart beats would be recorded (mean: 4.58, std+-0.85).
- There were three predictive schemes with high associations between cues and colours (highly predictive anticorrelated, highly predictive correlated, and variable predictive schemes) and one scheme with no associations between cues and colours (non-predictive scheme) (Fig.1C).biorxiv;2022.07.07.49894
- (a) task + cardiac-related neural signals (CRS) recorded at outcome for 4 sec -enough to get on average 3.5 CRSs (b) example of association between cues and predicted colour for one version of the task (anti-correlated blocks – see Methods) (c) prediction strengths for each block (d) model predictio
- A formal model comparison showed that the simpler prediction model, lacking any bias, outperformed the more complex version incorporating cue bias (BIC=362.1738, BIC=377.4045) and suggested that participants did not exhibit a bias towards one or other cue type.
- 1H).Grand average modulation of cardiac-related neural signals in learning-related dimensionsWe next looked for EEG signatures of the heartbeat evoked potential (HEP).
- Figure 2a presents the topographical characteristics of the HEP based on the averaged cardiac-related neural signals (CRSs) recorded during the outcome (see Methods for the construction of the CRS).
- A morphology analysis revealed that the HEP was widely distributed along fronto-central and centro-parietal areas including the following spatial regions (Fronto-central sites: F1, Fz, F2, FC1, FCz, CF2; Centro-parietal sites: C1, Cz, C2, CP1, CPz, CP2 as in Figure 2a).
- This approach has the advantage of looking at two orthogonal RL signals as seen in Figure 1H.
- The results of the cluster-based permutation analysis (see Methods) revealed an increased HEP amplitude for trials with negative signed PE in comparison to positive signed PE (Monte-Carlo p value = 0.004) between 198 and 252 milliseconds in the fronto-central sites (Figure 2b).
- The contrast between correct and incorrect trials revealed an HEP amplitude increase for correct trials (Monte-Carlo p value = 0.005) in the time range between 286 and 348 milliseconds in the centro-parietal sites (Figure 2c).
- When contrasting trials in the absolute PE domain, we found an increased HEP amplitude on the low surprising trials as opposed to the high surprising trials (Monte-Carlo p values < 0.003); these differences were observed in two clusters with latencies 222 - 252 milliseconds and 418 - 464 millisecond
- (a) Grand average waveforms across the scalp time-locked to the onset of the R-wave which is the biggest electrical wave generated during normal conduction (time 0 ms, see Methods).
- The set of electrodes clustered by ROIs (colour-coded) for the fronto-central and central-parietal electrodes are represented for further analyses (b-d) CRS waveforms across all trials following the onset of the R-wave (at time 0 ms) are shown separately for (b) positive and negative signed PEs for 
- The shaded areas represent the time windows during which the analyses were performed and the HEP typically takes place (0.1-0.6s).The CRS is related to trial-by-trial variation in the absolute PE dimension and not signed PERather than inspecting specific electrode averages, we next wanted to search 
- More specifically, for each participant, we used the average of the CRS for each outcome (see Fig.1a) and calculated the linear weights associated with each electrode that maximally separated (1) positive and negative signed PEs and (2) high versus low magnitude of absolute PE (i.e.
- This method has been well established in EEG data analysis 30,31.
- 2) – between very high versus very low absolute PE outcomes.
- This component peaked in the time range 100–300 milliseconds after the R-wave (Fig.
- On the other hand, we did not observe any CRS component discriminating between positive and negative PEs (Fig.3f).
- By contrast, as noted, a grand average response difference was identified in the ERP in fronto-central electrodes (Fig.2b).
- In conjunction, the two results suggest that there is, on average, a difference in cardiac related signals when the valence of the signed PE is positive or negative31 but that trial-by-trial variability in the heart-related CRS does not reliably covary on a trial-by-trial basis with the trial-by-tri
- low absolute PE [0.25 – 0.50]; and high absolute PE [0.5 – 0.75]) which were not originally used to train the classifier (also called the “unseen” data).
- 3c, blue: intermediate categories, grey: categories used for discrimination) confirming the linear relationship between the CRS-absolute PE component and its model-based counterpart (test on the left-out data: t31 =-7.3027; p=3.22e-8) and also the generalisability and robustness of our machine learn
- Applying this method, we showed that only the first CRS after feedback contained information about absolute PE that could be revealed with machine learning techniques, in the range 100–300 milliseconds after heart beat onset (Fig.
- Naturally, as the diastole phase is longer on average than the systole phase, we expect a higher number of outcomes presented during the diastole phase (m=65±5 and 54±5 for diastole and systole, respectively).
- predictive or non-predictive) employed in the task (see Methods; systole F3=0.2, p=0.893; diastole F3=0.2, p=0.896, supplementary Fig.3a) and were associated with similar levels of overall reward received in the task (t31=0.8046, p=0.4272, supplementary Fig.3b), unsigned PEs from the RL model (t31=-
- Additionally, beyond the linear relationship between absolute PE and CRS (fig3c), we found that the effect of the cardiac cycle increased as absolute PEs became smaller (main effect of absolute PE: t252=14.055, p=1.6e-33; heart cycle: t252=-2.154, p=0.0321; see fig4e).
- This effect was mainly driven by the fact that near-threshold absolute PE were more strongly represented at diastole (t31=2.4089, p=0.0221, fig4c).
- Participants with a higher regression coefficient would have a stronger decrease in the CRS for outcomes presented at diastole compared to systole (see figures 4f-k).
- In line with our predictions, we found that participants showing a higher difference in CRS between diastole and systole were the participants that had higher learning rates and better task performance as indexed by the total number of rewards received (learning rates: t30=2.1821, p=0.0371; reward: 
- The relationship was only present in the blocks in which learning was possible (predictive blocks: learning rates: t30=2.4468, p=0.0205; reward: t30=2.3751, p=0.0241 Fig.4g and 4j; non-predictive blocks: learning rates: t30=-0.4445, p=0.6598; reward: t30=1.1354, p=0.2652 Fig.4h and 4k).
- These results remain true even when including a covariate indexing features of the external outcome type – reward and absolute PE from the model as opposed to the internal, subjective, absolute prediction error (see supplementary figure 4).

## Figure Descriptions

### Figure 1.
Schematic representation of the task and RL results for all four association schemes, highly predictive anticorrelated (HA), highly predictive correlated (HC), variable predictive (VP) and non-predictive (NP). (a) task + cardiac-related neural signals (CRS) recorded at outcome for 4 sec -enough to g

### Figure 2.
CRS morphology and results. (a) Grand average waveforms across the scalp time-locked to the onset of the R-wave which is the biggest electrical wave generated during normal conduction (time 0 ms, see Methods). The set of electrodes clustered by ROIs (colour-coded) for the fronto-central and central-

### Figure 3.
Machine learning discrimination. (a) Description of the data used for the outcome absolute PE discrimination: we used the highest and lowest quantiles based on absolute PE (salience or surprise) as estimates for high and low absolute PE respectively. The analysis was performed on the CRS-locked EEG 

### Figure 4.
Influence of the cardiac cycle on the CRS and learning. (a) Schematic description of the systole and diastole phases. In red and blue are the systole and diastole periods respectively. Below is a representation of two example trials on which outcome onsets happened at systole or diastole. We then lo

### Supplementary Figure 1.
Main behavioural results. (a) Mean accuracy (number of time participants were rewarded) across the four main types of block (left panel) and across the four main types of blocks, played twice during one experimental session - HPA: highly-predictive anticorrelated block, HPC: highly-predictive correl

### Supplementary Figure 2.
Discriminator performance (Az) during high-vs-low salient outcome discrimination of CRS-locked EEG data, for all subjects.

### Supplementary Figure 3.
Control analyses for potential unaccounted effects. (a) The average number of trials for systole and diastole was the same across predictive and non-predictive blocks. (b) Mean absolute PE difference between the CRS for all outcomes presented at systole versus diastole (N=32). A violin plot is used 

### Supplementary Figure 4.
Control analyses for potential unaccounted effects of outcome (valence and absolute PE) in the relationship between CRS and heart cycle.

## References
Total references in published paper: 53

### Key References (from published paper)
- Interactions between cardiac activity and conscious somatosensory perception (, 2019)
- Heart–brain interactions shape somatosensory perception and evoked potentials (, 2020)
- Predicting and Explaining Intentions and Behavior: How Well Are We Doing? (, 1998)
- Decision theory, reinforcement learning, and the brain (, 2008)
- Separate neural representations of prediction error valence and surprise: Evidence from an fMRI meta (, 2018)
- Reinforcement Learning in Multidimensional Environments Relies on Attention Mechanisms (, 2015)
- Following One’s Heart: Cardiac Rhythms Gate Central Initiation of Sympathetic Reflexes (, 2009)
- Emotional appraisal is influenced by cardiac afferent information (, 2012)
- Augmentation of the auditory event related potentials of the brain during diastole (, 1984)
- Visual evoked potentials change as heart rate and carotid pressure change (, 1982)
- Effects of affective arousal on choice behavior, reward prediction errors, and feedback-related nega (, 2015)
- The macaque anterior cingulate cortex translates counterfactual choice value into actual behavioral  (, 2019)
- Dynamic Interaction between Reinforcement Learning and Attention in Multidimensional Environments (, 2017)
- Neuronal basis of sequential foraging decisions in a patchy environment (, 2011)
- Dopamine reward prediction-error signalling: a two-component response (, 2016)
- Model-based predictions for dopamine (, 2018)
- Reinforcement-learning in fronto-striatal circuits (, 2022)
- The valuation system: A coordinate-based meta-analysis of BOLD fMRI experiments examining neural cor (, 2013)
- Salience signals in the right temporoparietal junction facilitate value-based decisions (, 2013)
- S. Learning the value of information in an uncertain world (, 2007)
- Anterior Cingulate Cortex Signals Attention in a Social Paradigm that Manipulates Reward and Shock (, 2020)
- Attention for Learning Signals in Anterior Cingulate Cortex (, 2011)
- Brain–heart interactions: physiology and clinical implications (, 2016)
- Striatal BOLD and Midfrontal Theta Power Express Motivation for Action (, 2021)
- Two spatiotemporally distinct value systems shape reward-based learning in the human brain (, 2015)
- Affective interoceptive inference: Evidence from heart-beat evoked brain potentials (, 2019)
- Neural Mechanisms of Credit Assignment in a Multicue Environment (, 2016)
- A Neostriatal Habit Learning System in Humans (, 1996)
- Two spatiotemporally distinct value systems shape reward-based learning in the human brain (, 2015)
- Spatiotemporal neural characterization of prediction error valence and surprise during reward learni (, 2017)

## Ground Truth Reference
- Figures: 8
- Tables: 0
- References: 53