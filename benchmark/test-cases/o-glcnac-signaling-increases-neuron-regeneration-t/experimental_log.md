# Experimental Log: O-GlcNAc and Neuron Regeneration via One-Carbon Metabolism

## Experiment 1: Regenerative outgrowth after laser axotomy

Measured neuron regeneration length (um) 24h post-axotomy in C. elegans.

| Genotype | Mean Regeneration (um) | SEM | n | p-value vs WT |
|---|---|---|---|---|
| Wild-type (N2) | 45.2 | 3.1 | 30 | -- |
| ogt-1 mutant | 72.8 | 4.5 | 32 | <0.001 |
| ogt-1; mel-32 (OCM disrupted) | 43.7 | 3.8 | 28 | 0.78 (vs WT) |
| ogt-1 + OCM inhibitor | 46.1 | 4.0 | 25 | 0.85 (vs WT) |
| ogt-1; cth-1 (TSP disrupted) | 44.5 | 3.4 | 27 | 0.90 (vs WT) |

Key finding: ogt-1 mutation increases regeneration ~60% over WT, but this is fully abolished by disrupting OCM or TSP.

## Experiment 2: Glycolytic flux measurements

| Genotype | Relative Glycolytic Rate | Flux to OCM (fold vs WT) |
|---|---|---|
| Wild-type | 1.00 | 1.00 |
| ogt-1 mutant | 1.85 | 2.40 |
| ogt-1; OCM block | 1.80 | 0.35 |

## Experiment 3: Pathway disruption summary

| Intervention | Blocks OCM? | Blocks TSP? | Regeneration Rescued? |
|---|---|---|---|
| mel-32 RNAi | Yes | Partial | Yes (back to WT) |
| Pharmacological OCM inhibitor | Yes | No | Yes (back to WT) |
| cth-1 mutation | No | Yes | Yes (back to WT) |
| Double (OCM + TSP) | Yes | Yes | Yes (back to WT) |

## Notes

- The ogt-1 mutation channels extra glycolytic output specifically into OCM, not other branches.
- TSP lies downstream of OCM; blocking either is sufficient to abrogate the regeneration phenotype.
- Next step: identify specific TSP metabolites (e.g., glutathione, H2S) that mediate axon regrowth.
