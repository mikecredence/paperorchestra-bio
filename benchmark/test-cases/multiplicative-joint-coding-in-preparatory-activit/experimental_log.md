# Experimental Log: Multiplicative Joint Coding in Preparatory Activity for Reaching Sequence in Macaque Motor Cortex

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsBehavioral taskThree rhesus monkeys (Macaca mulatta, male 5-10 kg) performed the memory-guided double-reach task (Fig.
- After 300 ms, in 1/3 of the trials (single-reach, SR), another green dot was presented as a reaching goal for 400 ms (cue period) at one of the six corners of a regular hexagon (i.e., at directions of 0°, 60°, 120°, 180°, 240°, or 300°).
- After the peripheral cue was extinguished, there was a memory period of 400-800 ms.
- The triangle was displaced from the square by 120° clockwise (CW, 1/3 of trials) or 120°counterclockwise (CCW, 1/3 of trials).
- For a correct trial, the green square would reappear after the 1st reach, and the triangle would appear in purple after the 2nd reach.
- All 18 conditions (three trial types × six directions) were pseudo-randomly interleaved.
- Event markers are denoted as the GO signal (GO), the 1st/only movement onset (MO), the 1st/only movement end (ME), and the 2nd movement onset (MO2).biorxiv;2023.04.05.535305v1/FIG1F1fig1Figure 1Paradigm and behavior.a.
- In double-reach (DR) trials, two targets (a square and a triangle) were presented simultaneously in cue period, and then extinguished; the monkeys were required to hold the central target for a 400-800 ms memory period until it was turned off (GO signal).
- Next, monkeys finished reaching both targets in the sequence of the square to the triangle within 700-1200 ms.
- The triangles were located 120° from the squares in CW or CCW directions.
- Hand trajectories in different conditions are grouped by their 1st/only reach direction from monkey C.
- No significant difference was found before the end of 1st/only reach (one-way ANOVA, p>0.05).
- The Pearson correlation coefficient of the speed profile until 1st movement end between double reach and single reach was 0.99±0.006 (mean±sd) and of sEMG of extensor digitorum communis (EDC) was 0.99±0.005 (mean±sd) for monkey C.Hand trajectories exhibited a stereotype movement pattern in each cond
- All 1st reaches started from the center and moved towards the corresponding target in each condition (Fig.
- The Pearson correlation coefficient of speed profiles until ME between DR and SR was 0.99±0.006 (mean±sd), and of surface electromyography (sEMG) of extensor digitorum communis (EDC) was 0.99±0.005 (mean±sd) for monkey C (Fig.
- In addition, the dwell time on the 1st target was 194±75 ms (mean±sd) for monkey C, 350±110 ms (mean±sd) for monkey G, and 150±47 ms (mean±sd) for monkey B.
- The median duration of DR was 586±95 ms (mean±sd) for monkey C, 818±131 ms (mean±sd) for monkey G, and 481±72 ms (mean±sd) for monkey B, averaged across conditions.
- These results verified the expected transitory dwell on the 1st target in this task, and indicated behavioral consistency between SR and the 1st reach of DR in the same direction, in terms of hand trajectory, speed profile, and sEMG.Heterogeneity in neuronal activity indicated mixed selectivityAll e
- We collected 322 well-isolated task-related neurons from single-electrode recordings (224 from monkey B, 98 from monkey C left hemisphere) and 202 units sorted from array recordings (44 from monkey G, 158 from monkey C right hemisphere) in motor cortex (Fig.
- Figure 2 illustrates four representative cells.
- 2a exhibited a two-peak firing pattern in DR, each peak after a movement onset, while it had only one burst in SR.
- 2b fired with a constant PD towards the lower left.
- Surprisingly, even though its directional selectivity was remarkably similar for both SR and DR, the firing rate was significantly higher in DR (according to the 95% confidential interval plotted in shade), indicating that it conveyed information regarding target-movement number.
- Also, the preparatory activity would diverge with the 2nd reach before GO and MO in neurons, as in Fig.
- 2c and 2d.biorxiv;2023.04.05.535305v1/FIG2F2fig2Figure 2Examples of cells in motor cortex showing heterogeneous firing patterns.In each panel (a-d), the six subplots show PSTHs of the same neuron in three conditions with 1st reach toward the corresponding location (e.g., the upper-right subplot deno
- Rasters are plotted at the top of each PSTH (20-ms SD Gaussian kernel).
- Spike trains in SR (black line), CW (blue line), and CCW (red line) trials are aligned to the 1st/only movement onset (MO) in a, b, d, but aligned to GO-cue in c.
- Time of GO (magenta dots), MO (green dots), the 2nd movement onset (MO2, cyan dots), and the 2nd movement end (yellow dots) are presented in the rasters.We further examined the proportion of neurons with sequence selectivity in three periods: preparatory (600 ms before GO), pre-movement (200 ms befo
- Among the 322 neurons recorded by single-electrodes, 52% exhibited significantly different firing rates for SR and DR in the preparatory period (Wilcoxon rank sum test, p<0.05).
- This proportion increased to 68% in the pre-movement period, and then to 84% in the peri-movement period (Wilcoxon rank sum test, p<0.05).
- As for the comparison between CW and CCW trials, 30%, 48%, and 72% of neurons showed significant differences during the preparatory, pre-movement, and peri-movement periods, respectively (Wilcoxon rank sum test, p<0.05).
- For the 202 array-recorded neurons, 80%, 89%, and 97% were significantly tuned to sequence during preparatory, pre-movement, and peri-movement periods, respectively (Wilcoxon rank sum test, p<0.05).
- In comparing CW and CCW trials, the proportions were 48%, 68%, and 87% during the preparatory, pre-movement, and peri-movement periods, respectively (Wilcoxon rank sum test, p<0.05).
- For this kind of model, sequential modulation is a parallel process resulting from the preparation of the 2nd movement while the 1st movement still is in flight, as pointed out by Ames et al.
- Here, we focused on directional tuning alone, and defined an ‘additive model’ as follows:



where FR is neuronal firing rate, θ1is the movement direction of the 1st reach, θ21 is the 2nd movement direction starting from the 1st reaching endpoint, that is, in execution coordinates, since the regress
- S2) indicates that the 2nd reach is predominately conveyed in execution coordinates (movement direction) rather than visual coordinates (target location).
- θPD represents the PD, a1and a2 are coefficients, and c is the baseline firing rate.
- For simplicity, we assumed the PD to be consistent for both terms at the same time.However, since the visual targets in our task were presented simultaneously, rather than sequentially as in many previous studies 9, 15, 16, 28, the monkeys were more likely to prepare the entire reaching sequence bef
- For computational convenience, and as inspired by a previous study suggesting that hand speed may act as a ‘gain field’ to the directional cosine tuning function 30, we propose a ‘multiplicative model’ to depict the potential nonlinear gain-modulation between both elemental movements:



where b is 
- If we set Δθ = (θ21 − θ1)/2, then the multiplicative term in Eq.3 can be transformed into a summation form that includes a doubled frequency (Eq.
- 1a), we trained monkey C to perform an extended version of the task with multi-direction, in which the angle between the square and triangle could be 60°or 120°in both CW and CCW directions as well as 180°.
- This multi-direction task has 36 conditions in total (six SR and 30 DR).We tested these two possibilities on condition-averaged normalized firing rates with a 200-ms sliding window 31.
- 3, in comparison with its actual PSTHs.
- 2) reproduced the peri-movement firing pattern, but it did not capture the sequence-specific modulation during preparation.
- 3) better captured neural activity during the preparatory period, while losing that during the peri-movement period.
- 4, we plotted directional tuning curves of the same example cell with its actual firing rates (Fig.
- 4, left panel), along with reconstructed firing rates by additive (Fig.
- 4, middle panel) or multiplicative (Fig.
- The real firing rate for plotting and fitting was normalized and averaged around MO (−100∼100 ms to MO, peri-MO) and around ME (100∼300 ms to MO, peri-ME), respectively.
- 4a), the neural tuning curves consist mostly of two peaks and were only replicated by the tuning curves of the multiplicative model.
- 4b), PD shifted with conditions in data, and only the additive model yielded a similar outcome.
- Comparing two epochs, the two coding possibilities could co-exist and might alternate.biorxiv;2023.04.05.535305v1/FIG3F3fig3Figure 3Model fitting of an example neuron.Each row shows conditions with the same 1st reach (black arrow); the 2nd reach is plotted in different colors (CW 60° in green, CW 12
- All activity is aligned to MO (marked by the gray dots under timeline, time window is −800 ∼ 600 ms to MO).biorxiv;2023.04.05.535305v1/FIG4F4fig4Figure 4Joint tunings of the example neuron around movement onset and end.a.
- 3 were plotted around MO (−100∼100 ms to MO, peri-MO).
- R2 showed the goodness-of-fit of the model tuning curve.
- Similar with a, directional tuning curves around ME (100∼300ms to MO, peri-ME).To further investigate the temporal dynamics of joint-coding rules, we proposed a ‘full model’ to combine the two modulation forms:



where descriptions of notations are the same as in Eq.
- 3, defining a1as the 1st reach weight, a2as the additive weight, and b as the multiplicative weight.
- The fluctuation of the regression coefficients (a1, a2, and b) reflects the time-varying contribution of the corresponding terms, thus enabling the full model to profile the transition of coded objects.We compared the goodness-of-fit of the full model with that of the additive model, the multiplicat
- For M1 neurons (n=118), the goodness-of-fit for all models gradually increased during preparation, and the multiplicative model was significantly better than the additive model at MO (two-tailed Wilcoxon signed rank test, p=1.2e-05).
- Similar results were found in M1 data in all monkeys (Fig.
- S3, single-electrode recording from monkeys B and C, and array data from monkey G).
- For PMd neurons (n=40), the adjusted R2 remained stable during preparation.
- No significant difference was found between two models before MO (two-tailed Wilcoxon signed rank test, p=0.06).
- It seems that the transition from multiplicative to additive coding was different in M1 and PMd.biorxiv;2023.04.05.535305v1/FIG5F5fig5Figure 5Dynamics of goodness-of-fit and coefficienta.
- Results of regression on M1 neurons in array dataset from monkey C are illustrated at the population level.
- Left: Goodness-of-fit was evaluated with averaged adjusted R2 for all fitting models in a 200-ms sliding window (with twice standard error in shade).
- The upper line showed the significance (p<0.0005) of comparison between performance of multiplicative (purple line) and additive (blue line) model.
- Middle: Scatters compared the goodness-of-fit at MO (−100∼100 ms to MO) between the multiplicative and additive models, each dot represents the result of a neuron.
- For M1 neurons, the weights of the 1st reach and the multiplicative term ramped up over the chance level (given by a permutation test, see Methods) during preparation, whereas the additive weight remained at the chance level in preparation and mainly increased after MO.
- This contemporaneous activation of coefficients was similar to the situation in prefrontal cortex where neurons were modulated by both direction and sequence 32–34.
- S3), suggesting a common transition from a gain-modulation interplay during motor preparation to a concurrent coding during motor execution.
- This concurrence has been reported by the previous study 27.
- For PMd neurons, the overall encoding process was essentially consistent with that in M1: the 1st movement → the multiplicative term → the additive term.
- However, in PMd, these three components made comparable contributions in the preparation period, and there was no obvious peak of the 1st reach and multiplicative coefficients.
- The onset times for the increase of the additive coefficient, and the decrease of the 1st reach and multiplicative coefficients, were much earlier in PMd than in M1, implying that PMd takes precedent in coding of the 2nd reach.So far, we have analyzed the linear and nonlinear components comprised in
- The multiplicative joint coding, revealed by the multiplicative model and validated by the multiplicative weight in the full model, now becomes a key concern because it would be apparently a unique signature of continuous motor sequences.Multiplicative coding embodied in initial statesAccording to o
- From the dynamical systems perspective, preparatory activity would be set to a subspace optimal as initial states to trigger motor generation 35.
- Firstly, principal component analysis (PCA) was applied to the preparatory neural activity during a period of 600 ms before GO.
- Next, the Fisher’s linear discriminant analysis (LDA) was utilized to find the optimal discriminant projection in accordance with tagged conditions 36.
- Neural states clustered by conditions, as visualized in the 2-d projections found by LDA (Fig.
- Then, we projected both DR and SR data onto the resulted space and found that neural states of both DR and SR trials clustered according to their 1st or only reach direction.
- However, the variance explained were higher for SR than DR (For monkey C array, variance explained of SR is 10.9%, DR is 7.8%.
- For monkey B, variance explained of SR is 9.0%, DR is 6.6%.
- For monkey C single electrode, variance explained of SR is 6.2%, DR is 5.6%.
- For monkey G, variance explained of SR is 31.6%, DR is 27.5%.).
- To neutralize the tuning for the immediate movement, we used DR trials with the same 1st reach direction alone for the PCA-LDA analysis.
- Therefore, relatively low-dimensional neural states grouped by the 1st reach directions, could be projected again onto dimensions maximizing the difference brought by the 2nd reach directions.
- The result of trials where the 1st reach direction was towards the lower-right was visualized, with trials classified into six clusters corresponding to their subsequent reach directions (Fig.
- 6c; subsequent reach directions are indicated by markers; ten-fold cross-validation accuracy was higher than 0.6, above the chance level for the classification of six conditions, 1/6, excluding LDA overfitting).
- Interestingly, in some conditions, DR trials obviously clustered in order from CW 60°to CCW 60°, and the CW and CCW states were located on both sides of the 180°states.
- S5) may signify a condensation of subsequent movement information in the strong representation of occurrent movement.
- S6-S8).biorxiv;2023.04.05.535305v1/FIG6F6fig6Figure 6Projection of preparatory activity onto PCA-LDA resulting initial state space.a.
- Neural states of DR trials also clustered into six groups according to their 1st reach direction when projected onto the SR space.
- LDA classified neural states of trials with the same 1st reach direction into clusters grouped by 2nd reach directions, forming an initial state space for the subsequent movement.
- Colors indicate the 1st movement directions; DR trials are presented in the same color family of related SR trials.
- Markers indicate 2nd reaching direction.
- The ellipses show the covariance projection of related conditions.Multiplicative coding preserves linear readout of immediate reachAs several investigators have pointed out 12, 21, 37, 38, as well as PCA results suggested, the neural population preserves a reliable readout of ongoing movement direct
- Since nonlinear mixed selectivity is believed to form high-dimensional neural representations that guarantee the linear readout of particular parameters 39, we speculate that each linear readout in sequential movements benefits from multiplicative joint coding.We checked the linear readout of immedi
- To figure out the impact of the multiplicative or additive joint coding on PV, we adopted a proved simulation method 40 to obtain surrogate data corresponding to the cosine, additive, and multiplicative models (see Methods).
- Each dataset consisted of 200 model neurons with activity in an epoch of 600 ms from preparatory activity until the 1st reach end.
- Those additive and multiplicative neurons were regulated by a fixed 2nd reach direction as well.
- Obviously, the direction inducing the highest firing rate changed in additive and multiplicative neurons, compared to the ‘single cosine’ neurons, resulting in a modulated tunning curve (Fig.7b).
- Interestingly, PVs in the multiplicative DR dataset correctly and stably pointed to the immediate reach direction as in the SR condition, whereas PVs in the additive DR dataset deviated from the desired direction (Fig.7c).
- These simulations show that multiplicative joint coding can preserve a robust linear readout of immediate reach direction, even containing subsequent reach directions.biorxiv;2023.04.05.535305v1/FIG7F7fig7Figure 7Simulation of neural tunings on population vector during single and double reach.a.
- Averaged firing rates of different conditions (1st reach directions) are shown in corresponding colors.
- Population vectors were calculated every 50 ms.
- The population vector of multiplicative dataset pointed in the same direction as PV of single cosine dataset, while the PVs of additive dataset shift away from the desired reaching direction.Multiplicative joint coding emerged in recurrent neural network (RNN) generating motor sequenceDue to their f
- In contrast to previous work in which RNNs were instructed to generate velocity 40 or EMG 44, our model was required to produce PV.
- 7).biorxiv;2023.04.05.535305v1/FIG8F8fig8Figure 8Results of an RNN model.a.
- The black dots denote target on (TO), the 1st movement onset (MO), and the 2nd movement onset (MO2), respectively.
- The R2 was calculated across nodes.
- Time markers are ticked as: target on (TO), go-cue on (GO), the 1st movement onset (MO), and the 2nd movement onset (MO2).The trained RNN performed well (for training set R2=0.9711±0.0044, for validation R2=0.8976±0.1070, mean±SD; see Methods).
- For the node 088, the two bumps of its response indicate that it is closely related to the ongoing movement, which is typical for neurons in M1.
- The response of the node 061 seems more complex, as the augment around MO does not occur in all conditions.
- Interestingly, this node appears to have ‘direction selectivity’, the only exceptive movement direction for the 1st reach (in cyan) induces obviously distinguished response.
- 8c, the profile of regression coefficients of model nodes largely resembles that of real data (Fig.
- 5a, right, Fréchet distance = 0.47, see Methods).
- The weight of the 1st reach peaks at MO and decays afterwards.
- The weight of the additive term, which relates to the 2nd reach, reaches its apex around MO2 with a slightly smaller magnitude.

## Figure Descriptions

### Figure 1
Paradigm and behavior.a. Three types of trials were pseudo-randomly interleaved in each session. In single-reach (SR) trials, monkeys had to perform memory-guided center-out reach. In double-reach (DR) trials, two targets (a square and a triangle) were presented simultaneously in cue period, and the

### Figure 2
Examples of cells in motor cortex showing heterogeneous firing patterns.In each panel (a-d), the six subplots show PSTHs of the same neuron in three conditions with 1st reach toward the corresponding location (e.g., the upper-right subplot denotes the 1st reach to 60°). Rasters are plotted at the to

### Figure 3
Model fitting of an example neuron.Each row shows conditions with the same 1st reach (black arrow); the 2nd reach is plotted in different colors (CW 60° in green, CW 120° in blue, 180° in purple, CCW 120° in red, CCW 60° in orange; here angle is according to the target locations in cue period). Four

### Figure 4
Joint tunings of the example neuron around movement onset and end.a. Directional tuning curves of the example cell in Fig. 3 were plotted around MO (−100∼100 ms to MO, peri-MO). Left: Normalized firing rate in DR were trial-averaged and plotted in corresponding condition colors. Tuning curves were f

### Figure 5
Dynamics of goodness-of-fit and coefficienta. Results of regression on M1 neurons in array dataset from monkey C are illustrated at the population level. Left: Goodness-of-fit was evaluated with averaged adjusted R2 for all fitting models in a 200-ms sliding window (with twice standard error in shad

### Figure 6
Projection of preparatory activity onto PCA-LDA resulting initial state space.a. Projection on SR space. Neural states of SR trials were clearly clustered according to their reaching directions. b. Neural states of DR trials also clustered into six groups according to their 1st reach direction when 

### Figure 7
Simulation of neural tunings on population vector during single and double reach.a. Example neurons of three simulated datasets. Averaged firing rates of different conditions (1st reach directions) are shown in corresponding colors. These three example model neurons were simulated according to the s

### Figure 8
Results of an RNN model.a. Schematic of the RNN model. The RNN model consisted of an input layer, a hidden layer, and an output layer. The input layer received signal for position of two targets simultaneously, while the output layer produced population vector (PV), whose magnitude reflects the degr

## References
Total references in published paper: 59

### Key References (from published paper)
- On the relations between the direction of two-dimensional arm movements and cell discharge in primat (, 1982)
- Motor cortical activity during drawing movements: single-unit activity during sinusoid tracing (, 1992)
- Neuronal Specification of Direction and Distance during Reaching Movements in the Superior Precentra (, 1993)
- Motor cortical representation of speed and direction during reaching (, 1999)
- Spatiotemporal tuning of motor cortical neurons for hand position and velocity (, 2004)
- Sensing with the motor cortex (, 2011)
- Perspectives on classical controversies about the motor cortex (, 2017)
- Sequential organization of multiple movements: involvement of cortical motor areas (, 2001)
- Cortical activity in the null space: permitting preparation without movement (, 2014)
- Movement parameters and neural activity in motor cortex and area 5 (, 1994)
- Anticipatory activity in primary motor cortex codes memorized movement sequences (, 2005)
- Control of remembered reaching sequences in monkey (, 1996)
- Control of remembered reaching sequences in monkey (, 1996)
- Neural population partitioning and a concurrent brain-machine interface for sequential motor functio (, 2012)
- Encoding of Serial Order in Working Memory: Neuronal Activity in Motor, Premotor, and Prefrontal Cor (, 2018)
- Motor cortical encoding of serial order in a context-recall task (, 1999)
- Neuronal activity in the primate premotor, supplementary, and precentral motor cortex during visuall (, 1991)
- The parietal reach region codes the next planned movement in a sequential reach task (, 2001)
- Neuronal activity in motor cortical areas reflects the sequential context of movement (, 2004)
- Skill representation in the primary motor cortex after long-term practice (, 2007)
- Sub-optimal allocation of time in sequential movements (, 2009)
- Planning multiple movements within a fixed time limit: The cost of constrained time allocation in a  (, 2010)
- Motor control is decision-making (, 2012)
- Neural Competitive Queuing of Ordinal Structure Underlies Skilled Sequential Action (, 2019)
- Independent generation of sequence elements by motor cortex (, 2021)
- Simultaneous motor preparation and execution in a last-moment reach correction task (, 2019)
- The posterior parietal cortex encodes in parallel both goals for double-reach sequences (, 2008)
- Decoding arm speed during reaching (, 2018)
- Cortical correlates of fitts’ law (, 2011)
- Parallel processing of serial movements in prefrontal cortex (, 2002)

## Ground Truth Reference
- Figures: 8
- Tables: 0
- References: 59