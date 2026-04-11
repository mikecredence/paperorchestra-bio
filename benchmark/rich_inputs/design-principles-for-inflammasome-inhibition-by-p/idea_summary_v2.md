# Idea Summary

## Working title
Design Principles for Inflammasome Inhibition by Pyrin-Only-Proteins

## Core question
How do endogenous pyrin-only-proteins (POPs) recognize and inhibit different inflammasome PYD filaments, and what are the intrinsic target specificities and inhibitory mechanisms of POP1, POP2, and POP3?

## Motivation / gap
- Inflammasomes are irreversible filamentous signaling platforms; once assembled they do not dissociate and can self-perpetuate in a prion-like manner
- Dysregulated inflammasome activity is linked to autoinflammatory disorders, cancer, and severe COVID-19
- POPs were identified as endogenous regulators that block PYD filament assembly, but their intrinsic target specificities have remained speculative
- The previous report that POP1 directly inhibits the central adaptor ASC was based on indirect evidence from cell-based overexpression assays, not direct biochemical measurements
- No systematic study had combined computational (Rosetta) and biochemical approaches to define which PYD filaments each POP targets and through what mechanism (nucleation vs. elongation inhibition)
- Understanding the molecular rules governing POP-PYD recognition could inform therapeutic strategies for inflammasome-driven diseases

## Core contribution (bullet form)
- Demonstrated via Rosetta interface analysis and biochemical assays that POP1 is a poor inhibitor of ASCPYD, contradicting the prior model; instead POP1 inhibits upstream receptor PYD filaments (AIM2, IFI16, NLRP3, NLRP6)
- Showed that POP2 both suppresses nucleation of ASC (prolonged lag phases in polymerization) and inhibits elongation of receptor filaments
- Found that POP3 potently suppresses ASC nucleation and additionally inhibits elongation of AIM2 and NLRP6 filaments
- Revealed that effective POP-PYD recognition requires a combination of favorable and unfavorable interactions at the six unique filament interface surfaces, as determined by Rosetta energy scoring
- Established that POPs inhibit polymerization without co-assembling into filaments, in contrast to COPs which co-assemble with caspase-1 CARD filaments
- Showed that excess (super-stoichiometric) POP concentrations are needed for inhibition, especially in the presence of activating ligands like dsDNA

## Method in brief
The study uses a Rosetta-based in silico approach to map interaction energies at all six unique protein-protein interfaces in PYD helical filaments. A honeycomb-like sideview of the filament is constructed where each protomer provides Type 1a/b, 2a/b, and 3a/b interaction surfaces. The center protomer is replaced with each POP to compute interface energies (delta-G values) for all POP-PYD pairings. Cryo-EM structures of ASCPYD (PDB: 3j63), AIM2PYD (PDB: 7k3r), NLRP3PYD (PDB: 7pdz), and NLRP6PYD (PDB: 6ncv) served as templates, while POP1 used its crystal structure (PDB: 4qob) and POP2/POP3 were homology-modeled.

Biochemically, FRET-based and fluorescence anisotropy (FA)-based quantitative polymerization assays were performed. MBP-tagged PYD constructs were triggered for assembly by TEVp cleavage in the presence of increasing POP concentrations. Half-times for polymerization (t1/2) were measured, and IC50 values were calculated as the POP concentration that reduces 1/(t1/2) by 50%. Cell-based validation used HEK293T cells co-transfected with mCherry-tagged PYDs and eGFP-tagged POPs, with filament formation quantified by automated fluorescence microscopy. nsEM confirmed that POPs remain monomeric and do not form filaments themselves.

## Target venue
eLife
