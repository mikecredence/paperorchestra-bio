## Working title
DEBBIES: A Dataset of Life History Traits for Parameterizing DEB Integral Projection Models Across 185 Ectotherms

## Core question
Can a standardized dataset of eight key life history traits enable parameterization of dynamic energy budget integral projection models (DEB-IPMs) for cross-taxonomic comparisons of life history strategies in ectotherms, including data-deficient species that lack long-term individual tracking data?

## Motivation / gap
- Existing demographic model databases (COMPADRE, COMADRE, PADRINO) require long-term individual-level data scored from birth to death, creating strong taxonomic bias toward well-studied species
- Many ectotherm species cannot be individually tracked over lifetimes (micro-organisms, small soil-dwelling animals), leaving them underrepresented in demographic analyses
- Essential biodiversity variables and global biodiversity change monitoring require taxonomically balanced representation to avoid unwilling species bias
- DEB-IPMs need only eight life history traits to parameterize, making them suitable for data-deficient species, but no curated dataset of these traits existed across a broad ectotherm taxonomic range
- Cross-taxonomical comparisons of life history strategies (pace of life, reproductive strategy) require standardized trait data in a common modeling framework
- No existing dataset accommodated mechanistic description of the growth-reproduction trade-off needed for population forecasts under novel environmental conditions

## Core contribution (bullet form)
- DEBBIES dataset (Version 5) provides eight life history trait estimates for 185 ectotherm species across 18 orders, stored as CSV with metadata on FigShare
- Technical validation shows predicted population growth rate lambda is slightly above 1 at high feeding (E(Y)=0.9), centered around 1 at intermediate feeding (E(Y)=0.7), and mostly below 1 at low feeding (E(Y)=0.5), matching ecological expectations
- Predicted generation times are not significantly different from observed values at the highest feeding level (E(Y)=0.9); RMSE quantifies overall deviation at each feeding level
- Predicted age at maturity and longevity also validated against observed values from Fishbase, IUCN Red List, AnAge, and other databases
- MatLab code provided for computing 9 derived life history traits, population growth rate, demographic resilience (damping ratio), and elasticity analyses
- Compared to COMPADRE/COMADRE/PADRINO, DEBBIES uniquely accommodates data-deficient species and enables mechanistic population forecasting under novel conditions

## Method in brief
The DEBBIES dataset collects eight life history traits per species: length at birth (Lb), length at puberty (Lp), maximum length (Lm), maximum reproduction rate (Rm), fraction of energy allocated to respiration versus reproduction (kappa), von Bertalanffy growth rate, juvenile mortality rate (mu_j), and adult mortality rate (mu_a). These traits parameterize a DEB-IPM that models population dynamics through four fundamental functions: a survival function S(L(t)), a growth function G(L', L(t)), a reproduction function R(L(t)), and a parent-offspring size function D(L', L(t)). Population dynamics are described by an integral equation over the length domain omega.

The survival function incorporates starvation mortality when maintenance costs exceed assimilated energy (occurring when L > Lm * E(Y)/kappa), with separate juvenile and adult mortality rates. Growth and reproduction are derived from the Kooijman-Metz model, a simplified version of DEB theory assuming isomorphic organisms where ingestion rate scales with squared body length. A constant fraction kappa of assimilated energy goes to somatic maintenance and growth, with the remainder allocated to reproduction and maturation.

Technical validation compared DEB-IPM predictions against observed data from Fishbase, IUCN Red List, Animal Diversity Web, AnAge, and taxon-specific references. Linear regression without intercept (y ~ x) was used to compare predicted versus observed generation time, longevity, and age at maturity at three feeding levels (E(Y) = 0.5, 0.7, 0.9). The 95% confidence intervals of the regression coefficient were checked for overlap with 1. RMSE was used to quantify overall prediction deviation.

## Target venue
Scientific Data
