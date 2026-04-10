# Experimental Log: Network Statistics of the Whole-Brain Connectome of Drosophila

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- Repeating for all neuron pairs gives us a weighted graph describing the connectome, with 127,978 neurons and 2,613,129 total thresholded connections, representing the complete Drosophila brain (28) (Figure 1a, Methods).
- The synapses in this dataset were detected automatically (31, 32).
- To minimize the impact of spurious synapses, we applied a threshold of 5 synapses per connection for all of the analyses conducted in this study, unless otherwise noted (Methods).
- The exceptions are the distribution of synapses per connection, which is presented without threshold (Figure 1b), and controls to confirm that our qualitative observations are robust to threshold choice (Figure S1b-c, Table S2).
- We will be using synapse count as a proxy for edge strength in this paper: “stronger” and “weaker” will refer to higher or lower synapse counts, respectively.biorxiv;2023.07.29.551086v2/FIG1F1fig1Figure 1.Whole-brain network properties.(a) The FlyWire dataset (27, 28, 30) is an EM reconstruction of 
- The volume contains 127,978 neurons and 32 million synapses with a threshold of 5 synapses/connection applied (subsample of synapse locations shown in the inset).
- In the fly brain there exists one giant SCC containing 93.3% of all neurons after thresholding at 5 synapses per connection.
- In the fly brain there exists one giant WCC containing 98.8% of all neurons.
- (f) We examine the role high-degree neurons play in connecting the brain by plotting the sizes of the first two strongly connected components (SCCs) as nodes are removed by total degree (2500 neurons per step).
- Removal of neurons starting with those with largest degree results in the brain splitting into two SCCs when neurons of approximately degree 50 start to be removed, a deviation from when neurons are removed in a random order (dotted lines).
- (g) Removal of neurons starting with those with smallest degree results in a single giant SCC until all neurons are removed (2500 neurons per step).
- The range over which the relative rich club coefficient is greater than 1.01 is 37 to 93.
- We take all neurons with total degree > 37 to be within the rich club regime.The FlyWire connectome also contains synapse-level neurotransmitter predictions (33).
- Glutamate can be either excitatory or inhibitory, but within the brain of the fly it has largely been observed to be inhibitory (34–36).A key characteristic of the network is the distribution of degrees, which reflects the amount of connectivity between neurons.
- With a threshold of 5 synapses per connection, the average in/out-degree of an intrinsic neuron in the brain is 20.5 (28), but the distributions of in-degree and outdegree are not highly correlated (Pearson R = 0.76, p < 0.001) (Figure 1c).
- On average, each connection in the brain consists of approximately 12.6 synapses after the threshold is applied (28).
- Across the connectome, the probability that any two neurons is connected is 0.000161.
- elegans nervous system or the partial wiring diagrams of brain regions of larval zebrafish and mouse (Table 2).
- Over 71% of connections occur between neuron pairs located within 50 microns of each other, despite these pairs constituting less than 3% of the total number of pairs.
- The longrange sparsity is partially a consequence of the segregation of the neurons of the Drosophila brain into a large number (78) of brain regions (neuropils), and we further investigate connectivity within neuropils below (Figures 5-6, S5-S8).biorxiv;2023.07.29.551086v2/TBL2T2tbl2Table 2.Connect
- Connection reciprocity (the probability that two connected neurons are reciprocally connected) in the fly is 0.138, larger than in either an ER, CFG, or spatial null model (Methods) with the same sparsity.
- The clustering coefficient (the probability that if neuron α and neuron β are connected and neuron α and neuron γ are connected, then neuron β and neuron γ are also connected, irrespective of directionality) in the fly is 0.0463.
- Values for thresholds from 0 to 50 are plotted in Figure S1c.
- elegans were computed for the chemical networks of neurons in hermaphrodite and male worms (19).
- Statistics for larval zebrafish hindbrain (7) and mouse visual cortex (6) were computed excluding any truncated neuronsNeurons in the brain form a single connected componentTo assess the interconnectivity of the neurons in the brain, we searched the connectome for connected components using two sets
- All neurons within an SCC are mutually reachable via directed pathways (37).
- Second, we looked for weakly connected components (WCCs), a relaxed criterion in which all neurons within a WCC are mutually reachable, ignoring the directionality of connections.Despite its sparsity, the brain is highly connected under either criteria – 93.3% of neurons are contained in a single SC
- These giant connected components, which contain the overwhelming majority of neurons in the brain, persist when either the strongest connections or the weakest connections are pruned (Figure S1a-b), indicating that connectivity in the brain is robust: many paths connect neuron pairs.
- Within the giant SCC, the average shortest directed path length between neuron pairs is 4.42 hops, with every neuron reachable within 13 hops (Figure 1d).
- In the giant WCC, the average shortest undirected path length between neuron pairs is 3.91 hops, with every neuron reachable within 11 hops (Figure 1e).
- These numbers are comparable to those found in a similar analysis of the hemibrain dataset (38).
- The short path lengths within both connected components show that despite its size, the fly brain is still relatively shallow when compared to artificial networks (39).Is the high interconnectivity observed in the fly brain a consequence of a relatively large number of interconnected neurons, or is 
- Here, we plot the sizes of the two largest SCCs as we remove neurons from the directed network, starting with those of largest total degree (Figure 1f).
- We find that the first giant SCC persists until a total degree of 50, at which point the network splits into two SCCs of roughly equal size.
- These two SCCs correspond to a split between the left and right hemispheres, and demonstrate that despite the hemispheric anatomy of the brain, the two hemispheres are highly interconnected: they do not split into separate networks until about 60% of all neurons are removed.
- Removing neurons from the network by smallest total degree does not result in division of the first giant connected component (Figure 1g).
- We observe similar behavior in the WCCs when removing neurons from the undirected network (Figure S2a-b).
- These results also remain qualitatively consistent when neurons are pruned in either the directed or undirected network by either in-degree or out-degree alone (Figure S2c-d).The SCC criteria is more biologically realistic, since connections between real neurons are directed.
- In this random walk, the transition probability from neuron α to neuron β is , where  is the out-degree of neuron α, and δα→β ∈ {0, 1} indicates the existence of a connection.
- Such a random walk converges to a stationary distribution over all neurons in the giant SCC (Figure S1f).
- We found that in this random walk, 3% of neurons were visited 61.2% of the time—the remaining 97% of neurons were visited only 38.8% of the time.
- These top visited neurons can therefore be classified as attractor nodes (40) in the network.
- The reversed walk also converges to a stationary distribution in which 3% of neurons were visited 42.4% of the time (Figure S1g).
- This suggests that these neuropils engage in local (rather than integrative) computations.The fly brain has a large rich clubMany networks exhibit the “rich club” property (3, 11, 18), in which well connected nodes are preferentially connected to other well connected nodes (see Methods).
- We find that there exists a rich club regime in the FlyWire connectome, in which neurons are more highly interconnected than one would expect from a randomly connected network (Figure 1h).
- We will take this cutoff to be a total degree of 37, though we note that the exact choice of rich club cutoff is arbitrary (Methods).
- This large rich club regime contains 40,218 neurons, approximately 30% of all neurons in the brain.
- The connection probability within this rich club is 0.000870, 5.4 times higher than the overall connection probability in the brain.
- A rich club analysis considering in-degree alone returns an in-degree threshold of 10, while no rich club is observed when considering out-degree alone (Figure S2e).The fraction of neurons in the rich club regime in the fly is substantially larger in the fly than in C.
- elegans, which has a rich club of 11 neurons (4% of the neurons in the worm) (18).
- Across the whole brain, this connection reciprocity probability is 0.138 (Table 2).
- The over-representation of reciprocal connections in brains relative to null models is well established, and our results are consistent with previous observations both in Drosophila (38, 41, 42) and in other species (2, 6, 19, 22, 23, 43).We also computed the clustering coefficient, a higher-order c
- The clustering coefficient in the brain is 0.0477 (Table 2).
- elegans (2, 19, 44), and with two sub-volume wiring diagrams, the hindbrain of a larval zebrafish (7) and a region of L2/3 mouse visual cortex (6) (Table 2).
- Informed by the distribution of connections as a function of distance, we built a two-zone spatial null model, where the probability of randomly forming a connection between neurons is dependent on the distance between them (Figure S1e) (Methods).
- While the fly and worm datasets represent complete brains and nervous systems, respectively, the zebrafish and mouse datasets are derived from brain sub-volumes, with order 100s of neurons.
- elegans have been proofread to the level of individual synapses (2, 25, 44), it is not feasible to manually proofread every synapse in larger connectomics datasets such as Drosophila.
- Varying the synapse threshold in the fly did not significantly alter reciprocity and clustering coefficient values (Figure S1c, Table S2).Small-worldness of the fly brainA “small-world” network is one in which nodes are highly clustered and path lengths are short (10).
- High small-worldness co-efficients are associated with efficient communication between nodes (45, 46).
- We quantified the small-worldness of the connectome by comparing it to an Erdő s-Rényi (ER) graph (47).
- The average undirected path length in the ER graph, denoted as ℓrand, is estimated to be 3.57 hops, similar to the observed average path length in the fly brain’s WCC (ℓobs = 3.91).
- The clus-tering coefficient () of the ER graph is only 0.0003, much smaller than the observed clustering coefficient () (Table 2, Methods).
- elegans connectome (SΔ = 3.21) and close to that of the internet (SΔ = 98.1) (10), implying highly effective global communication among neurons in the brain.Strength and neurotransmitter composition of reciprocal connectionsThe average strength of edges participating in reciprocal connections is hig
- The majority of unidirectional connections are cholinergic (excitatory), while edges participating in reciprocal connections contain fewer cholinergic neurons and more GABAergic neurons (Figure 2b).
- Inhibitory connections in the brain have more synapses on average than excitatory connections (28), which may partially explain the higher average strength of reciprocal connections.
- The most common reciprocal pairing is between a cholinergic neuron and a GABAergic neuron and the second most common pairing is acetylcholine-glutamate (Figure 2c).
- Both of these reciprocal motifs are excitatory-inhibitory (E-I), and both are over-represented when compared to the neurotrans-mitter frequencies observed for reciprocal connections (Figure 2b).
- We observed reciprocal E-I (acetylcholine-GABA and acetylcholine-glutamate) connection strengths to be only weakly correlated, while E-E (acetylcholine-acetylcholine) pairs were uncorrelated (Figure 2d).
- Examples of reciprocal neuron pairs are shown in Figure 2g.biorxiv;2023.07.29.551086v2/FIG2F2fig2Figure 2.Characterizing reciprocal connections in the brain.(a) Edges that are part of reciprocal connections (reciprocal edges) are stronger on average than unidirectional connections.
- (f) Scatterplot of 2 times the reciprocal degree of neurons versus their total degree (in-degree + out-degree).
- Dotted lines indicate a factor of 2 around the x = y line.
- Cell labels are listed where available.Reciprocal degree across the neuronal populationOf the 127,978 neurons in the whole brain, 77,607 participate in at least one reciprocal connection: approximately 2 in every 3 neurons, even with the synapse threshold we applied (Methods).
- To characterize these neurons, we define the reciprocal degree as the number of reciprocal connections made by a given neuron (Figure S3a).
- Plotting the distributions of reciprocal degree by neurotransmitter, we observe that the overwhelming majority of neurons with high reciprocal degree (drec > 100) are GABAergic (Figures 2e, S3b), while at lower reciprocal degrees (drec < 100), all three primary neurotransmitter types are well repres
- For most neurons these fractions are low—on average 23% of incoming and 18% of outgoing connections are reciprocal.
- Plotting the fraction of reciprocal incoming connections against the fraction of reciprocal outgoing connections, we observe only a weak correlation (Figure S3c), suggesting that a given neuron’s reciprocal degree is not strongly coupled to either its in-degree or its out-degree.
- Comparing the number of reciprocal connections neurons make to the total number of connections they make by plotting 2× the reciprocal degree against the total degree of neurons (in-degree + out-degree), we again see no relationship (Figure 2f).
- Dividing the neuron population by neurotransmitter, however, we find that neurons of high total degree are mostly GABAergic, and that for many of these neurons, more than half of their total connections are reciprocal (Figure S3d).
- Examples of neurons which form reciprocal connections are shown in Figure 2g.Strength and neurotransmitter composition of threenode motifsThe high clustering coefficient of the brain implies an overrepresentation of triplet structures.
- We determined the frequency at which each of the 12 directed three-node motifs occur in the brain (Figure 3a).
- Feedforward motifs (motifs #1-3) are under-represented when compared to both ER and CFG null models, while all others, including the highly recurrent motifs (motifs #7-13), are over-represented.
- The strengths of edges participating in 3-node motifs are higher than the average edge strength (Figure 3b).
- Complex 3-node motifs which contain reciprocal connections tend to be stronger than feedforward motifs.biorxiv;2023.07.29.551086v2/FIG3F3fig3Figure 3.Examining 3-node motifs.(a) The distribution of three-node motifs across the whole brain.
- Absolute counts of each motif are on the left, and the frequency of each motif relative to that in an ER null model is plotted to the right, together with the average motif frequencies of 100 CFG models (gray violin plots).
- When we compare the whole-brain network to both ER and CFG null models, we observe an under-representation of simple motifs (#1-3) and an over-representation of other motifs, particularly highly recurrent motifs (#10, 12, 13).
- (b) The average strength of edges that are part of the 3-node motifs.
- (c) Breakdown by neurotransmitter of edges participating in two motifs: feed-forward loops (motif #4) and 3-unicycles (motif #7).
- (d) Further examining the neurotransmitter composition of these motifs, we find that feed-forward loops (motif #4) are most likely to be acetylcholine-acetylcholine-acetylcholine, (e) while 3-unicycles (motif #7) tend to contain at least one inhibitory edge (glutamate or GABA).
- (f) Visualizations of exemplar 3-node motifs.
- Cell labels are listed where available.Examining the neurotransmitter composition of two of these three-node motifs, feedforward loops (motif #4) and 3-unicycles (motif #7) (Figure 3c), we found that edges which participate in feedforward loops were predominantly cholinergic, and that the most commo
- 3-unicycles in contrast contain a higher proportion of inhibitory GABAergic and glutamatergic neurons, and the three most common 3-unicycle compositions all contain at least one inhibitory neuron (Figure 3e).
- It is interesting to note that the observed neurotransmitter composition frequencies are closer to what may be expected by chance for feedforward loops than they are for 3-unicycles.
- Examples of neurons which form 3-node motifs are shown in Figure 3f.The fly brain exhibits a high clustering coefficient and an over-representation of highly connected 3-neuron motifs.
- elegans (2, 19) and in mouse cortex (6, 22, 23).
- The over-representation of feedforward loops (motif #4) has been widely observed in other biological networks, such as in rat cortex and C.
- 3-unicycles (motif #7) may form recurrent local circuits capable of generating persistent oscillatory neural activity (7).Large-scale connectivity in the brainWithin the adult brain, the in-degree and out-degree of neurons are not tightly correlated.
- To examine these populations of neurons, we divided the intrinsic rich club neuron population into three categories based on their in-degree and out-degree (Figure 4a).
- We divided the rich club neurons by defining broadcaster neurons as those for which out-degree ≥ 5× in-degree, and integrator neurons as those for which in-degree ≥ 5× out-degree.
- In the FlyWire connectome we find 676 broadcasters and 638 integrators.
- The remaining intrinsic rich club neurons (37,093) fall into the balanced category (Region 3), including most highly reciprocal neurons.
- Some examples of broadcasters, integrators, and balanced neurons are shown in Figure 4d.biorxiv;2023.07.29.551086v2/FIG4F4fig4Figure 4.Large-scale neuron connectivity in the brain.(a) Using the in-degree vs.
- 2021 (28, 48), we determined the percentile rank distributions of rich club, integrator, and broadcaster neuron populations from all inputs to the brain (above), as well as to specific modalities (Figure S4d).
- Across all modalities, rich club neurons are closer than average to sensory inputs.biorxiv;2023.07.29.551086v2/FIG5F5fig5Figure 5.Neuropil-specific differences in connectivity.(a) An exploded view of the brain showing the brain regions, or neuropils, that the FlyWire dataset is divided into.
- With the standard threshold of 5 synapses per edge applied, all connections composed of synapses within the neuropil of interest (Neuropil A) are treated as edges of the Neuropil A subnetwork.
- Refer to Figure S6 for the absolute percentages.
- Examples of such pairs are shown in Figure S7e.When compared to the population of all neurons, rich club neurons are less likely to be cholinergic and more likely to be GABAergic (Figures 4b, S4a).
- Integrator neurons are even less likely to be cholinergic (49%), and include a large fraction of dopaminergic neurons, suggesting that these neurons may be engaged during learning.
- In contrast, broadcaster neurons are predominantly cholinergic (75%).
- Central brain neurons are dramatically over-represented in the rich club, while optic lobe intrinsic neurons are under-represented (Figures 4c, S4b).
- These include a large number of Mi1 and Tm3 neurons, excitatory cells in the medullae (ME) known to play key roles in the motion detection circuit (41, 49, 50).
- Most neurons are restricted to a single hemisphere—just 11% of neurons have inputs in both hemispheres and 11% have outputs in both hemispheres (Figure S4c)(28).
- In comparison, rich club neurons are more likely to have inputs or outputs spanning both hemispheres: 18% and 17%, respectively.
- This is more common for integrator neurons (23%) than it is for broadcaster neurons (16%).Rich club neurons are closer on average to sensory inputsTo assess the distance of the rich club neurons from sensory inputs, we employed a probabilistic information flow model to determine the relative distanc
- Neurons with percentile rank less than 50% are closer than average to the given sensory input, while neurons with percentile rank greater than 50% are farther.The rich club neurons have a mean percentile rank of 44% relative to the set of all sensory inputs (Figure 4e).
- Integrators have a mean percentile rank of 43%, while broadcasters have a mean percentile rank of 53%.
- Integrator neurons are closest, with many having a percentile rank of less than 10%.
- Examining the ranks with respect to individual sensory modalities, we find that rich club neurons are again closer than average to each modality (Figures 4f, S4d).
- In contrast, when looking at a single modality, neurons which are predominantly connected to a different modality will be farther than average.We examine the distance of neurons to multiple sensory modalities by plotting the percentile rank of neurons with respect to one modality against the percent
- In particular, integrator and broadcaster neurons which are low in rank relative to multiple sensory modalities may be good candidate sites of multi-sensory integration and information propagation.Differences in connectivity across brain regionsThe fly brain consists of a large number of distinct an
- The FlyWire connectome has been segmented into 78 neuropils (Figure 5a), each with different average connection strengths (28).
- To understand information flow between neuropils, we employed a fractional weighting method accounting for each neuron’s projections to and from every neuropil (Methods)(28).
- From these, we computed for each neuropil the relative fraction of internal, external incoming, and external outgoing connection weights (Figure S5a-b).
- These fractions reflect, respectively, the net number of connections within, being received, and being sent from each neuropil.We find significant differences in these fractions across brain regions: the ellipsoid body (EB) and fan-shaped body (FB) of the central complex have the highest fraction of
- This likely accounts for the high fraction of internal weights in regions such as the medullae (ME), which receive inputs from R7 and R8 photoreceptors, and the gnathal ganglia (GNG), which connects with large numbers of both ascending and descending neurons.
- Across the brain, 52% of all connection weights can be classified as internal.
- Comparing the putative neurotransmitters of the neurons contributing connection weights, we see that internal connections are more likely than external ones to be inhibitory (GABAergic or glutamatergic) (Figure S5c).
- We also see differences in neurotransmitter composition across brain regions (Figure S5d).Prevalence and neurotransmitter composition of reciprocal connections differ across neuropilsTo perform motif analyses within each neuropil, we first identified a subnetwork for each neuropil which treats all c
- Different neuropil subnetworks differ notably in both connection strength and density (Figure S6b).
- We computed the reciprocity in each neuropil subnetwork (Figures 5c, S6c).
- The relative number of reciprocal connections (reciprocity normalized by neuropil connection density) is high in the mushroom bodies (MB) and medullae (ME) (Figure S6b).
- Note that for these motif analyses, the results for small neuropils such as the cantles (CAN), bulbs (BU), galls (GA), accessory medullae (AME), and ocellar ganglion (OCG) are less interpretable due to the small number of samples.In most neuropils, as in the whole brain, reciprocal connections are s
- Comparing the relative prevalence of each neurotransmitter in reciprocal and unidirectional connections, we again see differences between neuropils (Figures 5d-e, S6d-h).
- Comparing the strengths of the edges of reciprocal excitatory-inhibitory (acetylcholine-GABA) connections within neuropil subnetworks, we observe that E-I connection strengths are more strongly correlated in some neuropils (such as the FB and NO) than in others (Figures 5f, S7a-b).
- These correlations do not appear to be dependent on neuropil size (Figure S7c).Identifying neuropil-specific reciprocal neuronsWe performed a comprehensive search for intrinsic highly reciprocal rich club neurons that make the majority of their connections within a single neuropil, and found 1,863 n
- These neuropil-specific highly reciprocal neurons (NSRNs) are predominantly inhibitory: 54% are GABAergic and another 10% are gluta-matergic (Figure S7d).
- In some neuropils, such as the antennal lobes (AL), medullae (MB), and ellipsoid body (EB), there are many NSRNs, while in other neuropils, such as the superior posterior slopes (SPS) and posteriorlateral protocerebra (PLP), there exist only a handful of such neurons.Some NSRNs, like the APL neurons
- Some have been shown to have compartmentalized activity, raising the possibility of local computation within these neurons (58–60).
- They may play similar roles in other circuits— for instance, it is likely that some of the NSRNs found in the AVLP provide feedback to the auditory circuits which span this brain region (61).Identifying inter-neuropil reciprocal connectionsWhile many reciprocal connections occur within single neurop
- We mapped the reciprocal connections that exist between the 78 neuropils (Figure 5h).
- The diagonal terms consist of the intra-neuropil reciprocal connections described above (Figure 5b-c), while the off-diagonal terms reflect the number of reciprocal pairs which connect across neuropils.
- Examples of such neuron pairs are shown in Figure S7e.From the map, we see that reciprocal connections exist between many neuropil pairs.
- The prevalence of such inter-neuropil reciprocal connections demonstrates that the recurrent motifs we observe in the brain are not limited to local connections—they can also exist at large spatial scales.Additional insight can be gleaned by comparing the map of reciprocal connections to the project
- Similarly, the LA boasts many neurons but very few reciprocal connections.Examining ach-gaba reciprocal connections, we can identify deviations from symmetry that represent a net imbalance of excitatory-inhibitory reciprocal connections (Figure S7f).
- For example, between the LO and PVLP, all ach-gaba reciprocal connections share the same directionality: the ach connections are in the LO and the gaba connections are in the PVLP.Three-node motifs differ across neuropils in their prevalence and strengthWe computed the prevalence of three-node motif
- Across most neuropils, we observed the same trend as we do across the entire brain: an under-representation of feedforward motifs (#1-3) and an overrepresentation of complex motifs (Figure 6b).
- In the cantles (CAN), epaulettes (EPA), and gorgets (GOR), for example, the frequency of 3-node motifs was closer to that expected in a CFG null model, while in other neuropils like the ellipsoid body (EB), complex motifs are highly over-represented (Figure 6b).biorxiv;2023.07.29.551086v2/FIG6F6fig6
- The frequency of each motif relative to that in an ER null model is plotted to the right, together with the average motif frequencies of 100 CFG models (gray violin plots).
- Further examples of other neuropils available in Figure S8a.
- (b) Motif frequencies for the 3-node motifs across all 78 neuropil subnetworks, normalized by their respective CFG null models.
- (c) Average strengths of edges participating in 3-node motifs in the different neuropil subnetworks relative to the average 3-node motif strength in each subnetwork.
- Refer to Figure S8b for average strengths relative to average neuropil subnetwork edge strength.Feedforward loops (motif #4) are over-represented in most neuropils, excepting in the fan-shaped body (FB), ellipsoid body (EB), noduli (NO), and mushroom body compartments (MB).
- 3-unicycles (motif #7), an indirect feed-back inhibition circuit, are over-represented across the whole brain (Figure 3c) but are under-represented in most neuropils.
- The over-representation of 3-unicycles in the ME implies the existence of localized cyclic structures within the early visual circuitry.
- Interestingly, this motif is also over-represented in the zebrafish oculomotor circuit (7).
- Motifs #7-10 are underrepresented in the antennal lobes (AL), perhaps a result of the small number of unidirectional edges in these regions.
- The most highly connected motifs (#12-13) are particularly over-represented in the ellipsoid body (EB) and fan-shaped body (FB), consistent with their high reciprocity.In most neuropils, we find that edges participating in under-represented motifs are also weaker on average than edges participating 
- We also observe that in most neuropil subnetworks, edges participating in 3-node motifs are stronger than the average subnetwork edge (Figure S8b).
- This is broadly consistent with the whole-brain 3-node motif strength results.

## Tables

### Table 1.
> Data availability.List of data products in this work, including statistics computed in this paper (left) and neuron populations (right). Complete, interactive neuron lists are available online as “Con


### Table 2.
> Connection probabilities, reciprocity, and clustering coefficient in the fly brain.The probability that any two neurons in the fly brain are connected is 0.000160. Connection reciprocity (the probabil


### Table S1.
> Supplement for Table 1.Definitions for all neuron populations identified in this paper.


### Table S2.
> Supplement for Table 2.Network statistics of the fly connectome with no threshold on the number of synapses per connection (left) and a threshold of 5 synapses per connection.


## Figure Descriptions

### Figure 1.
Whole-brain network properties.(a) The FlyWire dataset (27, 28, 30) is an EM reconstruction of the complete brain of an adult female Drosophila melanogaster, with both hemispheres of the brain and both optic lobes. The volume contains 127,978 neurons and 32 million synapses with a threshold of 5 syn

### Figure 2.
Characterizing reciprocal connections in the brain.(a) Edges that are part of reciprocal connections (reciprocal edges) are stronger on average than unidirectional connections. (b) Breakdown of unidirectional and reciprocal edges by neurotransmitter. Unidirectional connections are most likely to be 

### Figure 3.
Examining 3-node motifs.(a) The distribution of three-node motifs across the whole brain. Absolute counts of each motif are on the left, and the frequency of each motif relative to that in an ER null model is plotted to the right, together with the average motif frequencies of 100 CFG models (gray v

### Figure 4.
Large-scale neuron connectivity in the brain.(a) Using the in-degree vs. out-degree scatterplot, we can divide the intrinsic rich club neurons into three distinct categories: broadcasters, integrators, and large balanced neurons. Comparing the prevalence of (b) neurotransmitters and (c) intrinsic su

### Figure 5.
Neuropil-specific differences in connectivity.(a) An exploded view of the brain showing the brain regions, or neuropils, that the FlyWire dataset is divided into. Each synapse is assigned to a neuropil based on synapse location. (b) A schematic showing how neuropil subnetworks are identified for mot

### Figure 6.
Differences in three-node motifs across neuropils.(a) Three-node motif distributions for three example neuropils: the EB, AL(R), and MB-ML(R). The frequency of each motif relative to that in an ER null model is plotted to the right, together with the average motif frequencies of 100 CFG models (gray

### Figure S1.
Supplement for Figure 1.The effects of edge percolation on the size of the largest WCC when (a) large connections are removed first and when (b) small connections are removed first. (c) The sizes of the first two SCCs as a function of the synapse threshold. (d) Synapse probability (left) and connect

### Figure S2.
Additional supplement for Figure 1.(a) The sizes of the first two weakly connected components (WCCs) as nodes are removed by total degree (1 neuron per step). Removal of neurons starting with those with largest degree results in the brain splitting into two WCCs when neurons of approximately degree 

### Figure S3.
Supplement for Figure 2.(a) Distribution of reciprocal degree (gray) alongside distributions of in-degree (red) and out-degree (blue). (b) Distributions of reciprocal degree for glut, da, oct, and ser neurons. (c) Heatmap showing the fraction of reciprocal incoming connections versus the fraction of

### Figure S4.
Supplement for Figure 4.In-degree vs. out-degree scatterplots showing broadcaster, rich balanced, and integrator regimes, with neurons plotted by (a) the putative neurotransmitter of each neuron and (b) the superclass of each neuron. (c) Comparing the input and output sides of all intrinsic neurons,

### Figure S5.
Internal and external connections across neuropils.(a) The number and (b) relative fraction of neuron weights in each neuropil making connections internal to that neuropil, external incoming connections, and external outgoing connections. Each neuron contributes a total weight of 1, computed based o

### Figure S6.
Supplement for Figure 5.(a) The number of neurons included in each neuropil subnetwork. (b) The average connection strength (no synapse threshold applied) of connections made in each neuropil (above), and the connection probability of each neuropil (below). (c) Reciprocity normalized by connection d

### Figure S7.
Additional supplement for Figure 5.(a) Heatmaps showing the relationship between excitatory (ach) and inhibitory (GABA) connection strengths in reciprocal connections in different brain regions. (b) Ach-gaba reciprocal connection strength correlations (Pearson r-score) for all neuropils. (c) These c

### Figure S8.
Supplement for Figure 6.(a) Three-node motif distributions for additional neuropils. The frequency of each motif relative to that in an ER null model is plotted to the right, together with the average motif frequencies of 100 CFG models (gray violin plots). (b) Average strengths of edges participati

## References
Total references in published paper: 93

### Key References (from published paper)
- The human connectome: A structural description of the human brain (, 2005)
- Structural properties of the Caenorhabditis elegans neuronal network (, 2011)
- Rich-club organization of the human connectome (, 2011)
- Rich-club in the brain’s macrostructure: Insights from graph theoretical analysis (, 2020)
- The impact of neuron morphology on cortical network architecture (, 2022)
- Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity (, 2022)
- Cyclic structure with cellular precision in a vertebrate sensorimotor neural circuit (, 2023)
- Explorability and the origin of network sparsity in living systems (, 2017)
- Efficient behavior of small-world networks (, 2001)
- Network ‘small-world-ness’: a quantitative method for determining canonical network equivalence (, 2008)
- Detecting rich-club ordering in complex networks (, 2006)
- Mapping putative hubs in human, chimpanzee (pan troglodytes) and rhesus macaque (macaca mulatta) con (, 2013)
- Fulcher. Structural connectome topology relates to regional bold signal dynamics in the mouse brain (, 2017)
- Van Den Heuvel. Rich-club neurocircuitry: function, evolution, and vulnerability (, 2018)
- The human connectome project: A retrospective (, 2021)
- Connectomics-based analysis of information flow in the drosophila brain (, 2015)
- Optimized connectome architecture for sensory-motor integration (, 2017)
- Bullmore. The rich club of the c. elegans neuronal connectome (, 2013)
- Whole-animal connectomes of both caenorhabditis elegans sexes (, 2019)
- Network motifs: Simple building blocks of complex networks (, 2002)
- Motifs in brain networks (, 2004)
- Highly nonrandom features of synaptic connectivity in local cortical circuits (, 2005)
- A synaptic organizing principle for cortical neuronal groups (, 2011)
- The connectome of an insect brain (, 2023)
- Connectomes across development reveal principles of brain maturation (, 2021)
- Feedback loops and reciprocal regulation: recurring motifs in the systems biology of the cell cycle (, 2013)
- Flywire: Online community for whole-brain connectomics (, 2022)
- Neuronal wiring diagram of an adult brain (, 2023)
- A consensus cell type atlas from multiple connectomes reveals principles of circuit stereotypy and v (, 2023)
- A complete electron microscopy volume of the brain of adult drosophila melanogaster (, 2018)

## Ground Truth Reference
- Figures: 14
- Tables: 4
- References: 93