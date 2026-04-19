# Experimental log: Peafowl alignment-free ML phylogeny estimation

## Datasets

| # | Dataset | Taxa | Data type | Reference source |
|---|---------|------|-----------|------------------|
| 1 | 7 Primates | 7 | Full mitochondrial genomes | Bernard et al. reference [8] |
| 2 | Drosophila | 14 | Real genome skims subsampled to 100 Mb | Sarmashghi et al. reference [25] |
| 3 | 29 E.coli/Shigella | 29 | Assembled genomes | Yi and Jin [10] |
| 4 | 25 Labroidei fish | 25 | Assembled mitochondrial genomes | Fischer et al. [26] |
| 5 | 14 plants | 14 | Full genome sequences | Hatje and Kollmar [27] |
| 6 | 27 E.coli/Shigella | 27 | Full genome sequences | Chan et al. [28] |
| 7 | 8 Yersinia strains | 8 | Full genome sequences | Chan et al. [28] |

## Benchmark methods compared

FFP, co-phylog, mash, Skmer, FSWM/Read-SpaM, andi, phylonium, Multi-SpaM, CAFE-cvtree. Results for these methods on AFproject datasets were obtained directly from the AFproject benchmarking site.

## Primary performance metric

Normalized Robinson-Foulds distance (nRF). Computed as RF distance between estimated and reference tree divided by the maximum possible RF value for that tree size. Lower is better; 0 indicates an exact topological match. RF distances computed with PHYLIP; neighbor-joining and UPGMA trees for distance-matrix outputs built with MEGA-X (UPGMA results in supplementary).

## Peafowl nRF results on the seven datasets (canonical counting unless noted)

| Dataset | Peafowl nRF | Notes |
|---------|-------------|-------|
| 7 Primates | 0 | Tied with andi, Multi-SpaM, FFP; best possible score |
| Drosophila (14 species, 100 Mb skims) | not reported as single number in extracted main text; Peafowl tied with Skmer for lowest nRF along with phylonium; differs from reference by one branch (Drosophila mauritiana, simulans, sechellia) | |
| 29 E.coli/Shigella (assembled) | 0.23 | Outperformed by phylonium (best on this dataset) |
| 25 Labroidei fish (mt) | 0.05 | Tied with mash and FSWM for best |
| 14 plants | 0.36 | Best performers co-phylog, mash, Multi-SpaM; Peafowl ran with k in {9..17} to avoid resource exhaustion |
| 27 E.coli/Shigella (full) | 0.17 | Best performers co-phylog, andi, phylonium with nRF = 0.08 |
| 8 Yersinia strains (canonical) | 1 | Most tools > 0.8; only two methods achieved nRF below 0.8 |
| 8 Yersinia strains (non-canonical) | 0 | Reconstructs reference tree exactly; CAFE-cvtree best among benchmarked tools in the original AFproject comparison |

## Summary statistics

- Datasets on which Peafowl achieves the lowest nRF among compared methods: 3 (out of 7).
- Datasets on which phylonium achieves the lowest nRF: 4.
- Datasets on which Peafowl matches or ties the best method: includes 7 Primates (0), 25 Labroidei fish (0.05), and 8 Yersinia with non-canonical counting (0).

## Selection of k-mer lengths

For all seven datasets, the k-mer length with maximum cumulative entropy (k_entropy) coincided with the lowest observed nRF across the scanned odd k values from 9 to 31.

- 7 Primates: minimum nRF = 0 and maximum entropy both occur at k = 9. A secondary drop in nRF at k = 23 was observed but attributed to the dataset having only 7 species (single branch shifts cause large nRF changes).
- Drosophila (14 species): lowest nRF at k_entropy.
- Yersinia: entropy in non-canonical mode substantially exceeds entropy in canonical mode; non-canonical k_entropy yields the reference tree exactly.

## Methods parameters

| Parameter | Value |
|-----------|-------|
| k-mer counting tool | Jellyfish 2.2.4 |
| k-mer lengths scanned | odd k in {9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31} |
| k-mer lengths scanned for plant and Drosophila datasets | odd k in {9, 11, 13, 15, 17} (to avoid resource exhaustion) |
| Counting mode | Canonical (-r) default; non-canonical for Yersinia HGT experiment |
| Rows sampled for cumulative entropy | p = 5000 |
| Phylogeny estimation tool | RAxML 8.2.4 |
| Substitution model | BINGAMMA (binary-trait substitution model with gamma-distributed site rate prior) |
| Maximum supported taxa | 30 |
| Implementation languages | C++ and shell scripts |
| Benchmark RF distance tool | PHYLIP |
| Distance-matrix tree builders for competitor methods | neighbor-joining and UPGMA in MEGA-X |

## Runtime and peak memory

Hardware: Intel Core i7-7700 CPU at 3.60 GHz, 8 processors, 32 GB RAM.

Table 1 in the paper reports unzipped dataset size, runtime, and peak memory for Peafowl on each dataset. The plant and Drosophila dataset runtimes and memory usage are reported for the reduced k range k in {9, ..., 17}. Exact per-dataset cell values were not included in the extracted table block and are therefore marked "not reported" in quantitative plots generated here.

| Dataset | Unzipped size | Runtime | Peak memory |
|---------|---------------|---------|-------------|
| 7 Primates | not reported | not reported | not reported |
| Drosophila (k in 9..17) | not reported | not reported | not reported |
| 29 E.coli/Shigella | not reported | not reported | not reported |
| 25 Labroidei fish | not reported | not reported | not reported |
| 14 plants (k in 9..17) | not reported | not reported | not reported |
| 27 E.coli/Shigella | not reported | not reported | not reported |
| 8 Yersinia | not reported | not reported | not reported |

## Cumulative entropy equation

C_entropy(k) = sum over p = 5000 randomly sampled rows i of H(X_i)

where for row i across m species, H(X_i) = - sum_{x in {0,1}} f(x) log f(x), with f(x) the empirical frequency of value x in row i. Sites (rows) are assumed independent under the BINGAMMA model for tree likelihood evaluation.

## Statistical tests

No inferential statistical tests (e.g., t-test, Mann-Whitney U, ANOVA) were used in the main benchmarking. Comparisons are descriptive, based on nRF values of each method per dataset.

## Notes and caveats

- For the 14 plants dataset, binary matrices at k = 9 and k = 17 had degenerate entropies (all 1's at k = 9 giving zero entropy; k = 17 omitted for computational reasons), and were excluded from the entropy-variation plot.
- For the 29 E.coli/Shigella dataset, the reference tree was itself constructed from an alignment-based method and has not been thoroughly re-validated.
- Peafowl currently uses only presence/absence of k-mers and ignores their counts; it is limited to at most 30 taxa; it does not estimate branch lengths; and it requires assembled genomes (unassembled reads not yet supported).
