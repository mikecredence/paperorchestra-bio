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
