# Idea Summary

## Working title
TEMPy-REFF: Cryo-EM Structure Refinement and B-Factor Estimation Using Mixture Modelling with Ensemble Representation

## Core question
Can a mixture-model framework that treats each atom as a Gaussian component -- jointly optimizing positions, B-factors, and an ensemble of models -- produce better cryo-EM structure refinements than existing single-model approaches?

## Motivation / gap
- Current cryo-EM refinement methods blur the atomic model globally or locally to compare against the experimental map, but maps of flexible systems exhibit significant resolution heterogeneity that a single blurring parameter cannot capture
- B-factor estimation is typically disconnected from position refinement; no unified framework exists to handle both simultaneously
- Single-structure representations fail to capture the local variability around atomic positions, especially in lower-resolution or flexible regions
- No systematic method exists to combine multiple focused or multibody maps into an optimal composite map
- Map segmentation (assigning density to individual chains) is typically done manually or with ad hoc tools

## Core contribution (bullet form)
- Developed TEMPy-REFF, a mixture-model-based refinement protocol that jointly optimizes atomic positions and B-factors for cryo-EM maps, achieving higher CCC than both deposited PDB models and CERES-refined models on a 366-map benchmark (1.8-7.1 A resolution)
- Demonstrated that ensemble maps computed from multiple refined models provide a better representation of experimental maps than single-model simulated maps, with improvement especially evident at lower resolutions
- Validated on 366 EMDB maps from the CERES benchmark, showing that ensemble-based scoring remains near-constant at lower resolutions while CERES and single-model scores decline
- Showed that the mixture-model "responsibility" calculation naturally segments maps into chain-level submaps and enables principled composition of focused maps into composite maps
- Combined TEMPy-REFF with AlphaFold-Multimer to model previously unmodelled regions in deposited EMDB maps
- The refinement is computationally fast (timing benchmarked across multiple systems)

## Method in brief
TEMPy-REFF represents each atom as a Gaussian in a mixture model. The simulated map MS is computed as the sum of Gaussian contributions from all atoms, where each Gaussian has a mean at the atomic position xi, a variance determined by the B-factor Bi, and an amplitude proportional to the atomic number Ni. A uniform background error term kbg accounts for noise and reconstruction artifacts. The overall simulated map is: MS = sum_i [Ni * G(x, xi, Bi)] + kbg, where G is the Gaussian function.

The method iterates between an Expectation step (computing "responsibilities" -- the fraction of observed density attributable to each atom) and a Maximization step (re-estimating positions, B-factors, and the background parameter). Position updates are driven by a fictitious force Fmap = K * delta(xi), combined with molecular dynamics forces from the AMBER force field (with GB-Neck2 implicit solvent in OpenMM). B-factors converge in approximately 10-12 iterations.

After single-model refinement, an ensemble of models is generated to capture local variability. The ensemble map (sum of simulated maps from the ensemble members) provides improved CCC compared to any single model. The responsibility calculation also enables map segmentation (assigning density to specific chains) and composite map construction (optimally weighting multiple focused maps).

## Target venue
Nature Communications
