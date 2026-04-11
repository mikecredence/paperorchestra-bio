# Idea Summary: Criticality and partial synchronization analysis in Wilson-Cowan and Jansen-Rit neural mass models

## Working title
Criticality and partial synchronization analysis in Wilson-Cowan and Jansen-Rit neural mass models

## Core question
AbstractSynchronization is a phenomenon observed in neuronal networks involved in diverse brain activities. Neural mass models such as Wilson-Cowan (WC) and Jansen-Rit (JR) manifest synchronized states. Although they have been studied for decades, their ability to demonstrate second-order phase transition (SOPT) and criticality has not received enough attention, which serves as candidates for the development of healthy brain networks. In this study, two networks of coupled WC and JR nodes with s

## Motivation / gap
- 1IntroductionThe dynamics of macroscopic and mesoscopic brain activity is a challenging topic.
- The large-scale model activities can be complex and include a range of behaviors such as spiking and oscillatory, resting-state, chaotic, and periodic or nonperiodic activities [1, 2].
- The neural mass models which are based on the mesoscopic scale, describe the action of neural populations rather than the behavior of spiking neurons and have been used broadly in modeling some brain 
- These models depend on their output (voltage or rate) and are classified into two voltage- and activity-based models [6].
- The first voltage-based model in respect of one excitatory and one inhibitory ensemble was built by Lopes da Silva [7].

## Core contribution (bullet form)
Extracted from abstract:
AbstractSynchronization is a phenomenon observed in neuronal networks involved in diverse brain activities. Neural mass models such as Wilson-Cowan (WC) and Jansen-Rit (JR) manifest synchronized states. Although they have been studied for decades, their ability to demonstrate second-order phase transition (SOPT) and criticality has not received enough attention, which serves as candidates for the development of healthy brain networks. In this study, two networks of coupled WC and JR nodes with small-world topologies were constructed and Kuramoto order parameter (KOP) was used to quantify the amount of synchronization. In addition, we investigated the presence of SOPT using the synchronization coefficient of variation. Both networks reached high synchrony by changing the coupling weight between their nodes. Moreover, they exhibited abrupt changes in the synchronization at certain values of the control parameter not necessarily related to a phase transition. While SOPT was observed only in JR model, neither WC nor JR model showed power-law behavior. Our study further investigated the global synchronization phenomenon that is known to exist in pathological brain states, such as seizure. JR model showed global synchronization, while WC model seemed to be more suitable in producing partially synchronized patterns.Corresponding author summaryYousef Jamali received his M.Sc. degree in physics from Sharif University, Tehran, Iran, in 2004, and his Ph.D. degree in physics from Sharif University, Tehran, Iran, in 2009. After finishing his Ph.D. thesis, in 2009, he got two years postdoctoral research associate position at the University of California at Berkeley, Department of Bioengineering. He is currently an Associate Professor in the Applied Mathematics Department (Biomathematics division), at Tarbiat Modares University, Tehran, Iran. His current research interests include the interdisciplinary area of the complex system especially on the modeling of brain. In fact, his interests are how the brain works at the critical state and how this complex system synchronized under different conditions.

## Method in brief
2Methods2.1Wilson-Cowan modelThe classical WC model describes the dynamics of firing rates among neural populations in the brain [10, 46]. The activity of each neural population is computed as the mean firing rate of its excitatory (E) and inhibitory (I) subpopulations by using mean-field approximation. The temporal evolution of the excitatory and inhibitory firing rates, E(t) and I(t), respectively, is governed by the following differential equations [10]:



where τE (τI) shows the time constant for excitatory (inhibitory) populations. The sigmoid function 𝒮 introduces the thresholds θE and θI corresponding to the maximum slope values and can be different for excitatory and inhibitory subpopulations. Moreover, the slopes of the sigmoids are given by aE and aI . 𝒮 is given as follows:



The synaptic weights are determined by the connectivity coefficients cEE, cEI, cIE, and cII . P (t) represents the external stimuli acting on excitatory subpopulation in time t.Depending on parameter settings, specifically on the selection of the external input P(t), the dynamics of this dynamical system ranges from fixed-point relaxations to limit cycle oscillations. Table 1 shows the values of parameters with their interpretations, which can produce oscillatory behavior in the WC model.biorxiv;2023.10.03.560644v1/TBL1T1tbl1Table 1.Parameters in the WC model that shows the oscillatory behavior used in this study.In a network with N nodes, i = 1,…, N, the WC equations are as follows:



wher

## Target venue
PLOS ONE
