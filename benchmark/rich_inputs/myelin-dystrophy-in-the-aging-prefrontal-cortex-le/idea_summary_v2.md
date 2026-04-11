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
