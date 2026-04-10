## Working title

Network Statistics of the Whole-Brain Connectome of Drosophila

## Core question

What are the fundamental network-level organizational principles of a complete adult brain, and how do graph-theoretic properties such as motif prevalence, rich-club structure, and small-world characteristics emerge at whole-brain scale in Drosophila melanogaster?

## Motivation / gap

- The FlyWire project produced the first whole-brain connectome of an adult Drosophila, containing over 130,000 neurons and tens of millions of synapses, but systematic network analysis of this resource had not been performed
- Previous connectome-scale network analyses were limited to partial circuits or the much simpler C. elegans nervous system (302 neurons), leaving whole-brain network organization in a complex brain unexplored
- Understanding whether biological neural networks share organizational principles with engineered or theoretical networks requires quantitative characterization at whole-brain scale
- The relationship between network motif composition, neurotransmitter identity, and cell type classification in a complete brain connectome was unknown

## Core contribution

- First comprehensive graph-theoretic analysis of an entire adult brain connectome (127,978 neurons, 2.6 million thresholded connections)
- Demonstration of rich-club organization spanning approximately 30% of the connectome, identifying highly connected hub neurons that may serve as signal integrators or broadcasters
- Quantification of two-node and three-node network motifs across the whole brain, revealing overrepresentation of recurrent motifs relative to null models
- Measurement of clustering coefficient (0.048), small-world properties, path length distributions, and edge reciprocity at whole-brain scale
- Comparison of fly brain network statistics with connectomes from other organisms (C. elegans, mouse partial connectomes)
- Integration of network metrics with neurotransmitter identity (acetylcholine, GABA, glutamate) and cell type annotations

## Method in brief

The FlyWire v630 connectome snapshot is analyzed as a directed weighted graph with 127,978 nodes (neurons) and edges weighted by synapse count. A threshold of 5 synapses per connection is applied to filter spurious synaptic detections. Network statistics computed include: degree distributions (in-degree, out-degree, total degree), synapse count distributions, strong and weak connected components, edge percolation analysis, edge reciprocity, clustering coefficient, shortest path distributions, and small-world index. Two-node and three-node motif census is performed and compared against Erdos-Renyi (ER) and configuration model (CFG) null networks. Rich-club analysis identifies neurons with total degree exceeding 37 as belonging to the rich-club regime. All metrics are cross-referenced with FlyWire cell type annotations and predicted neurotransmitter identities.

## Target venue

Nature
