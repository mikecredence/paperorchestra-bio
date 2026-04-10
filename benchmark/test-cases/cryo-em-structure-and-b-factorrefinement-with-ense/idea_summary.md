## Working title

TEMPy-REFF: Ensemble-based atomic structure refinement with B-factor modeling for cryo-EM density maps

## Core question

Can we improve atomic model fitting to cryo-EM density maps by treating atomic positions as mixture model components with variance-based B-factors and ensemble representations?

## Motivation / gap

- Current refinement tools for cryo-EM maps do not fully exploit the statistical relationship between atomic displacement (B-factors) and map density
- Existing methods produce suboptimal fits, especially in flexible or poorly resolved regions
- There is no systematic large-scale benchmark comparing refinement quality across hundreds of EMDB entries
- Combining structure prediction (AlphaFold-Multimer) with density-guided refinement for newly modelled regions is underexplored

## Core contribution

- A novel refinement method (TEMPy-REFF) that models atomic positions as Gaussian mixture components with B-factor variances and ensemble descriptions
- Significantly improved map-model fit compared to state-of-the-art on a large benchmark (366 cryo-EM maps, 1.8-7.1 A resolution)
- Demonstration that combining TEMPy-REFF with AlphaFold-Multimer can model previously unmodelled regions in deposited EMDB maps
- A natural decomposition of maps into components, enabling accurate composite map creation

## Method in brief

- Represent each atom as a component in a Gaussian mixture model; atomic B-factors correspond to component variances
- Optimize fit to cryo-EM density using this mixture framework with an ensemble of conformations
- Validate on 366 EMDB maps (resolution range 1.8-7.1 A) with corresponding PDB assembly models
- Combine with AlphaFold-Multimer predictions to extend modelling into unresolved regions

## Target venue

Nature Communications
