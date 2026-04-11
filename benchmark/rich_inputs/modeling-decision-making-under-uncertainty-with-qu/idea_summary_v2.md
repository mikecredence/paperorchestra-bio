## Working title

Extracting quantitative subjective values from qualitative decision outcomes using hierarchical Bayesian modeling of risk and ambiguity attitudes

## Core question

Can a computational model extract meaningful quantitative subjective values from choices involving qualitative outcomes (e.g., medical treatment improvements), and do ambiguity attitudes show cross-domain consistency between monetary and medical decision-making?

## Motivation / gap

- Decision-making under uncertainty has been extensively studied with quantitative (monetary) outcomes, but many real-world decisions involve qualitative outcomes (e.g., choosing between medical treatments described as "slight improvement" vs. "major improvement") that lack a natural numeric scale
- Existing approaches to studying decisions with non-monetary outcomes either quantify an aspect of the outcome (e.g., milligrams of medication, months of lifespan) or treat qualitative categories as having fixed distances, both of which impose assumptions that may not match subjective experience
- There is no established method for simultaneously estimating subjective values of qualitative outcomes and characterizing risk/ambiguity attitudes within a unified modeling framework
- Whether ambiguity attitudes are consistent across qualitative (medical) and quantitative (monetary) domains has not been tested with a model that extracts individualized values from both
- The medical domain is especially important because health decisions are central to patient care, yet uncertainty attitude characterization in this domain is underdeveloped

## Core contribution (bullet form)

- Developed an "Estimated Value" model using hierarchical Bayesian estimation that extracts individualized quantitative values for qualitative medical outcomes (slight improvement: mean 6.93, SD 1.79; moderate: +9.00, SD 2.62; major: +7.04, SD 2.89; complete recovery: +4.18, SD 2.41 in the in-person sample)
- The Estimated Value model outperformed a classical utility function even for monetary decisions where objective amounts are known, demonstrating that subjective value estimation provides a better fit than assuming objective value
- Found a positive cross-domain association between ambiguity aversion (beta) in monetary and medical domains, with robust regression showing the relationship in both in-person and online samples (89% HDPi reported)
- Replicated all primary findings in an independent online sample of 332 participants (online medical values: slight improvement 8.63, SD 2.54; moderate: +12.62, SD 4.25; significant: +4.66, SD 2.56; complete recovery: +2.37, SD 1.61)
- Validated on 66 in-person participants (cognitively screened with MoCA >= 26) and 332 online participants, spanning ages 18-89

## Method in brief

Participants completed a computerized decision-making task with four blocks: risky monetary, ambiguous monetary, risky medical, and ambiguous medical decisions. In each trial, participants chose between a certain outcome and a lottery offering a potentially better outcome. For monetary decisions, the certain option was $5 and lotteries offered $5, $8, $12, or $25 with risk levels of 25%, 50%, or 75% known probability, or ambiguity levels of 24%, 50%, or 74% occlusion. For medical decisions, the certain option was "no change" in a hypothetical condition and lotteries offered improvement levels (slight, moderate, major/significant, complete recovery) with matching risk and ambiguity structures. Each amount/risk or amount/ambiguity combination was repeated four times, with catch trials included.

The core modeling approach used hierarchical Bayesian estimation. The "Estimated Value" model (Equation 4) estimates subjective values for each outcome level as free parameters, bypassing the need for objective numeric values. This was compared against several alternatives: a No-Subjective Parameters model (Equation 5) that uses raw category distances, a Classical Utility model (Equation 1) with a power-law value function, and hybrid models. For the monetary domain, the Estimated Value model was directly compared to utility-based models that have access to the actual dollar amounts. Ambiguity attitudes (beta parameter) were extracted from each domain separately, and cross-domain associations were tested using robust regression with 89% highest density posterior intervals (HDPi). The in-person sample (n=66 after exclusions; MoCA >= 26 screening) was complemented by an independent online replication sample (n=332).

## Target venue

PLOS Computational Biology
