# Experimental Log: Transformations of sensory information in the brain reflect a changing definition of optimality

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- In recent years, there has been a concerted effort to characterize the visual “diet” of binocular disparities that is typical of natural experience (12–15).
- Using a previously-collected data set in which people were eye-tracked while performing natural tasks (12), we calculated the probability distribution of binocular disparities within a central 10° radius from fixation while people performed two different tasks: food preparation and navigation (Fig.
- 1C, “infomax” dashed line)(16, 17).
- This representation can be interpreted as a reference prior (18), which assumes the least possible information about the world, or Jeffrey’s prior, providing invariance across transformation of sensory units (19).Under common assumptions on computational limits, this FI ∝ p2 power law corresponds to
- Prior work has found signatures of this power law across a range of early sensory brain areas (3, 20).
- Thus, for perceptual discrimination, neural codes that minimize some other error metric like mean squared error are often appropriate (L2 norm; Fig.
- 1C, “discrimax” dotted line)(5, 17).
- The discrimination-maximizing “discrimax” line shown in the Figure corresponds to a specific power law of FI ∝ p0.5.
- This objective (along with objects that aim to minimize other Lp norm errors like the sum of absolute errors) results in consistently more compressive nonlinearities than information maximization (6, 21)).
- For neural codes for binocular disparity, we would therefore expect the population FI to be more strongly peaked at zero disparity in early visual regions, and more equally spread out across a broader range of disparities in later visual regions.Neural populations differ as predicted by a transition
- Since the precise shape of the disparity probability distribution varies between tasks (and different resource constraints can change the numerical value of the optimal exponent for the power law (5, 21)), here we focus on the relative transformation of the FI exponent between brain regions rather t
- To this end, we compiled a data set of 1056 neurons’ binocular disparity responses spanning brain areas V1, V2, and MT of the macaque monkey.
- The mean responses of each neuron as a function of binocular disparity were fit with a continuous 1D Gabor function and the individual neuron FI associated with each tuning curve was calculated from these fits based on assumption of Poisson spiking (Fig.
- 2A).biorxiv;2023.03.24.534044v1/FIG2F2fig2Fig.
- We compiled a data set of 1056 disparity tuning curves from brain areas V1, V2, and MT of the macaque monkey.
- 1C) is shown for each brain area (thick lines).
- Thin lines represent the population FI computed from 500 bootstrapped samples from each brain area.For a single neuron, the FI is high when the tuning curve is steep and the spike rate (and Poisson noise) is low, and the FI is low when the tuning curve is flat and the spike rate is high (for example
- Qualitatively, we see that the population FI is most kurtotic in V1/V2 and least kurtotic in MT, consistent with the hypothesis that the information-maximizing model is a better description of the early visual representation (V1 and V2) and the discrimination-maximizing model is a better description
- Binocular disparities are distributed non-uniformly across the visual field during natural behavior (12), so we started by resampling the natural disparity distributions based on the specific retinotopic locations of neuronal receptive fields in each population using kernel-smoothed density estimate
- S2A&B), despite the minor differences in sampling density between the different brain regions.We calculated the power law that, when applied to the corresponding disparity distributions, resulted in the best fit to the measured FI of each neuronal population.
- Consistent with our working hypothesis, we observed a systematic decrease in the distribution of exponents for the best fit power law from the lower-level areas V1 and V2 to mid-level area MT for both natural tasks (Fig.
- Note that in both plots, the distributions for V1 and V2 are largely overlapping.
- The results of these fits suggest that V1 and V2 are closer to populations optimized to preserve information about binocular disparity (particularly for the food preparation task, for which the best fit exponents are 1.64 and 1.57, respectively).
- Of course, the differences between V1/V2 and MT are not as extreme as the infomax and discrimax examples given in Fig 1, but the relative shift is robust and persistent across both example disparity distributions.biorxiv;2023.03.24.534044v1/FIG3F3fig3Fig.
- Histogram bars indicate the 500 bootstrapped samples for each brain area and solid lines indicate the Gaussian distribution fits to each set of samples.
- Note that the V1 and V2 distributions are highly overlapping.
- The power law exponents are as follows: V1: 1.51, V2: 1.69, MT:1.22.
- Power law exponents: V1: 0.61, V2: 0.62, MT: 0.41.However, we observed one notable inconsistency with this interpretation, with respect to V2 and the food preparation task.
- 3B&D show the matches between the population FI (solid lines) and the binocular disparity distributions scaled by the single best fit exponents (dashed lines) from Fig.
- The distributions match closely in all cases except for the V2 population and the food preparation task (green lines in Fig.
- S1): the V2 receptive fields are exclusively concentrated in the lower visual field, and the disparity statistics in the lower visual field are strongly biased towards near disparities during food preparation (12).
- The effect sizes, measured as Cohen’s D between pairs of populations, were large between the earlier areas and MT (food preparation: V1 vs.
- As expected from the similarity in their FI distributions, the effect sizes were small between V1 and V2 (food preparation: 0.36, navigation: V1 vs.
- Thus, the data support the notion that the MT FI reflects a different optimization but that V1 and V2 may contain similar information-driven codes.These differences correspond to a broad set of changes in individual tuning curve characteristicsfrom V1/V2 to MTWe next asked which aspects of the neura
- In sum, we find that MT neurons generally have higher response offsets, broader envelopes, and lower disparity frequencies than either V1 or V2.
- Full results of the statistical comparisons across populations are provided in Tables S1 & S2.
- This analysis expands on a previous comparison between V1 and MT (22) by including responses from V2 and a larger number of V1 neurons.
- Our subsampling from the initial larger data set resulted a good match between the brain areas in terms of eccentricity and vertical position within the visual field, although the MT data set is more concentrated in the left visual field and the V1/V2 data sets are more concentrated in the right vis
- Since there is no reason to hypothesize that disparity tuning should differ in terms of left or right visual field, these tuning differences most likely reflect differences in the underlying neural representation.biorxiv;2023.03.24.534044v1/FIG4F4fig4Fig.
- 4.We fit all the neuronal data with a modified 6 parameter Gabor function and plotted the distribution of best-fitting parameters for each cortical area from which we have data.
- The vertical dashed line in the Gaussian plot marks the center of the Gaussian envelope while the cosine plot indicates the 0 phase position.
- The parameters are defined as follows: A: Amplitude, r0: vertical response offset, μenv: Gaussian envelope mean, σenv: Gaussian envelope standard deviation, f: cosine frequency, ϕ: cosine phase.
- Distributions of best fitting Gabor parameters for each of the 3 cortical areas.
- Thin white bars indicate the 25th and 75th quartile and the thick black bar indicates the median.An increase in neurons preferring larger disparities is a key factor in the observed coding transformationThere are clear differences in the distribution of best fit Gabor parameters and the preferred di
- Therefore, we performed a resampling analysis to see if the changes in any one parameter in particular could account for the difference in the FI distributions between V1 and MT.
- Since the FI distributions from V1 and V2 were similar, we did not repeat this analysis for the difference between V2 and MT.
- 5A: for one tuning curve parameter at a time (illustrated just for frequency), we replaced the set of true V1 values with a new set of values obtained by randomly sampling from the distribution of MT fits.
- Lastly, we summed the individual cell FI distributions and normalized by the area under the curve to compare the overall shapes of the resampled FI distribution for V1 and the true FI distribution for MT.
- This process was repeated a total of 500 times for this Gabor parameter and then another 500 times for each of the Gabor parameters individually to assess the variability in the resulting resampled V1 population FI distributions.
- 5B shows the resulting V1 population FI distributions (black) for each of the parameters alongside the true MT population FI distribution (red).
- Of the six parameters, replacing the V1 envelope mean parameter with those from MT qualitatively results in the closest match with the lowest variability.biorxiv;2023.03.24.534044v1/FIG5F5fig5Fig.
- We investigated which of the 6 Gabor parameters best explained the difference in the population FI between V1 and MT by replacing (one parameter at a time) from V1 with randomly sampled values pulled from the distribution of best-fitting parameters from the MT population.
- We repeated this process to create 500 new bootstrapped V1 populations for each of the 6 parameters.
- The mean and interquartile range of the population FI distributions from the 6 resampled V1 populations (purple) are plotted against the true MT population FI (red, same in each of the 6 subplots).
- The original true V1 FI distribution before resampling is shown as blue lines for reference (same in each of the 6 subplots).
- Jensen-Shannon Divergence (JSD) between the resampled V1 population FI distributions and the true MT population FI distribution.
- RV1) and the true MT population FI.
- (Black circles, errorbars) Median JSD and interquartile range across all bootstraps.To examine the significance of these matches, we calculated the Jensen-Shannon divergence (JSD) between the FI of each of the resampled V1 populations and the true MT population FI distribution (Fig.
- We first tested whether there were significant differences between the sets of JSDs for each parameter using a Kruskal-Wallis test and confirmed there were differences in dissimilarity between the parameters (χ2 = 1.65E3; df=5; p<2.22E-16).
- While there were significant differences between each of the sets of resampled populations (see Table S3), the μenv parameter stood out in that it’s associated JSD values were substantially lower than all other parameters (note the large z-scores) – that is, it was the least divergent from (most sim
- S4 and Table S5 and S4).From this pattern of results, we can glean that much of the difference in how disparity information is represented between earlier and later cortical areas can be attributed the presence of a greater number of cells that are selective for larger disparities in MT.

## Figure Descriptions

### Fig. 1.
A. Points in the peripheral visual field tend to fall on disparate retinotopic locations because the eyes are laterally offset. The retinotopic difference in these locations is called the horizontal binocular disparity (abbreviated as simply disparity in figures). Populations of neurons that are tun

### Fig. 2.
A. We compiled a data set of 1056 disparity tuning curves from brain areas V1, V2, and MT of the macaque monkey. The mean responses of each neuron as a function of disparity were fit with a continuous function and the individual neuron FI associated with each tuning curve was calculated from these f

### Fig. 3.
A. The distribution of best-fit power law exponents linking population FI to the disparity probability densities is plotted for the food preparation data set (using the kernel-smoothed probability densities to guide sampling). Histogram bars indicate the 500 bootstrapped samples for each brain area 

### Fig. 4.
We fit all the neuronal data with a modified 6 parameter Gabor function and plotted the distribution of best-fitting parameters for each cortical area from which we have data. A. Decomposing the Gabor function into Gaussian (left plot) and cosine (right plot) components clarifies what each parameter

### Fig. 5.
A. We investigated which of the 6 Gabor parameters best explained the difference in the population FI between V1 and MT by replacing (one parameter at a time) from V1 with randomly sampled values pulled from the distribution of best-fitting parameters from the MT population. We repeated this process

## References
Total references in published paper: 39

### Key References (from published paper)
- Some informational aspects of visual perception (, 1954)
- Natural image statistics and neural representation (, 2001)
- Visual perception and the statistical properties of natural scenes (, 2008)
- Efficient sensory encoding and bayesian inference with heterogeneous neural populations (, 2014)
- Efficient neural codes that minimize l p reconstruction error (, 2016)
- The physiology of stereopsis (, 2001)
- Neural mechanisms underlying stereoscopic vision (, 1998)
- 3-D vision and figure-ground separation by visual cortex (, 1994)
- Binocular and monocular stimuli for motion in depth: Changing-disparity and changing-size feed the s (, 1979)
- Disruptive coloration and binocular disparity: breaking camouflage (, 2019)
- Stereopsis is adaptive for the natural environment (, 2015)
- A dataset of stereoscopic images and ground-truth disparity mimicking human fixations in peripersona (, 2017)
- Estimating 3d tilt from local image cues in natural scenes (, 2016)
- The southampton-york natural scenes (syns) dataset: Statistics of surface attitude (, 2016)
- Mutual information, fisher information, and population coding (, 1998)
- Mutual Information, Fisher Information, and Efficient Coding (, 2016)
- The formal definition of reference priors (, 2009)
- An invariant form for the prior probability in estimation problems (, 1946)
- Neural and perceptual signatures of efficient sensory coding (, 2016)
- Coding of horizontal disparity and velocity by mt neurons in the alert macaque (, 2003)
- Correlations and Neuronal Population Information (, 2016)
- Dethroning the Fano Factor: A Flexible, Model-Based Approach to Partitioning Neural Variability (, 2018)
- Range and mechanism of encoding of horizontal disparity in macaque V1 (, 2002)
- Binocular neurons in V1 of awake monkeys are selective for absolute, not relative, disparity (, 1999)
- A specialization for relative disparity in V2 (, 2002)
- Prior Expectations in Visual Speed Perception Predict Encoding Characteristics of Neurons in Area MT (, 2022)
- An unexpected specialization for horizontal disparity in primate primary visual cortex (, 2002)
- Measuring V1 Receptive Fields Despite Eye Movements in Awake Monkeys (, 2003)
- Understanding the Cortical Specialization for Horizontal Disparity (, 2004)
- Receptive Field Size in V1 Neurons Limits Acuity for Perceiving Disparity Modulation (, 2004)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 39