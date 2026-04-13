Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Cell Reports

## Idea Summary

## Working title
Optimal Corticothalamic Connectivity Structures for Learning in Thalamocortical Loops

## Core question
What corticothalamic connectivity structure optimally supports biologically plausible learning in thalamocortical synapses, and does the optimal structure depend on the type of task (motor control vs working memory)?

## Motivation / gap
- CTC loops are critical for cognition and motor control, but the computational role of thalamus is poorly understood
- Recent evidence shows plasticity in thalamocortical synapses, but how corticothalamic connectivity shapes learning is unknown
- Existing normative models for feedforward compression/expansion cannot be directly applied to recurrent CTC loops
- Current theories proposing computational roles for CTC loops do not address how connectivity weights could be learned
- No framework exists to link corticothalamic structure to task-specific learning optimization

## Core contribution (bullet form)
- Showed that local learning rules (RFLO) are effective for thalamocortical but not corticothalamic synapses, motivating structured corticothalamic connectivity
- Used meta-learning to identify optimal corticothalamic connectivity, finding that readout-aligned (efference copy) structure benefits autonomous motor control
- Demonstrated that principal component-aligned corticothalamic structure is optimal for working memory tasks
- Validated predictions with neural recordings from mice: motor cortex-thalamus interactions during grasping are consistent with readout structure; prefrontal cortex-thalamus interactions during delayed discrimination are consistent with PC structure
- Extended model to a two-module reaching task showing preparatory module benefits from PC structure while execution module benefits from readout structure

## Method in brief
The model consists of N interconnected cortical neurons reciprocally connected with M uncoupled thalamic neurons (M << N). Cortical activity evolves as: tau * dh/dt = -h + phi(W_CC * h + W_CT * r + W_I * x), where phi is tanh, and thalamic activity is r = phi(W_TC * h). The output y = W_o * h is a linear readout of cortical activity. The effective connectivity is W_eff = W_CC + W_CT * V * W_TC, a rank-M perturbation of the cortical recurrent weights. Thalamocortical weights (W_CT) are updated by RFLO, a biologically plausible local learning rule, while corticothalamic weights (W_TC) are optimized on a slow timescale via meta-learning (gradient descent on the outer loop).

Three candidate corticothalamic structures were tested: random projections, readout-aligned projections (communicating efference copy of motor output), and principal component projections (communicating directions of highest cortical variance). Tasks included autonomous pattern generation (motor control), delayed discrimination (working memory), and goal-directed reaching with a two-joint arm model requiring separate preparatory and execution thalamic modules.

## Target venue
Cell Reports


## Experimental Log

# Experimental Log: Corticothalamic Connectivity and Learning

## Model Architecture

| Parameter | Value |
|-----------|-------|
| Cortical neurons (N) | 256 (default) |
| Thalamic neurons (M) | 1 to 128 (varied) |
| Nonlinearity | tanh |
| Cortical recurrence | W_CC (fixed random) |
| Thalamocortical weights | W_CT (learned via RFLO) |
| Corticothalamic weights | W_TC (meta-learned or structured) |
| Readout | Linear y = W_o * h |

## Experiment 1: Learning Rule Comparison (Fig 1C)

### Performance vs Thalamic Population Size

| Thalamic Neurons (M) | Learning in W_TC (CT only) | Learning in W_CT (TC only) | Both |
|----------------------|---------------------------|---------------------------|------|
| 1 | Poor | Good | Good |
| 4 | Poor | Better | Better |
| 16 | Poor | Good | Good |
| 64 | Poor | Best | Best |
| 128 | Poor | Best | Best |

Key finding: RFLO-based learning is effective for thalamocortical synapses but ineffective for corticothalamic synapses. Error bars denote standard errors via bootstrapping.

## Experiment 2: Meta-Learning of Corticothalamic Structure (Fig 2)

### Candidate Corticothalamic Structures

| Structure | Description |
|-----------|-------------|
| Random | Random projection of cortical activity |
| Readout | Projects output-relevant subspace (efference copy) |
| PC (Principal Components) | Projects directions of highest cortical variance |
| Meta-learned | Optimized via outer-loop gradient descent |

### Meta-Learning Setup

| Parameter | Value |
|-----------|-------|
| Outer loop | Gradient descent on W_TC |
| Inner loop | RFLO updates on W_CT |
| Optimization | Minimize task error after learning |

Fig 2B: Schematic shows slow outer loop optimizing corticothalamic weights improves inner loop error-driven learning in thalamocortical synapses.

## Experiment 3: Task-Specific Optimal Structures (Fig 3)

### Autonomous Motor Control Task

| Corticothalamic Structure | M=1 Performance | M=4 Performance | M=16 Performance |
|--------------------------|-----------------|-----------------|------------------|
| Random | Poor | Moderate | Good |
| PC | Poor | Moderate | Good |
| Readout | Best | Best | Best |
| Meta-learned | Similar to Readout | Similar to Readout | Similar to Readout |

Fig 3A: Networks with readout-aligned corticothalamic connectivity produce outputs closest to the target function for the autonomous control task.

### Working Memory (Delayed Discrimination) Task

| Corticothalamic Structure | M=1 Performance | M=4 Performance | M=16 Performance |
|--------------------------|-----------------|-----------------|------------------|
| Random | Poor | Poor | Moderate |
| PC | Better | Best | Best |
| Readout | Poor | Moderate | Good |
| Meta-learned | Similar to PC | Similar to PC | Similar to PC |

Fig 3B: For working memory, PC-aligned corticothalamic connectivity outperforms other structures.

### Summary: Task x Structure Interaction

| Task Type | Optimal CT Structure | Interpretation |
|-----------|---------------------|----------------|
| Autonomous motor control | Readout-aligned | Efference copy of motor output |
| Working memory | PC-aligned | Highest-variance cortical dimensions |
| Reaching (preparation) | PC-aligned | Need to maintain stimulus information |
| Reaching (execution) | Readout-aligned | Need to drive motor output |

## Experiment 4: Goal-Directed Reaching (Fig 4)

### Model Setup

| Parameter | Value |
|-----------|-------|
| Arm model | Two-joint planar arm |
| Output dimensions | 2 (angular accelerations) |
| Thalamic modules | 2 (preparatory and execution) |
| Preparatory module | Active during preparation |
| Execution module | Active during movement |
| Reach targets | 8 directions |

### Performance by Corticothalamic Structure (Fig 4B)

| Prep CT Structure | Exec CT Structure | Performance |
|-------------------|-------------------|-------------|
| Random | Random | Worst |
| Random | Readout | Moderate |
| PC | Random | Moderate |
| PC | Readout | Best |
| Readout | Random | Poor |
| Readout | Readout | Moderate |

Best combination: PC for preparatory module, Readout for execution module. This aligns with the hypothesis that preparation requires maintaining high-variance cortical activity while execution requires communicating the motor command.

## Experiment 5: Neural Data Analysis (Fig 5)

### Motor Control: Grasping Task

| Analysis | Finding |
|----------|---------|
| Task | Mice reaching for food pellet |
| Recordings | Motor cortex + motor thalamus |
| Regression approach | Cortical activity regressed against behavior (hand acceleration) and thalamic activity |
| Key result | Cortical subspace predicting thalamic activity aligns more with readout (behavior) than with top PCs |

### Working Memory: Delayed Discrimination Task

| Analysis | Finding |
|----------|---------|
| Task | Delayed sensory discrimination |
| Recordings | Prefrontal cortex + mediodorsal thalamus |
| Key result | Cortical subspace predicting thalamic activity aligns more with top PCs than with readout |

### Alignment Metric Summary

| Brain Region Pair | More Aligned With | Consistent With Model |
|-------------------|-------------------|----------------------|
| Motor Ctx - Motor Thal | Readout | Yes (motor control prediction) |
| Prefrontal Ctx - MD Thal | PC | Yes (working memory prediction) |

Fig 5A: Motor cortex-thalamus data shows decoded thalamic activity follows behavioral readout.
Fig 5B: Prefrontal cortex-thalamus data shows thalamic activity captures high-variance cortical dimensions.

## Theoretical Analysis

| Property | Description |
|----------|-------------|
| Effective connectivity | W_eff = W_CC + W_CT * V * W_TC (rank-M perturbation) |
| Bottleneck interpretation | Thalamus compresses N-dim cortical activity into M-dim space |
| Meta-learning interpretation | CT structure reflects evolutionary/developmental optimization |
| Biological plausibility | Local RFLO rule for TC synapses; structured CT via development |

## Key Figure Observations

- Fig 1A: Schematic of cortical network (N neurons, recurrent) connected to thalamic units (M, no local recurrence)
- Fig 1B: Weight diagram showing which connections are plastic vs fixed
- Fig 1C: Performance improves with M for TC learning (green) but not CT learning (black)
- Fig 2A: Candidate subspaces illustrated in cortical activity space
- Fig 2C: Meta-learned structure converges to task-dependent optimal
- Fig 3: Clear task x structure interaction with crossover pattern
- Fig 4: Two-module reaching model confirms mixed strategy is optimal
- Fig 5: Neural data from mice qualitatively matches model predictions

## Methods Summary

| Component | Tool/Approach |
|-----------|---------------|
| Network simulation | Euler integration of RNN dynamics |
| Learning rule | RFLO (random feedback local online) |
| Meta-learning | Gradient descent on outer loop |
| Neural data (motor) | Electrophysiology in motor cortex and thalamus |
| Neural data (PFC) | Electrophysiology in PFC and mediodorsal thalamus |
| Statistical analysis | Bootstrap standard errors |
| Alignment metric | Subspace overlap / principal angles |

