# Experimental Log: A thalamic circuit represents dose-like responses induced by nicotine-related beliefs in human smokers

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- To examine if this design indeed induced changes in beliefs about nicotine in our subjects, we asked all participants to rate their perceived nicotine strength using a 10-point scale after vaping.
- Overall, participants’ perceived nicotine strength significantly increased as a function of instructed beliefs about nicotine dosage (mean ± SD (AU); ‘low’: = 3.52 ± 0.61, ‘medium’: = 4.52 ± 0.41, ‘high’: = 5.82 ± 0.47, rmANOVA F(2,38) = 9.71, P = 0.0004, partial η2□=□0.34, 90% CI□=□0.12≤□η□≤□048, F
- 1b), supporting the validity of our experimental manipulation.Next, we took extensive sanity checks to ensure the instruction did not interfere with participants’ nicotine intake, metabolism, or their baseline nicotine saturation levels.
- To control for this, we set vaping time to 20 minutes during data collection.
- Importantly, we also quantified the amount of nicotine intake, which equals the change in cartridge weight after vaping multiplied by the actual percentage of nicotine content (1.2%).
- We found that nicotine intake did not differ across belief conditions (nicotine intake (mg): ‘low’: = 0.928 ± 0.56, ‘medium’: = 0.719 ± 0.423, ‘high’: = 0.783 ± 0.434; rmANOVA F(2,38) = 1.806, P = 0.178; Fig.
- 1c), suggesting that difference in belief about nicotine did not affect how much liquid or nicotine was consumed by the smokers.
- The overall amount of consumed nicotine here is in a range that is similar to nicotine delivered by traditional cigarettes in previous experimental studies10,11,23.However, it might be possible that even with the same nicotine consumption, nicotine metabolism might still differ between belief condit
- To address this, we collected saliva samples both before and after vaping for high-performance liquid chromatography tandem mass spectrometry (LC-MS/MS) analytical quantification of cotinine—a nicotine metabolite indicative of plasma nicotine levels25 (see Materials and Methods for details).
- We found that vaping-induced changes in cotinine concentrations (ng/mL) were comparable across conditions (rmANOVA F(2,32) = 0.959, P = 0.393; Fig.
- 1d), suggesting that nicotine metabolism itself was unlikely a factor contributing to any brain-based differences.We also measured exhaled carbon monoxide (CO) before vaping as an index of participants’ baseline nicotine saturation level.
- We did not observe differences in CO levels across conditions (parts per million (ppm); rmANOVA F(2,32) = 0.364, P = 0.698; Fig.
- We chose to measure neural activities during a value-based decision-making task because both nicotine and belief about nicotine have been shown to influence similar circuitries involved in reward processing10,11,26,27.
- Specifically, we used a sequential investment task (see Materials and Methods for details) to probe reward processing; similar paradigms have been previously used in both healthy controls and those with nicotine addiction10,11,26,27.
- Briefly, participants made a series of choices regarding how to invest (or short-sell) in simulated stock markets, based on one’s prediction of market return rt, defined as rt = (pt−pt−1) / pt−1 (where pt denotes the market price at time t).
- As such, the absolute value |r| represents the actual reward value that is attainable to the subject.In a whole-brain ANOVA with belief as the main factor (“low”, “medium”, or “high”) and the value signal |rt| as the key parametric modulator (see Materials and Methods for details), we observed that 
- No other brain structures showed a similar neural activity pattern in relation to beliefs at the whole brain level with the same statistical threshold.biorxiv;2022.07.15.500226v2/FIG2F2fig2Fig.
- 2.Belief about nicotine strength induced dose-dependent responses in the thalamus.(a) Whole-brain effects of instructed beliefs about nicotine on value-tracking signals (rmANOVA, cluster-level PFWE = 0.006, k = 50).
- (b) Parameter estimates representing reward-related activities extracted from an independent thalamus mask (shown in purple) across belief conditions in smokers (P = 0.036), compared to a non-smoking healthy controls (HC, orange bar) Bars depict group means, points represent participants.
- (c) Permutation analysis for instructed beliefs conditions (N = 1,000, P = 0.002).
- P value is derived non-parametrically through a permutation test (N = 10,000).
- (e) Correlation between thalamic signals and subjective belief rating regarding perceived nicotine strength (r = 0.27, P = 0.035).
- 1).A region of interest (ROI) analysis using an independent anatomical mask28 further confirmed that BOLD signals from the thalamus differentiated between instructed belief conditions (mean ± SD (AU); ‘low’: = 0.157 ± 1.047, ‘medium’: = 0.601 ± 0.714, ‘high’: = 2.914 ± 0.865; rmANOVA test F(2,38) = 
- These activations did not differ significantly from non-smoking health controls (n=31 for HCs; see Materials and Methods for details; mean ± SD (AU) for HC: = 2.318 ± 4.258; two-sample t-test: ‘smokers-low’ vs ‘HC’ t(49) = 1.95, p = 0.057; ‘smokers-medium’ vs ‘HC’ t(49) = 1.53, p = 0.132; ‘smokers-h
- Using a permutation analysis approach, we iteratively extracted beta estimates from surrogate GLMs based on shuffled belief conditions (N = 2,000).
- We observed that beta estimates for the actual allocation of belief conditions ranked significantly higher than the surrogate distribution (P = 0.002, Fig.
- A finer parcellation of the thalamus29 revealed that ventral posterior nuclei – notably the centromedian (CM) and lateral geniculate nuclei (LGN), were the primary nuclei in which reward-tracking neural activity differentiated between instructed beliefs in a parametric manner (FDR corrected at q = 0
- 2).Next, we asked whether thalamic activities were actually predictive of the belief condition using a decoding analysis.
- We trained a regularized linear discriminant analysis (rLDA) model to decode instructed belief conditions from multivoxel spatial patterns extracted from the thalamus30,31.
- We were able to decode at 49.3 % accuracy the instructed belief condition from the distributed multivoxel patterns of thalamic activity.
- This decoding accuracy was significantly greater than chance level (33.3 %), as confirmed by a permutation test where we iterated the procedure with shuffled labels (N = 10,000) and compared the true decoding accuracy to the surrogate accuracy distribution (surrogate: 33.1 ± 6.3 %, P = 0.011, Fig.
- Following FDR correction only the posterolateral nucleus (VPL) nucleus showed decoding ability significantly higher than chance (FDR corrected at q = 0.05; VPL, P = 0.018; see Supplementary Fig.
- 4).Given the individual variability in susceptibility to instructed beliefs10,11, we also asked whether participants’ subjective beliefs, indexed by their self-reported perception about nicotine strength, also parametrically modulated thalamic responses.
- We found that across all participants and all sessions, subjective ratings of perceived nicotine strength correlated with reward-related activities in the thalamus (Spearman correlation, r = 0.27, P = 0.035, Fig.
- 2e), suggesting that these neural signals were linked to participants’ perceptions about nicotine strength following instructed beliefs.
- Taken together, these analyses further confirmed that experimental instructions about nicotine strength shaped subjective perception in smokers and induced dose-dependent neural responses in the thalamus, a brain region with one of the highest concentrations of nicotinic acetylcholine receptors and 
- This finding might provide a mechanistic account for the previously observed effects that smoking denicotinized or low-nicotine content cigarettes can still induce a substantial level of nAChR occupancy in the human brain22–24.Observed effect of beliefs on thalamic activity was not due to sensorimot
- 3a).Given that technical choices during fMRI preprocessing such as spatial smoothing could have an impact on the resulting findings33, we also conducted all of our main analyses again by using a preprocessing pipeline without spatial smoothing (see Materials and Methods for details).
- However, previous work10 has also identified the ventral striatum as a key region that could be modulated by belief about nicotine.
- Consistent with previous findings, we found that the ventral striatum tracked the market value signal |rt| across all conditions (PFDR q < 0.01, Fig.
- However, striatal responses did not differ between belief conditions at the whole brain level in an ANOVA analysis (P > 0.05, Supplementary Fig.
- 5a).biorxiv;2022.07.15.500226v2/FIG3F3fig3Fig.
- 3.Belief about nicotine strength did not modulate striatal reward-related responses.(a) Whole-brain effects of cross-condition brain activation tracking market return across all instructed belief conditions.
- (b) Parameter estimates representing reward-related activities extracted from an independent nucleus accumbens mask across belief conditions in smokers (teal bars) (rmANOVA P = 0.945; Permutations P = 0.94), compared to a non-smoking healthy controls (HC, orange bar).
- P value is derived non-parametrically through a permutation test (N = 10,000).biorxiv;2022.07.15.500226v2/FIG4F4fig4Fig.
- 4.Belief about nicotine strength modulated thalamus-vmPFC functional connectivity in a dose-dependent fashion.(a) Effects of instructed beliefs on the psychophysiological interaction (PPI) between the thalamus and the vmPFC.
- Error bars are SEM.An ROI analysis using an independent mask of the nucleus accumbens (NAcc) further confirmed that neural activities in the NAcc did not differentiate between belief conditions (rmANOVA F(2,38) = 0.056, P = 0.945, permutation test: P = 0.94 ; Fig.
- These parameter estimates were also comparable to those extracted from the same group of healthy controls using the same NAcc mask (smokers: ‘low’: = 1.228 ± 3.329, ‘medium = 1.248 ± 2.828 ‘high’: = 1.016 ± 2.6983, ‘HC’: = 1.781 ± 2.138; two-sample t-test: ‘low’ vs ‘HC’ t(49) = -0.740, p = 0.462; ‘m
- We did not find significant differences between belief conditions either in separate ROI analyses (putamen rmANOVA F(2,38) = 1.15, P = 0.327; caudate rmANOVA F(2,38) = 0.24, P = 0.781; Supplementary Fig.
- 5b-c).Seemingly surprising at a first glance, the lack of belief effects on the striatum was consistent with the lack of belief effect of instructed beliefs on reinforcement learning behavior in smokers in this study (see Supplementary Information and Supplementary Fig.
- 6 and Supplementary Table 1 for details).
- Combined with the main belief effect concerning the thalamus, we speculate that the experimentally manipulated beliefs in this study primarily modulated low-level information gating as opposed to high-level value-guided decision-making in the previous study10.
- This difference might be attributed to the fact that smokers were not familiar with e-cigarettes in the current study and thus were not driven by conditioned responses tied to using a traditional cigarette as is the case for previous work10.
- We will discuss this in more detail later.Belief about nicotine modulated functional connectivity between prefrontal cortex and thalamus in a dose-dependent mannerAt the circuit level, the thalamus is heavily connected to various cortical regions and is known to contribute to higher-order cognition 
- Specifically, the ventromedial prefrontal cortex (vmPFC) has been increasingly recognized as a key region in representing task states35,36 and the structure of abstract knowledge.
- Anatomically, it is well known that the thalamus and vmPFC are densely connected 37,38.
- Thus, we predicted that thalamic-vmPFC coupling would differ between belief conditions in our study.To this end, we carried out a psychophysiological interaction (PPI; see Materials and Methods) analysis39 with the thalamus as a seed region to investigate how beliefs about nicotine were represented 
- We found that belief about nicotine indeed modulated functional connectivity between the thalamus and the vmPFC both at the whole brain level (PSVC < 0.05, FWE cluster-corrected at a cluster-defining threshold of P < 0.005, uncorrected, P = 0.041; Fig.
- 3a) and via an ROI analysis using a vmPFC mask from an independent study involving belief formation40 (peak at MNI x = -11, y= 50, z = -6, k = 5; Supplementary Fig.
- The vmPFC is a brain region heavily implicated in the computation of value and belief updating36 Importantly, recent work has pinpointed to the vmPFC for its representation of task states41.

## Figure Descriptions

### Fig. 1.
Experimental paradigm and sanity check measures.(a) Participants completed three visits. In each visit, we collected saliva samples for cotinine measurement, measured carbon monoxide (CO) levels, instructed beliefs, and measured brain activities using fMRI as participants engaged in a decision-makin

### Fig. 2.
Belief about nicotine strength induced dose-dependent responses in the thalamus.(a) Whole-brain effects of instructed beliefs about nicotine on value-tracking signals (rmANOVA, cluster-level PFWE = 0.006, k = 50). (b) Parameter estimates representing reward-related activities extracted from an indep

### Fig. 3.
Belief about nicotine strength did not modulate striatal reward-related responses.(a) Whole-brain effects of cross-condition brain activation tracking market return across all instructed belief conditions. Heatmap signifies t values. (b) Parameter estimates representing reward-related activities ext

### Fig. 4.
Belief about nicotine strength modulated thalamus-vmPFC functional connectivity in a dose-dependent fashion.(a) Effects of instructed beliefs on the psychophysiological interaction (PPI) between the thalamus and the vmPFC. (b) Parameter estimates extracted from (a) representing functional coupling s

## References
Total references in published paper: 53

### Key References (from published paper)
- Localization of cognitive operations in the human brain (, 1988)
- Modeling subjective belief states in computational psychiatry: interoceptive inference as a candidat (, 2019)
- The Neurocircuitry of Impaired Insight in Drug Addiction (, 2009)
- Beliefs modulate the effects of drugs on the human brain (, 2015)
- Response expectancy as a determinant of experience and behavior (, 1985)
- The functional neuroanatomy of the placebo effect (, 2002)
- Placebo-induced changes in FMRI in the anticipation and experience of pain (, 2004)
- Neurobiological mechanisms of the placebo effect (, 2005)
- A comprehensive review of the placebo effect: Recent advances and current thought (, 2008)
- Belief about nicotine selectively modulates value and reward prediction error signals in smokers (, 2015)
- Belief about nicotine modulates subjective craving and insula activity in deprived smokers (, 2016)
- Nicotine intake and dose response when smoking reduced-nicotine content cigarettes (, 2006)
- Decreases in recollective experience following acute alcohol: A dose-response study (, 2010)
- Cognitive and subjective dose-response effects of acute oral Δ9-tetrahydrocannabinol (THC) in infreq (, 2002)
- Neural mechanisms underlying nicotine addiction: Acute positive reinforcement and withdrawal (, 2000)
- The thalamus in drug addiction: From rodents to humans (, 2018)
- The reward circuit: Linking primate anatomy and human imaging (, 2010)
- Learning and motivation in the human striatum (, 2011)
- Nicotinic receptor distribution in the human thalamus: Autoradiographical localization of [3H]nicoti (, 1997)
- Neuronal nicotinic receptors in the human brain (, 2000)
- Nicotinic acetylcholine receptors in the mesolimbic pathway: Primary role of ventral tegmental area  (, 2010)
- Cigarette smoking saturates brain alpha 4 beta 2 nicotinic acetylcholine receptors (, 2006)
- Brain nicotinic acetylcholine receptor occupancy: Effect of smoking a denicotinized cigarette (, 2009)
- Effect of secondhand smoke on occupancy of nicotinic acetylcholine receptors in brain (, 2011)
- Cotinine as a biomarker of tobacco exposure: Development of a HPLC method and comparison of matrices (, 2010)
- Neural signature of fictive learning signals in a sequential investment task (, 2007)
- Smokers’ brains compute, but ignore, a fictive error signal in a sequential investment task (, 2008)
- An automated method for neuroanatomic and cytoarchitectonic atlas-based interrogation of fMRI data s (, 2003)
- Thalamus Optimized Multi Atlas Segmentation (THOMAS): fast, fully automated segmentation of thalamic (, 2019)
- Linear discriminant analysis achieves high classification accuracy for the BOLD fMRI response to nat (, 2016)

## Ground Truth Reference
- Figures: 4
- Tables: 0
- References: 53