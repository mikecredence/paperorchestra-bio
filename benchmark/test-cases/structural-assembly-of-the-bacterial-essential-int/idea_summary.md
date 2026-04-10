## Working title

Structural Assembly of the Bacterial Essential Interactome

## Core question

Can we use AlphaFold2 to systematically predict the structural assembly of essential protein-protein interactions in bacteria, and can this reveal novel drug targets?

## Motivation / gap

- Understanding bacterial protein-protein interactions is fundamental for identifying drug targets, but the bacterial interactome remains poorly characterized structurally.
- Experimental structure determination of all essential protein complexes is infeasible at scale.
- Deep learning protein folding algorithms (AlphaFold2) have not been systematically applied to predict the full essential interactome of bacteria.

## Core contribution

- Model 1,089 interactions between essential bacterial proteins using AlphaFold2
- Generate 115 high-accuracy structural models of essential protein complexes
- Reveal previously unknown assembly mechanisms and structural features important for complex stability
- Identify several novel protein-protein interactions that represent new drug targets
- Provide a generalizable framework for predicting interactomes in other bacteria

## Method in brief

- Curate list of essential proteins in bacteria from literature and databases
- Generate all pairwise interaction predictions (1,089 pairs) using AlphaFold2 multimer
- Filter for high-confidence models based on predicted accuracy metrics (pLDDT, PAE, ipTM)
- Structural analysis of the 115 high-accuracy models for interface features
- Identify novel interactions not previously reported
- Assess druggability of novel interaction interfaces

## Target venue

eLife
