# Experimental Log: fastBE -- Structured Regression for Tumor Phylogeny

## Methods Compared

| Method | Type | Scales to Large n? | Requires Mutation Clustering? | Reference |
|--------|------|--------------------|-----------------------------|-----------|
| fastBE | Structured L1 regression + greedy search | Yes (1000+ clones) | No | This work |
| Pairtree | MCMC-based | No (fails beyond ~10 clones) | Yes | [11] |
| Orchard | Beam search | Partial | No | [12] |
| CALDER | Longitudinal constraints | No | Yes | [10] |
| CITUP | Enumeration-based | No | Yes | [7] |

## Problem Formulations Compared (Table 1)

| Method | Loss Function | Key Constraints |
|--------|--------------|-----------------|
| CITUP | L2 loss: ||F - UB||_2^2 | U >= 0, U*1 <= 1 |
| Pairtree | Weighted L2 | U >= 0, U*1 <= 1, clustering penalties |
| CALDER | L2 with longitudinal constraint | U >= 0, U*1 <= 1, temporal consistency |
| Orchard | L1 loss: ||F - UB||_1 | U >= 0, U*1 <= 1 |
| fastBE | L1 loss: ||F - UB||_1 | U >= 0, U*1 <= 1 |

## Experiment 1: Runtime Comparison -- Regression Algorithm vs. LP Solvers

### Setup

| Parameter | Value |
|-----------|-------|
| Number of instances | 264 |
| Clone counts (n) | 250, 500, 750, 1000 |
| Sample counts (m) | 50, 100, 200, 500 |
| LP solvers compared | Gurobi v9.0.3, CPLEX v22.1.0 |
| Metric | Wall-clock runtime (solve time only, excluding LP construction) |

### Speedup Results

| Comparison | Mean Speedup |
|------------|-------------|
| fastBE regression vs. Gurobi | 95.6x faster |
| fastBE regression vs. CPLEX | 105.1x faster |

- Supp Fig 1: Relative wall-clock runtime comparison shows consistent speedup across all (n, m) combinations
- Supp Fig 2: Absolute runtimes show LP solvers scale poorly with increasing n and m

## Experiment 2: Warm Start vs. Cold Start

### Setup

| Parameter | Value |
|-----------|-------|
| Number of base instances | 264 |
| SPR perturbations per instance | 25,000 |
| Clone counts (n) | 250, 500, 750, 1000 |
| Sample counts (m) | 50, 100, 200, 500 |

### Warm Start Results

| Setting | Description | Mean Speedup |
|---------|-------------|-------------|
| Cold start | Regression algorithm run from scratch for each SPR tree | Baseline |
| Warm start | Recomputation using Corollary 1 after single SPR | 6.2x faster than cold start |

- Supp Fig 3: Relative runtime comparison shows consistent warm-start advantage
- Supp Fig 4: Absolute runtimes for warm vs. cold across varying n and m
- LP solvers provide no warm-start capability for this problem

## Experiment 3: Simulated Data -- Small Instances (n <= 10)

### Setup

| Parameter | Value |
|-----------|-------|
| Clone counts (n) | 3, 5, 10 |
| Sample counts (m) | 5, 10, 25 |
| Total simulated instances | 108 |
| Coverage | 40x |
| Metric | F1-score for pairwise relationship reconstruction |

### Completion Rate

| Method | Instances Completed (of 108) | Completion Rate |
|--------|------------------------------|-----------------|
| fastBE | 108 | 100% |
| Pairtree | 108 | 100% |
| Orchard | 108 | 100% |
| CALDER | 106 | 98.1% |
| CITUP | 107 | 99.1% |

### F1-Score at n=10 Clones (Mean)

| Method | Mean F1-Score |
|--------|--------------|
| fastBE | 0.965 |
| Pairtree | 0.972 |
| Orchard | 0.965 |
| CALDER | Lower (not exact value reported) |
| CITUP | Lower (not exact value reported) |

- Fig 3 (left): F1-score vs. number of clones shows fastBE, Pairtree, and Orchard perform nearly identically for small instances
- Supp Fig 5: False positive rate and false negative rate for pairwise reconstruction across all small instances
- Supp Fig 6: Normalized L1 matrix error for usage matrix U and frequency reconstruction

## Experiment 4: Simulated Data -- Large Instances (n >= 100)

### Setup

| Parameter | Value |
|-----------|-------|
| Clone counts (n) | Up to 1000+ |
| Sample counts (m) | Up to hundreds |
| Time limit | 24 hours |

### Scalability Results

| Method | Scales Beyond 10 Clones? | Max Clones Tested |
|--------|-------------------------|-------------------|
| fastBE | Yes | 1000+ |
| Orchard | Partially | Some large instances |
| Pairtree | No (fails to complete in 24h) | ~10 |
| CALDER | No | ~10 |
| CITUP | No | ~10 |

- Fig 3 (right): Wall-clock runtime on instances with >= 100 clones vs. number of samples
- Only fastBE and Orchard appear in this plot; other methods excluded for not scaling
- fastBE demonstrates superior runtime scaling compared to Orchard on large instances

### Accuracy on Large Instances

| Method | Observation |
|--------|-------------|
| fastBE | Outperforms existing approaches in reconstruction accuracy |
| fastBE | Better sample efficiency (requires fewer samples for same accuracy) |
| fastBE | Fastest runtime |

## Experiment 5: Real Data -- B-Progenitor ALL (14 Patients)

### Dataset

| Parameter | Value |
|-----------|-------|
| Cancer type | B-progenitor acute lymphoblastic leukemia (B-ALL) |
| Number of patients | 14 |
| Data type | Multi-sample bulk DNA sequencing |

### Sum Condition Violation (Fig 4a)

| Metric | Description |
|--------|-------------|
| Total violation | Sum of violations of the constraint that clone frequencies must sum to <= 1 per sample |
| Lower violation = better | Indicates better fit to evolutionary constraints |

| Method | Relative Performance on Sum Condition |
|--------|--------------------------------------|
| fastBE | Fewer violations across most patients |
| Pairtree | More violations |

- Fig 4a: Bar chart comparing total sum-condition violation for phylogenies inferred by fastBE vs. Pairtree across all 14 patients
- fastBE infers similar phylogenies to Pairtree but with fewer constraint violations
- fastBE shows better agreement with observed mutational frequencies

## Experiment 6: Real Data -- Colorectal Cancer Models (2 Patients)

### Dataset

| Parameter | Value |
|-----------|-------|
| Cancer type | Patient-derived colorectal cancer models |
| Number of patients | 2 (POP66, CSC28) |
| Data source | [45] in references |

### POP66 Results (Fig 4b)

| Metric | fastBE | Pairtree |
|--------|--------|----------|
| Per-sample sum condition violation | Lower | Higher |

- Fig 4b: Per-sample violation comparison shows fastBE has less violation

### CSC28 Results (Fig 4c-d)

| Aspect | fastBE | Pairtree |
|--------|--------|----------|
| Phylogeny topology | Distinct from Pairtree | Distinct from fastBE |
| Interpretation of heterogeneity | Different subclonal structure | Different subclonal structure |
| Sum condition violation | Fewer violations | More violations |

- Fig 4c: fastBE-inferred phylogeny for CSC28
- Fig 4d: Pairtree-inferred phylogeny for CSC28
- Each vertex corresponds to a distinct subclone
- The two methods lead to different interpretations of intra-tumor heterogeneity

## Algorithmic Complexity Summary

| Operation | Time Complexity | Space |
|-----------|----------------|-------|
| L1-VAFRP solution (Theorem 1) | O(mnd) | O(mnd) |
| SPR recomputation (Corollary 1) | O(md * max(d(i), d(j))) | Uses precomputed data |
| fastBE full algorithm (per iteration) | Sum over placements, dominated by regression evaluations | -- |
| Naive LP for L1-VAFRP | Substantially slower (95-105x) | -- |

Where: m = number of samples, n = number of clones/mutations, d = depth of tree

## Key Definitions

| Term | Definition |
|------|-----------|
| Clonal tree | Rooted tree where vertices = clones, edges labeled by mutations |
| Clonal matrix B_T | n-by-n binary matrix; B(i,j)=1 iff clone i descends from or equals clone j |
| Usage matrix U | m-by-n matrix; U(s,i) = fraction of clone i in sample s |
| Frequency matrix F | m-by-n matrix; F = UB gives observed variant allele frequencies |
| VAFFP | Variant allele frequency factorization problem: find T and U minimizing loss |
| L1-VAFRP | Regression subproblem for fixed T: minimize ||F - UB_T||_1 |
| Sum condition | Constraint that clone frequencies in each sample sum to <= 1 |
| SPR | Subtree prune-and-regraft: tree topology modification operation |
| ISA | Infinite sites assumption: each locus mutated exactly once |
| Sequencing coverage | 40x in simulations |

## Software and Implementation

| Component | Detail |
|-----------|--------|
| Language | C++ |
| Repository | github.com/raphael-group/fastBE |
| LP solvers for comparison | Gurobi v9.0.3, CPLEX v22.1.0 |
| Input | Multi-sample bulk DNA sequencing read counts |
| Output | Clonal tree (phylogeny) |

## Evaluation Metrics

| Metric | Description | Used In |
|--------|-------------|---------|
| F1-score | Accuracy of pairwise ancestral relationships | Simulated data |
| False positive rate | Fraction of incorrectly inferred ancestral relationships | Simulated data (Supp) |
| False negative rate | Fraction of missed ancestral relationships | Simulated data (Supp) |
| Normalized L1 matrix error (U) | ||U - U_hat||_1 normalized | Simulated data (Supp) |
| Normalized L1 matrix error (F) | ||F - UB||_1 normalized | Simulated data (Supp) |
| Sum condition violation | Total constraint violation | Real data |
| Wall-clock runtime | Execution time in seconds | All experiments |

## Simulation Parameters

| Parameter | Values Tested |
|-----------|---------------|
| Number of clones (n) | 3, 5, 10, 100, 250, 500, 750, 1000+ |
| Number of samples (m) | 5, 10, 25, 50, 100, 200, 500 |
| Sequencing coverage | 40x |
| Read sampling | Variant and non-variant reads sampled from F |
| Tree generation | Random clone trees with random usage matrices |
| Frequency computation | F = UB |

## Limitations and Future Directions

| Limitation | Potential Improvement |
|-----------|----------------------|
| Time complexity O(mnd) vs. optimal O(mn) | Open theoretical question |
| Only handles SNVs in copy-neutral regions | Extend to copy number heterogeneity (CCF or DCF) |
| Infinite sites assumption only | Support Dollo model and generalizations for mutation loss |
| No uncertainty estimates | Add confidence intervals or posterior sampling |
| No automatic mutation clustering | Could integrate clustering as optional preprocessing |
| No longitudinal consistency enforcement | Could add temporal constraints as in CALDER |

## Reference Count

- Total references cited: 44
