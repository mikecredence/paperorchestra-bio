## Working title
Sensory Coding Transitions from Information Preservation to Discrimination Optimization Along the Visual Dorsal Stream

## Core question
Do neural populations along the dorsal visual stream (V1, V2, MT) shift from optimizing for information preservation about natural binocular disparity statistics to optimizing for perceptual discrimination?

## Motivation / gap
- Optimal coding theory predicts that early sensory areas maximize information about stimulus distributions (FI proportional to p^2), but how this optimization changes along the processing hierarchy is poorly understood
- Previous work found FI ~ p^2 in early sensory areas, but the optimal coding goal may shift in later areas
- Differences in disparity tuning curves between V1, V2, and MT have been documented but lack a normative explanation
- A discrimination-optimized code (FI proportional to p^(2/3)) has been predicted theoretically but not tested empirically
- The specific tuning curve parameters driving the transition between coding regimes are unknown

## Core contribution (bullet form)
- Re-analyzed 1,056 disparity tuning curves from macaque V1, V2, and MT, combined with natural binocular disparity statistics from eye-tracked humans performing food preparation and navigation
- Showed that the power law exponent relating population Fisher Information to stimulus probability shifts from ~2 (infomax) in V1/V2 to ~2/3 (discrimination-optimal) in MT
- V1 and V2 distributions of power law exponents are highly overlapping and near 2; MT distribution is shifted significantly lower
- Identified the preferred disparity parameter (Gabor envelope center) as the key driver of the FI shift from V1 to MT
- Fit tuning curves with 6-parameter modified Gabor function and systematically tested which parameters explain the V1-to-MT transition

## Method in brief
Natural binocular disparity statistics were derived from a previously collected dataset of eye-tracked humans performing food preparation and navigation tasks, computing probability distributions within 10 degrees of fixation. Disparity statistics were resampled based on receptive field center distributions of each neural population to account for hemifield biases. 1,056 disparity tuning curves from macaque V1 (n~400), V2 (n~300), and MT (n~350) were compiled from multiple studies using awake fixating monkeys.

Each tuning curve was fit with a modified 6-parameter Gabor function (Gaussian envelope center, width, amplitude, plus cosine frequency, phase, and baseline). Population Fisher Information was computed from individual neuron FI (assuming Poisson-like noise) and compared to the disparity probability distribution via power law fitting: FI ~ p^alpha. The key theoretical predictions are alpha = 2 for infomax coding (minimizing L0 reconstruction error) and alpha = 2/3 for discrimination-optimal coding (minimizing L2 error). Parameter swapping analysis replaced individual Gabor parameters from V1 with MT values to identify which parameters drive the FI transition.

## Target venue
PLOS Computational Biology
