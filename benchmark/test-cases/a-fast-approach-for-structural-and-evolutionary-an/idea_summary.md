# Idea Summary: A Fast Approach for Structural and Evolutionary Analysis Based on Energetic Profile Protein Comparison

## Working title
A Fast Approach for Structural and Evolutionary Analysis Based on Energetic Profile Protein Comparison

## Core question
AbstractIn structural bioinformatics, the efficiency of predicting protein similarity, function, and evolutionary relationships is crucial. Our approach proposed herein leverages protein energy profiles derived from a knowledge-based potential, deviating from traditional methods relying on structural alignment or atomic distances. This method assigns unique energy profiles to individual proteins, facilitating rapid comparative analysis for both structural similarities and evolutionary relationsh

## Motivation / gap
- IntroductionA thorough understanding of protein function holds paramount importance within the domains of biology, medicine, and pharmacy.
- While experimental methods exhibit high accuracy in protein function associations, their inherent limitations, such as being time-intensive and expensive, have instigated the exploration of computatio
- The evaluation of protein similarity by comparing two proteins has consistently emerged as a key methodology.
- This assessment plays a pivotal role in uncovering insights into the functions and evolutionary relationships of proteins.
- Advances in high-throughput technologies have led to the establishment of extensive repositories containing protein sequences, a substantial proportion of which, however, lack annotations1.

## Core contribution (bullet form)
Extracted from abstract:
AbstractIn structural bioinformatics, the efficiency of predicting protein similarity, function, and evolutionary relationships is crucial. Our approach proposed herein leverages protein energy profiles derived from a knowledge-based potential, deviating from traditional methods relying on structural alignment or atomic distances. This method assigns unique energy profiles to individual proteins, facilitating rapid comparative analysis for both structural similarities and evolutionary relationships across various hierarchical levels. Our study demonstrates that energy profiles contain substantial information about protein structure at class, fold, superfamily, and family levels. Notably, these profiles accurately distinguish proteins across species, illustrated by the classification of coronavirus spike glycoproteins and bacteriocin proteins. Introducing a separation measure based on energy profile similarity, our method shows significant correlation with a network-based approach, emphasizing the potential of energy profiles as efficient predictors for drug combinations with faster computational requirements. Our key insight is that the sequence-based energy profile strongly correlates with structure-derived energy, enabling rapid and efficient protein comparisons based solely on sequences.

## Method in brief
MethodsA curated dataset of non-redundant protein chains was utilized from PISCES46. The dataset was selected based on the following criteria:Pairwise sequence identity: Less than 50% to ensure non-redundancy.Resolution: Higher than 1.6 Å to guarantee structural accuracy.R-factor: Below 0.25 to ensure reliable crystallographic data.Protein length: Between 40 and 1,000 residues to include proteins of varying sizes while excluding excessively short or long chains.Overlap: Proteins overlapping with the test sets from this manuscript were removed from the training set.These filtered proteins were utilized to train and calculate the knowledge-based potential function as follows.Pairwise Distance-Dependent Knowledge-Based PotentialKnowledge-based potentials are derived from databases of known protein structures and are essential for estimating the energies of pairwise interactions. These potentials can be based on various factors, including distance dependencies, dihedral angles, and accessible surface areas8. In this study, we employed a distance-dependent potential function where atomic contacts were identified using the tessellation method9, 47, 48 as follows:Contact IdentificationRepresentation: All amino acids in each protein chain were represented by their heavy atoms (excluding hydrogen atoms).Delaunay Tessellation: A Delaunay tessellation of the resulting point set was computed using Qhull49, identifying neighboring atoms based on spatial proximity.Defining Contacts: Two at

## Target venue
Nature Communications
