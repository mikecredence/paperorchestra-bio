## Working title

A time-irreversible nucleotide substitution model for SARS-CoV-2 evolution

## Core question

Can we build a nucleotide substitution model that accounts for the strong directional C-to-U mutation bias observed in SARS-CoV-2, and use it to accurately estimate substitution rates?

## Motivation / gap

- SARS-CoV-2 genome sequences show a dramatic overrepresentation of C-to-U substitutions, likely driven by host APOBEC deaminase editing
- Traditional phylogenetic substitution models (e.g., GTR) are time-reversible and cannot capture this asymmetry
- Accurate substitution rate estimation is needed to predict the evolutionary trajectory of the virus

## Core contribution

- Propose a new time-irreversible nucleotide substitution model that explicitly allows asymmetric rates (especially C->U vs. U->C)
- Develop a companion estimation method for substitution rates under this model
- Validate the method with computer simulations showing accurate rate recovery
- Apply the method to real SARS-CoV-2 sequences, finding C-to-U rate is roughly 10x higher than other substitution types

## Method in brief

- Formulate a rate matrix that does not enforce detailed balance (time-irreversibility)
- Derive maximum-likelihood or moment-based estimators for the rate parameters
- Simulate sequence evolution under the model to benchmark estimation accuracy
- Apply the estimator to aligned SARS-CoV-2 genome sequences from public databases

## Target venue

NAR Genomics and Bioinformatics
