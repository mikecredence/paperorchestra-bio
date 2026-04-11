# Experimental Log: RatInABox: A toolkit for modelling locomotion and neuronal activity in continuous environments

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 3Demonstration and ResultsThe default parameters of the random motion model in RatInABox are matched to observed statistics of rodent locomotion, extracted by reanalysing data from Sargolini et al.
- 2a) closely compare to the artificially generated trajectories from RatInABox (Fig.
- Further, data[32] shows that rodents have a tendency to over-explore walls and corners, a bias often called “thigmotaxis” which is particularly pronounced when the animal is new to the environment (Fig.
- 2d & e).RatInABox can import and smoothly interpolate user-provided trajectory data.
- 3a where a low-resolution trajectory is imported into RatInABox and smoothly upsampled using cubic spline interpolation.
- Note that without upsampling, this data (2 Hz) would be far too low in temporal-resolution to usefully simulate neural activity.
- 3a & 2a is uploaded with permission to the GitHub repository and can be imported using Agent.import_trajectory(dataset=“sargolini”).
- [35].RatInABox is computationally efficient.
- 3f, purple bars) to typical non-RatInABox operations representing potential ‘bottlenecking’ operations in a downstream analysis or model-training procedure for which RatInABox is providing data (Fig.
- These were multiplying a matrix by a vector using the numpy[36] package and a forward and backward pass through a small feedforward artificial neural network using the pytorch package[37].
- BoundaryVectorCells (because they require integrating around a 360° field-of-view) are significantly slower than the other cells but still outpace the feedforward neural network.
- All vector, matrix, and cell populations were size n = 100, the feed forward network had layer sizes nL = (100, 1000, 1000, 1), the Environment was 2D with no additional walls and all operations were calculated on a consumer-grade CPU (MacBook Pro, Apple M1).
- 3f, inset) reveals that the combined time for updating the motion model and a population of PlaceCells scales sublinearly O(1) for small populations n > 1000 where updating the random motion model dominates compute time, and linearly for large populations n > 1000.
- 1D simulations are significantly quicker than 2D simulations due to the reduced computational load of the 1D geometry.3.1Case studiesWe envisage RatInABox being used to support a range of theoretical studies by providing data and, if necessary, infrastructure for building models powered by this data
- Data – the location and firing rate trajectories of an Agent randomly exploring a 2D Environment – are generated using RatInABox.
- 3e).Additional tutorials, not described here but available online, demonstrate how RatInABox can be used to model splitter cells, conjunctive grid cells, biologically plausible path integration, successor features, deep actor-critic RL, whisker cells and more.

## Tables

### Table S1:
> Default values, keys and allowed ranges for RatInABox parameters. ∗ This parameter is passed as a kwarg to Agent.update() function, not in the input dictionary. ∗∗ This parameter is passed as a kwarg 


## Figure Descriptions

### Figure 1:
RatInABox is a flexible toolkit for simulating locomotion and neural data in complex continuous environments. (a) One minute of motion in a 2D Environment with a wall. By default the Agent follows a physically realistic random motion model fitted to experimental data. (b) Premade neuron models inclu

### Figure 2:
The RatInABox random motion model closely matches features of real rat locomotion. (a) An example 5 minute trajectory from the Sargolini et al. [10] dataset. Linear velocity (Rayleigh fit) and rotational velocity (Gaussian fit) histograms and the temporal autocorrelations (exponential fit) of their 

### Figure 3:
Advanced features and computational efficiency analysis. (a) Low temporal-resolution trajectory data (2 Hz) imported into RatInABox is upsampled (“augmented”) using cubic spline interpolation. The resulting trajectory is a close match to the ground truth trajectory (Sargolini et al. [10]) from which

### 


### 


### Figure S1:
RatInABox used for a simple neural decoding experiment. (a) Training (5 min) and testing (1 min) trajectories are sampled in a 1 m square environment containing a small barrier. (b) The firing rates of a population of Ncells = 20 cells, taken over the training trajectory, are used to fit a Gaussian 

### Figure S2:
RatInABox used in a simple reinforcement learning project. (a) A schematic of the 1 layer linear network. Using a simple model-free policy iteration algorithm the Agent, initially moving under a random motion policy, learns to approach an optimal policy for finding a reward behind a wall. The policy

## References
Total references in published paper: 41

### Key References (from published paper)
- A quantitative description of membrane current and its application to conduction and excitation in n (, 1952)
- Quantal components of the end-plate potential (, 1954)
- Modeling place fields in terms of the cortical inputs to the hippocampus (, 2000)
- Geometric determinants of human spatial memory (, 2004)
- Remembering the past and imagining the future: A neural model of spatial memory and imagery (, 2007)
- Vector-based navigation using grid-like representations in artificial agents (, 2018)
- Predictive maps in rats and humans for spatial navigation (, 2022)
- Introduction and removal of reward, and maze performance in rats (, 1930)
- The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat (, 1971)
- Conjunctive Representation of Position, Direction, and Velocity in Entorhinal Cortex (, 2006)
- Speed cells in the medial entorhinal cortex (, 2015)
- Head-direction cells recorded from the postsubiculum in freely moving rats. I. Description and quant (, 1990)
- Experience-dependent asymmetric shape of hippocampal receptive fields (, 2000)
- Accurate Path Integration in Continuous Attractor Network Models of Grid Cells (, 2009)
- Grid cells, place cells, and geodesic generalization for spatial reinforcement learning (, 2011)
- The hippocampus as a predictive map (, 2017)
- Neurobiological successor features for spatial navigation (, 2020)
- Rapid learning of predictive maps with STDP and theta phase precession (, 2022)
- No free lunch from deep learning in neuroscience: A case study through models of the entorhinal-hipp (, 2022)
- Place cells may simply be memory cells: Memory compression leads to spatial tuning and history depen (, 2021)
- Minigrid & miniworld: Modular & customizable reinforcement learning environments for goal-oriented t (, 2023)
- Neuro-Nav: A Library for Neurally-Plausible Reinforcement Learning (, 2022)
- A generative model of the hippocampal formation trained with theta driven local learning rules (, 2023)
- Geometric determinants of the place fields of hippocampal neurons (, 1996)
- The Boundary Vector Cell Model of Place Cell Firing and Spatial Memory (, 2006)
- Representation of Geometric Borders in the Entorhinal Cortex (, 2008)
- Modeling Boundary Vector Cell Firing Given Optic Flow as a Cue (, 2012)
- Place cells may simply be memory cells: Memory compression leads to spatial tuning and history depen (, 2021)
- ERK2 contributes to the control of social behaviors in mice (, 2011)
- Phase relationship between hippocampal place units and the EEG theta rhythm (, 1993)

## Ground Truth Reference
- Figures: 7
- Tables: 1
- References: 41