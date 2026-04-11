# Experimental Log: Benchmarking copy number aberrations inference tools using single-cell multi-omics datasets

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- Specifically, we included eight colorectal cancer (CRC)[22] samples, two acute lymphoblastic leukemia (ALL)[23], one glioma, one neuroendocrine tumor and NPC43 cell line, along with HUVEC cell line samples[24] (Table S1).In this study, we benchmarked five widely used tools for CNAs inference.
- The selection of these tools was based on two primary criteria: (1) they require only single-cell RNA sequencing (scRNA-Seq) data as input, and (2) they are recognized as popular tools within the field.
- (See Supplementary Note 1 for details).
- These tools can be broadly categorized into two major groups: those that solely require an expression matrix (inferCNV, CopyKAT, and SCEVAN), and those that require both expression matrix and B-allele frequency data (Numbat and CaSpER) (Fig1).
- The performance was assessed by three common applications in tumor cells: (1) classification of tumor and normal cells, (2) accuracy of CNAs events, (3) tumor subclone inference.
- Several publications have reported clonal expansion of CNAs in benign tissues[21, 25].
- identified prevalent CNAs in immune cells, endothelial cells, and fibroblasts within the TME of CRC[22].
- Therefore, we also evaluated the performance of aneuploidy detection in normal cells.biorxiv;2024.09.26.615284v2/FIG1F1fig1Figure 1:Overview of the benchmarking workflowWe evaluated five tools designed to infer copy number alterations (CNAs) from single-cell RNA-seq data.
- Cell type annotations for all cells were obtained from corresponding published studies[22, 24, 26].
- Only epithelial cells for CRC, endocrine cells for neuroendocrine tumor and glial cells for glioma were retained for tumor vs normal cell classification (Figure 2A).
- Overall, Numbat performed the best in distinguishing tumor cells from normal cells (Figure 2B, C, Figure S1-S2A and Table S2).
- SCEVAN exhibited poor performance in samples with a low frequency of tumor cells (less than 40%), such as CRC11, CRC12, CRC16, and CRC15 (Figure 2B and Figure S2A).
- InferCNV was reliable except in CRC02, where the majority of cells are tumors (approximately 88%).
- In CRC02, the copy number gains and losses in tumors cells were incorrectly centered to be the copy number baseline by inferCNV, while normal cells were predicted to harbor the opposite CNAs profile and thus incorrectly classified to be tumor cells based on global copy number alteration levels (Figu
- CaSpER also made the same error (Figure S1F).
- To address this issue, we investigated whether including TME cells (such as immune, endothelial, and fibroblast cells) could improve the performance of inferCNV, CopyKAT, and SCEVAN, in cases with imbalanced tumor vs normal ratios (Figure 2E, Figure S3A-C).
- The inclusion of TME cells significantly improved the accuracy of tumor cell prediction for SCEVAN (Figure2E, Figure S3C).
- Although this overall improvement was not observed in inferCNV, certain samples with a higher number of tumor cells, such as CRC02 (88%), CRC22 (91%), and CRC03 (67%), showed dramatic increases in their F1 scores, from 0, 0.5, and 0.55 to 1, 0.9, and 0.99, respectively (Figure 2E, Figure S3A).
- For instance, incorporating TME cells into the CRC02 sample not only improved the ability to distinguish between tumor and normal cells, but also accurately identified copy number alterations, including copy number amplifications on chr8 and chr20, and copy number deletions on chr15 (Figure 2F).
- This preliminary conclusion was further supported by the excellent performance of inferCNV in patient CRC15 where the tumor purity was exceptionally low (6%) (Figure 2G).biorxiv;2024.09.26.615284v2/FIG2F2fig2Figure 2:Benchmark of tumor and normal cells classificationA: A bar plot illustrates the cou
- T represents tumor cells, while N represents normal cells.H: F1 scores are shown for glioma downsampling experiments, with the x-axis indicating the ratio of tumor and normal cells.I: The upper heatmap represents the CNAs profiles of glioma from a downsampling experiment with a T : N ratio of 1 : 20
- The lower heatmap represents the average CNA profile of tumor cells based on scDNA-Seq.J: F1 scores for tumor and normal cell classification under different sequencing depths.K: The heatmap demonstrates that CopyKAT less affected by sequencing depths.
- The upper heatmap represents the tumor cells CNAs profiles from scDNA-seq, the middle heatmap shows CNAs profiles from scRNA-seq, and the bottom heatmap exhibits CNAs profiles from down-sampled low-sequencing depth (1K).L: The ratios of cells passing quality control at different down-sampled sequenc
- NS: p > 0.05, *: p < 0.01, **: p < 0.001, ***: p < 0.0001.
- T: Tumor cells, N: Normal cells.Additional data can be found in Figures S1-S5 and Tables S1-3.To systematically explore the impact of tumor purity on the accuracy of CNA inference, we generated a synthetic dataset spanning a broad range of tumor/normal cell ratios (from 1:100 to 100:1) to examine th
- Numbat consistently outperformed the other tools, even in extreme cases with low tumor/normal cell ratios (Figure 2I).
- Notably, inferCNV exhibited opposite calling between tumor and normal cells when tumor purity was higher, consistent with the results observed in CRC02 (Figure S4).To explore the impact of sequencing depth on the accuracy of CNAs inference, we’ve down-sampled the sequencing depth from several sample
- As sequencing depth decreased, the overall tumor-normal classification F1 scores for all tools dropped, especially in Numbat (Figure 2J and Figures S5A,D-E, Table S3).
- For instance, even at median of 1K UMIs per cell, CopyKAT could still correctly distinguish tumor from normal cells even though the CNA signal-to-noise ratios clearly decreased with the sequencing depth (Figure 2J-K and Figure S5A).
- The paradoxical increase in F1 scores in SCEVAN was mostly attributed to filtering out more nonmalignant cells due to lower sequencing depth, thus rectifying the prediction bias towards assigning most nonmalignant cells into malignant cells (Figure 2L and Figure S5A-D).
- Given the potential problem of incorrect centering in inferCNV (as shown in Figure 2C) when using one-pass mode (single-run without specifying reference cells, Figure 3A), we hypothesized that employing a two-pass mode (first-pass run to identify normal cells and second-pass run using these normal c
- The similarity between CNAs profiles calling form scDNA-Seq and inferred CNAs profiles from scRNA-seq significantly increased in eight of nine cases for inferCNV (Figure 3B-C).
- In contrast, CopyKAT and SCEVAN already incorporated a two pass-like approach in their algorithms where they initially predict normal reference cells and then utilize them as a baseline to correct tumor cell CNAs[17, 18].
- Thus, adopting a two-pass approach has minimal impact on the performance of these two methods (Figure S6A-B).
- Consequently, when assessing the accuracy of inferred CNAs profiles for inferCNV, the results obtained from the two-pass mode were utilized.biorxiv;2024.09.26.615284v2/FIG3F3fig3Figure 3:Benchmark of the accuracy of inferred CNAs profilesA: Diagram illustrating CNAs profiles under unspecified (one-p
- Each dot represents the Pearson correlation between CNA profiles in scDNA-seq and inferred CNA profiles from paired scRNA-seq from the same cell.C: Heatmap showing CNAs profiles of glioma tumor cells obtained from scDNA-seq (upper), unspecified reference (middle), and specified reference using infer
- Green regions are identified LOH regions.M: Sequenza CNA AB allele copy number results from combined scDNA-Seq on chr5 and chr8, respectively suggested that the LOH events were correct on chr5 and incorrect on chr8.“+” in (B) and (D) indicates tumor cell CNAs profiles estimated when both epithelial 
- NS: p > 0.05, *: p < 0.01, **: p < 0.001, ***: p < 0.0001 Additional information is available in Figures S6-S11.Numbat and CaSpER generated integral copy number profiles, which are easier to interpret and appear cleaner, while inferCNV, CopyKAT and SCEVAN output continuous copy number.
- No single tool consistently outperformed others in term of consistency between scRNA-Seq inferred profile and scDNA-Seq profile in all cases (Figure 3D-E).
- All tools performed well in cases with sufficient number of both tumor and normal cells, such as glioma, CRC13, CRC11 and CRC12.
- In samples with an imbalanced number of tumor and normal cells, such as CRC02, CRC22 and CRC15, the overall accuracy of CNAs profiles predicted by the five tools decreased considerably.
- Notably, in CRC03, although Numbat correctly assigned tumor cells, it accurately identified only a small fraction of deletion CNAs in high CNAs burden tumor cells, resulting in low similarity with CNAs profiles obtained from scDNA-Seq (Figure 3D, Figure S1I).
- However, due to the unavailability of raw fastq data, we could only evaluate the performance of inferCNV, CopyKAT and SCEVAN (Figure S7).
- Among them, CopyKAT achieved the best performance, although noticeable false positive signals on CNAs were observed for both CopyKAT and SCEVAN (Figure S7C, S7F).
- All four tools except for Numbat performed poorly when applied to cancer cell line alone (Figure S8).
- The inclusion of normal cells improved the performance of these four tools, but not Numbat (Figure S9).In addition, we assessed the performance of the tools in detecting breakpoints.
- Except for inferCNV, the other four tools were able to output CNV segments at the single-cell level (Figure 3F).
- Numbat and CaSpER detected tens to hundreds of segments, while CopyKAT and SCEVAN identified thousands of segments, which clearly exceeded the expected number of chromosomal breakpoints in cancer [27].
- Therefore, we focused our evaluation on the accuracy of the tumor clonal breakpoints in inferCNV, Numbat and SCEVAN (CopyKAT and CaSpER do not implement the function to call clonal breakpoint, see more details in Supplementary Note 2, Figure 3F).
- CNA calls derived from pseudo bulk scDNA-Seq data were performed using the method adopted in CopyKAT [17] and served as the ground truth.
- Our results showed that, SCEVAN showed overall the best performance in term of F1 scores and sensitivity, while inferCNV was better at precision (Figure 3G and Figure S10A-B).
- Both inferCNV and Numbat detected much fewer breakpoints compared with SCEVAN and the ground truth from DNA-Seq (Figure S10C-D).
- More specifically, the lower F1 score breakpoints for inferCNV and Numbat may be due to reduced resolution in identifying complex CNAs.
- For instance, SCEVAN detected two breakpoints on chr10, while Numbat and inferCNV merged these two adjacent deletions to one single deletion (Figure 3H and Figure S10E).
- It could also be attributed to missed breakpoints detection, such as on chr14 (Figure 3I and Figure S10E).
- Lastly, false positive CNAs calls were also occasionally observed in Numbat (Figure 3J and Figure S10E).Due to the integration of AB allele analysis, both Numbat and CaSpER are able to detect Loss of Heterozygosity (LOH).
- The performance of LOH calling for CaSpER was not further evaluated, as it made too many obviously false positive calls both in malignant and nonmalignant cells (Figure S1).
- Numbat identified a total of 17 LOH events across multiple samples.
- In addition, we obtained the merged pseudobulk tumor and normal samples from scDNA-Seq data and performed CNA calling with Sequenza to obtain the allelic copy number states [28].
- Our analysis revealed that the majority of LOH events detected by Numbat (14 out of 17, ∼82%) were actually CNV amplifications or deletions (Figure 3K and Figure S11A).
- For example, in the CRC13 sample, Numbat identified chr8q as an LOH event; however, analysis of CNAs profiles from DNA data revealed that chr8q had actually undergone CNV amplification (Figure 3L).
- This false positive LOH call by Numbat was due to a significant copy number gain on A allele while the B allele remains unchanged on 8q region, as observed in DNA-Seq analysis (Figure 3M).
- When cross-referenced with DNA data, three regions of chr5q (Figure 3L-M), chr12q (Figure S11A-B), and chr17p (Figure S11C) were identified as cnLOH by Numbat and further validated by AB allele states (B allele copy number is equal to zero for the true positive LOH event) from paired DNA-Seq.
- Noticeably, the LOH event on chr17p resulted in the loss of heterozygosity of the tumor suppressor TP53 gene, thus considered to be crucial event during cancer evolution[29, 30].
- To further confirm the high sensitivity performance of Numbat on cnLOH calling, we also evaluated one gastric tumor sample (GX109) with four cnLOH events annotated from a published study[31].
- All four previously defined cnLOH events were correctly detected by Numbat, and in the meantime no false positive calls were made (Figure S11D).
- In term of specific tasks, SCEVAN performed the best in breakpoint detection, while Numbat achieved high sensitivity in detecting cnLOH.Evaluation of subclonal structure inference accuracyHuman cancer exhibits extensive intra-tumoral heterogeneity, constantly evolving through emerging mutations and 
- Both subclones and the tumor evolutionary history can be inferred from single-cell copy number profiles[33].
- To evaluate the accuracy of subclonal structure inference by these tools, we selected all cases with more than 10 tumor cells (glioma and 7 CRC samples) (Figure 1A, TableS1).In the case of glioma, previous study has already defined the subclonal structures and only Numbat correctly assigned the smal
- We found that the subclone structure inferred by Numbat was largely consistent with scDNA-Seq-based results (Figure 4C).biorxiv;2024.09.26.615284v2/FIG4F4fig4Figure 4:Benchmark of tumor clonal evolution inferenceA: Sankey diagrams illustrate the clonal structures inferred from scDNA and scRNA of gli
- Additional information is available in Figure S12-13.For CRC cases, we studied the cases with at least 10 tumor cells (Figure 2A).
- If the number of predicted subclones are larger than two by different methods, clusters were combined based on similarity of their CNV profiles (Figure S12A-B).
- Upon manual inspection, two samples (CRC03 and CRC11) showed two sizeable subclones.
- In the case of CRC03, a similar tumor calling error occurred only with inferCNV (Figure 4D).
- InferCNV incorrectly assigned the tumor C1 subclone as normal cells, thus failing to detect the two subclones correctly.
- Adding TME cells to inferCNV corrected the misclassification and improved subclonal structure inference (Figure S12 C-E).
- Most of the other four tools performed well in assigning subclones (Figure 4 E-F), although the CNAs profiles for subclones from scDNA-Seq were not fully recapitulated.
- In the case of CRC11, where all tools correctly classified tumor cells, all tools achieved favorable performance (ARI >0.8 for all tools, Figure 4G-I).
- Interestingly in one extreme case, a subclone defined in CRC12 consisted of only one single cell, and inferCNV and SCEVAN correctly detected such single cell subclone (Figure S13A-B).To conclude, given the premise of correct tumor cell classification, all five tools achieve desirable performance in 
- We selected four cell types (fibroblast, T, B and endothelial cells) with higher frequent autosomal aneuploidy events[22].
- However, the performance of all tools in identifying single-chromosome aneuploidy was generally poor (Figure S14).
- Firstly, CNA complexity in malignant is much higher (compare Figure S1 versus Figure S14).
- In addition, both the UMI count and gene count per cell in non-malignant cells were significantly lower than that of malignant cells (Figure S15).
- This highlights the importance of developing more sensitive methods for detecting low-burden CNAs in non-malignant cells.Computational speed performanceTo evaluate the computation speed of various methods, we tracked the CPU time used (Table S4).
- Based on our tests, a laptop computer could comfortably handle datasets with less than 1000 cells for all five tools.

## Figure Descriptions

### Figure 1:
Overview of the benchmarking workflowWe evaluated five tools designed to infer copy number alterations (CNAs) from single-cell RNA-seq data. The methods fall into two categories: three rely solely on gene expression matrices: inferCNV, CopyKAT, and SCEVAN, while the remaining two, Numbat and CaSpER,

### Figure 2:
Benchmark of tumor and normal cells classificationA: A bar plot illustrates the counts of tumor and normal cells for each patient.B: The F1 scores for tumor and normal cell classification in Glioma, CRC02 and CRC15.C: Boxplot showed the overall F1 scores for tumor and normal cell classification in s

### Figure 3:
Benchmark of the accuracy of inferred CNAs profilesA: Diagram illustrating CNAs profiles under unspecified (one-pass) and specified reference cells (two-pass) with inferCNV. In the one-pass scenario, inferCNV processes the whole cell population with the average as the reference. Conversely, in the t

### Figure 4:
Benchmark of tumor clonal evolution inferenceA: Sankey diagrams illustrate the clonal structures inferred from scDNA and scRNA of gliomas.B: A bar plot indicates the percentage of correct classification of the C1 subclone as tumor cells.C: Heatmaps compare the CNAs profiles of two subclones in gliom

### Figure 5:
Comparison overview for all methods.We systematically summarized the methodology, programming language used, tools version, input data formats, parameters settings, output data, computational speed and recommendations for each software. Two-pass represents running inferCNV twice and inputs normal ce

## References
Total references in published paper: 37

### Key References (from published paper)
- Single-cell technologies: From research to application (, 2022)
- Single-cell RNA sequencing technologies and applications: A brief overview (, 2022)
- Tutorial: guidelines for the computational analysis of single-cell RNA sequencing data (, 2021)
- Liver tumour immune microenvironment subtypes and neutrophil heterogeneity (, 2022)
- Insights Gained from Single-Cell Analysis of Immune Cells in the Tumor Microenvironment (, 2021)
- Single-cell landscape of the ecosystem in early-relapse hepatocellular carcinoma (, 2021)
- Single-cell RNA-seq highlights intra-tumoral heterogeneity and malignant progression in pancreatic d (, 2019)
- Single-Cell Transcriptomic Analysis of Primary and Metastatic Tumor Ecosystems in Head and Neck Canc (, 2017)
- Single-cell RNA-seq enables comprehensive tumour and immune cell profiling in primary breast cancer (, 2017)
- Tracking Cancer Evolution through the Disease Course (, 2021)
- Assessment of megabase-scale somatic copy number variation using single-cell sequencing (, 2016)
- Optimizing sparse sequencing of single cells for highly multiplex copy number profiling (, 2015)
- Single-cell, genome-wide sequencing identifies clonal somatic copy-number variation in the human bra (, 2014)
- Resolving single-cell copy number profiling for large datasets (, 2022)
- Interactive analysis and assessment of single-cell copy-number variations (, 2015)
- Dissecting the multicellular ecosystem of metastatic melanoma by single-cell RNA-seq (, 2016)
- Delineating copy number and clonal substructure in human tumors from single-cell transcriptomes (, 2021)
- A variational algorithm to detect the clonal copy number substructure of tumors from scRNA-seq data (, 2023)
- Haplotype-aware analysis of somatic copy number variations from single-cell transcriptomes (, 2023)
- CaSpER identifies and visualizes CNV events by integrative analysis of single-cell or bulk RNA-seque (, 2020)
- Spatially resolved clonal copy number alterations in benign and malignant tissue (, 2022)
- Single-Cell Multiomics Sequencing Reveals Prevalent Genomic Alterations in Tumor Stromal Cells of Hu (, 2020)
- A Highly Scalable Method for Joint Whole-Genome Sequencing and Gene-Expression Profiling of Single C (, 2020)
- scONE-seq: A single-cell multi-omics method enables simultaneous dissection of phenotype and genotyp (, 2023)
- Somatic genome variations in health and disease (, 2010)
- Single-cell transcriptome and genome analyses of pituitary neuroendocrine tumors (, 2021)
- The genomic landscape of 2,023 colorectal cancers (, 2024)
- Allele-specific genomic data elucidate the role of somatic gain and copy-number neutral loss of hete (, 2022)
- Ordered and deterministic cancer genome evolution after p53 loss (, 2022)
- p53 mutation in normal esophagus promotes multiple stages of carcinogenesis but is constrained by cl (, 2022)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 37