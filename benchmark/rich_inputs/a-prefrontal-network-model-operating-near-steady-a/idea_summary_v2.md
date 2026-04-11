## Working title

Linking NMDAR synaptic deficits to spike desynchronization in schizophrenia through a prefrontal spiking network model operating near a steady-oscillatory boundary

## Core question

How do NMDA receptor synaptic deficits -- implicated by genetic evidence as causal in schizophrenia -- lead to the loss of zero-lag spike synchrony observed in prefrontal cortical circuits, and what network-level mechanism connects synaptic-level disruptions to circuit-level failures?

## Motivation / gap

- Schizophrenia involves prefrontal network dysfunction, but the bridge from synaptic perturbation to network-level failure is poorly understood
- Experimental work in monkey PFC showed that NMDAR blockade (phencyclidine) reduces zero-lag synchronous spiking before motor responses during cognitive control tasks (DPX task)
- Similar desynchronization phenotype was found in a mouse genetic model (miRNA-processing risk gene deletion), suggesting convergent pathogenesis
- No existing computational model explains *why* NMDAR loss specifically prevents the task-locked emergence of synchrony
- Understanding this synaptic-to-network link is critical for connecting genetic risk factors to cognitive deficits in the disease

## Core contribution (bullet form)

- Developed a recurrent spiking network model (4,000 excitatory + 1,000 inhibitory neurons, connection probability 0.2) with explicit AMPAR, NMDAR, and GABAR synaptic currents that reproduces monkey PFC spike timing data
- Used linear stability analysis and mean field theory to derive a state diagram in the (AMPA/GABA, external input) parameter plane, identifying a critical boundary separating asynchronous and synchronous oscillatory regimes
- Showed that a network tuned near this critical boundary ("critical state") can switch from asynchronous to synchronous gamma oscillations (~40 Hz) with small increases in external input, producing zero-lag spike synchrony
- Demonstrated that reducing NMDAR conductance prevents the network from crossing into the synchronous regime, thereby explaining the experimentally observed desynchronization under PCP
- Found that the AMPA/GABA balance controls the oscillation frequency at the onset of instability, while the NMDA/GABA balance controls the orientation of the critical line and thus how sensitive the network is to external input modulation
- Provided direct quantitative comparison between model spike correlations and monkey PFC recordings in drug-naive vs. drug conditions across task epochs

## Method in brief

The model is a sparsely connected recurrent spiking network of leaky integrate-and-fire neurons: 4,000 excitatory and 1,000 inhibitory, connected randomly with probability 0.2. Excitatory synapses carry both fast AMPA and slow NMDA receptor-mediated currents, while inhibitory synapses carry GABA-mediated currents. The NMDA current includes voltage-dependent magnesium block. External inputs are modeled as independent Poisson spike trains driving both populations.

The key analytical approach combines mean field theory (to find self-consistent firing rates and synaptic conductances) with linear stability analysis of the asynchronous state. The stability analysis yields the rate of instability growth (lambda) as a function of network parameters, defining a critical line (lambda = 0) in the parameter plane that separates stable asynchronous states from oscillatory synchronous states. This critical line depends on the ratios of NMDA-to-GABA and AMPA-to-GABA currents as well as external input strength.

Two reference networks were analyzed: a "steady state" network operating deep in the asynchronous regime and a "critical state" network positioned just below the critical boundary. Simulations verified that only the critical state network transitions to synchronous gamma oscillations when external input increases, and that reducing NMDAR conductance (simulating PCP blockade) prevents this transition. Spike correlations and synchrony metrics from the model were directly compared with those measured from 47 neural ensembles (893 neurons total) recorded in monkey dorsolateral PFC during the DPX cognitive control task.

## Target venue

eLife
