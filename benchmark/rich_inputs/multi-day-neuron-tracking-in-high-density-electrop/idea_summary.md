# Idea Summary: Multi-day Neuron Tracking in High Density Electrophysiology Recordings using EMD

## Working title
Multi-day Neuron Tracking in High Density Electrophysiology Recordings using EMD

## Core question
AbstractAccurate tracking of the same neurons across multiple days is crucial for studying changes in neuronal activity during learning and adaptation. Advances in high density extracellular electrophysiology recording probes, such as Neuropixels, provide a promising avenue to accomplish this goal. Identifying the same neurons in multiple recordings is, however, complicated by non-rigid movement of the tissue relative to the recording sites (drift) and loss of signal from some neurons. Here we p

## Motivation / gap
- 1IntroductionThe ability to longitudinally track neural activity is crucial to understanding central capabilities and changes of neural circuits that operate on long time-scales, such as learning and 
- We seek to develop a method capable of tracking single units regardless of changes in functional responses for the duration of an experiment spanning one to two months.High-density multi-channel extra
- Examples include perceptual decision making, exploration and navigation.8–13 Electrode arrays with hundreds to thousands of sites, for example Neuropixels, are now used extensively to record the neura
- Spike sorting identifies individual neurons by grouping detected action potentials using waveform profiles and amplitudes.
- Specific algorithms include principal components based methods,14,15 and template matching methods, for example, Kilosort.9, 11, 16, 17 Due to the high dimensional nature of the data, spike sorting is

## Core contribution (bullet form)
Extracted from abstract:
AbstractAccurate tracking of the same neurons across multiple days is crucial for studying changes in neuronal activity during learning and adaptation. Advances in high density extracellular electrophysiology recording probes, such as Neuropixels, provide a promising avenue to accomplish this goal. Identifying the same neurons in multiple recordings is, however, complicated by non-rigid movement of the tissue relative to the recording sites (drift) and loss of signal from some neurons. Here we propose a neuron tracking method that can identify the same cells independent of firing statistics, that are used by most existing methods. Our method is based on between-day non-rigid alignment of spike sorted clusters. We verified the same cell identity in mice using measured visual receptive fields. This method succeeds on datasets separated from one to 47 days, with an 84% average recovery rate.

## Method in brief
4MethodsOur neuron tracking algorithm uses the Earth Mover’s Distance (EMD) optimization algorithm. The minimized distance is a weighted combination of physical distance and ‘waveform distance’: the algorithm seeks to form pairs that are closest in space and have the most similar waveforms. We test the performance of the algorithm by comparing EMD matches to reference pairs determined from visual receptive fields (Sec. 4.4). We calculate two performance metrics. The ‘recovery rate’ is the percentage of reference units that are correctly matched by the EMD procedure. The ‘accuracy’ is the percentage of correctly matched reference units that pass the z-distance threshold (Figure 4a). ‘Putative units’ are units matched by the procedure which do not have reference receptive field information. ‘Chains’ are units that can be tracked across at least three consecutive datasets. The full procedure is summarized in Algorithm 1.Algorithm 1Neuron Matching Procedurebiorxiv;2023.08.03.551724v5/ALG1AF8alg1a4.1Algorithm4.1.1Earth Mover’s DistanceThe EMD is an optimization-based metric developed in the context of optimal transport and measuring distances between probability distributions. It frames the question as moving dirt, in our case, units from the first dataset, into holes, which here are the neural units in the second dataset. The distance between the “dirt” and the “holes” determines how the optimization program will prioritize a given match. Specifically, the EMD seeks to minimize t

## Target venue
eLife
