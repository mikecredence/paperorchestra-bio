Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: PLOS Computational Biology

## Idea Summary

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


## Experimental Log

# Experimental Log: Sensory Coding Transitions Along Visual Dorsal Stream

## Neural Dataset

| Brain Area | Approximate Neuron Count | Source |
|-----------|------------------------|--------|
| V1 | ~400 | Multiple studies, awake fixating macaque |
| V2 | ~300 | Multiple studies, awake fixating macaque |
| MT | ~350 | Multiple studies, awake fixating macaque |
| Total | 1,056 tuning curves | -- |

All recordings from isolated single units in awake fixating macaque monkeys.

## Natural Disparity Statistics

| Parameter | Value |
|-----------|-------|
| Dataset | Previously collected eye-tracked human data |
| Subjects | 3 adults |
| Tasks | Food preparation and navigation |
| Field analyzed | Central 10 degrees radius from fixation |
| Distribution properties | Zero-mean, symmetric, highly kurtotic |
| Small disparities | Much more probable than large disparities |

### Task-Specific Distribution Differences (Fig 1B)

| Task | Distribution Feature |
|------|---------------------|
| Food preparation | More large disparities (close objects) |
| Navigation | Fewer large disparities (distant objects) |
| Both | Approximately zero-mean, symmetric, kurtotic |

## Theoretical Predictions

### Power Law: FI ~ p^alpha

| Coding Goal | Alpha | Error Norm Minimized | Interpretation |
|-------------|-------|---------------------|----------------|
| Infomax (information preservation) | 2 | L0 (error sparsity) | All errors penalized equally |
| Discrimination optimal | 2/3 | L2 (mean squared error) | Large errors penalized more |
| Intermediate | Between 2/3 and 2 | Between L0 and L2 | Transition state |

Fig 1C: Theoretical prediction showing FI ~ p^2 (infomax dashed line) vs FI ~ p^(2/3) (discrimax dashed line).
Fig 1D: Error norm visualization - L0 maximizes error sparsity; L2 minimizes large errors.

## Population Fisher Information (Fig 2)

### Population FI by Brain Area (Fig 2B)

| Brain Area | FI Distribution Shape | Relative to Disparity Probability |
|-----------|----------------------|-----------------------------------|
| V1 | Concentrated near zero disparity | Closely follows p^2 |
| V2 | Similar to V1 | Closely follows p^2 |
| MT | More spread, flatter | Closer to p^(2/3) |

500 bootstrapped samples per brain area shown as thin lines. Thick lines are mean population FI.

## Power Law Exponent Analysis (Fig 3)

### Food Preparation Task

| Brain Area | Median Alpha | Distribution Width | Interpretation |
|-----------|-------------|-------------------|----------------|
| V1 | ~2 | Narrow | Near infomax |
| V2 | ~2 | Narrow (highly overlapping with V1) | Near infomax |
| MT | ~0.67 | Moderate | Near discrimination optimal |

### Navigation Task

| Brain Area | Median Alpha | Interpretation |
|-----------|-------------|----------------|
| V1 | ~2 | Near infomax |
| V2 | ~2 | Near infomax |
| MT | ~0.67 | Near discrimination optimal |

Fig 3A: Histograms of bootstrapped power law exponents for food preparation. V1/V2 near 2, MT near 2/3.
Fig 3D: Similar pattern for navigation task.

### Statistical Comparisons

| Comparison | Result |
|-----------|--------|
| V1 vs V2 | Highly overlapping, not significantly different |
| V1 vs MT | Significantly different |
| V2 vs MT | Significantly different |

## Tuning Curve Fitting (Fig 4)

### 6-Parameter Modified Gabor Function

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Gaussian center | mu | Preferred disparity |
| Gaussian width | sigma | Tuning bandwidth |
| Gaussian amplitude | A | Response amplitude |
| Cosine frequency | f | Frequency of modulation |
| Cosine phase | phi | Phase of modulation |
| Baseline | b | Spontaneous rate |

### Parameter Distributions by Brain Area (Fig 4)

| Parameter | V1 | V2 | MT |
|-----------|----|----|----| 
| Preferred disparity (mu) | Concentrated near 0 | Concentrated near 0 | Shifted to larger disparities |
| Tuning width (sigma) | Narrower | Intermediate | Broader |
| Frequency (f) | Higher | Intermediate | Lower |
| Phase (phi) | Variable | Variable | Variable |
| Amplitude (A) | Variable | Variable | Variable |
| Baseline (b) | Variable | Variable | Variable |

Key observation: MT neurons tend to prefer larger disparities and have broader tuning compared to V1/V2.

## Parameter Swapping Analysis (Fig 5)

### Which Parameter Drives the V1-to-MT FI Transition?

| Parameter Swapped (V1 -> MT values) | Effect on V1 Population FI | Drives Transition? |
|--------------------------------------|---------------------------|-------------------|
| Preferred disparity (mu) | FI shifts toward MT pattern | Yes - key driver |
| Tuning width (sigma) | Modest effect | Partial |
| Frequency (f) | Small effect | No |
| Phase (phi) | Minimal effect | No |
| Amplitude (A) | Minimal effect | No |
| Baseline (b) | Minimal effect | No |

Fig 5A: Protocol - replace one V1 parameter at a time with random MT values, recompute population FI.
Fig 5B: Mean and IQR of resampled V1 population FI for each swapped parameter (purple) vs original V1 (orange).

Key finding: Replacing V1 preferred disparities with MT values (shift toward larger disparities) is the primary driver of the coding transition from infomax to discrimination-optimal.

## Spike Count Properties (Fig S3)

| Brain Area | Spike Count Properties | Comparison |
|-----------|----------------------|-----------|
| V1 | Standard | Similar across areas |
| V2 | Standard | Similar |
| MT | Standard | Similar |

Noise analysis suggests spike count properties are similar across examined areas, supporting the assumption of comparable resource constraints.

## Bootstrapping Procedures

| Analysis | Bootstraps | CI |
|----------|-----------|-----|
| Disparity distribution | 100 resamples | 95% CI |
| Population FI | 500 bootstrapped samples | Shown as thin lines |
| Power law exponents | 500 bootstrapped samples | Gaussian fit histograms |
| Parameter swapping | 500 new V1 populations per parameter | IQR shown |

## Receptive Field Center Distributions (Fig S1)

| Brain Area | RF Center Distribution |
|-----------|----------------------|
| V1 | Primarily one hemifield |
| V2 | Primarily one hemifield |
| MT | Primarily one hemifield |
| Correction | Kernel-smoothed 2D probability densities used for resampling disparity statistics |

## Key Figure Observations

- Fig 1A: Diagram of binocular disparity definition and tuning curve populations
- Fig 1B: Natural disparity distributions for food preparation and navigation - kurtotic, zero-mean
- Fig 1C: Theoretical FI ~ p^alpha with infomax (alpha=2) and discrimax (alpha=2/3) predictions
- Fig 2A: 1,056 tuning curves compiled from three brain areas
- Fig 2B: Population FI shows progressive transition from V1 to MT
- Fig 3A: Power law exponent histograms: V1/V2 near 2, MT near 2/3
- Fig 3B: Population FI plotted with theoretical best-fit power laws
- Fig 4: Gabor parameter distributions reveal MT has larger preferred disparities and broader tuning
- Fig 5: Parameter swapping identifies preferred disparity as key driver of coding transition

## Discussion Points

| Consideration | Note |
|--------------|------|
| Independent neurons assumption | Cannot verify noise correlations from single-unit data |
| Resource constraints | Assumed similar across areas |
| Broader tuning in MT | May partly reflect pooling across orientations for direction selectivity |
| Even/odd symmetry | No difference observed between areas (unlike some prior reports) |

