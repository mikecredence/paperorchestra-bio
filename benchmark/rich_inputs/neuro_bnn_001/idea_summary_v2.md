## Working title

Network Statistics of the Whole-Brain Connectome of Drosophila

## Core question

What are the large-scale network properties, recurring connectivity motifs, and organizational principles of the first complete adult Drosophila brain connectome -- and how do these features compare across brain regions and with other organisms?

## Motivation / gap

- Mesoscale connectomes (MRI/MEG-based) exist for mammalian brains, but they rely on functional correlation proxies rather than direct synaptic-resolution wiring
- Prior microscale connectome analyses have been limited to small nervous systems (C. elegans ~300 neurons, partial Drosophila volumes like the hemibrain)
- The FlyWire whole-brain connectome (~130k neurons, millions of connections) is now available but its global network topology has not been systematically characterized
- Rich club organization has been observed at mesoscale in several species, but never validated at synaptic resolution in a complete brain
- No comprehensive survey of 2- and 3-node motif frequencies exists at whole-brain scale for any organism
- It remains unclear how network features (motif composition, reciprocity, clustering) differ across anatomically distinct brain regions (neuropils) within a single brain
- Identifying which highly connected neurons serve as integrators vs. broadcasters could guide experimental neuroscience toward key circuit elements

## Core contribution (bullet form)

- Comprehensive characterization of the FlyWire whole-brain network: 127,978 neurons and 2,613,129 thresholded connections (threshold = 5 synapses/connection), including degree distributions, path length analysis (mean shortest path ~4.5 hops within the giant SCC containing 93.3% of neurons), and robustness to node removal
- Discovery of rich club organization at synaptic resolution: ~30% of the connectome qualifies as rich club neurons, far exceeding what random or configuration-model null models predict
- Classification of rich club neurons into functional subtypes -- broadcasters (high out-degree, low in-degree), integrators (high in-degree, low out-degree), and large balanced neurons -- with distinct neurotransmitter compositions and superclass distributions
- Whole-brain census of 2-node and 3-node motifs with comparison to Erdos-Renyi and configuration (CFG) null models: reciprocal connections and recurrent motifs (e.g., 3-cycles, motif #9, motif #13) are over-represented while simple feedforward chains are under-represented
- Characterization of reciprocal connections: reciprocity = 0.138 (higher than all null models), reciprocal edges are stronger on average than unidirectional ones, GABAergic neurons are over-represented in reciprocal pairs
- Region-specific network analysis across 78 anatomically defined neuropils, revealing substantial variation in motif composition, connection strength distributions, and local clustering -- e.g., the ellipsoid body and antennal lobe display distinct motif profiles

## Method in brief

The study builds a weighted directed graph from the FlyWire v630 snapshot of a 7-day-old adult female Drosophila melanogaster brain. For each neuron pair, the total number of algorithmically detected synapses (confidence > 50) is summed to produce edge weights. A threshold of 5 synapses per connection is applied throughout to reduce false positives from the automated synapse detection pipeline. Neurotransmitter identity for each neuron is assigned by averaging per-synapse predictions from a convolutional neural network across all outgoing synapses, then taking the highest-probability transmitter among 6 candidates (acetylcholine, GABA, glutamate, dopamine, octopamine, serotonin).

Network analyses include: (1) computation of in-degree and out-degree distributions, connected component decomposition (strongly and weakly connected components), and shortest path length distributions within the giant SCC; (2) systematic enumeration of all 2-node and 3-node directed motifs with comparison to Erdos-Renyi (ER) and configuration (CFG) null models (100 random instances each); (3) rich club coefficient computation as a function of degree threshold, compared against null model expectations; (4) subdivision of the connectome into 78 neuropil-level subnetworks based on synapse location and separate motif/connectivity analysis for each.

Robustness checks include varying the synapse threshold, testing node-removal strategies (targeted vs. random) to assess network resilience, and computing edge percolation curves. All data products (neuron lists, connectivity tags, motif counts) are shared publicly via the FlyWire Codex platform.

## Target venue

Nature
