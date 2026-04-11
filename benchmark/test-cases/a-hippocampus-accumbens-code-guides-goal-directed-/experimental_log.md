# Experimental Log: A hippocampus-accumbens code guides goal-directed appetitive behavior

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- Mice had to run on a self-propelled treadmill, traversing a 360 cm long textile belt with six differently textured zones, including one otherwise unmarked 30 cm long fixed reward zone (35, 36).
- Licking a spout in this zone causes a liquid reward to be dispensed once per lap (Figure 1A and Figure S1A-E).
- Mice underwent five days of training in which they learned to obtain more rewards by progressively increasing their licking in both reward zone and a 30 cm “anticipation zone” preceding the reward zone (Figure 1B-D and Figure S1F-N).biorxiv;2023.03.09.531869v1/FIG1F1fig1Figure 1.Dual-color two-photo
- Mice moved on a cue-enriched self-propelled treadmill belt of 360 cm length and obtained a liquid reward when licking at a spout in a hidden reward zone of 30 cm length (yellow).
- (B) Representative traces of one mouse’s behavior on training day 1 and day 5.
- (D) Number of rewarded laps per training session (F (4) = 6.344, GG-correction), anticipatory (F (4) = 3.803) and reward licking (F (4) = 4.276, GG-correction) significantly increased over the course of five training days (n = 18 mice, repeated-measures ANOVA).
- Thy1-GCaMP6s mice were injected with AAVrg-Cre in the medial NAc and DIO-mCherry in dHPC.
- Representative coronal brain slice showing axonal mCherry expression in NAc (AP -1.3; left).
- Representative coronal brain slice stained with DAPI (blue) of dHPC, showing the outlines of the 3 mm cannula window used for imaging; scale bar represents 1 mm (second left).
- Field of view of one sample experiment showing Thy1-GCaMP6s expression in green and mCherry expression of putative NAc-projecting neurons in red; outlines show detected components used for analysis (right).
- *p < 0.05, **p < 0.01.To understand the neural coding properties of large numbers of dHPC→NAc neurons in behaving animals, we turned to dual-color two-photon imaging in mice pan-neuronally expressing the calcium indicator GCaMP6s, as well as the static red marker mCherry in defined NAc-projecting ne
- For this, we injected AAVrg-Cre in NAc and DIO-mCherry in dHPC (CA1/subiculum border region) of Thy1-GCaMP6s mice (37).
- This approach allowed us to obtain dynamic calcium signals both in a large majority of mCherry-negative hippocampal neurons (dHPC−) and specifically mCherry co-expressing NAc-projecting neurons (dHPC→NAc), simultaneously within the same field of view using the same calcium indicator (Figure 1E and F
- It allowed us to overcome constraints of electrophysiological studies such as relatively low sample sizes (19, 20) or indirect connectivity measurements (38, 39).
- Optical access to dorsal CA1 and pro-subiculum (also known as proximal subiculum (40, 41)) was established by implanting a chronic hippocampal window after virus injections (Figure S1C) (42, 43).
- Imaging data was acquired after 5 days of behavioral training, was motion-corrected using NormCorre, and spatio-temporal components were extracted using constrained non-negative matrix factorization (CNMF) (44).
- We thus obtained calcium signals for further analysis from a total of 5,372 GCaMP-expressing neurons including 444 putative dHPC→NAc neurons in 6 mice across 19 imaging sessions (Figure 1F and Figures S2 and S3).
- These numbers approximate previously established proportions of NAc-projecting neurons in dorsal prosubiculum and distal CA1 (20, 45, 46).Enhanced spatial coding by dHPC→NAc neuronsGiven the dHPC’s well-established role in representing spatial information and the role of dHPC→NAc projections in spat
- Indeed, we found large numbers of both dHPC− and dHPC→NAc neurons with repeatedly elevated calcium levels on the same positions of the belt (Figure 2A-C and Figure S3).
- Comparing each neuron’s spatial information content (47) with that of a randomly shuffled distribution, we identified a significantly higher proportion of such place cells in dHPC→NAc neurons (169/444 neurons; 38 %) compared to dHPC− neurons (1,581/4,928 neurons; 32 %; χ2, p = 0.012; Figure 2D).
- Within this population of place cells, we further analyzed how specifically space is encoded, and found that dHPC→NAc place cells had a higher spatial information rate (47) (p < 0.001, Welch’s t-test; Figure 2E).
- They also had significantly higher levels of sparsity (p < 0.001, Welch’s t-test; Figure 2F), a measure for how diffuse a neuron is firing in the spatial domain (48).
- Furthermore, both the relative calcium activity (activity inside the place field – activity outside the place field; p = 0.0044, Welch’s t-test) and reliability of in-place field activity per lap (p = 0.014, Welch’s t-test) were significantly higher for dHPC→NAc place cells compared to dHPC− neurons
- These results suggest that the dHPC routes enhanced and more reliable spatial information to NAc compared to the general dHPC population, in line with previous results pointing towards the necessity of dHPC→NAc projections for spatial memory expression (31, 32).biorxiv;2023.03.09.531869v1/FIG2F2fig2
- NAc-projecting neurons contain a higher proportion of place cells (D, χ2(1, 5372) = 6.364); these place cells contain more spatial information per second (E, Welch’s t (186.55) = 4.770), show increased sparsity (F, Welch’s t (218.79) = 3.657), higher reliability (G, probability of firing maximally w
- n = 6 mice, 19 imaging sessions, 5,372 (inc.
- 444 mCherry-coexpressing) neurons, 1,750 (inc.
- 169 mCherry-coexpressing) place cells.
- *p < 0.05, **p < 0.01, ***p < 0.001.
- See also Figure S3.Place fields are modulated by local cue boundaries and are overrepresented near the reward zonePrevious studies found that place fields are often not homogenously distributed across the environment but can be modulated by salient environmental features such as textures, borders, o
- We hypothesized that information about such spatial features may be preferentially routed to NAc, given the relevance of NAc for spatial memory (29, 30) and particularly for reward-related behaviors (51).Upon inspection of place cells’ spatially binned calcium profiles (Figure 3A-B and Figures S3, S
- We found a significant overrepresentation of place field start and end positions (but not centers) near texture boundaries for both dHPC− and dHPC→NAc populations (ratios >99.9th percentile, permutation test).
- This effect was more pronounced in dHPC→NAc neurons (PF start: p = 0.033, PF end: p = 0.036, χ2; Figure 3C-D and Figure S4A-C).
- This suggests that dHPC→NAc neurons are more strongly modulated by local cue boundaries.biorxiv;2023.03.09.531869v1/FIG3F3fig3Figure 3.dHPC→NAc place fields are modulated by local cues and reward zone.(A) Heat maps of dHPC− (left) and dHPC→NAc (right) place cells’ normalized position-binned average 
- Dotted line and shade represent average and 95th CI of 1000x randomly shuffled place fields.
- Both dHPC− and dHPC→NAc place field start and end positions are significantly overrepresented at the 99.9th percentile (dotted black lines) compared to a randomly shuffled distribution.
- Start (χ2(1, 5134) = 5.735) and end positions (χ2(1, 5217) = 4.397) of dHPC→NAc place fields are furthermore significantly overrepresented compared to the dHPC− population.
- 2-way ANOVA, F success(1,1) = 54.918, p < 0.001, F projection(1,1) = 0.958, p = 0.338, F interaction(1,1) = 2.969, p = 0.098.
- Post-hoc Welch’s t -tests with Bonferroni correction: t dHPC– (3.561) = 3.698; t dHPC→NAc (3.479) = 8.671; t low success(13.629) = 0.093, p = 1; t high success(3.952) = 2.075, p = 0.215.
- Wilcoxon’s t -test, W (9) = 5.0, n = 10 imaging sessions.
- *p < 0.05, **p < 0.01, ***p < 0.001.
- See also Figure S4.Mice were trained to lick for reward in a hidden reward zone.
- Previous studies have shown that such zones and their preceding vicinity are often over-represented by place cells (35, 52, 53) – we hypothesized that this effect might involve dHPC→NAc neurons, given the NAc’s role in reward-related behaviors (51).
- When pooled across all sessions, we found little evidence of such an overrepresentation (Figure S4D-E).
- Mouse behavior generally shows great variability though, and previous work demonstrated the dependence of such an overrepresentation on individual task success (35, 52).
- We thus divided sessions into high- and low-success based on lick performance (lick precision and reward dispensation, see Methods) and found significantly more dHPC→NAc place cells near the reward zone (reward and anticipation zones) in high-success sessions compared to low-success sessions (p = 0.
- In contrast, dHPC− neurons only showed a trend towards significance (p = 0.051, Welch’s t-test; Figure 3E-F).
- In line with previous studies, both neuronal populations also showed a strong correlation between the success rate (percentage of rewarded laps) and the proportion of place fields near the reward zone across sessions (r = 0.62; Figure S4F).If reward zone information is preferentially encoded in dHPC
- We found that, within individual sessions, decoding accuracy of the reward anticipation zone was significantly enhanced for dHPC→NAc populations (p = 0.0195, Wilcoxon’s test; Figure 3G).
- These findings demonstrate significant modulation of dHPC→NAc neurons by local cue boundaries and enhanced reward zone coding.Enhanced coding of low velocities in dHPC→NAc neuronsAs correct performance in the spatial reward learning task goes hand in hand with a reduction in velocity and an increase
- In line with previous analyses of speed coding in hippocampal and parahippocampal regions (8, 56), we av-eraged each neuron’s calcium activity per velocity bin from 2 to 30 cm/s and regressed this activity against velocity.
- Neurons with a significant regression model (after correcting for false discovery rate) and positive slope were classified as speed-excited (Figure 4A-B).
- We found around 15 % of neurons were positively speed-modulated, with comparable proportions between dHPC− and dHPC→NAc neurons (13 % vs.
- 16 %, p = 0.109, χ2; Figure 4C-D).
- We also identified neurons with a significant velocity regression but a negative slope (Figure 4E-F).
- We found approximately 15 % of such speed-inhibited neurons, with a significantly larger proportion among the dHPC→NAc population (15 % vs.
- 21 %, p = 0.00022, χ2; Figure 4G-H).
- These results suggest widespread modulation of dHPC neuronal activity by non-spatial features such as velocity, with dHPC→NAc neurons specifically over-representing low speeds.biorxiv;2023.03.09.531869v1/FIG4F4fig4Figure 4.Speed-inhibited cells are overrepresented in dHPC→NAc neurons.(A-D) Speed-exc
- (B) Linear regression on average calcium events per velocity bin shows a significant positive relationship (slope = 7.43×10−4, intercept = -2.097×10−3, r = 0.937, p = 0.0058).
- (D) Proportions of speed-excited neurons are comparable between dHPC− and dHPC→NAc populations (χ2(1, 5372) = 2.565, p = 0.109).
- (F) Linear regression on average calcium events per velocity bin shows a significant negative relationship (slope = -1.0437×10−4, intercept = 2.814×10−3, r = -0.933, p = 0.0065).
- (H) Negatively tuned neurons are overrepresented in the NAc-projecting population (χ2(1, 5372) = 13.66, p = 0.00022).
- Speed-modulated neurons were classified as showing a significant linear regression at p < 0.05 after Benjamini/Hochberg FDR correction.
- ns: not significant, ***p < 0.001.Overrepresentation of appetitive licking-excited dHPC→NAc neuronsBesides a decrease in velocity when approaching the reward zone, mice also increasingly engaged in licking behavior (see Figure 1B-D).
- Given the NAc’s dual role in appetitive and consummatory behaviors (57), we wondered if licking behaviors might be reflected in the neural activity of dHPC→NAc neurons.
- We found a significant decrease of calcium activity during reward consumption in both dHPC− and dHPC→NAc populations (Figure S5A-C).Appetitive licking, on the other hand, had no apparent effect on neural activity in dHPC− neurons but coincided with a significant increase in calcium activity in the d
- We investigated if this population-averaged data is reflected on the single-cell level and if there are individual cells that are reliably modulated by appetitive licking (Figure 5D-E and Figure S5D-E).
- Comparing the pre- and post-lick neural activity for each neuron for each appetitive lick event, we identified a total of 1,268 neurons (24 %) that were significantly (negatively or positively) modulated by appetitive licking (Figure 5F-I).
- Interestingly, while the proportion of lick-inhibited neurons was comparable between dHPC− and dHPC→NAc populations (19.7 % vs 17.1 %, p = 0.20, χ2; Figure 5I), we found a significantly larger proportion of lick-excited neurons in dHPC→NAc populations (3.8 % vs 7.4 %, p < 0.001, χ2; Figure 5H).
- These findings suggest that dHPC does not route reward information per se to NAc, but rather information on appetitive behaviors required to obtain such rewards.biorxiv;2023.03.09.531869v1/FIG5F5fig5Figure 5.dHPC→NAc neurons are excited by appetitive licking and are over-represented in lick-excited 
- (C) Calcium activity is differentially modulated by appetitive licking onset only in dHPC→NAc neurons; two-way mixed ANOVA; F licktiming(1, 5370) = 2.843, p = 0.0918, F projection(1, 5370) = 43.779, p < 0.001 F interaction(1, 5370) = 7.073, p = 0.0079.
- Post-hoc t -tests with Bonferroni correction: tdHPC– (4927) = 0.871, p = 0.768; tdHPC→NAc (443) = 2.470, p = 0.0277.
- (D) Field of view showing spatial profiles of dHPC− (green outlines) and dHPC→NAc (red outlines), some of which are classified as lick-excited (violet fill) or lick-inhibited (dark blue fill); neurons #11 and #118 are highlighted.
- (E) Behavioral traces and calcium activity of sample neurons #11 (lick-inhibited) and #118 (lick-excited).
- (H) Proportion of appetitive licking-excited neurons is higher in NAc-projecting neurons; χ2(1, 5372) = 13.018, p= 0.00031.
- (I) Proportion of appetitive licking-inhibited neurons is not different between populations; χ2(1, 5372) = 1.626, p = 0.202.
- ns: not significant, *p < 0.05, ***p < 0.001.
- See also Figure S5.Optogenetic activation of dHPC terminals in NAc induces mouth movement and decelerationGiven the NAc’s hypothesized role as an interface between limbic and motor systems (25), we investigated if the observed increase of calcium activity in dHPC→NAc neurons may be a corollary signa
- To enable high-resolution behavioral tracking, we monitored mouse orofacial movements using a high-speed near-infrared camera (Figure 6A-C).
- To test for a causal role of excitatory dHPC→NAc projections in appetitive behaviors, we injected animals with either CaMKIIa-driven ChR2 or EYFP into dHPC and implanted light fibers in the NAc (n = 4/3 mice; Figure 6D-F).
- After habituating mice to run on the treadmill and receive rewards upon licking on the lick spout, mice were given 5 mW of 473 nm 20 Hz (5 ms duration) pulsed laser light for up to 10 seconds upon entry into a hidden light stimulation zone.biorxiv;2023.03.09.531869v1/FIG6F6fig6Figure 6.Optogenetic s
- (A) Example still image from near-infrared camera, sampled at 75 Hz.
- (E) Somatic expression of ChR2-EYFP in dorsal pro-subiculum.
- (F) Axonal expression of ChR2-EYFP in the NAc, where light fibers are placed (tracts indicated by white dotted lines).
- (G) Representative examples of mouth motion around onset of optogenetic stimulation in an animal expressing ChR2 (top) or EYFP control (bottom).
- (H) Trial-averaged mouth motion activity around time of optogenetic stimulation in ChR2 (blue) and EYFP (gray)-expressing mice.
- Mouth motion is significantly increased with optogenetic stimulation in ChR2 animals (t (3) = 7.485; p = 0.00494) but not EFYP animals (t (2) = 1.353; p = 0.309).
- Paired t -tests; n = 4 mice (ChR2), n = 3 mice (EYFP).
- (J) Trial-averaged relative velocity around time of optogenetic stimulation in ChR2 (blue) and EYFP (gray)-expressing mice.
- (K) Velocity is significantly decreased with optogenetic stimulation in ChR2 animals (t (3) = -3.551; p = 0.0381) but not EFYP animals t (2) = -1.263; p = 0.334.
- Paired t - tests; n = 4 mice (ChR2), n = 3 mice (EYFP).
- ns: not significant, *p < 0.05, **p < 0.01.We found that, shortly after stimulation onset, ChR2-expressing mice reliably showed increased mouth movement for up to two seconds after stimulation, while we observed no effects in mice expressing EYFP (pChR2 = 0.0099, pEYFP = 0.617, paired t-tests; Figur
- In line with this, we also found a significant deceleration of running on the treadmill upon light delivery in ChR2 animals but not EYFP animals (pChR2 = 0.0381, pEYFP = 0.334, paired t-tests; Figure 6J-K).
- Previous studies suggested that individual hippocampal neurons do not necessarily exclusively code for one single feature but are instead able to conjunctively encode various environmental properties (9, 55, 59, 60).
- Such conjunctive coding may be particularly relevant for downstream linear decoders to select task-appropriate actions (61, 62).
- We thus investigated speed and lick modulation of projection-specific place cells and interactions between velocity and lick modulation.We first analyzed speed coding in dHPC→NAc place cells and compared it to the dHPC− population (Figure 7A-B).
- We found about one third of hippocampal place cells were also speed-inhibited, in contrast to only about 7 % of non-place cells.
- This effect was particularly pronounced in dHPC→NAc place cells (43 % vs.
- Conversely, place cells were significantly less likely to be speed-excited than non-place cells (10 % vs.
- 15 %, p < 0.001, χ2), an effect that was again more pronounced in dHPC→NAc neurons.
- This shows that dHPC place cells, and in particular those projecting to NAc, are more likely to be speed-inhibited, and less likely to be speed-excited.biorxiv;2023.03.09.531869v1/FIG7F7fig7Figure 7.Enhanced conjunctive coding of space, velocity and licking in NAc-projecting neurons.(A and B) Conjun
- A larger proportion of place cells is speed-inhibited compared to non-place cells (dHPC−: χ2(1, 4928) = 522.71; dHPC→NAc: χ2(1, 444) = 75.02).
- dHPC→NAc place cells also have a higher proportion of speed-inhibited cells than dHPC− place cells (χ2(1, 1750) = 8.977).
- Speed-excited neurons are overrepresented in non-place cells compared to place cells (dHPC−: χ2(1, 4928) = 20.034; dHPC→NAc: χ2(1, 444) = 9.966).
- dHPC→NAc non-place cells also have a higher proportion of speed-excited cells than dHPC− non-place cells (χ2(1, 3622) = 6.255).
- (D) Proportions of lick-excited neurons are significantly enriched in dHPC− (χ2(1, 4928) = 114.515) and dHPC→NAc (χ2(1, 444) = 23.248) place cells compared to non-place cells.
- The proportion of dHPC→NAc lick-excited place cells is also higher than the proportion of dHPC− lick-excited place cells (χ2(1, 1750) = 9.442); there is no difference between non-place cells (χ2(1, 3622) = 0.488, p = 0.485).
- There is no difference in the proportions of lick-inhibited place and non-place dHPC− and dHPC→NAc neurons (χ2s, all p > 0.05).
- Proportions of lick-excited cells are overrepresented in speed-inhibited cells (dHPC−: χ2(2, 4928) = 100.484; dHPC→NAc: χ2(2, 444) = 27.608).
- Lick-excited neurons are further enriched in speed-inhibited dHPC→NAc neurons compared to dHPC− neurons (χ2(1, 830) = 6.564).
- Proportions of lick-inhibited cells are overrepresented in speed-excited cells (dHPC−: χ2(2, 4928) = 290.832; dHPC→NAc: χ2(2, 444) = 18.825).
- ns: not significant, *p < 0.05, **p < 0.01, ***p < 0.001.We next analyzed lick modulation of place cells and, surprisingly, found that the previously observed lick-related increase in calcium activity (Figure 5B) was largely carried by place cells and not by non-place cells (Figure 7C).
- This effect seems to be mostly carried by lick-excited neurons that are significantly overrepresented in place cells compared to non-place cells (8 % vs.
- 2 %, p < 0.001, χ2), particularly in dHPC→NAc neurons (15 % vs.
- 3 %, p < 0.001, χ2; Figure 7D).
- Comparing velocity correlations of lick-excited and lick-inhibited neurons, we observed a clear skew of lick-excited cells to have more negative velocity correlations and lick-inhibited cells to have more positive velocity correlations, visible in both dHPC− and dHPC→NAc populations (Figure 7E).
- This results in significantly more speed-inhibited cells to be lick-excited compared to speed-excited cells (11 % vs.
- 2 %, p < 0.001, χ2), an effect that was even more pronounced in dHPC→NAc neurons (20 % vs.
- 1 %, p < 0.001, χ2; Figure 7F).
- Conversely, speed-excited neurons were much more likely to be lick-inhibited than speed-inhibited neurons (40 % vs.
- These results demonstrate that there is a strong inverse relationship between lick and velocity modulation.One caveat of such conjunctive coding analyses is that in our behavioral task, trained mice often show highly stereotypical behavior, such that mice would mostly lick at one location where they
- To account for this collinearity, we modelled the influence of three key behavioral features (space, velocity, and appetitive licking) on the activity of each neuron by building a generalized linear model for each neuron (GLM; Figure 8A).
- On average, we found that our models could explain close to 40% of the variance observed in our test datasets (Figure S6A), with dHPC→NAc neurons showing increased feature importance for position and licking (Figure S6B).
- To determine significant contributions of the three behavioral features, we next built 3 × 100 models in which one of the behavioral features was randomly shuffled against time, and compared the variance explained to the original model (Figure 8A; see also ref (63)).
- The average drop in variance explained to the full model was significantly stronger in dHPC→NAc neurons compared to dHPC− for position and velocity but not licking (Figure S6C).
- We classified significant modulation as behavioral features whose shuffling led to a reduction in variance explained in more than 95% of shuffled models.
- We found that cells thus encoding space, velocity, and lick-ing were overrepresented in dHPC→NAc compared to dHPC− neurons (space: p < 0.001; velocity: p < 0.001; licking: p = 0.0015; χ2; Figure 8B).
- Importantly, we also found significantly increased proportions of conjunctive coding for all three feature combinations as well as triple-conjunctive neurons in dHPC→NAc neurons compared to dHPC− (all combinations p < 0.001, χ2; Figure 8C-D).
- This results in a significantly higher proportion of conjunctive coding neurons in dHPC→NAc neurons compared to dHPC− (44 % vs.
- 19 %, p < 0.001, χ2; Figure 8E).biorxiv;2023.03.09.531869v1/FIG8F8fig8Figure 8.A generalized linear model confirms enhanced conjunctive coding in NAc-projecting neurons.(A) Schematic of the generalized linear model (GLM) using position, velocity, and appetitive licking data as predictors for each ne
- Bottom histograms show R2 distributions for 100 shuffled models for each feature.
- Dotted line represents value of 95th percentile, thick black line represents original model’s R2.
- (B) Increased proportions of dHPC→NAc neurons modulated by position (χ2(1, 5372) = 93.634), velocity (χ2(1, 5372) = 141.86), and licking (χ2(1, 5372) = 10.050).
- (C) Increased proportions of conjunctive coding in dHPC→NAc neurons for position & velocity (χ2(1, 5372) = 163.97), position & licking (χ2(1, 5372) = 26.029), velocity & licking (χ2(1, 5372) = 27.145), and position & velocity & licking (χ2(1, 5372) = 34.993).
- Non-coding neurons are overrepresented in dHPC− neurons (χ2(1, 5372) = 35.382); single-coding neurons are comparably distributed (χ2(1, 5372) = 0.0057); dual-coding (χ2(1, 5372) = 61.336) and triple-coding (χ2(1, 5372) = 30.447) neurons are overrepresented in dHPC→NAc neurons.
- (G) Conjunctive-coding neurons allow a linear decoder to classify the presence of reward zone more accurately than non-conjunctive coding neurons (Wilcoxon’s W (18) = 14.0).
- See also Figure S6.As conjunctive coding has been suggested to aid downstream linear decoders to select task-appropriate actions (55, 61), we wondered if this increased conjunctive code might allow linear decoders to identify the presence of the reward zone more correctly in our task.
- We thus trained an SVM-based linear classifier on each trial’s odd/even laps’ reward zones and tested the decoding accuracy on even/odd laps, based on conjunctive or randomly sample size-matched non-conjunctive coding neurons (Figure 8F).
- We found enhanced reward zone decoding accuracy for conjunctive compared to non-conjunctive coding neurons (p < 0.001, Wilcoxon’s test; Figure 8G).

## Figure Descriptions

### Figure 1.
Dual-color two-photon calcium imaging of dHPC allows projection-specific activity monitoring during goal-directed navigation.(A-D) Training mice on a spatial reward learning task. (A) Schematic of behavioral task. Mice moved on a cue-enriched self-propelled treadmill belt of 360 cm length and obtain

### Figure 2.
dHPC→NAc neurons carry enhanced and more reliable spatial information.(A) Excerpt from one representative recording session showing behavioral activity (top) and denoised neural activity of identified place cells (bottom) over the course of several minutes from one mouse. White vertical lines mark n

### Figure 3.
dHPC→NAc place fields are modulated by local cues and reward zone.(A) Heat maps of dHPC− (left) and dHPC→NAc (right) place cells’ normalized position-binned average calcium events, ordered by place field location. Texture boundaries are indicated as white dashed lines. Yellow rectangle represents re

### Figure 4.
Speed-inhibited cells are overrepresented in dHPC→NAc neurons.(A-D) Speed-excited dHPC neurons. (A and B) Representative example of one speed-excited neuron. (A) Sample traces of velocity, position and one neuron’s denoised calcium activity. Note the increased calcium activity in times of high veloc

### Figure 5.
dHPC→NAc neurons are excited by appetitive licking and are over-represented in lick-excited neurons.(A-C) Appetitive licking is accompanied by increased neural activity in dHPC→NAc neurons but not dHPC− neurons. (A) Representative example showing reward dispensation (purple bar) and appetitive licki

### Figure 6.
Optogenetic stimulation of dHPC axons in NAc induces mouth movement and deceleration.(A-C) Tracking of orofacial movements via infrared camera recordings. (A) Example still image from near-infrared camera, sampled at 75 Hz. (B) False-color coded motion energy (pixel-by-pixel intensity difference to 

### Figure 7.
Enhanced conjunctive coding of space, velocity and licking in NAc-projecting neurons.(A and B) Conjunctive coding of space and velocity. (A) Venn diagrams of dHPC− (left) and dHPC→NAc (right) place cells and their overlaps with negatively (ocher) and positively (purple) tuned speed cells. Numbers sh

### Figure 8.
A generalized linear model confirms enhanced conjunctive coding in NAc-projecting neurons.(A) Schematic of the generalized linear model (GLM) using position, velocity, and appetitive licking data as predictors for each neuron’s calcium activity (left). Example modelling approach for a triple conjunc

### Figure S1.
Spatial reward learning task.(A and B) Sample infrared images of face (A) and body (B) that were continuously captured at 25/75 Hz. (C) Image of one head-fixed experimental mouse from top, illustrating craniotomy and head-fixation. (D) Sample image of two-photon imaging of a head-fixed mouse on trea

### Figure S2.
In vivo dual-color two-photon imaging of dynamic GCaMP and static mCherry signals.(A) Sample field of view (FOV) of one imaged region crossing putative CA1 and prosubiculum (pSub). Green channel shows GCaMP6s local correlations image, red channel shows average motion-corrected mCherry signal. (B) De

### Figure S3.
Spatial tuning of different neurons in sample FOVs.Three representative fields of view (FOVs) from three different mice are shown, with single-lap spatial calcium activity of each 10 representative neurons, some putatively NAc-projecting. FOV information is shown on top, including numbers of identif

### Figure S4.
Place field distribution across the belt and behavioral performance.(A) Extent of place fields of dHPC− (left) and dHPC→NAc (right) place cells, sorted by each place cell’s center of mass (COM). Turquoise represents place field, yellow represents COM, black lines represent left and right borders of 

### Figure S5.
Lick modulation during consumption and general licking.(A-C) Consummatory licking leads to a depression in neural activity. (A) Sample experiment showing reward dispensation (purple bars) and consummatory licking onsets (golden vertical lines) and population calcium activity from dHPC− (green) and d

### Figure S6.
Generalized linear model reveals coding differences for dHPC→NAc neurons.(A) GLMs’ explained variance R2 is significantly lower for dHPC→NAc neurons (Welch’s t (615.15) = 2.147, p = 0.032). (B) Scaled feature importance (standardized GLM coefficients retrieved by H2O’s varimp() method) is higher in 

## References
Total references in published paper: 89

### Key References (from published paper)
- What Are Memories For? The Hippocampus Bridges Past Experience with Future Decisions (, 2020)
- Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit f (, 1973)
- LOSS OF RECENT MEMORY AFTER BILAT-ERAL HIPPOCAMPAL LESIONS (, 1957)
- Spatial correlates of firing patterns of single cells in the subiculum of the freely moving rat (, 1994)
- Cell type, sub-region, and layer-specific speed representation in the hippocampal–entorhinal circuit (, 2020)
- The contributions of position, direction, and velocity to single unit activity in the hippocampus of (, 1983)
- Place Cells, Grid Cells, and the Brain’s Spatial Representation System (, 2008)
- Spatial goal coding in the hippocampal formation (, 2022)
- Spatial and behavioral correlates of hippocampal neuronal activity (, 1989)
- Hip-pocampal Neurons Encode Information about Different Types of Memory Episodes Occurring in the Sa (, 2000)
- What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior (, 2018)
- Organization of cell assemblies in the hippocampus (, 2003)
- Computational analysis of the role of the hippocampus in memory (, 1994)
- Heterogeneity within classical cell types is the rule: lessons from hippocampal pyramidal neurons (, 2019)
- CA1 pyramidal cell diversity enabling parallel information processing in the hippocampus (, 2018)
- Selective information routing by ventral hippocampal CA1 projection neurons (, 2015)
- Robust information routing by dorsal subiculum neurons (, 2021)
- Organization of the projections from the subiculum to the ventral striatum in the rat. A study using (, 1987)
- The distribution of the projection from the hippocampal formation to the nucleus accumbens in the ra (, 1982)
- The Nucleus Accumbens: An Interface Between Cognition, Emotion, and Action (, 2015)
- The nucleus accumbens as a nexus between values and goals in goal-directed behavior: a review and a  (, 2013)
- From motivation to action: Functional interface between the limbic system and the motor system (, 1980)
- The hippocampal–striatal axis in learning, prediction and goal-directed behavior (, 2011)
- Synchronous Activity in the Hippocampus and Nucleus Accumbens In Vivo (, 2001)
- Pennartz. Hippocampus Leads Ventral Striatum in Replay of Place-Reward Information (, 2009)
- Spatial, movement- and reward-sensitive discharge by medial ventral striatum neurons of rats (, 1994)
- Spatial Localization in the Morris Water Maze in Rats:: Acquisition Is Affected by Intra-Accumbens I (, 1994)
- Functional Interaction between the Hippocampus and Nucleus Accumbens Shell Is Necessary for the Acqu (, 2008)
- A Hippocampus-Accumbens Tripartite Neuronal Motif Guides Appetitive Memory in Space (, 2019)
- Synaptic and Behavioral Profile of Multiple Glutamatergic Inputs to the Nucleus Accumbens (, 2012)

## Ground Truth Reference
- Figures: 14
- Tables: 0
- References: 89