# Idea Summary: Agent-Based Model of Nonlinear Cytokine Interactions in Muscle Regeneration

## Working title
Agent-based model demonstrates the impact of nonlinear, complex interactions between cytokines on muscle regeneration

## Core question
How do individual cellular behaviors and nonlinear cytokine interactions in the microenvironment drive muscle recovery from injury, and can combined cytokine perturbations enhance regeneration beyond single-factor interventions?

## Motivation / gap
- Skeletal muscle injuries account for >30% of all injuries and are among the most common orthopedic complaints
- Standard treatments (rest, ice, compression, elevation, anti-inflammatories) lack firm scientific basis and often result in incomplete recovery, scar tissue, or injury recurrence
- Muscle regeneration involves five interrelated phases (degeneration, inflammation, regeneration, remodeling, functional recovery) with highly coordinated cell-cytokine interactions
- Experimental testing of cytokine dynamic alterations is complex and expensive due to difficulties in quantification and confounding pleiotropic effects
- Prior computational models of muscle regeneration did not incorporate spatial interactions between cytokines and the microvasculature
- No existing model comprehensively captures the ~100 rules governing behavior of all major cell types (fibers, SSCs, fibroblasts, neutrophils, macrophages) plus microvasculature remodeling

## Core contribution (bullet form)
- Built a novel ABM using the Cellular Potts framework in CompuCell3D with ~100 literature-derived rules and >100 parameters governing 7 cell/structure types and their microenvironment interactions
- Calibrated 52 unknown parameters using parameter density estimation (Latin hypercube sampling + alternative density subtraction) against temporal CSA recovery, SSC, and fibroblast count data
- Validated independently against macrophage (total, M1, M2), neutrophil, and capillary count experimental data not used in calibration
- Successfully replicated 8 model perturbations (VEGF-A injection, cell depletions, hindered angiogenesis, cytokine KOs) against published experiments
- Identified via sensitivity analysis (LHS + PRCC) that combined cytokine alterations (decreasing HGF/VEGF-A decay, increasing TGF-beta/MMP-9 decay, increasing MCP-1 diffusion) yield a 13% increase in CSA recovery at day 28 compared to unaltered regeneration
- Demonstrated nonlinear and threshold effects: VEGF-A dose response plateaus, HGF effect saturates, TNF-alpha shows non-monotonic relationship with fibroblast counts

## Method in brief
The ABM was implemented in CompuCell3D (version 4.3.1) using the Cellular Potts modeling framework. The simulation represents a cross-section of murine skeletal muscle tissue containing muscle fibers, satellite stem cells (SSC), fibroblasts, neutrophils, macrophages (M1 and M2 phenotypes), microvessels, and lymphatic vessels. Over 100 published studies were referenced to define approximately 100 rules dictating cell behaviors including recruitment, activation, proliferation, differentiation, apoptosis, and cytokine secretion. Key cytokines modeled include TNF-alpha, TGF-beta, HGF, VEGF-A, MCP-1, MMP-9, and IL-10, each with diffusion and decay dynamics governing their spatial distribution.

Parameter calibration used Latin hypercube sampling (LHS) to generate 600 unique parameter sets run in triplicate. Simulations were filtered against experimental bounds for CSA recovery, and alternative density subtraction (ADS) was used to iteratively narrow parameter bounds. Partial rank correlation coefficients (PRCC) provided sensitivity analysis to guide parameter adjustment. The 52 unknown parameters were narrowed into a final calibrated set. Model validation compared non-calibration outputs (macrophage, neutrophil, capillary counts) against independent experimental data, and 8 perturbation scenarios were tested against published results.

Sensitivity analysis for cytokine dynamics used LHS and PRCC to systematically vary cytokine diffusion coefficients and decay rates. This identified which cytokine parameters most influenced CSA recovery, SSC counts, and fibroblast behavior at different time points. Combined perturbations were then tested to identify synergistic effects that enhanced regeneration outcomes beyond individual interventions.

## Target venue
eLife
