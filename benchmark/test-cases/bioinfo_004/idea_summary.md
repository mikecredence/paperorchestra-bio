## Working title

Improved protein complex prediction with AlphaFold-multimer by denoising the MSA profile

## Core question

Can learning a bias to the multiple sequence alignment (MSA) representation via gradient descent through the AlphaFold-multimer network improve the accuracy of protein complex structure predictions, especially for difficult targets?

## Motivation / gap

- AlphaFold-multimer (AFM) has advanced protein complex structure prediction, yet only about 60% of dimers are accurately predicted
- Many biologically important complexes remain beyond the reach of standard AFM inference
- The quality of the MSA critically influences prediction accuracy, but current pipelines use MSAs without task-specific optimization
- Existing sampling-based approaches (e.g., AFsample) improve predictions at massive computational cost, motivating more efficient alternatives

## Core contribution

- Introduce AFProfile, a protocol that learns a continuous bias applied to the MSA representation by performing gradient descent through the AFM network, guided by predicted confidence (MMscore)
- On seven difficult CASP15 targets, AFProfile raises the average MMscore from 0.63 to 0.76
- Across 487 protein complexes where standard AFM fails, AFProfile achieves a 33% success rate (MMscore > 0.75)
- Demonstrate that MSA denoising is an efficient, complementary strategy to brute-force sampling for improving complex prediction

## Method in brief

AFProfile parameterizes a learnable bias vector added to the MSA embedding used by AlphaFold-multimer. Gradient descent is performed through the frozen AFM network to maximize the predicted confidence metric (MMscore), which correlates strongly with DockQ (Spearman r > 0.8 for heteromers, > 0.9 for homomers). The optimized MSA profile effectively filters input information so AFM can better utilize it for structure prediction. Evaluation covers CASP15 targets and a curated benchmark of 487 difficult protein complexes.

## Target venue

PLOS Computational Biology
