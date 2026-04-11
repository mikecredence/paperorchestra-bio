# Experimental Log: Benchmarking CNA Inference Tools from scRNA-seq

## Benchmark Datasets

### Table 1: Dataset Overview

| Dataset | Tumor Type | Source Study | N Cells (approx.) | Ground Truth | scRNA-seq Platform |
|---------|-----------|-------------|-------------------|-------------|-------------------|
| CRC01-CRC08 | Colorectal cancer | Zhou et al. | Multiple samples | Paired scDNA-seq | Multi-omics |
| ALL (2 samples) | Acute lymphoblastic leukemia | Zachariadis et al. | Variable | Paired scDNA-seq | GSE144296 |
| Glioma | Glioma | Yu et al. | Variable | Paired scDNA-seq | GSE185269 |
| Neuro | Neuroendocrine tumor | Cui et al. | Variable | Paired scDNA-seq | PRJCA002946 |
| NPC43 | NPC43 cell line | Yu et al. | Variable | Paired scDNA-seq | GSE185269 |
| HUVEC | Endothelial cell line (control) | Yu et al. | Variable | Paired scDNA-seq | GSE185269 |
| GX109 | Additional sample | Huang et al. | Variable | Paired scDNA-seq | Raw FASTQ |

### Table 2: Data Accessions

| Dataset | Repository | Accession |
|---------|-----------|-----------|
| CRC | NGDC Genome Sequence Archive | HRA000201 |
| Glioma, NPC43, HUVEC | NCBI GEO | GSE185269 |
| Neuro | NGDC | PRJCA002946 |
| ALL | NCBI GEO | GSE144296 |

---

## Tools Benchmarked

### Table 3: Tool Characteristics

| Tool | Version | Input Category | Expression Matrix | B-Allele Frequency | Programming Language | Key Algorithm |
|------|---------|---------------|-------------------|--------------------|--------------------|---------------|
| inferCNV | 1.18.1 | Expression-only | Yes | No | R | Corrected moving average |
| CopyKAT | Default | Expression-only | Yes | No | R | Integrative Bayesian segmentation + GMM |
| SCEVAN | Default | Expression-only | Yes | No | R | Multi-channel segmentation |
| Numbat | Default | Expression + allele | Yes | Yes | R | Haplotype-aware HMM |
| CaSpER | Default | Expression + allele | Yes | Yes | R | Multiscale signal-processing |

### Table 4: Tool Input Requirements Comparison

| Feature | inferCNV | CopyKAT | SCEVAN | Numbat | CaSpER |
|---------|----------|---------|--------|--------|--------|
| Expression matrix | Required | Required | Required | Required | Required |
| B-allele frequency | No | No | No | Required | Required |
| Population haplotype | No | No | No | Required | No |
| Reference cells (optional) | Yes | Yes | Yes | N/A | N/A |
| Automatic reference detection | One-pass/Two-pass | Yes (GMM) | Yes | N/A | N/A |

---

## Evaluation Task 1: Tumor vs. Normal Cell Classification

### Table 5: F1 Scores for Tumor/Normal Classification

| Sample | inferCNV | CopyKAT | SCEVAN | Numbat | CaSpER |
|--------|----------|---------|--------|--------|--------|
| Glioma | Evaluated | Evaluated | Evaluated | Best or near-best | Evaluated |
| CRC02 | Evaluated | Evaluated | Evaluated | Best or near-best | Evaluated |
| CRC15 | Evaluated | Evaluated | Evaluated | Best or near-best | Evaluated |
| Overall (boxplot) | Variable | Competitive (expression-only best) | Variable | Highest median | Variable |

Fig 2B shows F1 scores for tumor/normal classification across glioma, CRC02, and CRC15.

Fig 2C shows boxplots of overall F1 scores across all glioma, CRC, and neuroendocrine datasets. Numbat demonstrates the highest overall performance.

### Table 6: Impact of Reference Settings on Classification

| Setting | inferCNV Behavior | Effect |
|---------|-------------------|--------|
| Unspecified reference (one-pass) | Uses input population average as background | May remove real CNA signals when tumor purity is high |
| Specified reference (two-pass) | Uses normal cells from first run as reference | Improved CNA centering |
| With TME cells | Additional cell types in input | Generally improves performance |
| Without TME cells | Only epithelial/tumor cells | Performance may decrease |

Fig 2D shows heatmaps of CNA profiles from CRC02 under different reference conditions, demonstrating incorrect centering with one-pass inferCNV.

Fig 2E shows that including TME cells improves performance for both inferCNV and SCEVAN.

---

## Evaluation Task 2: CNA Profile Accuracy

### Table 7: Pearson Correlation -- Inferred vs. Ground Truth CNA Profiles

| Method | Metric | Overall Performance Ranking |
|--------|--------|---------------------------|
| Numbat | Pearson correlation | Highest |
| CopyKAT | Pearson correlation | Best among expression-only |
| inferCNV (two-pass) | Pearson correlation | Improved over one-pass |
| SCEVAN | Pearson correlation | Moderate |
| CaSpER | Pearson correlation | Variable |

Fig 3B shows Pearson correlations between inferred CNA profiles from scRNA-seq and ground truth from scDNA-seq across tools.

### Table 8: Impact of Reference Settings on CNA Accuracy (inferCNV)

| Approach | Description | Effect on Accuracy |
|----------|-------------|-------------------|
| One-pass | Single run, average as reference | Baseline |
| Two-pass | Second run using normal cells from first run | Improved accuracy |

Fig 3A diagrams the one-pass vs. two-pass inferCNV workflow.

---

## Evaluation Task 3: Tumor Subclone Inference

### Table 9: Subclone Detection Results

| Sample | Subclones in Ground Truth (scDNA) | Tool Performance Summary |
|--------|----------------------------------|--------------------------|
| Glioma | 2 subclones (C1, C2) | Numbat best at recovering clonal structure |
| CRC03 | Multiple subclones | Variable across tools |
| CRC11 | Multiple subclones | Variable across tools |

Fig 4A shows Sankey diagrams comparing clonal structures inferred from scDNA and scRNA in gliomas.

Fig 4B shows percentage of correct C1 subclone classification as tumor cells.

Fig 4C shows heatmaps comparing CNA profiles of two glioma subclones between scDNA-seq and Numbat inference.

Fig 4D and 4G show heatmaps for CRC03 and CRC11 subclones from scDNA-seq and scRNA-seq tools.

### Table 10: Clonal Breakpoint Detection

| Tool | Clonal Breakpoint Detection | Ranking |
|------|---------------------------|---------|
| SCEVAN | Best performance | 1st |
| Numbat | Good | 2nd |
| CopyKAT | Moderate | 3rd |
| inferCNV | Moderate | Variable |
| CaSpER | Lower | 5th |

---

## Evaluation Task 4: Aneuploidy in Non-Malignant Cells

### Table 11: Non-Malignant Cell Aneuploidy Detection

| Cell Type Tested | Context | Tools Evaluated |
|-----------------|---------|-----------------|
| Immune cells | CRC TME | All 5 tools |
| Endothelial cells | CRC TME | All 5 tools |
| Fibroblasts | CRC TME | All 5 tools |

Accumulating evidence suggests CNAs exist in non-malignant cells and are associated with non-cancer diseases. Tools were evaluated for their ability to detect these events.

---

## LOH Detection (Numbat and CaSpER Only)

### Table 12: Copy Number Neutral LOH (cnLOH) Detection

| Tool | Sensitivity | Precision | False Positive Source |
|------|------------|-----------|---------------------|
| Numbat | High | Low | Most FP calls were actually copy number deletions |
| CaSpER | Lower | Variable | Different error patterns |

### Table 13: Genotype Confusion in LOH Calls

| Genotype | Description | Numbat Classification Issue |
|----------|-------------|---------------------------|
| (2,0) | cnLOH -- 2 copies of A allele, 0 of B | Correctly identified as LOH |
| (1,0) | Deletion-mediated LOH -- 1 copy of A, 0 of B | Often misclassified as cnLOH |
| Extreme amplification (e.g., chr8) | High copy number gain | Sometimes misclassified as LOH |

Fig 3K shows that most false positive cnLOH calls from Numbat correspond to copy number deletions.

Fig 3L-M shows an example on chr8 where extreme copy number amplification was misclassified as LOH by Numbat.

---

## Impact of Tumor Purity

### Table 14: Tumor Purity Effects on Expression-Based Methods

| Purity Level | inferCNV Behavior | SCEVAN Behavior |
|-------------|-------------------|-----------------|
| High purity | CNA signals incorrectly removed as background (incorrect centering) | Better performance |
| Low purity | Better with appropriate reference | Tends to misassign non-malignant cells as malignant |
| High purity + TME cells | Improved | Improved |
| Low purity + TME cells | Improved | Improved |

Fig S3A,C show supplementary analyses of TME cell inclusion effects.

### Table 15: Sequencing Depth Impact

| Tool | Robustness to Lower Depth |
|------|--------------------------|
| CopyKAT | Most robust |
| Numbat | Moderate |
| inferCNV | Moderate |
| SCEVAN | Variable |
| CaSpER | Variable |

---

## Overall Tool Recommendations

### Table 16: Summary Recommendations by Task

| Task | Recommended Tool | Condition |
|------|-----------------|-----------|
| Overall best performance | Numbat | When allele data is available |
| Expression-only input | CopyKAT | When only expression matrix available |
| Clonal breakpoint detection | SCEVAN | Best breakpoint accuracy |
| cnLOH detection | Numbat | High sensitivity (mind low precision) |
| Low sequencing depth | CopyKAT | Most robust to depth variation |
| High tumor purity (expression-only) | Include TME cells | Improves centering for inferCNV |
| Low tumor purity (expression-only) | Include TME cells | Reduces SCEVAN false positives |

### Table 17: Computational Speed Ranking

| Tool | Relative Speed |
|------|---------------|
| SCEVAN | Fastest |
| CopyKAT | Moderate |
| inferCNV | Moderate |
| Numbat | Slower (additional allele processing) |
| CaSpER | Slower (additional allele processing) |

Fig 5 provides a comprehensive comparison overview table summarizing methodology, language, version, inputs, parameters, outputs, speed, and recommendations for all five tools.

---

## Figure Observations

- **Fig 1**: Overview of benchmarking workflow. Two tool categories: expression-only (inferCNV, CopyKAT, SCEVAN) and expression + allele (Numbat, CaSpER). Evaluation across four criteria using multi-omics ground truth.

- **Fig 2**: Tumor/normal classification benchmark. Numbat highest F1 overall. InferCNV shows incorrect centering with high tumor purity. TME cell inclusion helps both inferCNV and SCEVAN.

- **Fig 3**: CNA profile accuracy. Numbat leads in Pearson correlation. Two-pass inferCNV better than one-pass. Numbat cnLOH detection has high sensitivity but low precision. False positives traced to deletion/amplification confusion.

- **Fig 4**: Subclone inference. Sankey diagrams show varying agreement between scDNA and scRNA clonal structures. SCEVAN best at breakpoint detection. Numbat best at overall subclone recovery.

- **Fig 5**: Comprehensive tool comparison summary table covering all practical aspects.

---

## Metrics Used

| Metric | Application |
|--------|-------------|
| F1 score | Tumor vs. normal cell classification |
| Pearson correlation | CNA profile accuracy (inferred vs. ground truth) |
| Sensitivity | cnLOH detection |
| Precision | cnLOH detection |
| Correct classification rate | Subclone assignment accuracy |
| Breakpoint detection accuracy | Clonal breakpoint identification |
