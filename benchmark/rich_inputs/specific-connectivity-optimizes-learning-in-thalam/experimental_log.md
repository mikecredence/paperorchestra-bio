# Experimental Log: Specific connectivity optimizes learning in thalamocortical loops

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 3ResultsWe begin by constructing a model combining cortex and thalamus based on two fundamental properties of thalamic nuclei that distinguish them from the cortex.
- First, there are far fewer neurons in the thalamus (Halley & Krubitzer, 2019) which acts as a structural bottleneck in this loop.
- Second, local recurrent excitation is a defining feature of the cortex but absent within the thalamus (Arcelli, Frassoni, Regondi, Biasi, & Spreafico, 1997; Halassa & Sherman, 2019).
- Therefore, we consider a model in which a network of N interconnected cortical neurons is reciprocally connected with M uncoupled thalamic neurons, with M ≪ N (Figure 1A).
- Thalamic activity, on the other hand, is assumed to depend only on cortical activity as r t = ϕ(W TC h t) where W TC ∈ ℝ M ×N 1denotes the matrix of corticothalamic weights.
- Network output y t∈ ℝR, which we optimize to perform behavioral tasks, is modeled as a linear readout of the cortical activity, y t = W °h twith readout weights W °∈ ℝR×N.biorxiv;2022.09.27.509618v1/FIG1F1fig1Figure 1:Combined model of cortex and thalamus.A.
- Models have N = 256 cortical neurons.
- The number of thalamic neurons (M) is varied from 1 to 128.
- Such models are interesting from a computational perspective because recent theoretical work has shown that many tasks can be solved by combining a full-rank random component with appropriate low-rank connectivity structures (Mastrogiuseppe & Ostojic, 2018) and that gradient-based learning typically
- We ask whether low-rank CTC connectivity can be learned to support behavioral tasks in a biologically plausible manner within our model.3.1Thalamocortical learning ruleRecent experimental evidence suggests that thalamocortical plasticity continues into adulthood and is a major substrate for learning
- Accordingly, we assume that thalamocortical synapses (W CT, Figure 1B – green) are adjusted such that the overall model minimizes Σ t ∥ε t ∥ 2, where  denotes the mismatch between the network output y t and some desired target output function .
- Specifically, we train thalamocortical synapses in the model using a local, biologically plausible learning rule based on a recently proposed algorithm (Random-Feedback-Local-Online, or RFLO, learning; see Methods) (Murray, 2019).The synaptic weight updates in this scheme are derived by making two a
- This relaxation is made possible by learning readout weights W ° in conjunction with thalamocortical weights, such that alignment between readout and feedback weights can be established during the course of learning (Lillicrap, Cownden, Tweed, & Akerman, 2016).
- Like other three-factor rules (Gerstner, Lehmann, Liakoni, Corneil, & Brea, 2018), the update rule for thalamocortical synapses depends only on the presynaptic activity (thalamic neuron), the postsynaptic activity (cortical neuron), and the error signal at each moment (Methods).
- Evidence for error signals in the superficial layers of the cortex (Inoue, Uchimura, & Kitazawa, 2016; Heindorf, Arber, & Keller, 2018) suggests that thalamocortical synapses located on apical dendrites e.g.
- (Guo et al., 2018) are particularly good candidates for this learning rule, but apical error signals could also drive plasticity in basal thalamocortical synapses via dendritic plateau potentials (Guerguiev, Lillicrap, & Richards, 2017; Bittner, Milstein, Grienberger, Romani, & Magee, 2017).We found
- This improvement in learning performance is accompanied by an increase in the alignment between weights in the feedback pathway B (which communicate error signals to post-synaptic neurons) and readout weights W°(Figure S1B – green), indicating that the learning rule performs credit assignment – conv
- Nonetheless, the performance of this learning strategy may depend critically on the signal received by thalamic neurons via corticothalamic projections (W TC, Figure 1B – black).
- Studies of biologically plausible algorithms in recurrent neural networks have typically dealt only with the learning of synapses onto neurons that are directly connected to the readout (Miconi, 2017; Alemi, DenÈve, Machens, & Slotine, 2018; Murray, 2019; Gilra & Gerstner, 2017).
- To test this, we trained our model by applying a local plasticity rule analogous to Equation 2 to update corticothalamic synapses (Methods – Equation 6, Figure S1A).
- In contrast to models that learn by updating thalamocortical synapses, the resulting model fails to learn even when the thalamic population size is comparable to the size of the cortex (Figure 1C – black).
- In fact, local plasticity operating simultaneously at both thalamocortical and corticothalamic synapses does not yield any improvement in learning performance over what is obtained from learning only thalamocortical synapses with fixed random corticothalamic connections (Figure 1C – gray vs green).T
- Whereas local plasticity achieves a high level of feedback alignment in cortical neurons, the alignment is no greater than chance in thalamic neurons (Figure S1B).
- Therefore, error signals cannot mediate learning via local plasticity in corticothalamic synapses (Figure S1C).
- In our model, this means that weight updates in corticothalamic synapses would need to be guided by error signals gated through both the time-varying neural activity in the cortex and thalamocortical weights, a requirement that cannot be easily implemented in a biologically plausible way.3.2Optimal 
- In particular, we sought to identify subspaces of cortical activity that, when communicated to the thalamus, improve learning supported by thalamocortical plasticity (Figure 2A).
- Specific corticothalamic connectivity that routes activity in such subspaces may be established by evolutionary or developmental processes, or by plasticity rules of a different form than Equation (2).biorxiv;2022.09.27.509618v1/FIG2F2fig2Figure 2:Corticothalamic connectivity optimized by meta-learn
- Error bars denote ± 1 SEM estimated by bootstrapping.
- All models have N = 256 cortical neurons and M = 32 thalamic neurons.To begin, we took an approach known as meta-learning or “learning to learn” (Wang, 2021; Hospedales et al., 2022).
- Corticothalamic weights were optimized at a longer time scale across thousands of epochs (“outer loop”), each of which comprises a few hundred trials of thalamocortical learning (“inner loop”) (Figure 2B; Methods).
- We optimized corticothalamic weights for each task as outlined above, and found that meta-learned corticothalamic weights substantially improved learning supported by thalamocortical weights in both tasks (Figure 2C).
- We quantified the task performance error as 1–R2 where R2 denotes the fraction of variance in the target that is predicted by the readout at the end of thalamocortical learning.
- The error dropped several fold across both tasks when thalamocortical learning was performed using optimized corticothalamic weights as opposed to random corticothalamic weights (Figure 2D; Median factor of reduction in error — Motor control: 5.8, Working memory: 5.1).
- We found qualitatively similar results when learning in the presence of random error-feedback weights, B (Methods; Figure S2A), showing that the improvement in learning performance cannot be attributed to feedback alignment used in the meta-learning procedure.We next sought to understand what struct
- We calculated the alignment β between the optimized corticothalamic weights and both the direction with the highest variance (principal component direction) and the direction that drives output (readout direction) (Methods; Figure 2E).
- We express the alignment in a normalized scale, (β − β0)/(1 − β
0) where β0corresponds to the average alignment between meta-learned corticothalamic weights and a random direction in the cortical activity space.
- Whereas alignment with the readout direction was significantly greater than the alignment with the leading principal component in the motor control task, this pattern was inverted for the working memory task where in fact the corticothalamic weights were more strongly aligned with the direction of t
- Pre-aligning corticothalamic weights to the readout direction at the beginning of the meta-learning procedure did not alter these results (Figure S2B).
- Specifically, corticothalamic projections promote learning of autonomous control largely by communicating the cortical output to the thalamus, while learning of working memory benefits from communicating the principal components of the cortical activity to the thalamus.3.3Subspace aligned corticotha
- To directly test whether these subspaces are able to support learning by themselves, we consider three idealized models with categorically different forms of corticothalamic connectivity that correspond to varying degree of structure (Methods; Figure 2B).
- Finally, we consider corticothalamic connectivity that is aligned with the readout direction and thus transmits a copy of the network output to the thalamus.We first trained the above models separately on different tasks by assuming maximum corticothalamic compression (M = 1).
- For autonomous control, aligning corticothalamic connectivity with the readout direction yielded a substantial improvement over other strategies (Median −log(1 − R2); Random: 1.2, PC: 1.2, Readout: 2.1; Figure 3A).
- In contrast, the working memory task benefited from aligning corticothalamic connectivity to the leading principal component of cortical activity (Random: 1.9, PC: 2.5, Readout: 1.8; Figure 3B).
- These is consistent with the structure of corticothalamic weights optimized by meta-learning of each task (Figure 3E).biorxiv;2022.09.27.509618v1/FIG3F3fig3Figure 3:Different corticothalamic structures support different tasks.A.
- Top: Median outputs (across simulations) of networks with a single thalamic unit (M = 1) and different corticothalamic connectivity, trained on the autonomous control task.
- Network inputs and outputs for 8 different conditions of the working memory task.
- Lower values of 1 − R2 correspond to better performance.
- All models have N = 256 cortical units.
- When aligning corticothalamic connectivity with the readout subspace, the remaining M − 1 thalamic neurons receive random projections.
- As expected, the performance of all models gradually improved with the number of thalamic neurons (Figure 3C,D).
- Nonetheless, the advantage of aligning corticothalamic projections with the readout direction (for autonomous control; Figure 3C) or principal component directions (for working memory; Figure 3D) persists even when M is relatively large, demonstrating that structured connectivity is beneficial for r
- We found that the choice of corticothalamic structure that maximized learning is robust to task complexity, depending only on the type of task being learned (Figure 3E,F).
- In the autonomous motor control task, the temporal fluctuations of the leading principal components tend to be very slow (Figure S3G).
- In contrast, the principal components of the cortical activity in the working memory task are dominated by the transient external inputs, and therefore encode the identity of the input (Figure S3H).
- The benefits of optimized corticothalamic connectivity are not observed unless thalamocortical synapses are learned (Figure S3A,B).
- Furthermore, we found that the readout signal need not be concentrated in a single thalamic neuron in order to support learning motor control (Figure S3C).
- Likewise, for the working memory task, different principal components need not be segregated in different thalamic neurons (Figure S3D).
- Finally, we found that structure in the corticothalamic connectivity is useful even if this structure is established gradually in conjunction with the learning of thalamocortical synapses (Figure S3E,F).
- Thus learning is facilitated regardless of whether the corticothalamic connectivity is developmentally hardwired (as for efferent copies of signals to the motor periphery) or learned via activity-dependent mechanisms (as for projections of the principal components of cortical activity).3.4Composite 
- To test whether our results generalize to such settings, we consider the problem of goal-directed reaching inspired by experiments in primates (Churchland et al., 2012).
- Specifically, we hypothesized that learning benefits from communicating the principal component directions during the delay period versus the readout direction during the movement period.To test this, we considered a thalamocortical model in which a cortical network is reciprocally connected to two 
- This architecture is motivated by recent experiments which show that distinct populations of thalamic neurons are active before and during movement (Gaidica, Hurst, Cyr, & Leventhal, 2018).
- Due to the two-dimensional nature of this task, we considered a minimal model in which thalamic nuclei have two neurons each (M =2).
- Consistent with our hypothesis, maximal performance was obtained in a model that conveyed principal components and readout signals to the thalamic nucleus that engaged in learning during preparation and execution, respectively (Figure 4B).
- This model exhibited excellent reaching performance to all targets (Figure 4C).
- The results are robust both to the number of target locations and the distribution of delays (Figure S4).
- These results suggest that thalamocortical learning allows the cortex to perform different movements over a range of realistic delays, provided the corticothalamic structure is chosen appropriately.biorxiv;2022.09.27.509618v1/FIG4F4fig4Figure 4:Thalamocortical model of goal-directed reaching.A.
- The 2D output of the network controls the angular accelerations of the links of a two-joint arm.
- Left: Outputs of the best model for 8 different reach conditions, shown in different shades of gray.
- Error bars denote standard errors.3.5Data are consistent with model predictionsTwo recent studies in rodents used a combination of neurophysiology and optogenetics to demonstrate that dexterous movement generation (Sauerbrei et al., 2020) and working memory (Guo et al., 2017) both depend on interact
- Since our findings indicate that thalamocortical learning of movement and memory are optimized by distinct patterns of corticothalamic interactions, we reanalyzed data from both experiments to directly test whether thalamic activity during those tasks depends on the components of cortical activity p
- In the second (Guo et al., 2017), recordings were performed in the frontal cortex specifically anterior lateral motor cortex (ALM), and thalamus – specifically ventral medial (VM) and ventral anterior–lateral (VAL) nuclei, while mice performed a delayed discrimination task to report the location of 
- We used a linear regression model to decode behavior (hand acceleration or choice depending on the task) and the activity of individual thalamic neurons, from the cortical population activity (Figures 5A-B – right, Methods).
- We restricted our analyses to the movement period and delay period for the motor control and working memory task, respectively.biorxiv;2022.09.27.509618v1/FIG5F5fig5Figure 5:Corticothalamic interactions in mice are consistent with the model.A.
- Left: Working memory task (modified from (Bjerre & Palmer, 2020)) mice reported the location of a pole by directional licking after a delay period, during recordings from frontal cortex and thalamus.
- (Motor control: n=3 sessions, Working memory: n=5).
- Fractions were normalized to a scale between 0 and 1 for each thalamic neuron before averaging.
- Error bars in D and E denote standard errors in mean (Motor control: n=101, Working memory: n=72).We found that behavior was well explained by cortical activity in both tasks (R2 — Motor control: 0.93, Working memory: 0.97).
- In mice performing the working memory task, leading principal components (PCs) of the frontal cortex activity had a large influence on the animal’s behavioral choice (Figure 5C – blue).
- In contrast, hand movements during the motor task were primarily influenced by PCs of lower variance in the motor cortex (Figure 5C – red, Figure S5C).
- We first quantified the fraction of variance explained (R2) in each thalamic neuron when using the activity of all neurons recorded in the cortex (Methods).
- We found that we could capture a substantial fraction of thalamic variance in both tasks, although the fraction was higher in the working memory task (Motor control: 0.46 ± 0.01, Working memory: 0.70 ± 0.01; Figure S5D).
- We then repeated this analysis to compute the fraction of variance explained in each thalamic neuron when using only the k leading PCs of cortical activity (R2(k)).
- To compare corticothalamic interactions across the two tasks, we computed the fraction of explainable variance as a function of the number of PCs, R2(k)/R2.
- Consistent with the model prediction, we found that more principal components are needed to explain thalamic activity during the motor control task than in working memory task (Figure 5D – red vs blue, Figure S5E).
- The fraction of explainable variance in thalamus captured by the top 5 cortical PCs was significantly greater during the working memory task than motor control (Motor control: 0.29 ± 0.02, Working memory: 0.63 ± 0.04).Further analysis suggested that corticothalamic interactions identified above are 
- In the working memory task, inhibiting cortex dramatically reduces variability in thalamus indicating that the interactions are causal (Guo et al., 2017).
- We found that thalamic activity on any given trial was substantially better predicted by cortical activity in the same trial (Figure 5E – top) suggesting that the corticothalamic interactions do not merely reflect common inputs to motor cortex and thalamus that are similar across trials, such as con
- Furthermore, we found that corticothalamic weights that capture trial-by-trial activity in thalamic neurons were better aligned with the readout weights than those that capture only trial-averaged thalamic activity (Figure 5E – bottom).

## Figure Descriptions

### Figure 1:
Combined model of cortex and thalamus.A. Schematic illustration of a thalam-ocortical network model. B. Synaptic weights of the model. Corticocortical weights (W CC) are fixed. Local learning rules can be used to update thalamocortical weights (W CT), but it is not known whether such rules are effec

### Figure 2:
Corticothalamic connectivity optimized by meta-learning.A. Corticothalamic weights may prioritize communicating specific subspaces of cortical activity, such as the readout (cyan) or principal component directions (purple), in contrast to a random subspace (orange). B. Schematic of meta-learning pro

### Figure 3:
Different corticothalamic structures support different tasks.A. Top: Median outputs (across simulations) of networks with a single thalamic unit (M = 1) and different corticothalamic connectivity, trained on the autonomous control task. Bottom: The deviation of the output from the target function (b

### Figure 4:
Thalamocortical model of goal-directed reaching.A. The model comprises two thalamic modules, one of which is active only during movement preparation and the other only during movement execution (dark gray period). The 2D output of the network controls the angular accelerations of the links of a two-

### Figure 5:
Corticothalamic interactions in mice are consistent with the model.A. Left: Motor control task – mice reached for a pellet of food following an acoustic cue, during recordings from motor cortex and motor thalamus. Right: Regression of cortical activity against behavior (hand acceleration) and thalam

## References
Total references in published paper: 87

### Key References (from published paper)
- Structural alterations in cortical and thalamocortical white matter tracts after recovery from prefr (, 2021)
- Thala-mocortical and corticothalamic pathways differentially contribute to goal-directed behaviors i (, 2018)
- Gabaergic neurons in mammalian thalamus: A marker of thalamic complexity? (, 1997)
- Rapid plasticity of higher-order thalamocortical inputs during sensory learning (, 2019)
- Recurrent neural networks as versatile tools of neuroscience research (, 2017)
- Motor cortex maturation is associated with reductions in recurrent connectivity among functional sub (, 2015)
- Thalamocortical projections onto behaviorally relevant neurons exhibit plasticity during adult motor (, 2016)
- Reorganization of recurrent layer 5 corticospinal networks following adult motor training (, 2019)
- Behavioral time scale synaptic plasticity underlies ca1 place fields (, 2017)
- Probing cortical activity during head-fixed behavior (, 2020)
- Thalamic projections sustain prefrontal activity during working memory maintenance (, 2017)
- Corticothalamic projections from the primary visual cortex in rats: a single fiber study using biocy (, 1995)
- Corticothalamic projections from the cortical barrel field to the somatosensory thalamus in rats: A  (, 1995)
- A burst-based “hebbian” learning rule at retinogeniculate synapses links retinal waves to activity-d (, 2007)
- Comparison of emg-based and accelerometer-based speed estimation methods in pedestrian dead reckonin (, 2011)
- Neural population dynamics during reaching (, 2012)
- Reciprocal circuits linking the prefrontal cortex with dorsal and ventral thalamic nuclei (, 2018)
- Synaptic plasticity in thalamic nuclei enhanced by motor skill training in rat with transient middle (, 2003)
- The role of population structure in computations through neural dynamics (, 2022)
- Distinct descending motor cortex pathways and their roles in movement (, 2018)
- Distinct populations of motor thalamic neurons encode action initiation, action selection, and movem (, 2018)
- Compressed sensing, sparsity, and dimensionality in neuronal information processing and data analysi (, 2012)
- Eligibility traces and plasticity on behavioral time scales: Experimental support of neohebbian thre (, 2018)
- Predicting non-linear dynamics by stable local learning in a recurrent spiking neural network (, 2017)
- Towards deep learning with segregated dendrites (, 2017)
- Branched thalamic afferents: What are the messages that they relay to the cortex? (, 2011)
- Cortex commands the performance of skilled movement (, 2015)
- Maintenance of persistent activity in a frontal thalamocortical loop (, 2017)
- Cortico-thalamocortical circuits of mouse forelimb s1 are organized primarily as recurrent loops (, 2020)
- Anterolateral motor cortex connects with a medial subdivision of ventromedial thalamus through cell  (, 2018)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 87