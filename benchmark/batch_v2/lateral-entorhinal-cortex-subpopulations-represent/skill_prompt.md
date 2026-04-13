Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Nature Neuroscience

## Idea Summary

## Working title

Lateral entorhinal cortex neurons encode distinct experiential epochs around reward during goal-directed navigation in mice

## Core question

Does the lateral entorhinal cortex (LEC) provide the non-spatial "what" information about reward experience epochs (approach, consumption, departure) that the hippocampus needs to contextualize spatial maps during goal-directed navigation?

## Motivation / gap

- The hippocampus integrates "where" (spatial) and "what" (experiential) information to form episodic memories and guide navigation, but the source of the "what" signal is unknown
- The medial entorhinal cortex (MEC) is known to carry spatial information (grid cells, border cells, head direction cells), but the role of the LEC in reward-guided behavior is poorly understood
- Place cells in the hippocampus show context-dependent and reward-dependent firing (overrepresentation near reward locations, distinct goal approach vs departure signals), implying upstream non-spatial input
- Previous LEC studies have been limited by inability to perform two-photon calcium imaging in this anatomically challenging lateral structure during behavior
- No study has dissociated object coding from reward experience coding in LEC, or shown how LEC representations respond when reward location changes

## Core contribution (bullet form)

- Developed a novel two-photon imaging method using a microprism implant to access the LEC in head-fixed behaving mice, recording ~500 active neurons per imaging field (range 150-843 across 47 imaging fields)
- Discovered three functionally distinct neuronal populations in LEC: pre-reward (goal approach), reward consumption active (RCA), and post-reward (goal departure) populations
- Demonstrated that when reward location is moved, pre-reward and post-reward populations immediately shift their representations to track the new reward location, while maintaining their functional identity
- Showed that these populations are largely invariant to spatial location and environment, unlike MEC spatial cells
- Found via optogenetic inhibition of LEC that silencing LEC disrupts learning of a new reward location but does not impair behavior at an already-learned reward location
- Identified that pre-reward population activation can be modeled as a state transition (hidden Markov model) rather than a gradual ramp, with transition points variable across laps

## Method in brief

The key technical innovation was a surgical preparation for two-photon calcium imaging of the LEC in behaving mice. Because the LEC is situated ventral to the rhinal fissure as a lateralized structure, direct optical access requires approaching at >90 degrees to horizontal. A cranial window (3 mm round coverslip) with an attached 2.0 mm square microprism was implanted to rotate the imaging plane 90 degrees. GCaMP6s transgenic mice were used, and imaging was performed with a conventional upright two-photon microscope accessing depths >250 um. Fields of view were approximately 700 x 700 um.

Mice were head-fixed on a treadmill traversing a 3.1 m linear virtual reality track with water reward delivered at a specific location (e.g., 2.3 m). The track was visually cue-rich but the reward location was not marked by any visual feature. Movies were motion corrected and cells segmented using Suite2p. A novel iterative algorithm was used for neuropil correction, baseline adjustment, and deconvolution of calcium transients. Spatial cells were identified by comparing firing peak distributions to shuffled data. Pre-reward and post-reward populations were classified based on the location of their firing peaks relative to reward. Reward relocation experiments moved reward to a new position mid-session. Optogenetic experiments used Arch-expressing mice with bilateral fiber placement over LEC. A hidden Markov model was fit to pre-reward population activity to distinguish recruitment vs state-change models of ramping activity.

## Target venue

Nature Neuroscience


## Experimental Log

# Experimental Log: LEC Reward Experience Epoch Representations

## Imaging Preparation and Recording Parameters

| Parameter | Value |
|-----------|-------|
| Species | Mouse (transgenic, GCaMP6s) |
| Brain region | Lateral entorhinal cortex (LEC) |
| Comparison regions | MEC, CA1 (separate mouse groups) |
| Imaging method | Two-photon calcium imaging |
| Window | 3 mm No. 0 glass coverslip |
| Microprism | 2.0 x 2.0 mm, 45-degree angle |
| Imaging depth | >250 um accessible |
| Field of view | ~700 x 700 um |
| Mean active cells per field | 496 |
| Range of active cells per field | 150 to 843 |
| Number of imaging fields | 47 |
| Motion correction | Suite2p |
| Signal extraction | Novel iterative algorithm (neuropil correction, baseline adjustment, deconvolution) |

## Behavioral Paradigm

| Parameter | Value |
|-----------|-------|
| Apparatus | Head-fixed treadmill, 1-D virtual track |
| Track length | 3.1 m |
| Reward location (standard) | 2.3 m |
| Alternative reward locations | 0.7 m, 1.5 m |
| Reward type | Water drop |
| Visual cues | Cue-rich track, no visual marker at reward |
| Session duration | ~40 minutes |
| Behavioral criterion | At least 2 laps per minute with anticipatory licking |
| Velocity binning | 1 cm intervals, stationary periods excluded |
| Example traversals averaged | 43 laps (Fig 2a) |

## Experiment 1: Enrichment of LEC Firing Near Reward

### Cell Population Summary Across Brain Regions

| Region | Spatial Cells Identified | Reward Clustering | Pre-Reward Population | Post-Reward Population | RCA Neurons |
|--------|------------------------|-------------------|----------------------|----------------------|-------------|
| LEC | Yes | Prominent enrichment near reward | Distinct population | Distinct population | Present |
| MEC | Yes | Little change around reward | Not prominent | Not prominent | Minimal |
| CA1 | Yes | Overrepresentation near reward | Present (different character) | Present (different character) | Present |

- Fig 2 shows prominent reward clustering in LEC with clear segregation into pre- and post-reward populations
- Mice learn to decelerate and lick in anticipation of reward location over training sessions
- Fig 2a shows averaged velocity and lick traces over 43 traversals, binned at 1 cm

### Spatial Cell Peak Distribution

| Region | Peak Distribution Pattern | Reward-Related Enrichment |
|--------|--------------------------|--------------------------|
| LEC | Strong bimodal clustering before and after reward | Yes, highly prominent |
| MEC | More uniform distribution | Minimal reward enrichment |
| CA1 | Overrepresentation near reward | Yes, but different from LEC |

- Supplementary Fig 2 shows histograms of spatial cell peaks and mean transient rates relative to reward location across combined datasets

## Experiment 2: Pre-Reward and Post-Reward Population Dedication

### Reward Relocation Protocol

| Phase | Description | Duration |
|-------|-------------|----------|
| Familiar reward | Imaging at learned reward location | ~15 min |
| Reward move | Reward relocated (e.g., 2.3 m to 1.5 m) | Mid-session switch |
| Novel reward | Imaging at new reward location | ~15 min |

### Population Response to Reward Relocation

| Population | Response to Reward Move | Latency |
|------------|------------------------|---------|
| Pre-reward | Immediately shifts to encode approach to new reward location | Within first few laps |
| Post-reward | Immediately shifts to encode departure from new reward location | Within first few laps |
| RCA | Shifts to fire during consumption at new reward location | Immediate |

- Fig 3a shows licking (% of laps with sensor contact) and velocity before (66 laps) and after (49 laps) reward relocation, with SEM
- In the example session, reward was moved from 2.3 m (familiar, blue) to 1.5 m (new, green)
- Fig 3c shows spatial firing patterns sorted by peak for spatial cells before and after the reward move

### Cross-Condition Peak Shift Analysis

| Region | Peak Location Shift | Interpretation |
|--------|-------------------|----------------|
| LEC pre-reward | Shifted to track new reward | Dedicated to reward approach |
| LEC post-reward | Shifted to track new reward | Dedicated to reward departure |
| MEC | Minimal shift | Spatially anchored, not reward-relative |
| CA1 | Some redistribution | Mixed spatial and reward influence |

- Supplementary Fig 3a shows spatial firing patterns for MEC and CA1 across reward conditions
- Supplementary Fig 3b shows distributions of difference in peak location for MEC and CA1 spatial cells across conditions

## Experiment 3: Environment Switch

### Population Stability Across Environments

| Condition | Pre-Reward Population | Post-Reward Population | Interpretation |
|-----------|-----------------------|------------------------|----------------|
| Environment A (familiar) | Active before reward | Active after reward | Baseline |
| Environment B (novel) | Same cells active before reward | Same cells active after reward | Environment invariant |

- Fig 3 also contains environment switch data showing that pre- and post-reward populations maintain their functional identity across different visual environments
- Supplementary Fig 3 provides additional details on dedication of populations for both reward moves and environment switches

## Experiment 4: Pre-Reward Population Dynamics (State vs Recruitment Model)

### Hidden Markov Model Analysis

| Parameter | Value |
|-----------|-------|
| Time window analyzed | 10 seconds before reward delivery |
| Model structure | 2 states: inactive and active (absorbing) |
| Observable | Number of active cells per time bin |
| Trained parameters | Emission probabilities per state, transition probabilities |

### Model Comparison

| Model | Description | Fit to Data |
|-------|-------------|-------------|
| Recruitment model | Cell activity or number of active cells increases gradually on each trial | Poor fit to single-trial data |
| State model | Whole population activates together at variable location before reward | Better fit; HMM captures variable transition points |

- Fig 4a shows that pre-reward population activity exhibits a ramp-up until reward delivery at the mean level
- At single-trial level, activity is better described by a state transition at a variable location
- Supplementary Fig 4a describes the HMM setup: system begins in inactive state, can transition to absorbing active state, HMM learns emission and transition probabilities

### Pre-Reward Activation Characteristics

| Feature | Observation |
|---------|-------------|
| Mean activity profile | Gradual ramp up |
| Single-trial profile | Abrupt state transition |
| Transition location | Variable across laps |
| Behavioral correlate | Partly linked to deceleration behavior |

- Fig 4 shows that pre-reward cell activation is partly composed of state changes linked to behavior

## Experiment 5: Reward Consumption Active (RCA) Neurons

### RCA Cell Properties

| Region | RCA Neurons Present | Timing of Peak Firing | Specificity |
|--------|--------------------|-----------------------|-------------|
| LEC | Yes (selection criteria applied) | Within first second after reward delivery | Reward-specific |
| MEC | Minimal | -- | -- |
| CA1 | Present | Within first second | Mixed |

- Fig 5a shows mean transient rate relative to time of reward delivery for LEC, MEC, and CA1, averaged by imaging session
- Blue bar in Fig 5a highlights first second after reward delivery
- Fig 5b describes selection criteria and properties of RCA neurons in LEC
- Bottom plot in Fig 5a is a histogram of peak firing timing for individual cells from each session

### RCA Response Properties

| Property | LEC RCA Neurons |
|----------|----------------|
| Temporal alignment | Locked to reward delivery time |
| Spatial invariance | Fire at reward regardless of location on track |
| Environment invariance | Maintained across different virtual environments |
| Reward relocation response | Immediately track new reward location |

## Experiment 6: Layer-Specific Analysis

### Depth-Dependent Properties

| Layer | Reward Clustering | Population Characteristics |
|-------|-------------------|---------------------------|
| Superficial LEC | Present | Described in Supplementary Fig 2b |
| Deep LEC | Present (different magnitude) | Described in Supplementary Fig 2b |

- Supplementary Fig 2b compares calcium transients and firing properties across LEC depths
- ANOVA tested effects of imaging depth (50 um bins), anticipatory deceleration, gender, and age on reward clustering (Supplementary Table 1)

### ANOVA Factors for Reward Clustering (Supplementary Table 1)

| Factor | Description | Effect Tested |
|--------|-------------|---------------|
| Imaging depth | Discretized into 50 um bins | Depth effect on clustering |
| Anticipatory deceleration | Mean velocity in 1s before reward < half max velocity | Behavioral effect |
| Gender | Male/female | Sex effect |
| Age | In weeks | Age effect |

## Experiment 7: Learning and Optogenetic Inhibition

### Learning Dynamics

| Phase | Behavioral Indicator | Neural Indicator |
|-------|---------------------|-----------------|
| Early learning (new reward) | Gradual deceleration shift | Pre/post populations shift within first few laps |
| Late learning | Stable anticipatory licking | Stable population representations |

- Fig 6a shows an example session where reward is moved later on the track
- Velocity traces shown for final 10 laps at familiar location and first 15 laps at new location
- Pre-reward and post-reward population firing shifts with learning

### Optogenetic Inhibition Protocol

| Parameter | Value |
|-----------|-------|
| Opsin | Arch (inhibitory) |
| Delivery | Bilateral fiber placement over LEC |
| Light condition | Light ON vs Light OFF trials |
| Behavioral readout | Learning rate for new reward location |

### Optogenetic Inhibition Results

| Condition | Learning New Reward Location | Behavior at Familiar Reward |
|-----------|----------------------------|---------------------------|
| Light OFF (control) | Normal learning rate | Normal |
| Light ON (LEC inhibition) | Significantly disrupted / slowed | Not disrupted |

- Fig 6 shows that LEC stably represents reward experience during learning while optogenetic inhibition disrupts learning
- Critical finding: LEC inhibition impairs learning of a new reward location but does not impair already-learned behavior
- Supplementary Table 3 shows number of sessions for optogenetic inhibition experiments

### Session Counts (Supplementary Table 2)

| Reward Location | Number of LEC Imaging Fields | Number of Neurons |
|-----------------|------------------------------|-------------------|
| Location 1 (2.3 m) | Reported | Reported |
| Location 2 (0.7 m) | Reported | Reported |
| Location 3 (1.5 m) | Reported | Reported |
| Reward change sessions | Reported | Spatial neurons for familiar and novel |

## Comparison Across Brain Regions

### LEC vs MEC vs CA1 Summary

| Feature | LEC | MEC | CA1 |
|---------|-----|-----|-----|
| Spatial cells | Yes | Yes (grid, border, HD) | Yes (place cells) |
| Reward clustering | Prominent | Minimal | Present |
| Pre-reward population | Distinct, dedicated | Not prominent | Present but different |
| Post-reward population | Distinct, dedicated | Not prominent | Present but different |
| RCA neurons | Yes | Minimal | Yes |
| Response to reward move | Immediate shift | Little change | Some redistribution |
| Environment invariance | Yes | No (spatial remapping) | No (remapping) |
| Reward experience encoding | Primary role | Not primary | Integrative |

## Key Observations and Conclusions

1. LEC contains three functionally distinct populations that encode the experiential epochs of goal-directed navigation: approach, consumption, and departure
2. These populations are reward-centric rather than spatially anchored, shifting immediately with reward relocation
3. Pre-reward ramping at the population level reflects variable-timing state transitions rather than gradual recruitment
4. LEC provides stable, environment-invariant reward experience representations in parallel to MEC spatial representations
5. Optogenetic results establish a causal role for LEC in learning new reward associations
6. This parallel representation scheme is well-suited for generating episodic memories and flexible navigation

