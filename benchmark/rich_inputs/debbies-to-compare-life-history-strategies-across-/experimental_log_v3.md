# Experimental Log: DEBBIES Dataset for Ectotherm Life History Strategies

## Dataset Overview

| Parameter | Value |
|-----------|-------|
| Dataset name | DEBBIES (Version 5) |
| Number of species | 185 |
| Number of orders | 18 |
| Organism type | Ectotherms |
| Number of life history traits per species | 8 |
| Storage format | CSV with metadata text file on FigShare |
| Projection interval | 1 year |
| Length units | centimeters |
| Rate units | per year |

---

## Eight Input Life History Traits

| Trait | Symbol | Description |
|-------|--------|-------------|
| Fraction energy to respiration | kappa | Fraction of assimilated energy allocated to respiration vs reproduction |
| Length at birth | Lb | Body length at birth |
| Length at puberty | Lp | Body length at sexual maturity |
| Maximum length | Lm | Maximum achievable body length under unlimited resources |
| Juvenile mortality rate | mu_j | Mortality rate for juveniles (Lb <= L < Lp) |
| Adult mortality rate | mu_a | Mortality rate for adults (Lp <= L <= Lm) |
| Von Bertalanffy growth rate | rB | Growth rate parameter |
| Maximum reproduction rate | Rm | Maximum offspring production at maximum length |

---

## Nine Derived Life History Traits (Table 3)

| Trait | Description |
|-------|-------------|
| Population growth rate (lambda) | Dominant eigenvalue of matrix A |
| Generation time (T) | T = log(R0)/log(lambda) |
| Mean life expectancy (eta_e) | eta_e = 1^T * N where N = (I - S)^-1 |
| Age at sexual maturity | Derived from longevity calculation |
| Mature life expectancy | Longevity minus age at maturity |
| Progressive growth (gamma) | Weighted mean across length bins |
| Retrogressive growth (rho) | Weighted mean across length bins |
| Mean sexual reproduction (phi) | Weighted by stable stage distribution |
| Degree of iteroparity | Measure of reproductive event dispersion |

Matrix discretization: 200 bins (p = q = 200). R0 = dominant eigenvalue of F = V(I - GS)^-1.

---

## Data Sourcing Hierarchy

### Von Bertalanffy growth rate (elasmobranchs)
Priority order:
1. Primary literature (female growth curve, empirically measured)
2. Froese supplementary material
3. Calculated as rB = 3/tmax (where tmax = longevity from Fishbase)

### Body lengths (152 species)
- Source: Sharks of the World or Rays of the World
- Total lengths converted to fork lengths using Fishbase scalar values

### Length at birth (5 species from IUCN)
- M. ambigua, M. birostris, A. parmifera, D. trachyderma, R. australiae

### Maximum reproduction rate
- Formula: Rm = (c x n) / i
- c = mean clutch size, n = mean litters per year, i = remigration interval

### Adult mortality rate
- Formula: mu_a = 1/[(tmax + a)/2]
- tmax = longevity, a = age at maturity

### Juvenile mortality rate
- Calculated from survival to maturity: l_alpha = exp(-mu_j * a)

### Kappa values
- Primary: Add My Pet database
- Default if unavailable: kappa = 0.8

### Starvation condition
- Individuals die when L > Lm * E(Y) / kappa
- At kappa = 0.8: L_starvation = 1.25 * L_infinity
- Individuals never reach starvation length at constant feeding (25% larger than achievable ultimate length)

---

## Technical Validation (Figure 2, Table 2)

### Population growth rate (lambda) distributions

| Feeding level E(Y) | Lambda distribution |
|--------------------|---------------------|
| 0.9 (high) | Most species slightly above lambda = 1 (population increase) |
| 0.7 (intermediate) | Centered around lambda = 1 (stability) |
| 0.5 (low) | Most species below lambda = 1 (population decline) |

### Generation time validation (linear regression y ~ x, no intercept)

| Feeding level | Regression coefficient 95% CI | Overlap with 1 | RMSE (years) | R2 |
|--------------|-------------------------------|-----------------|--------------|-----|
| E(Y) = 0.5 | not reported here (see Table 2) | not reported | not reported | not reported |
| E(Y) = 0.7 | not reported here (see Table 2) | not reported | not reported | not reported |
| E(Y) = 0.9 | not reported here (see Table 2) | overlaps | not reported | not reported |

- Predicted generation times higher than observed at lower feeding levels
- Not significantly different from observed at E(Y) = 0.9
- 95% of observed values fall within 19-23 years of predicted values across feeding levels
- Average RMSE across three feeding levels: 10 years
- Highest observed generation time: 53 years (Carcharodon carcharias)
- Average error rate: 19% (10 / 53 = 0.19)

### Longevity validation

| Feeding level | Outcome |
|--------------|---------|
| Lower levels | Predicted lower than observed |
| E(Y) = 0.9 | Not significantly different from observed |

- 95% of observed values fall within 12-43 years of predicted values across feeding levels
- Average RMSE across three feeding levels: 13 years
- Highest observed longevity: 100 years (Squalus suckleyi)
- Average error rate: 13% (13 / 100 = 0.13)

### Age at maturity validation

| Feeding level | Outcome |
|--------------|---------|
| All levels | Predicted higher than observed |
| E(Y) = 0.5 | Best fit with observed values |

- 95% of observed values fall within 11-13 years of predicted values across feeding levels
- Average RMSE across three feeding levels: 6 years
- Highest observed age at maturity: 39 years (Chelonia mydas)
- Average error rate: 15% (6 / 39 = 0.15)

### Summary of error rates

| Life history trait | Average RMSE (years) | Max observed value (years) | Species with max | Average error rate |
|-------------------|---------------------|---------------------------|-----------------|-------------------|
| Generation time | 10 | 53 | Carcharodon carcharias | 19% |
| Longevity | 13 | 100 | Squalus suckleyi | 13% |
| Age at maturity | 6 | 39 | Chelonia mydas | 15% |

---

## DEB-IPM Model Specifications

### Key equations

Survival function: S(L(t)) depends on starvation condition L > Lm * E(Y) / kappa

Growth (von Bertalanffy): L' = L + rB * (Lm * E(Y) - L)

Growth variance: sigma^2(L') depends on sigma(Y) and growth parameters

Reproduction: R(L(t)) = Rm * (L/Lm)^2 * E(Y) for adults (Lp <= L <= Lm)

### Model parameters

| Parameter | Value |
|-----------|-------|
| Matrix discretization bins | 200 |
| Minimum viable feeding level | ~0.7 for most species (some down to 0.4) |
| Feeding level range tested | 0.5 to 0.9 |
| Individual variability source | Gaussian-distributed feeding level Y |

---

## Dataset Versions

| Version | Content |
|---------|---------|
| Version 1 | 47 species |
| Version 2 | Corrections to Version 1 |
| Version 3 | Added 157 elasmobranch species |
| Version 4 | Added 3 more elasmobranchs |
| Version 5 (current) | Updated symbols for kappa and rB |

---

## Validation Data Sources

| Taxonomic group | Generation time source | Longevity source | Age at maturity source |
|----------------|----------------------|-----------------|----------------------|
| Ray-finned fish | Fishbase (primary), IUCN Red List | Fishbase | Animal Diversity Web |
| Cartilaginous fish | IUCN Red List (all species) | IUCN (18 species), Sharks/Rays of the World, Barrowclift et al. | Sharks/Rays of the World, Barrowclift et al. |
| Silvertip shark | N/A | Primary literature | N/A |
| Galapagos shark | N/A | Fishbase | N/A |
| Other species | Animal Diversity Web (primary), IUCN Red List | AnAge (primary), Animal Diversity Web | AnAge, Animal Diversity Web |

---

## Statistics Summary

1. **Linear regression without intercept (y ~ x)** - Comparison of observed (x) vs predicted (y) life history traits across three feeding levels
2. **Root mean square error (RMSE)** - Quantification of prediction deviation
3. **95% confidence intervals** - Approximated as regression coefficient +/- twice standard error; overlap with 1 tested
4. **Coefficient of determination (R2)** - Model fit assessment
5. **Dominant eigenvalue calculation** - Population growth rate from discretized IPM matrix
