## Working title

Criticality and partial synchronization analysis in Wilson-Cowan and Jansen-Rit neural mass models on small-world networks

## Core question

Do Wilson-Cowan (rate-based) and Jansen-Rit (voltage-based) neural mass models, when coupled in small-world network topologies, exhibit second-order phase transitions, power-law behavior, and partial synchronization patterns relevant to healthy and pathological brain states?

## Motivation / gap

- Neural mass models have been used for decades to model mesoscopic brain dynamics, but their ability to demonstrate second-order phase transitions (SOPT) and criticality has received insufficient attention
- Global synchronization in neural networks is associated with pathological states (epilepsy, Parkinson's), while partial synchronization may better represent healthy brain function, yet systematic comparison of WC and JR models on this dimension is lacking
- The critical brain hypothesis proposes that healthy brain networks operate near a phase transition, but whether standard neural mass models can reproduce this behavior is unclear
- Previous synchronization studies focused mostly on global synchronization (all nodes in unison) rather than the more physiologically relevant partial synchronization patterns
- No prior study has directly compared WC and JR models using the same network topology and the same synchronization/criticality measures

## Core contribution (bullet form)

- Constructed networks of coupled WC and JR nodes with small-world topologies and quantified synchronization using the Kuramoto order parameter (KOP)
- Both models showed transitions from unsynchronized to highly synchronized states as coupling weight increased, but the transition characteristics differed: JR exhibited a second-order phase transition, while WC did not
- In the JR model, a high-synchrony regime was identified between coupling coefficients K=1.25 and K=4.25, with candidate phase transition points at K=1.5 and K=4.0 (large KOP variance)
- In the WC model, an unexpected local minimum in KOP was found between K=0.075 and K=0.175 where synchronization decreased despite increasing coupling
- Neither WC nor JR models exhibited power-law behavior in fluctuation analysis, indicating that SOPT alone is not sufficient for criticality in these models
- WC model produced partial synchronization patterns (synchronous and asynchronous behaviors simultaneously), while JR model showed global synchronization -- suggesting WC may be more appropriate for modeling healthy brain dynamics

## Method in brief

Two networks of N coupled neural mass nodes were constructed with small-world topology. The Wilson-Cowan model describes excitatory and inhibitory population firing rates via a 2D system of differential equations with sigmoid activation functions, connectivity coefficients (cEE, cEI, cIE, cII), and external input P(t). The Jansen-Rit model uses six first-order ODEs describing pyramidal cells, excitatory interneurons, and inhibitory interneurons, with sigmoid transforms and parameters derived from experimental data. Both models were tuned to produce oscillatory behavior (WC in delta band, JR producing alpha-like activity).

For each model, simulations were run across a range of coupling coefficients K, with 20 runs per coupling value to assess variability. The Kuramoto order parameter (KOP) was computed from the output phase of each node to quantify global synchronization. The coefficient of variation (CV) of KOP was used to detect potential SOPT (maxima in CV correspond to transition points). Partial synchronization was assessed by examining colored output matrices showing the temporal activity of all nodes. Detrended fluctuation analysis (DFA) was applied to test for long-range temporal correlations (LRTCs) and power-law behavior, plotted in log-log space and assessed for linearity.

## Target venue

PLOS ONE
