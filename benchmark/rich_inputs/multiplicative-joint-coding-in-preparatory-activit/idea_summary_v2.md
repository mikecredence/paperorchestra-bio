# Idea Summary

## Working title
Multiplicative Joint Coding in Preparatory Activity for Reaching Sequences in Macaque Motor Cortex

## Core question
How does primate motor cortex encode the elements of a sequential movement during preparation -- are they represented independently (in parallel) or jointly through an interactive coding mechanism?

## Motivation / gap
- Motor cortex is known to encode movement kinematics (direction, speed, distance), but how it handles multi-step sequential movements is poorly understood
- Prior studies mostly used serially presented sensory cues to instruct sequences, potentially confounding sensory-driven and motor-planning activity
- The "competitive queuing" hypothesis posits parallel, independent representations of sequence elements, but this has not been rigorously tested during the preparation period
- A recent study suggested two independent motor processes for double-reach, but did not examine possible interaction between movement elements before execution begins
- If movements were truly independently planned, reaching errors should accumulate across elements, which has not been observed
- The neural coding mechanism (additive vs. multiplicative) underlying sequential motor preparation has not been characterized

## Core contribution (bullet form)
- Discovered a substantial multiplicative component in motor cortex preparatory activity that jointly encodes impending (1st) and subsequent (2nd) reaching targets, transitioning to additive/parallel coding during execution
- Showed that in the peri-movement-onset window, the multiplicative model outperforms the additive model (population-level adjusted R2 comparison, p < 0.0005), while around movement end the additive model provides a better fit
- Demonstrated via PCA-LDA dimensionality reduction that preparatory neural states sub-cluster by 2nd reach direction within the optimal subspaces defined by 1st reach direction
- Proved via population vector simulation that multiplicative coding preserves robust linear readout of the ongoing movement element, whereas purely additive coding introduces systematic directional bias
- Trained a recurrent neural network (RNN) on the double-reach task that spontaneously developed multiplicative joint coding resembling the real neural data, with conspicuous nonlinearity
- Replicated findings across three rhesus macaques using both implanted micro-electrode arrays and single electrodes

## Method in brief
Three rhesus monkeys performed a memory-guided double-reach task. In single-reach (SR) trials, one target appeared at one of six equally spaced directions (0-300 degrees in 60-degree steps). In double-reach (DR) trials, two targets (square and triangle) appeared simultaneously for 400 ms, then were extinguished during a 400-800 ms memory period. After the GO signal, monkeys reached first to the square, then immediately to the triangle (displaced 120 degrees CW or CCW from the square). All 18 conditions (3 trial types x 6 directions) were pseudo-randomly interleaved. Only correct trials were analyzed. Surface EMG and hand speed confirmed that the first reach in DR was kinematically indistinguishable from the corresponding SR (Pearson r = 0.99 +/- 0.006).

Regression analysis tested whether DR firing rates could be modeled as an additive combination (f_DR = f_1st + f_2nd + constant) or a multiplicative combination (f_DR = f_1st * g(2nd) where g is a gain function of the 2nd target) of directional tunings. Goodness-of-fit was evaluated via adjusted R2 in sliding 200-ms windows aligned to movement onset. A full model combining both additive and multiplicative terms was also tested. Dimensionality reduction used PCA followed by linear discriminant analysis (LDA) to project neural states into subspaces that best separated conditions by 1st and 2nd reach directions. Population vector (PV) simulations with model neurons tested whether multiplicative vs. additive coding preserved directional readout accuracy. An RNN consisting of input, hidden, and output layers was trained on the double-reach task to produce population vector outputs reflecting movement direction and timing.

## Target venue
Nature Communications
