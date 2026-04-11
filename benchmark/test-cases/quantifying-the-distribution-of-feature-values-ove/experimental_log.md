# Experimental Log: Quantifying the distribution of feature values over data represented in arbitrary dimensional spaces

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 3.Results3.1.SI quantifies the topological distribution of scalar feature valuesBefore applying our method to the study of neural data, we used toy model data to illustrate its performance and robustness to a wide range of point cloud characteristics.
- We generated 3 independent toy-models, including a 2D linear gradient (40,000 points), a 3D solid ball (40,000 points) where the feature was distributed along the radius, and a 3D lamp (32,000 points) whose feature varies in terms of the three axes (Fig.
- 3A).biorxiv;2022.11.23.517657v1/FIG3F3fig3Fig.
- 3.Robustness of SI under a wide range of data-cloud characteristics.A, Three toy models used to evaluate performance of SI (40,000 points for the gradient and the ball; 32,000 points for the lamp).
- D, Effects of the number of points in the data cloud as examined in a 2D space.
- Importantly, the SI performed smoothly for a wide range of points in the cloud when examined in 2 dimensions (Fig.
- 3D).In terms of the number of bin-groups used when computing the SI, there are two potential cases.
- 3E), the topological characteristics of the data cloud may have different impacts that should be examined for each application.Finally, we studied the sensitivity of the SI to different levels of noise in terms of the Signal to Noise Ratio (SNR), as defined in (Zeng et al., 2019).
- To this purpose, we introduced Gaussian noise across all existing dimensions (Fig.3F, left).
- This renders the SI suitable for testing a wide variety of experimental data sets.3.2.Evaluating the structure distribution of vectorial featuresThe definition of bin-groups used in the SI can be extended to vectorial features which integrate values from several characteristics.
- Thus, a point (p) in the cloud will fall within the bin-group u if and only if both entries of the associated feature vector fall within the common range.To illustrate the case, we generated a point cloud sampled from a sphere of unitary radius using two angles θ, φ, with added Gaussian noise in 3D.
- 4B).biorxiv;2022.11.23.517657v1/FIG4F4fig4Fig.
- 4.Evaluating structure of vectorial features.A, 3D sphere defined by trigonometric equations depending on angles θ and φ (40,000 points).
- C, A D-dimensional sphere is defined by trigonometric equations depending on D-1 angles (8DxN points, with N=40,000 points to keep cloud density over D-dimensional spaces).
- The plot at right shows the dependence of SI on the sphere dimension, computed for the D-1 angle alone, and for all angles in vectorial form.
- Dashed lines indicate results from shuffled distribution values (99th percentile).
- D, Behavior of SI for a feature defined in 2D according to the equation shown (20,000 points).To evaluate the generalization of this behavior to vectorial features of any dimension, we generated point-clouds sampled from D-dimensional spheres according to the equation shown in Fig.
- For each point cloud in D-dimensional space, we computed the SI for both the D − 1 angle used to generate the sphere and all angles together as a feature vector (Fig.
- However, when only the D − 1 angle is considered, the SI declined as the dimensionality of the sphere increased.
- This reflects the fact that as the dimensions become larger, a lower percentage of coordinates depend on the D− 1 angle, and thus the position of a given point is less dependent on it.This property of the SI can be exploited to examine the interdependence between distinct interrelated features.
- For instance, we created a 2D cloud where the position of each point depends on two features: a, b (Fig.
- However, SI(a, b) rapidly increased with α reaching a plateau at maximum structure around 1 when both a and b equally contributed to the position of points.These examples illustrate the capability of the SI to capture the structure of vectorial features, opening new avenues to study the relative imp
- To illustrate the effectiveness of the approach, we chose a public dataset of extracellular recordings from multi-site silicon probes in the anterodorsal thalamic nucleus (ADn) of freely moving mice (Peyrache et al., 2015).
- This dataset has been recently used to demonstrate the intrinsic attractor manifold of the mammalian head-direction system (Chaudhuri et al., 2019), permitting direct testing of the ability of SI to extract feature structure.In their study, Chaudhuri et al.
- showed that neural activity of N-simultaneously recorded ADn neurons of mice foraging in an open environment was constrained to a ring-shaped 3D manifold (Fig.
- 5A, right; n=6 mice), which they visualized in 3D using Isomap (Fig.
- Therefore, structure was implicitly expected at least in the low dimensional representation.biorxiv;2022.11.23.517657v1/FIG5F5fig5Fig.
- 5.Using SI to evaluate neural representations.A, In the neural manifold framework, firing rates from N-neurons at a given time (ts) are represented in an N-dimensional Euclidean space.
- B, 3D neural manifold computed from the head direction system by Chaudhuri et al., with the head direction angle projected over the data cloud.
- C, SI of the head direction angle in the original (og) and 3D-embedded representations (emb).
- Dashed lines indicate results from shuffled distribution values (99th percentile).
- D, Example of the weighted directed graphs from the same mouse (mouse12 - 120806) in the original and in the low-dimensional embedding.
- Fitting curve parameters: α= -0.12; β=4.47; γ=-4.7 and Δ=0.9; tested significant at p<0.05.
- F, Head direction data plotted over the 3D embedding for awake, REM, and SWS states separately.
- ANOVA effects for space (F(2,1)=8.2, p=0.007) but not for feature nor interaction.
- Post-hoc tests: *, p<0.05; **, p<0.01; ***, p<0.001.
- ANOVA effects for state (F(2,1)=83.5, p<0.0001), space (F(2,1)=25.7, p<0.0001) and interaction.
- Post-hoc tests: *, p<0.05; **, p<0.01; ***, p<0.001.When computing the SI of the head-direction angle over the neural manifold (3 neighbors), we obtained a high structure concordant with visual inspection of the embedding (Fig.
- the analysis was mainly restricted to the 3D reduced space.
- 5C; grey, paired sample t-test p=0.011).
- Visualization of individual weighted directed graphs from the high- and the low-dimensional representations confirm similar organization (Fig.5D).In their original work, the author parametrized the manifold with splines of matching topology and used them to decode the represented latent variable (he
- We found that the SI correlated with the decoder error (Spearman correlation -0.83, p=0.042), following an exponential decay relationship (R2=0.98; Fig.5E).
- That is, manifolds with lower decoding errors had higher head-direction structure as measured by SI.Given the nature of the data, we wondered whether the head direction representation can be retrieved during REM as well as in SWS states (Senzai and Scanziani, 2022).
- To tackle this question, we resorted to the same dataset but used all neural data to compute the 3D manifold as reported in Chaudhuri et al.
- The SI returned structure for both the animal state and the head-direction angle, with higher values in the original than in the reduced space (Fig.5G; ANOVA effects for space, F(2,1)=8.2, p=0.007, but not for feature nor interaction).
- 5G).Finally, we computed the SI of the head-direction angle for each state separately (Fig.
- In general, data represented in the original space provided more structure than in the manifold embedding (ANOVA effects for state (F(2,1)=83.5, p<0.0001), space (F(2,1)=25.7, p<0.0001) and interaction).
- Thus, being able to evaluate neural activity in the original space using the SI might provide new insights into the representative capacity during multiple brain states.3.4.Application to arbitrary D-dimensional spaces (temporal samples and images)Finally, we applied the SI to two additional general
- Data consisted on 4 seconds of musical notes of different pitch and velocity downsampled as 4800 time stamps.
- Notes were represented in the 4800-dimensional space (Fig.S1A), and the SI was calculated both locally (using 3 neighbors) and globally (60 neighbors).
- In general, data showed a higher local than global structure (Fig.S1B; ANOVA effects F(3,1)=4.0, p<0.0001).
- We found that the pitch provided maximal structure, followed by the source and family, as confirmed by the weighted directed graph returned by the overlapping of instrument families (Fig.S1C; ANOVA effects for features F(3,1)=12.0, p<0.0001).
- Reducing data to 3D allowed for visualization of these trends (Fig.S1D), and provided similar SI figures as for the original space (Fig.S1E).For image analysis, we chose using images of one hundreds bird species, typically exploited in fine-grained recognition problems.
- Data consist on RGB images (56×56×3 pixels) so that each image was represented as a point in a 9408-dimensional space (Fig.S2A).
- SI was maximal for bird species, followed by family and order (Fig.2SB).
- S2C,D).These examples illustrate how the SI method successful operates in arbitrary D-dimensional spaces, allowing for a range of multidisciplinary applications in neuroscience, as well as across other research fields.

## Figure Descriptions

### Fig. 1.
Illustration of the concepts behind the definition of the Structure Index (SI).A, Feature gradient distribution in a 2D-ellipsoid data cloud. Each point in the data cloud is assigned to a group associated with a feature bin value (bin-group). B, C, Next, the overlapping matrix between bin-groups is 

### Fig. 2.
Parametric dependence of SI on the number of neighbors.A, A local pattern is simulated in 2D by projecting feature values differently along the data cloud (9000 points). Note local structure between bin-groups. B, The same 2D data cloud exhibiting a global distribution of feature values. C, Dependen

### Fig. 3.
Robustness of SI under a wide range of data-cloud characteristics.A, Three toy models used to evaluate performance of SI (40,000 points for the gradient and the ball; 32,000 points for the lamp). B, Objects in A were embedded into spaces of increasing dimensionality by adding noise and then rotating

### Fig. 4.
Evaluating structure of vectorial features.A, 3D sphere defined by trigonometric equations depending on angles θ and φ (40,000 points). Feature values can be defined for each angle independently, θ or φ, and for both together in a vectorial form (θ, φ). B, SI for each individual angle values and for

### Fig. 5.
Using SI to evaluate neural representations.A, In the neural manifold framework, firing rates from N-neurons at a given time (ts) are represented in an N-dimensional Euclidean space. Activity is constrained in a subspace which can be retrieved using dimensionality reduction approaches (d-dimension).

## References
Total references in published paper: 21

### Key References (from published paper)
- Event-based sonification of EEG rhythms in real time (, 2007)
- The intrinsic attractor manifold and population dynamics of a canonical cognitive circuit across wak (, 2019)
- Neural population dynamics during reaching (, 2012)
- Dimensionality reduction for large-scale neural recordings (, 2014)
- Hippocampal gamma oscillations form complex ensembles modulated by behavior and learning (, 2022)
- Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders (, 2017)
- Neural Manifolds for the Control of Movement (, 2017)
- Toroidal topology of population activity in grid cells (, 2022)
- Efficient Neural Coding in Auditory and Speech Perception (, 2019)
- Global Forebrain Dynamics Predict Rat Behavioral States and Their Transitions (, 2004)
- Parsing Hippocampal Theta Oscillations by Nested Spectral Components during Spatial Exploration and  (, 2018)
- Multimodal determinants of phase-locked dynamics across deep-superficial hippocampal sublayers durin (, 2020)
- Geometry of abstract learned knowledge in the hippocampus (, 2021)
- Internally organized mechanisms of the head direction sense (, 2015)
- Field potential signature of distinct multicellular activity patterns in the mouse hippocampus (, 2010)
- A cognitive process occurring during sleep is revealed by rapid eye movements (, 2022)
- A global geometric framework for nonlinear dimensionality reduction (, 2000)
- A multi-encoder variational autoencoder controls multiple transformational features in single-cell i (, 2022)
- Mechanisms for Selective Single-Cell Reactivation during Offline Sharp-Wave Ripples and Their Distor (, 2017)
- Cell types in the mouse cortex and hippocampus revealed by single-cell RNA-seq (, 2015)
- 3D Point Cloud Denoising using Graph Laplacian Regularization of a Low Dimensional Manifold Model (, 2019)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 21