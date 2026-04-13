Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

# Idea Summary

## Working title
Profiling of Chimeric RNAs in Human Retinal Development with Retinal Organoids

## Core question
What is the landscape of chimeric RNAs during human retinal development, and does the chimeric RNA CTNNBIP1-CLSTN1 (CTCL) -- previously implicated in cerebral development -- also play a key role in retinogenesis?

## Motivation / gap
- Chimeric RNAs regulate stem/progenitor cell differentiation and CNS development, but their role in retinal development is completely unknown
- Retina is part of the CNS, yet no study has profiled chimeric RNAs across retinal developmental stages
- CTCL downregulation causes premature neuronal differentiation in cerebral organoids, but whether it functions in retinogenesis is untested
- Obtaining normal human retinal tissue is difficult; retinal organoids (ROs) from hESCs provide a model system spanning D0-D120
- The chimeric RNA transcriptome of the developing retina has not been catalogued

## Core contribution (bullet form)
- Presented the first expression atlas of chimeric RNAs throughout human retinal organoid development from D0 to D120 across 22 RO samples at 8 stages
- Found that intra-chromosomal chimeric RNAs increase with RO development (r2 = 0.93, p = 0.00076, Pearson correlation), while inter-chromosomal chimeric RNAs do not show this trend
- Identified that 61.9% of chimeric RNAs were formed between two protein-coding genes, with "In frame" chimeric RNAs accounting for 11.2% of events
- Confirmed four isoforms of CTCL in retinal organoids via PCR and Sanger sequencing
- Demonstrated that CTCL knockdown obstructed RO differentiation but promoted RPE differentiation, with thinner outer layers visible at D60
- Transcriptomic analysis of CTCL-knockdown organoids revealed alterations in EMT, extracellular matrix organization, and epithelial cell differentiation pathways rather than the expected Wnt signaling changes

## Method in brief
Human embryonic stem cell-derived retinal organoids (ROs) were cultured following established protocols from D0 to D120. Total RNA from 22 organoid samples spanning 8 developmental stages was sequenced using VAHTS Universal V6 RNA-seq Library Prep Kit for Illumina. Chimeric RNAs were identified using FusionCatcher software, with a stringency filter requiring at least one spanning unique read. Expression levels were quantified as log(spanning unique reads / total reads * 10,000,000). Parental gene expression was analyzed by mapping to hg38 with Hisat2 and assembling transcripts with featureCounts.

Loss-of-function experiments used a CRX-tdTomato hES reporter line. Lentiviral shRNA targeting CTCL was transduced into ROs at D12, with scramble shRNA as control. Knockdown efficiency was confirmed 48-72 hours post-infection. Organoids were collected at D60 for immunohistochemistry (markers: CRX, OTX2, VSX2, RCVRN, MITF, RPE65, PAX6), RNA sequencing, differential expression analysis, and GSEA using the R package clusterProfiler. Sequence motifs around fusion sites were analyzed with the seqLogo R package.

## Target venue
eLife


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the chimeric RNA profiling in retinal organoids study.

---

## Datasets and Samples

| Parameter | Value |
|-----------|-------|
| Cell line | hESC-derived (CRX-tdTomato reporter) |
| Total RO samples sequenced | 22 |
| Developmental stages | 8 (D0, D30, D45, D60, D75, D90, D105, D120) |
| Chimeric RNA detection tool | FusionCatcher |
| Positive criteria | Spanning unique reads >= 1 |
| Expression metric | log(spanning_unique_reads / total_reads * 10^7) |
| Genome reference | hg38 |
| Alignment tool | Hisat2 |
| Transcript assembly | featureCounts |

---

## Experiment 1: Chimeric RNA Landscape During RO Development

| Chimeric RNA Category | Trend Over Development | Statistical Test |
|----------------------|----------------------|-----------------|
| Intra-chromosomal | Increase with development | r2 = 0.93, p = 0.00076 (Pearson) |
| Inter-chromosomal | No significant trend | Not significant |
| Total chimeric events | Continuously expressed | Present at all stages |

Fig. 2A: Circos plots showing genomic distribution of chimeric RNA parental genes at each stage.
Fig. 2B: Types of chimeric RNAs based on genomic distribution of parental genes.
Fig. 2C: Correlation analysis showing intra-chromosomal increase.

---

## Experiment 2: Chimeric RNA Characterization

| Predicted Effect Category | Percentage |
|--------------------------|------------|
| In frame | 11.2% |
| CDS(truncated)_UTR | 10.7% |
| UTR_UTR | 10.7% |
| Other categories (11 more) | Remaining |

| Parental Gene Biotype Combination | Percentage |
|----------------------------------|------------|
| Protein-coding + Protein-coding | 61.9% |
| Other combinations | 38.1% |

Fig. 3A: Top 14 types and numbers of chimeric RNAs by predicted effect.
Fig. 3B: Biotype quantification of parental gene combinations across all samples.
Fig. 3C: Motifs consisting of 20 bp DNA sequences around fusion sites analyzed by seqLogo.
Fig. 3D: Spearman correlation of chimeric RNA expression vs parental gene expression was not significant (p > 0.05).
Fig. 3 - Supplement 1: Detailed breakdown of chimeric RNA types by predicted effect.

---

## Experiment 3: CTCL Isoform Identification

| Isoform | Type | Presence in ROs |
|---------|------|----------------|
| In-frame | CTNNBIP1 exons 1-5 fused to CLSTN1 exons (last 17) | Confirmed by PCR and Sanger |
| UTR_CDS(truncated)-1 | Truncated coding region | Confirmed |
| CDS(truncated)Intronic | Intronic fusion | Confirmed |
| UTR_CDS(truncated)-2 | Another truncated variant | Confirmed |

Fig. 4A: Heatmap of CTCL spanning unique reads for each isoform across developmental stages.
Fig. 4B: Schematic of the four isoform structures (blue = upstream CTNNBIP1, red = downstream CLSTN1).
Fig. 4C: PCR validation of four isoforms in D60 ROs.
Fig. 4D: Sanger sequencing confirming fusion junctions.

---

## Experiment 4: CTCL Knockdown Experiment Design

| Parameter | Value |
|-----------|-------|
| Reporter line | CRX-tdTomato |
| shRNA delivery | Lentiviral transduction at D12 |
| Controls | Scramble shRNA |
| Independent experiments | 3 |
| Collection timepoint | D60 (except KD efficiency at 48-72h) |
| Knockdown efficiency assessment | 48-72 hours post-infection |

Fig. 5A: Schema of shRNA experimental timeline.
Fig. 5B: Knockdown efficiency confirmation.

---

## Experiment 5: CTCL Knockdown Phenotype

| Observation | shCTCL | Scramble Control |
|-------------|--------|-----------------|
| RO outer layer thickness | Thinner | Normal |
| CRX-tdTomato signal | Altered | Normal |
| RPE differentiation | Promoted | Baseline |
| RO neural differentiation | Obstructed | Normal progression |

| Parental Gene Expression After KD | Effect | Statistical Test |
|-----------------------------------|--------|-----------------|
| CTNNBIP1 mRNA | No change | t-test, p > 0.05 (n=4) |
| CLSTN1 mRNA | No change | t-test, p > 0.05 (n=4) |

Fig. 5 - Supplement 1: Live imaging at D60 showing thinner outer layer in shCTCL organoids.
Fig. 5 - Supplement 2A: RT-qPCR showing no effect on CTNNBIP1 expression.
Fig. 5 - Supplement 2B: RT-qPCR showing no effect on CLSTN1 expression.

---

## Experiment 6: Immunohistochemistry of CTCL-KD Organoids

| Marker | Category | shCTCL vs Control |
|--------|----------|-------------------|
| CRX | Photoreceptor precursor | Reduced |
| OTX2 | Neural/retinal marker | Altered |
| VSX2 | Retinal progenitor | Changed |
| RCVRN | Photoreceptor | Reduced |
| MITF | RPE-specific | Increased |
| RPE65 | RPE-specific | Increased |
| PAX6 | Eye field/progenitor | Altered pattern |

Fig. 5 - Supplement 3A-B: MITF immunostaining elevated in CTCL-KD organoids.
Fig. 5 - Supplement 3C-D: RPE65 immunostaining elevated in CTCL-KD organoids.
Fig. 5 - Supplement 3E-F: PAX6 staining altered in CTCL-KD organoids.

---

## Experiment 7: Transcriptomic Analysis of CTCL Knockdown

| Analysis | Tool/Method | Key Findings |
|----------|------------|--------------|
| DEG identification | |Log2(shCTCL/scramble)| > 1, p < 0.05 | Hundreds of DEGs identified |
| Functional enrichment (upregulated) | Metascape | EMT, extracellular matrix, epithelial differentiation |
| Functional enrichment (downregulated) | Metascape | Neurogenesis, morphogenesis |
| GSEA | clusterProfiler (c8 reference gene set) | Enriched for RPE-related gene sets |

| Expected vs Observed Pathway Changes | Expected? | Observed? |
|--------------------------------------|-----------|-----------|
| Wnt signaling modulation | Yes (based on CTNNBIP1 function) | No significant change |
| Vesicular transport | Yes (based on CLSTN1 function) | No significant change |
| EMT pathway | Not expected | Significantly changed |
| Extracellular matrix organization | Not expected | Significantly changed |
| Epithelial cell differentiation | Not expected | Significantly changed |

Fig. 6A: Volcano plot of DEGs between shCTCL and scramble at D60.
Fig. 6B: Heatmap of DEGs.
Fig. 6C: Functional enrichment of up- and down-regulated DEGs.
Fig. 6D: GSEA results showing enriched gene sets in shCTCL organoids.
Fig. 6E: RPE-related gene expression elevated in shCTCL-treated organoids.

---

## Experiment 8: RPE Gene Expression

| RPE Marker Gene | Direction in shCTCL | Significance |
|----------------|--------------------|----|
| MITF | Upregulated | Significant |
| RPE65 | Upregulated | Significant |
| BEST1 | Upregulated | Significant |
| TYR | Upregulated | Significant |

Fig. 6E: Expression of RPE-related genes confirmed by RNA-seq.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total chimeric RNA events detected | Hundreds across all stages |
| Intra-chromosomal correlation with development | r2 = 0.93, p = 0.00076 |
| Protein-coding parental gene pairs | 61.9% |
| CTCL isoforms identified | 4 |
| Parental gene expression change after KD | None (p > 0.05 for both) |
| Key unexpected pathway finding | EMT and ECM rather than Wnt |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | RO generation scheme from D0-D120 and FusionCatcher screening pipeline |
| Fig. 2 | Chimeric RNAs continuously expressed; intra-chromosomal increase over development |
| Fig. 3 | In-frame chimeric RNAs are 11.2%; protein-coding pairs dominate at 61.9% |
| Fig. 4 | Four CTCL isoforms validated by PCR and Sanger sequencing |
| Fig. 5 | CTCL knockdown obstructs RO differentiation but promotes RPE fate |
| Fig. 6 | Transcriptome changes in EMT/ECM/epithelial pathways rather than Wnt or vesicular transport |

---

## Reference Count
34 references cited.

