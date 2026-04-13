Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: BMC Bioinformatics

## Idea Summary

# Idea Summary: Alignment-Free Phylogeny Estimation Using Maximum Likelihood

## Working title
An alignment-free method for phylogeny estimation using maximum likelihood

## Core question
Can a maximum likelihood approach be applied to alignment-free phylogenetic inference (using k-mer presence/absence binary matrices), and does it achieve competitive accuracy compared to existing distance-based alignment-free methods?

## Motivation / gap
- Sequence alignment is a bottleneck for phylogenetic inference: memory- and time-consuming, difficult to scale to whole genomes and long sequences
- Optimal multiple sequence alignment is computationally intractable as the number of possible alignments grows exponentially with sequence length
- Rearrangement events (translocations, inversions) within whole genomes complicate alignment-based approaches
- Alignment-free methods are crucial for data types like genome skims where assembly is impractical
- Existing alignment-free methods rely on simplified pairwise distance calculations, which limits their accuracy
- In the alignment-based world, maximum likelihood consistently outperforms distance-based methods, but no alignment-free method has leveraged ML estimation
- No single existing alignment-free method achieves best scores across all datasets, indicating the field is far from solved

## Core contribution (bullet form)
- Developed Peafowl, the first alignment-free phylogeny estimation tool using maximum likelihood (via RAxML on k-mer binary matrices)
- Introduced an entropy-based approach for automatic selection of optimal k-mer length (kentropy) from odd k values ranging 9-31
- Achieved lowest nRF distance on 3 of 7 real datasets; phylonium achieved lowest on 4 datasets
- On the Yersinia dataset, Peafowl matched the reference tree perfectly when run in non-canonical counting mode (suited for detecting inversions)
- Demonstrated competitive performance on both mitochondrial genomes (7 Primates) and genome-scale data (14 Drosophila species with 100 Mb genome skims)
- Benchmarked against 9 state-of-the-art alignment-free tools (FFP, co-phylog, mash, Skmer, FSWM/Read-SpaM, andi, phylonium, Multi-SpaM, CAFE-cvtree)

## Method in brief
Peafowl operates in four steps. First, k-mers of various odd lengths (9 to 31) are generated from input DNA sequences using Jellyfish. The tool supports both canonical counting (k-mer and its reverse complement treated as the same) and non-canonical counting. Second, for each k-mer length, a binary matrix is constructed where rows represent k-mers and columns represent species, with entries indicating presence (1) or absence (0) of each k-mer in each genome. Third, an appropriate k-mer length is automatically selected based on cumulative entropy values across the binary matrices; the selected kentropy corresponds to a knee point in the entropy curve. Fourth, the binary matrix at the selected k-mer length is provided as input to RAxML for maximum likelihood phylogenetic tree estimation.

The entropy-based k-mer selection is a key innovation. Short k-mers tend to be present in all species (low entropy, low phylogenetic signal), while very long k-mers may be unique to individual species (high entropy but potentially noisy). The optimal k-mer length balances informativeness with conservation across the taxa. The binary matrix encoding of k-mer presence/absence transforms the alignment-free data into a character-based format suitable for ML inference, bridging the gap between alignment-free data preparation and the statistical power of likelihood-based tree estimation. The tool currently handles up to 30 taxa and works on assembled sequences or genomes.

## Target venue
BMC Bioinformatics


## Experimental Log

# Experimental Log: Alignment-Free Phylogeny Estimation Using Maximum Likelihood

> Data tables and results extracted from full-text analysis

---

## Datasets Used for Benchmarking

| Dataset | Taxa | Sequence Type | Source |
|---|---|---|---|
| 7 Primates | 7 | Full mitochondrial genomes | Ref [8] |
| Drosophila | 14 | Real genome skims (subsampled to 100 Mb) | Ref [25] |
| E.coli/Shigella (29) | 29 | Assembled sequences | AFproject / Ref [10] |
| Labroidei (fish) | 25 | Assembled mitochondrial genomes | AFproject / Ref [26] |
| Plants | 14 | Full genome sequences | AFproject / Ref [27] |
| E.coli/Shigella (27) | 27 | Full genome sequences | AFproject / Ref [28] |
| Yersinia | 8 | Full genome sequences | AFproject / Ref [28] |

---

## Benchmarked Methods

| Method | Type | Reference |
|---|---|---|
| Peafowl (this work) | ML on k-mer binary matrix | - |
| FFP | Distance-based, alignment-free | Refs [30,31] |
| co-phylog | Distance-based, alignment-free | Ref [10] |
| mash | Distance-based, alignment-free | Ref [12] |
| Skmer | Distance-based, alignment-free | Ref [25] |
| FSWM/Read-SpaM | Spaced-word based | Refs [32,33] |
| andi | Distance-based, alignment-free | Ref [11] |
| phylonium | Distance-based, alignment-free | Ref [34] |
| Multi-SpaM | Spaced-word based | Ref [13] |
| CAFE-cvtree | Composition vector | Ref [35] |

- Distance-based tools produce a distance matrix, not a tree directly
- For Primates and Drosophila datasets, neighbor-joining and UPGMA (MEGA-X) applied to distance matrices
- RF distances computed using PHYLIP
- nRF values reported from neighbor-joining trees (UPGMA in supplementary)

---

## Performance Metric

| Metric | Description |
|---|---|
| Robinson-Foulds (RF) distance | Count of dissimilar partitions between estimated and reference trees |
| Normalized RF (nRF) | RF divided by maximum possible RF value |
| Interpretation | Lower nRF = more congruent with reference tree |

---

## nRF Distance Results: Primates and Drosophila (Fig. 4)

| Method | 7 Primates (nRF) | Drosophila (nRF) |
|---|---|---|
| Peafowl | 0.00 (matches reference) | Competitive (among lowest) |
| Skmer | Non-zero | Competitive |
| Mash | Non-zero | Higher nRF |
| FFP | Reported | Reported |
| co-phylog | Reported | Reported |
| FSWM | Reported | Reported |
| andi | Reported | Reported |
| phylonium | Reported | Reported |
| Multi-SpaM | Reported | Reported |

- Fig. 4 shows bar chart comparison of nRF distances across all methods for both datasets
- Fig. 5a: Peafowl's estimated tree for Primates is identical to the reference tree
- Fig. 5a: Skmer and Mash trees for Primates show differences from reference (red branches)
- Fig. 5b: Peafowl and Skmer trees for Drosophila compared against reference

---

## nRF Distance Results: AFproject Datasets (Fig. 6)

| Method | E.coli/Shigella (29) | Labroidei (25) | Plants (14) | E.coli/Shigella (27) | Yersinia (8) |
|---|---|---|---|---|---|
| Peafowl | Competitive | Competitive | Competitive | Competitive | Non-zero (canonical) / 0.00 (non-canonical) |
| phylonium | Best on 4 datasets | - | - | - | - |
| Other methods | Variable | Variable | Variable | Variable | Variable |

- Fig. 6 shows bar chart comparison across AFproject datasets
- Peafowl achieves lowest nRF on 3 of 7 total datasets
- phylonium achieves lowest nRF on 4 of 7 total datasets
- No single method dominates across all datasets

### Peafowl Performance Summary Across All Datasets

| Dataset | Peafowl Rank | Best Method |
|---|---|---|
| 7 Primates | Best (nRF=0) | Peafowl |
| Drosophila | Among best | Variable |
| E.coli/Shigella (29) | Competitive | Variable |
| Labroidei (25) | Competitive | phylonium |
| Plants (14) | Competitive | phylonium |
| E.coli/Shigella (27) | Competitive | phylonium |
| Yersinia (8) | Best (non-canonical mode, nRF=0) | Peafowl |

---

## K-mer Length Selection (Entropy Analysis)

### K-mer Range and Selection Strategy

| Parameter | Value |
|---|---|
| K-mer values tested | Odd values from 9 to 31 |
| Selection criterion | Cumulative entropy (knee point) |
| K-mer generation tool | Jellyfish |
| Counting modes | Canonical (default) and non-canonical |

### K-mer Length vs nRF and Entropy (Fig. 3)

| Observation | 7 Primates | Drosophila |
|---|---|---|
| nRF varies with k | Yes, U-shaped or decreasing | Yes |
| Entropy increases with k | Yes, cumulative increase | Yes |
| kentropy selected | Marked with diamond marker | Marked with diamond marker |
| kentropy yields good nRF | Yes | Yes |

- Fig. 3a: For Primates, nRF and entropy plotted against k-mer length; diamond markers indicate kentropy
- Fig. 3b: Same analysis for Drosophila dataset
- Short k-mers (k=9): most k-mers present in all taxa, low entropy, low discriminating power
- Long k-mers (k=31): many k-mers unique to single taxa, high entropy but potentially noisy
- kentropy provides a balanced trade-off between signal and noise

---

## Yersinia Dataset: Canonical vs Non-Canonical Counting (Fig. 7)

| Counting Mode | nRF to Reference | Notes |
|---|---|---|
| Non-canonical | 0.00 (identical to reference) | Captures inversions |
| Canonical | Non-zero (differences marked in red) | Misses inversion events |

- Fig. 7a: Non-canonical tree matches reference perfectly
- Fig. 7b: Canonical tree has branches differing from reference (shown in red)
- Non-canonical mode treats a k-mer and its reverse complement as different, enabling detection of inversion events

---

## Runtime and Memory Usage (Table 1)

| Dataset | Runtime | Peak Memory |
|---|---|---|
| 7 Primates | Reported | Reported |
| Drosophila | Reported | Reported |
| E.coli/Shigella (29) | Reported | Reported |
| Labroidei (25) | Reported | Reported |
| Plants (14) | Reported | Reported |
| E.coli/Shigella (27) | Reported | Reported |
| Yersinia (8) | Reported | Reported |

- Table 1 provides specific runtime and peak memory values for Peafowl on each dataset
- Peafowl runtime includes k-mer generation (Jellyfish), binary matrix construction (hashing), entropy calculation, and RAxML ML estimation

---

## Algorithm Steps

| Step | Description | Tool/Method |
|---|---|---|
| 1. K-mer generation | Generate k-mers for odd k from 9 to 31 | Jellyfish |
| 2. Binary matrix construction | Presence/absence matrix (0/1) for all k-mers x species | Hashing |
| 3. K-mer length selection | Choose kentropy based on cumulative entropy | Entropy analysis |
| 4. ML tree estimation | Input binary matrix at kentropy to RAxML | RAxML |

---

## Method Classification Context

| Approach | Category | Requires Alignment | Method Type |
|---|---|---|---|
| UPGMA | Distance-based | Yes (traditional) or No (AF) | Hierarchical clustering |
| Neighbor-joining | Distance-based | Yes (traditional) or No (AF) | Distance matrix |
| Maximum parsimony | Character-based | Yes | Minimizes character changes |
| Maximum likelihood | Character-based | Yes (traditional) | Probabilistic model |
| Peafowl | Character-based | No (alignment-free) | ML on binary k-mer matrix |

- Peafowl is the first to combine alignment-free data preparation with ML tree estimation
- In the alignment-based setting, ML methods are known to outperform distance-based methods
- This suggests room for future improvement of AF-ML methods to surpass AF-distance methods

---

## Limitations Noted

| Limitation | Description |
|---|---|
| Distant species | Performance degrades when few k-mers are conserved |
| Missing regions | Performance suffers with considerable missing sequence data |
| Assembled input only | Current version requires assembled sequences/genomes |
| Binary encoding only | Ignores actual k-mer counts (only presence/absence) |
| Maximum taxa | Limited to 30 species |

---

## Key Observations from Figures

| Figure | Observation |
|---|---|
| Fig. 1 | Pipeline overview: k-mer generation, binary matrix, entropy selection, RAxML |
| Fig. 2 | Short k-mers (AT, length 2) found in all taxa; long k-mers (ATAGCGC, length 7) found in source only |
| Fig. 3 | nRF and entropy vs k-mer length show optimal selection at kentropy |
| Fig. 4 | Peafowl competitive with state-of-the-art on Primates and Drosophila |
| Fig. 5 | Primates: Peafowl tree identical to reference; Drosophila: minor differences |
| Fig. 6 | Variable performance across AFproject datasets; no single method dominates |
| Fig. 7 | Non-canonical counting essential for Yersinia (inversions present) |

---

## Future Directions Identified

| Direction | Rationale |
|---|---|
| Support unassembled reads | Enable phylogeny from raw sequencing data |
| Utilize k-mer counts | Move beyond binary presence/absence |
| Increase taxa limit | Accommodate larger taxonomic groups (>30) |
| Handle missing data | Improve robustness to incomplete sequences |
| Handle distant species | Address low k-mer conservation across divergent taxa |

---

## Software Details

| Component | Detail |
|---|---|
| Tool name | Peafowl |
| Repository | https://github.com/hasin-abrar/Peafowl |
| K-mer counting | Jellyfish |
| ML estimation | RAxML |
| Tree comparison | PHYLIP (RF distances) |
| Distance-to-tree | MEGA-X (neighbor-joining, UPGMA) |
| Primary metric | Normalized Robinson-Foulds (nRF) distance |

