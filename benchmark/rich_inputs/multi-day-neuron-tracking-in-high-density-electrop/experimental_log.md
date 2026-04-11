# Experimental Log: Multi-day Neuron Tracking in High Density Electrophysiology Recordings using EMD

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 2Results2.1ProcedureOur datasets consist of multiple recordings taken from three mice (Figure 7a) over 2 months.
- The time gap between two recordings ranges from two to 25 days.
- Each dataset is spike-sorted individually with a standard Kilosort 2.5 pipeline.
- are used as input for our method (post-processed using ecephys spike sorting pipeline29) (Sec.
- KSgood units are mainly determined by the amount of inter-spike-interval violations and are believed to represent a single unit.16Our overall strategy is to run spike-sorting once per session, and then to generate a unit-by-unit assignment between pairs of datasets.
- 4.2), or match consecutive pairs of sessions and then trace matched units through all sessions (Sec.
- 2.4).We refer to the subset of KSgood units with strong and distinguishable visual responses in both datasets of a comparison as reference units (See Sec.
- Similar to Steinmetz et al.7 we validated our unit matching of reference units using visual receptive field similarity.
- Finally, we showed that trackable units with strong visual responses are qualitatively similar to those without (Figure 5-supplement Figure 1 to Figure 5).To provide registration between pairs of recordings, we used the Earth Mover’s Distance (EMD).30, 31 We use a feature space consisting of a geome
- 4.1.1).We use EMD in two stages: rigid drift correction and unit assignment.
- a distance between two units dik is given by  (Figure 2a).
- The first EMD stage estimates the homogeneous vertical movement of the entire population of KSgood units (Figure 2b).
- The rigid drift estimation procedure is illustrated in figure 2b.
- 4.4).biorxiv;2023.08.03.551724v5/FIG2F2fig2Fig.
- 2:The EMD can detect the displacement of single units:a.
- Each blue unit in day 1 is matched to a red unit in day 2.
- Open and filled circles show positions of units in days 1 and 2, respectively.
- Solid lines indicate a z-match distance within 15μm, while a dashed line indicates a z distance > 15μm.
- Expanded view shows probe area from 3120 to 3220 μm.
- The light blue dashed line shows the mode (dm = 15.65μm).
- The dark blue dashed line shows the imposed drift (di = 12μm).
- The red region shows the matches within 15μm of the mode.
- units in the black region that are unlikely to be the real matches due to biological constraints.For each unit, the location is determined by fitting the peak to peak amplitudes on the 10 sites nearest the site with peak signal, based on the triangulation method in Boussard, et al.32 (Sec.
- The waveform distance is an L2 norm between two spatial-temporal waveforms that spans 22 channels and 2.7 msec (Sec.
- First, we compared all subsequent datatsets to dataset 1 using recovery rate and accuracy.
- matched units without receptive field information but whose z-distance is smaller than the threshold.Second, we tracked units between consecutive datasets and summarized and analyzed the waveforms, unit locations, firing rates and visual responses (see Figure 5-supplement Figure 1 to Figure 5 for de
- units which can be tracked across at least three consecutive datasets.2.2Measuring rigid drift using the EMDDrift happens mostly along the direction of probe insertion (vertical or z direction).
- We want to estimate the amount of vertical drift under the assumption that part of the drift is rigid; this is likely a good assumption given the small (≈ 720μm) z-range of these recordings.
- For ideal datasets with a few units consistently detected across days, this problem is relatively simple (Figure 2a).
- In the real data analyzed here, we find that only ≈ 60% of units are detected across pairs of days, so the rigid motion of the real pairs must be detected against a background of units with no true match.
- These units with no real match will have z-shifts far from the consensus z-shift of the paired units (Figure 2c).In Figure 2 the EMD match of units from the first dataset (Figure 2b, open circles) to the dataset recorded the next day (Figure 2b, closed circles) is indicated by the arrows between the
- To demonstrate detection of significant drift, we added a 12 micron upward drift to the z-coordinate of the units from the second day.
- The first stage of the EMD is used to find matches using the combined distance metric as described in section 4.1.2.
- We used a kernel fit to the distribution of z-distances of all matched units to find the mode (Mode = 15.65μm); this most probable distance is the estimate of the drift (Figure 2c).
- It is close to the actual imposed drift (di = 12μm).As the EMD is an optimization algorithm with no biological constraints, it assigns matches to all units in the smaller dataset regardless of biophysical plausibility.
- For the illustration in Figure 2, the threshold is set to 15μm, which is chosen to be larger than most of the z-shifts observed in our experimental data.
- The threshold value will be refined later by distribution fitting (Figure 4).
- In Figure 2 all of the sub-threshold (short) distances belong to upward pairs (Figure 2b and c, red solid arrows), showing that the EMD can detect the homogeneous movement direction and the amount of imposed drift.When determining matched reference units from visual response data, we require that un
- After correcting for drift, we find that we recover more reference units (Figure 2-supplement Figure 1), indicating improved spatial match of the two ensembles.
- This improved recovery provides further evidence of the success of the drift correction.2.3A vertical distance threshold is necessary for accurate trackingTo detect the homogeneous z-shift of correct matches against the background of units without true matches, it is necessary to apply a threshold o
- The Receiver Operator Characteristic (ROC) curve in Figure 3 shows the fraction of reference units matched correctly and the number of reference pairs retained as a function of z-distance threshold.
- We want to determine the threshold that maximizes the overall accuracy in the reference units (Figure 3, blue curve) while including as many reference units as possible (Figure 3, red curve).biorxiv;2023.08.03.551724v5/FIG3F3fig3Fig.
- 3:The ROC curve of matching accuracy vs.
- The solid vertical line indicates the average z distance across all reference pairs in all animals (z = 6.96μm).
- The dashed vertical black line indicates a z-distance threshold at z = 10μm.Since reference units only account for 29% of KSgood units (units with few inter-spike-interval violations that are believed to represent a single unit), and the majority of KSgood units did not show a distinguishable visual
- While both distributions may be fit to an exponential decay, the best fit decay constant is significantly different (Kolmogorov-Smirnov test, reject H0, p = 5.5 × 10−31).
- Therefore, the accuracy predicted by the ROC of reference pairs in Figure 3 will not apply to the set of all KSgood pairs.
- To estimate the ROC curve for the set of all KSgood units, we must estimate the z-distance distribution for a mixture of correct and incorrect pairs.biorxiv;2023.08.03.551724v5/FIG4F4fig4Fig.
- 4:Recovery rate, accuracy and putative pairs:a.
- z = 10μm threshold has a false positive rate = 27% for KSgood units.
- The green bars show matching accuracy for the set of pairs with z-distance less than the 10μm threshold.
- Purple bars are the number of putative units (unit with no reference information) inferred with z-threshold = 10μm.We assume that the distribution of z-distances P (Δ) for reference units is the conditional probability P (Δ ∣ H); that is, we assume all reference units are true hits.
- The distance distribution of false positives is the difference between the two.A Monte Carlo simulation determined that the best model for fitting the z-distance distribution of reference units P (Δ ∣ H) is a folded Gaussian distribution (Figure 4a, middle panel) and an exponential distribution for 
- The KSgood distribution is a weighted combination of the folded Gaussian and an exponential:



We fit the KSgood distribution to Equation 3 to extract the individual distribution parameters and the fraction of true hits (f).
- (Figure 4a, bottom panel, see Figure 4-supplement Figure 2 for details).Based on the the estimated false positive rate (Figure 4a, bottom panel), we used a threshold of 10μm (Figure 3, black dotted line) to obtain at least 70% accuracy in the KSgood units.
- We used the same threshold to calculate the number of matched reference units and the corresponding reference unit accuracy (Figure 4b, green bars).Note that this threshold eliminates most of the known false positive matches of reference pairs (Figure 4b, red fraction) at the cost of recovering fewe
- The recovery rate varies from day to day; datasets separated by longer times tend to have higher tracking uncertainty (Figure 4-supplement Figure 3).In addition to the units with visual response data, we can track units which have no significant visual response (Figure 4b, purple bars).
- All comparisons are between subsequent datasets and the day 1 dataset.2.4Units can be tracked in discontinuous recordings for 48 daysTo assess long-term tracking capabilities, we tracked neurons across all datasets for each mouse.
- Figure 5 shows a survival plot of the number of unit chains successfully tracked over all durations.
- There are 133 reference chains, 135 mixed chains and 84 putative chains across all the subjects.
- Among them, 46 reference, 51 mixed, and 9 putative units can be followed across all datasets.
- One example trackable unit in each group is shown in Figure 6, Figure 6-supplement Figure 1, and Figure 6-supplement Figure 2.biorxiv;2023.08.03.551724v5/FIG5F5fig5Fig.
- 5:Number of reference units (deep blue, dark orange and green for different subjects), putative (medium green, medium orange and blue) units, and mixed units (light green, yellow, and light blue) tracked for different durations.
- Note that chains can start on any day in the full set of recordings, so the different sets of neurons have chains with different spans between measurements.biorxiv;2023.08.03.551724v5/FIG6F6fig6Fig.
- Above: Firing rates of this neuron on each day (Day 1, 2, 13, 23, 48).
- In order to check for differences among the three groups, we analyzed the locations, firing rates, waveforms, and receptive fields of the fully trackable units in the three groups: reference, putative, and mixed.The spatial-temporal waveform similarity is measured by the L2 distance between waveform
- A Kruskal-Wallis test is performed on the magnitude of L2 change between all pairs of matched waveforms among the three groups.
- There is no statistical difference in the waveform similarity in reference, putative, and mixed units (H = 0.59, p = 0.75) (Figure 5-supplement Figure 1).
- There is no significant difference in the physical distances of units per dataset (H = 1.31, p = 0.52) (Figure 5-supplement Figure 2, bottom panel), nor in the location change of units (H = 0.23, p = 0.89) (Figure 5-supplement Figure 2, top panel).Firing rate is characterized as the average firing r
- There is no difference in the firing rate fold change in the three groups of units (H = 1, p = 0.6) (Figure 5- supplement Figure 3).The receptive field similarity between units in different datasets is described by visual finger-print (vfp) correlation and Peristimulus Time Histogram (PSTH) correlat
- The change in vfp between matched units is similar among the three groups (H = 2.23, p = 0.33).
- Similarly, the change in PSTH is not different among the three groups (H = 1.61, p = 0.45) (Figure 5-supplementFigure 4).

## Figure Descriptions

### Fig. 1:
Schematic depiction of drift:a. Mice were implanted with a 4-shank Neuropixels 2.0 probe in visual cortex area V1. b. Each colored star represents the location of a unit recorded on the probe. In this hypothetical case, the same color indicates unit correspondence across days. The black unit is miss

### Fig. 2:
The EMD can detect the displacement of single units:a. Schematic of EMD unit matching. Each blue unit in day 1 is matched to a red unit in day 2. Dashed lines indicate the matches to be found by minimizing the weighted sum of physical and waveform distances. b. Open and filled circles show positions

### Fig. 3:
The ROC curve of matching accuracy vs. distance.The blue curve shows the accuracy for reference units. The red line indicates the number of reference units included. The solid vertical line indicates the average z distance across all reference pairs in all animals (z = 6.96μm). The dashed vertical b

### Fig. 4:
Recovery rate, accuracy and putative pairs:a. The histogram distribution fit for all KS-good units (top) and reference units alone (middle). False positives for reference units are defined as units matched by EMD but not matched when using receptive fields. The false positive fraction for the set of

### Fig. 5:
Number of reference units (deep blue, dark orange and green for different subjects), putative (medium green, medium orange and blue) units, and mixed units (light green, yellow, and light blue) tracked for different durations. The loss rate is similar for different chain types in the same subject. N

### Fig. 6:
Example mixed chain:a. Above: Firing rates of this neuron on each day (Day 1, 2, 13, 23, 48). Below: Firing rate fractional change compared to the previous day. b. Visual response similarity (yellow line), PSTH correlation (orange line), and visual fingerprint correlation (blue line). The similarity

### Fig. 7:
Summary of dataset: a. The recording intervals for each animal. A black dash indicates one recording on that day. b. All recordings are from visual cortex V1 with a 720 μm section of the probe containing 96 recording sites. The blue arrow indicates the main drift direction. c. Examples of visual fin

### 


### 


### Figure 2 - figure supplement 1:
The effect of drift correction on reference units yield for all three animals. Note that drift correction improves the recovery rate for most cases; the degree of improvement is a function of the magnitude of the drift.

### Figure 2 - figure supplement 2:
EMD cost can be used to detect discontinuities in the data. In animal AL036, we noted a large decrease in the number of reference units (units with matched visual responses, see Sec. 4.4) after the second dataset. This likely indicates a large physical shift in the tissue relative to the probe. It i

### Figure 2 - figure supplement 3:
The normalized EMD cost (unitless), z distance (μm), physical distance (μm), and waveform distance (unitless) and the corresponding recovery rate of reference unit (units with matched visual responses) in pairwise matches of all to all pairs of recordings, on each shank. Each triangle represents the

### Figure 2 - figure supplement 4:
Recovery rate vs. L2-weight. We varied the weight ω in Equation 4 used to combine the physical and waveform distances in increments of 500. The vertical line indicates weight = 1500, where the overall recovery rate = 86.29%. The maximum recovery rate = 87.68% occurs at weight = 3000. We chose weight

### Figure 4 - figure supplement 1:
Determining the functional form for the z-distance distribution of all pairs. As shown in Figure 4a, the z distance distribution of reference pairs differs significantly from that of all pairs. The z-distance distribution for all pairs is the sum of z-distance distributions for true hits (P (Δ ∣ H))

### Figure 4 - figure supplement 2:
Fits of experimental z-distance distributions to the model. When reference data is available, the z-distance distribution of these known true hits can be fit to obtain the width σ of the folded Gaussian. σ can then be fixed in the fit of the distribution of all KSgood units to Equation 3, which is u

### Figure 4 - figure supplement 3:
The reference unit recovery rate vs. days between matched recordings. Each triangle represents the matching results of two datasets. Animal AL031 has 6 sets of matched units, with one outlier removed. Animal AL032 has 24 sets of matched units. Animal AL036 has 60 sets of matching. The recovery rate 

### Figure 5 - figure supplement 1:
Distribution of waveform L2 similarity change per dataset for each neuron group (reference, putative and mixed) and across all neurons. Box plots indicate 25% percentile, medians, and 75% percentile. Whiskers at the ends of the box plot show maximum and minimum values. n and N are the number of unit

### Figure 5 - figure supplement 2:
Distributions of individual unit location changes over whole chains (top) and unit location changes between pairs of datasets (bottom), for each neuron group and across all neurons. Box plots indicate 25% percentile, medians, and 75% percentile. Whiskers at the ends of the box plot show maximum and 

### Figure 5 - figure supplement 3:
Distribution of firing rate fold change per dataset for each neuron group and across all neurons. Box plots indicate 25% percentile, medians, and 75% percentile. Whiskers at the ends of the box plot show maximum and minimum values. n and N are the number of units. A Kruskal-Wallis test indicates no 

### Figure 5 - figure supplement 4:
The visual fingerprint and PSTH change distributions per dataset for each neuron group and across all neurons. Box plots indicate 25% percentile, medians, and 75% percentile. Whiskers at the ends of the box plot show maximum and minimum values. n and N are the number of unit comparisons, i.e. (numbe

### Figure 5 - figure supplement 5:
The similarity score distribution per dataset for each neuron group and across all neurons. Box plots indicate 25% percentile, medians, and 75% percentile. Whiskers at the ends of the box plot show maximum and minimum values. n and N are the number of observations of the units, i.e. ∑units (observat

### Figure 6 - figure supplement 1:
Example reference chain. a. Above: Firing rates of this neuron on each day. Below: Firing rate fractional change compared to the previous day. b. Visual response similarity (yellow line), PSTH correlation (orange line), and visual fingerprint correlation (blue line). The similarity score is the sum 

### Figure 6 - figure supplement 2:
Example putative chain. Order is the same as the previous figure.

### Figure 7 - figure supplement 1:
An example similarity score (vfp + PSTH) heatmap from animal AL032, shank 2, Kilosort-good units between day 1 and 2. Each small square represents the similarity score (value range from [-2,2]) between one unit from day 1 and one unit from day 2. A warm colored square indicates a higher score. The c

### Figure 7 - figure supplement 2:
The Kilosort-good and reference unit counts for the animals AL031 and AL036, as shown for animal AL032 in Figure 7.

### Figure 7 - figure supplement 3:
The ratio of the count of reference units to KSgood units decreases for pairs of datasets with larger time intervals. However, the variability of the number of reference units is generally large for all time intervals.

## References
Total references in published paper: 31

### Key References (from published paper)
- Stable Ensemble Performance with Single-Neuron Variability during Reaching Movements in Primates (, 2005)
- Multiple dynamic representations in the motor cortex during sensorimotor learning (, 2012)
- Unstable neurons underlie a stable learned behavior (, 2016)
- Variance and invariance of neuronal long-term representations (, 2017)
- Automated long-term recording and analysis of neural activity in behaving animals (, 2017)
- Long-term stability of single neuron activity in the motor system (, 2022)
- Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings (, 2021)
- An approach for long-term, multi-probe Neuropixels recordings in unrestrained rats (, 2020)
- Improving data quality in neuronal population recordings (, 2016)
- Large-scale recording of neuronal ensembles (, 2004)
- Multiple neural spike train data analysis: state-of-the-art and future challenges (, 2004)
- Extracting information from neuronal populations: information theory and decoding approaches (, 2009)
- Neural signatures of cell assembly organization (, 2005)
- Unsupervised Spike Detection and Sorting with Wavelets and Superparamagnetic Clustering (, 2004)
- Automated spike sorting algorithmbased on Laplacian eigenmaps and k-means clustering (, 2011)
- Continuing progress of spike sorting in the era of big data (, 2019)
- Fully integrated silicon probes for high-density recording of neural activity (, 2017)
- Evaluation and resolution of many challenges of neural spike sorting: a new sorter (, 2021)
- Recording Chronically From the Same Neurons in Awake, Behaving Primates (, 2007)
- Spike sorting for polytrodes: a divide and conquer approach (, 2014)
- Spike sorting: Bayesian clustering of non-stationary data (, 2006)
- A Fully Automated Approach to Spike Sorting (, 2017)
- High-Density, Long-Lasting, and Multiregion Electrophysiological Recordings Using Polymer Electrode  (, 2019)
- Long-Term Recording of Single Neurons and Criteria for Assessment (, 2016)
- Motor Learning with Unstable Neural Representations (, 2007)
- A review of methods for spike sorting: the detection and classification of neural action potentials  (, 1998)
- ecephys spike sorting (, )
- Efficient Tracking of Sparse Signals via an Earth Mover’s Distance Dynamics Regularizer (, 2020)
- Three-dimensional spike localization and improved motion correction for Neuropixels recordings (, 2021)
- Cortical pattern generation during dexterous movement is input-driven (, 2020)

## Ground Truth Reference
- Figures: 26
- Tables: 0
- References: 31