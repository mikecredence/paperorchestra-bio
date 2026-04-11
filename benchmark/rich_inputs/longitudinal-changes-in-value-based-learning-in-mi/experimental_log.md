# Experimental Log: Hippocampus and Striatum Showed Distinct Contributions to Longitudinal Changes in Value-Based Learning in Middle Childhood

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- A descriptive overview is provided in Table 1 and Figure 2.
- The details of the reported GLMM models, including the random effects structure and the effects of age and sex, are described in the Appendix 2.
- Since some children were poor learners who failed to reach 50 % average accuracy in their last 20 trials (13 children at wave 1 and 6 children at wave 2), we also performed behavioral analyses with a reduced dataset in which results remained unchanged (Appendix 6).biorxiv;2023.04.13.536699v5/FIG2F2f
- (C) Reaction time differed by feedback timing, in which decisions for cues learned with delayed feedback were faster, and reaction times were faster at wave 2 compared to wave 1.
- Significant correlations are circled, p-values were adjusted for multiple comparisons using bonferroni correction.biorxiv;2023.04.13.536699v5/TBL1T1tbl1Table 1.Descriptive behavioral results of dependent variables Accuracy (ACC, probability correct), win-stay probability (WS), lose-shift probability
- Furthermore, win-stay probability increased and lose-shift probability decreased longitudinally, again without differences by feedback timing (WS: βwave=2 = .586, SE = .071, z = 8.22, p < .001, βfeedback=delayed = .023, SE = .033, z = 0.69, p = .489; LS: βwave=2 = -.252, SE = .037, z = -6.87, p < .0
- Reaction times were faster at wave 2 compared to wave 1, and they were faster for delayed compared to immediate feedback trials (βwave=2 = -221, SE = 22.8, t(dfSatterthwaite = 135) = -9.70, p < .001, βfeedback=delayed= -13.8, SE = 6.59, t(dfSatterthwaite = 136) = -2.10, p = .038).
- To summarize, children’s average accuracy improved over 2 years, while their win-stay probability increased and their lose-shift probability decreased between waves.
- Children were able to respond faster to cues paired with delayed feedback compared to cues paired with immediate feedback, and they became faster in their decision-making across waves (see mixed model effects overview in Table 1).
- Of note, reaction times were largely uncorrelated with accuracy and switching behavior (win-stay, lose- shift), while accuracy and switching behavior showed significant correlations at both waves (Figure 2D).Modeling resultsChildren’s behavior was best described by value-based learningWe conducted a
- Model comparison using leave-one-out cross validation showed evidence in favor of the value-based learning model, reflected in the highest expected log pointwise predictive density and highest model weights, confirming that children’s learning behavior in the longitudinal data can generally be bette
- Children whose individual fit was better for a heuristic model (wsls) than for the value-based model (vbm1), were at both waves more likely to be poor learners (defined as an accuracy below 50% in the last 20 trials).
- Taken together, children’s learning behavior was best described by a value-based model, and a heuristic strategy model captured more poor learners compared to a value-based model.biorxiv;2023.04.13.536699v5/TBL2T2tbl2Table 2.Model comparison results.Feedback timing modulated choice stochasticityMode
- Table 3 and Figure 3A provide a descriptive overview of the winning model parameters.
- Of note, there were only small differences in model fit (elpd100) to the second-best model (vbm2, 1α2ρ, Δelpdl00= -2.93, elpd_SEl00 = 2.92, pseudo-BMA+ = 0.24), which suggests a potential separable feedback timing effect on outcome sensitivity.
- We also performed the model comparison with a reduced dataset in which the winning model remained the same (Appendix 6).
- The average inverse temperature did not differ by feedback condition, but showed large within-person condition differences at both waves, indicating individual differences in feedback timing modulation (wave 1: Δτ($,7;<$ Mean = 0.22, SD = 3.80, Range = 21.74, wave 2: Δτ($,7;<$Mean = 0.35, SD = 3.70,
- The correlations between the parameters are reported in Appendix 3.biorxiv;2023.04.13.536699v5/FIG3F3fig3Figure 3.(A) Individual differences in the learning rate and inverse temperature of the winning model and their longitudinal change.
- (B) The condition differences in the inverse temperature correlated with reaction time, i.e., higher delayed compared to immediate inverse temperature was related to faster delayed compared to immediate reaction time.biorxiv;2023.04.13.536699v5/TBL3T3tbl3Table 3.Description of model parameters from 
- Indeed, at both waves, children who responded faster during delayed compared to immediate feedback had a higher inverse temperature at delayed compared to immediate feedback (wave 1: r = -.261, t(df = 138 = -3.18, p = .002, wave 2: r = -.345, t(df = 124) = - 4.10, p < .001, Figure 3B).
- Specifically, more value-guided choice behavior (i.e., higher inverse temperature) was related to faster responses during delayed feedback relative to immediate feedback, suggesting a link between model parameter and behavior in relation to feedback timing.Children’s value-based learning became more
- We simulated 10,000 parameter combinations and created a learning score map according to each parameter combination (Figure 4A).
- The optimal parameter combination was at a learning rate α = 0.29, and an inverse temperature τ = 19.8, and with an average learning score of 96.5 % (Figure 4A).
- Children’s fitted learning rates ranged 0.01 – 0.22 and inverse temperature 6.73 – 18.70 and were outside the parameter space of a learning score above 96 % (Table 3 and Figure 4A).
- The average longitudinal increases in learning rate and inverse temperature were mirrored by average increases in the learning scores, confirming our prediction that their parameters developed towards optimal value-based learning (arrow in Figure 4B).
- We further found that the average longitudinal change in win-stay and lose-shift proportion also developed towards more optimal value- based learning (Appendix 4).biorxiv;2023.04.13.536699v5/FIG4F4fig4Figure 4.(A) The model simulation depicts parameter combinations and simulation-based average learn
- The cyan “X” in the middle top depicts the optimal parameter combination where average learning scores were at 96.5 %, and the cyan rectangle depicts the space of the fitted parameter combinations, (B) Enlarged view of the space of fitted parameter combinations.
- The colored lines depict averaged trial-by-trial task behavior for each feedback condition, and a cyan ribbon indicates the 95% highest density interval of the one-step-ahead prediction using the entire posterior distribution.Model validation.
- To validate our winning model vbm8, we estimated its predictive accuracy by comparing one-step-ahead model predictions with the choice data.
- The one-step ahead predictions of the winning model captured children’s choices overall well, with predictive accuracies of 65.3 % at wave 1 and 75.7 % at wave 2 (Figure 4C).
- Further, our winning model showed a good parameter recovery for learning rate (r = 0.85) and inverse temperature (r = 0.75 – 0.77).
- Our winning model showed excellent on the group level (100%) when comparing it to a set of models used during model comparison (vbm/, vbm2, wsls).
- The individual model recovery was lower (58%), with 35% of the simulated winning model fitting best on our baseline model vbm/with a single inverse temperature, which likely reflects the noisy property of the inverse temperature (Appendix 1).Longitudinal brain-cognition linksSignificant longitudinal
- All four variables of interest showed significant positive mean changes and variances, and all univariate models provided a good fit to the data (see Appendix 5).
- This allowed us to further relate the differences in structural brain changes to changes in learning.biorxiv;2023.04.13.536699v5/FIG5F5fig5Figure 5.(A) Recognition memory (corrected recognition = hits - false alarms) for objects presented during delayed feedback was only enhanced at trend.
- Depicted are significant paths cross-domain (brain-cognition, dashed lines) and within-domain (brain or cognition, solid lines), other paths are omitted for visual clarity and are summarized in Table 4.
- Depicted brain-cognition links included ϕSTRw1, LSime,w1 (covariance between striatal volume and immediate learning score at wave 1), as well as ϕHPCw1, LSdel,w1 (covariances between hippocampal and striatal volumes and delayed learning score at wave 1).
- Brain links included ϕSTRw1, HPCw1 (wave 1 covariance and change-change covariance), and similarly, cognition links included ϕLSime,w1, LSdel,w1, and ρΔSTR,ΔHPC.
- ** denotes significance at α < .001, * at α < .05.biorxiv;2023.04.13.536699v5/TBL4T4tbl4Table 4.Parameter estimates of a four-variate latent change score model that includes brain (striatal and hippocampal volume) and cognition domains (immediate and delayed learning score)Hippocampal volume exhibit
- First, the bivariate LCS model provided a good data fit (χ² (14) = 10.09, CFI = 1.00, RMSEA (CI) = 0 (0-.06), SRMR = .04).
- We then further fitted two constrained models, to see whether setting the mean striatal change or the mean hippocampal change to 0 would lead to a drop in the model fit.
- Compared to the unrestricted model, the constrained model that assumed no striatal change did not lead to a drop in model fit (Δχ2 (1) = 2.74, p = .098), whereas the model that assumed hippocampal change dropped in model fit (Δχ2 (1) = 12.69, p < .001).
- Finally, we tested a more stringent assumption of equal change for striatal and hippocampal volumes, in which the model dropped in model fit compared to the unrestricted model (Δχ2 (1) = 18.04, p < .001) and suggests that striatal and hippocampal change differed.
- The LCS model provided good data fit (χ2 (27) = 15.4, CFI = 1.00, RMSEA (CI) = 0 (0 – .010, SRMR = .045), and all relevant paths are shown in Figure 5D (see Table 4 for a detailed model overview).
- For the striatal associations to cognition, we found that wave 1 striatal volume covaried with both immediate learning score and delayed learning score (ϕSTRw1, LSi,w1 = 0.19, z = 2.52, SE = 0.07, p = .012, ϕSTRw1, LSd,w1 = 0.18, z = 2.37, SE = 0.07, p = .018).
- Constraining the striatal association to immediate learning to 0 worsened the model fit relative to the unrestricted model (Δχ2 (1) = 5.66, p = .017), which was the same when constraining the striatal association to delayed learning to 0 (Δχ2 (1) = 5.14, p = .023).
- This pattern remained the same in the results of the reduced dataset (Appendix 6).Hippocampal volume, on the other hand, only covaried with delayed learning at wave 1 (ϕSTRw1, LSi,w1 = 0.14, z = 2.05, SE = 0.07, p = .041), not with immediate learning score (ϕSTRw1, LSi,w1 = 0.12, z = 1.68, SE = 0.07
- Fixing the path between hippocampal volume and delayed learning to 0 worsened the model fit relative to the unrestricted model (Δχ2 (1) = 4.19, p = .041), but not when its path to immediate learning was constrained to 0 (Δχ2 (1) = 2.94, p = .086).
- In the results of the reduced dataset, the hippocampal association to the delayed learning score was no longer significant, suggesting a weakened pattern when excluding poor learners (Appendix 6).
- A model equal-constraining striatal and hippocampal paths to immediate learning (Δχ2 (1) = 0.41, p = .521) and another model equal-constraining these paths to delayed learning (Δχ2 (1) = 0.14, p = .707) did not lead to a worse model fit compared to the unrestricted model, which suggests that the bra
- This is in line with the high wave 1 covariance and change-change covariance within the brain and cognition domain (see Table 4).
- We found no longitudinal links between the brain and cognition domains, which suggests that the found brain-cognition links at wave 1 remained longitudinally stable (see Appendix 5 for an exploratory LCS model that related the model parameters to striatal and hippocampal volume).Taken together, the 
- Episodic memory, as measured by individual corrected object recognition memory (hits - false alarms) of confident (“sure”) ratings, showed at trend better memory for items shown in the delayed feedback condition (βfeedback = delayed = .009, SE =.005, t(df = 137) = 1.80, p = .074, see Figure 5A).
- Note that in the reduced dataset, delayed feedback predicted enhanced item memory significantly (Appendix 6).

## Tables

### Table 1.
> Descriptive behavioral results of dependent variables Accuracy (ACC, probability correct), win-stay probability (WS), lose-shift probability (LS), and reaction time (RT, in seconds), as well as mixed 


### Table 2.
> Model comparison results.


### Table 3.
> Description of model parameters from the winning value-based model vbm3.


### Table 4.
> Parameter estimates of a four-variate latent change score model that includes brain (striatal and hippocampal volume) and cognition domains (immediate and delayed learning score)


### Appendix 2–table 1.
> Mixed effects model structure and fixed effects results for the models using the dependent variables Accuracy (ACC), win-stay (WS), lose-shift (LS) and Reaction time (RT).


### Appendix 5–table 1.
> Model fit and parameter estimates of the univariate LCS models for immediate and delayed feedback learning score as well as for striatal (STR) and hippocampal (HPC) brain volumes.


### Appendix 6–table 1.
> Comparison of the fixed effects results for the models with the reduced and with the complete dataset, each with the dependent variables accuracy (ACC), win-stay (WS), lose-shift (LS) and reaction tim


### Appendix 6–table 2.
> Model comparison results obtained with the reduced dataset and the complete dataset.


## Figure Descriptions

### Figure 1.
(A) Depiction of two example trials of immediate and delayed feedback conditions presented at wave 1. For immediate feedback (top panel), between choice response and feedback, cue and choice were presented for 1 s. At feedback, a green frame around the incidentally encoded object indicated a positiv

### Figure 2.
Individual differences in the behavioral reinforcement learning outcomes and their longitudinal change. (A) Accuracy did not differ by feedback timing and increased between waves. (B) Win-stay and lose-shift proportion did not differ by feedback timing, and win-stay increased and lose-shift proporti

### Figure 3.
(A) Individual differences in the learning rate and inverse temperature of the winning model and their longitudinal change. The inverse temperature τ but not learning rate α was separated by feedback timing, and both increased between waves in their values (top panel). The condition difference in th

### Figure 4.
(A) The model simulation depicts parameter combinations and simulation-based average learning scores. The cyan “X” in the middle top depicts the optimal parameter combination where average learning scores were at 96.5 %, and the cyan rectangle depicts the space of the fitted parameter combinations, 

### Figure 5.
(A) Recognition memory (corrected recognition = hits - false alarms) for objects presented during delayed feedback was only enhanced at trend. (B) Learning scores depicted here were used in the LCS analyses. Learning scores were the model-derived choice probability of the contingent choice using fit

### Appendix 1—figure 1.
Parameter recovery of the winning model, the black line represents the identity line, whereas the blue line is loess regression line, Correlations are calculated by Pearson’s r.

### Appendix 1—figure 2.
Model recovery on the group (left) and individual level (right). Group-level recovery values are the average model weights (across 20 groups, 50 datasets each) Pseudo-BMA+ using Bayesian model averaging stabilized by Bayesian bootstrap using 100,000 iterations. Individual-level recovery values are t

### Appendix 2–figure 1.
Fixed effects plots of significant predictors across behavioral variables accuracy (ACC), win-stay (WS), lose-shift (LS) and reaction time (RT).

### Appendix 3–figure 1.
Parameter correlations of the winning model. Significant correlations are circled, p-values were adjusted for multiple comparisons using bonferroni correction.

### Appendix 4–figure 1.
(A) The arrows depict mean change (bold white) and individual change (transparent black) of the empirical win-stay and lose-shift proportions. The greyscale gradient-filled dots, that are connected by the arrows, depict the individual learning score, while the the greyscale gradient in the backgroun

## References
Total references in published paper: 76

### Key References (from published paper)
- States versus Rewards: Dissociable neural prediction error signals underlying model-based and model- (, 2010)
- Developmental Changes in Learning: Computational Mechanisms and Social Influences (, 2017)
- A brain network supporting social influences in human decision- making (, 2020)
- Feedback Timing Modulates Brain Systems for Learning in Humans (, 2011)
- Factors that influence the relative use of multiple memory systems (, 2013)
- Memory Systems of the Basal Ganglia. Handb (, 2016)
- An Upside to Reward Sensitivity: The Hippocampus Supports Enhanced Reinforcement Learning in Adolesc (, 2016)
- Interactive Development of Adaptive Learning and Memory (, 2021)
- Emotional modulation of habit memory: neural mechanisms and implications for psychopathology (, 2018)
- Stress and multiple memory systems: from ‘thinking’ to ‘doing’ (, 2013)
- A role for the medial temporal lobe in feedback-driven learning: Evidence from amnesia (, 2013)
- Feedback timing modulates interactions between feedback processing and memory encoding: Evidence fro (, 2020)
- Feedback-Based Learning in Aging: Contributions and Trajectories of Change in Striatal and Hippocamp (, 2018)
- Using reinforcement learning models in social neuroscience: Frameworks, pitfalls and suggestions of  (, 2020)
- Reinforcement learning across development: What insights can we draw from a decade of research? (, 2019)
- Experiential reward learning outweighs instruction prior to adulthood (, 2015)
- Differential representation of feedback and decision in adolescents and adults (, 2014)
- The Computational Development of Reinforcement Learning during Adolescence (, 2016)
- Distentangling the systems contributing to changes in learning during adolescence (, 2020)
- Cognitive flexibility in adolescence: Neural and behavioral mechanisms of reward prediction error pr (, 2015)
- Change, stability, and instability in the Pavlovian guidance of behaviour from adolescence to young  (, 2018)
- Striatum-medial prefrontal cortex connectivity predicts developmental changes in reinforcement learn (, 2012)
- The computational basis of following advice in adolescents (, 2019)
- The Teenage Brain: Sensitivity to Rewards (, 2013)
- A cross-sectional and longitudinal analysis of reward- related brain activation: Effects of age, pub (, 2014)
- What do RL Models MeasureInterpreting Model Parameters in Cognition and Neuroscience (, 2021)
- The rational use of causal inference to guide reinforcement learning strengthens with age. npj Sci (, 2020)
- Longitudinal four-dimensional mapping of subcortical anatomy in human development (, 2014)
- Typical development of basal ganglia, hippocampus, amygdala and cerebellum from age 7 to 24 (, 2014)
- Structural Magnetic Resonance Imaging of the Adolescent Brain (, 2004)

## Ground Truth Reference
- Figures: 10
- Tables: 8
- References: 76