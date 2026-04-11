# Experimental Log: Factorized visual representations in the primate visual system and deep neural networks

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- These include building invariance of responses to non-identity scene parameters (or, more realistically, partial invariance6) and/or factorizing non-identity-driven response variance into isolated (factorized) subspaces (Figure 1A, left vs.
- In a non-invariant, non-factorized representation, other variables like camera viewpoint also drive variance within the identity subspace, “entangling” the representations of the two variables (Figure 1A, right; viewpoint driven variance is mainly in identity subspace, orange flat shaded region).bio
- (C) In a simulation of coding strategies for two binary variables out of 10 total dimensions that are varying (see Methods), a decrease in orthogonality of the relationship between the encoding of the two variables (alignment a>0, or going from a square to a parallelogram geometry), despite maintain
- Gaussian noise is present in the data samples (only 3 of 10 dimensions used in simulation are shown).To formalize these different representational strategies, we introduced measures of factorization and invariance to scene parameters in neural population responses (Figure 1B; see Equations 2-4 in Me
- Factorization is computed by identifying the axes in neural population activity space that are influenced by varying the parameter of interest and assessing how much it overlaps the axes influenced by other parameters (“a” in Figure 1B,C; lower overlap corresponds to higher factorization).
- We quantified this overlap in two different ways (“PCA based” and “covariance based” factorization, corresponding to Equations 2 and 4 in Methods) which produced similar results when compared in subsequent analyses (unless otherwise noted, factorization scores will generally refer to the PCA based m
- Though the example presented in Figure 1 focused on factorization of and invariance to object identity versus non-identity variables, we stress that our definitions can be applied to any scene variables of interest.
- Furthermore, we presented a simplified visual depiction of the geometry within each scene variable subspace in Figure 1.
- We emphasize that our factorization metric does not require a particular geometry within a variable’s subspace, whether parallel linearly ordered coding of viewpoint as in the cylindrical class manifolds shown in Figure 1A and 1B, or a more complex geometry where there is a lack of parallelism and/o
- Intuitively, factorization increases with higher dimensionality as this decreases overlap, all other things being equal (in the limit, the angle between points will approach 90° or a fully orthogonal code in high dimensions), and for a given finite, fixed dimension, factorization is mainly driven by
- In a simulation, we found that the extent to which the variables of interest were represented in a factorized way (i.e., along orthogonal axes, rather than correlated axes) influenced the ability of a linear discriminator to successfully decode both variables in a generalizable fashion from a few tr
- Specifically, we took advantage of an existing dataset in which the tested images independently varied object identity versus object pose plus background context13.
- We found that both V4 and IT responses exhibited more significant factorization of object identity information from non-identity information than a shuffe control (which accounts for effects on factorization due to dimensionality of these regions) (Figure S1; see Methods).
- Furthermore, the degree of factorization increased from V4 to IT (Figure 2A).
- Consistent with prior studies, we also found that invariance to non-identity information increased from V4 to IT in our analysis (Figure 2A, right, solid lines)14.
- Invariance to non-identity information was even more pronounced when measured in the subspace of population activity capturing the bulk (90%) of identity-driven variance, as a consequence of increased factorization of identity from non-identity information (Figure 2A, right, dashed lines).To illustr
- Specifically, we analyzed a transformed neural representation obtained by rotating the population data so that inter-class variance more strongly overlapped with the principal components of the intra-class variance in the data (see Equation 1 in Methods).
- The applied linear basis rotation leaves all other activity statistics completely intact (such as mean neural firing rates, covariance structure of the population, and its invariance to non-class variables) yet has the effect of strongly reducing object identity decoding performance in both V4 and I
- Our analysis shows that maintaining invariance alone in the neural population code was insufficient to account for a large fraction of decoding performance in high-level visual cortex; factorization of non-identity variables is key to the decoding performance achieved by V4 and IT representations.bi
- Like factorization, invariance also increased from V4 to IT (note, “identity” refers to invariance to all non-identity position factors, solid black line)(right).
- between-class variance (Equation 1 in Methods).
- dark red bars in each plot, chance = 1/64; n=128 multi-unit sites in V4 and 128 in IT).We next asked whether factorization is found in deep neural network (DNN) model representations and whether this novel, heretofore unconsidered metric is a strong indicator of more brainlike models.
- In this fashion, we may indirectly assess the relative significance of geometric properties like factorization and invariance to biological visual representations – if, for instance, models with more factorized representations consistently match neural data more closely, we may infer that those neur
- To measure factorization, invariance, and decoding properties of DNN models, we generated an augmented image set, based on the images used in the previous dataset (Figure 2), in which we independently varied the foreground object identity, foreground object pose, background identity, scene lighting,
- Specifically for each base image from the original dataset, we generated sets of images that varied exactly one of the above scene parameters while keeping the others constant, allowing us to measure the variance induced by each parameter relative to the variance across all scene parameters (Figure 
- We presented this large image dataset to models (4000 images total) to assess the relative degree of representational factorization of and invariance to each scene parameter.
- These included models using supervised training for object classification15,16, contrastive self-supervised training17,18, and self-supervised models trained using auxiliary objective functions19–22 (see Methods and Table S2).biorxiv;2023.04.22.537916v3/FIG3F3fig3Figure 3.Measurement of factorizatio
- For computing the representational metrics of factorization of and invariance to a scene parameter, variance in model responses was induced by individually varying each of four scene parameters (n=10 parameter levels) for each base scene (n=100 base scenes)(see images at top left).
- The combination of model-layer metric and model-layer dataset predictivity for a choice of model, layer, metric, and dataset specifies the coordinates of a single dot on the scatter plots in Figures 4 and 7, and the across model correlation coefficient between a particular representational metric an
- We found that the final layers of trained networks exhibited consistent increases in factorization of all tested scene parameters relative to a randomly initialized (untrained) baseline with the same architecture (Figure 4A, top row, rightward shift relative to black cross, a randomly initialized Re
- By contrast, training DNNs produced mixed effects on invariance, typically increasing it for background and lighting but reducing it for object pose and camera viewpoint (Figure 4A, bottom row, leftward shift relative to black cross for left two panels).
- Moreover, we found that the degree of factorization in models correlated with the degree to which they predicted neural activity for single-unit IT data (Figure 4A, top row), which can be seen as correlative evidence that neural representations in IT exhibit factorization of all scene variables test
- Invariance showed mixed correlations with neural predictivity (Figure 4A, bottom row), suggesting that IT neural representations build invariance to some scene information (background and lighting) but not to others (object pose and observer viewpoint).
- Similar effects were observed when we assessed correlations between these metrics and fits to human behavioral data rather than macaque neural data (Figure 4B).biorxiv;2023.04.22.537916v3/FIG4F4fig4Figure 4.Neural and behavioral predictivity of models versus their factorization and invariance proper
- Note that factorization (PCA based, see Methods) in trained models is consistently higher than that for an untrained, randomly initialized Resnet-50 DNN architecture (rightward shift relative to black cross).
- (B) Same as (A) except for human behavior performance patterns across images (human I2 dataset).
- A noticeable drop in neural predictivity was seen for high levels of invariance to object pose (bottom row, second panel).To assess the robustness of these findings to choice of images and brain regions used in an experiment, we conducted the same analyses across a large and diverse set of previousl
- Consistently, increased factorization of scene parameters in model representations correlated with models being more predictive of neural spiking responses, voxel BOLD signal, and behavioral responses to images (Figure 5A, black bars; see Figure S2 for scatter plots across all datasets).
- Although invariance to appearance factors (background identity and scene lighting) correlated with more brainlike models, invariance for spatial transforms (object pose and camera viewpoint) consistently did not (zero or negative correlation values; Figure 5C, red and green open circles).
- Our results were preserved when we re-ran the analyses using only the subset of models with the identical ResNet-50 architecture (Figure S3) or when we evaluated model predictivity using representational dissimilarity matrices of the population (RDMs) instead of linear regression (encoding) fits of 
- Furthermore, the main finding of a positive correlation between factorization and neural predictivity was robust to the particular choice of PCA threshold we used to quantify factorization (Figure S5).
- We found similar results using a covariance based method for computing factorization that does not have any free parameters (Figure 5C faded filled circles; see Equations 4 in Methods).biorxiv;2023.04.22.537916v3/FIG5F5fig5Figure 5.Scene parameter factorization correlates with more brainlike DNN mod
- In all cases, model representational metric and neural predictivity score were computed by averaging scores across the last 5 model layers.
- (B) Instead of computing factorization scores using our synthetic images (Figure 3, top left), recomputing camera viewpoint or object pose factorization from natural movie datasets that primarily contained camera or object motion, respectively, gave similar results for predicting which model represe
- Results using a comparable, alternative method for computing factorization (covariance based, Equation 4 in Methods; light closed symbols) are shown adjacent to the original factorization metric (PCA based, Equation 2 in Methods; dark closed symbols).Finally, we tested whether our results generalize
- Here, instead of relying on our synthetically generated images, where each scene parameter was directly controlled, we re-computed factorization from two types of relatively unconstrained natural movies, one where the observer moves in an urban environment (approximates camera viewpoint changes)27 a
- Similar to the result found for factorization measured using augmentations of synthetic images, factorization of frame-by-frame variance (local in time, presumably dominated by either observer or camera motion; see Methods) from other sources of variance across natural movies (non-local in time) was
- human), cortical brain areas (V4 vs.
- Prior work had identified a similar correlation between object classification performance (measured fitting a decoder for object class using model representations) and fidelity to neural data3.
- A priori, it is possible that the correlations we have demonstrated between scene parameter factorization and neural fit can be entirely captured by the known correlation between classification performance and neural fits2,3, as factorization and classification may themselves be correlated.
- However, we found that factorization scores significantly boosted cross-validated predictive power of neural/behavioral fit performance compared to simply using object classification alone, and factorization boosted predictive power as much if not slightly more when using RDMs instead of linear regr
- Thus, considering factorization in addition to object classification performance improves upon our prior understanding of the properties of more brainlike models (Figure 7).biorxiv;2023.04.22.537916v3/FIG6F6fig6Figure 6.Scene parameter factorization combined with object identity classification impro
- Linearly combining factorization with classification in a regression model (unfaded bars at right) produced significant improvements in predicting the most brainlike models (performance cross-validated across models and averaged across datasets, n=4 datasets for each of V4, IT/HVC and behavior).
- Error bars are standard deviations over bootstrapped resampling of the models.biorxiv;2023.04.22.537916v3/FIG7F7fig7Figure 7.Combining classification performance with object pose factorization improves predictions of the most brainlike models on IT/HVC data.Example scatter plots for neural and fMRI 

## Tables

### Table S1.
> Datasets used for measuring similarity of models to the brain.Datasets from both macaque and human high-level visual cortex as well as high-level visual behavior were collated for testing the brainlik


### Table S2.
> Models tested.For each model, we measured representational factorization and invariance in each of the final five layers of the model as well as evaluating their brainlikeness using the datasets in Ta


## Figure Descriptions

### Figure 1.
Framework for quantifying factorization in neural and model representations.(A) A subspace for encoding a variable, for example object identity, in a linearly separable manner can be achieved by becoming invariant to non-class variables (compact spheres, middle column, where the volume of the sphere

### Figure 2.
Benefit of factorization to neural decoding in macaque V4 and IT.(A) Factorization of object identity and position increased from macaque V4 to IT (PCA based factorization, see Methods; dataset E1 – multiunit activity in macaque visual cortex)(left). Like factorization, invariance also increased fro

### Figure 3.
Measurement of factorization in DNN models and comparison to brain data.Schematic showing how metaanalysis on models and brain data was conducted by first computing various representational metrics on models and then measuring a model’s predictive power across a variety of datasets. For computing th

### Figure 4.
Neural and behavioral predictivity of models versus their factorization and invariance properties.(A) Scatter plots for example neural dataset (IT single-units, macaque E2 dataset) showing the correlation between a model’s predictive power as an encoding model for IT neural data versus a model’s abi

### Figure 5.
Scene parameter factorization correlates with more brainlike DNN models.(A) Factorization of scene parameters in model representations computed using the PCA based method consistently correlated with a model being more brainlike across multiple independent datasets measuring monkey neurons, human fM

### Figure 6.
Scene parameter factorization combined with object identity classification improves correlations with neural predictivity.Average across datasets of brain predictivity of classification (faded black bar), dimensionality (faded pink bar), and factorization (remaining faded colored bars) in a model re

### Figure 7.
Combining classification performance with object pose factorization improves predictions of the most brainlike models on IT/HVC data.Example scatter plots for neural and fMRI datasets (macaque E1 & E2, IT multi-units & single-units; human F1 & F2, fMRI voxels) showing a saturating and sometimes reve

### Figure S1.
Factorization and invariance in V4 & IT neural data.Normalized factorization and invariance as in Figure 2A but after subtracting shuffe control for V4 and IT neural datasets. Shuffing the image identities of each population vector accounts for increases in factorization driven purely by changes in 

### Figure S2.
Scatter plots for all datasets.Scatter plots as in Figure 4A,B for all datasets. Brain metrics (y-axes) by panel are: (A) macaque neuron/human voxel fits in V4 cortex, (B) macaque neuron/human voxel fits in ITC/HVC, and (C) macaque/human per-image classification performance (I1) and image-by-distrac

### Figure S3.
Predictivity of factorization and invariance restricting to ResNet-50 model architectures.Same format as Figure 5C except with the analyses restricted to using only models with the Resnet-50 architecture. The main finding of factorization of scene parameters in DNNs being generally positively correl

### Figure S4.
Predictivity of factorization and invariance for RDMs.Same format as Figure 5C except for predicting population representational dissimilarity matrices (RDMs) of macaque neurophysiological and human fMRI data (in Figure 5C linear encoding fits of each single neuron/voxel were used to measure brain p

### Figure S5.
Effect on neural and behavioral predictivity of PCA threshold for computing PCA based factorization, Related to Figure 5.The % variance threshold used in the main text for estimating a PCA linear subspace capturing the bulk of the variance induced by all other parameters besides the parameter of int

## References
Total references in published paper: 48

### Key References (from published paper)
- Deep Neural Networks Rival the Representation of Primate IT Cortex for Core Visual Object Recognitio (, 2014)
- Brain-Score: Which Artificial Neural Network for Object Recognition is most Brain-Like? (, 2020)
- Performance-optimized hierarchical models predict neural responses in higher visual cortex (, 2014)
- Brain hierarchy score: Which deep neural networks are hierarchically brain-like? (, 2021)
- Untangling invariant object recognition (, 2007)
- Functional Compartmentalization and Viewpoint Generalization Within the Macaque Face-Processing Syst (, 2010)
- Explicit information for category-orthogonal object properties increases along the ventral stream (, 2016)
- The ventral visual pathway: an expanded neural framework for the processing of object quality (, 2013)
- Capturing the objects of vision with neural networks. Nat (, 2021)
- Classification and Geometry of General Perceptual Manifolds (, 2017)
- Abstract representations emerge naturally in neural networks trained to perform multiple tasks (, 2023)
- Simple Learned Weighted Sums of Inferior Temporal Neuronal Firing Rates Accurately Predict Human Cor (, 2015)
- Selectivity and Tolerance (“Invariance”) Both Increase as Visual Information Propagates from Cortica (, 2010)
- ImageNet Classification with Deep Convolutional Neural Networks (, 2012)
- Deep Residual Learning for Image Recognition (, 2015)
- Momentum Contrast for Unsupervised Visual Representation Learning (, 2020)
- A Simple Framework for Contrastive Learning of Visual Representations (, 2020)
- Contrastive Multiview Coding (, 2019)
- Unsupervised Visual Representation Learning by Context Prediction (, 2016)
- Large Scale Adversarial Representation Learning (, 2019)
- Balanced Increases in Selectivity and Tolerance Produce Constant Sparseness along the Ventral Visual (, 2012)
- Large-Scale, High-Resolution Comparison of the Core Visual Object Recognition Behavior of Humans, Mo (, 2018)
- Identifying natural images from human brain activity (, 2008)
- Deep image reconstruction from human brain activity (, 2019)
- Discovering important people and objects for egocentric video summarization (, 2012)
- Goal-Driven Recurrent Neural Network Models of the Ventral Visual Stream (, 2021)
- Deep Clustering for Unsupervised Learning of Visual Features (, 2019)
- Unsupervised Learning of Visual Features by Contrasting Cluster Assignments (, 2020)
- Disentangling by Factorising (, 2018)
- A Framework for the Quantitative Evaluation of Disentangled Representations (, 2018)

## Ground Truth Reference
- Figures: 12
- Tables: 2
- References: 48