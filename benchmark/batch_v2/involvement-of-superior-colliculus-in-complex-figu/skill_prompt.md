Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

## Working title

Superficial superior colliculus is causally involved in complex figure detection and encodes figure-ground signals in mice

## Core question

Is the superficial superior colliculus (sSC) of mice causally involved in detecting figures defined by complex features (contrast, orientation, phase) on textured backgrounds, and do sSC neurons encode figure-ground information in a behaviorally relevant manner?

## Motivation / gap

- Object detection is a core visual function, traditionally attributed to visual cortex (V1); however, mice can still detect simple stimuli after V1 silencing/ablation, likely mediated by SC
- SC involvement has been demonstrated for detecting isolated stimuli and simple changes, but not for detecting figures on complex, non-homogeneous backgrounds
- Recent work showed mouse sSC encodes visual features of complex objects independently of V1 input, but the behavioral relevance of this encoding was unknown
- Existing models of texture-defined figure detection focus exclusively on cortical circuits (V1 figure-ground modulation, higher area feedback), leaving SC out of the picture
- Prior SC inhibition/ablation studies typically targeted deeper layers or were unilateral; bilateral sSC-specific manipulations are rare

## Core contribution (bullet form)

- Optogenetic inhibition of bilateral sSC (N=8 GAD2-Cre mice, ChR2 in inhibitory neurons) significantly decreased performance on all three figure detection tasks: contrast, orientation, and phase
- Inhibition was most effective at early latencies (0-100 ms after stimulus onset), with effects diminishing at later time points (100-200 ms)
- sSC visually evoked responses were reduced by 33% on average during optogenetic inhibition (p < 0.001), though silencing was not complete
- Neural recordings (5 C57BL/6J mice) showed sSC neurons respond more strongly to figure elements than identical ground elements for contrast and orientation tasks
- Linear SVM decoder could discriminate figure vs. ground from sSC population activity above chance for all three tasks including phase
- Figure-ground discriminability (d-prime) was significantly higher on correct trials than error trials, linking sSC activity to behavioral decisions
- A small group of putative multisensory neurons at slightly deeper locations showed task-related responses peaking later (~700 ms), after lick spout presentation but before licking

## Method in brief

For optogenetic experiments, 8 GAD2-Cre mice received bilateral injections of Cre-dependent ChR2 (ssAAV-9/2-hEF1a-dlox-hChR2(H134R)_mCherry, titer 5.4e12) into sSC, followed by optic fiber implantation. Blue laser light activated inhibitory neurons, suppressing overall sSC activity. Mice performed a two-alternative forced choice figure detection task (left vs. right figure position, reported by licking a Y-shaped spout). Three task variants used figures differing from background by contrast, orientation, or phase. Inhibition was applied at different latencies (0-200 ms) after stimulus onset, with response allowed from 200 ms. A blue LED flashed at random intervals above the head to prevent behavioral cueing by the laser. Mice ran 100-250 trials per session over 2-5 months.

For electrophysiology, 5 C57BL/6J mice were implanted with silicon probes (Neuropixels or 32-channel linear arrays) targeting sSC. Neurons were classified by receptive field location relative to the figure: inside the figure, on the figure edge, or outside. Population responses were compared between figure and ground conditions using cluster-based permutation tests. A linear SVM classifier with a 50 ms sliding window (10 ms steps) decoded figure vs. ground identity. Behavioral relevance was assessed by comparing figure-ground discriminability (d-prime from ROC analysis) between hit and error trials. The response window was 500 ms before lick response was allowed.

## Target venue

eLife


## Experimental Log

# Experimental Log: Superior Colliculus Involvement in Complex Figure Detection

## Animals

| Experiment | Strain | N | Sex | Age at Start |
|-----------|--------|---|-----|-------------|
| Awake behaving electrophysiology | C57BL/6J (Charles River) | 5 | All male | 2-5 months |
| Behavior + optogenetics | GAD2-Cre (Jackson #028867) | 8 | 6 male, 2 female | 2-5 months |
| Anesthetized electrophysiology | GAD2-Cre | 3 | All male | 2-5 months |
| Total | -- | 16 | -- | -- |

### Housing and Light Cycle

| Parameter | Value |
|-----------|-------|
| Light cycle | Reversed 12hr/12hr |
| Food access | Ad libitum laboratory pellets |
| Experiment timing | During dark cycle |
| Housing | Solitary or in pairs |

## Surgical Parameters

| Parameter | Value |
|-----------|-------|
| Anesthesia induction | 3-5% isoflurane |
| Anesthesia maintenance | 1.2-2% isoflurane |
| O2 mixture | 50% air, 50% O2, 0.5 L/min |
| Body temperature | 36.5-37.5 C (heated pad + rectal thermometer) |
| General analgesic | Meloxicam 2.5 mg/kg SC |
| Local analgesic (ears) | Xylocaine cream |
| Local analgesic (periosteum) | Lidocaine spray |
| Dental primer | Kerr Optibond (light-cured) |
| Base cement | Heraeus Charisma (light-cured) |
| Fixation cement | Vivadent Tetric evoflow (light-cured) |

## Viral Injection Parameters

| Parameter | Value |
|-----------|-------|
| Virus | ssAAV-9/2-hEF1a-dlox-hChR2(H134R)_mCherry(rev)-dlox-WPRE-hGHp(A) |
| Titer | 5.4 x 10^12 |
| Target | Bilateral sSC |
| Opsin | ChR2 (excitatory, Cre-dependent) |
| Reporter | mCherry |
| Mouse line | GAD2-Cre (targets inhibitory neurons) |

## Optogenetic Inhibition Parameters

| Parameter | Value |
|-----------|-------|
| Light source | Blue laser |
| Target | sSC inhibitory neurons (bilateral) |
| Mechanism | Activating GABAergic neurons to suppress overall sSC activity |
| Fiber implant | Optic fibers over SC, shielded externally |
| Control for visual cueing | Blue LED above mouse head, random flashing |
| Inhibition latencies tested | 0-200 ms after stimulus onset |
| Response allowed from | 200 ms after stimulus onset |

### Anesthetized Control: Inhibition Effectiveness

| Measure | Value | P-value |
|---------|-------|---------|
| Average reduction of visually evoked responses in sSC | 33% | p < 0.001 |
| Complete silencing achieved? | No (partial inhibition) | -- |

- Fig S1: Visually evoked responses significantly reduced but not eliminated during optogenetic inhibition

## Behavioral Task Design

### Figure Detection Tasks (Fig 1A)

| Task | Figure Definition | Background |
|------|------------------|------------|
| Contrast | Grating differs from background in contrast | Textured |
| Orientation | Grating differs from background in orientation | Textured |
| Phase | Grating differs from background in phase | Textured |

### Task Structure (Fig 1D)

| Parameter | Value |
|-----------|-------|
| Response type | 2-AFC (left vs. right lick on Y-shaped spout) |
| Hit definition | Licking on side corresponding to figure |
| Trials per session | 100-250 |
| Sessions per week | 5 |
| Recording period | 2-5 months |
| Response window onset | 200 ms after stimulus |

## Optogenetic Behavioral Results (Fig 1E)

### Effect of sSC Inhibition on Task Accuracy

| Task | No Laser Accuracy | Laser Effect | Significance |
|------|-------------------|-------------|-------------|
| Contrast | Baseline (indicated by 'no') | Significant decrease | Yes |
| Orientation | Baseline | Significant decrease | Yes |
| Phase | Baseline | Significant decrease | Yes |

- Fig 1E: Inhibition of sSC significantly decreased task performance for ALL three figure detection tasks
- Dots represent means +/- SEM across N=8 mice

### Temporal Profile of Inhibition Effect

| Inhibition Latency (ms) | Contrast Task | Orientation Task | Phase Task |
|------------------------|--------------|-----------------|-----------|
| 0-100 (early) | Strongest effect | Strongest effect | Strongest effect |
| 100-200 (late) | Diminished effect | Diminished effect | Diminished effect |

- Inhibition was most effective when applied early (0-100 ms) after stimulus onset
- Effects diminished at later latencies (100-200 ms)

## Electrophysiology Setup (Fig 2A-C)

| Parameter | Value |
|-----------|-------|
| Probe types | Neuropixels, 32-channel linear arrays |
| Target | sSC |
| Histological verification | DiI track + DAPI staining |
| Response window for mice | 500 ms before lick allowed |
| RF mapping | Estimated receptive fields for each neuron |

### Neuron Classification by RF Location

| RF Category | Description |
|-------------|-------------|
| Inside figure | RF entirely within the figure region |
| On figure edge | RF on the boundary between figure and ground |
| Outside figure | RF entirely in the background region |

## Electrophysiological Results: Population Responses (Fig 2)

### Figure vs. Ground Responses -- RF Inside Figure (Fig 2F-H)

| Task | Figure Response vs. Ground Response | Statistical Significance |
|------|-------------------------------------|------------------------|
| Contrast | Stronger for figure | Significant time clusters (p < 0.05) |
| Orientation | Stronger for figure | Significant time clusters (p < 0.05) |
| Phase | Not significantly increased at population level | Not significant (population level) |

- Fig 2D: Mouse accuracy by task, mean +/- SEM
- Fig 2E: Estimated receptive fields of neurons with RF entirely inside the figure
- Fig 2F: Receptive field of example neuron
- Fig 2G-H: Example neuron and population responses show enhanced activity for figure vs. ground stimuli

### Figure vs. Ground Responses -- RF on Edge (Fig 3A-B)

| Task | Population Response Difference | Significant Time Clusters |
|------|-------------------------------|--------------------------|
| Contrast | Figure > Ground | Grey patches where p < 0.05 |
| Orientation | Figure > Ground | Grey patches where p < 0.05 |
| Phase | Weaker difference | Less prominent |

- Fig 3A: Estimated receptive fields of neurons with RF on the figure edge
- Fig 3B: Mean (+/- SEM) population responses of RF edge-neurons for each task, with grey patches indicating significant time clusters

## SVM Decoding Results (Fig 3C)

### Linear SVM Classifier Performance

| Task | Decoding Performance | Above Chance? | Window |
|------|---------------------|--------------|--------|
| Contrast | Above chance | Yes | Multiple time bins |
| Orientation | Above chance | Yes | Multiple time bins |
| Phase | Above chance | Yes | Multiple time bins |

| Decoding Parameter | Value |
|-------------------|-------|
| Classifier | Linear SVM |
| Window size | 50 ms sliding |
| Step size | 10 ms |
| Chance level | 50% |

- Fig 3C: Decoding performance for each task; grey regions indicate significant time bins above chance
- Importantly, even phase task (where population response difference was not significant) could be decoded above chance, indicating consistent but subtle response differences

## Behavioral Relevance: Hits vs. Errors (Fig 4)

### Figure-Ground Discriminability by Trial Outcome

| Measure | Hits | Errors | Comparison |
|---------|------|--------|-----------|
| Figure-ground response difference | Larger | Smaller | Hits > Errors |
| d-prime (from ROC analysis) | Higher | Lower | Significant difference |

- Fig 4A: Example stimuli showing that RF content is identical between hit and error trials (only the mouse's response differs)
- Fig 4B: Population responses show larger figure-ground differences for hits than errors; dashed grey line indicates mean reaction time
- Fig 4C: Neuronal discriminability (d-prime) is higher for correct trials

### d-prime Analysis

| Task | d-prime Hits | d-prime Errors | Statistical Significance |
|------|-------------|---------------|------------------------|
| Contrast | Higher | Lower | Significant |
| Orientation | Higher | Lower | Significant |
| Phase | Higher | Lower | Significant |

- Figure-ground discriminability in sSC predicts behavioral outcome, suggesting sSC contributes to the decision process

## Putative Multisensory Neurons (Fig 5)

### Identification

| Criterion | Value |
|-----------|-------|
| Location | Slightly deeper than sSC (deeper laminae) |
| Peak response time | ~700 ms (after lick spout presentation, before licking) |
| Number recorded | Small group |
| Classification | Putative multisensory (based on timing and depth) |

### Response Properties (Fig 5A-B)

| Property | Visual Neurons | Putative Multisensory Neurons |
|----------|---------------|------------------------------|
| Peak response timing | Early (within 100-200 ms of stimulus) | Late (~700 ms, around lick spout time) |
| Task-related modulation | Yes (figure vs. ground) | Yes (similar pattern) |
| Response to figure vs. ground | Figure > Ground | Figure > Ground (similar trend) |

- Fig 5A: All recorded neurons sorted by peak response time; small unshaded group peaks at ~700 ms
- Fig 5B: Example putative multisensory neuron responses; raster plot with orientation (red) and phase (blue) task trials

## Analysis Software and Methods

| Tool/Method | Application |
|-------------|-------------|
| MATLAB R2019a | All offline analysis |
| Cluster-based permutation test | Population response statistics |
| Linear SVM classifier | Figure vs. ground decoding |
| ROC analysis / d-prime | Neuronal discriminability |
| Sliding window (50 ms, 10 ms step) | Temporal decoding analysis |

## Summary of Key Statistical Results

| Test | Context | Result |
|------|---------|--------|
| Optogenetic inhibition vs. no laser | All 3 tasks | Significant accuracy decrease (p values in Fig 1E) |
| Visual response reduction (anesthetized) | sSC evoked responses | 33% reduction, p < 0.001 |
| Population figure vs. ground (contrast) | RF inside figure | Significant time clusters, p < 0.05 |
| Population figure vs. ground (orientation) | RF inside figure | Significant time clusters, p < 0.05 |
| Population figure vs. ground (phase) | RF inside figure | Not significant at population level |
| SVM decoding (all tasks) | RF edge neurons | Above chance for all three tasks |
| d-prime hits vs. errors | All tasks | Significantly higher for hits |

## Key Conclusions from Data

| Finding | Significance |
|---------|-------------|
| sSC is causally involved in complex figure detection | Not just simple stimulus detection |
| Involvement spans contrast, orientation, AND phase | Even features requiring more complex processing |
| Earliest time window (0-100 ms) is most critical | Consistent with feedforward visual processing timeline |
| sSC neurons show figure-ground modulation | Previously mainly attributed to V1 |
| Neural discriminability predicts behavioral success | sSC activity is behaviorally relevant |
| Phase stimulus decoded despite weak population effect | Information present at single-neuron level |
| Multisensory neurons respond at decision time | Suggests sSC integrates visual and motor/decision signals |

