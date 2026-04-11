# Idea Summary: RatInABox: A toolkit for modelling locomotion and neuronal activity in continuous environments

## Working title
RatInABox: A toolkit for modelling locomotion and neuronal activity in continuous environments

## Core question
ABSTRACTGenerating synthetic locomotory and neural data is a useful yet cumbersome step commonly required to study theoretical models of the brain’s role in spatial navigation. This process can be time consuming and, without a common framework, makes it difficult to reproduce or compare studies which each generate test data in different ways. In response we present RatInABox, an open-source Python toolkit designed to model realistic rodent locomotion and generate synthetic neural data from spati

## Motivation / gap
- 1.IntroductionComputational modelling provides a means to understand how neural circuits represent the world and influence behaviour, interfacing between experiment and theory to express and test how 
- Such models have been central to understanding a range of neural mechanisms, from action potentials [1] and synaptic transmission between neurons [2], to how neurons represent space and guide complex 
- Relative to empirical approaches, models can offer considerable advantages, providing a means to generate large amounts of data quickly with limited physical resources, and are a precise means to test
- To fully realise these benefits, computational modelling must be accessible and standardised, something which has not always been the case.Spurred on by the proposition of a “cognitive map”[8], and th
- In this field it is common for theoretical or computational models to rely on artificially generated data sets.

## Core contribution (bullet form)
Extracted from abstract:
ABSTRACTGenerating synthetic locomotory and neural data is a useful yet cumbersome step commonly required to study theoretical models of the brain’s role in spatial navigation. This process can be time consuming and, without a common framework, makes it difficult to reproduce or compare studies which each generate test data in different ways. In response we present RatInABox, an open-source Python toolkit designed to model realistic rodent locomotion and generate synthetic neural data from spatially modulated cell types. This software provides users with (i) the ability to construct one-or two-dimensional environments with configurable barriers and visual cues, (ii) a physically realistic random motion model fitted to experimental data, (iii) rapid online calculation of neural data for many of the known self-location or velocity selective cell types in the hippocampal formation (including place cells, grid cells, boundary vector cells, head direction cells) and (iv) a framework for constructing custom cell types, multi-layer network models and data-or policy-controlled motion trajectories. The motion and neural models spatially and temporally continuous as well as topographically sensitive to boundary conditions and walls. We demonstrate that out-of-the-box parameter settings replicate many aspects of rodent foraging behaviour such as velocity statistics and the tendency of rodents to over-explore walls. Numerous tutorial scripts are provided, including examples where RatInABox is used for decoding position from neural data or to solve a navigational reinforcement learning task. We hope this tool significantly streamline computational research into the brain’s role in navigation.

## Method in brief
Methods not available from XML.

## Target venue
eLife
