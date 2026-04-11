# Idea Summary: A deep learning framework for automated and generalized synaptic event analysis

## Working title
A deep learning framework for automated and generalized synaptic event analysis

## Core question
ABSTRACTQuantitative information about synaptic transmission is key to our understanding of neural function. Spontaneously occurring synaptic events carry fundamental information about synaptic function and plasticity. However, their stochastic nature and low signal-to-noise ratio present major challenges for the reliable and consistent analysis. Here, we introduce miniML, a supervised deep learning- based method for accurate classification and automated detection of spontaneous synaptic events.

## Motivation / gap
- INTRODUCTIONSynaptic communication serves as the fundamental basis for a wide spectrum of brain functions, from computa- tion and sensory integration to learning and memory.
- Synaptic transmission either arises from spontaneous or action potential-evoked fusion of neurotransmitter-filled synaptic vesicles (Kaeser and Regehr, 2014) resulting in an electrical response in the
- Such synaptic events are a salient feature of all neural circuits and can be recorded using electrophysiological or imaging techniques.Random fluctuations in the release machinery or intracellular Ca2
- Measurements of amplitude, kinetics, and timing of these events provide essential information about the function of individual synapses and neural circuits.
- Miniature events are therefore key to our understanding of fundamental processes, such as synaptic plasticity or synaptic computation that support neural function (Abbott and Regehr, 2004; Holler et a

## Core contribution (bullet form)
Extracted from abstract:
ABSTRACTQuantitative information about synaptic transmission is key to our understanding of neural function. Spontaneously occurring synaptic events carry fundamental information about synaptic function and plasticity. However, their stochastic nature and low signal-to-noise ratio present major challenges for the reliable and consistent analysis. Here, we introduce miniML, a supervised deep learning- based method for accurate classification and automated detection of spontaneous synaptic events. Comparative analysis using simulated ground-truth data shows that miniML outperforms existing event analysis methods in terms of both precision and recall. miniML enables precise detection and quantification of synaptic events in electrophysiological recordings. We demonstrate that the deep learning approach generalizes easily to diverse synaptic preparations, different electrophysiological and optical recording techniques, and across animal species. miniML provides not only a comprehensive and robust framework for automated, reliable, and standardized analysis of synaptic events, but also opens new avenues for high-throughput investigations of neural function and dysfunction.

## Method in brief
MATERIALS AND METHODSElectrophysiological recordingsAnimals were treated according to national and institutional guidelines. All experiments were approved by the Cantonal Veterinary Office of Zurich (approval number no. ZH206/2016 and ZH009/2020). Experiments were performed in male and female C57BL/6J mice (Janvier Labs, France). Mice were 1–5-months-old, but for recordings from the Calyx of Held, which were performed in P9 animals. Animals were housed in groups of 3–5 in standard cages under a 12h-light/12h-dark cycle with food and water ad libitum. Mice were sacrificed by rapid decapitation after isoflurane anesthesia. The cerebellar vermis was quickly removed and mounted in a chamber filled with chilled extracellular solution. Parasagittal 300-µm thick slices were cut with a Leica VT1200S vibratome (Leica Microsystems, Germany), transferred to an incubation chamber at 35 °C for 30 minutes, and then stored at room temperature until experiments. The extracellular solution (artificial cerebrospinal fluid, ACSF) for slicing and storage contained (in mM): 125 NaCl, 25 NaHCO3, 20 D-glucose, 2.5 KCl, 2 CaCl2, 1.25 NaH2PO4, 1 MgCl2, aerated with 95% O2 and 5% CO2.Slices were visualized using an upright microscope with a 60×, 1 NA water immersion objective, infrared optics, and differential interference contrast (Scientifica, UK). The recording chamber was continuously perfused with ACSF. For event-free recordings, we blocked excitatory and inhibitory transmission using ACSF supple

## Target venue
eLife
