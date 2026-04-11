# Experimental Log: Neurofeedback Training Modulates SWRs and Replay

## Subjects and Experimental Design

| Parameter | Value |
|-----------|-------|
| Species | Rat |
| Cohorts | 2 (manipulation cohort + control cohort) |
| Manipulation cohort | Neurofeedback at one center port, delay at other |
| Control cohort | Delay at both center ports (no neurofeedback) |
| Recording target | CA1 hippocampus |
| Recording method | Tetrode drives (LFP + single-unit spiking) |
| LFP ripple band | 150-250 Hz |
| SWR detection | Real-time, suprathreshold event in ripple-filtered LFP |

### Task Structure

| Step | Description |
|------|-------------|
| 1 | Initiate trial: nosepoke at home port |
| 2 | Maintain nosepoke at randomly assigned center port (NF or delay) |
| 3 | Choose one of 8 arms, visit it, return to home port |
| Memory requirement | Search for and remember rewarded arm locations |

### Neurofeedback Protocol (Fig 1A)

| Component | Detail |
|-----------|--------|
| Trigger | First SWR event exceeding set SD threshold during nosepoke at NF port |
| Reward | Tone + food reward delivered immediately upon detection |
| Targeted interval | Pre-reward period at center port on NF trials |
| Delay port control | Wait duration matched to recent NF trial durations |
| Delay reward | Same tone + food reward after matched wait |

### Experimental Timeline (Fig 1D)

| Phase | Manipulation Cohort | Control Cohort |
|-------|--------------------|-|
| Training | Neurofeedback embedded in spatial memory task | Spatial memory task with delay-only ports |
| Duration | Several weeks | Same task duration |
| Data collection | Ongoing throughout training | Same |

## Experiment 1: SWR Rate Enhancement (Fig 2)

### SWR Rate During Pre-Reward Period

| Trial Type | SWR Rate Trend | Comparison |
|------------|---------------|------------|
| NF trials (manipulation cohort) | Greatly increased before reward delivery | vs. delay and control |
| Delay trials (manipulation cohort) | Weaker but still elevated vs. control | vs. control |
| Control cohort trials | Very few SWRs during pre-reward | Baseline reference |

- Fig 2A: Example raw and ripple-filtered LFP traces from NF trial, delay trial, and control trial, with SWRs highlighted
- Fig 2B: SWR rate calculated in 0.5 s bins aligned to reward delivery time
- Manipulation subjects developed striking increases in SWR rate prior to reward at center ports
- Effect was strongest on NF trials (where SWRs were required) and weaker on delay trials (where they were not)

### SWR Rate Quantification

| Comparison | Direction | Statistical Notes |
|------------|-----------|-------------------|
| NF trials vs. delay trials (manipulation cohort) | NF >> delay | Significantly higher |
| NF trials (manipulation) vs. control trials | NF >> control | Significantly higher |
| Delay trials (manipulation) vs. control trials | Delay > control | Significantly higher (weaker effect) |

## Experiment 2: Speed Controls (Fig 3)

### Head Velocity During Pre-Reward Period

| Comparison | p-value | Notes |
|------------|---------|-------|
| Manipulation NF vs. delay (trial-level ranksum) | 2.447e-223, 2.760e-85, 3.247e-80, 9.077e-36 | Multiple comparisons across time bins |
| Manipulation NF vs. control (groupwise) | 1.260e-7 | Significant difference |
| Manipulation delay vs. control (groupwise) | 1.121e-4 | Significant difference |

- Fig 3A: Mean head velocity (smoothed) during pre-reward time at center ports
- Head velocity differed between NF and delay trials
- However, SWR rate differences persisted after controlling for speed
- Fig 3B: Mean head velocity for subsequent analyses showed speed alone does not account for SWR rate changes

### Speed-Controlled SWR Analysis

| Analysis | Result |
|----------|--------|
| SWR rate after matching speed distributions | NF still significantly higher than delay and control |
| Interpretation | Speed differences cannot explain the neurofeedback-driven SWR increase |

## Experiment 3: Replay Content Preservation (Fig 4)

### Decoding Method

| Parameter | Value |
|-----------|-------|
| Decoding approach | Clusterless decoding |
| Spatial representation | 2D maze linearized to 1D |
| Input data | Spiking activity during SWR events |
| Output | Posterior probability distribution over maze positions |
| Replay classification | Local (current/recent location) vs. Remote (not recently visited) |

### Replay Observations (Fig 4)

| Observation | Detail |
|-------------|--------|
| Fig 4A | Linearized maze trajectory for example NF trial, with SWR times highlighted |
| Fig 4B | Decoding during movement times shows close correspondence between decoded and real position |
| Fig 4C | Several example SWR replay events from same trial: local replay (near current arm), remote replay (representing distant arms), sequence replay (compressed trajectory) |
| Fig 4D | Replay during NF interval contains behaviorally relevant spatial content |

### Remote Replay Rate Comparison

| Trial Type | Remote Replay Rate | Comparison |
|------------|-------------------|------------|
| NF trials | Higher | vs. delay trials |
| Delay trials | Lower | Reference |

- NF trials showed increased rate of remote replay compared to delay trials
- Replay content evolved and adapted to changing task demands
- SWR events during neurofeedback contained robust and diverse replay representing experiences relevant to current task state

### Replay Diversity

| Property | NF Trials | Delay Trials |
|----------|-----------|-------------|
| Spatial diversity (arms represented) | High (multiple arms) | Present |
| Task relevance | Relevant to current goal state | Relevant |
| Content prescription | Not overly prescribed by NF | N/A |

## Experiment 4: Behavioral Performance (Fig 5)

### Search Accuracy (Fraction Choosing Unsampled Arm)

| Comparison | p-value | Interpretation |
|------------|---------|----------------|
| NF vs. delay (manipulation cohort) | 0.9562, 0.7509, 0.7509, 0.9562 | Not significant (multiple comparisons) |
| NF trials (manipulation) vs. control | 0.5425 | Not significant |
| Delay trials (manipulation) vs. control | 0.5425 (groupwise) | Not significant |

- Fig 5A: Fraction of trials choosing previously unsampled arm during goal search
- No significant differences between NF and delay trials within manipulation cohort
- No significant differences between manipulation and control cohorts
- Neurofeedback training does not impose a cognitive burden on spatial memory performance

### Additional Behavioral Metrics

| Metric | NF vs. Delay | NF vs. Control |
|--------|-------------|----------------|
| Search accuracy | No difference | No difference |
| Task completion | Comparable | Comparable |

## Experiment 5: Post-Targeted Period Compensation

### Observation

| Finding | Detail |
|---------|--------|
| Neural compensation | Changes in SWR dynamics after the targeted (pre-reward) period |
| Behavioral compensation | Performance adjustments associated with NF-driven SWR increases |
| Temporal regulation | Short-timescale regulation of SWR generation revealed |

- After the targeted neurofeedback interval, neural and behavioral compensation was observed
- This suggests the brain actively regulates SWR occurrence on a short timescale
- The increase in SWRs during the targeted period was not achieved without downstream consequences

## SWR Detection Parameters

| Parameter | Value |
|-----------|-------|
| LFP recording site | CA1 hippocampus |
| Ripple filter band | 150-250 Hz |
| Detection threshold | Set standard deviation (SD) threshold |
| Detection speed | Real-time |
| Trigger latency | Rapid (immediate tone + food delivery) |

## Supplementary Observations

### Supplementary Figure 1

| Panel | Content |
|-------|---------|
| Fig S1A | Details of SWR detection algorithm |
| Fig S1B | Detection performance validation |
| Fig S1C | Pre-reward duration matching between NF and delay ports |

- Delay period length randomly chosen from pre-reward durations of recent NF trials
- Approximately matched time spent at each center port

## Comparison to Prior Work

| Prior Approach | Limitation | Our Advance |
|---------------|-----------|-------------|
| Operant conditioning of SWRs (Ishikawa et al. 2014) | Used intracranial stimulation as reinforcer | External food reward (more clinically translatable) |
| Electrical stimulation of SWRs | May not engage SWR-permissive brain states | Subjects learn to enter SWR-permissive state |
| Optogenetic SWR evocation | Requires invasive procedures, not clinically viable | Non-invasive positive reinforcement |
| Continuous oscillation neurofeedback | Modulates sustained oscillatory power | Modulates discrete memory-related events |

## Key Metrics and Definitions

| Metric | Definition |
|--------|-----------|
| SWR rate | Number of suprathreshold SWR events per unit time (0.5 s bins) |
| Remote replay | Decoded replay representing maze locations not recently visited |
| Local replay | Decoded replay representing current or recently visited location |
| Search accuracy | Fraction of trials choosing a previously unsampled arm |
| Pre-reward period | Time from nosepoke onset to reward delivery at center port |
| Targeted interval | The pre-reward period on NF trials when SWR detection is active |
| Clusterless decoding | Bayesian decoding without spike sorting, using spike features directly |
| Linearized position | 1D representation of 2D maze for decoding efficiency |

## Datasets and Baselines

| Dataset | Description |
|---------|-------------|
| Manipulation cohort | Subjects with NF port + delay port |
| Control cohort | Subjects with two delay ports only (data from Gillespie et al. 2021) |
| Within-subject control | Delay trials vs. NF trials (same session, same subject) |
| Behavioral baseline | Search performance on delay trials |
| Neural baseline | SWR rate during control cohort pre-reward periods |

## Statistical Tests Referenced

| Test | Application | Key p-values |
|------|-------------|-------------|
| Ranksum (Wilcoxon) | NF vs. delay trial-level comparisons | Multiple: 2.447e-223 to 9.077e-36 (velocity) |
| Groupwise comparison | Manipulation vs. control cohort | NF vs. control: 1.260e-7; delay vs. control: 1.121e-4 (velocity) |
| Ranksum | Behavioral accuracy NF vs. delay | 0.9562, 0.7509, 0.7509, 0.9562 (not significant) |
| Groupwise comparison | Behavioral accuracy manipulation vs. control | NF vs. control: 0.5425 (not significant) |

## Reference Count

- Total references cited: 58
