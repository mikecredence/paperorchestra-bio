# Experimental Log: A Synergistic Workspace for Human Consciousness Revealed by Integrated Information Decomposition

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- Theoretical work in cognitive science 26 and the field of distributed signal processing 54,55 has long recognised the computational benefits of combining multiple distinct processing streams.
- However, having a single source of inputs to and outputs from the workspace introduces what is known as a “single point of failure,” which can lead to catastrophic failure in case of damage or malfunction 56.
- Therefore, a natural solution is to have not a single but multiple units dedicated to gathering and broadcasting information, respectively, thereby forming a workspace that can be in charge of synthesising the results of peripheral processing 57.Pertaining to Stage (ii), we previously identified whi
- Here, we consider the architecture of the global workspace more broadly, and combine Integrated Information Decomposition with graph-theoretical principles to bring insights about processing stages (i) and (iii) (Figure 1).
- We term this proposal the “Synergy-Φ-Redundancy” neurocognitive architecture (SAPHIRE) (Figure 1).biorxiv;2020.11.25.398081v5/FIG1F1fig1Figure 1.Schematic of the proposed SAPHIRE neurocognitive architecture.Below, specialised modules characterised by robust redundant functional interactions process 
- Thus, we postulate that regions that mediate the access to the synergistic workspace are functionally connected with multiple modules within networks of synergistic interactions, synthesising incoming inputs from diverse sources 58,59.
- We refer to such regions as gateways (Figure 1, violet nodes).
- These regions are designated as broadcasters (Figure 1, orange nodes).One approach to operationalise these ideas is by leveraging well-established graph-theoretical tools.
- Here, we propose to assess the diversity of intermodular functional connections using the participation coefficient 60 which captures to what extent a given node connects to many modules beyond its own (Materials and Methods).
- 50); the participation coefficient instead quantifies the diversity of modules that a region is connected to.
- Conversely, broadcasters are global workspace regions (i.e., also having high synergy) that have a highly-ranked participation coefficient rank for redundant interactions.In other words, we identify the synergistic workspace as regions where synergy predominates, which as our previous research has s
- Thus, a broadcaster is a region in the synergistic workspace (i.e., a region with strong synergistic interactions) that in addition has a high participation coefficient for its redundant interactions.To explore these hypotheses, we quantified synergistic and redundant interactions between 454 cortic
- In particular, following our previous work 50 we focused on the persistent synergy (henceforth simply synergy) and persistent redundancy (henceforth simply redundancy), which correspond to the information that is always carried synergistically (respectively, redundantly) by X and Y.We then subdivide
- Based on this partition into modules, we identified gateways and broadcasters by comparing the participation coefficients of synergistic versus redundant interactions, for brain regions belonging to the synergistic workspace previously identified (we show a significant correlation for participation 
- In contrast, broadcasters are mainly located in the executive control network, especially lateral prefrontal cortex (Figure 2B, orange).
- Remarkably, the latter results are in line with Global Neuronal Workspace Theory, which consistently identifies lateral prefrontal cortex as a major broadcaster of information 24,66.biorxiv;2020.11.25.398081v5/FIG2F2fig2Figure 2.Gateways and broadcaster regions identified by their network connectivi
- (C) Regions are identified as gateways (violet) or broadcasters (orange) based on the difference between rank of participation coefficient for synergy and redundancy, (only shown for brain regions identified as belonging to the synergistic global workspace, as per Luppi et al., 2022).
- Sub, subcortical network (comprised of 54 regions of the Tian 2020 atlas 64).
- These results were also replicated using an alternative parcellation with 232 cortical and subcortical nodes (Figure S3).Information decomposition identifies a synergistic core supporting human consciousnessHaving introduced a taxonomy within the synergistic global workspace based on the distinct in
- Furthermore, we also reasoned that any brain regions that are specifically involved in supporting consciousness should “track” the presence of consciousness: the reductions should occur regardless of how loss of consciousness came about, and they should be restored when consciousness is regained.We 
- Resting-state fMRI data were parcellated into 400 cortical regions from the Schaefer atlas, and 54 subcortical brain regions from the Tian atlas (same parcellation as for the previous analysis).
- Building on the IIT literature, which provides a formal definition of integrated information, we assessed integration corresponding to conscious activity via two alternative metrics: the well-known whole-minus-sum Φ measure introduced by Balduzzi and Tononi 31, and the “revised Φ” (ΦR) measure recen
- Being demonstrably non-negative, this revised measure overcomes a major conceptual limitation of the original formulation of integrated information 49.biorxiv;2020.11.25.398081v5/FIG3F3fig3Figure 3.Integrated information decomposition.Integrated information decomposition identifies how two sources X
- This shortcoming can be corrected with the revised measure of Φ, termed ΦR.For each subject, we computed the integrated information between each pair of BOLD signal timeseries, resulting in a 454-by-454 matrix of integrated information between brain regions.
- Treating this matrix as an (undirected) network enabled us to study consciousness-related changes in integrated information across conditions, which were analysed using the Network Based Statistic correction for multiple comparisons 67.
- Importantly, since we are interested in changes that are shared between the DOC and propofol datasets, we computed edge-level statistics using a composite null hypothesis test designed to detect such shared effects (Materials and Methods).Analysis based on ΦR revealed a widespread reorganisation of 
- Likewise, propofol anaesthesia was also characterised by significant changes in integrated information between brain regions, both when compared with pre-anaesthetic wakefulness (p < 0.001; Figure 4B) and post-anaesthetic recovery (p < 0.001; Figure 4C).biorxiv;2020.11.25.398081v5/FIG4F4fig4Figure 4
- (D) Overlaps between the three contrasts in (A-C), showing increases and decreases that are common across anaesthesia and disorders of consciousness.Our analysis identified a number of the ΦR connections that were reduced when consciousness was lost due to both anaesthesia and brain injury, and were
- Remarkably, almost all regions showing consistent decreases in ΦR when consciousness was lost were members of the global synergistic workspace, and specifically located in the default mode network (bilateral precuneus and medial prefrontal cortex) - and bilateral inferior parietal cortex – although 
- Additionally, some connections exhibited increases in ΦR during loss of consciousness, and were restored upon recovery (Figure 4D), including areas in frontal cortex - especially lateral prefrontal cortex.
- Nevertheless, the overall balance was in favour of reduced integrated information: sum of F-scores associated with significant edges = −25.37 (Figure S4).These results were in contrast with the analysis based on the original formulation of Φ introduced by Balduzzi and Tononi 31, which did not identi
- Since IIT predicts that loss of consciousness corresponds to reductions in integrated information, we focused on regions exhibiting reliable reductions in ΦR when consciousness is lost (whether due to anaesthesia or DOC), which were restored upon recovery (shown in blue in Figure 4D).Remarkably, our
- Indeed, all reductions occur specifically within the default mode network (Figure 5B).
- Thus, these results suggest that loss of consciousness across anaesthesia and disorders of consciousness would correspond to anterior-posterior disconnection - in terms of integrated information - between DMN nodes that act as gateways into the synergistic workspace.biorxiv;2020.11.25.398081v5/FIG5F
- Sub, subcortical network (comprised of 54 regions of the Tian 2020 atlas).Robustness and sensitivity analysisTo ensure the robustness of our results to analytic choices, we also replicated them using an alternative cortical parcellation of lower dimensionality: we used the Schaefer scale-200 cortica
- Additionally, we also show that our results are not dependent on the choice of parameters in the NBS analysis, and are replicated using an alternative threshold definition for the connected component (extent rather than intensity) or a more stringent value for the cluster threshold (F > 12) (Figure 

## Figure Descriptions

### Figure 1.
Schematic of the proposed SAPHIRE neurocognitive architecture.Below, specialised modules characterised by robust redundant functional interactions process information about the environment. Information is then collected by workspace gateways through synergistic interactions [Stage (i)]; synergistic 

### Figure 2.
Gateways and broadcaster regions identified by their network connectivity profiles.(A) Group-average matrix of synergistic interactions between regions of the 454-ROI augmented Schaefer atlas. (B) Group-average matrix of redundant interactions. For ease of visualization, the colorscale in (B) pertai

### Figure 3.
Integrated information decomposition.Integrated information decomposition identifies how two sources X and Y jointly convey information across time, corresponding to all possible 4×4 combinations of redundancy, unique information (of X and of Y), and synergistic information. This decomposition highl

### Figure 4.
Loss of consciousness induces similar reorganisation of cortical integrated information across anaesthesia and disorders of consciousness.Top: Brain regions exhibiting overall NBS-corrected increases (red) and decreases (blue) in integrated information exchange when consciousness is lost. (A) DOC pa

### Figure 5.
Synergistic core of human consciousness.(A) Surface representations of medial and lateral views of the brain (L indicates left, R indicates right). Colours indicate brain regions that belong to the synergistic workspace, as identified from HCP data. Orange indicates broadcasters, and violet indicate

## References
Total references in published paper: 201

### Key References (from published paper)
- The brainweb: Phase synchronization and large-scale integration (, 2001)
- Brain Networks and Cognitive Architectures (, 2015)
- Neuromodulatory Influences on Integration and Segregation in the Brain (, 2019)
- Précis of The Modularity of Mind (, 1985)
- Revisiting the global workspace: Orchestration of the functional hierarchical organisation of the hu (, 2021)
- A Domain-General Cognitive Core Defined in Multimodally Parcellated Human Cortex (, 2020)
- Human cognition involves the dynamic integration of neural activity and neuromodulatory systems (, 2019)
- Mapping the structural core of human cerebral cortex (, 2008)
- Distributed hierarchical processing in the primate cerebral cortex (, 1991)
- The natural axis of transmitter receptor distribution in the human cerebral cortex (, 2021)
- Neurodevelopment of the association cortices: Patterns, mechanisms, and implications for psychopatho (, 2021)
- Development of structure–function coupling in human brain networks during youth (, 2020)
- The diverse club (, 2017)
- Gradients of structure– function tethering across neocortex (, 2019)
- Situating the default-mode network along a principal gradient of macroscale cortical organization (, 2016)
- Hierarchy of transcriptomic specialization across human cortex captured by structural neuroimaging t (, 2018)
- Hierarchical Heterogeneity across Human Cortex Shapes Large-Scale Neural Dynamics (, 2019)
- Dynamical consequences of regional heterogeneity in the brain’s transcriptional landscape (, 2021)
- Mapping gene transcription and neurocognition across human neocortex (, 2021)
- Mapping neurotransmitter systems to the structural and functional organization of the human neocorte (, 2022)
- Integrated information theory: From consciousness to its physical substrate (, 2016)
- Theories of consciousness (, 2022)
- Experimental and Theoretical Approaches to Conscious Processing (, 2011)
- Conscious Processing and the Global Neuronal Workspace Hypothesis (, 2020)
- The global neuronal workspace model of conscious access: From neuronal architectures to clinical app (, 2011)
- Global workspace theory of consciousness: Toward a cognitive neuroscience of human experience (, 2005)
- Towards a cognitive neuroscience of consciousness: Basic evidence and a workspace framework (, 2001)
- Consciousness as Integrated Information (, 2008)
- An information integration theory of consciousness (, 2004)
- Complexity and coherency: Integrating information in the brain (, 1998)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 201