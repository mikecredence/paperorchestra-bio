## Working title
DEBBIES to compare life history strategies across ectotherms

## Core question
Can a standardized dataset of eight life history traits for ectotherm species enable cross-taxonomical comparisons of life history strategies using dynamic energy budget integral projection models (DEB-IPMs), including for data-deficient species?

## Motivation / gap
- Existing demographic model databases (COMPADRE, COMADRE, PADRINO) require long-term individual-level data scored from birth to death, creating taxonomic bias against species difficult to track (e.g., micro-organisms, small soil-dwelling animals)
- More than 99% of species are ectotherms, so no biological prediction can be considered universal if it does not include these organisms
- DEB-IPMs require only eight life history traits to predict survival, growth, and reproduction, making them suitable for data-deficient species, but only two small datasets existed (13 marine megafauna species and 13 microorganisms)
- Existing MPMs and IPMs do not include a mechanistic description of the growth-reproduction trade-off, limiting population forecasts to novel conditions such as climate change
- Cross-taxonomical comparisons require standardized parameterization, which existing datasets do not readily accommodate

## Core contribution (bullet form)
- Compiled DEBBIES dataset (Version 5) containing eight life history trait estimates for 185 ectotherm species across 18 orders, stored as csv on FigShare
- Technical validation shows predicted population growth rate lambda centered around 1 at intermediate feeding level E(Y) = 0.7, slightly above 1 at E(Y) = 0.9, and below 1 at E(Y) = 0.5
- Average RMSE for generation time across three feeding levels equals 10 years, with average error rate of 19% (10 / 53 = 0.19, where 53 years is the highest observed generation time for Carcharodon carcharias); 95% of observed values fall within 19-23 years of predicted values
- Average RMSE for longevity across three feeding levels equals 13 years, with average error rate of 13% (13 / 100 = 0.13, where 100 years is the highest observed longevity for Squalus suckleyi); 95% of observed values fall within 12-43 years of predicted values
- Average RMSE for age at maturity across three feeding levels equals 6 years, with average error rate of 15% (6 / 39 = 0.15, where 39 years is the highest observed age at maturity for Chelonia mydas); 95% of observed values fall within 11-13 years of predicted values
- Provides MatLab code for calculating nine derived life history traits, population growth rate, demographic resilience, and elasticity analyses

## Method in brief
The DEB-IPM describes population dynamics through four fundamental functions: survival S(L(t)), growth G(L', L(t)), reproduction R(L(t)), and parent-offspring association D(L', L(t)). The survival function incorporates starvation at body length L > Lm * E(Y) / kappa. Growth follows a von Bertalanffy curve with growth rate rB and maximum length Lm = kappa * epsilon * Imax / xi. The reproduction function R(L(t)) = Rm * (L/Lm)^2 * E(Y) applies to adults (Lp <= L <= Lm). Individual variability arises from Gaussian-distributed feeding levels Y with mean E(Y) and standard deviation sigma(Y). The IPM is discretized into 200 length bins for matrix approximation. Population growth rate lambda is the dominant eigenvalue; generation time T = log(R0)/log(lambda).

Eight life history traits are required per species: kappa (fraction of energy to respiration), Lb (length at birth), Lp (length at puberty), Lm (maximum length), mu_j (juvenile mortality rate), mu_a (adult mortality rate), rB (von Bertalanffy growth rate), and Rm (maximum reproduction rate). For elasmobranchs, rB was sourced hierarchically: (i) primary literature using female growth curves, (ii) Froese supplementary material, or (iii) calculated as rB = 3/tmax where tmax is longevity. Adult mortality rate calculated as mu_a = 1/[(tmax + a)/2]. Juvenile mortality rate calculated using survival to maturity. For most species, kappa was taken from the Add My Pet database; if unavailable, kappa = 0.8 was assumed (standard practice). Maximum reproduction rate Rm = (c * n) / i where c is mean clutch size, n is mean litters per year, and i is remigration interval. The projection interval is 1 year; all rates expressed per year, lengths in centimeters.

## Target venue
Scientific Data
