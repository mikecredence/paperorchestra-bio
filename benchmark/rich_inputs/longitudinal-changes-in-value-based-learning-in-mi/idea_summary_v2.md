## Working title

Hippocampal and striatal volume contributions to the longitudinal development of feedback-timing-dependent reinforcement learning in 6-to-7-year-old children

## Core question

Do hippocampal and striatal structural volumes differentially contribute to the development of value-based reinforcement learning over a 2-year period in middle childhood, and does feedback timing (immediate vs. delayed) modulate these brain-cognition associations as predicted by the adult memory systems literature?

## Motivation / gap

- Adult studies show that feedback timing modulates engagement of hippocampal (delayed feedback) vs. striatal (immediate feedback) memory systems during reinforcement learning, but whether similar dissociations exist in developing children is unknown
- Longitudinal developmental trajectories of reinforcement learning in middle childhood (ages 6-10) have not been examined with computational models that decompose learning rate and value-guided decision-making (inverse temperature)
- The hippocampus and striatum have different maturational timelines, yet how their structural volumes relate to RL parameter changes over time in children has not been tested
- Cross-sectional developmental studies have described age-related increases in learning accuracy and win-stay behavior, but longitudinal evidence including lose-shift behavior and computational parameters is lacking
- Whether the hippocampal and striatal memory systems operate cooperatively or competitively during value-based learning in childhood (as opposed to the more differentiated pattern in adults) is an open question

## Core contribution (bullet form)

- Two-year longitudinal study of 142 children (wave 1 age: mean 7.19, SD 0.46) showing improved reinforcement learning: increased accuracy (beta_wave2 = 0.550, p < 0.001), increased win-stay (beta = 0.586, p < 0.001), decreased lose-shift (beta = -0.252, p < 0.001), and faster reaction times (beta = -221 ms, p < 0.001)
- Feedback timing modulated reaction time (delayed feedback was faster, beta = -13.8, p = 0.038) and the inverse temperature parameter (value-guided decision-making), but not accuracy or win-stay/lose-shift
- Computational modeling identified longitudinal increases in both learning rate and inverse temperature toward more optimal parameter combinations, with children's learning rates (0.02-0.05) still far from adult optima (~0.29)
- Hippocampal volume showed more protracted maturation than striatal volume across the 2-year period
- Larger hippocampal volume was associated with better delayed model-derived learning longitudinally, consistent with adult findings
- Unexpectedly, larger striatal volume was associated with both immediate AND delayed learning, suggesting a less differentiated, more cooperative role for the striatum in middle childhood

## Method in brief

Children (n=142 at wave 1, n=127 at wave 2; 46% female) completed an adapted probabilistic reinforcement learning task with four cue-choice pairs (87.5% contingent reward probability) across immediate and delayed feedback conditions. In the immediate condition, feedback followed the choice after 1 second; in the delayed condition, a 6-second delay with an incidentally presented object was interposed before feedback. Behavioral measures included accuracy, win-stay probability, lose-shift probability, and reaction time, analyzed with generalized linear mixed models (GLMMs). Computational modeling compared multiple value-based models using Bayesian model comparison (Pseudo-BMA+ with Bayesian bootstrap, 100,000 iterations), with the winning model estimating learning rate (alpha) and inverse temperature (tau) parameters, where tau was allowed to differ by feedback timing condition.

A subgroup underwent structural MRI at both waves (73 children with longitudinal MRI data; 82 usable scans at wave 1, 99 at wave 2 after motion exclusion). Hippocampal and striatal volumes were extracted from T1-weighted scans. Brain-cognition associations were modeled using four-variate latent change score (LCS) models that simultaneously captured longitudinal change in striatal volume, hippocampal volume, immediate learning score, and delayed learning score (model-derived choice probabilities from fitted posterior parameters). This framework allowed testing whether brain volume changes predicted learning changes and whether these associations differed by feedback timing condition. Parameter and model recovery analyses confirmed the reliability of the computational modeling approach.

## Target venue

eLife
