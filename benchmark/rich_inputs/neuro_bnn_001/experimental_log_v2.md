# Experimental Log: Whole-Brain Drosophila Connectome Network Analysis

## Dataset Overview

| Parameter | Value |
|---|---|
| Organism | Adult female Drosophila melanogaster (7-day-old) |
| Genotype | [iso] w1118 x [iso] Canton-S G1 |
| Dataset version (primary) | FlyWire v630 Snapshot |
| Dataset version (updated) | FlyWire v783 Snapshot |
| Total neurons (v630) | 127,978 |
| Total thresholded connections (v630) | 2,613,129 |
| Total synapses | ~32 million |
| Synapse threshold | 5 synapses per connection |
| Total neurons (v783) | 139,255 |
| Total thresholded connections (v783) | 2,701,601 |
| Synapse detection method | Algorithmic (automated) |
| Synapse confidence cutoff | 50 |
| Central brain proofreading | Fully proofread |
| Optic lobe proofreading (v630) | ~80% complete |
| Optic lobe proofreading (v783) | Complete |
| Missing neurons (v630) | Mostly photoreceptors |
| Neurotransmitter prediction accuracy | 87% per-synapse |
| Number of neurotransmitter classes | 6 (ach, gaba, glut, da, oct, ser) |
| Number of anatomical brain regions (neuropils) | 78 |
| Data availability platform | FlyWire Codex (codex.flywire.ai) |

---

## Experiment 1: Whole-Brain Network Properties

### 1.1 Connected Component Analysis

| Metric | Value |
|---|---|
| Giant strongly connected component (SCC) size | 93.3% of all neurons |
| Giant weakly connected component (WCC) size | 98.8% of all neurons |
| Synapse threshold used | 5 synapses/connection |

The giant SCC contains the vast majority of neurons, meaning nearly all neurons can reach each other via directed paths. The giant WCC is even larger, covering almost the entire brain when edge direction is ignored.

### 1.2 Shortest Path Length Distribution

Fig 1d shows the distribution of shortest path lengths between neuron pairs within the giant SCC. The network is compact -- neurons are separated by relatively few synaptic hops.

Fig 1e shows path length distributions within the giant WCC (ignoring edge direction).

### 1.3 Node Removal / Robustness Analysis

Fig 1f shows the sizes of the first two SCCs as high-degree neurons are progressively removed (2,500 neurons per step). When neurons of approximately degree 50 begin to be removed via targeted removal (highest degree first), the brain splits into two SCCs. This is a clear deviation from random-order removal, which preserves the giant SCC for much longer.

Fig S2a shows the analogous analysis for WCCs (1 neuron per step). The WCC also fractures earlier under targeted removal than random removal, with the split occurring around degree 50 as well.

### 1.4 Degree Distribution

Fig 1c plots in-degree (number of presynaptic partners) vs. out-degree (number of postsynaptic partners) on log-log axes. The distribution is broad, spanning several orders of magnitude.

### 1.5 Synapse Distribution

Fig 1b shows the distribution of the number of synapses per connected neuron pair. Most connections have relatively few synapses.

### 1.6 Distance-Dependent Connectivity

Fig S1d shows synapse probability and connection probability as a function of the average distance between neuronal arbors (based on a subsample of 700 million pairs, representing 5% of the total ~14 billion possible pairs).

---

## Experiment 2: Connection Statistics and Null Model Comparisons

### 2.1 Core Network Statistics

| Statistic | Fly Brain Value | ER Null Model | CFG Null Model | Spatial Null Model |
|---|---|---|---|---|
| Connection probability | 0.000160 | -- | -- | -- |
| Connection reciprocity | 0.138 | < 0.138 | < 0.138 | < 0.138 |
| Clustering coefficient | reported (see Table 2) | lower | lower | lower |

The reciprocity of 0.138 means that among connected neuron pairs, approximately 13.8% are reciprocally connected. This exceeds what would be expected by chance in all three null model types (Erdos-Renyi, configuration model, and spatial null model).

### 2.2 Threshold Sensitivity Analysis

Table S2 compares network statistics at two thresholds:

| Statistic | No threshold | Threshold = 5 synapses/connection |
|---|---|---|
| Number of neurons | 127,978 | 127,978 |
| Number of connections | higher (includes weak connections) | 2,613,129 |

Fig S1b-c confirms that the qualitative observations (SCC size trends, rich club presence) are robust to threshold choice. The giant SCC size as a function of synapse threshold is plotted in Fig S1c.

### 2.3 Edge Percolation

Fig S1a shows the effects of edge percolation on the largest WCC size when large connections are removed first.

Fig S1b shows the same when small connections are removed first.

The network is more vulnerable to removal of strong connections than weak ones, consistent with the importance of high-weight edges for global connectivity.

---

## Experiment 3: Reciprocal Connection Analysis

### 3.1 Reciprocal vs. Unidirectional Edge Strength

| Connection Type | Average Strength |
|---|---|
| Reciprocal edges | Higher (stronger on average) |
| Unidirectional edges | Lower |

Fig 2a demonstrates that edges participating in reciprocal connections are stronger on average than unidirectional connections.

### 3.2 Neurotransmitter Composition of Reciprocal vs. Unidirectional Connections

| Neurotransmitter | Unidirectional Connections | Reciprocal Connections |
|---|---|---|
| Acetylcholine (ach) | Most prevalent | Present but lower fraction |
| GABA | Lower fraction | Over-represented relative to unidirectional |
| Glutamate (glut) | Present | Present |
| Dopamine (da) | Present (low) | Present (low) |
| Octopamine (oct) | Present (low) | Present (low) |
| Serotonin (ser) | Present (low) | Present (low) |

Fig 2b shows that unidirectional connections are most likely to be cholinergic, while reciprocal connections are more likely than unidirectional ones to involve a GABAergic neuron.

### 3.3 Neurotransmitter Pair Frequencies in Reciprocal Connections

Fig 2c compares the frequency of neurotransmitter pairs forming reciprocal connections against expected frequencies. Some pairings are enriched or depleted relative to what random pairing would predict.

### 3.4 Reciprocal Degree Distribution

Fig S3a shows the reciprocal degree distribution alongside in-degree and out-degree distributions.

Fig S3b shows reciprocal degree distributions broken down by neurotransmitter type (glutamate, dopamine, octopamine, serotonin).

Fig S3c is a heatmap showing fraction of reciprocal incoming connections vs. fraction of reciprocal outgoing connections. Dotted lines indicate a factor of 2 around the identity line (x = y).

---

## Experiment 4: Three-Node Motif Analysis

### 4.1 Whole-Brain Motif Census

All 13 possible three-node directed motif types were enumerated across the entire brain.

| Motif ID | Description | Observed Count | Relative to ER Model | Relative to CFG Model |
|---|---|---|---|---|
| #1 | Simple chain (A->B->C) | counted | Under-represented | Under-represented |
| #2 | Simple divergence/convergence | counted | Under-represented | Under-represented |
| #3 | Simple motif variant | counted | Under-represented | Under-represented |
| #4-#8 | Intermediate complexity motifs | counted | Variable | Variable |
| #9 | Feedforward loop | counted | Over-represented | Over-represented |
| #10-#12 | Complex recurrent motifs | counted | Over-represented | Over-represented |
| #13 | Fully connected (all 6 edges) | counted | Over-represented | Over-represented |

Fig 3a presents the complete distribution. The key finding: simple motifs (#1-#3) are under-represented compared to both ER and CFG null models, while complex recurrent motifs (particularly #9, #13) are over-represented. The over-representation of motif #13 (full connectivity among 3 neurons) and #9 (feedforward loop) is consistent with the high reciprocity observed in the 2-node analysis.

### 4.2 Motif Comparison with Other Organisms

The fly brain motif frequencies were compared with wiring diagrams of other animals. The overall pattern of motif enrichment/depletion is broadly consistent with other nervous systems but with quantitative differences in the degree of enrichment for specific motifs.

### 4.3 Motif Strength Analysis

In addition to counting motifs, the strength (synapse count) of connections within each motif type was examined. Motifs involving reciprocal edges tend to have higher average connection weights.

### 4.4 Motif Neurotransmitter Composition

The neurotransmitter composition of neurons participating in each motif type was characterized. Certain motifs show enrichment for particular transmitter combinations.

---

## Experiment 5: Rich Club Analysis

### 5.1 Rich Club Organization

| Metric | Value |
|---|---|
| Rich club fraction of connectome | ~30% of neurons |
| Rich club criterion | Highly connected neurons interconnecting above chance |
| Comparison to ER null model | Rich club coefficient exceeds null |
| Comparison to CFG null model | Rich club coefficient exceeds null |

The fly brain displays rich club organization at synaptic resolution. Approximately 30% of neurons qualify as rich club members -- a much larger fraction than observed in smaller connectomes like C. elegans. The rich club coefficient (normalized against null models) exceeds 1.0 across a range of degree thresholds, confirming that high-degree neurons interconnect more densely than expected by chance.

### 5.2 Rich Club Neuron Subtypes

| Subtype | Definition | Neurotransmitter Profile | Superclass Profile |
|---|---|---|---|
| Broadcasters | High out-degree, low in-degree | Distinct from overall population | Over-representation of specific superclasses |
| Integrators | High in-degree, low out-degree | Distinct from overall population | Over-representation of specific superclasses |
| Large balanced neurons | High in-degree AND high out-degree | Closer to overall distribution | Mixed superclass representation |

Fig 4a shows the division of intrinsic rich club neurons into broadcasters, integrators, and large balanced neurons based on the in-degree vs. out-degree scatterplot.

Fig 4b compares the neurotransmitter prevalence across all intrinsic neurons, rich club neurons, integrators, and broadcasters. There are systematic differences in transmitter composition between these subtypes.

Fig 4c compares the superclass distributions (optic lobe intrinsic, visual projection, visual centrifugal, central brain intrinsic) across the same neuron populations.

Fig 4d provides examples of rich club neurons from each category.

### 5.3 Laterality of Rich Club Subtypes

Fig S4c compares input and output sides (left vs. right hemisphere) of all intrinsic neurons, rich club neurons, integrators, and broadcasters. The asymmetry in L/R percentages for broadcaster neurons is attributed to the large number of medulla-intrinsic broadcasters connecting with photoreceptors.

### 5.4 Additional Rich Club Neuron Populations

The paper identifies several additional populations of interest:

| Population | Description |
|---|---|
| Attractors | Neurons that attract paths in the network |
| Repellers | Neurons that paths tend to avoid |
| NSRNs | Non-self-referencing neurons with distinct connectivity patterns |

These populations are available as interactive lists ("Connectivity Tags") on the FlyWire Codex.

---

## Experiment 6: Neuropil-Specific Network Analysis

### 6.1 Neuropil Subnetwork Construction

78 anatomically defined brain regions (neuropils) were analyzed as separate subnetworks. Each synapse was assigned to a neuropil based on synapse location. With the standard threshold of 5 synapses per edge applied, all connections composed of synapses within a given neuropil were treated as edges of that neuropil's subnetwork.

Fig 5a shows an exploded view of the brain with all 78 neuropil regions.

Fig 5b provides a schematic of how neuropil subnetworks are defined for motif analysis.

### 6.2 Cross-Neuropil Connectivity Variation

Neuropils differ substantially in their internal connectivity properties:

| Property | Variation Across Neuropils |
|---|---|
| Connection strength distribution | Varies -- some neuropils have predominantly weak connections, others have heavier tails |
| Reciprocity | Varies across regions |
| Clustering coefficient | Varies across regions |
| Motif composition | Substantially different profiles across neuropils |

### 6.3 Neuropil Motif Profiles -- Example Regions

Three example neuropils are highlighted in Fig 6a:

| Neuropil | Key Motif Feature |
|---|---|
| Ellipsoid body (EB) | Distinctive motif profile, different from whole-brain average |
| Antennal lobe right (AL(R)) | Distinct motif enrichment pattern |
| Mushroom body medial lobe right (MB-ML(R)) | Distinct motif enrichment pattern |

Each neuropil's motif frequencies were normalized against both ER and CFG null models tailored to that specific subnetwork (matching size, density, and degree sequence).

### 6.4 Comprehensive Neuropil Motif Comparison

Fig 6b shows motif frequencies for all 13 three-node motifs across all 78 neuropil subnetworks, normalized by their respective CFG null models. There is visible heterogeneity: some neuropils cluster together in motif space, suggesting shared organizational principles, while others are outliers.

Fig S8a provides additional neuropil-specific motif distributions beyond the three examples in the main text.

---

## Experiment 7: Null Models Used

### 7.1 Null Model Specifications

| Null Model | Abbreviation | Preserved Properties |
|---|---|---|
| Erdos-Renyi | ER | Same number of nodes and edges; edges placed uniformly at random |
| Configuration model | CFG | Same in-degree and out-degree sequence as real network |
| Spatial null model | spatial | Accounts for spatial positions of neurons |
| Number of CFG instances per comparison | 100 | Violin plots show distribution of 100 CFG realizations |

For each null model, the relevant network statistic (reciprocity, clustering, motif frequency, rich club coefficient) was computed and compared against the observed value in the real connectome.

---

## Experiment 8: Neurotransmitter Assignment Validation

| Parameter | Value |
|---|---|
| Prediction method | Convolutional neural network on EM images |
| Per-synapse accuracy | 87% |
| Number of transmitter classes | 6 |
| Transmitter candidates | Acetylcholine, GABA, Glutamate, Dopamine, Octopamine, Serotonin |
| Assignment rule | Average per-synapse probabilities across all outgoing synapses of a neuron, assign highest-probability transmitter |
| Assumption | Each neuron expresses a single outgoing neurotransmitter (Dale's principle) |

The per-synapse prediction returns a 1x6 probability vector. These are averaged across all outgoing synapses for a given neuron to get a neuron-level 1x6 vector, and the argmax is taken as the putative neurotransmitter identity.

---

## Key Quantitative Findings Summary

| Finding | Numeric Value |
|---|---|
| Total neurons in connectome (v630) | 127,978 |
| Total thresholded connections (v630) | 2,613,129 |
| Total synapses (approximate) | 32,000,000 |
| Synapse threshold | 5 synapses/connection |
| Giant SCC as fraction of all neurons | 93.3% |
| Giant WCC as fraction of all neurons | 98.8% |
| Connection probability (any two neurons) | 0.000160 |
| Connection reciprocity | 0.138 |
| Rich club fraction | ~30% |
| Number of neuropils analyzed | 78 |
| Neurotransmitter prediction accuracy | 87% |
| Number of neurotransmitter classes | 6 |
| Degree at which targeted removal splits SCC | ~50 |
| Number of three-node motif types | 13 |
| Number of CFG null model instances | 100 |
| Total neurons (v783 updated) | 139,255 |
| Total thresholded connections (v783 updated) | 2,701,601 |
| Distance subsample for connectivity analysis | 700 million pairs (5% of ~14 billion) |
| Synapse confidence threshold | 50 |
| Reference count | 93 |

---

## Datasets and Baselines Used

| Resource | Description |
|---|---|
| FlyWire v630 Snapshot | Primary dataset for all analyses |
| FlyWire v783 Snapshot | Updated dataset available at publication time |
| C. elegans connectome | Cross-species comparison for motifs and rich club |
| Other biological wiring diagrams | Used for motif frequency comparisons |
| Hemibrain connectome | Prior partial Drosophila brain dataset; thresholding precedent |
| ER null model | Random graph baseline with matched node/edge count |
| CFG null model (x100) | Degree-preserving random graph baseline |
| Spatial null model | Position-aware random graph baseline |

---

## Metrics Computed

| Metric | Category |
|---|---|
| In-degree, out-degree distributions | Degree statistics |
| Total degree | Degree statistics |
| Reciprocal degree | Degree statistics |
| Connection probability | Global connectivity |
| Connection reciprocity | Global connectivity |
| Clustering coefficient | Global connectivity |
| Shortest path length distribution | Path analysis |
| SCC/WCC sizes and composition | Component analysis |
| Node removal robustness (targeted vs. random) | Robustness |
| Edge percolation curves | Robustness |
| 2-node motif frequencies | Motif analysis |
| 3-node motif frequencies (all 13 types) | Motif analysis |
| Motif Z-scores vs. ER and CFG models | Motif analysis |
| Rich club coefficient vs. degree threshold | Rich club |
| Broadcaster/integrator classification | Rich club subtypes |
| Neuropil-level motif profiles (78 regions) | Regional analysis |
| Neuropil connection strength distributions | Regional analysis |
| Neurotransmitter composition by connection type | Neurotransmitter analysis |
| Neurotransmitter pair frequencies in reciprocal connections | Neurotransmitter analysis |

---

## Figure Observations (Factual Statements)

- **Fig 1b**: The distribution of synapses per connected neuron pair is right-skewed, with most connections having few synapses and a long tail of strong connections.
- **Fig 1c**: In-degree and out-degree are positively correlated on log-log axes, spanning several orders of magnitude.
- **Fig 1d**: Shortest path lengths within the giant SCC form a unimodal distribution peaking at a small number of hops.
- **Fig 1e**: Path lengths in the WCC are similarly compact.
- **Fig 1f**: Targeted high-degree node removal causes the SCC to fragment at approximately degree 50; random removal does not cause this fragmentation until much later.
- **Fig 2a**: Reciprocal edges are stronger on average than unidirectional connections.
- **Fig 2b**: Unidirectional connections are predominantly cholinergic; reciprocal connections show an elevated fraction of GABAergic neurons.
- **Fig 2c**: Certain neurotransmitter pairings in reciprocal connections deviate from expected frequencies.
- **Fig 3a**: Simple 3-node motifs (#1-#3) are under-represented relative to both ER and CFG null models; complex recurrent motifs (especially #9 and #13) are over-represented.
- **Fig 4a**: Rich club neurons partition into broadcasters, integrators, and large balanced neurons in the in-degree vs. out-degree plane.
- **Fig 4b**: Rich club neurons, integrators, and broadcasters each have distinct neurotransmitter profiles compared to all intrinsic neurons.
- **Fig 4c**: Superclass composition differs across rich club subtypes, with specific superclasses enriched in broadcasters vs. integrators.
- **Fig 5a**: The 78 neuropil regions tile the entire brain volume.
- **Fig 5b**: Neuropil subnetworks are constructed by retaining only intra-neuropil connections.
- **Fig 6a**: The EB, AL(R), and MB-ML(R) each display qualitatively distinct motif enrichment profiles.
- **Fig 6b**: Across all 78 neuropils, there is substantial heterogeneity in motif composition, with some neuropils clustering together and others being clear outliers.
- **Fig S1a-b**: The network is more vulnerable to removal of strong connections than weak connections in edge percolation.
- **Fig S1c**: The SCC size is robust to reasonable variation in the synapse threshold.
- **Fig S1d**: Both synapse probability and connection probability decrease with increasing inter-arbor distance.
- **Fig S3a**: Reciprocal degree distribution overlaps with but is distinct from in-degree and out-degree distributions.
- **Fig S4c**: Broadcaster neurons show hemispheric asymmetry in input/output sides due to medulla-intrinsic broadcasters connecting with photoreceptors.

---

## Statistical Comparisons and Tests

- All motif frequencies were compared against 100 independent CFG null model realizations (displayed as violin plots showing the null distribution).
- Rich club coefficient was normalized against both ER and CFG expectations.
- Reciprocity was tested against ER, CFG, and spatial null models; all three produce reciprocity values lower than the observed 0.138.
- Clustering coefficient was similarly compared to null models and found to exceed null expectations.
- Threshold robustness checks confirmed that qualitative conclusions hold across a range of synapse-per-connection thresholds (Fig S1b-c, Table S2).
