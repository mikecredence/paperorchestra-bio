Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title

Variable PC-CbN synaptic weights enable concurrent rate and timing codes in cerebellar output

## Core question

How does the highly variable distribution of Purkinje cell (PC) to cerebellar nuclei (CbN) synapse sizes -- discovered here in juvenile mice -- affect the ability of PCs to control CbN neuron firing through rate codes, synchrony-based timing codes, and their interplay?

## Motivation / gap

- Leading theories debate whether PCs encode information via rate codes or synchrony/timing codes, but these have been treated as largely separate mechanisms
- Previous electrophysiology characterized PC-CbN inputs as relatively small and uniform in size, but recordings were mostly in young animals (P13-29) with limited sample sizes (n~30)
- Prior dynamic clamp studies used 40 uniform-sized PC inputs, which may not reflect the actual synaptic weight distribution
- The functional consequences of having a skewed distribution of input sizes (some very large) on CbN neuron firing control are unknown
- It is unclear how the refractory period of spontaneously firing PCs interacts with synaptic inhibition to shape CbN output timing

## Core contribution (bullet form)

- Discovered that PC-CbN unitary input sizes in juvenile mice (P23-32, n=83) follow a highly skewed distribution, significantly different from the more uniform distribution in young mice (P10-20, n=74; p < 0.0001, Kolmogorov-Smirnov test)
- Demonstrated via dynamic clamp that single large PC inputs (30 nS) strongly influence both rate and timing of CbN neurons -- transiently eliminating CbN firing for several milliseconds
- Found that the PC refractory period causes a brief elevation of CbN firing prior to suppression by each PC spike, creating a disinhibition-then-inhibition temporal motif
- Showed that nonuniform input sizes elevate baseline CbN firing rates by increasing inhibitory conductance variability, reducing the relative influence of synchrony on firing rate
- Demonstrated that synchronizing even two large inputs can significantly increase CbN neuron firing despite reduced relative synchrony influence with nonuniform inputs
- Confirmed rate code transmission: varying firing rate of small, medium, or large inputs all modulate CbN output, with large inputs having disproportionate influence

## Method in brief

Acute sagittal cerebellar slices (170 um) were prepared from C57BL/6 mice. Unitary PC-CbN input sizes were measured using minimal stimulation of PC axons in the white matter while recording whole-cell voltage-clamp IPSCs from large glutamatergic CbN projection neurons (>70 pF). Recordings were performed in young (P10-20, n=74 inputs) and juvenile (P23-32, n=83 inputs) animals. The internal solution used high chloride (ECl = 0 mV) with BAPTA to prevent long-term plasticity. All experiments were at 34-35 degrees C with AMPAR, NMDAR, glycine, and GABAB receptor blockers present.

Dynamic clamp experiments (P26-32) used the measured distribution to approximate the juvenile input profile with 16 small (3 nS), 10 medium (10 nS), and 2 large (30 nS) inputs firing at rates derived from in vivo PC recordings. Ten PCs recorded in vivo provided realistic interspike interval distributions that were fit with lognormal functions. Rate coding was tested by varying the firing rate of one size class while holding others at 80 spikes/s. Synchrony was manipulated by introducing correlated pauses across inputs. Cross-correlograms between individual PC input spike trains and CbN neuron output were computed to assess the timing influence of each input.

Complementary computational simulations using a simple integrate-and-fire CbN neuron model with conductance-based inhibitory inputs faithfully reproduced the experimental findings, allowing systematic exploration of parameter space including number and size of inputs, degree of synchrony, and firing rate.

## Target venue

eLife


## Experimental Log

# Experimental Log: Variable PC-CbN Synaptic Weights and Cerebellar Output Coding

## Animals and Slice Preparation

| Parameter | Value |
|-----------|-------|
| Species/strain | C57BL/6 wild-type mice (Charles River) |
| Sex | Both sexes |
| Age range (input size recordings) | P10-P32 |
| Age range (dynamic clamp) | P26-P32 |
| Slice orientation | Sagittal cerebellar nuclei |
| Slice thickness | 170 um |
| Cutting solution | Warm choline ACSF (34 C) |
| Recording temperature | 34-35 C |
| Flow rate | 3-5 ml/min |

## Electrophysiology Recording Conditions

| Parameter | Value |
|-----------|-------|
| Target neurons | Large CbN glutamatergic projection neurons (>70 pF) |
| Nuclei targeted | Lateral and interposed deep cerebellar nuclei |
| Recording mode (input sizes) | Whole-cell voltage clamp |
| Holding potential | -30 to -40 mV |
| Internal solution | High chloride (ECl = 0 mV), CsCl-based |
| Key internal components | 110 CsCl, 20 Cs-BAPTA, 2 QX314, 0.2 D600 |
| Plasticity blocker | BAPTA |
| Series resistance compensation | Up to 80% |
| Electrode resistance | 1-2 MOhm |

### Pharmacological Blockers Present

| Blocker | Target | Concentration |
|---------|--------|---------------|
| NBQX | AMPARs | 5 uM |
| (R,S)-CPP | NMDARs | 2.5 uM |
| Strychnine | Glycine receptors | 1 uM |
| CGP 55845 | GABABRs | 1 uM |

## Unitary PC-CbN Input Size Distributions (Fig 1)

### Recording Summary

| Age Group | Age Range | Number of Inputs Recorded |
|-----------|-----------|--------------------------|
| Young | P10-P20 | 74 |
| Juvenile | P23-P32 | 83 |

### Example Unitary Inputs from Single P27 Cell (Fig 1a-c)

| Input Classification | IPSC Amplitude (pA) |
|---------------------|---------------------|
| Small | 720 |
| Medium | 1690 |
| Large | 6280 |

### Distribution Comparison

| Property | Young (P10-20) | Juvenile (P23-32) |
|----------|---------------|-------------------|
| Distribution shape | Relatively uniform, modest variability | Highly skewed, many medium and large inputs |
| Statistical comparison (K-S test) | -- | p < 0.0001 vs. young |
| Similarity to prior literature | Consistent with Person & Raman 2012a (P13-29, n=30) | Novel finding -- skewed distribution only apparent with larger n |

- Fig 1d: Young mouse input size distribution is relatively narrow
- Fig 1e: Juvenile mouse input size distribution is markedly broader with a long tail toward large inputs
- Fig 1f: Cumulative histograms of IPSC conductances show significantly different distributions between age groups (p < 0.0001, K-S test)

## Dynamic Clamp Experimental Design

### Input Configuration (Fig 2)

| Input Class | Number of Inputs | Conductance per Input (nS) | Color Code |
|-------------|-----------------|---------------------------|------------|
| Small | 16 | 3 | Green |
| Medium | 10 | 10 | Blue |
| Large | 2 | 30 | Red |
| Total inputs | 28 | -- | -- |
| Total average conductance | ~228 nS at 80 Hz baseline | -- | -- |

- This configuration approximates the corrected juvenile PC-CbN input size distribution
- Fig 2a: Raster plots show spike times for all three input classes
- Fig 2b: Total conductance waveform (black) with color-coded contributions from each input class

### In Vivo PC Firing Properties (Fig 2 supplement 1)

| Parameter | Value |
|-----------|-------|
| Number of PCs recorded in vivo | 10 |
| ISI distribution fit | Lognormal |
| SD vs. mean relationship | Linear function |
| Firing rate range | Varied (indicated in legends) |

- Fig 2 supplement 1a: Normalized ISI histograms of 10 PCs with different firing rates
- Fig 2 supplement 1b: Same histograms normalized to peak
- Fig 2 supplement 1c: Example lognormal distribution fit to one PC (83 Hz)
- Fig 2 supplement 1d: Linear relationship between SD and mean of lognormal fits

## PC Refractory Period and Disinhibition Effect (Fig 3)

### ISI and Autocorrelation Analysis

| Input Type | Refractory Period | Autocorrelation at 0 ms | Key Feature |
|-----------|-------------------|------------------------|-------------|
| In vivo PC (low rate) | Present (several ms) | Peak at 1 | Post-refractory dip then recovery |
| In vivo PC (medium rate) | Present | Peak at 1 | Post-refractory dip then recovery |
| In vivo PC (high rate) | Present | Peak at 1 | Post-refractory dip then recovery |
| Poisson (no refractory) | Absent | Peak at 1 | Flat after 0 ms |

- Fig 3a: ISI histograms for three in vivo PCs (left panels) vs. artificial Poisson input (right)
- Fig 3b: Autocorrelation functions show clear refractory period effects for real PCs but not Poisson
- The refractory period creates a temporal window of reduced spike probability after each PC spike

### Spike-Triggered Conductance and CbN Response (Fig 3c)

| Condition | Pre-spike Conductance | Post-spike Conductance | CbN Effect |
|-----------|----------------------|----------------------|------------|
| Real PC (with refractory period) | Drops briefly (disinhibition) | Sharp increase (inhibition) | Brief firing elevation THEN suppression |
| Poisson (no refractory period) | Flat | Sharp increase | Pure suppression only |

- Fig 3c: Calculated spike-triggered average inhibitory conductances for different input configurations
- Key finding: PC refractory period creates a brief conductance dip before each spike, leading to transient CbN disinhibition preceding inhibition

## Constant vs. Fluctuating Inhibitory Conductance (Fig 4)

### CbN Firing Under Constant Inhibitory Conductance (Fig 4a-b)

| Constant Conductance (nS) | CbN Firing Rate Pattern |
|---------------------------|------------------------|
| Low | High firing rate |
| Medium | Moderate firing rate |
| High | Low/suppressed firing rate |
| Very high | Near-zero firing |

- Fig 4a: Example CbN spiking at different constant conductance levels
- Fig 4b: Summary of CbN firing rates (n=7 cells) shows monotonic decrease with increasing conductance

### Effect of Conductance Fluctuations at Same Mean (Fig 4c-d)

| Condition | Mean Conductance (nS) | Input Configuration | CbN Firing Rate |
|-----------|----------------------|--------------------|-----------------| 
| Constant | 56 | Flat conductance | Lowest firing rate |
| Low variability | 56 | Many small uniform inputs | Low firing |
| Medium variability | 56 | Mix of sizes | Moderate firing |
| High variability | 56 | Fewer, larger inputs | Highest firing rate |

- Fig 4c: Different input configurations producing the same average conductance (56 nS) but different fluctuation levels
- Fig 4d: CbN neuron firing increases with conductance variability even when mean is identical
- Key insight: nonuniform input sizes elevate baseline CbN firing by increasing inhibitory conductance variability

## Rate Code Experiments (Fig 5)

### Experimental Protocol

- Dynamic clamp with small (16 x 3 nS), medium (10 x 10 nS), and large (2 x 30 nS) inputs
- Firing rate of one input class varied every 2 seconds while others held at 80 spikes/s

### Rate Code Transmission by Input Size

| Input Class Varied | Rate Range Tested | Effect on Mean Inhibitory Conductance | Effect on CbN Firing Rate | Sensitivity |
|-------------------|-------------------|--------------------------------------|--------------------------|-------------|
| Small (16 x 3 nS) | Varied around 80 Hz | Small modulation | Modest inverse modulation | Low |
| Medium (10 x 10 nS) | Varied around 80 Hz | Moderate modulation | Clear inverse modulation | Moderate |
| Large (2 x 30 nS) | Varied around 80 Hz | Large modulation | Strong inverse modulation | High |

- Fig 5a: Rate variations for each input class shown separately
- Fig 5b: Resulting average inhibitory conductances for the three conditions
- Fig 5c: CbN firing rate changes inversely with PC input firing rate for all sizes
- Key finding: all input sizes can convey rate codes, but large inputs have disproportionate influence

## Cross-Correlogram Analysis of Individual Inputs

### Timing Influence by Input Size

| Input Size | Cross-Correlogram Features | Pre-spike Effect | Post-spike Effect | Duration of Suppression |
|-----------|---------------------------|-----------------|-------------------|------------------------|
| Small (3 nS) | Weak modulation | Minimal disinhibition | Brief, weak suppression | Short (~1-2 ms) |
| Medium (10 nS) | Moderate modulation | Moderate disinhibition | Clear suppression | Moderate (~2-4 ms) |
| Large (30 nS) | Strong modulation | Strong disinhibition peak | Deep suppression | Extended (several ms) |

- Large inputs transiently eliminate CbN firing for several milliseconds following each PC spike
- The refractory-period-driven disinhibition peak is visible before suppression for all input sizes but most prominent for large inputs

## Synchrony Experiments (Fig 6)

### Uniform Inputs -- Synchrony Effect on Firing Rate (Fig 6a)

| Synchrony Level | Input Configuration | CV of Inhibitory Conductance | CbN Firing Rate Change |
|----------------|--------------------|-----------------------------|----------------------|
| 0% (desynchronized) | 40 x 5 nS | Low | Baseline |
| 25% | 40 x 5 nS | Moderate | Increased |
| 50% | 40 x 5 nS | High | Further increased |
| 75% | 40 x 5 nS | Very high | Substantially increased |
| 100% (fully synchronized) | 40 x 5 nS | Maximum | Maximum increase |

- Fig 6a.i: Synchrony of uniform inputs varies from desynchronized to fully synchronized
- Fig 6a.ii: Inhibitory conductance waveforms show increasing fluctuations with synchrony
- Fig 6a.iii: CV of inhibitory conductance increases with synchrony
- Fig 6a.iv: CbN neuron firing rate increases with synchrony for uniform inputs

### Nonuniform Inputs -- Synchrony Effect on Firing Rate (Fig 6b)

| Synchrony Level | Input Configuration | CV of Inhibitory Conductance | CbN Firing Rate Change |
|----------------|--------------------|-----------------------------|----------------------|
| 0% (desynchronized) | 16S + 10M + 2L | Already elevated (baseline) | Higher baseline than uniform |
| 25% | 16S + 10M + 2L | Increased | Modest increase |
| 50% | 16S + 10M + 2L | Further increased | Moderate increase |
| 100% | 16S + 10M + 2L | Maximum | Increase but relatively smaller |

- The relative influence of synchrony on CbN firing rate is SMALLER for nonuniform than uniform inputs
- This is because nonuniform inputs already produce high conductance variability at baseline

### Synchrony of Selected Large Inputs

| Condition | Inputs Synchronized | Effect on CbN Firing |
|-----------|--------------------|--------------------|
| No large input synchrony | 0 of 2 large inputs | Baseline |
| Two large inputs synchronized | 2 of 2 large inputs | Significant increase in CbN firing |

- Synchronizing even two large inputs can meaningfully increase CbN neuron firing
- This provides a mechanism for timing-based coding without requiring widespread PC synchrony

## Cross-Correlograms for Synchrony Conditions (Fig 7)

### Uniform Inputs (Fig 7k)

| Condition | Cross-Correlogram Shape | Normalized to Baseline |
|-----------|------------------------|----------------------|
| Nonsynchronous | Weak modulation, broad | Small dips/peaks |
| 50% synchronous | Sharper modulation | Clear suppression-rebound pattern |

### Nonuniform Inputs by Size (Fig 7l)

| Input Size | Nonsynchronous Shape | 50% Synchronous Shape |
|-----------|---------------------|----------------------|
| Small (3 nS) | Very weak | Modest modulation |
| Medium (10 nS) | Moderate | Enhanced modulation |
| Large (30 nS) | Strong disinhibition-suppression | Very strong disinhibition-suppression |

- Fig 7k: Cross-correlograms for uniform inputs show synchrony sharpens timing influence
- Fig 7l: For nonuniform inputs, large inputs dominate cross-correlogram structure regardless of synchrony level

## Simulation Model Parameters

| Parameter | Value |
|-----------|-------|
| Neuron model | Simple integrate-and-fire |
| Input type | Conductance-based inhibitory |
| Excitatory drive | Modeled as constant or Poisson |
| Reproduction of experimental data | Faithful match to dynamic clamp results |

### Simulation Explorations

| Parameter Varied | Range | Key Finding |
|-----------------|-------|-------------|
| Number of inputs | Varied | More inputs with same total conductance = less variability = lower baseline rate |
| Input size distribution | Uniform vs. skewed | Skewed distributions increase firing rate and timing precision |
| Firing rate of inputs | 10-150 Hz | Rate code transmission confirmed for all configurations |
| Synchrony fraction | 0-100% | Relative synchrony influence depends on input size distribution |
| Number of large inputs synchronized | 1-5 | Even 2 large inputs synchronized has measurable effect |

## Summary of Key Physiological Findings

| Finding | Implication |
|---------|------------|
| Juvenile PC-CbN inputs are highly variable (skewed distribution) | Previous uniform-size assumptions do not hold in mature animals |
| Large single inputs strongly modulate CbN timing | Individual PCs can have outsized influence without synchrony |
| PC refractory period causes pre-spike disinhibition | CbN neurons receive a brief excitatory signal before each inhibitory event |
| Nonuniform sizes elevate baseline CbN rates | Variability in inhibitory conductance is functionally equivalent to partial disinhibition |
| Rate codes work for all input sizes | PC-CbN synapses support rate coding regardless of weight |
| Synchrony effect is relatively reduced for nonuniform inputs | But synchronizing few large inputs still effective |
| Disinhibition-inhibition sequence per PC spike | Creates precisely timed CbN output locked to PC firing |

## Datasets and Methods Summary

| Resource/Method | Application |
|----------------|-------------|
| Minimal stimulation electrophysiology | Isolate unitary PC-CbN inputs |
| Dynamic clamp | Inject realistic PC conductance patterns into CbN neurons |
| In vivo PC recordings (10 cells) | Provide realistic firing statistics |
| Lognormal ISI fitting | Parameterize PC firing for dynamic clamp |
| Cross-correlogram analysis | Quantify timing influence of individual inputs |
| Integrate-and-fire simulation | Systematic parameter exploration |
| Kolmogorov-Smirnov test | Compare input size distributions across ages |

