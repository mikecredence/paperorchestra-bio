# Experimental Log: A Fast Approach for Structural and Evolutionary Analysis Based on Energetic Profile Protein Comparison

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- Various potential functions, such as distance-dependent, dihedral angles, and accessible surface energies leverage information from known protein structures to estimate energies of pairwise interactions7, 8.
- The energy between atom pairs was computed following equation (3) in the Method section (Fig.
- Given the 20 amino acids in proteins, equation (4) was applied to represent each protein structure using 210 distinct pairwise interaction types (Fig.
- 1C), leading to the generation of the 210-dimensional Structural Profile of Energy (SPE).
- Additionally, equation (7) was employed to compute the Compositional Profile of Energy (CPE) based on protein sequences (Fig.
- For each pair of proteins, the Manhattan distance between the profiles of energies is considered a measure of dissimilarity between them.biorxiv;2025.01.31.635838v1/FIG1F1fig1Fig.
- 1:Development of knowledge-based potential function and profile of energy.A) Construction of the knowledge-based potential function.
- D) Construction of the compositional profile of energy (CPE) based on protein sequence.Correlation between Energy estimated based on structure and SequenceTo examine the profile of energy at various levels of SCOP, we employed the ASTRAL40 (95) database (version 2.08) from SCOPe as a benchmark datas
- At first, we calculated energies for protein domains in the ASTRAL40 and ASTRAL95 datasets using both structure- and sequence-based methods.
- 2A and 2B depict the strong correlation between total energy derived from structural data (y-axis) and energy estimated from sequence data (x-axis) for the ASTRAL40 and ASTRAL95 datasets.
- Furthermore, we calculated the total energy for both protein sequences and their corresponding structures using protein domains from the ASTRAL40 dataset and analyzed the differences between these estimates.
- 2C, we specifically examined the correlation between energy differences and protein length.
- This confirms that sequence-based energy calculations can serve as a robust approximation of structural energies across proteins of varying lengths.biorxiv;2025.01.31.635838v1/FIG2F2fig2Fig.
- 2:Sequence-Structure relationship.Two-sided Pearson correlation comparing total energy estimates derived from protein sequence (X-axis) and protein structure (Y-axis) for protein domains in the A) ASTRAL40 data set and B) ASTRAL95 dataset.
- The red lines represent the least squares regression line, and the gray shaded area represents the 95% confidence intervals around the regression line.
- Two-sided Pearson correlation comparing the distances of profile of energy derived from sequence (X-axis) and structure (Y-axis) for all pairs of domains in D) ASTRAL40 and E) ASTRAL95 datasets, respectively.
- The exact p-value is less than 10e-16, which is below the precision threshold of standard statistical computations.
- F) Histogram showing the distribution of correlation coefficients between the difference in energy estimates (from sequence and structure) and protein length across all 210 pairwise interactions.
- Source data are provided as a Source Data file.For each pair of domains within the ASTRAL40 and ASTRAL95 datasets, the distances between their energy profiles were calculated using both structural and sequence-based energy estimates.
- 2D and 2E, the x-axis represents the distance between Compositional Profiles of Energies (CPE), while the y-axis represents the distance between Structural Profiles of Energies (SPE).
- 2F, 96% of the interaction types displayed a correlation of less than 0.5 between energy differences and protein length, indicating that protein length does not significantly affect the accuracy of energy estimates for most interaction types.
- 1 provides scatter plots for all 210 interaction types.
- 2 presents the distribution of total energy within protein domains from the ASTRAL40 and ASTRAL95 datasets, categorized into four structural SCOP classes: all-alpha, all-beta, alpha + beta, and alpha/beta.
- 2B).Unveiling the Energy Patterns Across SCOP HierarchyWe visualized energy profiles derived from sequence and structure for domains within the all-alpha and all-beta classes.
- 3, UMAP embeddings effectively capture structural characteristics distinguishing all-alpha and all-beta domains.
- To explore structural information at lower hierarchical levels of SCOP, two folds (a.100 and a.104) from the all-alpha class, two superfamilies (a.29.2 and a.29.3) from fold a.29, and two families (a.25.1.0 and a.25.1.2) from superfamily a.25.1 were randomly selected.
- 3 displays two figures per panel, with the left figure illustrating CPE profiles and the right figure showcasing SPE profiles.
- 3 demonstrate that protein domains within the same fold, superfamily, or family share similar energy patterns and cluster together.biorxiv;2025.01.31.635838v1/FIG3F3fig3Fig.
- 3:UMAP Visualization of Energy Profiles.The UMAP projection of structural profile of energy (SPE) and Compositional Energy Profiles (CPE) of protein domains from ASTRAL40 and ASTRAL95 represents the structural information embedded in energy profiles across hierarchical levels of SCOP; each panel inc
- The folds a.100 and a.104, superfamilies a.29.2 and a.29.3, as well as families a.25.1.0 and a.25.1.2, are randomly selected for analysis, and the UMAP plots were generated using parameters n_neighbors = 30 and min_dist = 0.1.
- Source data are provided as a Source Data file.To delve deeper into differences in distances among protein domains within the same class, we calculated pairwise distances for domains within the all-alpha class from the ASTRAL95 dataset.
- 4A-B, intraclass distances in purple are significantly lower than interclass distances in yellow.
- Similar results were obtained when calculating pairwise distances from domains within fold a.29 and comparing them with distances from domains in different folds within the all-alpha class.
- Likewise, distances between energy patterns of domains within the same superfamily a.29.3 are significantly less than distances between energy patterns of domains within fold a.29 that belong to different superfamilies (Supplementary Fig.
- Consequently, it can be inferred that energy patterns of domains belonging to the same superfamily/fold/class exhibit higher similarity than those from different superfamilies/folds/classes.biorxiv;2025.01.31.635838v1/FIG4F4fig4Fig.
- 4:Performance and Computational Efficiency of Protein Dissimilarity Measures.A) Time versus accuracy for the 1-NN classifier using GR-Align, RMSD, TM-score, Yau-Hausdorff distance, TM-Vec, and the distance between energy profiles SPE and CPE as measures of protein dissimilarity.
- B) Running times of the evaluated methods, scaled to 12 hours, with an inset zooming in on the region indicated by the dashed circle.
- The entire circle represents 80 seconds.
- n_neighbors = 13, min_dist = 0.1.
- Root Mean Square Deviation (RMSD)24 quantifies the average spatial variance between corresponding atoms or components within superimposed proteins, providing a fundamental measure of structural deviation.
- The TM-score (Template Modeling score)25 evaluates similarity by considering both residue-level alignment and overall topology, offering a nuanced assessment of structural resemblance.
- TM-Vec26, a recent advancement, employs deep learning techniques trained on diverse protein structures to enhance accuracy and efficiency in similarity assessment.
- On the alignment front, we utilized GR-Align27 with its default parameters, employing the graphlet degree similarity (GDS) metric to capture topological similarities between protein structures.
- Finally, the Hausdorff distance28 provides a measure of dissimilarity between sets of points, offering further insight into structural comparisons.
- Moreover, the method assumes that global geometric similarity correlates with functional similarity, which may not always hold true, especially for proteins whose function is dictated by specific local conformations.We employed a benchmark dataset from the CATH v4.2.0 database, consisting of 251 pro
- The protein domains varied in the number of residues, ranging from 44 to 854, with an average of 211.
- Proteins were classified using the 1-NN (1-nearest neighbor) method based on various similarity metrics, including GR-Align, RMSD, TM-score, Yau-Hausdorff distance, TM-Vec, and energy profile distances (CPE and SPE).
- As shown in Supplementary Table 1 and Fig.
- 4A, B, both CPE and TM-Vec achieved 100% accuracy in distinguishing between the two protein families.
- However, the CPE method significantly reduced computation time, completing the task in just one second compared to TM-Vec’s 67 seconds.
- The computation times listed in Supplementary Table 1 were measured on a system with a 2.4 GHz processor and 8GB of RAM.biorxiv;2025.01.31.635838v1/TBL1T1tbl1Table 1.Total accuracy and F1 measure for each of the five superfamilies by 1-NN based on CPE, SPE, and TM-Vec.To evaluate the effectiveness o
- Our classification approach utilized both energetic profiles and TM-Vec representations as features, applying 1-nearest neighbor (1-NN) classifier.
- The results, summarized in Table 1, report metrics for accuracy and F1-score, demonstrating the model’s effectiveness.
- All methods achieved performance levels approaching 100%, as shown in Table 1.
- Although α and β globins are closely related and share a common evolutionary origin, they have distinct and well-characterized functions within the hemoglobin α2β2 tetramer, despite their highly similar structures.
- Freiberger et al.23 utilized a non-redundant set of experimental structures representing 21 mammalian hemoglobins (both α- and β-globins), and their analysis revealed distinct patterns of conserved energetic frustration, corresponding to their divergent functional roles in hemoglobin.
- 4C presents the UMAP projection for these proteins, where all methods effectively differentiate between the α and β globins.Phylogeny Inference of the Ferritin-Like SuperfamilyIn conjunction with the organizational frameworks provided by SCOP, CATH, and Pfam for the protein universe, it is important
- Lundin et al.19 conducted a comprehensive analysis of protein structures within the functionally diverse ferritin-like superfamily and investigated how ferritin-like proteins are classified across Pfam, SCOP, and CATH.
- Notably, this superfamily encompasses a diverse range of proteins, including iron-storing ferritins, methane monooxygenases, the small subunit of Ribonucleotide reductase-like (RNR R2), rubrerythrins, bacterioferritins, Dps (DNA binding protein from starved cells that protects against oxidative DNA 
- As discussed by Lundin et al.19 at the superfamily level, the classification of the ferritin-like superfamily appears consistent across these databases but does differ in the amount of information provided regarding the relationships and functions of superfamily constituents.
- Malik et al.30, and Puente-Lelievre et al.31 delved into the evolutionary relationships of this superfamily by creating a phylogenetic network.
- They employed the distance-based NeighborNet network method32, utilizing distances calculated through structure-based alignment methods.
- 5A depicts the schematic tree built by Malik et al.30, and Lelievre et al.31.biorxiv;2025.01.31.635838v1/FIG5F5fig5Fig.
- 5:Phylogenetic network reconstruction of the ferritin-like superfamily.A) Schematic representation of the relationships among major ferritin-like protein families, with each subgroup shown in a distinct color.
- The red dotted line highlights the separation between two SCOP families: ferritins (SCOP ID a.25.1.1), which includes the Bacterioferritin, Ferritins, Dps, and Rubrerythrin subgroups, and the Ribonucleotide Reductase-like family (SCOP ID a.25.1.2), which includes the BMM-alpha, BMM-beta, Fatty_acid,
- Source data are provided as a Source Data file.Using the same protein structures from this superfamily as employed by Malik et al.30 and Lelievre et al.
- 31, we reconstructed the phylogeny of these proteins based on energy profiles (CPE and SPE) and the TM-Vec method.
- The dataset focuses on the SCOP Ferritin-like superfamily (a.25.1), which includes two curated families: Ferritin (a.25.1.1), containing ferritins, bacterioferritins, and Dps proteins, and Ribonucleotide Reductase-like [RNR] (a.25.1.2), comprising the RNR R2 subunit, BMM, and fatty acid desaturases.
- Phylogenetic trees constructed from SPE, TM-Vec, and CPE data using the phangorn package33 and visualized with SplitTree software34 are shown in Fig.
- 5B, D, F.In line with the reference in Fig.
- 5A, a notable observation is that all three phylogenetic trees exhibit two main branches (marked by dashed lines), representing the two families a.25.1.1 and a.25.1.2.
- Delving into specifics, the family a.25.1.1 (depicted by orange color triangles) further divides into four subgroups: ferritins, Dps, Rubrerythrin, and Bacterioferritins indicated by distinct colors in Fig.
- On the other hand, the second branch related to the a.25.1.2 family (dark blue triangles), despite SCOP and CATH assigning these proteins to a unified RNR-like family, reveals three distinct families according to Pfam—Phenol_Hydrox (PF02332), Ribonuc_red_sm (PF00268), and Fatty acid desaturase (PF03
- 5A are color-coded, corresponding to the colors used in Fig.
- 5B-G.For a comprehensive comparison with the manual annotation in Fig.
- 5A, we calculated the average interprotein distances across the eight subfamily groups using three distinct methods: CPE, SPE, and TM-Vec.
- For instance, in the a.25.1.2 family, TM-Vec incorrectly places the subgroup BMM-b first, whereas it should appear last in the manual network.
- Similarly, in the a.25.1.1 family, although TM-Vec correctly identifies the initial branch, it misorders the remaining subgroups.
- These correlations, summarized in Table 2, demonstrate that both SPE and CPE outperform TM-Vec in aligning with the manually annotated network.
- Notably, SPE achieves a perfect correlation in the a.25.1.1 family, while TM-Vec shows a negative correlation in the a.25.1.2 family, illustrating its limitations.
- Our findings indicate that the energy-based phylogenies within the ferritin-like superfamily reveal substantial relationships among its members, aligning closely with established evolutionary connections and functional roles suggested by Malik et al.30, and Lelievre et al.31 showed in Fig.
- 5A.biorxiv;2025.01.31.635838v1/TBL2T2tbl2Table 2.Spearman Correlation Between the Manual Network and Predicted Branching Orders by SPE, TM-Vec, and CPE.Clustering of the SARS-CoV-2, SARS-CoV and 2012 MERS-CoV proteinsOver the past two decades, coronaviruses (CoVs) have been linked to several signifi
- Since February 2020, a substantial number of SARS-CoV-2 protein structures have been deposited in the Protein Data Bank (PDB), with the spike glycoprotein being of particular interest due to its crucial role in viral infection by mediating host receptor binding.
- This protein is a primary target for neutralizing antibodies and vaccine development.To explore the structural landscape and evolutionary relationships of these spike glycoproteins, we used the CoV3D database(https://cov3d.ibbr.umd.edu), which provides a comprehensive collection of coronavirus prote
- From this resource, we curated a dataset of 143 spike glycoprotein structures, all containing a closed receptor-binding domain (RBD).
- This dataset comprises 80 spike protein chains from SARS-CoV-2, 31 from SARS-CoV, and 32 from MERS-CoV (Supplementary Table 4).Initially, we conducted a multiple sequence alignment of spike proteins using the ClustalW method via the msa package35 in R.
- Protein distances were calculated with the seqinr package36, using sequence identity as the distance metric.
- Phylogenetic trees were subsequently generated using the UPGMA method from the phangorn package33, and the resulting tree based on sequence similarity is presented in Fig.
- To further examine structural variations and relationships among the spike glycoproteins, we applied structural methods including RMSD, TM-Score, and SPE, alongside sequence-based methods such as CPE and TM-Vec, to calculate pairwise distances and cluster the spike glycoproteins into three distinct 
- 6A-F.biorxiv;2025.01.31.635838v1/FIG6F6fig6Fig.
- 6:Clustering analysis of spike glycoprotein structures from SARS-CoV, SARS-CoV-2, and MERS-CoV.The dendrograms depict the clustering of spike glycoprotein structures from the three viruses: SARS-CoV, SARS-CoV-2, and MERS-CoV.
- G) Displays the ARI values for each method, H) shows the running time associated with each method scaled to 12 hours, with an inset zooming in on the region indicated by the dashed circle.
- The entire circle represents 80 seconds, and I) presents the average distance between the three virus groups as calculated by each method.
- Source data are provided as a Source Data file.All methods consistently showed a clear separation between the SARS-CoV/SARS-CoV-2 lineage and MERS-CoV, which belongs to a different coronavirus subgenus.
- 6C, E, and F, methods like RMSD, TM-Score, and TM-Vec were less effective in capturing these evolutionary patterns.
- Additionally, we performed a bootstrap analysis with 100 replicates to assess the robustness of phylogenetic tree reconstructions using CPE, SPE, TM-Vec, and MSA methods.
- 6A-B and 6D, reinforcing the reliability of the energy profile-based model in reconstructing the phylogenetic tree.
- 5-8.In terms of computational efficiency, our methods—CPE and SPE—are significantly faster than the alternatives.
- CPE completes the analysis in 0.9 seconds, and SPE takes just 3 minutes, whereas TM-Vec requires 89 seconds, RMSD takes 70 minutes, MSA takes 72 seconds, and TM-Score takes 9.7 hours (Fig.
- To evaluate clustering performance, we used the Adjusted Rand Index (ARI), which measures the similarity between two clustering results, with values ranging from −1 to 1 (where 1 indicates perfect agreement).
- 6G and Supplementary Table 3, CPE method achieved the highest clustering performance with an ARI of 0.95 at a cut tree of 4, while TM-Vec performed best at a cut tree of 5, with an ARI of 0.87 and MSA with cut tree of 3 with ARI of 0.49.
- Among the structure-based methods, SPE achieved a perfect ARI of 1 at a cut tree of 3, while RMSD and TM-Score performed best at cut trees of 6 and 4, with ARIs of 0.73 and 0.56, respectively (Supplementary Table 2).
- We also computed the average distance between the three virus groups—SARS-CoV, SARS-CoV-2, and MERS-CoV—across all six methods.
- All methods consistently show that SARS-CoV-2 is more closely related to SARS-CoV than to MERS-CoV (Fig.
- Additionally, the distance between SARS-CoV-2 and MERS-CoV is nearly identical to the distance between SARS-CoV and MERS-CoV.biorxiv;2025.01.31.635838v1/TBL3T3tbl3Table 3.Large Scale: Analysis of the SARS-CoV-2 Proteome across 28 families, encompassing 4,405 proteins.The overall accuracy, F1 score, 
- We analyzed the bacteriocins family available in the BAGEL database, those with a length larger than 30 amino acids, including a total of 690 proteins21.
- To address this issue, the BAGEL tool was developed in 2006, specifically designed for identifying Ribosomally synthesized and post-translationally modified peptides (RiPP) and bacteriocin biosynthetic gene clusters (BGCs).
- BAGEL categorizes bacteriocins based on size and stability into RiPPs (also defined as class I bacteriocins by BAGEL), class II bacteriocins (small heat stable proteins < 10 kDa) and class III bacteriocins (large heat-labile proteins > 10 kDa).
- 7A, our analysis revealed that profile of energy (CPE) can clearly partition bacteriocins according to BAGEL annotation.
- Hamamsy et al.26 leveraged the deep protein language models to develop the TM-Vec model, which is trained on pairs of protein sequences and their TM-scores.
- We compared CPE distances to the TM-scores of protein structures predicted by AlphaFold237, OmegaFold38, and ESMFold39, as well as the TM-Vec predicted by the model.
- 7B, the TM-score of proteins predicted by AlphaFold2, OmegaFold, and ESMFold from the same class is similar to proteins from different classes.
- Our method also effectively distinguishes between proteins from the same class and those from other classes in bacteriocin dataset.biorxiv;2025.01.31.635838v1/FIG7F7fig7Fig.
- 7:UMAP Projection of Energy Profiles for Bacteriocins and Betacoronavirus Domains, with Distance Comparisons and Scalability Analysis.A) UMAP projection of Compositional Energy Profiles (CPE) for 690 peptides, representing three different classes of bacteriocins.
- B) Comparison of CPE distances with the TM-scores produced by running TM-align on structures predicted by AlphaFold2, OmegaFold and ESMFold, and TM-Vec for all pairs of bacteriocins, pairs at different classes (n = 125869), pairs at the same class (n = 111349), pairs from the same class from subclas
- Boxplots display the median (center line), the 25th and 75th percentiles (bounds of the box), and the minimum and maximum values (whiskers) excluding outliers.
- Comparisons of CPE distances revealed statistically significant differences across the groups (different class, same class, and subclass1 within the same class), with p-values for all three tests being < 10e-16.
- The exact p-value is less than 10e-16, which is below the precision threshold of standard statistical computations.
- The UMAP projection shows clustering of PLPro domains from Sarbecovirus (n = 31), Nobecovirus (n = 11), Merbecovirus (n = 35), and Embecovirus (n = 45) using SPE, CPE, and TMVec representations.
- n_neighbors = 13, min_dist = 0.5.
- The blue line illustrates the least squares regression line, and the gray shaded area represents the 95% confidence intervals around the regression line.
- Processing time per amino acid for subsets from the ASTRAL95 dataset, ranging in size from 1,000 to 30,000 proteins (at intervals of 5,000).
- Source data are provided as a Source Data file.Effective Drug Combination suggestion using Energetic SignaturesThe identification and validation of effective drug combinations are crucial in the treatment of various complex diseases, aiming to enhance therapeutic efficacy while minimizing toxicity40
- Cheng et al.22 introduced a network-based methodology to pinpoint clinically effective drug combinations tailored to specific diseases.
- When SAB < 0, the targets of the two drugs are in the same network neighborhood; when SAB > 0, the two targets are topologically separated.The authors demonstrated that the topological relationship between two drug-target modules, as indicated by SAB, reflects both biological and pharmacological rel
- 7D depicts the correlation between sAB values, as computed by Cheng et al.22, for a set of 65 antihypertensive drugs exhibiting complementary exposure to the hypertension disease module, and the corresponding EAB.
- It is important that our approach only requires protein sequences and is significantly faster than computing the shortest path in a protein-protein interaction network.Large-Scale Application of Family Detection in CoronavirusesTo evaluate our method on a larger dataset, we utilized a coronavirus da
- Then sequences were aligned using MAFFT software43, with non-structural protein sequences trimmed to focus on regions specifically relevant to SARS-CoV-2.
- These aligned sequences were then clustered using CD-Hit44 to ensure high similarity within each cluster.
- Structural models for these sequences were generated using AlphaFold2, retaining only those that met stringent quality criteria.
- The high-quality models were subsequently grouped into subfamilies using S3Det software45, allowing for the identification of Specificity Determining Positions (SDPs) within the proteins.
- This meticulous process resulted in a final set of 28 high-quality protein families, comprising 4,405 protein models.
- The 1-nearest neighbor (1-NN) method was then utilized to classify the proteins into different families.
- The results, shown in Table 3, include metrics for accuracy and F1-score, demonstrating the effectiveness of our model.
- Both methods achieved performance levels near 100%, with CPE offering faster performance.
- Detailed outcomes of the 1-NN classification are provided in Supplementary Supplementary Table 5-7, and the UMAP projections of SPE, CPE, and TM-Vec representations are displayed in Supplementary Fig.
- 9-11.The Papain-like Protease (PLPro) domain plays a crucial role in viral replication by catalyzing the proteolysis of viral polyproteins.
- In addition, PLPro interacts with two host proteins, ubiquitin (Ub) and the ubiquitin-like interferon-stimulated gene 15 protein (ISG15), allowing the virus to evade or weaken the host immune response.
- In this dataset, PLPro was divided into four subfamilies aligned with the Betacoronavirus subgenera: Sarbecovirus (n = 31), Nobecovirus (n = 11), Merbecovirus (n = 35), and Embecovirus (n = 45)23.
- 7C, where proteins from each subfamily are clearly clustered together.

## Tables

### Table 1.
> Total accuracy and F1 measure for each of the five superfamilies by 1-NN based on CPE, SPE, and TM-Vec.


### Table 2.
> Spearman Correlation Between the Manual Network and Predicted Branching Orders by SPE, TM-Vec, and CPE.


### Table 3.
> Large Scale: Analysis of the SARS-CoV-2 Proteome across 28 families, encompassing 4,405 proteins.The overall accuracy, F1 score, and computation time for detecting families using the 1-NN classifier.


## Figure Descriptions

### Fig. 1:
Development of knowledge-based potential function and profile of energy.A) Construction of the knowledge-based potential function. B) Estimation of the predictor matrix P. C) Construction of the structural profile of energy (SPE) based on protein structure. D) Construction of the compositional profi

### Fig. 2:
Sequence-Structure relationship.Two-sided Pearson correlation comparing total energy estimates derived from protein sequence (X-axis) and protein structure (Y-axis) for protein domains in the A) ASTRAL40 data set and B) ASTRAL95 dataset. C) Two-sided Pearson correlation between the difference in tot

### Fig. 3:
UMAP Visualization of Energy Profiles.The UMAP projection of structural profile of energy (SPE) and Compositional Energy Profiles (CPE) of protein domains from ASTRAL40 and ASTRAL95 represents the structural information embedded in energy profiles across hierarchical levels of SCOP; each panel inclu

### Fig. 4:
Performance and Computational Efficiency of Protein Dissimilarity Measures.A) Time versus accuracy for the 1-NN classifier using GR-Align, RMSD, TM-score, Yau-Hausdorff distance, TM-Vec, and the distance between energy profiles SPE and CPE as measures of protein dissimilarity. B) Running times of th

### Fig. 5:
Phylogenetic network reconstruction of the ferritin-like superfamily.A) Schematic representation of the relationships among major ferritin-like protein families, with each subgroup shown in a distinct color. B) Phylogenetic network reconstructed using SPE. C) Neighbor-joining tree generated based on

### Fig. 6:
Clustering analysis of spike glycoprotein structures from SARS-CoV, SARS-CoV-2, and MERS-CoV.The dendrograms depict the clustering of spike glycoprotein structures from the three viruses: SARS-CoV, SARS-CoV-2, and MERS-CoV. The clustering is based on pairwise distances calculated from different meth

### Fig. 7:
UMAP Projection of Energy Profiles for Bacteriocins and Betacoronavirus Domains, with Distance Comparisons and Scalability Analysis.A) UMAP projection of Compositional Energy Profiles (CPE) for 690 peptides, representing three different classes of bacteriocins. B) Comparison of CPE distances with th

## References
Total references in published paper: 50

### Key References (from published paper)
- Database resources of the national center for biotechnology information (, 2021)
- Gapped BLAST and PSI-BLAST: a new generation of protein database search programs (, 1997)
- Improved global protein homolog detection with major gains in function identification (, 2023)
- Evolution-strengthened knowledge graph enables predicting the targetability and druggability of gene (, 2023)
- pLM4ACE: A protein language model based predictor for antihypertensive peptide screening (, 2024)
- RNAincoder: a deep learning-based encoder for RNA and RNA-associated interaction (, 2023)
- Boltzmann’s principle, knowledge-based mean fields and protein folding. An approach to the computati (, 1993)
- Knowledge-based potentials in protein fold recognition (, 2010)
- A distance-dependent atomic knowledge-based potential and force for discrimination of native structu (, 2009)
- Identification of native protein structures captured by principal interactions (, 2019)
- Discrimination power of knowledge-based potential dictated by the dominant energies in native protei (, 2019)
- Hydrophobic residues can identify native protein structures (, 2018)
- The pairwise energy content estimated from amino acid composition discriminates between folded and i (, 2005)
- A method to identify protein sequences that fold into a known three-dimensional structure (, 1991)
- Protein tertiary structure recognition using optimized Hamiltonians with local interactions (, 1992)
- CATH: increased structural coverage of functional space (, 2021)
- SCOP: a structural classification of proteins database (, 2000)
- SCOPe: Structural Classification of Proteins—extended, integrating SCOP and ASTRAL data and classifi (, 2014)
- Use of structural phylogenetic networks for classification of the ferritin-like superfamily (, 2012)
- CoV3D: a database of high resolution coronavirus protein structures (, 2021)
- BAGEL3: automated identification of genes encoding bacteriocins and (non-)bactericidal posttranslati (, 2013)
- Network-based prediction of drug combinations (, 2019)
- Local energetic frustration conservation in protein families and superfamilies (, 2023)
- Significance of root-mean-square deviation in comparing three-dimensional structures of globular pro (, 1994)
- TM-align: a protein structure alignment algorithm based on the TM-score (, 2005)
- Protein remote homology detection and structural alignment using deep learning (, 2023)
- GR-Align: fast and flexible alignment of protein 3D structures using graphlet degree similarity (, 2014)
- Comparing protein structures and inferring functions with a novel three-dimensional Yau–Hausdorff me (, 2018)
- Automatic classification and analysis of αα-turn motifs in proteins (, 1996)
- Structural phylogenetics with confidence (, 2020)

## Ground Truth Reference
- Figures: 7
- Tables: 3
- References: 50