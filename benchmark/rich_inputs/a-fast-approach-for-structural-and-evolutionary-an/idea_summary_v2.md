# Idea Summary

## Working title
A Fast Approach for Structural and Evolutionary Analysis Based on Energetic Profile Protein Comparison

## Core question
Can knowledge-based energy profiles derived from amino acid composition serve as a fast, alignment-free alternative for assessing protein structural similarity and evolutionary relationships?

## Motivation / gap
- Traditional protein comparison relies on structural alignment (e.g., TM-score, RMSD) or sequence alignment (e.g., BLAST), both of which are computationally expensive at scale
- Existing methods struggle with the growing volume of unannotated protein sequences in databases
- Structure-based methods require solved 3D structures, which are unavailable for many proteins
- There is no widely adopted approach that captures structural information purely from sequence composition in a fixed-length, alignment-free representation
- Drug combination prediction methods based on network separation are slow; a faster proxy is needed

## Core contribution (bullet form)
- Developed a 210-dimensional energy profile (Compositional Profile of Energy, CPE) derived solely from amino acid pair frequencies, which strongly correlates with structure-based energy profiles (Pearson r near 1.0 on ASTRAL40 and ASTRAL95 datasets)
- Demonstrated that CPE achieves 100% classification accuracy on a CATH benchmark of 251 protein domains using a 1-nearest-neighbor classifier, matching TM-Vec but completing the task in approximately 1 second vs. 67 seconds for TM-Vec
- Showed that energy profiles capture hierarchical structural information at SCOP class, fold, superfamily, and family levels via UMAP visualization
- Reconstructed phylogenetic networks of the ferritin-like superfamily that recapitulate known evolutionary relationships, with Spearman correlations to a manually curated reference network
- Successfully clustered coronavirus spike glycoproteins (SARS-CoV, SARS-CoV-2, MERS-CoV) by virus of origin using CPE
- Demonstrated significant correlation between the CPE-based separation measure and network-based drug combination predictions, providing a computationally faster alternative

## Method in brief
The method begins by constructing a distance-dependent knowledge-based potential from a curated, non-redundant set of PDB chains (sequence identity < 50%, resolution < 1.6 A, R-factor < 0.25, length 40-1000 residues). Atomic contacts are identified via Delaunay tessellation, and pairwise energies are computed across 30 distance shells (starting at 0.75 A, width 0.5 A each) for 167 atom types. The potential energy between atom types i and j at distance d follows the Sippl formulation: E(i,j,d) = -RT * ln[f_ij(d) / f_xx(d)], weighted by observation counts.

From these atomic potentials, residue-level pairwise energies are summed, yielding a 210-dimensional vector (one entry per unique amino acid pair) called the Structural Profile of Energy (SPE). A predictor matrix P is then estimated to approximate these pairwise energies directly from amino acid composition, producing the Compositional Profile of Energy (CPE). The Manhattan distance between two proteins' CPE vectors serves as the dissimilarity measure, requiring no alignment and running in constant time per comparison.

For evaluation, the approach is benchmarked against GR-Align, RMSD, TM-score, Yau-Hausdorff distance, and TM-Vec on SCOP/CATH-classified domains. Phylogenetic networks are built using NeighborNet with the phangorn package. Drug combination analysis uses a separation measure analogous to network-based methods but computed from energy profile distances.

## Target venue
Nature Communications
