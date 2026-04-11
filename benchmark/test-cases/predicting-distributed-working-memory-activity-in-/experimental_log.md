# Experimental Log: Predicting distributed working memory activity in a large-scale mouse brain: the importance of the cell type-specific connectome

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsA decreasing gradient of PV interneuron density from sensory to association cortexOur large-scale circuit model of the mouse cortex uses inter-areal connectivity provided by anatomical data within the 43-area parcellation in the common coordinate framework v3 atlas (Oh et al.
- 1B-C, neuron density is shown in Fig.
- 1F, the PV cell fraction is plotted as a function of the cortical hierarchy, which shows a moderate negative correlation between the two.
- Therefore, primary sensory areas have a higher density of PV interneurons than association areas, although the gradient of PV interneurons does not align perfectly with the cortical hierarchy.biorxiv;2022.12.05.519094v4/FIGS1F10figS1Figure 1 - Supplement 1.Anatomical details of the mouse cortex.
- Connectivity matrix depicting cortico-cortical connections between 43 cortical areas.
- 2018.biorxiv;2022.12.05.519094v4/FIG1F1fig1Figure 1.Anatomical basis of the multi-regional mouse cortical model.
- Normalized PV cell fraction for each brain area, visualized on a 3d surface of the mouse brain.
- Hierarchical position for each area on a 3d brain surface.
- The hierarchical position is normalized and the hierarchical position of VISp is set to be 0.
- Correlation between PV cell fraction and hierarchy (Pearson correlation coefficient r = −0.35, p < 0.05).A whole-mouse cortex model with a gradient of interneuronsIn our model, each cortical area is described by a local circuit (Fig.
- 2A), using a mean-field reduction (Wong and Wang 2006) of a spiking neural network (Wang 2002).
- Therefore, feedforward connections have a greater net excitatory effect than feedback connections, which is referred to as counterstream inhibitory bias (CIB) (Mejias and Wang 2022; Javadzadeh and Hofer 2022; Wang 2022).
- According to the CIB assumption, long-range connections to inhibitory neurons are stronger for feedback connections and weaker for feedforward connections, while the opposite holds for long range connections to excitatory neurons.biorxiv;2022.12.05.519094v4/FIG2F2fig2Figure 2.Distributed working mem
- 2014) and follows counterstream inhibitory bias (CIB) (Mejias and Wang 2022).
- The activity of 6 selected areas during a working memory task is shown.
- A visual input of 500ms is applied to area VISp, which propagates to the rest of the large-scale network.
- Delay period firing rate for each area on a 3d brain surface.
- 1B, the positions of 5 areas are labeled.
- Delay-period firing rate is positively correlated with cortical hierarchy (r = 0.91, p < 0.05).
- Delay-period firing rate is negatively correlated with PV cell fraction (r = −0.43, p < 0.05).Distributed working memory activity depends on the gradient of inhibitory neurons and the cortical hierarchyWe simulated the large-scale network to perform a simple visual delayed response task that require
- This persistent firing rate could last for more than 10 seconds and is a stable attractor state of the network (Inagaki et al.
- 2019).The cortical hierarchy and PV fraction predict the delay period firing rate of each cortical area (Fig.
- The delay activity pattern has a stronger correlation with hierarchy (r = 0.91) than with the PV fraction (r = −0.43).
- 2D) that marks an abrupt transition in the cortical space.
- 2 - supplement 1), by stimulating primary somatosensory area SSp-bfd and primary auditory area AUDp.
- Moreover, the cortical hierarchy could predict the delay period firing rate of each cortical area well (r = 0.89, p < 0.05), while the PV cell fraction could also predict the delay period firing rate of each cortical area with a smaller correlation coefficient (r = −0.4, p < 0.05).
- 2018).We explored the potential contributions of PV gradients and CIB in determining spatially-patterned activity across the cortex.
- 3A(i)), we found that, during the delay period, the number of cortical areas displaying persistent activity is diminished, but the abrupt transition in delay period firing rates remains.
- Thus, CIB may be particularly important in determining which areas exhibit persistent activity.biorxiv;2022.12.05.519094v4/FIGS2F11figS2Figure 2 - Supplement 1.Example simulation for different sensory modalities.
- 2, except that the external input is applied to primary sensory areas related to two other sensory modalities: somatosensory and auditory.
- The activity of 6 selected areas during the working memory task is shown.
- A somatosensory input of 500ms is applied to primary somatosensory area SSp-bfd, which propagates to the rest of the large-scale network.
- 2D), delay period firing for somatosensory stimulation is positively correlated with cortical hierarchy (r = 0.89, p<0.05).
- Delay period firing rate is moderately correlated with PV cell fraction (r =−0.4, p<0.05).
- Delay period firing is also positively correlated with cortical hierarchy (r = 0.89, p<0.05).
- Delay period firing rate is moderately correlated with PV cell fraction (r = −0.4, p<0.05)biorxiv;2022.12.05.519094v4/FIGS3F12figS3Figure 3 - Supplement 1.Dependence of persistent activity on inhibitory model parameters (A).
- If the base inhibitory strength is larger than a threshold (0.155, marked by the dashed line), none of the areas show independent persistent activity.biorxiv;2022.12.05.519094v4/FIG3F3fig3Figure 3.The role of PV inhibitory gradient and hierarchy-based counter inhibitory bias (CIB) in determining per
- Delay firing rate as a function of PV cell fraction with both CIB and PV gradient present (r =−0.42, p<0.05).
- Delay firing rate as a function of hierarchy after removal of PV gradient (r= 0.85, p<0.05).
- Delay firing rate as a function of PV cell fraction after removal of CIB (r =−0.74, p<0.05).
- Delay firing rate as a function of PV cell fraction with both CIB and PV gradient present, in the alternative regime (r =−0.7, p<0.05).
- Delay firing rate as a function of hierarchy after removal of PV gradient, in the alternative regime (r = 0.95, p<0.05).
- Delay firing rate as a function of PV cell fraction after removal of CIB, in the alternative regime (r =−0.84, p<0.05).
- Number of areas showing persistent activity (color coded) as a function of the local inhibitory gradient (gEI,scaling, X axis) and the base value of the local inhibitory gradient (gEI,0, Y axis) for the following scenarios: (C) CIB and PV gradient, (D) with PV gradient replaced by a constant value, 
- Blue shaded squares in the heatmap mark the absence of a stable baseline.To further explore the model parameter space and better understand the interplay between PV gradient and CIB, we systematically varied two critical model parameters: i) the base local inhibitory weight gEI,0 onto excitatory neu
- 3C, we simulate the network with both CIB and PV gradient, while in Fig.
- 3E we simulate networks when PV gradient or CIB is removed, respectively.
- In each of these networks, we identify two regimes based on specific values for gEI,0 and gEI,scaling: a reference regime (used throughout the rest of the paper) and an alternative regime.If we remove the PV gradient in the alternative parameter regime, persistent activity is lost (Fig.
- 3B(i)), this suggests the existence of a CIB mechanism at play.
- 3C) results in a more robust system, i.e., a far wider set of parameters can produce realistic persistent activity (Fig.
- 3D, 3E).Local and long-range projections modulate the stability of the baseline state in the cortexThe stability of the baseline state for any given cortical area may have contributions from local inhibition or from long-range projections that target local inhibitory circuits.
- 4A, see methods for theoretical calculation of stability in a local circuit).
- Thus, inhibition from local and long-range circuits contribute to the baseline stability of cortical areas.biorxiv;2022.12.05.519094v4/FIG4F4fig4Figure 4.Local and long-range projections modulate the baseline stability of individual cortical areas.
- Steady state firing rates are shown as a function of hierarchy for different scenarios: (A) without long-range connections in the reference regime (gE,self = 0.4nA, gEI,0 = 0.192nA), (B) with long-range connections in the reference regime (μEE = 0.1nA), (C) without long-range connections and increas
- 2020), whereby recurrent excitation is balanced by inhibition to maintain stability of the baseline state.
- 4C and see stability analysis in the Methods section).
- 4B shows that the network becomes unstable if long-range projections onto inhibitory interneurons are removed.
- 4F)In summary, we have shown that distinct local and long-range inhibitory mechanisms shape the pattern of working memory activity and stability of the baseline state.Thalamocortical interactions maintain distributed persistent activityTo investigate how thalamocortical interactions affect the large
- There are no recurrent connections in the thalamus within or across thalamic nuclei (Jones 2007).
- The effect of thalamic reticular nucleus neurons was included indirectly as a constant inhibitory current to all thalamic areas (Crabtree 2018; Hádinger et al.
- Thalamocortical projections in the model are slightly more biased toward excitatory neurons in the target area if they are feedforward projections and towards inhibitory neurons if they are feedback.biorxiv;2022.12.05.519094v4/FIGS5F13figS5Figure 5 - Supplement 1.Anatomical data of thalamus and cort
- Connectivity matrix of corticothalamic connections: 43 cortical areas to 40 thalamic areas.
- Connectivity matrix of thalamocortical connections: 40 thalamic areas to 43 cortical areas.biorxiv;2022.12.05.519094v4/FIG5F5fig5Figure 5.Thalamocortical interactions help maintain distributed persistent activity.
- 2A, but with modified parameters.
- The activity of 6 sample cortical areas in a working memory task is shown during control (blue) and when thalamic areas are inhibited in the delay period (red).
- The activity pattern has a positive correlation with cortical hierarchy (r = 0.78, p < 0.05).
- The activity pattern has a negative correlation with PV cell fraction, but it is not significant (r =−0.26, p = 0.09).
- The firing rate has a positive correlation with thalamic hierarchy (r = 0.94, p < 0.05).
- Delay period firing rate of cortical areas in thalamocortical network has a positive correlation with delay firing rate of the same areas in a cortex-only model (r = 0.77, p < 0.05).
- 5B, blue) but is maintained with the help of the thalamocortical loop, as observed experimentally (Guo et al.
- 5B, red).In the thalamocortical model, the delay activity pattern of the cortical areas correlates with the hierarchy, again with a gap in the firing rate separating the areas engaged in persistent activity from those that do not (Fig.
- This comparison suggests that the cortical model captures most of the dynamical properties in the thalamocortical model; therefore in the following analyses, we will mainly focus on the cortex-only model for simplicity.Cell type-specific connectivity measures predict distributed persistent firing pa
- There is no significant correlation between input strength and delay period firing rate (r = 0.25, p = 0.25, Fig.
- 6A(i), A(ii)) and input strength cannot predict which areas show persistent activity (prediction accuracy = 0.51, Fig.
- As a result, the modified cell type-specific connectivity measures increase if the target area has a low density of PV interneurons and/or if long-range connections predominantly target excitatory neurons in the target area.biorxiv;2022.12.05.519094v4/FIGS6F14figS6Figure 6 - Supplement 1.Details of 
- The cell type projection coefficient is given by the formula kcell = mij−PVi(1−mij).
- The modified connectivity strength is given by .biorxiv;2022.12.05.519094v4/FIG6F6fig6Figure 6.Cell type-specific connectivity measures are better at predicting firing rate pattern than nonspecific ones.
- Input strength does not show significant correlation with delay period firing rate for areas showing persistent activity in the model (r = 0.25, p = 0.25).
- Input strength cannot be used to predict whether an area shows persistent activity or not (prediction accuracy = 0.51).
- Cell type-specific input strength has a strong correlation with delay period firing rate of cortical areas showing persistent activity (r = 0.89, p < 0.05).
- Cell type-specific input strength predicts whether an area shows persistent activity or not (prediction accuracy = 0.95).
- Similarly, we found that the cell type-specific eigenvector centrality, but not standard eigenvector centrality (Newman 2018), was a good predictor of delay period firing rates (Fig.
- 6 - supplement 2).A core subnetwork for persistent activity across the cortexMany areas show persistent activity in our model.
- We can assign the areas to the four classes based on three properties: a) the effect of inhibiting the area during stimulus presentation on delay activity in the rest of the network; b) the effect of inhibiting the area during the delay period on delay activity in the rest of the network; c) the del
- Firing rates of areas with small firing rate (<1Hz) are partially shown (only RSPv and RSPd are shown because their hierarchical positions are close to areas showing persistent activity).
- Classification of 4 types of areas based on their delay period activity after stimulus- and delay-period inhibition (color denotes the type for area, as in A).
- 7C), which we identify as a core for working memory.
- 7D).We have defined a core area for working memory maintenance as a cortical area that, first, exhibits persistent activity, and second, removal of this area (e.g., experimentally via a lesion or opto-inhibition) significantly affects persistent activity in other areas.
- 7-supplement 1A), as by definition, inhibiting any single readout area will not exhibit a strong inhibition effect.biorxiv;2022.12.05.519094v4/FIGS6AF15figS6aFigure 6 - Supplement 2.Cell type-specific eigenvector centrality measures are better at predicting firing rate patterns than raw eigenvector 
- 6, where we compared cell type-specific input strength and raw input strength.
- Eigenvector centrality does not show a significant correlation with delay period firing rate for areas showing persistent activity in the model (r = 0.24, p = 0.29).
- Eigenvector centrality cannot be used to predict whether an area shows persistent activity or not (prediction accuracy = 0.46).
- Cell type-specific eigenvector centrality has a strong correlation with the firing rate of cortical areas showing persistent activity (r = 0.94, p < 0.05).
- Cell type-specific eigenvector centrality predicts whether an area shows persistent activity or not (prediction accuracy = 0.79).
- Raw input strength and cell type-specific input strength are also included for comparison.biorxiv;2022.12.05.519094v4/FIGS6BF16figS6bFigure 6 - Supplement 3.Sign only input strength measure and noPV input strength measure predict firing rate well.
- noPV input strength has a strong correlation with delay period firing rate of cortical areas showing persistent activity (r =0.90, p <0.05).biorxiv;2022.12.05.519094v4/FIGS7F17figS7Figure 7 - Supplement 1.Multiple-area inhibition experiments demonstrate the relative importance for core and readout a
- Although some readout areas show persistent firing, there is 48% decrement in average firing rate.We first inhibited pairs of readout areas and evaluated the effect of this manipulation at a network level.
- Moreover, there was a 48% decrement in the average firing rate compared with a 15% decrement for a single core area and a 3% decrement for a single readout area.
- 8A).biorxiv;2022.12.05.519094v4/FIG8F8fig8Figure 8.The core subnetwork can be identified structurally by the presence of strong excitatory loops.
- Distribution of length-2 loops.
- Loop strengths of each area calculated using different length of loops (e.g., length 3 vs length 2) are highly correlated (r = 0.96, p < 0.05).
- Loop strength (blue) is plotted alongside Core Areas (orange), a binary variable that takes the value 1 if the area is a Core Area, 0 otherwise.
- The loop strength is normalized to a range of (0, 1) for better comparison.
- A high cell type-specific loop strength predicts that an area is a core area (prediction accuracy = 0.93).
- Here we focus on length-2 loops (Fig.
- 8A); the strength of a loop is the product of two connection weights for a reciprocally connected pair of areas; and the loop strength measure of an area is the sum of the loop strengths of all length-2 loops that the area is part of.
- 8 - supplement 1 for results of longer loops).
- 8D(ii), prediction accuracy = 0.93).
- Cell type-specific connectivity, and new metrics that account for such connectivity, are necessary to infer the role of brain areas in supporting large-scale brain dynamics during cognition.biorxiv;2022.12.05.519094v4/FIGS8F18figS8Figure 8 - Supplement 1.Cell type-specific loop strengths (Length 3 l
- Loop strengths (length 3 loops or L3) is calculated using similar method as loop strengths (length 2 loops).
- The only difference is we considered loops with length 3 (eg.
- 7, where we compared cell type-specific loop strengths (length 2 loops) and raw loop strengths.
- Loop strength (blue) is plotted alongside Core Areas (orange), a binary variable that takes the value 1 if the area is indeed a Core Area, 0 otherwise.
- Loop strength is normalized to a range of (0, 1) for better comparison.
- High cell type-specific loop measures predicts that an area is a Core Area (prediction accuracy = 0.95).
- Same as (A), but for cell type-specific loop strength.biorxiv;2022.12.05.519094v4/FIGS8AF19figS8aFigure 8 - Supplement 2.(A1).
- Relationship between core areas (orange) and length 2 (sign only) loop strength.
- Whether an area is a core area is represented in either 0 or 1.
- Blue curve shows the logistic regression analysis used to differentiate the core areas versus non core areas (prediction accuracy = 0.83).
- Same as (A1) and (A2), but with length 3 sign only loop strength.
- Length 3 sign only loop strength does not show a positive relationship with core areas (prediction accuracy = 0.83) (C1).
- Same as (A1) and (A2), except for comparing whether an area is a core area (orange) and length 2 noPV loop strength.
- Length 2 noPV loop strength predicts the core areas.
- prediction accuracy = 0.90 (D1).
- Same to A1 and A2, except for comparing whether an area is a core area (orange) and length 3 noPV loop strength.
- Length 3 noPV loop strength does not show a positive relationship with core areas.
- prediction accuracy = 0.83.To better demonstrate our cell type-specific connectivity measures, we have implemented two other measures for comparison: a) a loop-strength measure that adds a ‘sign’ without further modification, and b) a loop strength measure that takes hierarchical information - and n
- On the other hand, the prediction of the core areas greatly depends on cell-type specificity: the sign-only and ‘no-PV’ mechanisms do not reliably predict whether an area is a core area or not, especially in the case of calculating with length 3 loops, demonstrating the importance of cell-type speci
- 8 - supplement 2).Multiple attractor states emerge from the mouse mesoscopic connectome and local recurrent interactionsDifferent tasks lead to dissociable patterns of internally sustained activity across the brain, described dynamically as distinct attractor states.
- Generally, attractor states may enable computations such as decision making and working memory (Wang 1999; Wang 2002; Mejias et al.
- These parameters affect the number of attractors in a model of the macaque cortex (Mejias and Wang 2022).
- This leads to less variability and fewer attractors.biorxiv;2022.12.05.519094v4/FIG9F9fig9Figure 9.Multiple attractors coexist in the mouse working memory network.
- Delay activity is shown on a 3D brain surface.
- In (D), local excitatory strengths are fixed (gE,self = 0.44 nA) while long-range connection strengths vary in the range μEE = 0.01-0.05 nA.
- Left and right panels of (D) show one specific parameter μEE = 0.03 nA.
- Inset panel of (D) shows the number of attractors under different long-range connection strengths while gE,self is fixed at 0.44 nA.
- In (E), long range connection strengths are fixed (μEE = 0.02 nA) while local excitatory strengths varies in the range gE,self = 0.4-0.44 nA.
- Left and right panels of (E) show one specific parameter gE,self = 0.43 nA.
- Inset panel of (E) shows the number of attractors under different local excitatory strengths, while μEE is fixed at 0.02 nA.
- Prediction of the delay period firing rate using input strength and cell type-specific input strength for each attractor state identified under μEE = 0.04 nA and gE,self = 0.44 nA.
- 143 distinct attractors were identified and the average correlation coefficient using cell type-specific input strength is better than that using input strength.
- A example attractor state identified under the parameter regime μEE = 0.03 nA and gE,self = 0.44 nA.
- The 5 areas with persistent activity are shown in red.
- For a regime where 5 areas exhibit persistent activity during the delay period, inactivation of the premotor area MOs yields a strong inhibition effect (<0.95 orange dashed line) and is therefore a Core area for the attractor state in (G).
- Only 5 areas with persistent activity are used to calculate the loop strength.
- Loop strength is normalized to be within the range of 0 and 1.
- High cell type-specific loop measures predict that an area is a Core area (prediction accuracy is 100% correct).
- 9D).When the local excitatory strength is increased, the number of attractors increased as well (Fig.
- This can be understood by a simple example of two areas 1 and 2, each capable of two stimulus-selective persistent activity states; even without coupling there are 2 × 2 = 4 attractor states with elevated firing.
- In an example parameter regime (μEE = 0.04 nA and gE,self = 0.44 nA), we identified 143 attractors.
- In one example attractor, we found 5 areas that show persistent activity: VISa, VISam, FRP, MOs and ACAd (Fig.
- 9G) (parameter regime, μEE = 0.03 nA and gE,self = 0.44 nA).

## Tables

### Table 1:
> Supplementary experimental evidence. The listed literature include experiments that provide supporting evidence for working memory activity in cortical and subcortical brain areas in the mouse or rat.


### Table 2:
> Parameters for numerical simulations


## Figure Descriptions

### Figure 1 - Supplement 1.
Anatomical details of the mouse cortex. (A). Connectivity matrix depicting cortico-cortical connections between 43 cortical areas. Areas are sorted according to their hierarchy. (B). The raw PV cell density for each cortical area (Y axis), with areas sorted (X axis). Each area belongs to one of five

### Figure 1.
Anatomical basis of the multi-regional mouse cortical model. (A). Flattened view of mouse cortical areas. Figure adapted from (Harris et al. 2019). (B). Normalized PV cell fraction for each brain area, visualized on a 3d surface of the mouse brain. Five areas are highlighted : VISp, Primary somatose

### Figure 2.
Distributed working memory activity depends on the gradient of PV interneurons and the cortical hierarchy. (A). Model design of the large-scale model for distributed working memory. Top, connectivity map of the cortical network. Each node corresponds to a cortical area and an edge is a connection, w

### Figure 2 - Supplement 1.
Example simulation for different sensory modalities. The simulation protocol is the same as the default one in Fig. 2, except that the external input is applied to primary sensory areas related to two other sensory modalities: somatosensory and auditory. (A). The activity of 6 selected areas during 

### Figure 3 - Supplement 1.
Dependence of persistent activity on inhibitory model parameters (A). The maximum firing rate of all areas depends on the constant PV cell fraction in models without a gradient of PV. Average PV cell fraction from the anatomical data is shown as an orange dot. (B). Same as (A), except for the number

### Figure 3.
The role of PV inhibitory gradient and hierarchy-based counter inhibitory bias (CIB) in determining persistent activity patterns in the cortical network. (A(i)). Delay firing rate as a function of PV cell fraction with both CIB and PV gradient present (r =−0.42, p<0.05). This figure panel is the sam

### Figure 4.
Local and long-range projections modulate the baseline stability of individual cortical areas. Steady state firing rates are shown as a function of hierarchy for different scenarios: (A) without long-range connections in the reference regime (gE,self = 0.4nA, gEI,0 = 0.192nA), (B) with long-range co

### Figure 5 - Supplement 1.
Anatomical data of thalamus and cortical connectivity. (A). Connectivity matrix of corticothalamic connections: 43 cortical areas to 40 thalamic areas. (B). Connectivity matrix of thalamocortical connections: 40 thalamic areas to 43 cortical areas.

### Figure 5.
Thalamocortical interactions help maintain distributed persistent activity. (A). Model schematic of the thalamocortical network. The structure of the cortical component is the same as our default model in Fig. 2A, but with modified parameters. Each thalamic area includes two excitatory populations (

### Figure 6 - Supplement 1.
Details of cell type-specific connectivity measures. (A). The matrix of cell type projection coefficients between cortical areas. The cell type projection coefficient is given by the formula kcell = mij−PVi(1−mij). (B). The matrix of connectivity strengths, modified by cell type projection coefficie

### Figure 6.
Cell type-specific connectivity measures are better at predicting firing rate pattern than nonspecific ones. (A(i)). Delay period firing rate (orange) and input strength for each cortical area. Input strength of each area is the sum of connectivity weights of incoming projections. Areas are plotted 

### Figure 7.
A core subnetwork generates persistent activity across the cortex. (A). We propose four different types of areas. Input areas (red) are responsible for coding and propagating external signals, which are then propagated through synaptic connections. Core areas (blue) form strong recurrent loops and g

### Figure 6 - Supplement 2.
Cell type-specific eigenvector centrality measures are better at predicting firing rate patterns than raw eigenvector centrality measures. The analysis is the same as in Fig. 6, where we compared cell type-specific input strength and raw input strength. Eigenvector centrality (EC, eigencentrality) o

### Figure 6 - Supplement 3.
Sign only input strength measure and noPV input strength measure predict firing rate well. (A1). Delay period firing rate (orange) and sign only input strength for each cortical areas. (A2). Sign only input strength has a strong correlation with delay period firing rate of cortical areas showing per

### Figure 7 - Supplement 1.
Multiple-area inhibition experiments demonstrate the relative importance for core and readout areas in maintaining network-level persistent activity. (A). The x-axis shows readout areas that are inhibited as part of a pair (blue), triplet (orange), or quadruplet (green). For any given readout area A

### Figure 8.
The core subnetwork can be identified structurally by the presence of strong excitatory loops. (A). Distribution of length-2 loops. X axis is the single loop strength of each loop (product of connectivity strengths within loop) and Y axis is their relative frequency. (B). Loop strengths of each area

### Figure 8 - Supplement 1.
Cell type-specific loop strengths (Length 3 loops) are also better at predicting firing rate patterns than raw loop measures. Loop strengths (length 3 loops or L3) is calculated using similar method as loop strengths (length 2 loops). The only difference is we considered loops with length 3 (eg. A1-

### Figure 8 - Supplement 2.
(A1). Relationship between core areas (orange) and length 2 (sign only) loop strength. Areas are sorted according to their hierarchy. Whether an area is a core area is represented in either 0 or 1. (A2). High loop strength is a good predictor of whether an area is a core area. Blue curve shows the l

### Figure 9.
Multiple attractors coexist in the mouse working memory network. (A-C) Example attractor patterns with a fixed parameter set. Each attractor pattern can be reached via different external input patterns applied to the brain network. Delay activity is shown on a 3D brain surface. Color represents the 

## References
Total references in published paper: 109

### Key References (from published paper)
- “The mind of a mouse (, 2020)
- “Vestibulo-ocular reflex arc (, 1933)
- “An International Laboratory for Systems and Computational Neuroscience (, 2017)
- Working Memory: Theories, Models, and Controversies (, 2012)
- “Alterations of Cortical Pyramidal Neurons in Mice Lacking High-Affinity Nicotinic Receptors (, 2010)
- Small-World Brain Networks Revisited (, 2017)
- “Thalamic Projections Sustain Prefrontal Activity during Working Memory Maintenance (, 2017)
- “Hierarchy of Transcriptomic Specialization across Human Cortex Captured by Structural Neuroimaging  (, 2018)
- “Role of Local Network Oscillations in Resting-State Functional Connectivity (, 2011)
- “Local Connectivity and Synaptic Dynamics in Mouse and Human Neocortex (, 2022)
- “A Large-Scale Circuit Mechanism for Hierarchical Dynamical Processing in the Primate Cortex (, 2015)
- “The Distributed Nature of Working Memory (, 2017)
- “Functional Diversity of Thalamic Reticular Subnetworks (, 2018)
- “The Hebbian paradigm reintegrated: local reverberations as internal representations (, 1995)
- “How Local Excitation–Inhibition Ratio Impacts the Whole Brain Dynamics (, 2014)
- “Hierarchical Heterogeneity across Human Cortex Shapes Large-Scale Neural Dynamics (, 2019)
- “Stable Propagation of Synchronous Spiking in Cortical Neural Networks (, 1999)
- “Feature-Based Visual Short-Term Memory Is Widely Distributed and Hierarchically Organized (, 2018)
- “Graded Persistent Activity in Entorhinal Cortex Neurons (, 2002)
- “Complex Dendritic Fields of Pyramidal Cells in the Frontal Eye Field of the Macaque Monkey: Compari (, 1998)
- “A Cortical Substrate for Memory-Guided Orienting in the Rat (, 2011)
- “A Cell Atlas for the Mouse Brain (, 2018)
- Distributed Hierarchical Processing in the Primate Cerebral Cortex (, 1991)
- “A Dopamine Gradient Controls Access to Distributed Working Memory in the Large-Scale Monkey Cortex (, 2021)
- “Gradients of Neurotransmitter Receptor Expression in the Macaque Cortex (, 2023)
- “Multimodal Gradients across Mouse Cortex (, 2019)
- “Mnemonic Coding of Visual Space in the Monkey’s Dorsolateral Prefrontal Cortex (, 1989)
- “Neuron Activity Related to Short-Term Memory (, 1971)
- “The Mouse Cortical Connectome, Characterized by an Ultra-Dense Cortical Graph, Maintains Specificit (, 2018)
- A Cortico-Cerebellar Loop for Motor Planning (, 2018)

## Ground Truth Reference
- Figures: 19
- Tables: 2
- References: 109