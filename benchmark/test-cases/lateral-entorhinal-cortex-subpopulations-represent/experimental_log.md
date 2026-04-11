# Experimental Log: Lateral entorhinal cortex subpopulations represent experiential epochs surrounding reward

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsTwo-photon imaging of the lateral entorhinal cortex in behaving miceTwo-photon functional imaging offers the capability to record from large numbers of neurons simultaneously, but this technique has not previously been used in the LEC during behavior34.
- As it is situated ventral to the rhinal fissure36, the LEC is a lateralized structure in rodents, and direct access with a microscope requires approaching from an angle greater than 90 degrees to the horizontal plane.
- A further complication is the surrounding anatomy: the pinna, nearby vasculature such as the petrosal squamosal sinus, and protrusions of the skull (zygomatic process) each impinge upon optical access with a microscope37.
- To overcome these limitations, we developed surgical methods to implant a cranial window (3 mm round coverslip) with an attached microprism (2.0 mm square) to rotate the imaging plane 90 degrees (Figure 1b).
- Using this approach in transgenic mice expressing the fluorescent Ca2+ indicator GCaMP6s38,39, we could capture a large field of view of the LEC using a conventional upright two-photon microscope and access depths > 250 µm (Figure 1c) in head-fixed mice running on a treadmill to traverse a 1-D virtu
- Movies were motion corrected and cells identified and segmented using Suite2p40.
- Neuropil-corrected, baseline-adjusted, and deconvolved neural Ca2+ transients (referred to here as “firing”) were recovered using a novel iterative algorithm (Methods).
- In a typical imaging field of 700 x 700 µm, ~500 active cells were observed during behavior (mean across 47 imaging fields: 496 cells; range: 150 to 843 cells) (Figure 1d).
- Mice learned over several training sessions to decelerate and lick in anticipation of the reward location, where a drop of water was delivered (Figure 2a).
- In parallel, we also performed two-photon Ca2+ imaging of populations of neurons in MEC and in CA1 in separate groups of mice implanted with microprisms41 or cannulas42, respectively (Figure 2b).
- We first show data from the most commonly used reward location (2.3 m) and pool data from the other reward locations (0.7 m and 1.5 m) where appropriate.biorxiv;2023.10.09.561557v1/FIG2F2fig2Figure 2:Prominent reward clustering in LEC with segregation of pre- and post-reward populationsa) Head-fixed
- Treadmill velocity and detected licks, averaged over 43 traversals, are binned at 1 cm intervals with stationary periods excluded (Methods).
- Once behavior reached criteria (at least two laps per minute over a ~40 minute training session along with the presence of anticipatory licking and deceleration for reward), imaging sessions began.
- On subsequent days, reward location was moved to either 0.7 m or 1.5 m.
- At least one session with the new reward location was interspersed to allow for it to become familiar to the animal as assessed by anticipatory behavior of the new reward location.b) Schematics of imaging approaches using implanted microprisms (LEC, MEC) or cannulae (CA1).c) Population spatial firin
- Each row of the image is the firing of one neuron averaged over odd laps, binned at 1 cm intervals after Gaussian filtering (170 ms standard deviation), and normalized to its maximum value.
- Histograms underneath each plot show proportion of peak locations for neurons in 10-cm bins, with ‘chance’ calculated as expected number in each bin if uniformly distributed (1/31 bins) and ‘reward cells’ those that peak within the blue rectangle (±40 cm from reward).
- Black lines indicate 1, 2, and 3 m locations.
- Correlations are calculated between average firing on even and odd laps, so the diagonal is not necessarily equal to one.e) Quantification of spatial field widths in each region, computed as the distance of the track for which the firing rate is at least 30% of the maximum for each spatial cell.
- Statistical tests performed between each pair of regions (2-sample t-test).f) Fraction of active cells that are spatial cells and fraction of spatial cells that are reward cells in each region.
- Statistical tests performed between each pair of regions (2-sample t-test) and, for reward cells, compared to chance as well (1-sample t-test).
- Since the reward zone is 80 cm total and the track length in 310 cm, chance is 80/310, or ~0.26.g) Reward clustering ratio, calculated as the number of cells that peak in each reward zone (blue rectangle shown in c) divided by the expected number of cells if peaks were uniformly distributed along th
- Statistical tests performed between each pair of regions (2-sample t-test) and compared to chance (1-sample t-test).h) Reward clustering ratio stratified by imaging depth.
- For LEC: up to 150 µm below dura (layer II) and at least 200 µm below dura (layer III); for MEC: up to 150 µm below dura (nominal layer II) and at least 150 µm below dura (nominal layer III).
- Statistical tests performed between each pair of regions (2-sample t-test) and compared to chance (1-sample t-test).
- For all statistical tests: * indicates p < 0.05 and n.s.
- indicates p > 0.05.Among active neurons in the LEC, we selected for those with significant spatial information along the track43 (Methods).
- From 17 fields-of-view across 7 mice with the reward located at 2.3 m, 2016 such spatial cells were found, which represent 24.9% of active cells (Figure 2f).
- Across all reward positions, we identified 3956 spatial cells out of 14489 active neurons from 32 fields-of-view (Supplementary Tables 1 and 2).
- Nearly half of spatial cells in LEC were active near the reward location, with such reward cells defined as spatial cells whose mean firing peaked within 40 cm of the reward location (Figure 2c,f).
- By comparison, MEC spatial cells were active nearly uniformly across the track, and the fraction active around reward was as expected by chance, while in CA1 an enhanced fraction of cells was active near reward, but less than what was observed in LEC (Figure 2c,f and Supplementary Figure 2a).
- Track position could still be decoded from activity in non-reward spatial cells in LEC, but the decoder performance error was higher for LEC than in MEC or CA1 (p < 0.05, 2-sample t-test; Supplementary Figure 2c).
- Cells from all three brain regions also tended to cluster near the start and end of the track, but we focused our analysis on the cells active around the reward location.biorxiv;2023.10.09.561557v1/TBLS1T1tblS1Supplementary Table 1Multiway analysis of variance (ANOVA) was performed using the anovan 
- For this data, ‘Spatial neurons’ shows number of spatial neurons for familiar and novel reward location, respectively.Beyond clustering near the reward, LEC spatial cells had wide spatial fields and were separated by whether they were active before or after the reward location (Figure 2c).
- These features are clearly visible when plotting the correlation matrix of the mean spatial firing maps, sorted by where each cell peaked (Figure 2d).
- While MEC shows a clear diagonal band structure, indicating narrow spatial fields across all track locations, LEC shows a block-like structure, indicating wide spatial fields (Figure 2e) that largely segregate into pre-reward-active neurons and post-reward-active neurons, a division confirmed by k-m
- This reward clustering ratio was enhanced in LEC for pre-reward compared to CA1 and MEC and in both LEC and CA1 for post-reward (Figure 2g).The superficial layers of LEC are known to differ in cell type and connectivity21, so we next explored whether laminar differences may relate to reward clusteri
- In particular, layer II contains fan cells, which receive an outsized number of dopaminergic inputs from the VTA35,44, suggesting a potential region where reward information may enter the system.
- We imaged at depths targeting the two layers: 80-150 µm below dura for layer II (23 fields) and 200-250 µm below dura for layer III (9 fields) (Supplementary Figures 1 and 2b).
- While both regions show preferential firing near the reward location, the enhancement of firing in the pre-reward region was significantly larger in layer II versus layer III (Figure 2h).
- To determine whether the differences in reward-related neural responses across LEC layers could be explained by other factors, we performed a multiway analysis of variance using imaging depth, age, gender, and deceleration (a behavioral measure of task performance) as predictors of reward clustering
- To disentangle whether reward cells are encoding spatial information (track position) or reward itself, the reward location was moved without any cue, indication, or change to the environment in the middle of a session after ~40 laps with a familiar reward location.
- Mice learned to anticipate the new reward location by shifting their deceleration along the track (Figure 3a).
- Imaging was performed throughout the session, thus capturing representations both before and after the reward switch in the same cells.biorxiv;2023.10.09.561557v1/FIG3F3fig3Figure 3:Dedication of pre- and post-reward populations in the LECa) Licking (percent of laps with contact of sensor) and veloc
- In this example session, the reward was moved earlier on the track, from a familiar location (rew1, 2.3 m, blue) to a new location (rew2, 1.5 m, green).
- Once a reward location became familiar, an imaging session was performed spanning ~15 minutes with the familiar reward location and ~15 minutes with the new reward location.b) Spatial firing (deconvolved Ca2+ transients) for three exemplar neurons from the same session as a, with ±SEM shown in light
- Imaging was performed for a subset of laps (56 laps before and 44 laps after change in reward location).c) Spatial firing patterns along the track and histogram of firing peaks for spatial cells sorted by their firing peaks with the familiar reward location, analogous to Figure 2c.
- Only cells that pass criteria for spatial information under both conditions are included.d) Dot raster of peaks for spatial cells in LEC, MEC, and CA1.
- Cells on the diagonal maintain their firing position along the track while cells at the intersection of reward locations (blue and green lines) adjusted their firing positions relative to the reward locations.e) Histograms measure the fraction of spatial cells that are stable after the reward locati
- For comparison, we computed the difference in peak location for even and odd trials with the original reward location (rew1-rew1); black rectangle represents mean ± SEM across sessions.
- Next, the fraction of reward cells that remain reward cells after the reward location change is quantified by the fraction of reward cells that maintain their peak location within 40 cm of the new reward location.f) Peak locations shown relative to reward locations with familiar reward condition on 
- Selected cells are chosen for being pre-reward cells with the familiar reward location (rew1) and spatial cells in both; what is shown here is where their peak locations are for the novel reward location (rew2).
- Statistical tests performed between each pair of regions (2-sample t-test).
- indicates p > 0.05.Some LEC neurons maintained their firing field with respect to track position (LEC stable spatial cell, Figure 3b) and others with respect to the reward location (LEC stable pre- and post-reward cells, Figure 3b).
- We plotted all spatial neurons before and after this change in reward location from 2.3 m to 1.5 m, sorted by their firing peaks with respect to the familiar reward location (Figure 3c).
- Indeed, relatively few LEC neurons continued to fire at the same track location, especially compared to MEC and CA1 (Figure 3d-e, Supplementary Figure 3a-b).
- Instead, over half of the cells active in the reward zone for the familiar location shifted their firing fields to the new reward location (stable reward cells), more than expected by chance.An even more significant picture of dedicated cell populations emerged when examining pre-reward and post-rew
- We found that nearly all pre-reward cells for the familiar reward location remained pre-reward cells relative to the new reward location and, similarly, post-reward cells remained post-reward relative to the new reward location (Figure 3f-h).
- The probability of a pre-reward cell remaining a pre-reward cell was 2.7x chance and 2.4x for post-reward cells (geometric mean of ratio for each session, Figure 3i).
- This dedication was largely absent in the MEC, as pre-reward cells for the familiar and new reward locations were not significantly related (Figure 3g,i) and the post-reward cells were only partially preserved (Figure 3h-i).
- Cells in CA1 showed a mixture of the strong dedication from LEC and the weak dedication from MEC (Figure 3g-i).
- When we teleported mice to new environments with unmarked reward locations, we found that reward dedication was similarly maintained in the new environment (1.5x for pre-reward and 2.3x for post-reward cells; Supplementary Figure 3c-h).
- Both behavioral changes (slowing, Figure 2a) and the firing in pre-reward neurons in LEC (ramping, Figure 4b) precede the reward, which led us to investigate two questions: first, what are the dynamics of population activity of the pre-reward cells, which may give insight into to the internal state 
- The number of pre-reward cells active (out of 61) is shown as the raw value (gray trace) and after applying a 2 s Gaussian filter (dark trace).e) Running velocity and number of pre-reward cells active on each lap.
- r indicates Pearson correlation coefficient.g) Pearson correlation coefficients for each session, calculated as in f, for fields with at least 10 pre-reward cells.
- Statistical tests performed between each pair of regions (2-sample t-test) and to zero as well (1-sample t-test).On average, mean firing in pre-reward LEC neurons ramped up until the reward was delivered (Figure 4b), similar to activity previously observed in other brain regions such as the ventral 
- Various models have been proposed47–49.
- For example, an increasing number of neurons might be recruited or firing in individual neurons could increase as the animal approaches reward, in which case ramping activity would be observed across the population on both individual trials and the trial averages (recruitment model, Figure 4a).
- Alternatively, the pre-reward population might undergo coherent state changes at different times or positions with respect to reward on each trial, in which case discrete changes in activity, not ramping, would be observed across the population on individual trials and ramping would only be observed
- We often observed step-like increases in the active number of neurons (Figure 4d-e).
- Indeed, when we used a hidden Markov model (HMM) to identify such transition times from inactive to active population states (Supplementary Figure 4a) and then plotted the firing rate of the pre-reward neurons aligned to these transition times (with each ‘epoch’ spanning the time between transitions
- We further calculated that 44% of the variance in single-lap activity was explained by a step increase.
- However, some ramping activity was still observed on top of the step-like change (Figure 4b).
- Interestingly, on individual trials we also observed state changes in mouse behavior: mice switched from a fast running speed to a much slower speed ahead of the reward location and maintained this slow speed until the reward was encountered (Figure 4d and Supplementary Figure 4b-c), with the timing
- To investigate whether the discrete behavior changes correlated with the LEC population state changes, as suggested by individual example trials (Figure 4d), we examined the relationship between the HMM state transition times with the deceleration times on each trial (Figure 4e).
- We found these times were highly correlated, both for the example session (Figure 4f) and across all LEC sessions (Figure 4g).
- A similar effect was observed for CA1 pre-reward cells, but no correlation was observed for MEC pre-reward cells (Figure 4g).
- At the time of reward delivery, we observed that LEC population firing increased dramatically and transiently, a signal not prominent in either MEC or CA1 (Figure 5a).
- Nearly 1 in 8 LEC neurons peaked within the first second after reward delivery.
- Using a shuffle test for significance of this firing peak, we developed criteria for ‘reward consumption active’ (RCA) neurons20 that contain such a peak in firing at reward, or RCA cells.
- Across all sessions, 13.7% of active LEC neurons (1978 of 14489) qualified as RCA cells (Figure 5b-c), and this proportion was similar between layers II and III of the LEC (Supplementary Figure 2b).
- The fraction of RCA cells was much lower in the MEC (299 of 9488, or 3.1%), while CA1 was intermediate (816 of 11564, or 7.1%) (Figure 5d).biorxiv;2023.10.09.561557v1/FIG5F5fig5Figure 5:A population of LEC neurons signal reward consumptiona) Mean transient rate relative to the time of reward deliver
- Fluorescence traces for a subset of laps are shown, with averages of all laps underneath for both fluorescence and inferred transient rate following deconvolution relative to a familiar reward location (rew1, blue) and a new reward location (rew2, green) in the same imaging session.
- Statistical tests performed between pairs of regions (2-sample t-test) or paired tests within LEC (1-sample t-test).
- indicates p > 0.05.e) Fraction of stable RCA cells (reward consumption active for both a familiar and a new reward location), either as a fraction of all active cells or as a fraction of RCA cells for the familiar reward location (rew1).
- Statistical tests performed between each pair of regions (2-sample t-test).
- indicates p > 0.05.Given that the reward consumption epoch, which determines whether a neuron is an RCA cell, is excluded from the calculation of spatial cells, we next asked whether and how the RCA cell population overlapped with spatial cells in LEC.
- We found that similar fractions of spatial and non-spatial cells were RCA cells (Figure 5d).
- The non-spatial ‘pure’ RCA cells, such as the exemplar shown (Figure 5c), were robustly active only during reward consumption.
- As for spatial cells, RCA cells were more common within the pre-reward cell population of LEC, but they were found within the post-reward population as well (Figure 5d).
- Importantly, when the reward location was moved, the reward consumption signal occurred at the new reward (Figure 5c,e), with a third of RCA cells in LEC maintaining their firing pattern with respect to reward time, higher than in CA1 and MEC (Figure 5e).
- When the environment was changed, again RCA cells in LEC maintained their firing pattern with respect to reward time in the new environment (Figure 5e).
- In these sessions, we still observed a dramatic and transient increase in firing immediately after reward delivery (for 1 s), as seen for RCA cells, but did not observe the increasing ramp in firing leading up to reward delivery nor the later increase in firing 2-4 s after reward delivery (Supplemen
- Thus, the signal carried by RCA cells appear to be a generalizable reward signal while the pre-reward and post-reward signals are specific to our navigation task.biorxiv;2023.10.09.561557v1/FIG6F6fig6Figure 6:LEC stably represents reward experience during learning while optogenetic inhibition of LEC
- Velocity along the track, binned at 1 cm intervals, is shown for the final 10 laps with the familiar reward location and the first 15 laps with the new reward location.
- Inset shows imaging paradigm (similar to Figure 3a).b) Line plots show deceleration and HMM transition times during the learning period, averaged across imaging sessions (only sessions with at least 10 pre-reward neurons are included; further, the first session with any reward location move is exclu
- Pearson correlation coefficients between pre-reward HMM transition and decelerations on each lap, shown for all laps with the familiar reward location (rew1) and the new reward location (rew2).
- Statistical tests performed between rew1 and rew2 conditions (Wilcoxon signed-rank test) and to zero as well (1-sample t-test).
- indicates p > 0.05.c) Mean firing for pre-reward neurons, RCA cells, or post-reward neurons.
- For pre-reward cells, data resampled as a function of behavioral epoch, shown for 20 laps before and 30 laps after reward location change.
- Insets show firing averaged over subsets of laps (rew1: last 20 laps with familiar reward location; +1: first lap after reward location change; 2-5: next 4 laps; 6+: remaining laps with new reward location).
- For RCA or post-reward cells, mean firing shown as a function of time relative to reward delivery, with mean transient rate averaged over the first 2 s after reward delivery for RCA cells or the remaining time after reward (2 to 10 s) for post-reward cells.d) Velocity and licking behavior for exempl
- Trials with optogenetic inhibition by 633 nm light are indicated by red bar (light delivered over entire track traversal for these trials), which is delivered for the final 10-20 laps with the familiar reward location (rew1, blue line) and the first ~20 laps with the new reward location (rew2, green
- Velocity max for the color scale is 30 cm/s for the control and 50 cm/s for Jaws.
- Underneath, the lap-by-lap measures of deceleration time relative to reward and the lick selectivity index (LSI, Methods) are shown, with dots representing the value for individual laps and the line the smoothed data (5-point rectangular filter).
- LSI ranges from −1, indicating 100% of the licks are near the familiar reward location, and +1, indicating 100% of the licks are near the new reward location.
- For Jaws data, the mean control trace is reproduced using light gray for comparison; moreover, the difference between Jaws and control data is shown underneath, with baseline adjusted for the deceleration data for each session (calculated as the mean deceleration times for laps before reward switch 
- “Mean during learning” quantifies mean value of deceleration times (on laps 13-20 after reward is moved) relative to baseline (calculated as mean deceleration times on the 10 laps before reward is moved) and mean value of lick selectivity on laps 2-6.
- Data is shown both for all mice (‘all’) and broken up by individual mice (C1 to C4 are control mice; J1 to J5 are Jaws mice).
- * indicates p < 0.05, 2-sample t-test.
- indicates p > 0.05.Trajectory of LEC population firing encodes the reward experienceInspired by a prior study using a cue-reward association task to investigate layer II fan cells in the LEC35, we applied principal component analysis to our population of 9554 active LEC neurons for the 22 imaging se
- The LEC population firing was plotted with respect to reward experience epochs as established in Figure 4.
- First, in this state space, jumps in the neural activity trajectory occur during transitions between the (previously defined) experience epochs (post-reward/running to pre-reward approach to consumption), which was quantified as the magnitude of the difference between successive points (Supplementar
- Second, after the reward was moved, the neural activity was largely unperturbed, following a similar trajectory as for the familiar reward (Supplementary Figure 7a).
- This observation was quantified by taking the difference between the state space trajectories in the first two principal component dimensions (Supplementary Figure 7c).
- For reference, we compared this quantity to the same measure applied to MEC and CA1.
- Unlike LEC, the trajectories in MEC and CA1 differed more after the reward location was moved.
- We next investigated the lap-by-lap changes in these representations following a reward location change to determine if the cells quickly and stably encoded the new reward or whether they slowly formed their representations, as seen for CA1 place cells in prior studies27,50.As mice learned a new rew
- While mouse behavior adapted over several laps, throughout this time the pre-reward population and the post-reward population continued to fire before and after the new reward location on each lap (Figure 6a).In particular, the pre-reward population appeared to evolve during the learning period.
- Initially, these cells were broadly active across a large portion of the track, which gradually sharpened to be active only in locations just before the reward (Figure 6a).
- This switch from inactive to active on individual laps, fit with an HMM as in Figure 4, captured this evolution as well (Figure 6b).
- Moreover, activation of the pre-reward cells was highly correlated to slowing behavior on individual laps for both the familiar and the new reward locations (Figure 6b).
- Indeed, when reexamining cell firing with respect to the approach epoch, defined by the time from deceleration until reward delivery (as in Figure 4c), the stability of the pre-reward representation across the switch becomes evident (Figure 6c).
- When mean activity is evaluated for this pre-reward epoch, no detectable change in firing rate across the pre-reward population was observed during learning of the new reward location (Figure 6c).Surprisingly, both the RCA population and the post-reward population began encoding the reward consumpti
- Even though the receipt of reward was unexpected at the new location, the amplitude of the transient increase in firing in the RCA population did not change across the reward switch laps (Figure 6c).
- The post-reward population rapidly shifted to fire at the new reward location (Figure 6a), thus encoding the new post-reward epoch from the first traversal after the switch and with no detectable change in firing rate (Figure 6c).Overall, these results indicate that pre-, post-reward and RCA populat
- We expressed the inhibitory opsin Jaws51 or a nonfunctional fluorescent marker (mCherry) as a control in LEC and, using 633 nm illumination delivered to chronically implanted fibers in bilateral LEC, inhibited LEC activity in the 10-20 laps prior to moving the reward and through the first 20 laps du
- When the reward was moved, control mice quickly adapted their behavior to the new reward location, shifting their decelerations and licking within the first ~10 laps (Figure 6d-e), similar to the behavior seen in mice during two-photon imaging of the LEC (Figure 6b).
- However, mice expressing Jaws took longer to adapt their behavior to the new reward location (Figure 6d-e).
- These results indicate that LEC is necessary for the learning of new reward locations but not for already learned reward locations.biorxiv;2023.10.09.561557v1/TBLS3T3tblS3Supplementary Table 3Number of sessions for optogenetic inhibition experiments in LEC.

## Tables

### Supplementary Table 1
> Multiway analysis of variance (ANOVA) was performed using the anovan function in MATLAB.The effects of the following factors were tested for their effect on reward clustering for each imaging session:


### Supplementary Table 2
> Number of LEC imaging fields and number of neurons for each of the three reward locations used.Final row shows data for sessions where the reward location was changed. For this data, ‘Spatial neurons’


### Supplementary Table 3
> Number of sessions for optogenetic inhibition experiments in LEC.


## Figure Descriptions

### Figure 1:
Two-photon imaging of the lateral entorhinal cortexa) A schematic of goal-directed navigation that requires a spatial map along with a reward experience representation. In this proposed model, episodic memories of goal-directed navigation combine spatial “where” information with experiential “what” 

### Figure 2:
Prominent reward clustering in LEC with segregation of pre- and post-reward populationsa) Head-fixed mice traverse a 3.1 m linear track in virtual reality with water reward delivered at 2.3 m. Treadmill velocity and detected licks, averaged over 43 traversals, are binned at 1 cm intervals with stati

### Figure 3:
Dedication of pre- and post-reward populations in the LECa) Licking (percent of laps with contact of sensor) and velocity before (66 laps) and after (49 laps) change in reward location with ±SEM shown in light shading. In this example session, the reward was moved earlier on the track, from a famili

### Figure 4:
Pre-reward cell activation is partly composed of state changes linked to behaviora) Pre-reward population activity exhibits a ramp up until the reward delivery. Two potential models that can give rise to mean ramping activity are shown. In a recruitment model, cell activity or the number of active c

### Figure 5:
A population of LEC neurons signal reward consumptiona) Mean transient rate relative to the time of reward delivery, shown for LEC, MEC, and CA1 imaging fields averaged by imaging session. Bottom plot is a histogram of the timing of peak firing for individual cells from each session. All active cell

### Figure 6:
LEC stably represents reward experience during learning while optogenetic inhibition of LEC disrupts learninga) Mice learned a new reward location over the course of a few laps. In this exemplar session, the reward location is moved later along the track. Velocity along the track, binned at 1 cm int

### Supplementary Figure 1:
Histological confirmation of imaging window over LECa) Histology of lateral entorhinal cortex (LEC). Injection of retrograde tracer in CA1 labels CA1-projecting LIII pyramidal cells of entorhinal cortex in a mouse with GCaMP6s expression. Horizontal section is taken after PFA fixation.b) Zoomed in i

### Supplementary Figure 2:
LEC firing peaks around reward and differs by layera) Histogram of spatial cell peaks and mean transient rates relative to the reward location. Datasets were combined across days where the reward location was either at 2.3 m (as in Figure 2a-d), 0.7 m, or 1.5 m. Histograms are binned every 10 cm; tr

### Supplementary Figure 3:
Additional details on dedication or pre- and post-reward populations for both reward moves and environment switchesa) Spatial firing patterns along the track and histogram of firing peaks for spatial cells sorted by their firing peaks with the familiar reward location for MEC and CA1. Same format as

### Supplementary Figure 4:
Additional details on hidden Markov model used to model LEC pre-reward population firinga) A hidden Markov model (HMM) was used to detect transitions in the pre-reward population activity. The 10 seconds before reward delivery were considered. The system begins in an inactive state and can transitio

### Supplementary Figure 5:
Pairwise correlations between LEC neurons across trials decrease near rewardsa) Correlation matrices were formed for the activity patterns of a neural population in a given imaging session at a given position. We calculated the correlation between the activity of each pair of cells at a given positi

### Supplementary Figure 6:
Pre- and post-reward firing in LEC is specific to a virtual navigation taska) Mean running velocity at track positions surrounding reward are similar (pre: 40 cm before reward, mean of 22.8 cm/s; post: 40 cm after reward, mean of 25.0 cm/s) but lower than running speed along the rest of the track (o

### Supplementary Figure 7:
Trajectory of LEC population firing using state space analysisa) Population LEC firing with respect to behavioral epochs is reduced to two dimensions using principal component analysis. The mean trajectory is plotted, with the color coded by the behavioral epoch (yellow: post-reward/running, gray: r

## References
Total references in published paper: 74

### Key References (from published paper)
- Navigating for reward (, 2021)
- Spatial goal coding in the hippocampal formation (, 2022)
- Distinct Roles of Medial and Lateral Entorhinal Cortex in Spatial Cognition (, 2013)
- A model of hippocampally dependent navigation, using the temporal difference learning rule (, 2000)
- Improving Generalization for Temporal Difference Learning: The Successor Representation (, 1993)
- The hippocampus as a predictive map (, 2017)
- The Hippocampus, Memory, and Place Cells: Is It Spatial Memory or a Memory Space? (, 1999)
- Hippocampal place cells, context, and episodic memory (, 2006)
- Hippocampal Neurons Encode Information about Different Types of Memory Episodes Occurring in the Sam (, 2000)
- Trajectory Encoding in the Hippocampus and Entorhinal Cortex (, 2000)
- Hippocampal Place Cells Acquire Location-Specific Responses to the Conditioned Stimulus during Audit (, 2003)
- Interactions between location and task affect the spatial and directional firing of hippocampal neur (, 1995)
- Place units in the hippocampus of the freely moving rat (, 1976)
- Accumulation of Hippocampal Place Fields at the Goal Location in an Annular Watermaze Task (, 2001)
- A Dedicated Population for Reward Coding in the Hippocampus (, 2018)
- Cue-sampling and goal-approach correlates of hippocampal unit activity in rats performing an odor-di (, 1987)
- The Integration of Goal-Directed Signals onto Spatial Maps of Hippocampal Place Cells (, 2019)
- Studies on single neurons in dorsal hippocampal formation and septum in unrestrained rats: Part I. B (, 1973)
- Neurons and networks in the entorhinal cortex: A reappraisal of the lateral and medial entorhinal su (, 2019)
- Microstructure of a spatial map in the entorhinal cortex (, 2005)
- Representation of Geometric Borders in the Entorhinal Cortex (, 2008)
- Topography of Head Direction Cells in Medial Entorhinal Cortex (, 2014)
- Remembered reward locations restructure entorhinal spatial maps (, 2019)
- The entorhinal cognitive map is attracted to goals (, 2019)
- Entorhinal cortex directs learning-related changes in CA1 representations (, 2022)
- Reward expectation extinction restructures and degrades CA1 spatial maps through loss of a dopaminer (, 2022)
- A Role for the Locus Coeruleus in Hippocampal CA1 Place Cell Reorganization during Spatial Reward Le (, 2020)
- Locus coeruleus and dopaminergic consolidation of everyday memory (, 2016)
- Traces of Experience in the Lateral Entorhinal Cortex (, 2013)
- Representation of Non-Spatial and Spatial Information in the Lateral Entorhinal Cortex (, 2011)

## Ground Truth Reference
- Figures: 13
- Tables: 3
- References: 74