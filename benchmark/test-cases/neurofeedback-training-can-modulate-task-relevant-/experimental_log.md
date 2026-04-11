# Experimental Log: Neurofeedback training can modulate task-relevant memory replay rate in rats

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- RESULTSA neurofeedback paradigm to promote SWRsTo reinforce SWR activity, our neurofeedback paradigm linked the online detection of large SWRs with positive reinforcement: delivery of a tone and food reward (Figure 1A).
- We embedded the neurofeedback requirement into a flexible spatial memory task (Figure 1B) that we have studied extensively (Gillespie et al., 2021), allowing us to compare neural and behavioral data from subjects that perform the task with neurofeedback manipulation to those without the manipulation
- All subjects performed the same overall task, which comprised structured trials consisting of three steps (Figure 1C): first, initiating a trial by nosepoking at the home port; second, maintaining a nosepoke at whichever center port illuminates (randomly assigned on each trial) for a duration determ
- Top trace: raw CA1 LFP; bottom trace: ripple filtered (150-250 Hz) CA1 LFP.
- At the neurofeedback port, the subject had to maintain its nose in the port until a suprathreshold SWR was detected, which triggered delivery of a tone and food reward (Figure 1A, Supplementary Figure 1A,B; and see Methods).
- The delay period length was randomly chosen from the pre-reward duration of recent neurofeedback trials, such that the amount of time spent waiting at each of the center ports was approximately matched (Supplementary Figure 1C, and see Methods).
- In the control cohort, whose data have been presented previously (Gillespie et al., 2021), both center ports required the subject to maintain its nose in the port for an unpredictable delay period (see Methods), after which a tone and food reward was delivered.The memory aspect of this task is requi
- Occasionally, the rewarded arm changes, prompting the subject to return to sampling different arms to find the new goal location (Gillespie et al., 2021).
- Before implant, all subjects were pretrained on a delay-only version of this task, as summarized in the experimental timelines in Figure 1D.
- Once performance stabilized, a microdrive containing 30 independently movable tetrodes was implanted targeted to dorsal CA1 (Supplementary Figure 1D).
- After implant, subjects were given several days to recover; during this time tetrodes were gradually lowered into the CA1 cell layer and the animal was briefly re-trained to perform the delay-only version of the task.
- The control cohort of subjects continued such performance for many days (Gillespie et al., 2021).For subjects in the manipulation cohort, the neurofeedback component of the task was then introduced.
- Each day, 4-6 CA1 tetrodes were used for online SWR detection (Supplementary Figure 1A, and see Methods).
- Because we use just a small subset of tetrodes, our online detection algorithm does not detect every SWR event identified by our offline detection strategy, which incorporates all CA1 tetrode data.
- First, it means that rewards are provided to SWR events on an unpredictable, variable schedule – an operant conditioning regime which drives robust, persistent task engagement (Ferster and Skinner, 1957).
- SWR size, as defined by the peak amplitude of the event, can be generally described by a long-tailed distribution, with larger events occurring less frequently than smaller events (Yu et al., 2017).
- Starting with a low threshold ensures that the animals received feedback relatively rapidly and remained engaged early in training.Over subsequent days of training, the size threshold for SWR detection at the neurofeedback port was gradually increased, requiring the subject to generate larger and la
- We then maintained the threshold at a high level for several additional days of behavior (“stable period”).Neurofeedback training increases SWR rate during the targeted intervalIn response to the increasing SWR detection threshold, subjects in the manipulation cohort successfully produced increasing
- This was not the case: instead, subjects produced large SWR events much faster than would have been predicted based on the initial prevalence of similarly sized events (Supplementary Figure 2B).
- To quantify systematic group effects of cohort, we used linear mixed-effects models (see Methods), since this approach allows us to appropriately account for correlations between measurements taken from each subject (Yu et al., 2022).First, to assess whether subjects learned to directly increase the
- These analyses revealed that subjects did not consistently increase SWR size: only two out of four subjects showed very slight but significant increases (Supplementary Figure 2C).
- We also found no difference in SWR size between either trial type in the manipulation cohort and the control cohort (Supplementary Figure 2C, inset).
- Instead, when we quantified the number of events of each size per behavioral epoch, we found that within the manipulation cohort, neurofeedback trials contained roughly twice as many events relative to delay trials for all SWR sizes (Supplementary Figure 2D).
- These results rule out our first candidate strategy and indicate that subjects met the neurofeedback criteria efficiently by modulating SWR rate, not event size.The increase in SWR rate pre-reward was associated with striking differences in when SWRs occurred both within and across cohorts that were
- To assess how SWR rate was changing during the time spent at the center ports, we calculated SWR rate in 0.5 s bins throughout the time subjects spent nosepoked at the center ports, aligning each trial to reward delivery (Figure 2B).
- By contrast, subjects in the control cohort rarely generated SWRs during the pre-reward period but showed much higher SWR rates than the manipulation cohort after reward delivery.biorxiv;2022.10.13.512183v4/FIG2F2fig2Figure 2.Neurofeedback training enhances SWR rate during targeted interval.(A) Exam
- Trigger SWRs on NF trials are excluded from the rate calculation, and time bins with fewer than 100 trials contributing data are not shown.
- Manipulation cohort n = 1892, 684, 1157, and 1602 NF trials and 2022, 640, 1201, and 1552 delay trials; control cohort n = 2490, 2629, 2027, and 3021 trials.
- For the pre-reward period, manipulation cohort ranksum comparisons between NF and delay trials: p = 4.382x10−258, 7.111x10−83, 5.689x10−214, and 3.285x10−191.
- Manipulation cohort NF trials vs control cohort trials: p = 1.126x10−16; manipulation cohort delay trials vs control cohort trials: p = 0.009.
- For the post-reward period, manipulation cohort ranksum comparisons between NF and delay trials: p = 3.646x10−127, 0.038, 6.538x10−11, and 2.768x10−23, respectively.
- Manipulation cohort NF trials vs control cohort trials: p = 0.142; manipulation cohort delay trials vs control cohort trials p = 0.691.
- For pre+post combined, manipulation cohort ranksum comparisons between NF and delay trials p = 3.324x10−64, 3.136x10−40, 2.996x10−69, and 9.066x10−50, respectively.
- Manipulation cohort NF trials vs control cohort trials: p = 0.237; manipulation cohort delay trials vs control cohort trials: p = 0.504.(D) Count of SWR events detected during the pre-reward period (left), post-reward period (middle) and for the total time at the center ports (right).
- For the pre-reward period, manipulation cohort ranksum comparisons between NF and delay trials: p = 3.133x10−96, 8.936x10−37, 1.266x10−106, and 6.024x10−65.
- Manipulation cohort NF trials vs control cohort trials: p = 6.790x10−7; manipulation cohort delay trials vs control cohort trials: p = 0.0018.
- For the post-reward period, manipulation cohort ranksum comparisons between NF and delay trials: p = 1.797x10−137, 6.100x10−10, 6.688x10−13, and 2.152x10−130.
- Manipulation cohort NF trials vs control cohort trials: p = 2.361x10−12; manipulation cohort delay trials vs control cohort trials p = 5.820x10−9.
- For pre+post combined, manipulation cohort ranksum comparisons between NF and delay trials: p = 1.534x10−19, 5.828x10−14, 6.735x10−32, and 0.083.
- Manipulation cohort NF trials vs control cohort trials p = 0.366; manipulation cohort delay trials vs control cohort trials: p = 0.299.
- Manipulation cohort ranksum comparisons between NF and delay trials: p = 1.397x10−23, 8.588x10−49, 6.180x10−4, and 7.127x10−257.
- Manipulation cohort NF trials vs control cohort trials: p = 4.075x10−18; manipulation cohort delay trials vs control cohort trials: p = 1.835x10−18.For C-E, all within-subject ranksum p-values are corrected using the Benjamini-Hochberg method and all groupwise comparisons are performed using linear 
- Indeed, we found that during the pre-reward period, SWR rates were approximately twice as high on neurofeedback compared to delay trials, and both trial types from the manipulation cohort had much higher rates than trials from the control cohort (Figure 2C, left).
- This effect was not dependent on the trigger SWR, as excluding suprathreshold events from both neurofeedback and delay trials did not change the result (Supplementary Figure 2E).
- This finding indicates that the neurofeedback training caused far more SWRs to occur prior to reward delivery at both center ports in the manipulation cohort, with the most pronounced effect occurring on neurofeedback trials.These patterns differed after the reward at the center ports, where SWR rat
- Relative to the pre-reward period, SWR rates were maintained at a high level during neurofeedback trials, while they increased substantially during delay and control trials (Supplementary Figure 2F).
- Note that the slightly lower SWR rate post-reward on neurofeedback trials compared to delay trials could not be explained by a refractory period following the trigger SWR (Supplementary Figure 2G).
- When considering both pre- and post-reward periods together, the neurofeedback trials still showed higher SWR rates than delay trials within the manipulation cohort, but the differences between each trial type and the control cohort were not significant (Figure 2C, right).
- We quantified the number of SWRs during pre-reward, post-reward, and total center port times (Figure 2D).
- Our SWR count results were completely consistent with the SWR rate findings during the pre-reward period (Figure 2D, left) and largely consistent when considering the total center port time (Figure 2D, right).
- However, we found striking differences during the post-reward period, during which we saw a clear reversal of the pre-reward effect on SWR counts: neurofeedback trials contained fewer SWRs than delay trials, and both trial types contained far fewer SWRs post-reward than trials from the control cohor
- It was notable, therefore, that neurofeedback trials had slightly but significantly shorter post-reward periods than delay trials (Figure 2E).
- Even more strikingly, subjects in the manipulation cohort remained at the port for approximately half as long as subjects in the control cohort (Figure 2E, inset), despite all trial types receiving the same amount of reward.
- The difference in dwell time could not be explained by the control cohort having fewer days of task experience than the manipulation cohort, since post-reward dwell time tended to increase, rather than decrease, over subsequent days of performance within the control cohort (Supplementary Figure 2H).
- The mean speeds of the head-mounted LEDs while the subjects were nosepoked were below our cutoff for immobility (4 cm/s) for all trial types, however, we did observe a slightly but significantly lower mean speed during the pre-reward period on neurofeedback trials compared to delay trials and trials
- Trial n are the same as in (E); manipulation cohort ranksum comparisons between NF and delay trials: p = 2.447x10−223, 2.760x10−85, 3.247x10−80, and 9.077x10−36.
- Manipulation cohort NF trials vs control cohort trials: p = 1.260x10−7; manipulation cohort delay trials vs control cohort trials: p = 1.121x10−4.(B) Mean head velocity for subsets of trials: the quartile of trials with the lowest mean head velocities are shown for the control cohort and for delay t
- Manipulation cohort n = 473, 171, 289, and 400 NF trials and 505, 160, 300, and 388 delay trials; control cohort n = 624, 794, 423, and 913 trials.
- Manipulation cohort ranksum comparisons between NF and delay trials: p = 1.342x10−160, 1.053x10−55, 9.488x10−98, and 4.751x10−130.
- Manipulation cohort NF trials vs control cohort trials: p = 0.989; manipulation cohort delay trials vs control cohort trials: p = 4.196x10−4.(C) SWR rate for the pre-reward period for the subset of trials included in G, showing that even in neurofeedback trials with equal or higher velocities than d
- Trial n are the same as in (G); manipulation cohort ranksum comparisons between NF and delay trials: p = 3.923x10−11, 1.155x10−8, 1.902x10−18, and 5.081x10−6.
- Manipulation cohort NF trials vs control cohort trials: p = 1.019x10−6; manipulation cohort delay trials vs control cohort trials: p = 7.958x10−3.To assess whether this difference could affect SWR rates, we selected the quartile of neurofeedback trials with the highest mean speeds and compared them 
- Even with much higher mean speeds (Figure 3B), the neurofeedback trials showed higher SWR rates than control and delay trials (Figure 3C).
- However, we did not find evidence for such a relationship consistently: the correlation coefficients between pre-reward and post-reward SWR counts were positive in some subjects and negative in others, and always very small in magnitude, indicating a weak relationship (r = -0.084, 0.130.
- 0.118, and - 0.061 and p = 1.47x10−7, 3.84x10−6, 8.60x10−9, and 6.01x10−4, for each subject in the manipulation cohort, respectively).
- These results suggest that while compensatory regulation of SWR generation may be evident across hundreds of trials, high variability in SWR rate, count, and dwell time across trials may prevent consistent detection of this effect at the level of single trials.Neurofeedback training preserves replay
- As hippocampal CA1 neurons often fire reliably at particular locations in space (“place cells”) while an animal moves through an environment, replay content has most often been studied with regard to its spatial content.
- Inverting this “encoding model” yields a “decoding model” that can predict the spatial locations represented by the neural spiking within SWRs (Zhang et al., 1998).We used a clusterless state-space model (Chen et al., 2012; Deng et al., 2016; Denovellis et al., 2021; Kloosterman et al., 2014) identi
- Briefly, we first project the 2D maze environment to 1D (Figure 4A).
- We next use times when the animal is moving through the maze to build a model that relates amplitude features of detected spikes to the location on the 1D maze where they were observed.
- We then can predict the spatial representation of spikes observed during movement (Figure 4B) and during SWRs (see Methods).biorxiv;2022.10.13.512183v4/FIG4F4fig4Figure 4.Neurofeedback preserves replay content.(A) The 2D maze is linearized to 1D for decoding efficiency; movement trajectory for an ex
- Manipulation cohort n = 37, 14, 18, and 26 behavioral epochs per subject for each trial type and control cohort n = 24, 32, 23, and 33 behavioral epochs.
- Manipulation cohort ranksum comparisons between NF and delay trials: p = 0.1813, 0.5978, 0.0273, and 0.6738.
- Manipulation cohort NF trials vs control cohort trials: p = 0.5523; manipulation cohort delay trials vs control cohort trials: p = 0.2098.(E) Rate of remote replay events during pre-reward period.
- Manipulation cohort n = 1843, 558, 1011, and 1513 NF trials and 1982, 535, 1038, and 1447 delay trials; control cohort n = 2058, 2509, 1879, and 2795 trials per subject, respectively.
- Manipulation cohort ranksum comparisons between NF and delay trials: p = 6.507x10−126, 9.703x10−30, 2.991x10−79, and 6.293x10−55, respectively.
- Manipulation cohort NF trials vs control cohort trials: p = 9.073x10−4; manipulation cohort delay trials vs control cohort trials: p = 0.4304.(F) Rate of remote replay events during the pre- and post-reward periods combined.
- Manipulation cohort ranksum comparisons between NF and delay trials: p = 7.666x10−47, 1.573x10−6, 1.044x10−16, and 5.768x10−6.
- Manipulation cohort NF trials vs control cohort trials: p = 0.6644; manipulation cohort delay trials vs control cohort trials: p = 0.1477.(G) Generalized linear model coefficients quantify the extent to while replay of an arm is modulated by its behavioral relevance.
- Manipulation cohort n = 1661, 392, 866, and 1281 NF trials and 1705, 367, 894, and 1213 delay trials per subject; control cohort n = 1458, 1636, 1464, and 2181 trials, respectively.For panels D-F, all ranksum p-values are corrected using the Benjamini-Hochberg method and all groupwise comparisons ar
- These events frequently represent the subject’s current location (“local” replay; Figure 4C, left two events) as well as locations or trajectories that encompass distant regions of the maze environment (“remote” replay; Figure 4C, middle four events).
- In small subset of cases, SWRs contain a mixture of disjoint spatial representations with no single location clearly dominant (fragmented events; Figure 4C, right), which do not meet our replay criteria and are excluded from analysis.Across a variety of measures, we found that neurofeedback training
- In SWRs during the pre-reward period, there was no difference in the fraction of SWRs that qualified as replay between the two cohorts, and within each manipulation cohort subject, there was no consistent difference between neurofeedback and delay trials (Figure 4D).Replay of remote locations has be
- Consistent with our SWR findings, we find much higher rates of remote replay during the pre-reward period in neurofeedback trials compared to delay trials within the manipulation cohort, and low rates of remote replay during this time in trials from the control cohort (Figure 4E).
- However, if we consider both the pre-and post-reward periods combined, we find no difference in remote replay rate between the two cohorts for either trial type (Figure 4F).
- Within the manipulation cohort, neurofeedback trials have slightly but significantly higher rates of remote replay than delay trials over the combined pre- and post-reward period.Prior work demonstrated that replay events in this task were enriched for specific, relevant past experiences that change
- As previously seen in the control cohort, we observed consistently enhanced representation of previous goal locations in replay events during the pre-reward period in both neurofeedback and delay trials within the manipulation cohort (Figure 4G).
- These results also remain unchanged when we analyzed replay events during both pre- and post-reward time at the center ports (Supplementary Figure 3A).Together, these results indicate that while the timing of replay is altered by the neurofeedback training, the content and behavioral relevance is pr
- Our previous findings (Gillespie et al., 2021), suggested that SWRs and replay do not drive trial-by-trial choice behavior in this task, so we did not predict that the increase in SWRs on individual neurofeedback trials would necessarily improve performance on those trials.
- The manipulation cohort subjects show a slight improvement in search efficiency compared to control subjects, which only reached significance on delay trials (Figure 5A).
- However, rather than relating to the neurofeedback training, this difference could have been driven by the additional days of experience that the manipulation cohort has on the task, since the control cohort showed a subtle but consistent increase in this performance measure over time (Supplementary
- We found no bias toward either of the two trial types: neurofeedback trials accounted for approximately half of redundant search trials for each subject (Figure 5B), indicating that neither the neurofeedback nor delay trial type was consistently overrepresented among the trials with suboptimal behav
- Manipulation cohort ranksum comparisons between neurofeedback (NF) and delay trials: p = 0.9562, 0.7509, 0.7509, and 0.9562, respectively.
- Manipulation cohort NF trials vs control cohort trials: p = 0.5425; manipulation cohort delay trials vs control cohort trials: p = 0.0069.(B) The fraction of redundant search trials per epoch which are NF (vs delay).
- Two-sided sign test vs 0.5: p = 0.1102, 0.2668, 1, and 1, respectively.(C) During trials when the subject has discovered the goal arm, the fraction of subsequent trials in which the goal arm is visited (“correct” choice).
- Manipulation cohort ranksum comparisons between NF and delay trials: p = 0.7202, 0.7202, 0.8123, and 0.7202.
- Manipulation cohort NF trials vs control cohort trials: p = 0.6946; manipulation cohort delay trials vs control cohort trials: p = 0.2857.(D) The fraction of error repeat trials which are NF trials.
- Two-sided sign test: p = 0.3770, 0.7744, 1, and 0.0227, respectively.For all panels, manipulation cohort n = 37, 14, 18, and 26 behavioral epochs per subject, respectively, and control cohort n = 24, 32, 23, and 33 behavioral epochs.
- We also saw no difference between the two cohorts or between neurofeedback and delay trials on this measure (Figure 5C).
- Within the manipulation cohort, we also found that error trials, when subjects do not choose to visit a known goal arm, were equally distributed between neurofeedback and delay trials (Figure 5D).
- Overall, these results suggest that on a single-trial timescale, the neurofeedback manipulation had neither a beneficial nor detrimental effect on behavior, in line with our previous findings (Gillespie et al., 2021).

## Figure Descriptions

### Figure 1.
A neurofeedback paradigm to promote SWRs.(A) Schematic of the neurofeedback (NF) protocol: while subject’s nose remains in the neurofeedback port, SWRs (yellow) are detected in real time. Top trace: raw CA1 LFP; bottom trace: ripple filtered (150-250 Hz) CA1 LFP. During the neurofeedback interval, t

### Figure 2.
Neurofeedback training enhances SWR rate during targeted interval.(A) Example CA1 raw LFP traces and ripple filtered LFP traces (150-250Hz) with SWRs highlighted in yellow, from the time spent at a center port on a neurofeedback (NF) trial (top) and a delay trial (middle) from a manipulation subject

### Figure 3.
Speed does not account for differences in SWR rate.(A) Mean head velocity (smoothed), during pre-reward time at the center ports. Trial n are the same as in (E); manipulation cohort ranksum comparisons between NF and delay trials: p = 2.447x10−223, 2.760x10−85, 3.247x10−80, and 9.077x10−36. Inset: G

### Figure 4.
Neurofeedback preserves replay content.(A) The 2D maze is linearized to 1D for decoding efficiency; movement trajectory for an example neurofeedback (NF) trial is shown in green. Times of SWR events are highlighted in yellow, and the small letters indicate the SWRs that are shown in (C).(B) Decoding

### Figure 5.
Neurofeedback does not alter behavioral performance.(A) During trials when the subject is searching for a new goal location, we quantify the fraction of trials in which the subject chooses an arm that has not yet been sampled. Manipulation cohort ranksum comparisons between neurofeedback (NF) and de

## References
Total references in published paper: 58

### Key References (from published paper)
- Disrupting ripples: Methods, results, and caveats in closed-loop approaches in rodents (, 2021)
- Hippocampal sharp wave bursts coincide with neocortical “up-state” transitions (, 2004)
- Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning (, 2015)
- Reward revaluation biases hippocampal replay content away from the preferred outcome (, 2019)
- Transductive neural decoding for unsorted neuronal spikes of rat hippocampus (, 2012)
- Rapid Classification of Hippocampal Replay Content for Real-time Applications (, 2016)
- Hippocampal replay of experience at real-world speeds (, 2021)
- Disruption of ripple-associated hippocampal activity during rest impairs spatial learning in the rat (, 2010)
- Inducing gamma oscillations and precise spike synchrony by operant conditioning via brain-machine in (, 2013)
- Long-duration hippocampal sharp wave ripples improve memory (, 2019)
- Schedules of Reinforcement (, 1957)
- The evolving view of replay and its functions in wake and sleep (, 2020)
- The organization of recent and remote memories (, 2005)
- Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice (, 2021)
- Apolipoprotein E4 Causes Age-Dependent Disruption of Slow Gamma Oscillations during Hippocampal Shar (, 2016)
- Selective suppression of hippocampal ripples impairs spatial memory (, 2009)
- Learning-induced plasticity regulates hippocampal sharp wave-ripple drive (, 2014)
- Assembly-Specific Disruption of Hippocampal Replay Leads to Selective Memory Deficit (, 2020)
- Hippocampal replay is not a simple function of experience (, 2010)
- Gamma frequency entrainment attenuates amyloid load and modifies microglia (, 2016)
- Operant conditioning of synaptic and spiking activity patterns in single hippocampal neurons (, 2014)
- Integration and segregation of activity in entorhinal-hippocampal subregions by neocortical slow osc (, 2006)
- Awake hippocampal sharp-wave ripples support spatial memory (, 2012)
- Pacing Hippocampal Sharp-Wave Ripples With Weak Electric Stimulation (, 2018)
- Sharpening Working Memory With Real-Time Electrophysiological Brain Signals: Which Neurofeedback Par (, 2022)
- Early Hippocampal Sharp-Wave Ripple Deficits Predict Later Learning and Memory Impairments in an Alz (, 2019)
- The hippocampal sharp wave-ripple in memory retrieval for immediate use and consolidation (, 2018)
- Replay, the default mode network and the cascaded memory systems model (, 2022)
- A hippocampal network for spatial coding during immobility and sleep (, 2016)
- Targeting hippocampal hyperactivity with real-time fMRI neurofeedback: protocol of a single-blind ra (, 2021)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 58