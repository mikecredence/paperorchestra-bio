# Idea Summary

## Working title
RatInABox: A Toolkit for Modelling Locomotion and Neuronal Activity in Continuous Environments

## Core question
Can a lightweight, open-source Python toolkit provide researchers with standardized, physically realistic locomotory and neural data generation for spatial navigation studies, eliminating the need to reinvent this infrastructure for each project?

## Motivation / gap
- Generating synthetic locomotory and neural data is a cumbersome but necessary step for studying theoretical models of hippocampal navigation
- No universal standard exists for trajectory and cell activity modeling, making cross-study comparison difficult
- Researchers must rewrite motion and neural data generation code from scratch for each project
- Existing approaches are either discrete (gridworld/MDP), use cached precomputed rate maps on discretized grids, or focus on biophysical detail rather than higher-level representations
- Inefficiently written software can become a computational bottleneck, pushing researchers toward unnecessarily complex solutions (GPUs, multithreading)

## Core contribution (bullet form)
- Released RatInABox, an open-source Python toolkit with three core classes (Environment, Agent, Neurons) for simulating locomotion and neural data in continuous 1D and 2D environments
- Validated the random motion model against real rodent data from the Sargolini et al. dataset, replicating velocity statistics (Rayleigh-distributed linear velocity, Gaussian rotational velocity) and thigmotaxis (wall-hugging) behavior
- Achieved computational efficiency: 100 PlaceCells for 10 min of random 2D motion (dt = 0.1 s) in ~2 seconds on a consumer CPU; BoundaryVectorCells slower but still outpace typical downstream operations
- Demonstrated scaling: combined Agent + PlaceCell update time is O(1) for small populations (n < 1000, dominated by motion model) and O(n) for large populations
- Provided premade neuron models for place cells, grid cells, boundary vector cells, head direction cells, and speed cells, plus framework for custom cell types and multi-layer networks
- Included tutorial scripts for position decoding from neural data (Gaussian Process regression with 20 cells) and navigational reinforcement learning (TD learning)

## Method in brief
RatInABox operates through three composable classes. The Environment class defines 1D or 2D spaces with configurable walls, barriers, holes, objects (visual cues), and periodic or solid boundary conditions. The Agent class implements a temporally continuous smooth random motion model fitted to experimental rodent locomotion data, with parameters for mean/std of speed and rotational velocity, plus a single thigmotaxis parameter controlling wall-exploration bias. The Neurons class provides subclasses for known cell types (PlaceCells, GridCells, BoundaryVectorCells, HeadDirectionCells) with online firing rate calculation based on continuous agent state, plus Poisson spike sampling.

A typical workflow initializes Environment, Agent, and Neuron populations with specified parameters, then iterates through time steps where the Agent updates its position/velocity and Neurons update firing rates. All data (timestamps, positions, velocities, rates, spikes) are saved for analysis. The motion model parameters were fitted to match statistics from the Sargolini et al. dataset: Rayleigh-distributed linear velocity with exponential temporal autocorrelation, and Gaussian rotational velocity. The toolkit also supports imported trajectory data with cubic spline interpolation for upsampling, policy-controlled motion for reinforcement learning applications, and FeedForwardLayer neurons for custom architectures.

## Target venue
eLife
