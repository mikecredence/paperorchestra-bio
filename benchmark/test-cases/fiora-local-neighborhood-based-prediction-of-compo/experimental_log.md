# Experimental Log: Fiora: Local neighborhood-based prediction of compound mass spectra from single fragmentation events

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- To this end, we employ a GNN to learn hidden representations of the molecules and formulate bond breaks as an edge property prediction task, as illustrated in Figure 1.
- Our model takes into account the local neighborhood of each bond, thus exploiting a close-to-complete chemical representation relevant for deciphering fragmentation events and ion rearrangements.biorxiv;2024.04.22.590551v1/FIG1F2fig1Figure 1:Illustration of how a graph network translates local struc
- Further details on the model and the spectral reconstruction algorithm can be found in the Methods section.The graph network module also allows traditional molecular property prediction, as seen in other fields such as drug property prediction [24].
- The training and test datasets are aggregated from multiple sources and much effort has been put to accommodate a variety of MS experiments.DataFiora is trained on a merged library from NIST (2017) and MS-Dial [34].
- Two 10% splits are taken for validation and testing, respectively.
- In addition, spectra from the CASMI challenges in 2016 and 2022 provide a more independent distribution of unknown compounds.
- Although spectral reference libraries have since been expanded, the CASMI challenge compounds remain important cornerstones for cross-referencing the performance of metabolomics software and have been used for benchmarking purposes in many studies [23, 31].
- The effect of different architectures on cosine similarity (using square root intensities, as described in Evaluation metrics) between the spectral reconstruction and the ground truth validation spectra is shown in Figure 2.
- There is a sweet spot in graph depth at 4 to 6 layers, which maximizes cosine similarity to the validation set.
- Notably, 0 or 1 graph layers are significantly less powerful because very little structure information is aggregated.
- Similarly, a high number of graph layers (>7) leads to reduced performance.
- GNNs are known to lose expressive power when too many graph convolutions are applied, as the hidden node representations become indistinguishable [35].
- The integration of bond type information to graph convolutions, as seen in the RGCN compared to the GCN, appears to have a small positive impact on prediction quality for high network depth.biorxiv;2024.04.22.590551v1/FIG2F3fig2Figure 2:Median cosine similarity evaluated on the validation split.
- Error bars show the 95% confidence interval.
- Cosine similarity reaches its peak between a network depth of 3 and 6 layers before it falls off again.
- This way, at depth 0 the predictor is aware of the bond type and the connected atoms.
- Similarly, at depth 5, substructure information of up to 6 atoms from either side is aggregated, thereby covering a complete 6-cycle ring structure.
- The RGCN with a depth of 6, which performed best on the validation set, was selected for subsequent benchmarking on the three test sets.
- [31] conducted a comprehensive benchmarking study, in which ICEBERG outperformed all other spectral prediction software.
- For this reason, we compare Fiora with ICEBERG and CFM-ID.Table 1 shows the overall cosine scores, separated for positive [M+H]+ and negative [M-H]-precursor charges.
- For CFM-ID this was not feasible and the latest model, pre-trained on the METLIN library [17], was used instead.biorxiv;2024.04.22.590551v1/TBL1T1tbl1Table 1:Median cosine similarity of spectral predictions to ground truth test spectra.
- For more information on the test sets, please refer to the Training and testing section.Fiora’s predicted MS/MS spectra exhibit the highest median cosine similarity to reference test spectra for the test split and CASMI 16 dataset, with a gain ranging from 10% to 44% over the runner-up.
- For the CASMI 22 dataset, the overall cosine scores are significantly lower for all algorithms compared to the other test sets.
- The performance between ICEBERG and CFM-ID is similar, with ICEBERG being slightly better on the test split and CASMI 16, but CFM-ID being superior on the CASMI 22 dataset.
- Keep in mind, that our filtered training library is smaller than the library ICEBERG was trained on [31] and different from the METLIN database [17] used by CFM-ID.
- Fiora takes this idea even further by using continuous collision energies as an input parameter, which might be another reason for Fiora’s overall stellar performance.Interestingly, the low cosine scores for CASMI 22 coincide with the results reported by Goldman et al.
- In fact, we also find that compounds in the CASMI 22 dataset have lower structural similarity to our training sets, compared to the 2016 dataset.
- Moreover, we identified 15 compounds from the CASMI 22 challenge in the initial NIST and MS-Dial spectral libraries, which were subsequently removed for test/training separation.
- This overlap allows us to examine differences between the spectral measurements recorded in the spectral (training) libraries and the CASMI 22 test set.
- For instance, 25% of matching spectra have a cosine similarity of less than 0.1.
- To clarify, the matching library spectra present a completely valid test set with the same compounds as CASMI 22, but have very little spectral similarity to the actual CASMI 22 spectra, despite similar experimental conditions.
- This suggests that the CASMI 22 test set cannot be considered canonical.
- With that said, we deliberately report the CASMI 22 results to explore the limits of the different implementations.
- A section in the Supplementary Material is specifically dedicated to explaining the discrepancies and intricacies with the CASMI 22 dataset, including a more nuanced performance analysis.
- It is evident that CASMI 22 contains examples that are difficult to model, predominantly spectra with little signal intensity that can be explained by single-step fragmentation.
- We identify this as the main reason Fiora’s underperformance on this particular dataset, which we discuss thoroughly in The impact of single-step fragmentation section.Overall, Fiora outperforms both ICEBERG and CFM-ID in all but one test set, and even surpasses CFM-ID on the “challenging” CASMI 22 
- In this section, we provide an overview of Fiora’s ability to generalize to unknown compounds, evaluate the performance across different compound classes, and contextualize the latent feature representation acquired by Fiora’s graph module with the structural properties of the compounds under study.
- These compounds are of particular interest for spectral prediction because they cannot be easily related to other reference compounds using methods such as Molecular Networking, and constitute the unexplored chemical space, i.e., metabolomic “dark matter” [4].
- Figure 3 depicts the median cosine similarity at different levels of Tanimoto similarity.
- Interestingly, Fiora’s prediction quality remains stable with a median cosine similarity of above 0.85 for Tanimoto similarities above 0.6 and decreases only at lower Tanimoto similarity levels.
- Even for the most dissimilar set of compounds, the median cosine similarity is above 0.7, indicating excellent performance when generalizing to unfamiliar structures.
- ICEBERG appears to have difficulty predicting spectra for compounds with a very low Tanimoto similarity of 0.2 to 0.3.
- This is evident in Figure 3, where there is a lack of a clear upward trend for CFM-ID and wider confidence intervals (as seen in the error bars).
- Importantly, the performance of CFM-ID is also lower for low Tanimoto similarities between 0.2 and 0.4, indicating that these compounds are either in fact rather uncommon or at the very least challenging to predict.
- We conclude that Fiora generalizes quite well to structurally dissimilar compounds, but shows a visible drop in quality for compounds with Tanimoto scores below 0.6, as expected.
- Still, the relative loss of performance loss is lower for Fiora (18%) than for ICEBERG (26%), when comparing the best performing interval to the interval with the lowest Tanimoto similarity.
- For the CASMI challenges this trend is even less pronounced (as shown in the Supplementary Material).biorxiv;2024.04.22.590551v1/FIG3F4fig3Figure 3:Cosine similarity at intervals of structural similarity of compounds from the test split to training compounds, measured by maximum Tanimoto similarity 
- Figure 4b shows the cosine similarity scores for individual compound superclasses, annotated using ClassyFire [36].
- Fiora consistently achieves a median cosine score well above 0.7 for all compound superclasses, except for organohalogen compounds, which have a median score of 0.61.
- However, there are only three unique organohalogen compounds (11 spectra) in the test set, so this result carries little statistical weight.
- Similarly, nucleosides, nucleotides and analogues have an extremely high cosine similarity of 0.88 based on only 5 unique compounds (19 spectra).
- Overall, Fiora’s performance appears to be robust across the test set without emphasizing specific compounds at the superclass level.biorxiv;2024.04.22.590551v1/FIG4F5fig4Figure 4:a) Uniform Manifold Approximation and Projection (UMAP) [37] visualization of the molecular graph embeddings.
- Each point corresponds to a unique compound and is color-coded based on compound superclasses, annotated by Classy-Fire [36].
- Prediction performance is consistent across most superclasses, with median scores of above 0.7.At the same time, the shared molecular structures within the compound superclasses have a significant impact on the latent representation that Fiora learns.
- Figure 4a shows Fiora’s graph embeddings (mean pooled over all nodes) after a UMAP dimensionality reduction to 2-D [37], with each compound colored according to its corresponding superclass.
- It is all the more impressive to see that this still results in compound embeddings that form structural clusters in Figure 4a, which can be broadly separated by their superclasses.
- Fiora not only produces structurally meaningful embeddings, but also encapsulates critical information about the 3-D structure (CCS) and chromatographic properties (RT), and quite possibly other pertinent molecular properties as well.Retention time and collision cross sectionFiora’s architecture was
- The model was trained on a small dataset of 409 compounds with RT information and 1346 compounds with CCS values from the MS-Dial library.
- (2019) on the Metlin small molecule retention time (SMRT) dataset [38].Figure 5 presents parity plots for RT and CCS values, comparing Fiora’s predictions to the experimental measurements.
- In terms of RT prediction, the majority of RT predictions fall within a 30-second deviation, although a non-negligible number do not.
- The Pearson correlation coefficient (r) between the predictions and observations is 0.82 and an R2 value is 0.65.
- report a good performance with a median absolute deviation of 35 seconds on the SMRT dataset [38].
- All RT values in our study come from the BMDMS-NP library [39], which is a part of the MS-Dial spectral library.
- The results suggest that RT prediction with Fiora is possible, but requires extensive retraining with a larger and more homogeneous dataset.biorxiv;2024.04.22.590551v1/FIG5F6fig5Figure 5:Parity plot of RT a) and CCS b) predictions by Fiora.
- Retention time values for the test sets were retrieved from the BMDMS-NP library [39] and CCS values from the whole MS-Dial library [34].
- The dashed lines indicate a 30 second deviation for RT and a 10% deviation for CCS values from the ground truth observations.Predicted CCS values are shown for all three test sets in Figure 5b.
- CCS values for CASMI 16 and CASMI 22 compounds could be partially annotated using the MS-DIAL library as reference, although only 2 compounds were found for CASMI 22.
- The vast majority of predictions fall within a 10% error range.
- Fiora achieves a very high Pearson correlation coefficient (r) of 0.97 and R2 value of 0.95 for the test split, which is slightly better than linear regression (with r= 0.95; R2=0.9).
- Notably, for CASMI 16 compounds, Fiora predictions are significantly better than linear regression with a Pearson correlation coefficient of 0.96 and R2 of 0.92 (compared to r=0.79 and R2=0.61).
- Table 2 shows the total and average prediction time measured for the algorithms across all test sets.
- Fiora runs approximately 20 times faster on the GPU than on the CPU, and predicts around 10,000 spectra within just five minutes on an NVIDIA A100 GPU.
- On CPU, Fiora is still 4.6 times faster than CFM-ID but slightly slower than ICEBERG.biorxiv;2024.04.22.590551v1/TBL2T2tbl2Table 2:Run time comparison over all test sets.
- [31], we observe a slightly lower average prediction time for ICEBERG and a significantly lower prediction time for CFM-ID.
- This was realized for the training loop, where 200 epochs of training and validation (without early stopping) were completed in 3 hours.
- Additional training of RT and CCS values took under 10 minutes.
- In comparison, ICEBERG was trained on only the positive spectra on a GPU for over 6 days.
- Figure 6 displays the impact of peak intensity coverage on the cosine similarity of the predicted spectra.
- The maximum cosine similarity that can be reached is bounded by the square root of the coverage, shown by the dotted line in Figure 6.
- We have also shown in the section Fiora generalizes well across compound classes and to unknown compounds that our approach does not lead to major performance differences between compound superclasses or for structurally distinct compounds.biorxiv;2024.04.22.590551v1/FIG6F7fig6Figure 6:Cosine simila
- Occasional outliers above arise from differences in the relative tolerance (50 ppm) Fiora uses for fragment annotation and the absolute tolerance (0.05 Da) used to calculate cosine similarity.
- CASMI 2016 represents a standard dataset with high coverage distribution, resulting in overwhelmingly high cosine scores.
- CASMI 2022 represents a rare low-coverage scenario, which leads to low cosine scores.However, low coverage still has a noticeable effect on the overall performance.
- This is particularly evident in Figure 6 (top panel) for the CASMI 22 dataset, where most compound spectra have an intensity coverage of close to 0.
- Remember that we have already pointed out inconsistencies in the CASMI 22 data in the Spectral prediction quality section, so the low coverage is likely influenced by an abundance of noise peaks or poor spectral quality.
- High coverage, as seen in CASMI 16 and the test split, is directly correlated with a significantly higher prediction quality for Fiora.While Fiora undoubtedly faces a limitation with its fragmentation method, it effectively compensates by leveraging graph substructures and covariate information to n

## Tables

### Table 1:
> Median cosine similarity of spectral predictions to ground truth test spectra. The columns are arranged according to the test sets and precursor ion modes (positive and negative). ICEBERG operates in 


### Table 2:
> Run time comparison over all test sets. The number of predictions vary due to the specifications of each algorithm. Fiora is the only software that predicted all compounds at all collision energies.


### Table 3:
> Overview of the two spectral libraries used for training. Sources list only the biggest contributions. Additional information is found on the provider websites https://www.sisweb.com/software/ms/nist1


## Figure Descriptions

### 


### Figure 1:
Illustration of how a graph network translates local structure information into molecular property prediction. The network performs multiple graph convolutions on the molecular structure graph, thereby aggregating the local neighborhood, i.e., the surrounding substructure, into hidden representation

### Figure 2:
Median cosine similarity evaluated on the validation split. Error bars show the 95% confidence interval. Cosine similarity reaches its peak between a network depth of 3 and 6 layers before it falls off again. The graph convolution (GCN) and relational graph convolutional networks (RGCN) perform bett

### Figure 3:
Cosine similarity at intervals of structural similarity of compounds from the test split to training compounds, measured by maximum Tanimoto similarity (Jaccard index) using Morgan fingerprints with 2048 bits and a radius of 3. Results are shown for positive ionization spectra to ensure the same dat

### Figure 4:
a) Uniform Manifold Approximation and Projection (UMAP) [37] visualization of the molecular graph embeddings. Each point corresponds to a unique compound and is color-coded based on compound superclasses, annotated by Classy-Fire [36]. Clustering of compounds according to their superclasses is evide

### Figure 5:
Parity plot of RT a) and CCS b) predictions by Fiora. Retention time values for the test sets were retrieved from the BMDMS-NP library [39] and CCS values from the whole MS-Dial library [34]. The diagonal lines describe perfect prediction. The dashed lines indicate a 30 second deviation for RT and a

### Figure 6:
Cosine similarity over peak intensity coverage for predicted spectra from the CASMI 2016 and 2022 challenges. The dotted line describes an optimistic upper bound, i.e., maximum cosine similarity at that specific intensity coverage. Occasional outliers above arise from differences in the relative tol

### Figure 7:
Depiction of Fiora’s fragmentation algorithm exemplified for the central bond. Fiora learns the local neighborhood of the bond over several graph convolutions, as illustrated by the dotted arrows indicating the information flow. The learned molecular structure is outlined in blue. For visual clarity

## References
Total references in published paper: 49

### Key References (from published paper)
- From mass to metabolite in human untargeted metabolomics: Recent advances in annotation of metabolit (, 2019)
- The basics of mass spectrometry in the twenty-first century (, 2003)
- Electrospray ionisation mass spectrometry: principles and clinical applications (, 2003)
- Illuminating the dark matter in metabolomics (, 2015)
- Searching molecular structure databases with tandem mass spectra using CSI: FingerID (, 2015)
- SIRIUS 4: a rapid tool for turning tandem mass spectra into metabolite structure information (, 2019)
- Hydrogen rearrangement rules: computational MS/MS fragmentation and structure elucidation using MS-F (, 2016)
- Identifying metabolites by integrating metabolome databases with mass spectrometry cheminformatics (, 2018)
- Topic modeling for untargeted substructure exploration in metabolomics (, 2016)
- Critical assessment of small molecule identification 2016: automated methods (, 2017)
- Physicochemical Prediction of Metabolite Fragmentation in Tandem Mass Spectrometry (, 2018)
- PubChem 2019 update: improved access to chemical data (, 2019)
- HMDB 4.0: the human metabolome database for 2018 (, 2018)
- De novo molecular formula annotation and structure elucidation using SIRIUS 4 (, 2020)
- Sharing and community curation of mass spectrometry data with Global Natural Products Social Molecul (, 2016)
- METLIN: a technology platform for identifying knowns and unknowns (, 2018)
- Metabolomics: an emerging but powerful tool for precision medicine (, 2015)
- Overview of experimental methods and study design in metabolomics, and statistical and pathway consi (, 2020)
- Metabolomics in the clinic: A review of the shared and unique features of untargeted metabolomics fo (, 2018)
- MetFrag relaunched: incorporating strategies beyond in silico fragmentation (, 2016)
- Competitive fragmentation modeling of ESI-MS/MS spectra for putative metabolite identification (, 2015)
- CFM-ID 4.0: more accurate ESI-MS/MS spectral prediction and compound identification (, 2021)
- A compact review of molecular property prediction with graph neural networks (, 2020)
- Using Graph Neural Networks for Mass Spectrometry Prediction (, 2020)
- MassFormer: Tandem mass spectrum prediction with graph transformers (, 2021)
- Do transformers really perform badly for graph representation? (, 2021)
- Mass Spectra Prediction with Structural Motif-based Graph Neural Networks (, 2023)
- QC-GN2oMS2: a Graph Neural Net for High Resolution Mass Spectra Prediction (, 2023)
- Efficiently predicting high resolution mass spectra with graph neural networks (, 2023)
- Generating molecular fragmentation graphs with autoregressive neural networks (, 2023)

## Ground Truth Reference
- Figures: 8
- Tables: 3
- References: 49