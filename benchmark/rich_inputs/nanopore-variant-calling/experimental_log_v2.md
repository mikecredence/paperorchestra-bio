# Experimental Log: Bacterial Nanopore Variant Calling Benchmark

> Pre-writing data log and raw results notebook

---

## 1. Study Design Overview

**Organisms:** 14 bacterial species (Gram-positive and Gram-negative)
**GC content range:** 30-66%
**Sequencing platforms:** ONT R10.4.1 (MinION Mk1b / GridION) and Illumina (NextSeq 500 / NextSeq 2000)
**Read length:** ONT variable long reads (filtered >1000bp, Q>10); Illumina 150bp PE
**Same DNA extraction used for both platforms** to eliminate extraction bias.

### ONT Basecalling Configurations

| Basecaller | Version | Model | Accuracy Mode | Duplex Compatible |
|---|---|---|---|---|
| Dorado | v0.5.0 | dna_r10.4.1_e8.2_400bps_fast@v4.3.0 | fast | No |
| Dorado | v0.5.0 | dna_r10.4.1_e8.2_400bps_hac@v4.3.0 | hac | Yes |
| Dorado | v0.5.0 | dna_r10.4.1_e8.2_400bps_sup@v4.3.0 | sup | Yes |

All basecalling performed on Nvidia A100 GPU for consistency. Reads subsampled to max 100x mean depth with Rasusa v0.8.0.

### Variant Callers Benchmarked

| Variant Caller | Version | Type | Provides Indel Calls | Platform |
|---|---|---|---|---|
| BCFtools | v1.19 | Traditional (pileup) | Yes | ONT |
| Clair3 | v1.0.5 | Deep learning | Yes | ONT |
| DeepVariant | v1.6.0 | Deep learning | Yes | ONT |
| FreeBayes | - | Traditional (haplotype) | Yes | ONT |
| Longshot | - | Statistical | No | ONT |
| Medaka | - | Deep learning (neural network) | Yes | ONT |
| NanoCaller | - | Deep learning | Yes | ONT |
| Snippy | - | Traditional (pipeline) | Yes | Illumina |

Note: Longshot does not produce indel calls. Medaka performs its own alignment internally.

---

## 2. Sample and Truthset Summary

14 samples were selected spanning diverse bacterial species. Donor genomes were chosen with ANI closest to 99.5%. Variants were identified between each sample and its donor via minimap2 and MUMmer intersection, removing overlapping calls and indels >50bp.

### Sample Characteristics

| Sample ID | Species | GC Content (%) | ANI to Donor (%) | Total SNPs | Total Indels |
|---|---|---|---|---|---|
| Sample 1 | Species A (low GC) | ~30 | ~99.5 | ~2,102 (min) | Consistent |
| Sample 2 | Species B | ~35 | ~99.5 | Variable | Consistent |
| Sample 3 | Species C | ~38 | ~99.5 | Variable | Consistent |
| Sample 4 | Species D | ~40 | ~99.5 | Variable | Consistent |
| Sample 5 | Species E | ~42 | ~99.5 | Variable | Consistent |
| Sample 6 | Species F | ~45 | ~99.5 | Variable | Consistent |
| Sample 7 | Species G | ~48 | ~99.5 | Variable | Consistent |
| Sample 8 | Species H | ~50 | ~99.5 | Variable | Consistent |
| Sample 9 | Species I | ~52 | ~99.5 | Variable | Consistent |
| Sample 10 | Species J | ~55 | ~99.5 | Variable | Consistent |
| Sample 11 | Species K | ~58 | ~99.5 | Variable | Consistent |
| Sample 12 | Species L | ~60 | ~99.5 | Variable | Consistent |
| Sample 13 | Species M | ~63 | ~99.5 | Variable | Consistent |
| Sample 14 | Species N (high GC) | ~66 | ~99.5 | ~57,887 (max) | Consistent |

**Key observations:**
- SNP counts ranged widely from 2,102 to 57,887 across the 14 samples
- Indel counts were relatively consistent across all species despite the SNP variation
- GC content spans from 30% to 66%, covering a broad range of bacterial genomic composition
- Known species included: M. tuberculosis, S. pyogenes, S. dysgalactiae subsp. equisimilis, E. coli (ATCC_25922), K. pneumoniae (KPC2_202310), among others

---

## 3. Read Quality Results (Figure 1)

Median alignment-based read identity was computed by aligning each readset to its respective ground truth assembly.

### Median Read Identity by Basecalling Model and Read Type

| Read Type | Basecalling Model | Median Read Identity (%) | Qscore |
|---|---|---|---|
| Duplex | sup | 99.93 | Q32 |
| Duplex | hac | 99.79 | Q27 |
| Simplex | sup | 99.26 | Q21 |
| Simplex | hac | 98.31 | Q18 |
| Simplex | fast | 94.09 | Q12 |

**Qscore formula:** Q = -10 * log10(1 - identity), where identity is the fraction of correctly aligned bases.

**Fig 1 observation:** Each sample appears as a point; the spread within each model/type combination is relatively tight, indicating consistent quality across species. Duplex sup achieves the highest per-read accuracy at Q32.

---

## 4. Variant Calling Accuracy at Full Depth (Figures 2, 3)

Evaluation performed using vcfdist v2.3.3. Each variant classified as TP, FP, or FN. Precision, recall, and F1 computed at each quality score threshold; the best F1 across all thresholds is reported.

### Best Median F1 Scores -- SNPs (100x depth, sup model)

| Variant Caller | Simplex SNP F1 (%) | Duplex SNP F1 (%) |
|---|---|---|
| Clair3 | 99.99 | 99.99 |
| DeepVariant | 99.99 | 99.99 |
| Medaka | Lower than Clair3/DV | Lower than Clair3/DV |
| NanoCaller | Lower than Clair3/DV | Lower than Clair3/DV |
| BCFtools | Substantially lower | Substantially lower |
| FreeBayes | Substantially lower | Substantially lower |
| Longshot | Lower than Clair3/DV | Lower than Clair3/DV |
| Illumina (Snippy) | 99.45 | N/A |

### Best Median F1 Scores -- Indels (100x depth, sup model)

| Variant Caller | Simplex Indel F1 (%) | Duplex Indel F1 (%) |
|---|---|---|
| Clair3 | 99.53 | 99.20 |
| DeepVariant | 99.61 | 99.22 |
| Medaka | Lower | Lower |
| NanoCaller | Lower | Lower |
| BCFtools | Substantially lower | Substantially lower |
| FreeBayes | Substantially lower | Substantially lower |
| Longshot | N/A (no indel calls) | N/A |
| Illumina (Snippy) | 95.76 | N/A |

**Key findings:**
- Clair3 and DeepVariant both reach 99.99% SNP F1 on sup data, surpassing Illumina's 99.45%
- For indels, Clair3 (99.53%) and DeepVariant (99.61%) drastically outperform Illumina (95.76%)
- The gap between ONT deep learning callers and Illumina is roughly an order of magnitude in error rate for both variant types
- Simplex indel F1 slightly exceeds duplex indel F1, likely due to higher total read depth in simplex datasets
- Fast-model results are approximately an order of magnitude worse than hac/sup models
- hac model performance is close to sup but slightly below across all callers

### Performance Relative to Illumina by Basecalling Model

| Basecalling Model | Deep Learning SNP vs Illumina | Deep Learning Indel vs Illumina |
|---|---|---|
| sup | Exceeds Illumina | Exceeds Illumina |
| hac | Matches or exceeds Illumina | Matches or exceeds Illumina |
| fast | Below Illumina (parity only in best SNP case) | Below Illumina |

### Precision-Recall Curve Characteristics (Figure 3)

| Variant Caller | Curve Shape (sup) | Quality Filtering Needed |
|---|---|---|
| Clair3 | Right-angle (high P and R simultaneously) | None for sup SNPs; QUAL>=4 for duplex indels |
| DeepVariant | Right-angle | None for sup SNPs; QUAL>=4 for duplex indels |
| BCFtools | Gradual trade-off | Higher thresholds needed |
| FreeBayes | Gradual trade-off | Higher thresholds needed |
| Longshot | Moderate | Moderate thresholds |
| Medaka | Better than traditional, worse than Clair3/DV | Moderate thresholds |
| NanoCaller | Better than traditional, worse than Clair3/DV | Moderate thresholds |

**Fig 3 observation:** The "right-angle" shape of Clair3 and DeepVariant precision-recall curves indicates that even minimal quality filtering achieves high precision without sacrificing recall. For sup data, no quality filtering is optimal for SNPs; a quality threshold of 4 provides the best F1 for duplex indels.

---

## 5. Error Analysis: Missed and False Calls (Figure 4)

### Illumina Error Sources

Illumina's lower F1 is driven primarily by lower recall rather than precision.

| Error Source | Impact on Illumina | Impact on Clair3 (ONT sup) |
|---|---|---|
| Variant-dense regions (~20 var/100bp) | Bimodal FN distribution; second peak at 20 var/100bp | No bimodal distribution; few missed calls at high density |
| Repetitive genomic regions | Major source of FN; alignment gaps visible | Minimal impact due to long reads |
| Short read alignment ambiguity | Significant in high-density and repeat regions | Not applicable (reads span repeats) |

### F1 Score Change When Masking Repetitive Regions (Figure 4c)

| Method | F1 Without Masking (%) | F1 With Repeat Masking (%) | Change |
|---|---|---|---|
| Illumina (Snippy) | 99.3 | 99.7 | +0.4% |
| Clair3 (100x simplex sup) | ~99.99 | ~99.993 | +0.003% |

**Fig 4 observations:**
- Fig 4a: Illumina false negatives show a bimodal variant density distribution, with the second peak centered around 20 variants per 100bp window. TP and FP calls do not show this pattern.
- Fig 4b: Clair3 (simplex sup, 100x) shows a unimodal density distribution for all call categories, with very few FN or FP calls even at high variant density.
- Fig 4c: Masking repetitive regions boosts Illumina F1 from ~99.3% to ~99.7%, while Clair3 gains only 0.003%, confirming that ONT long reads handle repeats far better than 150bp Illumina reads.

### Notable Outlier Cases
- E. coli ATCC_25922: simplex sup SNP outlier in Fig 2 caused by a variant-dense repetitive region
- K. pneumoniae KPC2_202310: duplex sup SNP outlier caused by very low duplex read depth for that sample

---

## 6. Homopolymer Indel Error Analysis (Figure 5)

Historical weakness of ONT: homopolymer runs cause basecalling errors that manifest as false indel calls. Evaluated whether this remains an issue with R10.4.1 chemistry and modern callers.

### False Positive Indel Counts by Homopolymer Association -- Clair3 (100x simplex)

| Basecalling Model | Total FP Indels | Homopolymer-Associated FP | Non-Homopolymer FP | Notes |
|---|---|---|---|---|
| fast | Many (order of magnitude more) | Dominant source | Minor | Frequent miscalculation of homopolymer length |
| hac | Reduced vs fast | Still notable | Reduced | Mainly 1bp miscalculations in homopolymers |
| sup | 8 | 5 | 3 | 3 non-HP errors near similar-sequence insertions |

### Comparison Across Variant Callers (sup model, 100x simplex)

| Variant Caller | FP Indel Profile | Homopolymer Bias Present |
|---|---|---|
| Clair3 | 8 FP indels total; 5 homopolymer-associated | Minimal -- effectively eliminated |
| DeepVariant | 11 FP indels total; 8 homopolymer-associated | Minimal -- similar profile to Clair3 |
| BCFtools | Persistent homopolymer indel errors even on sup | Yes -- traditional caller does not learn to compensate |
| FreeBayes | Handles errors without inherent bias | No systematic homopolymer bias |
| Medaka | Similar to Clair3/DeepVariant profile | Minimal |
| NanoCaller | Similar to Clair3/DeepVariant profile | Minimal |

**Fig 5 observations:**
- Fast model: clear cluster of FP indels along the homopolymer axis, with indel lengths of 1-2bp in homopolymer tracts of 5+ bases
- Hac model: reduced cluster but still visible homopolymer association
- Sup model: only scattered points, no systematic pattern; homopolymer errors effectively absent
- Illumina comparison (lower right): shows its own distinct indel error pattern unrelated to homopolymer length
- Deep learning callers trained on sup data learn to compensate for residual systematic basecalling errors, while traditional callers (BCFtools) propagate them

---

## 7. Read Depth Analysis (Figures 6, 7)

Reads subsampled to 5x, 10x, 25x, 50x, and 100x mean depth. Duplex max at 50x (limited by duplex read yield), simplex max at 100x. Variants called at each depth and compared to truthset.

### SNP F1 Score vs Read Depth (Figure 6)

| Depth | Clair3 Simplex sup F1 (%) | Clair3 Duplex sup F1 (%) | DeepVariant Simplex sup F1 (%) | Illumina Reference F1 (%) |
|---|---|---|---|---|
| 5x | Below Illumina | Near Illumina (BCFtools matches) | Below Illumina | 99.45 |
| 10x | >= Illumina | >= Illumina | >= Illumina | 99.45 |
| 25x | Well above Illumina | Well above Illumina | Well above Illumina | 99.45 |
| 50x | Near full-depth | Near full-depth | Near full-depth | 99.45 |
| 100x | 99.99 | 99.99 | 99.99 | 99.45 |

### Indel F1 Score vs Read Depth (Figure 7)

| Depth | Clair3 Simplex sup F1 (%) | Clair3 Duplex sup F1 (%) | DeepVariant Simplex sup F1 (%) | Illumina Reference F1 (%) |
|---|---|---|---|---|
| 5x | Below Illumina | Variable | Below Illumina | 95.76 |
| 10x | >= Illumina | >= Illumina | >= Illumina | 95.76 |
| 25x | Well above Illumina | Well above Illumina | Well above Illumina | 95.76 |
| 50x | Near full-depth | Near full-depth | Near full-depth | 95.76 |
| 100x | 99.53 | 99.20 | 99.61 | 95.76 |

### Key Depth Thresholds

| Depth Threshold | SNP Performance | Indel Performance | Recommendation |
|---|---|---|---|
| 5x | Below Illumina for most callers; duplex sup BCFtools matches Illumina SNP precision | Below Illumina generally | Insufficient for most applications |
| 5x duplex sup | SNP accuracy comparable to Illumina | Variable | Minimum for SNP-only applications |
| 10x sup simplex | Matches or exceeds Illumina | Matches or exceeds Illumina | Minimum recommended for resource-limited settings |
| 25x | High accuracy, recommended minimum | High accuracy | Recommended for clinical/public health use |
| 50-100x | Near-optimal performance | Near-optimal performance | Gold standard for comprehensive analysis |

**Fig 6 observations:**
- Precision and recall both decrease as depth drops, with notable degradation below 25x
- At 10x with sup simplex, Clair3 and DeepVariant F1 scores are consistent with full-depth Illumina
- At 5x, SNP precision remains above Illumina for duplex reads with all methods except NanoCaller
- Clair3 and DeepVariant simplex sup at 5x also maintain precision above Illumina
- 95% confidence intervals shown as bars; intervals widen at lower depths

**Fig 7 observations:**
- Indel F1 shows similar depth-dependent trends as SNP F1 but with more variability
- 10x sup simplex with Clair3/DeepVariant matches or exceeds full-depth Illumina indel F1
- Indel performance degrades more sharply than SNP performance at very low depths

---

## 8. Computational Resource Usage (Figure 8)

Runtime measured as CPU seconds per megabase of sequencing data. Memory is maximum RAM usage during the run. Reference genome: 4 Mbp at 100x depth used for time estimates.

### Variant Caller Resource Consumption

| Tool | Median Runtime (s/Mbp) | Est. Time for 4Mbp @ 100x | Median Max Memory | Notes |
|---|---|---|---|---|
| DeepVariant | 5.7 | ~38 minutes | 8 GB | Slowest and most memory-intensive |
| FreeBayes | Variable (max 597) | Up to 2.75 days (worst case) | Variable | Largest runtime variation |
| Clair3 | 0.86 | <6 minutes | 1.6 GB | Fast and memory-efficient |
| BCFtools | Low | Fast | Low | Traditional pileup, minimal resources |
| Longshot | Low-moderate | Fast | Low-moderate | Statistical approach |
| Medaka | Moderate | Moderate | Moderate | Neural network-based |
| NanoCaller | Moderate | Moderate | Moderate | Deep learning-based |
| Alignment (minimap2) | Included in Fig 8 | - | - | Baseline alignment step |

### Basecalling Resource Usage (GPU)

| Basecalling Model | Median Runtime (s/Mbp) | Est. Time for 4Mbp @ 100x | Hardware |
|---|---|---|---|
| sup | 0.77 | ~5.1 minutes | Single Nvidia A100 GPU |
| hac | Faster than sup | < 5 minutes | Single Nvidia A100 GPU |
| fast | Fastest | < 5 minutes | Single Nvidia A100 GPU |

**Fig 8 observations:**
- Two panels: upper shows max memory usage, lower shows runtime normalized per megabase
- DeepVariant is the clear outlier in both memory and runtime
- Clair3 offers the best accuracy-to-resource trade-off: near-identical accuracy to DeepVariant at ~7x faster runtime and ~5x lower memory
- FreeBayes has extreme runtime outliers (up to 597 s/Mbp) making it unreliable for production pipelines
- Basecalling on GPU is faster than most variant callers, so it does not represent a bottleneck

---

## 9. Datasets and Tools Summary

### Sequencing Platforms and Library Prep

| Platform | Model | Library Kit | Read Config |
|---|---|---|---|
| ONT | MinION Mk1b / GridION | Rapid Barcoding V14 (SQK-RBK114.96) or Native Barcoding V14 (SQK-NBD114.96) | R10.4.1 flowcell, 5 kHz sampling |
| Illumina | NextSeq 500 / NextSeq 2000 | Illumina DNA Prep (20060059), quarter reagents | 150bp paired-end |

### Bioinformatics Tools Used

| Tool | Version | Purpose |
|---|---|---|
| Dorado | v0.5.0 | ONT basecalling (fast/hac/sup/duplex) |
| SeqKit | v2.6.1 | Read filtering (length >1000bp, Q>10) |
| Rasusa | v0.8.0 | Random subsampling to target depths |
| fastp | v0.23.4 | Illumina adapter trimming, QC, dedup |
| Filtlong | v0.2.1 | ONT read quality filtering (keep best 90%) |
| Trycycler | v0.5.4 | Consensus assembly from 24 sub-assemblies |
| minimap2 | - | Long-read alignment; variant identification |
| MUMmer | - | Genome alignment for variant identification |
| vcfdist | v2.3.3 | Variant call evaluation (TP/FP/FN classification) |

### Evaluation Metrics

| Metric | Formula | Usage |
|---|---|---|
| Precision | TP / (TP + FP) | Fraction of called variants that are correct |
| Recall | TP / (TP + FN) | Fraction of true variants that are detected |
| F1 Score | 2 * (Precision * Recall) / (Precision + Recall) | Harmonic mean; overall accuracy measure |
| Qscore | -10 * log10(1 - identity) | Log-transformed read identity |

---

## 10. Summary of Key Quantitative Findings

### Top-Line Numbers

| Metric | Best ONT Result | Illumina Result | ONT Advantage |
|---|---|---|---|
| Median SNP F1 (sup, 100x) | 99.99% (Clair3/DeepVariant) | 99.45% (Snippy) | ~10x lower error rate |
| Median Indel F1 (sup, 100x) | 99.53-99.61% (Clair3/DeepVariant) | 95.76% (Snippy) | ~10x lower error rate |
| Best read identity | 99.93% / Q32 (duplex sup) | N/A | Highest per-read accuracy |
| Min depth matching Illumina | 10x (sup simplex) | Full depth (~50-200x) | Lower sequencing cost |
| Min depth for SNP parity | 5x (duplex sup) | Full depth | Minimal data needed |
| Clair3 FP indels (sup, 100x) | 8 total across 14 species | - | Homopolymer errors eliminated |
| Clair3 runtime | 0.86 s/Mbp, 1.6 GB RAM | - | Practical for clinical use |
| Sup basecalling runtime | 0.77 s/Mbp (A100 GPU) | - | Not a bottleneck |
| Illumina F1 gain from repeat masking | +0.4% (99.3% to 99.7%) | - | Repeats cause Illumina errors |
| ONT F1 gain from repeat masking | +0.003% | - | Repeats not an issue for ONT |

### Practical Recommendations from Results

| Use Case | Recommended Setup | Minimum Depth | Expected SNP F1 |
|---|---|---|---|
| Clinical / public health | ONT sup simplex + Clair3 | 25x | >99.99% |
| Resource-limited fieldwork | ONT sup simplex + Clair3 | 10x | >= Illumina (99.45%) |
| Rapid SNP screening | ONT duplex sup + any DL caller | 5x | ~Illumina parity |
| Maximum accuracy | ONT sup simplex 100x + Clair3 | 100x | 99.99% |

---

## 11. Statistical and Methodological Notes

- 95% confidence intervals computed and displayed as bars at each depth point in Figures 6-7
- Confidence intervals widen at lower read depths due to fewer qualifying samples
- Grey bars in depth figures indicate the number of samples with sufficient native depth at each level; samples lacking native depth at a given level were excluded from that depth's metrics
- Variant truthset construction used intersection of minimap2 and MUMmer variant calls to maximize reliability
- Indels >50bp excluded from analysis (focus on small variants only)
- Ground truth assemblies generated via Trycycler with 24 separate sub-assemblies per sample, representing near-perfect references achievable with current technology
- Illumina read depths vary by sample (see Supplementary Table S1); ONT data subsampled to controlled depths

---

## 12. Figure-by-Figure Factual Observations

**Figure 1 (Read identity):** Duplex sup reads achieve 99.93% median identity (Q32). Clear separation between all five basecalling configurations. Minimal inter-sample spread within each configuration.

**Figure 2 (Best F1 scores):** Clair3 and DeepVariant dominate across all panels. Sup > hac >> fast for all callers. Illumina sits below the deep learning ONT callers for both SNPs and indels. Individual sample points show tight clustering for top callers.

**Figure 3 (Precision-recall curves):** Clair3 and DeepVariant show characteristic right-angle curves indicating simultaneous high precision and recall. Traditional callers show gradual precision-recall trade-offs. Aggregated across all 14 samples.

**Figure 4 (Illumina error sources):** Bimodal variant density for Illumina FNs (peaks at low density and ~20 var/100bp). No bimodal pattern for Clair3. Repeat masking improves Illumina F1 by 0.4% but Clair3 by only 0.003%.

**Figure 5 (Homopolymer indel errors):** Fast model shows clear homopolymer-correlated FP indel cluster. Hac model shows reduced but visible pattern. Sup model shows only scattered points with no systematic pattern. Illumina shows a distinct non-homopolymer error pattern.

**Figure 6 (SNP depth analysis):** At 10x, Clair3/DeepVariant sup simplex match Illumina full-depth. At 5x, precision still above Illumina for duplex sup. Below 25x, confidence intervals widen.

**Figure 7 (Indel depth analysis):** Similar trend to SNP but with more variability. 10x sup simplex with deep learning callers matches Illumina indel F1. Indel performance more sensitive to depth reduction than SNP performance.

**Figure 8 (Computational resources):** DeepVariant: 5.7 s/Mbp median, 8 GB. Clair3: 0.86 s/Mbp, 1.6 GB. FreeBayes: extreme outlier at 597 s/Mbp max. Basecalling at 0.77 s/Mbp (sup model, A100).
