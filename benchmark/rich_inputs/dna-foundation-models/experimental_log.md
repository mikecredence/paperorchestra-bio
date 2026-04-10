# Experimental Log: Benchmarking DNA Foundation Models for Genomic and Genetic Tasks

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsSequence Classification: Pooling Methods BenchmarkWe evaluated the zero-shot embeddings from DNA foundation models on 57 sequence classification datasets, including 52 binary classification datasets and 5 multi-class datasets (Section Methods: Benchmarking Datasets).
- The detailed workflow of sequence classification benchmarking can be found in Figure 1.biorxiv;2024.08.16.608288v2/FIG1F1fig1Figure 1.Overview of sequence classification benchmark workflow.DNA sequences are input into foundation models, generating token embeddings from the final layer.
- Using DeLong’s test for statistical significance (p < 0.01), we systematically assessed which pooling method performed better for each dataset.
- Our analysis showed that mean token embedding consistently delivered superior performance against others (Supplementary Table 1).
- Specifically, mean token embedding delivered higher AUROC (AUC) with statistical significance than both summary-token embedding and maximum pooling, in 41 out of the 52 binary sequence classification datasets for DNABERT-2, 42 for NT-v2, 35 for HyenaDNA, 37 for Caduceus-Ph, and 41 for GROVER.
- On the contrary, maximum pooling or summary-token pooling rarely outperformed the other methods, being optimal in only a few specific datasets.Figure 2 illustrates the distribution of AUC scores for all models when using different pooling methods.
- The average increase in AUC when switching from summary token to mean token embedding was 4.0% (interquartile range: 2.0%-5.5%) for DNABERT-2, 6.8% (interquartile range: 3.7%-9.6%) for NT-v2, 8.7% (interquartile range: 4.6%-12.9%) for HyenaDNA, 5.9% (interquartile range: 2.8%-9.1%) for Caduceus-Ph, 
- For example, in the promoter identification task for the GM12878 cell line, mean token embedding improved the AUC from 0.964 to 0.986 for DNABERT-2, a 2.3% increase of statistical significance (p<0.01 by DeLong’s test).
- amyloliquefaciens genome, the improvement was from 0.689 to 0.864 for HyenaDNA, representing a 25.4% increase of statistical significance (p<0.01 by DeLong’s test).
- These examples illustrate how mean token embedding can capture distributed features more effectively across the entire sequence.biorxiv;2024.08.16.608288v2/FIG2F2fig2Figure 2.Boxplots comparing the AUC scores distribution on the choice of using mean output pooling, summary-token pooling, or maximum 
- Boxplots show the median (center line), interquartile range (box = 25th–75th percentiles), and whiskers correspond to 1.5 × interquartile range.
- Specifically, the range of average AUC scores across models decreased from 0.708 to 0.799 with summary-token pooling, to 0.795 to 0.822 with mean pooling.
- To evaluate our approach, we run random forest, naïve Bayes, and elastic-net logistic regression on all binary sequence classification datasets (Supplementary Figure 1).
- Given its strong performance and well-documented generalization capabilities, we selected random forest as the standard classifier for all analyses in our sequence classification benchmark, providing a reliable estimate of each foundation model’s performance on similar tasks.Sequence Classification:
- For these tasks, as shown in Table 1, when using mean token pooling, all five models achieved AUC scores above 0.8 on the majority of tasks, indicating their ability to capture meaningful semantic information from human DNA sequences.
- For promoter identification in cell lines GM12878, HUVEC, Hela-S3 and NHEK, both DNABERT-2 and Caduceus-Ph achieved statistically significant superior performance.
- DNABERT-2 showed particular strength in splice site prediction, significantly outperforming other models in both donor and acceptor identification tasks with AUCs of 0.906 and 0.897, respectively.
- For transcription factor binding site (TFBS) prediction, Caduceus-Ph consistently outperformed all other models, demonstrating its ability to capture complex regulatory patterns in the human genome.biorxiv;2024.08.16.608288v2/TBL1T1tbl1Table 1:The AUC results for binary sequence classification tasks
- Bolded: higher than at least two other AUCs, p<0.01.
- P-values are calculated using one-sided DeLong’s test.When compared to our baseline CNN model trained directly on DNA sequences, the DNA foundation models demonstrated clear advantages in several key tasks (Supplementary Tables 2-3).
- For example, for GM12878 and HUVEC cell lines promoter identification, DNABERT-2, GROVER, Caduceus-Ph, and NT-v2 all showed significant improvements over the baseline CNN.
- Overall, these four DNA foundation models demonstrated statistically significant performance gains compared to the baseline CNN.Sequence Classification: Multispecies Genome RegionsIn multispecies genome classification tasks using mean token pooling (Table 2), HyenaDNA demonstrated unexpected advanta
- For the human versus worm classification task, Caduceus-Ph and GROVER demonstrated the strongest performance (AUCs: 0.992 and 0.984), with both models achieving statistically significant advantages over other models.
- Capsulatus (AUC: 0.715) while no model achieved clear statistical superiority for B.
- amyloliquefaciens, suggesting challenges in generalizing to more distantly related prokaryotic genomes.biorxiv;2024.08.16.608288v2/TBL2T2tbl2Table 2:The AUC results for binary sequence classification tasks which have multiple species involved, including promoter region prediction (first four rows), 
- Bolded: higher than at least two other AUCs, p<0.01.
- P-values are calculated using one-sided DeLong’s test.Compared to the baseline CNN model, DNA foundation models generally underperformed for these multispecies tasks (Supplementary Tables 2-3).
- This pattern was particularly evident for the almost all datasets in Table 2, as most of the times all foundation models were outperformed by the baseline CNN.
- For human epigenetic modifications, specifically the detection of 5-methylcytosine (5mC) and N6-methyladenosine (6mA), using mean token pooling, NT-v2, Caduceus-Ph, and GROVER consistently demonstrated strong performance (Table 3).
- All three models achieved statistically significant superiority for 5mC detection, with AUCs of 0.738 (NT-v2), 0.783 (Caduceus-Ph), and 0.744 (GROVER) respectively.
- A similar pattern was observed for 6mA detection, where NT-v2, Caduceus-Ph, and GROVER again outperformed the other models.biorxiv;2024.08.16.608288v2/TBL3T3tbl3Table 3:The AUC results for each model on 5mC, 6mA detection in human; epigenetic marks detection in yeast, and 4mC detection in multiple s
- Bolded: higher than at least two other AUCs, p<0.01.
- P-values are calculated using one-sided DeLong’s test.On yeast epigenetic mark prediction, among the foundation models, DNABERT-2 showed especially robust performance across the full range of yeast epigenetic marks and performance on the 4mC detection tasks across multiple species is detailed in Tab
- As noted in our Methods, the interpretation of results for the eukaryotic 4mC datasets (A.
- With these considerations, the 4mC detection tasks (Table 4) showed that NT-v2 achieved notable performance for A.
- coli dataset (AUC: 0.628), where 4mC annotations are more directly supported.
- elegans, both NT-v2 and GROVER showed significantly better performance than other models.biorxiv;2024.08.16.608288v2/TBL4T4tbl4Table 4:Overall performance of DNA foundation models in gene expression prediction using random forest regression.
- *Note that for long input sequences, only a subset of human genes are involved in analysis.Compared to the baseline CNN, DNA foundation models generally underperformed on the human and multi-species epigenetic tasks (Supplementary Tables 2-3).
- For instance, in predicting Yeast H3, H3K4me1, and H3K79me3 marks, five and four foundation models respectively showed superior performance.
- Overall, epigenetic prediction proved more challenging for all models, with AUC scores typically 10-15% lower than for tasks distinguishing functional genomic regions.Lastly, in the rest five classification tasks with more than two classes (Supplementary Table 4), we observed notable performance var
- HyenaDNA demonstrated exceptional performance in the Regulatory Region Type classification task, achieving an accuracy of 0.83, significantly outperforming the rest.
- Similarly, for Splice Site Type classification using NT’s dataset, HyenaDNA achieved the highest accuracy of 0.563.
- For Covid Variants classification, DNABERT-2 and GROVER take the lead, while for Enhancer Strength prediction, GROVER, DNABERT-2, and Caduceus-Ph all performed comparably with accuracies over 0.7.
- Across all foundation models tested, random forest regression significantly outperformed XGBoost, achieving better correlation and lower mean squared error (MSE) between predicted and actual gene expression values (all p < 0.001) (Supplementary Table 5), regardless of whether they used shorter or lo
- Based on these results, we use random forest regression to predict gene expression from DNA foundation model zero-shot embeddings, and our subsequent conclusions are all based on random forest regression outcomes.On average, the Pearson correlation between predicted and actual gene expression was mo
- Within the short sequence models, Caduceus-Ph and HyenaDNA exhibited the highest average correlations, significantly outperforming DNABERT-2 and GROVER.
- GROVER, which used a shorter 2048 bp input, achieved a slightly lower average correlation than the other short-sequence models.
- HyenaDNA-450K demonstrated significantly better performance than Enformer (p<0.01).
- When comparing HyenaDNA and Caduceus-Ph with their longer sequence input counterparts (HyenaDNA-450K and Caduceus-Ph with longer sequence inputs) on the same set of genes, we observed that extending the sequence length significantly improved performance for HyenaDNA (p < 0.001), while the improvemen
- While average correlations were modest, certain genes were consistently predicted with substantially higher accuracy, with correlations exceeding 0.4 and reaching up to 0.9.
- This indicates that while zero-shot embeddings may not capture the regulatory complexity for all genes, they successfully identify and model genes whose expression is tightly controlled by their local sequence.biorxiv;2024.08.16.608288v2/FIG3F3fig3Figure 3.The distribution of prediction correlation 
- HyenaDNA-450K which takes longer input sequences (196K bps).
- Both models demonstrate similar distribution patterns with a slight positive skew in the histogram, indicating that while most genes have modest predictability, a subset of genes shows stronger sequence-expression relationships.Analysis of the best-predicted genes revealed a remarkable consistency i
- With 6k bp inputs, the gene CUTALP was consistently the top-predicted gene across all five short-sequence models, with correlations exceeding 0.89.
- Other highly predictable genes that consistently ranked among the top 10 across these models included CPNE1, NT5C3B, DDX11, and PEX6.
- For the long sequence models, which analyzed an extended genomic context of up to ∼196K bp, DDX11 and HLA-DRB5 consistently achieved the highest correlations across all three models.
- Other genes showing strong predictability with longer sequences included DHFR and CD151.
- Of particular relevance to blood tissue, CD151 is a tetraspanin family member that plays important roles in platelet activation and aggregation, making it highly relevant to blood function [20].
- DHFR (dihydrofolate reductase) is essential for DNA synthesis and is targeted by several drugs used to treat blood disorders [21], further highlighting the biological relevance of these predictions.While our results identify specific genes whose expression patterns appear more predictable from seque
- For the task of distinguishing pathogenic from common SNPs, the transformer-based foundation models NT-v2 and Caduceus-Ph surprisingly emerged as the top performers.
- NT-v2 was particularly dominant, achieving the highest average test AUC of 0.73 and the largest effect size (Cohen’s d: 0.88), substantially outperforming all other models, including those trained on functional tracks like Enformer (AUC: 0.69, Cohen’s d: 0.73) and Sei (Table 5).
- This suggests that the pre-training objectives of these specific foundation models are exceptionally well-suited for capturing the subtle, sequence-level patterns that differentiate pathogenic variants.biorxiv;2024.08.16.608288v2/TBL5T5tbl5Table 5:Overall performance of DNA foundation models and oth
- Bolded: top 2 highest (absolute) value.In contrast, for the putative causal QTL variant effect benchmark to distinguish putative causal QTLs from non-causal variants, models explicitly trained to predict genomic tracks (AlphaGenome [22], Enformer [23], and Sei [24]) held a clear and consistent advan
- AlphaGenome was the standout model, achieving the highest AUC and Cohen’s d scores across all four QTL types (e.g., AUC = 0.80 for sQTLs, AUC = 0.86 for ipaQTLs).
- Enformer and Sei also significantly outperformed the general DNA foundation models; for example, in eQTL prediction, Enformer achieved an AUC of 0.77, compared to the best-performing general foundation model, Caduceus-Ph, at 0.65.
- A notable finding for both Enformer and Sei was that their internal hidden states were often as predictive as their final processed output tracks; for instance, in sQTL prediction, Sei’s hidden state representation achieved an AUC of 0.65 compared to 0.63 for its output tracks.biorxiv;2024.08.16.608
- This instability was particularly pronounced on the QTL tasks with the smaller sample sizes (ipaQTL, paQTL and sQTL) where several models, including DNABERT-2, HyenaDNA, Caduceus-Ph with long sequence input, and GROVER, may yield an average AUC slightly below 0.5.
- Our nested cross-validation design makes this variance explicit: the detailed results for each test chromosome group (Supplementary Table 8) reveal that performance on these small datasets is highly sensitive to the choice of holdout chromosomes.Finally, a direct comparison between the short-and lon
- For the pathogenic SNP task, the short-sequence version of Caduceus-Ph (AUC: 0.70) clearly outperformed its long-sequence counterpart (AUC: 0.62).
- This suggests that for a single nucleotide change, a larger genomic context may dilute the local signal when using this embedding subtraction methodology.Pre-Training ExperimentWe investigated the impact of pre-training dataset diversity by re-pretraining HyenaDNA on DNABERT-2’s multi-species datase
- We maintained the hyperparameters comparable to the original HyenaDNA-1K checkpoint referring to their descriptions, though our implementation may slightly differ from the original model’s training scale in number of training steps and batch size as these were not clearly stated.The newly pre-traine
- It achieved statistically significant improvements in 14 of the 49 evaluated datasets, particularly in areas requiring cross-species generalization and diverse epigenetic pattern recognition (Supplementary Table 9).
- For instance, in human epigenetic modification tasks, the AUC for 5mC detection increased from 0.707 to 0.749, and in the cross-species human versus worm genome classification, the AUC improved from 0.968 to 0.984.
- elegans 4mC detection and various promoter identification tasks.
- On the other hand, the original HyenaDNA-1K achieved superior AUC on 3 out of the 49 datasets, related to human enhancer identification, human open chromatin region identification and yeast epigenetic mark prediction.
- To investigate this, we assessed NT-v2’s capability to recognize topologically associating domains (TADs) by analyzing attention patterns in the self-attention mechanism.
- Unfortunately, such analysis is currently constrained by model architecture; other foundation models evaluated in our study either lack accessible attention mechanisms (HyenaDNA and Caduceus-Ph), accessible attention matrices (DNABERT-2), or have input length limitations that preclude meaningful ana
- We processed 1500 TAD-centered sequences and 1500 randomly selected background sequences through NT-v2, extracting and averaging attention matrices across all layers and attention heads.
- Therefore, if NT-v2 can recognize TAD structures inherently, we would expect the attention weights to increase in the central region (approximately token positions 300-700), resulting in a vertical band of positive values in the average attention matrix when key tokens fall within the TAD region.
- Hence the differences between these two attention matrices will also show a vertical band.Supplementary Figure 2 displays the heatmap of the difference between attention matrices for TAD-centered versus background sequences.
- This suggests that NT-v2’s self-attention mechanism does not recognize TAD boundaries without specific fine-tuning.Our analysis represents the current extent of attention mechanism interpretability for DNA foundation models associated with chromatin structures, and reveals current DNA foundation mod
- This finding highlights a critical challenge and a vital area for future research, and extending such interpretability analyses is crucial for moving these models from “black box” predictors to tools that can generate essential biological insights.Runtime AnalysisOur runtime analysis revealed comput
- Despite the logarithmic scale of sequence lengths, none of the models demonstrated clear quadratic scaling, suggesting that attention computation was not the dominant factor within our experiment of batch size equal to 1.
- The HyenaDNA-160K model maintained relatively stable performance for shorter sequences (below 2K nucleotides), while HyenaDNA-1M showed excellent scaling even at sequence lengths approaching 500K nucleotides.
- DNABERT-2 demonstrated competitive runtime for sequences approaching its recommended length limit (∼2K nucleotides), beyond which we observed a dramatic runtime increase, indicated by the spike in the orange line.
- NT-v2 consistently required the highest runtime across all sequence lengths, approximately 2.5 seconds for 100 replications, which reflects its substantially larger model size of 500M parameters, yet the runtime is highly stable.
- GROVER demonstrated the fastest runtime among all tested models for sequences within its supported length range (2K nucleotides), while Caduceus-Ph-131K showed moderate performance with gradually increasing runtime as sequence length increased.biorxiv;2024.08.16.608288v2/FIG4F4fig4Figure 4.Runtime c

## Tables

### Table 1:
> The AUC results for binary sequence classification tasks on human genome. The tasks include promoter region identification (multiple datasets), coding region detection, splice site donor and acceptor 


### Table 2:
> The AUC results for binary sequence classification tasks which have multiple species involved, including promoter region prediction (first four rows), human vs worm classification and mouse transcript


### Table 3:
> The AUC results for each model on 5mC, 6mA detection in human; epigenetic marks detection in yeast, and 4mC detection in multiple species. Using mean token pooling method. Bolded: higher than at least


### Table 4:
> Overall performance of DNA foundation models in gene expression prediction using random forest regression. *Note that for long input sequences, only a subset of human genes are involved in analysis.


### Table 5:
> Overall performance of DNA foundation models and other genomic models in the pathogenic versus common variant effect quantification task. All metrics represent the average test AUC and Cohen’s d value


### Table 6:
> Overall performance of DNA foundation models and other genomic models in QTL variant effect quantification tasks. All metrics represent the average AUC and Cohen’s d values calculated across three ind


## Figure Descriptions

### Figure 1.
Overview of sequence classification benchmark workflow.DNA sequences are input into foundation models, generating token embeddings from the final layer. These embeddings undergo output pooling to produce high-dimensional representations of input sequences. A supervised classifier (random forest) is 

### Figure 2.
Boxplots comparing the AUC scores distribution on the choice of using mean output pooling, summary-token pooling, or maximum pooling.We calculate AUC scores from all 52 binary sequence classification datasets included in this study. Boxplots show the median (center line), interquartile range (box = 

### Figure 3.
The distribution of prediction correlation between predicted and actual gene expression values.The histograms showing the prediction correlation on all genes using a. HyenaDNA and b. HyenaDNA-450K which takes longer input sequences (196K bps). Both models demonstrate similar distribution patterns wi

### Figure 4.
Runtime comparison of DNA foundation models.The sequence lengths range from 64 to 524,288 nucleotides, measured as total seconds for 1000 replications using batch size 1 on an A100 GPU. Dashed vertical lines indicate points where sequence length either exceeds the supported/recommended model input l

## References
Total references in published paper: 40

### Key References (from published paper)
- The Llama 3 Herd of Models (, 2024)
- Large language models generate functional protein sequences across diverse families (, 2023)
- scGPT: toward building a foundation model for single-cell multi-omics using generative AI (, 2024)
- Language models of protein sequences at the scale of evolution enable accurate structure prediction (, 2022)
- Epigenetic patterns in a complete human genome (, 2022)
- Understanding Transcription Factor Regulation by Integrating Gene Expression and DNase I Hypersensit (, 2015)
- DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genome (, 2024)
- Nucleotide Transformer: building and evaluating robust foundation models for human genomics (, 2025)
- HyenaDNA: long-range genomic sequence modeling at single nucleotide resolution (, 2023)
- Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling (, 2024)
- DNA language model GROVER learns sequence context in the human genome (, 2024)
- High-coverage whole-genome sequencing of the expanded 1000 genomes project cohort including 602 trio (, 2022)
- LoRA: Low-Rank Adaptation of Large Language Models (, 2021)
- Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning (, 2022)
- BEND: Benchmarking DNA Language Models on biologically meaningful tasks (, 2024)
- The tetraspanin superfamily member CD151 regulates outside-in integrin αIIbβ3 signaling and platelet (, 2004)
- DNA variants in the dihydrofolate reductase gene and outcome in childhood ALL (, 2008)
- AlphaGenome: A foundation model for genome interpretation (, 2024)
- Effective gene expression prediction from sequence by integrating long-range interactions (, 2021)
- A sequence-based global map of regulatory activity for deciphering human genetics (, 2022)
- iDHS-EL: identifying DNase I hypersensitive sites by fusing three different modes of pseudo nucleoti (, 2016)
- Predicting the in vivo signature of human gene regulatory sequences (, 2005)
- Identification of DNase I hypersensitive sites in the human genome by multiple sequence descriptors (, 2024)
- Deep learning for DNase I hypersensitive sites identification (, 2018)
- iDNA-ABF: multi-scale deep biological language learning model for the interpretable prediction of DN (, 2022)
- iDNA-MS: An Integrated Computational Tool for Detecting DNA Modification Sites in Multiple Genomes (, 2020)
- iDNA-ABT: advanced deep learning model for detecting DNA methylation with adaptive features and tran (, 2021)
- iPro-WAEL: a comprehensive and robust framework for identifying promoters in multiple species (, 2022)
- Deep4mC: systematic assessment and computational prediction for DNA N4-methylcytosine sites by deep  (, 2021)
- Genomic benchmarks: a collection of datasets for genomic sequence classification (, 2023)

## Ground Truth Reference
- Figures: 4
- Tables: 6
- References: 40