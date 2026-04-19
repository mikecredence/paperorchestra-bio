{
  "statistical_sentences": [
    "We also evaluated our method to reconstruct evolutionary relationships among proteins from the ferritin-like superfamily that are beyond the \u201ctwilight zone\u201d19 \u2014a sequence similarity range (typically 20-35% identity) that complicates the differentiation between true homologs and random matches due to insufficient sequence conservation.",
    "D) Construction of the compositional profile of energy (CPE) based on protein sequence.Correlation between Energy estimated based on structure and SequenceTo examine the profile of energy at various levels of SCOP, we employed the ASTRAL40 (95) database (version 2.08) from SCOPe as a benchmark dataset, comprising domains with no more than 40% (95%) sequence similarity, as determined by BLAST identity, and filtered for E-value similarity scores18.",
    "The red lines represent the least squares regression line, and the gray shaded area represents the 95% confidence intervals around the regression line.",
    "As shown in Fig. 2F, 96% of the interaction types displayed a correlation of less than 0.5 between energy differences and protein length, indicating that protein length does not significantly affect the accuracy of energy estimates for most interaction types.",
    "As shown in Supplementary Table 1 and Fig. 4A, B, both CPE and TM-Vec achieved 100% accuracy in distinguishing between the two protein families.",
    "All methods achieved performance levels approaching 100%, as shown in Table 1.",
    "Confidence intervals were calculated to statistically validate the accuracy of these results.",
    "The bootstrap values and confidence intervals for the main branches distinguishing the three species are provided in Fig. 6A-B and 6D, reinforcing the reliability of the energy profile-based model in reconstructing the phylogenetic tree.",
    "B) Comparison of CPE distances with the TM-scores produced by running TM-align on structures predicted by AlphaFold2, OmegaFold and ESMFold, and TM-Vec for all pairs of bacteriocins, pairs at different classes (n = 125869), pairs at the same class (n = 111349), pairs from the same class from subclass1 (n = 13431).",
    "The UMAP projection shows clustering of PLPro domains from Sarbecovirus (n = 31), Nobecovirus (n = 11), Merbecovirus (n = 35), and Embecovirus (n = 45) using SPE, CPE, and TMVec representations. n_neighbors = 13, min_dist = 0.5.",
    "The blue line illustrates the least squares regression line, and the gray shaded area represents the 95% confidence intervals around the regression line.",
    "Both methods achieved performance levels near 100%, with CPE offering faster performance.",
    "In this dataset, PLPro was divided into four subfamilies aligned with the Betacoronavirus subgenera: Sarbecovirus (n = 31), Nobecovirus (n = 11), Merbecovirus (n = 35), and Embecovirus (n = 45)23.",
    "The profile of energy (CPE) method demonstrates a remarkable accuracy of 100%, significantly surpassing other methods such as GR-Align, RMSD, and TM-Score, which range from 59.2% to 81.5%.",
    "The dataset was selected based on the following criteria:Pairwise sequence identity: Less than 50% to ensure non-redundancy.Resolution: Higher than 1.6 \u00c5 to guarantee structural accuracy.R-factor: Below 0.25 to ensure reliable crystallographic data.Protein length: Between 40 and 1,000 residues to include proteins of varying sizes while excluding excessively short or long chains.Overlap: Proteins overlapping with the test sets from this manuscript were removed from the training set.These filtered proteins were utilized to train and calculate the knowledge-based potential function as follows.Pairwise Distance-Dependent Knowledge-Based PotentialKnowledge-based potentials are derived from databases of known protein structures and are essential for estimating the energies of pairwise interactions."
  ],
  "methods_sentences": [
    "In terms of computational efficiency, the CPE method stands out as the most time-efficient, requiring a mere 1 sec for processing."
  ],
  "table_count": 0
}