# Idea Summary: Network Statistics of the Whole-Brain Connectome of Drosophila

## Working title
Network Statistics of the Whole-Brain Connectome of Drosophila

## Core question
AbstractBrains comprise complex networks of neurons and connections. Network analysis applied to the wiring diagrams of brains can offer insights into how brains support computations and regulate information flow. The completion of the first whole-brain connectome of an adult Drosophila, the largest connectome to date, containing 130,000 neurons and millions of connections, offers an unprecedented opportunity to analyze its network properties and topological features. To gain insights into local

## Motivation / gap
- IntroductionMathematical network theory has been applied to connectomes at multiple scales (from detailed synaptic-resolution wiring diagrams to putative connectivity between brain regions) to underst
- Network analyses quantify the interconnectivity and robustness of a network(8–10), and can identify highly connected nodes in the brain that may act as hubs (11).
- Such analyses can also serve as a basis for comparison across brain regions, individuals, developmental stages, or species, enabling researchers to uncover commonalities and differences in brain organ
- Rich club organization has been observed in several mesoscale connectomes, including Drosophila (16, 17), humans, and other mammals (3, 4, 14).
- It has been suggested that such a network architecture contributes to the ability of brains to efficiently integrate and disseminate information.Advancements in electron microscopy and dense volumetri

## Core contribution (bullet form)
Extracted from abstract:
AbstractBrains comprise complex networks of neurons and connections. Network analysis applied to the wiring diagrams of brains can offer insights into how brains support computations and regulate information flow. The completion of the first whole-brain connectome of an adult Drosophila, the largest connectome to date, containing 130,000 neurons and millions of connections, offers an unprecedented opportunity to analyze its network properties and topological features. To gain insights into local connectivity, we computed the prevalence of two- and three-node network motifs, examined their strengths and neurotransmitter compositions, and compared these topological metrics with wiring diagrams of other animals. We discovered that the network of the fly brain displays rich club organization, with a large population (30% percent of the connectome) of highly connected neurons. We identified subsets of rich club neurons that may serve as integrators or broadcasters of signals. Finally, we examined subnetworks based on 78 anatomically defined brain regions or neuropils. These data products are shared within the FlyWire Codex and will serve as a foundation for models and experiments exploring the relationship between neural activity and anatomical structure.

## Method in brief
MethodsDatasetThe FlyWire connectome is the reconstruction of a 7-day-old adult female Drosophila melanogaster, genotype [iso] w1118 x [iso] Canton-S G1 (30). The EM images were aligned and neurons were automatically reconstructed using deep learning and computer vision methods, then proofread by the community (27, 28). Neuron cell types and community labels were also attached to these data (29, 91). All analyses presented in this paper were performed on the v630 Snapshot of the Fly-Wire dataset. The v630 snapshot contains 127,978 neurons and 2,613,129 thresholded connections, the central brain of the fly was fully proofread, with the optic lobes ∼80% complete. Most of the neurons missing from the v630 Snapshot were photoreceptors, and we do not expect that the addition of these neurons would significantly change our whole-brain network results. At time of publication, the most up-to-date version of the FlyWire dataset is the v783 Snapshot, containing 139,255 neurons, 2,701,601 thresholded connections, and completed optic lobes. Both data snapshots are available at Codex (Connectome Data Explorer): codex.flywire.ai.Synaptic connections and thresholdingSynapses were detected algorithmically (31, 32), with each synapse receiving a confidence score. We then removed synapses if (1) either the pre- or postsynaptic location of the synapse was not assigned to a segment, or (2) the synapse had a confidence score of less than 50. We then set a threshold of 5 synapses per connection be

## Target venue
Nature
