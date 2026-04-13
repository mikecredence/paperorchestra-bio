Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title

Multiscale computational modeling of how age-related myelin dystrophy in prefrontal cortex impairs axonal conduction and working memory

## Core question

How do age-related myelin degradation (demyelination) and subsequent partial remyelination in the rhesus monkey dorsolateral prefrontal cortex quantitatively affect action potential propagation and, ultimately, spatial working memory performance?

## Motivation / gap

- Normal aging in rhesus monkeys causes extensive myelin dystrophy in dlPFC (3-6% of sheaths show splitting, balloons, redundant myelin), and this correlates with cognitive decline
- Remyelination occurs but produces shorter and thinner sheaths; a 90% increase in paranodal profiles has been observed in aged vs. young monkeys
- Prior computational models examined demyelination or remyelination separately, but never the biologically realistic combination of both occurring simultaneously on the same axon
- No existing model has linked ultrastructural myelin changes to network-level working memory impairment through a continuous multiscale pipeline
- Understanding this link has implications beyond aging for demyelinating diseases such as multiple sclerosis and schizophrenia

## Core contribution (bullet form)

- Built a multicompartment pyramidal neuron model (soma, dendrites, 101 nodes, 100 myelinated segments with paranodes, juxtaparanodes, internodes, and tight junctions) fitted to monkey dlPFC electrophysiology data
- Systematically explored demyelination and remyelination across a cohort of 50 model neurons with Latin Hypercube Sampling of axon parameters, revealing that combined demyelination plus partial remyelination produces higher AP failure rates than either alone
- Demyelinating 75% of segments by removing 50% of lamellae reduced conduction velocity by approximately 70% and caused AP failures
- Complete remyelination nearly recovered CV and AP propagation to unperturbed levels, but biologically plausible partial remyelination left substantial AP failure rates
- Incorporated single-neuron AP failure probabilities into a spiking neural network model of the delayed response task, showing that myelin dystrophy alone can account for working memory decline
- Found significant negative correlations between percentage of normal myelin and memory duration, and between percentage of new (remyelinated) myelin sheaths and memory performance

## Method in brief

The single-neuron model adapts an existing multicompartment rhesus monkey dlPFC Layer 3 pyramidal neuron model (originally from Rumbell et al., 2016) implemented in NEURON. The soma and dendritic arbors are schematic (68 compartments scaled to reconstructed surface area) with nine active ion channel types (NaF, NaP, KDR, KM, KA, CaL, KAHP, AR). The axon model attaches 101 nodes (13 compartments each) alternating with 100 myelinated segments, each comprising paranodes (5 compartments x 4 on each side), juxtaparanodes, and an internode, all endowed with myelin lamellae and tight junctions. A cohort of 50 axon models was generated via Latin Hypercube Sampling over parameters including axon diameter, node length, myelinated segment length, number of lamellae, and nodal ion channel densities. Demyelination was simulated by removing lamellae from selected segments; remyelination replaced demyelinated segments with two shorter, thinner segments separated by a new node.

At the network level, a spiking neural network model of spatial working memory simulates the delayed response task (DRT) with eight stimulus locations. The network includes excitatory and inhibitory populations with structured connectivity that supports persistent bump attractor activity. AP failure probabilities derived from the single-neuron cohort were injected as stochastic transmission failures in the excitatory recurrent connections of the network. Working memory performance was quantified by memory duration (how long the bump persisted) and a diffusion constant (how much the memory bump drifted from the cued location). Lasso regression was used to identify which axon parameters most strongly predicted CV changes and AP failures.

## Target venue

eLife


## Experimental Log

# Experimental Log: Myelin Dystrophy and Working Memory in Aging Prefrontal Cortex

## Model Architecture and Parameters

### Single Neuron Model Specification

| Component | Detail |
|-----------|--------|
| Simulation platform | NEURON |
| Base model | Rhesus monkey dlPFC Layer 3 pyramidal neuron |
| Soma/dendrite compartments | 68 (schematic, scaled to 3D reconstruction surface area) |
| Axon nodes | 101 (13 compartments each) |
| Myelinated segments | 100 |
| Paranode groups per segment | 4 on each side (5 compartments each) |
| Juxtaparanodes per segment | 2 (9 and 5 compartments respectively) |
| Internode | 1 per myelinated segment |
| Tight junctions | Present between innermost lamella and axolemma |
| Time step | 0.025 ms |
| Holding potential | -70 mV (somatic) |
| Current step duration | 2 seconds |

### Ion Channels in Model

| Channel | Type | Location |
|---------|------|----------|
| NaF | Fast inactivating sodium | Soma, dendrites, axon nodes |
| NaP | Non-inactivating persistent sodium | Soma, dendrites |
| KDR | Delayed rectifier potassium | Soma, dendrites, axon nodes |
| KM | Muscarinic receptor-suppressed potassium | Soma, dendrites |
| KA | Transient inactivating A-type potassium | Soma, dendrites |
| CaL | High-threshold non-inactivating calcium | Soma, dendrites |
| KAHP | Calcium-dependent slow potassium | Soma, dendrites |
| AR | Hyperpolarization-activated anomalous rectifier | Soma, dendrites |
| Passive | Leak conductance | All compartments |

### Axon Parameter Ranges for LHS Cohort (Table 1)

| Parameter | Range / Variation | Notes |
|-----------|-------------------|-------|
| Axon diameter | Biologically plausible range for PFC fibers | Often < 0.9 um |
| Node length | Varied across cohort | Key predictor of CV sensitivity |
| Myelinated segment length | Varied across cohort | Strongest predictor of CV change |
| Number of lamellae (wraps) | Varied across cohort | Determines insulation |
| Nodal NaF density | Varied across cohort | Affects AP regeneration |
| Nodal KDR density | Varied across cohort | Affects repolarization |
| Cohort size | 50 models | Latin Hypercube Sampling |

## Experiment 1: Demyelination Effects on Single Neurons

### Demyelination Protocol

Lamellae were removed from selected myelinated segments in three fractions of affected segments and multiple levels of lamellae removal.

### CV Change Under Demyelination (Fig 3)

| Fraction of Segments Demyelinated | Lamellae Removed (%) | CV Change (Approx. Range Across Cohort) | AP Failures Observed |
|----------------------------------|---------------------|----------------------------------------|---------------------|
| 25% | 25% | Modest reduction | Rare |
| 25% | 50% | Moderate reduction | Occasional |
| 25% | 75% | Larger reduction | More frequent |
| 25% | 100% (complete) | Large reduction | Frequent |
| 50% | 25% | Moderate reduction | Occasional |
| 50% | 50% | Substantial reduction | Frequent |
| 50% | 75% | Large reduction | Common |
| 50% | 100% (complete) | Very large reduction | Very common |
| 75% | 25% | Substantial reduction | Frequent |
| 75% | 50% | ~70% reduction | AP failures occur |
| 75% | 75% | Very large reduction | High failure rate |
| 75% | 100% (complete) | Near-complete block | Most APs fail |

- Fig 3A shows heat maps of CV reduction across the 50-neuron cohort, with axons sorted by myelinated segment length (longest at bottom)
- CV changes and AP failures were more sensitive to myelinated segment length and axon diameter than to other parameters
- Axons with longer myelinated segments were generally more vulnerable to demyelination
- Complete demyelination of 75% of segments resulted in widespread AP failures across the cohort

### Lasso Regression: Predictors of CV Sensitivity

| Parameter | Importance for CV Prediction |
|-----------|------------------------------|
| Myelinated segment length | High (strongest predictor) |
| Axon diameter | High |
| Node length | Moderate |
| Nodal ion channel densities | Moderate |
| Number of lamellae (baseline) | Lower but significant |

## Experiment 2: Remyelination and CV Recovery

### Remyelination Protocol

Previously demyelinated segments were replaced by two shorter myelinated segments with fewer lamellae and a new node between them.

### CV Recovery Under Remyelination (Fig 4)

| Demyelination Level | Fraction Remyelinated | Lamellae Restored (%) | CV Recovery | AP Failure Recovery |
|--------------------|-----------------------|----------------------|-------------|---------------------|
| 50% segments completely demyelinated | 25% of demyelinated | 25% | Partial | Partial |
| 50% segments completely demyelinated | 25% of demyelinated | 50% | Moderate | Moderate |
| 50% segments completely demyelinated | 25% of demyelinated | 75% | Substantial | Substantial |
| 50% segments completely demyelinated | 75% of demyelinated | 25% | Moderate | Moderate |
| 50% segments completely demyelinated | 75% of demyelinated | 50% | Good | Good |
| 50% segments completely demyelinated | 75% of demyelinated | 75% | Nearly complete | Nearly complete |
| 50% segments completely demyelinated | 100% of demyelinated | 100% | Near-full recovery | Near-full recovery |

- Fig 4A illustrates representative remyelination configurations with cartoons of an 8-segment axon
- A fully remyelinated axon (all demyelinated segments replaced) with full lamellae count nearly restores CV and eliminates AP failures
- However, biologically plausible remyelination (shorter, thinner sheaths with fewer lamellae) leaves residual CV slowing
- A few neurons in the cohort showed a paradoxical CV increase after remyelination, likely due to interplay between ion channels in new nodes and altered electrotonic lengths

### Key Finding: Combined Demyelination + Partial Remyelination

| Condition | Description | AP Failure Rate |
|-----------|-------------|-----------------|
| Unperturbed | All segments normal | 0% |
| Demyelination only | Some segments have reduced lamellae | Moderate |
| Demyelination + partial remyelination | Some normal, some demyelinated, some remyelinated with thinner sheaths | Higher than demyelination alone |
| Full remyelination (ideal) | All demyelinated segments replaced with full lamellae | Near 0% |

- Models with mixed normal/demyelinated/remyelinated segments had higher AP failure rates than previously reported for demyelination or remyelination alone
- This scenario is biologically most realistic for aging axons

## Experiment 3: Network Model of Working Memory (Delayed Response Task)

### Network Model Specification

| Parameter | Value |
|-----------|-------|
| Task | Delayed response task (DRT), 8 locations |
| Network type | Spiking neural network, bump attractor |
| Populations | Excitatory + Inhibitory |
| Connectivity | Structured (cosine-tuned for excitatory recurrence) |
| AP failure implementation | Stochastic transmission failures in excitatory recurrent connections |
| Performance metric 1 | Memory duration (time bump persists) |
| Performance metric 2 | Diffusion constant (drift of bump from cued location) |
| Stimulus | Spatial cue at one of 8 locations |

### Working Memory Impairment from Demyelination (Fig 5)

| Condition | Network Behavior | Memory Duration | Bump Precision |
|-----------|-----------------|-----------------|----------------|
| Unperturbed (0% AP failure) | Stable persistent bump activity | Long (maximum) | High (low diffusion) |
| Demyelination (moderate AP failures) | Degraded bump | Reduced | Reduced |
| Remyelination (low AP failures) | Partially recovered bump | Partially recovered | Partially recovered |

- Fig 5A shows schematic of the DRT: fixate, remember cue location through delay, indicate with eye movement
- Fig 5B(i): Unperturbed network maintains stable bump of excitatory activity at cued location throughout delay
- Fig 5B(ii): Demyelinated network shows degraded bump that drifts and eventually collapses
- Fig 5B(iii): Remyelinated network shows improved but not fully recovered bump activity

### Systematic Exploration of AP Failure Effects on WM (Fig 6)

| AP Failure Probability | Memory Duration (Relative) | Diffusion Constant (Relative) |
|-----------------------|---------------------------|-------------------------------|
| 0% (control) | 1.0 (normalized baseline) | 1.0 (normalized baseline) |
| Low (~5%) | ~0.9 | ~1.2 |
| Moderate (~15%) | ~0.7 | ~2.0 |
| High (~30%) | ~0.4 | ~4.0 |
| Very high (~50%) | ~0.1 | Very large |

- Fig 6A: Memory duration decreases systematically with increasing AP failure probability
- Fig 6B: Diffusion constant increases systematically with AP failure probability
- Left panels in Fig 6 show demyelination-only conditions
- Right panels show remyelination conditions where some failures are recovered
- The relationship between AP failure probability and WM impairment is approximately monotonic

## Experiment 4: Correlation Between Myelin Status and WM Performance

### Normal Myelin vs. Memory Duration (Fig 7)

| Percentage Normal Myelin | Memory Duration Trend | Diffusion Constant Trend |
|-------------------------|----------------------|-------------------------|
| 100% | Maximum | Minimum |
| 80% | Slightly reduced | Slightly increased |
| 60% | Moderately reduced | Moderately increased |
| 40% | Substantially reduced | Substantially increased |
| 20% | Severely reduced | Severely increased |

- Fig 7A: Schematic showing how cross-sectional quantification of normal myelin was modeled, mimicking electron microscopy of mixed axon populations
- Fig 7B: Significant negative correlation between percentage of normal myelin sheaths and memory duration (linear regression)
- Fig 7C: Significant positive correlation between percentage of normal myelin sheaths and diffusion constant

### New Myelin Sheaths vs. Memory Performance (Fig 8)

| Percentage New (Remyelinated) Myelin | Memory Duration Trend | Diffusion Constant Trend |
|-------------------------------------|----------------------|-------------------------|
| 0% (no remyelination) | Baseline (with existing demyelination) | Baseline |
| 10% | Slightly worse | Slightly worse |
| 20% | Moderately worse | Moderately worse |
| 30% | Substantially worse | Substantially worse |
| 40%+ | Severely impaired | Very high drift |

- Fig 8A: Schematic of quantification of new myelin sheaths in groups of neurons with intact and partly remyelinated axons
- Fig 8B: Significant negative correlation between percentage of new myelin sheaths and memory duration
- Fig 8C: Significant positive correlation between percentage of new myelin sheaths and diffusion constant
- This indicates that a higher proportion of new (thinner, shorter) sheaths is associated with worse WM performance, because the remyelinated sheaths are less effective insulators

## Summary of Key Findings Across Scales

| Scale | Finding |
|-------|---------|
| Ultrastructure | 3-6% of myelin sheaths in aged dlPFC show dystrophic alterations (splitting, balloons, redundant myelin) |
| Single axon - CV | Demyelination of 75% of segments with 50% lamellae removal causes ~70% CV reduction |
| Single axon - AP failures | Combined demyelination + partial remyelination produces higher failure rates than either alone |
| Network - WM duration | AP failure probabilities from biologically plausible myelin dystrophy reduce memory duration |
| Network - WM precision | Increased AP failures increase diffusion (bump drift) of the memory representation |
| Cross-scale link | Reduced normal myelin and increased new myelin both negatively correlate with WM performance |

## Supplementary Observations

### Supplementary Figure 1

- Fig S1A-B: Distribution of axon parameters across the 50-neuron LHS cohort
- Parameter space covers biologically plausible ranges for monkey dlPFC axons

### Supplementary Figure 4

- Axons with more transitions between long and short myelinated segments had slower CV
- Consistent with findings of Scurfield and Latimer (2018)

## Comparison with Prior Work

| Study | Focus | Our Extension |
|-------|-------|---------------|
| Scurfield and Latimer 2018 | Remyelination CV delays, transitions between segment lengths | Added coupling of demyelination + remyelination, AP failure analysis |
| Stephanova et al. 2005, 2008 | Demyelination causing CV slowing and AP failures | Extended to cohort-level analysis with LHS parameter sampling |
| Lasiene et al. 2008, Powers et al. 2012 | Remyelination with shorter/thinner sheaths causing CV slowing | Combined with simultaneous demyelination on same axon |
| Ibanez et al. 2020 | Aged network model with synaptic loss and firing rate changes | Added myelin dystrophy as mechanistic source of reduced excitatory drive |

## Empirical Data Referenced

| Data Type | Source Region | Species | Key Observation |
|-----------|--------------|---------|-----------------|
| Electron microscopy | dlPFC area 46 | Rhesus monkey | 3-6% of sheaths show age-related dystrophy |
| Paranodal profile counts | dlPFC | Rhesus monkey | 90% increase in aged vs. young |
| Electrophysiology (in vitro) | dlPFC Layer 3 | Rhesus monkey | Pyramidal neurons show hyperexcitability with aging |
| Electrophysiology (in vivo) | dlPFC | Rhesus monkey | Lower firing rates during DRT in aged monkeys |
| Behavioral | Spatial WM (DRT) | Rhesus monkey | Age-related decline in working memory accuracy |

## Clinical Relevance

| Condition | Myelin Pathology | WM Impairment |
|-----------|-----------------|---------------|
| Normal aging | Gradual myelin dystrophy with partial remyelination | Moderate decline |
| Multiple sclerosis | Widespread demyelination with variable remyelination | Often severe |
| Schizophrenia | White matter abnormalities, myelin alterations | Prominent WM deficits |
| Bipolar disorder | Myelin dystrophy reported | WM affected |
| Autism spectrum disorders | Myelin alterations observed | WM challenges |
| Traumatic brain injury | Acute myelin damage | Variable WM impairment |

## Reference Count

- Total references cited: 103

