# Experimental Log: DEBBIES Life History Trait Dataset

## Overview

DEBBIES (Version 5) provides eight life history traits for 185 ectotherm species across 18 orders, designed to parameterize DEB integral projection models for cross-taxonomical demographic analyses.

---

## Dataset Description

### Table 1: DEBBIES Dataset Versions

| Version | Number of Species | Key Changes |
|---------|------------------|-------------|
| 1 | 47 | Initial release |
| 2 | < 47 | Removed some incorrect entries from v1 |
| 3 | ~204 | Added 157 elasmobranch species |
| 4 | ~207 | Added 3 more elasmobranchs |
| 5 (current) | 185 | Changed kappa symbols to match data descriptor notation |

### Table 2: Eight Input Life History Traits

| Trait Symbol | Description | Type | Time-Variant? |
|-------------|-------------|------|---------------|
| Lb | Length at birth | Length measure | No (fixed for life cycle) |
| Lp | Length at puberty | Length measure | No (fixed for life cycle) |
| Lm | Maximum length | Length measure | No (maximum under best conditions) |
| Rm | Maximum reproduction rate | Rate | No (maximum under best conditions) |
| kappa | Fraction energy to soma vs reproduction | Fraction | No (assumed constant) |
| vB growth rate | von Bertalanffy growth rate | Rate | No |
| mu_j | Juvenile mortality rate | Rate | No |
| mu_a | Adult mortality rate | Rate | No |

### Table 3: Taxonomic Composition

| Category | Value |
|----------|-------|
| Total species | 185 |
| Number of orders | 18 |
| Major groups represented | Ray-finned fish, cartilaginous fish, other ectotherms |
| Data source | Scientific literature (multiple studies per species typical) |
| Storage format | CSV with metadata text file |
| Repository | FigShare |

---

## DEB-IPM Model Structure

### Table 4: Four Fundamental Functions of the DEB-IPM

| Function | Symbol | Description | Depends On |
|----------|--------|-------------|------------|
| Survival | S(L(t)) | Probability of surviving from t to t+1 | L, Lm, E(Y), kappa, mu_j, mu_a |
| Growth | G(L', L(t)) | Probability of growing from length L to L' | L, growth parameters |
| Reproduction | R(L(t)) | Number of offspring produced between t and t+1 | L, Lp, Rm, kappa |
| Parent-offspring | D(L', L(t)) | Association between parent and offspring size | L, Lb |

### Table 5: Survival Function Details

| Condition | Mortality Rule |
|-----------|---------------|
| Starvation | Occurs when L > Lm * E(Y) / kappa; then S(L(t)) = 0 |
| Juvenile (Lb <= L < Lp) and not starving | Mortality rate = mu_j |
| Adult (Lp <= L <= Lm) and not starving | Mortality rate = mu_a |
| Feeding level E(Y) | Ranges 0 (empty gut) to 1 (full gut) |

### Table 6: Kooijman-Metz Energy Budget Assumptions

| Assumption | Description |
|-----------|-------------|
| Organism shape | Isomorphic (surface area ~ L^2, volume ~ L^3) |
| Ingestion rate | I = Imax * Y * L^2 (proportional to squared length) |
| Assimilation efficiency | Constant epsilon |
| Kappa rule | Fraction kappa to somatic maintenance + growth |
| Remainder (1-kappa) | To reproduction and maturation |

---

## Feeding Level Analysis

### Table 7: Minimum Feeding Level Requirements

| Parameter | Value |
|-----------|-------|
| Minimum E(Y) for most species | ~0.7 |
| Lowest viable E(Y) for some species | 0.4 |
| Interpretation of E(Y) = 0.7 | Gut "just filled" on empty-to-bursting scale |
| Species with viable E(Y) < 0.5 | Less than half of all species |

---

## Technical Validation: Population Growth Rate

### Table 8: Population Growth Rate (lambda) Distribution by Feeding Level

| Feeding Level E(Y) | Lambda Distribution Pattern | Ecological Interpretation |
|--------------------|----------------------------|--------------------------|
| 0.9 (high) | Most species slightly > 1 | Population increase under favorable conditions |
| 0.7 (intermediate) | Centered around 1 | Population stability |
| 0.5 (low) | Mostly < 1 | Population decline under poor conditions |

Fig 2a shows frequency distributions of lambda at three feeding levels (blue: E(Y)=0.9, red: E(Y)=0.7, yellow: E(Y)=0.5). Results match general ecological expectation that populations grow under good conditions and decline under poor conditions.

---

## Technical Validation: Generation Time

### Table 9: Predicted vs Observed Generation Time Regression

| Feeding Level E(Y) | Regression Model | Regression Coefficient | 95% CI Overlaps 1? | RMSE (years) | Interpretation |
|--------------------|-----------------|----------------------|--------------------|--------------|----|
| 0.9 | y ~ x (no intercept) | Close to 1 | Yes | Lower | Not significantly different from observed |
| 0.7 | y ~ x (no intercept) | > 1 | Varies | Moderate | Predicted higher than observed |
| 0.5 | y ~ x (no intercept) | > 1 | No | Higher | Predicted significantly higher than observed |

Fig 2b shows observed vs predicted generation time scatterplots at three feeding levels. Black line denotes x=y (perfect agreement). At E(Y)=0.9, points cluster near the identity line. At lower feeding levels, predictions are biased upward.

Note: 95% CIs approximated as regression coefficient +/- 2 * standard error. Overlap with 1 indicates predicted values not significantly different from observed.

---

## Technical Validation: Longevity

### Table 10: Predicted vs Observed Longevity Regression

| Feeding Level E(Y) | Regression Coefficient | 95% CI Overlaps 1? | RMSE (years) | Note |
|--------------------|----------------------|--------------------|--------------|----|
| 0.9 | Reported in Table 2 | Reported | Reported | Longevity = age at maturity + mature life expectancy |
| 0.7 | Reported in Table 2 | Reported | Reported | |
| 0.5 | Reported in Table 2 | Reported | Reported | |

Fig 2c shows observed vs predicted longevity scatterplots at three feeding levels. The RMSE provides a 95% interval for observed values around predicted values.

---

## Technical Validation: Age at Maturity

### Table 11: Predicted vs Observed Age at Maturity Regression

| Feeding Level E(Y) | Regression Coefficient | 95% CI Overlaps 1? | RMSE (years) |
|--------------------|----------------------|--------------------|-------------|
| 0.9 | Reported in Table 2 | Reported | Reported |
| 0.7 | Reported in Table 2 | Reported | Reported |
| 0.5 | Reported in Table 2 | Reported | Reported |

Fig 2d shows observed vs predicted age at maturity at three feeding levels. Black lines denote x=y line of equal values.

---

## Derived Life History Traits

### Table 12: Nine Derived Life History Traits Computable from DEB-IPM

| Trait | Category | Description |
|-------|----------|-------------|
| Generation time | Turnover rate | Mean age of parents of newborns |
| Survivorship curve | Longevity | Probability of surviving to age x |
| Age at sexual maturity | Longevity | Age at which reproduction begins |
| Progressive growth | Growth | Size increase over lifetime |
| Retrogressive growth | Growth | Size decrease (if applicable) |
| Mean sexual reproduction | Reproduction | Average reproductive output |
| Degree of iteroparity | Reproduction | Spread of reproduction over lifetime |
| Net reproductive rate | Reproduction | Expected offspring per lifetime |
| Mature life expectancy | Longevity | Expected remaining lifespan after maturity |

### Table 13: Additional Demographic Quantities from DEB-IPM

| Quantity | Description | Computation |
|----------|-------------|-------------|
| Population growth rate (lambda) | Dominant eigenvalue of discretized IPM matrix | Matrix A (200 x 200 bins) |
| Demographic resilience | Damping ratio | Ratio of dominant to subdominant eigenvalue |
| Elasticity analysis | Proportional change in lambda per proportional change in each trait | Perturbation of kappa, Lb, Lp, Lm, mu_j, mu_a, vB, Rm |

---

## Data Sources for Validation

### Table 14: External Data Sources Used

| Source | Taxa Covered | Variables Obtained |
|--------|-------------|-------------------|
| Fishbase | Ray-finned fish, some cartilaginous fish | Generation time, age at maturity, longevity |
| IUCN Red List | Cartilaginous fish, general species | Generation time, longevity |
| Animal Diversity Web | General species | Generation time, age at maturity, longevity |
| AnAge database | General species | Age at maturity, longevity |
| Sharks of the World book | Cartilaginous fish | Longevity, age at maturity |
| Rays of the World book | Cartilaginous fish | Longevity, age at maturity |
| Scientific literature | Individual species | Specific longevity values |

### Table 15: Data Handling Rules for Validation

| Situation | Rule Applied |
|-----------|-------------|
| Value range given | Took median |
| Series of observations given | Took mean |
| Source priority | Animal Diversity Web first, then IUCN, then AnAge |

---

## Comparison with Existing Datasets

### Table 16: DEBBIES vs Other Demographic Databases

| Feature | COMPADRE/COMADRE | PADRINO | DEBBIES |
|---------|-----------------|---------|---------|
| Model type | Matrix Population Models | Integral Projection Models | DEB-IPMs |
| Data requirement | Long-term individual tracking | Long-term individual tracking | 8 life history traits only |
| Data-deficient species | Not accommodated | Not accommodated | Accommodated |
| Cross-taxonomical structure | Variable model structures | Variable | Uniform (all same structure) |
| Mechanistic trade-offs | No | No | Yes (growth-reproduction via kappa) |
| Novel condition forecasts | Limited | Limited | Yes (mechanistic energy budget) |
| Taxonomic scope | Plants and animals | Plants and animals | Ectotherms (185 species, 18 orders) |

---

## Applications and Code Availability

### Table 17: Provided MatLab Code Functions

| Code Package | Purpose | Repository |
|-------------|---------|------------|
| Cross-taxonomical analysis | Calculate 9 derived traits, lambda, damping ratio, elasticity for all species | FigShare (cross-taxonomical folder) |
| Single-species analysis | Calculate same quantities for one species across user-defined feeding levels | FigShare (single-species folder) |

### Table 18: Potential Applications

| Application Area | How DEBBIES Contributes |
|-----------------|------------------------|
| Essential Biodiversity Variables | Feed into EBV pipelines |
| MOSAIC meta-database | Integrate with existing trait databases |
| Conservation management | Identify sensitive life history traits via elasticity |
| Biogeography | Link life history strategies to geographic patterns |
| Evolutionary biology | Cross-taxonomical pace-of-life analyses |
| PCA of life history strategies | Phylogenetically corrected analyses of fast-slow continuum |

---

## Key Caveats

### Table 19: Known Limitations

| Limitation | Description |
|-----------|-------------|
| Multi-study trait sourcing | Traits per species often from different studies; may introduce systematic bias |
| Parameter non-identifiability | Similar growth/reproduction patterns can arise from different parameter sets |
| Population specificity | Dataset represents species-level averages, not population-specific values |
| Feeding level sensitivity | DEB-IPM predictions depend on assumed feeding level E(Y) |
| Minimum feeding level | Many species require E(Y) > 0.7 for viable model runs |
