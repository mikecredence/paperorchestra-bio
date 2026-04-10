## Working title

osl-dynamics, a toolbox for modeling fast dynamic brain activity

## Core question

How can we provide a unified, accessible computational framework for identifying and characterizing recurrent dynamic brain states from multimodal neurophysiological recordings on timescales as fast as tens of milliseconds?

## Motivation / gap

- Brain activity is fundamentally dynamic, with oscillatory bursts and network reconfigurations occurring on timescales of tens of milliseconds, but existing tools for studying such fast dynamics are fragmented and difficult to use
- Hidden Markov Models (HMMs) and newer deep learning approaches for dynamic brain state modeling lack a unified software implementation with standardized preprocessing, inference, and post-hoc analysis pipelines
- Current approaches require substantial methodological expertise, limiting adoption by the broader neuroscience community
- There is no single toolbox that handles the full pipeline from raw MEG/EEG data through dynamic network analysis with both classical (HMM) and modern (variational autoencoder) generative models

## Core contribution (bullet form)

- Present osl-dynamics, an open-source Python toolbox for modeling fast dynamic brain activity across multiple neuroimaging modalities (MEG, EEG, fMRI, LFP, ECoG)
- Implement time-delay embedded Hidden Markov Model (TDE-HMM) for discovering discrete dynamic brain states with spectral and spatial characteristics
- Introduce Dynamic Network Modes (DyNeMo), a deep learning generative model using variational autoencoders that allows overlapping/simultaneous activation of multiple dynamic modes
- Provide end-to-end pipelines including source reconstruction, sign-flipping, dynamic modeling, and comprehensive post-hoc spectral and connectivity analysis
- Demonstrate the toolbox on resting-state and task MEG data, showing data-driven oscillatory burst detection and dynamic network state identification

## Method in brief

The toolbox centers on two generative models: (1) TDE-HMM, which models brain dynamics as a sequence of discrete hidden states with multivariate normal observation distributions in a time-delay embedded space, capturing both amplitude and phase dynamics; (2) DyNeMo, which uses a variational autoencoder with a recurrent neural network to infer a continuous mixture of dynamic modes that can overlap in time. Both models learn the number, timing, spectral properties, and spatial topographies of dynamic brain states in a data-driven manner within a Bayesian framework. The toolbox includes preprocessing (source reconstruction, parcellation, sign-flipping), model training (expectation-maximization for HMM, stochastic variational inference for DyNeMo), and post-hoc analysis (multitaper spectral estimation, power and coherence maps, summary statistics of state dynamics). Demonstrated on CTF resting-state MEG and Elekta task MEG datasets.

## Target venue

eLife
