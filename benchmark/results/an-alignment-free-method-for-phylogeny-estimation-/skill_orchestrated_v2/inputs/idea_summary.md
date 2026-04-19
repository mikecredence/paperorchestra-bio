## Working title
An Alignment-free Method for Phylogeny Estimation using Maximum Likelihood

## Core question
Can a maximum-likelihood alignment-free phylogeny estimation approach based on the presence/absence of k-mers in genome sequences achieve performance competitive with state-of-the-art distance-based alignment-free methods across heterogeneous genome datasets?

## Motivation / gap
- Alignment-based phylogenetic inference (both distance- and character-based) requires multiple sequence alignment (MSA) which is memory- and time-intensive and computationally intractable to optimize exactly for large genomes.
- Alignment-based methods assume preserved linear order of homology, making them brittle to rearrangement events (translocation, inversion) common in whole-genome data.
- Alignment-free methods bypass MSA and scale to whole genomes and genome skims where assembly is impractical, but the majority developed to date are distance-based (e.g., co-phylog, andi, mash, Multi-SpaM) and rely on simplified pairwise distance models.
- In the alignment-based setting, character-based maximum-likelihood methods have been shown to outperform distance-based methods, motivating a likelihood-based alignment-free counterpart.
- Prior likelihood-style alignment-free work (Hoehl and Ragan) used a Bayesian approach but no widely used maximum-likelihood alignment-free tool exists.

## Core contribution (bullet form)
- We present Peafowl (Phylogeny Estimation through Alignment Free Optimization With Likelihood), the first alignment-free phylogeny tool that uses maximum-likelihood tree estimation on a k-mer presence/absence binary matrix.
- We provide an entropy-based, data-driven procedure for selecting the k-mer length (k_entropy) by maximizing cumulative entropy over p = 5000 randomly selected rows of the binary matrix, over odd k in {9, 11, ..., 31}.
- We evaluate Peafowl on seven real datasets (7 Primates mitochondrial genomes; 14 Drosophila genome skims subsampled to 100 Mb; 29 E.coli/Shigella assembled genomes; 25 Labroidei fish mitochondrial genomes; 14 plant genomes; 27 E.coli/Shigella full genomes; 8 Yersinia full genomes) and compare against FFP, co-phylog, mash, Skmer, FSWM/Read-SpaM, andi, phylonium, Multi-SpaM, and CAFE-cvtree using the AFproject benchmarking framework.
- On the 7 Primates and 25 Labroidei fish datasets, Peafowl achieves nRF = 0 and nRF = 0.05 respectively, tying the best methods; with non-canonical counting it reconstructs the reference tree exactly on the 8 Yersinia strains (nRF = 0), a dataset dominated by genome inversions on which most tools perform poorly (nRF > 0.8 for most).
- Peafowl uses the RAxML BINGAMMA substitution model for binary traits (gamma prior on site mutation rates) and relies on Jellyfish 2.2.4 for canonical or non-canonical k-mer counting; the tool is implemented in C++ and shell scripts and released open source at https://github.com/hasin-abrar/Peafowlrepo.
- Peafowl estimates tree topologies only; branch-length estimation is left as future work because neighboring k-mers are not independent under a single nucleotide substitution, violating the independence assumption of the binary-trait model.

## Method in brief
Peafowl takes a set of input DNA sequences (one per species) and produces a phylogenetic tree topology in four steps. First, k-mer counting: Jellyfish 2.2.4 enumerates all k-mers in each input sequence for odd k in {9, 11, ..., 31}. Users may choose canonical counting (a k-mer and its reverse complement are collapsed) or non-canonical counting (the two are distinct). Canonical counting is the default because assembled sequences may come from either strand; non-canonical counting is useful when the signal of interest is inversion rearrangement, since inversions are otherwise invisible to canonical counting except at inversion boundaries.

Second, binary-matrix construction: for each k, a matrix X is built whose rows are unique k-mers and whose columns are species; X_ij = 1 if the k-mer (or its reverse complement, in canonical mode) is present in species j and 0 otherwise. A hash table indexed by k-mer maps each k-mer to the species in which it was observed. Third, k-mer length selection: cumulative entropy C_entropy(k) is computed over p = 5000 randomly selected rows of X. For each row i, the per-row entropy uses the empirical frequencies of 0 and 1 across the m species. Odd k in {9, 11, ..., 31} are ranked, and k_entropy = argmax_k C_entropy(k) is chosen because intermediate-frequency k-mers (neither ubiquitous nor extremely rare) carry the most phylogenetic information.

Fourth, tree estimation: the binary matrix corresponding to k_entropy is fed into RAxML 8.2.4 under the BINGAMMA substitution model, which is a two-state (0/1) substitution model with a gamma prior on site rates, to obtain the maximum-likelihood tree topology. Performance is evaluated using the normalized Robinson-Foulds (nRF) distance between the estimated and reference trees; smaller is better. Reference methods that output a distance matrix (e.g., mash, Skmer) are post-processed with neighbor-joining in MEGA-X, with UPGMA results reported in the supplementary material, and RF distances are computed with PHYLIP.

## Target venue
BMC Bioinformatics
