# Experimental Log: Distinguishing examples while building concepts in hippocampal and artificial networks

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsMF encodings remain distinct while PP encodings build concepts in our model for CA3We model how representations of memories are transformed along the two pathways from EC to CA3 and then how the resultant encodings are stored and retrieved in CA3.
- First, we focus on the transformations between memories and their CA3 encodings.
- The sensory inputs whose encodings serve as memories in our model are FashionMNIST images (Xiao et al., 2017), each of which is an example belonging to one of three concepts: sneakers, trousers, and coats (Fig.
- They are converted to neural activity patterns along each projection from EC to CA3 (Fig.
- Our neurons are binary with activity values of 0 or 1.
- Only 10% of the neurons are allowed to be active, so the representation is sparse, and there are more EC neurons than image pixels, so the representation is overcomplete; sparse, overcomplete encoding models and autoencoder neural networks are common unsupervised models for natural image processing 
- Decoding pathways are used to visualize CA3 activity and are not intended to have biological significance.
- (D) From EC to CA3, we use random binary connectivity matrices to transform each presynaptic pattern  to a postsynaptic pattern .
- Points indicate means and bars indicate standard deviations over 8 random connectivity matrices.
- (F) To visualize CA3 encodings, we pass them through a feedforward network trained to produce the corresponding  for each  and .
- 2D), i.e., from EC to DG, from DG to CA3 via MF, and from EC to CA3 via PP.
- That is, the postsynaptic neurons receiving the largest inputs are set to 1 and the others are set to 0.
- At CA3, two encodings for each image converge:  with density 0.02 and  with density 0.2.
- Not only are MF patterns sparser, they are less correlated with average correlation 0.01, compared to a corresponding value of 0.09 for PP patterns.
- Such an association between sparsification and decorrelation has been widely reported across many theoretical models and brain regions (O’Reilly and McClelland, 1994; Vinje and Gallant, 2000; Pitkow and Meister, 2012; Cayco-Gajic et al., 2017), and it is also captured by our model.
- We contribute further insight by deriving an explicit mathematical formula that connects densities and correlations of patterns in presynaptic and postsynaptic networks:



and erfc−1 is the inverse complementary error function.
- Equation 1 is remarkable in that only these four quantities are involved, revealing that at least in some classes of feedforward networks, other parameters such as network sizes, synaptic density, and absolute threshold values do not contribute to decorrelation.
- S2B, C.Ultimately, the encoding pathways in Fig.
- 2C–E provide CA3 with a sparse, decorrelated  and a dense, correlated  for each memory, in accordance with our biological understanding (Fig.
- Next, we aim to store these patterns in an autoassociative model of CA3.
- Before doing so, we develop visualization pathways that decode CA3 representations back into images, so memory retrieval can be intuitively evaluated.
- 2C to recover the image encoded by CA3.
- These decoding pathways are for visualization only and are not designed to mimic biology, although there may be parallels with the neocortical output pathway from CA3 to CA1 and deep layers of EC (Amaral and Pierre, 2006).
- The neuroanatomical connectivity of CA1 is more complex and includes temporoammonic inputs from EC as well as strong secondary outputs through the subiculum, which also reciprocally connects with EC.Now, we model memory storage in the CA3 autoassociative network.
- For each example ν in concept μ, its MF encoding  arrives at the proximal dendrites and its PP encoding  arrives at the distal dentrites of CA3 pyramidal cells (Fig.
- The relative strength of PP inputs is weaker because PP synapses are located more distally and are observed to be much weaker than MF synapses, which are even called detonator synapses (Amaral and Pierre, 2006; Henze et al., 2002; Vyleta et al., 2016).
- The inputs are linearly summed and stored in a Hopfield-like network (Hopfield, 1982), with connectivity



where i and j are respectively postsynaptic and presynaptic neurons.
- Equation 2 captures the most crucial terms in Wij; see Methods for the full expression.
- While we assume linear summation between  and  for simplicity, integration of inputs across CA3 dendritic compartments is known to be nonlinear (Kim et al., 2012; Makara and Magee, 2013; Kaifosh and Losonczy, 2016).
- Moreover, sublinear summation can also arise from a temporal offset between MF and PP inputs, in which case changes in synaptic weights across pathways could be weaker than those within the same pathway according to spike-timing-dependent plasticity (Bi and Poo, 1998; Mishra et al., 2016).
- S3F, we show that network behavior can be maintained when nonlinearity is introduced.biorxiv;2023.02.21.529365v3/FIG3F3fig3Figure 3:We model CA3 to store both MF and PP encodings of the same memories; MF examples remain distinct while PP examples build concept representations.
- (A–C) Overview of the Hopfield-like model for CA3.
- In all networks, up to 30 cues are tested.
- MF patterns have density 0.01 and correlation 0.
- (I) Similar to H, but overlaying capacities for MF examples and PP concepts to highlight the existence of regimes in which both can be recovered.In previous models, CA3 would retrieve only MF encodings, only PP encodings, or only the activity common between MF–PP pairs (Treves and Rolls, 1992; McCle
- During retrieval, the network is asynchronously updated via Glauber dynamics (Amit et al., 1985).
- 3C determines the softness of the threshold.
- See Methods for the full expression of this update rule.The threshold θ represents the general inhibitory tone of CA3 and plays a key role in retrieval.
- Because our neurons are binary, active neurons in either the MF or the PP encoding would have the same activity level of 1, even though their connectivity strengths differ.
- Thus, we expect the network to approximately retrieve the PP encoding at low θ.Figure 3D–G illustrates the central behavior of our CA3 model; see Fig.
- S3A, B for trouser and coat visualizations, which behave similarly to the sneaker visualizations shown here.
- Meanwhile, retrieval of PP examples with low threshold fails above 1–2 examples stored per concept.
- 2A), which captures common sneaker features (Fig.
- 3E by computing the overlap between retrieved and target patterns.
- 3E coarsely estimates the largest overlap achievable (Methods).The network capabilities observed for MF cues are preserved when we instead use PP cues (Fig.
- 3F, G) or cues combining the neurons active in either encoding (Fig.
- S3C–E); again, these latter two are similar because MF encodings are sparse.
- S3F).To show that concept target patterns  and average images within concepts are indeed valid representations of concepts for our image dataset, we plot them in image space after transforming  through the visualization pathway (Fig.
- In cognitive science as well, clustering has been used as model for unsupervised category learning (Anderson, 1991; Love et al., 2004), and central representations called prototypes can be used for category assignment (Ashby and Maddox, 2005).
- With more complex image datasets, such as CIFAR10 (Krizhevsky and Hinton, 2009), examples may not be clustered in image space or in encoding space with our model’s simple autoencoder.
- 3H, I, we show regimes for successful retrieval of MF examples, PP examples, and PP concepts.
- Figure 3I overlays retrieval regimes for MF examples and PP concepts.
- 3D–G, and it is larger for more correlated PP encodings.
- Our capacity values agree with theoretical formulas calculated using techniques from statistical physics (Kang and Toyoizumi, 2023).
- 2.To further explore the heteroassociative capability of our network, we cue the network with an MF pattern and apply a time-varying threshold during retrieval.
- S4A, B, we present analogous results for randomly generated MF and PP patterns demonstrating that these retrieval properties also depend on MF pattern sparsity.
- All in all, while our network can represent either examples or concepts at each moment in time, an oscillating threshold provides access to a range of representations over every oscillation cycle.biorxiv;2023.02.21.529365v3/FIG4F4fig4Figure 4:The CA3 model can alternate between MF example and PP con
- Four scenarios are considered: a baseline condition with abrupt threshold changes, sinusoidal threshold changes, threshold values of 0.55 and 0.25 instead of 0.6 and 0.2, and the weak input of an MF cue throughout the simulation instead of only at the beginning.
- (C) Summary of retrieval behavior between update cycles 60 to 120.
- For each scenario, 20 cues are tested in each of 20 networks.
- In all networks, 50 randomly chosen examples from each of the 3 concepts depicted in Fig.
- One update cycle corresponds to the updating of every neuron in the network (Methods).Place cell data reveals predicted relationships between encoding properties and theta phaseThe central feature of our CA3 model is that an activity threshold determines whether the network retrieves example or conc
- We claim that the theta oscillation in CA3 physiologically implements this threshold and drives changes in memory scale.
- This single-neuron prediction can be tested by analyzing publicly available datasets of CA3 place cells.
- Figure 5B shows one example place cell recorded while a rat traverses a linear track (Mizuseki et al., 2013, 2014).
- During locomotion, single-neuron activity in CA3 is strongly modulated by the theta oscillation (Fig.
- 5C); we use this activity as an indicator of network sparsity since a relationship between the two has been observed (Fig.
- We assume an equivalence between the encoding of images by our CA3 model and the encoding of spatial positions by CA3 place cells (Fig.
- 5A) into a prediction about spatial tuning (Fig.
- This prediction relies on our claim that the theta oscillation in CA3 acts as the inhibitory threshold of our model.
- The sharpening of visual tuning curves by attention is an example of this alternative prediction (McAdams and Maunsell, 1999).
- 5E roughly correspond to subtractive and divisive modulation of firing rates, respectively.
- Both kinds of inhibitory effects are found in cortical circuits (Isaacson and Scanziani, 2011; Carandini and Heeger, 2012; Ferguson and Cardin, 2020).
- We will now test whether experimental data reflect our model prediction of sharper place field tuning with higher spatial information during sparser theta phases, which would support a subtractive role of theta as an oscillating inhibitory threshold over a divisive one.biorxiv;2023.02.21.529365v3/FI
- (A) Our CA3 model predicts that single neurons convey more information per spike about example identity during sparse regimes.
- (B) Example CA3 place cell activity along a linear track.
- (C) Activity by theta phase for 5 CA3 place cells.
- (D) To test our model, we construe CA3 place cells to store fine positions as examples, which can combine into coarser regions as concepts.
- (E) Our model predicts that CA3 place fields are more sharply tuned during sparse theta phases.
- We use the Collaborative Research in Computational Neuroscience (CRCNS) hc-3 dataset contributed by György Buzsäki and colleagues (Mizuseki et al., 2013, 2014).
- Figure 5F shows one extracted field that exhibits phase precession (for others, see Fig.
- 5H that is matched in spike phases; spike positions, however, are randomly chosen from a uniform distribution.
- To correct for this bias, we follow previous protocols and subtract averages over many null-matched samples from position information (Dotson and Yartsev, 2021).
- 5A, we report sparsity-corrected information.
- Figure 5J, K illustrates a second place field whose tuning also depends on theta phase but does not exhibit precession.
- For each theta-modulated CA3 place field, we partition phases into sparse and dense halves based on activity, and we average the sparsity-corrected position information per spike across each partition.
- CA3 place fields convey significantly more information during sparse phases than dense phases (Fig.
- Thus, experimental data support our model’s prediction that CA3 encodes information in a finer, example-like manner during sparse theta phases.
- Notably, CA1 place fields do not convey more information per spike during sparse phases, which helps to show that our prediction is nontrivial and demonstrates that the phase behavior in CA3 is not just simply propagated forward to CA1 (Fig.
- S5C).To characterize the relationship between information and theta phase more precisely, we aggregate spikes over phase-precessing fields in CA3 and in CA1 (Fig.
- These aggregate fields recapitulate the single-neuron results that CA3 spikes are uniquely more informative during sparse phases (Fig.
- In CA3, information is greatest during early progression through the field, which corresponds to future locations, with a smaller peak during late progression, which corresponds to past locations.
- In contrast, past locations are more sharply tuned in CA1.
- To test this prediction using the same CRCNS hc-3 dataset, we invoke the aforementioned equivalence between concepts in our model and coarser positions along a linear track (Fig.
- Thus, single CA3 neurons should encode more information per spike about coarse positions during dense theta phases.
- 5, we divided single place fields into multiple position bins during the computation of information.
- CA1 place cells also exhibit this property (Fig.
- Note that we always consider 4 bins at a time even for track scales smaller than 1/4, because changing the number of bins across scales introduces a bias in the shuffled data (Fig.
- 5 where intact fields were explicitly extracted.
- 6E, sparse phases do not convey more information like they do in Fig.
- 5L.biorxiv;2023.02.21.529365v3/FIG6F6fig6Figure 6:Place cell data support the model prediction that denser theta phases should preferentially encode coarser, concept-like positions.
- (A) Our CA3 model predicts that single neurons convey more information per spike about concept identity during dense regimes.
- (B) To test our model, we construe CA3 place cells to store fine positions as examples, which can combine into coarser regions as concepts.
- (C) We calculate position information at various track scales over windows of 4 contiguous bins.
- In the CRCNS hc-6 dataset contributed by Loren Frank and colleagues, CA3 place cells are recorded during a W-maze alternation task in which mice must alternately visit left and right arms between runs along the center arm (Karlsson et al., 2015).
- It is known that place cells along the center arm can encode the turn direction upon entering or leaving the center arm in addition to position (Frank et al., 2000; Wood et al., 2000).
- 7A), so they should be more tuned to a particular turn direction (Fig.
- During dense phases, they should generalize over turn directions and solely encode position.biorxiv;2023.02.21.529365v3/FIG7F7fig7Figure 7:W-maze data support the model prediction that sparser theta phases should preferentially encode turn direction in addition to position.
- (B) To test our model, we construe CA3 place cells to store turn directions during the central arm of a W-maze alternation task as examples.
- In A, G, and H, information is sparsity-corrected.Figure 7C shows spikes from one CA3 place cell accumulated over outward runs along the center arm followed by either left or right turns (Fig.
- Figure 7E, F show similar results for inward runs (for others, see Fig.
- Not only do these results support our model, they also reveal that in addition to splitter cells that encode turn direction over all theta phases (Duvelle et al., 2023), CA3 contains many more place cells that encode it only at certain phases (Fig.
- The difference between sparse and dense phases is significantly greater in CA3 than it is in CA1 (Fig.
- S7G–I).Beyond the single-neuron results presented above, we seek to test our predictions at the population level.
- We find that the CA3 population likelihood exhibits greater confidence during sparse phases (Fig.
- If pressed to choose the direction with higher likelihood as its estimate, CA3 is also more accurate during sparse phases (Fig.
- 7A, B and bolster our single-neuron results.
- Moreover, they are specific to CA3, as similar conclusions cannot be made about the CA1 place cell population (Fig.
- S7J–L).In summary, extensive data analysis reveals experimental support for our CA3 model over two datasets collected by different research groups, across two encoding modalities, for both example and concept representations, and at both the single-neuron and population level.CA3-like complementary 
- To address these questions through one framework, we turn to a classic paradigm in machine learning: a multilayer perceptron trained on MNIST digits (LeCun et al., 1998).
- The former requires clustering of images based on common features, which resembles concept learning in our CA3 model, and the latter requires discerning differences between similar images, which resembles example learning in our CA3 model (Fig.
- We use a held-out test dataset to evaluate digit classification performance and corrupted images from the train dataset to evaluate set identification performance.biorxiv;2023.02.21.529365v3/FIG8F8fig8Figure 8:Complementary encodings inspired by CA3 can improve machine learning performance in a comp
- Each hidden layer contains 50 neurons.
- 3) to decorrelate encodings in the final hidden layer, in analogy with MF patterns in CA3.
- Points indicate means and bars indicate standard deviations over 32 networks.
- Each hidden layer contains 100 neurons.
- The train dataset contains 1000 images and 10 sets.
- 4) to decorrelate encodings only among the second half of the final hidden layer.
- Correlated and decorrelated encodings are both present, in analogy with MF and PP patterns across the theta cycle in CA3.
- Open symbols represent individual networks and filled symbols represent means over 64 networks.
- (J) Influence of each neuron in HalfCorr networks on concept and example learning, defined as the average decrease in accuracy upon clamping its activation to 0.
- For all results, p-values are computed using unpaired two-tailed t-tests.In our CA3 model, we found that examples were preferentially encoded by the decorrelated MF pathway and concepts by the correlated PP pathway (Fig.
- 8D):



DeCorr mimics the MF pathway; the equation is approximate due to a slight modification of the Pearson correlation formula to aid numerical convergence (Methods).
- 8E) while DeCorr networks perform better in example learning (Fig.
- 8F), and these effects vary consistently with the strength of the DeCorr loss function (Fig.
- Note that DeCorr is different from the DeCov loss function previously developed to reduce overfitting (Cogswell et al., 2015).
- S8C, D).Complex tasks, including those performed by biological systems, may require information to be processed at different scales of correlation.
- In CA3, a spectrum of encodings is available during each theta cycle.
- 8H):



where  represents the second half of neurons in the final hidden layer.
- 8J).Note that we do not manipulate pattern sparsity in these artificial networks.
- It is possible that directly diversifying sparsity can also improve machine learning performance, especially since sparse coding is known to offer certain computational advantages as well as greater energy efficiency (Olshausen and Field, 1996, 2004; Sze et al., 2017).

## Tables

### Table 1:
> Key hippocampus model parameters and their values unless otherwise noted.


## Figure Descriptions

### Figure 1:
Overview and motivation. (A) Entorhinal cortex (EC) projects to CA3 directly via the perforant path (PP, orange) as well as indirectly through the dentate gyrus (DG) via mossy fibers (MF, purple). Adapted from The Mouse Brain Library (Rosen et al., 2000, free use license). (B) MF memory encodings ar

### Figure 2:
We model the transformation of memory representations along hippocampal pathways; MF and PP encodings of the same memories converge at CA3. (A) Memories are FashionMNIST images, each of which is an example of a concept. (B) Overview of model pathways. Encoding pathways correspond to the biological a

### Figure 3:
We model CA3 to store both MF and PP encodings of the same memories; MF examples remain distinct while PP examples build concept representations. (A–C) Overview of the Hopfield-like model for CA3. (A) We store linear combinations of MF and PP encodings, with greater weight on the former because MF i

### Figure 4:
The CA3 model can alternate between MF example and PP concept representations under an oscillating threshold. Four scenarios are considered: a baseline condition with abrupt threshold changes, sinusoidal threshold changes, threshold values of 0.55 and 0.25 instead of 0.6 and 0.2, and the weak input 

### Figure 5:
Place field data support the model prediction that sparser theta phases should preferentially encode finer, example-like positions. (A) Our CA3 model predicts that single neurons convey more information per spike about example identity during sparse regimes. Each point represents a neuron. (B) Examp

### Figure 6:
Place cell data support the model prediction that denser theta phases should preferentially encode coarser, concept-like positions. (A) Our CA3 model predicts that single neurons convey more information per spike about concept identity during dense regimes. Each point represents a neuron. (B) To tes

### Figure 7:
W-maze data support the model prediction that sparser theta phases should preferentially encode turn direction in addition to position. (A) Same as Fig. 5A. (B) To test our model, we construe CA3 place cells to store turn directions during the central arm of a W-maze alternation task as examples. By

### Figure 8:
Complementary encodings inspired by CA3 can improve machine learning performance in a complex task. (A) We extend the MNIST dataset by randomly assigning an additional set label to each image. (B–F) We train a multilayer perceptron to either classify digits or identify sets. (B) Network architecture

## References
Total references in published paper: 103

### Key References (from published paper)
- Resolving new memories: A critical look at the dentate gyrus, adult neurogenesis, and pattern separa (, 2011)
- Neurons, numbers and the hippocampal network (, 1990)
- A review of modularization techniques in artificial neural networks (, 2019)
- Spin-glass models of neural networks (, 1985)
- The adaptive nature of human categorization (, 1991)
- Memory out of context: Spacing effects and decontextualization in a computational model of the media (, 2023)
- Deep reinforcement learning (, 2017)
- Human category learning (, 2005)
- Cell numbers, distribution, shape, and regional variation throughout the murine hippocampal formatio (, 2019)
- Hippocampal-prefrontal theta oscilla-tions support memory integration (, 2016)
- Prediction of learning rate from the hippocampal electroencephalogram (, 1978)
- Synaptic modifications in cultured hippocampal neurons: Dependence on spike timing, synaptic strengt (, 1998)
- Assessments of dentate gyrus function: discoveries and debates (, 2023)
- Abstract memory representations in the ventromedial prefrontal cortex and hippocampus support concep (, 2018)
- Normalization as a canonical neural computation (, 2012)
- Sparse synaptic connectivity is required for decorrelation and pattern separation in feedforward net (, 2017)
- Mechanisms and functions of theta rhythms (, 2013)
- The necessity of the hippocampus for statistical learning (, 2018)
- Nonlocal spatiotemporal representation in the hippocampus of freely flying bats (, 2021)
- Semantic memory and the hippocampus: Revisiting, reaffirming, and extending the reach of their criti (, 2020)
- Temporal context and latent state inference in the hippocampal splitter signal (, 2023)
- Tonic inhibitory control of dentate gyrus granule cells by α5-containing GABAA receptors reduces mem (, 2015)
- Mechanisms underlying gain modulation in the cortex (, 2020)
- Generalization in a Hopfield network (, 1990)
- Trajectory encoding in the hippocampus and entorhinal cortex (, 2000)
- The role of acetylcholine in learning and memory (, 2006)
- A proposed function for hippocampal theta rhythm: Separate phases of encoding and retrieval enhance  (, 2002)
- Single granule cells reliably discharge targets in the hippocampal CA3 network in vivo (, 2002)
- Theta oscillations in human memory (, 2020)
- Neural networks and physical systems with emergent collective computational abilities (, 1982)

## Ground Truth Reference
- Figures: 8
- Tables: 1
- References: 103