# Experimental Log: Criticality and Partial Synchronization Analysis in Wilson-Cowan and Jansen-Rit Neural Mass Models

## 1. Model Specifications

### 1.1 Wilson-Cowan (WC) Model Parameters

| Parameter | Symbol | Value | Interpretation |
|---|---|---|---|
| Excitatory time constant | tau_E | Model-specific | Time constant for excitatory population |
| Inhibitory time constant | tau_I | Model-specific | Time constant for inhibitory population |
| Excitatory sigmoid threshold | theta_E | Model-specific | Maximum slope value for excitatory subpopulation |
| Inhibitory sigmoid threshold | theta_I | Model-specific | Maximum slope value for inhibitory subpopulation |
| Excitatory sigmoid slope | a_E | Model-specific | Slope of sigmoid for excitatory population |
| Inhibitory sigmoid slope | a_I | Model-specific | Slope of sigmoid for inhibitory population |
| E-to-E connectivity | c_EE | Model-specific | Excitatory-excitatory synaptic weight |
| E-to-I connectivity | c_EI | Model-specific | Excitatory-inhibitory synaptic weight |
| I-to-E connectivity | c_IE | Model-specific | Inhibitory-excitatory synaptic weight |
| I-to-I connectivity | c_II | Model-specific | Inhibitory-inhibitory synaptic weight |
| External input | P(t) | Model-specific | External stimuli acting on excitatory subpopulation |
| Oscillatory regime | -- | Delta band | Parameters chosen to match delta-band activity |

Note: Exact parameter values are given in Table 1 of the paper. The WC model describes the dynamics of firing rates with two coupled differential equations for E(t) and I(t) populations, each passed through a sigmoid activation function S.

### 1.2 Jansen-Rit (JR) Model Parameters

| Parameter | Symbol | Value | Interpretation |
|---|---|---|---|
| Mean PSP (pyramidal) | y_0 | From Table 2 | Mean postsynaptic potential of pyramidal neurons |
| Mean PSP (excitatory interneurons) | y_1 | From Table 2 | Mean PSP of excitatory interneurons |
| Mean PSP (inhibitory interneurons) | y_2 | From Table 2 | Mean PSP of inhibitory interneurons |
| Deviation (pyramidal) | y_3 | From Table 2 | Deviation of pyramidal PSP |
| Deviation (excitatory) | y_4 | From Table 2 | Deviation of excitatory interneuron PSP |
| Deviation (inhibitory) | y_5 | From Table 2 | Deviation of inhibitory interneuron PSP |
| External input | p(t) | Variable | External input from other columns |
| Oscillatory regime | -- | Alpha band (~8-12 Hz) | Experimentally derived parameters |

Note: Exact parameter values are given in Table 2 of the paper. The JR model uses six first-order ODEs and a sigmoid transform, producing richer dynamics than the WC model.

## 2. Network Construction

| Parameter | Value |
|---|---|
| Number of nodes (N) | Network of coupled oscillators |
| Topology | Small-world |
| Inter-node coupling | Through excitatory populations (WC) or excitatory connections (JR) |
| Adjacency matrix | M_il defines connections between nodes |
| Coupling coefficient | K (swept across range) |
| Number of simulation runs per K | 20 |

### 2.1 WC Network Equations

The coupled WC network for N nodes (i = 1,...,N) includes an adjacency matrix M_il and coupling coefficient K linking excitatory populations across nodes.

### 2.2 JR Network

Pyramidal neurons in each JR node receive input from excitatory and inhibitory interneurons within the same column, plus external input from other columns via the coupling term.

## 3. Synchronization Analysis

### 3.1 Kuramoto Order Parameter (KOP) Results

#### JR Model (Figure 2A)

| Coupling Coefficient K | KOP Value (approx.) | Dispersion (SD) | Regime |
|---|---|---|---|
| 0 to ~1.0 | Low (increasing) | Low | Unsynchronized |
| 1.25 | Sharp increase | High | Transition onset (start of high synchrony regime) |
| 1.5 | High | Large variance | Candidate phase transition point |
| 2.0 to 4.0 | High | Moderate | High synchrony regime (coherent state) |
| 4.0 | High | Large variance | Candidate phase transition point |
| 4.25 | Transition | High | End of high synchrony regime |
| >4.25 | Decreasing | Variable | Transition out of high synchrony |

Fig 2A: KOP vs coupling coefficient for JR model. High synchrony regime spans K = 1.25 to 4.25. Large dispersions at K = 1.25 and 4.25 mark boundaries. Coupling values K = 1.5 and K = 4.0 show large variance in mean KOP, serving as candidate phase transition points.

#### WC Model (Figure 2B)

| Coupling Coefficient K | KOP Value (approx.) | Dispersion (SD) | Regime |
|---|---|---|---|
| 0 to ~0.075 | Increasing | Low | Approaching synchrony |
| 0.075 to 0.175 | Decreasing (local minimum) | Variable | Unexpected desynchronization |
| >0.175 | Increasing again | Variable | Resuming synchronization trend |

Fig 2B: KOP vs coupling coefficient for WC model. Between K = 0.075 and 0.175, an unexpected decrease in synchronization was observed despite increasing coupling strength. This local minimum pattern has also been reported in Kuramoto model networks.

### 3.2 Comparison of Synchronization Behavior

| Feature | JR Model | WC Model |
|---|---|---|
| Transition from low to high sync | Yes | Yes |
| High synchrony regime | K = 1.25 to 4.25 | Gradual increase (no sharp plateau) |
| Local minimum in KOP | No | Yes (K = 0.075 to 0.175) |
| Global synchronization | Yes (K = 2 to 4) | Not observed (partial sync instead) |
| Partial synchronization | Not prominent | Yes (synchronous + asynchronous coexisting) |
| Phase transition candidate | K = 1.5 and K = 4.0 | Not clearly identified |

## 4. Partial Synchronization Analysis (Figures 3 and 4)

### 4.1 JR Model Output Matrices (Figure 3)

| Coupling Range | Observed Pattern | Brain State Analogy |
|---|---|---|
| Small K | Randomly distributed activity | Incoherent (healthy asynchronous state) |
| K = 2 to 4 | Complete synchronization (coherent in space and time) | Pathological (epileptic seizure-like) |
| K > 4.25 | Transition back from coherent state | -- |

Fig 3: Colored output matrices for JR model during last 2 seconds at different K values. In K = 1.25 to 4.25, the output signal shows ordered behavior (global synchronization). This coherent state corresponds to pathological brain activity (e.g., seizures).

### 4.2 WC Model Output Matrices (Figure 4)

| Coupling Range | Observed Pattern | Brain State Analogy |
|---|---|---|
| Small K | Randomly distributed activity | Incoherent state |
| K = 0.075 to 0.175 | Slight time-delay synchronization | Partial synchronization |
| Larger K | Synchronous and asynchronous behaviors coexist | Partial synchronization persists |

Fig 4: Colored output matrices for WC model during last 2 seconds at different K values. In K = 0.075 to 0.175, nodes show synchronization with slight delays. The WC model exhibits simultaneous synchronous and asynchronous dynamics, which was not observed in JR model.

### 4.3 Partial vs. Global Synchronization Summary

| Synchronization Type | JR Model | WC Model | Physiological Relevance |
|---|---|---|---|
| Global synchronization | Present (K = 2-4) | Not observed | Pathological (seizures, Parkinson's) |
| Partial synchronization | Not prominent | Present | Healthy brain function |
| Asynchronous state | Low K only | Coexists with synchronous nodes | Resting state |

## 5. Coefficient of Variation (CV) Analysis (Figure 5)

### 5.1 CV of KOP vs. Coupling Coefficient

| Model | CV Maxima Location | Interpretation |
|---|---|---|
| JR (Fig 5A) | At transition points matching Fig 2A | CV maxima correspond to candidate phase transition points |
| WC (Fig 5B) | No clear sharp maxima | No clear second-order phase transition |

Fig 5A: CV vs coupling coefficient for JR model shows peaks at coupling values corresponding to the synchronization transitions in Fig 2A, supporting the presence of SOPT.
Fig 5B: CV vs coupling coefficient for WC model does not show the sharp peaks characteristic of SOPT.

### 5.2 Second-Order Phase Transition (SOPT) Detection

| Model | SOPT Detected? | Evidence |
|---|---|---|
| JR | Yes | CV maxima at transition points; sharp KOP changes |
| WC | No | No clear CV peaks; gradual KOP changes |

## 6. Detrended Fluctuation Analysis / Power-Law Behavior (Figure 6)

### 6.1 DFA Results

| Model | Power-Law Behavior | LRTCs Present? | Log-Log Plot Shape |
|---|---|---|---|
| JR (Fig 6A) | Not observed | No | Piecewise linear; linear fit not suitable |
| WC (Fig 6B) | Not observed | No | Piecewise linear; linear fit not suitable |

Fig 6A: Log-log fluctuation plot for JR model at an arbitrary coupling value. X-axis shows segment sizes (seconds on log scale), Y-axis shows mean standard deviation. Data trend is piecewise linear, and a single linear fit is inappropriate, indicating no power-law scaling.
Fig 6B: Log-log fluctuation plot for WC model. Same piecewise linear pattern; no power-law behavior detected.

### 6.2 Criticality Assessment

| Criterion | JR Model | WC Model |
|---|---|---|
| Phase transition | Yes (SOPT) | No |
| Power-law behavior | No | No |
| Long-range temporal correlations | No | No |
| Overall criticality | Not achieved | Not achieved |

Key conclusion: A continuous phase transition (SOPT) at a critical point is a necessary but not sufficient condition for criticality. Neither model achieved true criticality under the tested conditions because power-law behavior and LRTCs were absent.

## 7. Model Dynamics Comparison

| Feature | WC Model | JR Model |
|---|---|---|
| Dimensionality | 2D system (E, I equations) | 6 first-order ODEs |
| Output type | Firing rate | Voltage (mean PSP) |
| Oscillatory types possible | Fixed points, limit cycles | Multiple brain wave types, spike-like, alpha-like |
| Bifurcation structure | Hopf bifurcation | Rich bifurcation diagram |
| Frequency regime (this study) | Delta band | Alpha band (~8-12 Hz) |
| Biophysical detail | Lower | Higher |
| Global synchronization capacity | Limited | Strong |
| Partial synchronization capacity | Strong | Limited |

## 8. Network Topology Details

| Parameter | Value |
|---|---|
| Topology type | Small-world |
| Node coupling | Excitatory populations linked between nodes |
| Coupling coefficient range (JR) | Swept from 0 to beyond 4.25 |
| Coupling coefficient range (WC) | Swept from 0 to beyond 0.175 |
| Runs per coupling value | 20 |
| Analysis window | Last 2 seconds of simulation (for output matrices) |

## 9. Analytical Measures Summary

| Measure | Purpose | Application |
|---|---|---|
| Kuramoto Order Parameter (KOP) | Quantify global phase synchronization | Both models, across coupling range |
| Coefficient of Variation (CV) of KOP | Detect SOPT via dispersion peaks | Both models |
| Colored output matrices | Visualize spatial-temporal synchronization patterns | Both models |
| Detrended Fluctuation Analysis (DFA) | Test for power-law scaling and LRTCs | Both models |
| Log-log fluctuation plots | Assess linearity (power-law criterion) | Both models |

## 10. Key Equations

| Equation | Description |
|---|---|
| WC firing rate equations | dE/dt and dI/dt with sigmoid S, connectivity c, external input P(t) |
| Sigmoid function S | S = 1/(1 + exp(-a*(x - theta))), with threshold theta and slope a |
| JR six ODEs | y_0 through y_5 with sigmoid transforms for pyramidal, excitatory, and inhibitory populations |
| KOP | r(t) = (1/N) * abs(sum(exp(i*theta_j(t)))), measures phase coherence |
| CV of KOP | CV = std(KOP) / mean(KOP), peaks indicate phase transitions |
| Network coupling | K * sum(M_il * E_l) added to excitatory input of each node |

## 11. Physiological Relevance

| Finding | Clinical/Neuroscience Implication |
|---|---|
| JR global sync (K=2-4) | Models pathological states like epileptic seizures |
| WC partial sync | Better represents healthy brain dynamics where some regions synchronize while others do not |
| Neither model shows criticality | Suggests that standard neural mass models with small-world topology may need additional mechanisms to achieve critical dynamics |
| SOPT in JR only | JR's richer dynamics (6 ODEs) enable phase transitions that 2D WC cannot produce |

## 12. Reference Context

| Item | Value |
|---|---|
| Total references | 75 |
| Key related phenomena | Epileptic seizure activity, Parkinson's, essential tremor, alpha rhythm |
| Experimental validation reference | Macaque monkey visual system partial synchronization |
| Related model studies | Kuramoto model local minimum in KOP also reported |
