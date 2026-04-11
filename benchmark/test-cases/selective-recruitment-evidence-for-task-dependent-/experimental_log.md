# Experimental Log: Selective recruitment: Evidence for task-dependent gating of inputs to the cerebellum

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsMotor taskTo test the selective recruitment hypothesis in the motor domain, we used a task which involved alternating finger presses of middle and ring finger (Figure 1A).
- Starting at a baseline level of 1Hz and 2.5N, we either increased the force of each response or the required rate (Table 1).
- Both manipulations are expected to produce an increase in the BOLD response in neocortical motor areas (Diedrichsen et al., 2013; Thickbroom et al., 1998).
- As such, our task-invariant connectivity model predicts increased cerebellar activity with both increases in speed and force (Spraker et al., 2012).
- Critically, selective recruitment predicts that for equivalent activity levels in the neocortex, cerebellar activity should be higher in the speed than in the force condition.biorxiv;2023.01.25.525395v3/TBL1T1tbl1Table 1.Mean and between-subject standard deviation (±) of force, speed, and error rate
- Reward feedback (e.g., +4) was based on their performance.Participants complied well with task instructions, as evidenced by the group-averaged peak forces and number of taps, which were close to the target values (Table 1).
- The high error rate for the baseline condition reflects the fact that some of the participants completed the 6 taps in less than the minimum interval of 4s in this very easy condition.Increasing force and speed leads to increased activation in cortico-cerebellar motor networkAs expected for right-ha
- Compared to the baseline condition, the combined M1/S1 ROI showed a significant activation increase in the high-force (t15 = 9.41, p = 1.10×10−7) and the high-speed conditions (t15 = 8.29, p = 5.54×10−7).
- Similarly, activity in the right anterior and posterior motor areas of the cerebellum (outlined in light gray in Figure 2, see Methods for details on region of interest) increased with increasing force (t15 = 14.21, p = 4.14×10−10) and speed (t15 = 7.60, p = 1.59×10−6).
- The medium force and speed conditions were between baseline and high conditions, replicating previous findings of a parametric modulation of activity with both force (Spraker et al., 2012) and speed (Jäncke et al., 1999).biorxiv;2023.01.25.525395v3/FIG2F2fig2Figure 2.Activation in the cortico-cerebe
- (D-F) Flat map of the cerebellum (Diedrichsen and Zotow, 2015) with lobular boundaries indicated in dotted line.
- The right anterior and posterior hand motor area (gray outline) was defined by a new functional atlas of the cerebellum (Nettekoven et al., 2023).Visual inspection of the activation maps (Figure 2D vs.
- 2F) suggests that cerebellar activity increased more with speed than with force.
- However, the neocortical activation patterns for speed and force conditions were not completely matched (Figure 2A vs.
- 2C): Increasing speed led to more widespread activation in secondary motor areas compared to increasing force.
- Therefore, the observed differences in cerebellar activity could have resulted from additional fixed inputs from premotor and supplementary motor areas, rather than from a task-dependent recruitment of cerebellar circuits for the speed task.Cerebellar activity for increased speed is larger than pred
- Figure 3A shows the connectivity weights from this model for the cerebellar right hand area, region M3 (Nettekoven et al., 2023).
- According to the model, inputs to cerebellar M3 do not only come from contralateral M1 and S1, but also from premotor and supplementary motor regions.biorxiv;2023.01.25.525395v3/FIG3F3fig3Figure 3.Selective recruitment of cerebellum for fast alternating finger movements.A) Average connectivity weigh
- Resting baseline (located at 0,0) is not shown explicitly but included in the regression.
- The error bars indicate the standard error of the mean of the signed residuals.We multiplied the neocortical activity patterns from each individual and condition with the connectivity weights from the model to predict the corresponding cerebellar M3 activity level.
- Note that the connectivity weights were estimated on subjects from independent task-based fMRI datasets; therefore, the predicted values were on a different scale compared to the observed values (Figure 3B).
- To account for this scaling difference, we used a simple linear regression between observed and predicted values.In general, the predicted values closely match the observed values (average R2 = 0.60, SEM = 0.01).
- To test for systematic deviations across subjects, we submitted the signed residuals for all conditions to a one-way ANOVA, revealing a significant effect of condition (F4, 60 = 6.796, p = 1.1 × 10-4).
- Post-hoc tests revealed that the signed residual for the high-speed condition was significantly higher than for the high force condition (t15 = 2.37, p = 0.0157).
- This was also the case when comparing medium speed and medium force (t15 = 1.94, p = 0.035).
- To ensure that our findings were robust, we replicated the results using 2 additional connectivity models.
- First, we used an L1-regularized model, which resulted in sparser connectivity weights.
- In our previous study, we found that this model performed only slightly worse in predicting left-out data compared to the L2-regularized model (King et al., 2023).
- high-force condition remained significant (L1 regression: t15 = 2.373, p = 0.0315, Fusion model: t15 = 2.140, p = 0.0492).
- Cerebellar activation, particularly in Lobules VI, Crus I and VIII is consistently observed in fMRI studies of working memory (Cohen et al., 1997; Courtney et al., 1997; D’Esposito and Postle, 2015; Nee et al., 2012).
- Here we test if these cerebellar areas are especially recruited for a specific component process of working memory.We implemented a digit span task in which participants memorized and subsequently recalled a sequence of visually presented digits (Figure 4A).
- Each trial began with a cue that signaled the recall direction (forward or backward) and the number of digits that had to be remembered (2, 4, 6).
- During the encoding phase, six digits were sequentially displayed from left to right at a rate of 1 digit/s.
- At the end of each 1 s presentation interval, the next digit was presented and the most recent digit either remained on the screen or was replaced by the hashtag symbol (#) if it had to be remembered.
- Thus, while the memory load varied between 2 and 6 items, all conditions involved the presentation and production of 6 digits.
- On 25% of the trials (no-go) the trial was terminated at the start of retrieval phase.
- In summary, we measured activity for 12 conditions (2 recall directions x 3 memory loads x 2 phases).biorxiv;2023.01.25.525395v3/FIG4F4fig4Figure 4.The digit span task and behavioral performance.a) Timeline of trial events.
- After a 1 s delay, the task progressed to either the retrieval phase (Go trial) or skipped directly to the next trial (No-go trials).
- Error bars indicate standard error of the mean across participants.Figure 4B shows the error rate (trials with at least 1 wrong press) during the scanning session.
- As expected, error rates increased with memory load and were also higher in the backwards condition.Consistent with previous imaging studies, the verbal working memory task led to high activity in the fronto-parietal network (Cohen et al., 1997; Courtney et al., 1997; D’Esposito and Postle, 2015; Ne
- Within the cerebellum, encoding and retrieval activated a superior region (lateral parts of lobule VI, extending to Crus I), as well as an inferior region (VIIb and VIIIa) (Chen and Desmond, 2005; Desmond et al., 1997).
- As observed previously for verbal working memory, the activity was more pronounced in the right than in the left cerebellar hemisphere (Desmond and Fiez, 1998).
- In our symmetric functional atlas (Nettekoven et al., 2023), the best corresponding functional region was right D3 (see Methods, Region of interest).biorxiv;2023.01.25.525395v3/FIG5F5fig5Figure 5.Average activation in the cortico-cerebellar network for working memory.Group-averaged activation during
- The D3R sub-region of the multi-demand network in the right cerebellar hemisphere was used in the main analysis (outlined in light gray).Cerebellar activity for encoding at high load is larger than predicted by task-invariant connectivityTo estimate which neocortical regions provide input to our cer
- The connectivity weights from the model (Figure 6A) suggest converging input from area 55b (located at the inferior end of the middle frontal gyrus), PEF (premotor eye field), area 6r (anterior to the primary motor cortex), and SCEF (dorsomedial frontal cortex (Glasser et al., 2016)).
- After fitting a linear regression to account for scale differences between predicted and observed activations, we found that the predicted values matched the observed values relatively well at the individual level (R2 = 0.42, SE = 0.01).biorxiv;2023.01.25.525395v3/FIG6F6fig6Figure 6.Selective recrui
- Error bars show SEM of the signed residuals for each condition across subjects.Turning to our test of selective recruitment, there was one clear deviation where the observed cerebellar activation was greater than predicted (Figure 6B): During encoding in the highest load condition.
- A repeated 1-factor measures ANOVA on the residuals across all 12 conditions found a systematic deviation across participants (F11, 165 = 2.22, p = 0.0156).
- When we analyze the residuals using a 2 (phase) x 2 (recall direction) x 3 (load) ANOVA, we found a significant 2-way interaction between load and phase (F2, 30 = 4.38, p = 0.02), but no significant effect of recall direction (F1, 15 = 0.95, p = 0.34).
- The same pattern of results was found with a significant difference across conditions (L1-regularized model trained on the MDTB dataset: F11, 165 = 2.34, p = 0.0105; L2-regularized model trained on 5 datasets: F11, 165 = 2.55, p = 5.3 × 10−3) due to a significant deviation from the predicted level o

## Tables

### Table 1.
> Mean and between-subject standard deviation (±) of force, speed, and error rate for each condition across subjects.


## Figure Descriptions

### Figure 1.
Timeline of events in the alternating finger tapping task.The height of the target force area indicated the target force, the number of white squares the target number of taps. During the press interval, the participant alternatively tapped the middle and ring finger. After each tap, the next box tu

### Figure 2.
Activation in the cortico-cerebellar motor network compared to rest.Activity maps for high force (left), baseline (middle), and high speed (right) conditions. High levels of force and speed were chosen to show the spatial distribution of activity. Medium level of force and speed resulted in similar 

### Figure 3.
Selective recruitment of cerebellum for fast alternating finger movements.A) Average connectivity weights from a group-level connectivity model (Ridge regression, MDTB, task set A) for the cerebellar right-hand area shown on inflated surface of the left hemisphere. B) Average observed cerebellar act

### Figure 4.
The digit span task and behavioral performance.a) Timeline of trial events. The cue signaled the recall direction (blue for backward and yellow for forward) and memory load (size of the white box indicated the number of memory digits) of the upcoming trial. During encoding, a new digit appeared ever

### Figure 5.
Average activation in the cortico-cerebellar network for working memory.Group-averaged activation during the encoding (A) and retrieval (B) phases on an inflated representation of the left cerebral hemisphere (as in Figure 2). C, D) Group average activity during the two phases in the cerebellum. The

### Figure 6.
Selective recruitment of cerebellum in digit span task.A) Average connectivity weights from a group-level connectivity model for the cerebellar D3R region of interest. B) Average observed cerebellar activation (y-axis) plotted against average prediction from the connectivity model (x-axis). Line sho

### Supp. Figure. 1.
Connectivity models evaluation.The connectivity model used in the main analysis was trained on task set A of the MDTB dataset using Ridge regression (King et al., 2023). As alternative connectivity models, we used Lasso regression on the same training set and a ridge regression model trained on 5 ta

## References
Total references in published paper: 64

### Key References (from published paper)
- Importance of nitric oxide for local increases of blood flow in rat cerebellar cortex during electri (, 1994)
- Differential involvement of cortical and cerebellar areas using dominant and nondominant hands: An F (, 2015)
- Complex motor task associated with non-linear BOLD responses in cerebro-cortical areas and cerebellu (, 2016)
- Attentional activation of the cerebellum independent of motor involvement (, 1997)
- A fast diffeomorphic image registration algorithm (, 2007)
- The neural basis of functional brain imaging signals (, 2002)
- Science and Statistics (, 1976)
- The organization of the human cerebellum estimated by intrinsic functional connectivity (, 2011)
- Context sensitivity of activity-dependent increases in cerebral blood flow (, 2003)
- Dissociation of spikes, synaptic activity, and activity-dependent increments in rat cerebellar blood (, 2003)
- Cerebrocerebellar networks during articulatory rehearsal and verbal working memory tasks (, 2005)
- Temporal dynamics of brain activation during a working memory task (, 1997)
- The Functional Relevance of Task-State Functional Connectivity (, 2021)
- Distinct critical cerebellar subregions for components of verbal working memory (, 2012)
- Transient and sustained activity in a distributed neural system for human working memory (, 1997)
- Neuroimaging studies of the cerebellum: language, learning and memory (, 1998)
- Lobular Patterns of Cerebellar Activation in Verbal Working-Memory and Finger-Tapping Tasks as Revea (, 1997)
- The cognitive neuroscience of working memory (, 2015)
- A spatially unbiased atlas template of the human cerebellum (, 2006)
- Universal Transform or Multiple Functionality? Understanding the Contribution of the Human Cerebellu (, 2019)
- A multivariate method to determine the dimensionality of neural representation from population activ (, 2013)
- Surface-Based Display of Volume-Averaged Cerebellar Imaging Data (, 2015)
- FreeSurfer (, 2012)
- Statistical parametric maps in functional imaging: A general linear approach (, 1994)
- Non-Linear Frequency Dependence of Neurovascular Coupling in the Cerebellar Cortex Implies Vasodilat (, 2022)
- A multi-modal parcellation of human cerebral cortex (, 2016)
- Physiological analysis of simple rapid movements in patients with cerebellar deficits (, 1991)
- Subtle cognitive deficits after cerebellar infarcts (, 2006)
- Updated energy budgets for neural computation in the neocortex and cerebellum (, 2012)
- The energy use associated with neural computation in the cerebellum (, 2010)

## Ground Truth Reference
- Figures: 7
- Tables: 1
- References: 64