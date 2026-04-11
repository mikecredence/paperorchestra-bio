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
