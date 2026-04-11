## Working title

fastBE: Scalable phylogenetic reconstruction from multi-sample bulk DNA sequencing via structured regression on clonal matrices

## Core question

Can the NP-complete variant allele frequency factorization problem (VAFFP) for tumor phylogeny reconstruction be practically solved at large scale by decomposing it into a tractable structured L1-regression subproblem (for a fixed tree) and a deterministic search over tree space, and does this approach outperform existing methods on datasets with hundreds of samples and thousands of clones?

## Motivation / gap

- Intra-tumor heterogeneity is more prevalent than previously appreciated (e.g., TracerX found up to 15 subclones in NSCLC, noting 65% of subclones would be missed without multi-region sequencing)
- Recent datasets contain up to 90 samples and 26 subclones per patient, and this scale is growing
- Existing phylogeny methods (Pairtree, CALDER, CITUP) do not scale beyond ~10 subclones in practice
- All existing methods except Orchard require pre-clustering mutations into clones, potentially losing phylogenetic signal
- Structured regression has been very successful in distance-based species phylogenetics (FastME, FastTree) but has not been applied to tumor evolution
- There is no efficient algorithm exploiting the unique combinatorial structure of clonal matrices for the L1-regression subproblem

## Core contribution (bullet form)

- Derived an O(mnd)-time algorithm for the L1-VAFRP (regression subproblem) by exploiting the combinatorial structure of clonal matrices, achieving mean 95.6x speedup over Gurobi and 105.1x over CPLEX LP solvers
- Developed warm-start capability enabling 6.2x faster recomputation after subtree prune-and-regraft (SPR) operations compared to cold starts
- Built fastBE, a deterministic beam-search algorithm for the full L1-VAFFP that iteratively constructs phylogenies one mutation at a time
- On simulated data with up to 1000+ clones and hundreds of samples, fastBE outperforms Pairtree, Orchard, CALDER, and CITUP in reconstruction accuracy (F1-score), sample efficiency, and runtime
- fastBE enables phylogenetic reconstruction directly from individual mutations without clustering into clones -- a first among scalable methods
- On real B-ALL patient data (14 patients) and colorectal cancer models (2 patients), fastBE produces phylogenies with fewer sum-condition violations and better agreement with observed mutational frequencies compared to existing methods

## Method in brief

The approach separates tumor phylogeny inference into two components. First, for a fixed clonal tree T with n vertices, the problem of finding the best usage matrix U (describing clone fractions across m samples) reduces to an L1-regression problem: minimize ||F - UB_T||_1 subject to U >= 0, U*1 <= 1, where F is the observed frequency matrix and B_T is the clonal matrix encoding clone genotypes. This is the L1-VAFRP. The key insight is that the clonal matrix B_T has a unique combinatorial structure (it is a binary matrix where entry (i,j) = 1 iff clone i is descended from or equal to clone j), enabling an algorithm running in O(mnd) time where d is the tree depth, with warm-start updates for SPR operations in O(md * max(d(i),d(j))) time.

Second, the search over tree space uses a deterministic greedy algorithm inspired by beam search. fastBE iteratively builds the phylogeny by adding one mutation at a time in a fixed order, choosing for each new mutation the parent vertex and subset of children to adopt that minimizes the L1 loss. This exploits the efficient recomputation capabilities of the regression algorithm. The total running time is dominated by the sum of regression evaluations across all possible placements at each iteration.

The method outputs a single phylogenetic tree without requiring pre-clustering of mutations or MCMC sampling. It is implemented in C++ for computational efficiency and is available open-source.

## Target venue

PLOS Computational Biology
