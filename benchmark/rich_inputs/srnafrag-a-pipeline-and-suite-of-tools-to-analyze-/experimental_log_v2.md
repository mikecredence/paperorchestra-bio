# Experimental Log: sRNAfrag Pipeline

## Pipeline Architecture

| Module | Function | Key Tools |
|--------|----------|-----------|
| P1 | Raw read processing, alignment, lookup table generation | UMI-tools, AdapterRemoval, bowtie, SAMtools, BEDTools |
| S1 | Multi-mapping correction, basic analyses, filtering | R scripts, ggseqlogo |
| P2 | Fragment merging/clustering, summary report | Bipartite graph clustering |

## Annotation Data Sources

| Species | Source | Annotation Type |
|---------|--------|-----------------|
| H. sapiens (snoRNA) | snoDB | snoRNA |
| H. sapiens (snRNA) | RNAcentral | snRNA |
| H. sapiens (rRNA) | ITRA | rRNA |
| M. musculus | NCBI | Parsed annotations |
| C. elegans | NCBI | Parsed annotations |
| A. thaliana | NCBI | Parsed annotations |

## Bowtie Alignment Parameters

| Parameter | Value |
|-----------|-------|
| Mismatches allowed | Up to 3 |
| Max alignments reported | 10000 |
| Multi-mapping handling | Report all, correct downstream |

## Experiment 1: Peak Calling Benchmark (Fig 1A)

### Ground Truth
Mature miRNA start/end loci from miRBase, using pre-miRNAs as source transcripts.

### Peak Calling Accuracy

| Metric | sRNAfrag | FlaiMapper |
|--------|----------|------------|
| Start loci within 1 bp | 94.7% | 92.4% |
| End loci within 1 bp | 86.5% | 85.2% |
| Pre-miRNAs with fragments | 597 | 642 |
| Reason for fewer in sRNAfrag | Multi-mapping count division makes filtering stricter | Default settings |

Note: Offsets are not false positive peaks but reflect genuine count peaks at positions slightly different from miRBase annotations.

### Count Validation (Fig 1B-C)

| Comparison | Metric | Value |
|-----------|--------|-------|
| Peak calling counts vs AASRA | Correlation | High (near 1:1) |
| Merged counts (P2) vs AASRA | Slope | 0.983 |
| Merged counts (P2) vs AASRA | Intercept | Slightly negative |
| Reason for underestimation | AASRA anchoring counts reads beyond annotation boundaries | -- |

Fig 1B: Scatter of raw peak-calling counts vs AASRA counts shows strong agreement (near diagonal).
Fig 1C: Merged counts after P2 module vs AASRA shows slight underestimation (slope 0.983) due to different handling of boundary reads.

## Experiment 2: Multi-Mapping Analysis (Fig 2)

### miRNA Multi-Mapping Validation

| Observation | Detail |
|-------------|--------|
| Most shared fragment in miR-30b/30c | Three clusters shared between family members |
| snoRD115 isoforms | One fragment shared between 12 isoforms, 5' end matches most conserved fragment |
| Key insight | Multi-mapping events recover the functionally important 5' seed sequence of miRNAs |

### Multi-Mapping Fragment Composition (Fig 2C-D)

| Category | Proportion |
|----------|-----------|
| Fragments with >1 possible source (merged) | Reported in pie chart |
| Most highly expressed fragment overlap with most shared | Significant overlap for miRNAs |

Fig 2A-B: Diagrams show the most expressed fragment (black triangle) and most shared fragment (red line) often overlap at the 5' end.
Fig 2C-D: Pie charts showing proportion of merged fragments with multiple potential sources.

## Experiment 3: Cross-Species snoRNA Conservation (Fig 3)

### Shared Fragment Counts Between Species

| Species Pair | Shared snoRNA Fragments |
|-------------|------------------------|
| H. sapiens - M. musculus | Highest (hundreds) |
| H. sapiens - C. elegans | Moderate |
| H. sapiens - A. thaliana | Lowest |
| M. musculus - C. elegans | Moderate |
| M. musculus - A. thaliana | Low |
| C. elegans - A. thaliana | Low |
| Total conservation events (2/4 species) | 1,411 |

Fig 3A: Heatmap of shared fragment counts between four species. Diagonals set to 0. Mammalian pair shares most fragments.

### Example Conserved Fragment (Fig 3B-D)

| Property | Value |
|----------|-------|
| Source | Unassigned transcript 14429 |
| Hamming distance (H. sapiens vs M. musculus) | 2 |
| Conservation | Fragment loci preserved across species with structural context |

Fig 3B: Shared fragment between species with Hamming distance of 2 relative to human and mouse.
Fig 3C-D: Species-specific fragment context showing conservation of fragmentation pattern.

## Experiment 4: Runtime Analysis (Fig 4A)

| Dataset Size | Approximate Runtime (minutes) |
|-------------|------------------------------|
| Small | ~5-10 |
| Medium | ~15-30 |
| Large | ~60+ |

Fig 4A: Overall runtime scales with dataset size. GNU Parallel enables parallelization.

## Out-of-Space Map Composition (Fig 4B-D)

| sRNA Type | Human Outside-Map Composition |
|-----------|-------------------------------|
| rRNA | Mixed biotype categories |
| snRNA | Mixed biotype categories |
| snoRNA | Mixed biotype categories |

Fig 4B-D: Composition of out-of-space maps for rRNA, snRNA, and snoRNA fragments in humans shows where fragments map outside their expected annotation space.

## Lookup Table Structure (Table 2)

| Field | Description |
|-------|-------------|
| License plate ID | Sequence-based unique identifier |
| Source transcript | Annotation source |
| Start position (normalized 0-1) | Averaged if multiple positions |
| 5' flanking sequence | Context information |
| 3' flanking sequence | Context information |
| Sources column | All possible sources, delimited |

## Annotation Statistics (Table 1)

| Species/Annotation | Max Possible Fragments | % Found in Test Data |
|-------------------|----------------------|---------------------|
| H. sapiens | Large | Subset detected |
| M. musculus | Large | Subset detected |
| C. elegans | Moderate | Subset detected |
| A. thaliana | Moderate | Subset detected |

## Clustering Algorithm (Fig 7)

| Parameter | Value |
|-----------|-------|
| Minimum cluster length | 10 nt |
| Clustering logic | Bipartite star graphs, sequential ID assignment |
| Smoothing | Prevents peaks near dominant peaks |
| Sandwich zeros | Assigned counts of adjacent loci |

## Normalization Methods Implemented

| Method | Description |
|--------|-------------|
| Ratio normalization | Normalize to miRNA counts |
| TPM | Transcripts per million |
| CPM | Counts per million reads |

## Key Limitations Noted

| Limitation | Description |
|-----------|-------------|
| Between-run comparison | Technical variation across sequencing runs not fully addressed |
| Annotation generation | Deliberately does not auto-generate annotations due to 65% false positive rate concern |
| Size selection bias | Library prep size selection affects fragment detection |
| Normalization between runs | Combining on license plates possible but risky due to technical variation |

## Software and Dependencies

| Tool | Purpose |
|------|---------|
| UMI-tools | UMI handling |
| AdapterRemoval | Adapter trimming |
| FastQC | Quality control (2 Mb subset) |
| bowtie | Alignment |
| SAMtools | BAM processing |
| BEDTools | Annotation sequence extraction |
| GNU Parallel | Parallelization |
| R | Statistical analysis, count correction |
| ggseqlogo | Sequence logo generation |
| MINTmap license plates | Sequence-based IDs |
