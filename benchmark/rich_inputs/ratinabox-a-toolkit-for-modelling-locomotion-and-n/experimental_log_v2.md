# Experimental Log

> Pre-writing data tables and observations for the RatInABox toolkit.

---

## Software Architecture

| Class | Role | Key Parameters |
|-------|------|---------------|
| Environment | Define spatial arena | Dimensionality (1D/2D), size, shape, boundary conditions, walls, holes, objects |
| Agent | Simulate locomotion | Speed mean/std, rotational velocity mean/std, thigmotaxis, dt |
| Neurons | Generate neural data | Cell type, number of cells, receptive field parameters, max firing rates |
| FeedForwardLayer | Custom multi-layer networks | Input layers, weights, activation functions |

---

## Premade Cell Types

| Cell Type | Description | Continuous? | Topography-Sensitive? |
|-----------|-------------|------------|---------------------|
| PlaceCells | Location-selective firing fields | Yes | Yes (walls affect fields) |
| GridCells | Hexagonal periodic firing fields | Yes | Yes |
| BoundaryVectorCells | Distance-to-boundary selective | Yes | Yes (360 degree field integration) |
| HeadDirectionCells | Directional tuning | Yes | N/A |
| SpeedCells | Velocity-modulated | Yes | N/A |
| FeedForwardLayer | Arbitrary function approximator | Yes | Depends on inputs |

---

## Experiment 1: Motion Model Validation Against Real Data

Reference dataset: Sargolini et al. rodent locomotion recordings.

| Statistic | Real Data (Sargolini) | RatInABox | Fit Type |
|-----------|----------------------|-----------|----------|
| Linear velocity distribution | Rayleigh | Rayleigh (matched) | Rayleigh fit |
| Rotational velocity distribution | Gaussian | Gaussian (matched) | Gaussian fit |
| Linear velocity temporal autocorrelation | Exponential decay | Exponential decay (matched) | Exponential fit |
| Rotational velocity temporal autocorrelation | Exponential decay | Exponential decay (matched) | Exponential fit |

Fig. 2a: 5-minute real trajectory with velocity histograms and autocorrelation functions.
Fig. 2b: 5-minute RatInABox trajectory with matched statistics.

---

## Experiment 2: Thigmotaxis (Wall-Exploration Bias)

| Condition | Wall Exploration Bias | Reference |
|-----------|---------------------|-----------|
| Real rodent (new to environment) | Pronounced wall preference | Satoh et al. data |
| RatInABox (high thigmotaxis) | Matches wall preference | Single parameter control |
| RatInABox (low thigmotaxis) | Reduced wall preference | Adjustable |
| RatInABox (zero thigmotaxis) | Uniform exploration | Default random walk |

Fig. 2c: Real data from Satoh et al. showing 10 minutes of open-field exploration with wall preference.
Fig. 2d-e: RatInABox replicates thigmotaxis bias, controllable by Agent.thigmotaxis parameter.

---

## Experiment 3: Trajectory Import and Upsampling

| Input Data | Resolution | Output After Upsampling | Method |
|------------|------------|------------------------|--------|
| Sargolini et al. | 2 Hz (low resolution) | High temporal resolution | Cubic spline interpolation |
| Ground truth | Full resolution | Reference for comparison | Direct |

Fig. 3a: Low-resolution (2 Hz) imported trajectory upsampled by RatInABox closely matches ground truth. Without upsampling, 2 Hz data is too low for meaningful neural activity simulation.

---

## Experiment 4: Computational Efficiency

| Operation | Time (n=100) | Relative Speed | Hardware |
|-----------|-------------|----------------|---------|
| PlaceCell update | < numpy matmul | Faster than downstream ops | MacBook Pro, Apple M1 |
| GridCell update | < numpy matmul | Faster than downstream ops | MacBook Pro, Apple M1 |
| Random motion model | < numpy matmul | Faster than downstream ops | MacBook Pro, Apple M1 |
| BoundaryVectorCell update | > numpy matmul, < feedforward NN | Slower (360 degree integration) | MacBook Pro, Apple M1 |
| numpy matrix-vector multiply (n=100) | Reference | Baseline comparison | MacBook Pro, Apple M1 |
| PyTorch feedforward NN (100,1000,1000,1) | Reference | Baseline comparison (slower) | MacBook Pro, Apple M1 |

Fig. 3f: Purple bars show RatInABox operations; red bars show potential downstream bottleneck operations. PlaceCells, GridCells, and motion model all update faster than both reference operations.

---

## Experiment 5: Scaling Analysis

| Population Size (n) | Scaling Behavior | Dominant Cost |
|---------------------|-----------------|--------------|
| n < 1000 | O(1) sublinear | Motion model dominates |
| n > 1000 | O(n) linear | Neural update dominates |

Fig. 3f inset: Combined time for Agent + PlaceCell population update as function of population size.

---

## Experiment 6: Full Simulation Benchmark

| Scenario | Cells | Duration | dt | Wall Time |
|----------|-------|----------|-----|-----------|
| 100 PlaceCells, 2D, no extra walls | 100 | 10 min | 0.1 s | ~2 seconds |
| 100 BoundaryVectorCells, 2D, no extra walls | 100 | 10 min | 0.1 s | ~7 seconds |

---

## Experiment 7: Position Decoding Tutorial

| Parameter | Value |
|-----------|-------|
| Environment | 1 m square with small barrier |
| Training trajectory | 5 minutes |
| Testing trajectory | 1 minute (unseen) |
| Number of cells | 20 (PlaceCells) |
| Decoder | Gaussian Process regressor |
| Performance | Close match between decoded and true position |

Fig. S1: Training and testing trajectories, receptive fields for 4 of 20 cells, decoded vs true position traces.

---

## Experiment 8: Reinforcement Learning Tutorial

| Parameter | Value |
|-----------|-------|
| Architecture | 1-layer linear network |
| Algorithm | Model-free policy iteration |
| Learning | TD learning (temporally continuous) |
| Policy | Drift velocity set from value function gradient |
| Environment | Contains wall between agent and reward |
| Result | Agent learns to navigate around wall to reach reward |

Fig. S2: Schematic of RL network; agent initially moves randomly, then learns near-optimal policy for finding reward behind wall.

---

## Default Parameters (Table S1 Summary)

| Parameter | Default Value | Allowed Range |
|-----------|--------------|---------------|
| Environment dimensions | 2D | 1D or 2D |
| Environment scale | 1 m | Positive float |
| Boundary conditions | Solid | Solid or periodic |
| Agent speed mean | ~0.08 m/s | Positive float |
| Agent speed std | ~0.08 m/s | Positive float |
| Agent rotation mean | 0 rad/s | Float |
| Agent rotation std | ~120 deg/s | Positive float |
| Agent thigmotaxis | 0.5 | [0, 1] |
| PlaceCell n | 10 | Positive int |
| GridCell n | 10 | Positive int |
| dt (simulation timestep) | 0.01 s | Positive float |

---

## Comparison with Related Toolkits

| Feature | RatInABox | Biophysical Simulators | Discrete Gridworld |
|---------|-----------|----------------------|-------------------|
| Continuous space | Yes | Yes | No |
| Continuous time | Yes | Yes | No |
| Motion model included | Yes | No (focus on neural biophysics) | Basic transitions |
| Spatially modulated cells | Yes (premade) | Yes (detailed biophysics) | No |
| Lightweight | Yes | No (computationally heavy) | Yes |
| Custom cell types | Yes (FeedForwardLayer) | Yes | N/A |
| Policy-controlled motion | Yes | No | Yes |
| Data import | Yes (spline interpolation) | No | No |

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Continuous (not discrete) position/velocity | More physically realistic; smooth dynamics |
| Online rate calculation (not cached grid) | Accommodates dynamic environments and fast processes |
| Fitted to experimental data | Ensures biological plausibility of motion statistics |
| No biophysical neural detail | Focus on computational/representational level |
| No built-in learning algorithms | Intentionally data-generation focused; not a benchmark suite |
| Single thigmotaxis parameter | Parsimonious control of wall-exploration bias |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Overview: Environment, Agent, Neuron classes; example cell types in complex environments |
| Fig. 2 | Motion model closely matches real rodent locomotion statistics and thigmotaxis |
| Fig. 3 | Trajectory import/upsampling; drift velocity control; computational efficiency analysis |
| Fig. S1 | Position decoding demo with 20 PlaceCells and GP regressor |
| Fig. S2 | RL policy iteration demo with TD learning |

---

## Reference Count
41 references cited (including Sargolini et al. and Tanni et al. datasets).
