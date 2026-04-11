# Experimental Log: Optimizing 5’UTRs for mRNA-delivered gene editing using deep learning

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsOptimus 5-Prime predictions generalize to cells relevant to mRNA therapeuticsWe performed Massively Parallel Reporter Assays (MPRAs) to measure translation efficiency from our previously developed 5’UTR reporter library in HepG2 and T cells (Figure 1B), following an identical procedure as we 
- Briefly, our library comprised in vitro transcribed (IVT) mRNAs, with a 5’UTR containing an initial constant 25nt-long segment followed by a 50nt-long fully random region, an EGFP CDS, and a 3’UTR derived from the bovine growth hormone (BGH) gene.
- We transfected the IVT mRNA library and, after an 8 hour incubation period, extracted cell lysates in the presence of the translational inhibitor cycloheximide, performed polysome profiling to separate polysome fractions, and sequenced each fraction.
- As a proxy for translation efficiency, we calculated the Mean Ribosome Load (MRL) for each 5’UTR, by multiplying the normalized read count on each fraction by the corresponding number of ribosomes33.After filtering for sequences with at least 100 reads in all datasets, we obtained translation measur
- Analyzing a subset of the 20,000 sequences with the highest coverage, we found MRLs to be highly correlated across cell lines (Figure 1C, Supplementary Figure 1C), with coefficients of determination between cell lines (r2 = 0.837-0.870 for HEK293T versus T cells and r2 = 0.847-0.871 for HEK293T vers
- While r2 decreased as we included more sequences with lower coverage, likely an artifact of decreasing data quality, their relationship across cell lines was maintained (Supplementary Figure 1D).biorxiv;2023.06.15.545194v1/FIGS1F5figs1Supplementary Figure 1.Comparison of polysome profiling MPRA data
- (B) Comparison of number of reads for each 5’UTR sequence across all pairs of replicates.
- (C) MRL comparison for the 20,000 5’UTR sequences with the highest minimum read coverage across all replicates.
- A regression line for each pair is shown in black along with the coefficient of determination r2.
- (D) r2 as a function of the number of sequences used.
- Then, the top x sequences (x axis) were used to calculate a corresponding r2 value (y axis).
- The large marker and the gray lines indicate the number of sequences and r2 in (C).Next, we compared these measurements to Optimus 5-Prime predictions (Figure 1D).
- While the highest correlation was observed with HEK293T measurements (r2 = 0.937 on 20,000 sequences with the highest read coverage held out from training, Figure 1E), correlations with measurements in T cells and HepG2 were also high (r2 = 0.841 and 0.840 respectively).
- Prediction accuracy did not consistently increase when retraining Optimus 5-Prime individually in each cell line (Supplementary Figure 2) or when training a single multi-output model to predict on all cell lines simultaneously (Supplementary Figure 3).
- Finally, given that the most influential known regulatory elements are composed of three letters (AUG, CUG, GUG, etc), we investigated whether any 3-mers could have differential effects over MRL in different cell types.
- To this end, we trained simple 3-mer-with-position linear models on each replicate (Supplementary Figure 4A,B) and analyzed the resulting weights, but failed to find any cell line differences beyond those present in replicates of the same cell line (Supplementary Figure 4C).
- Together, these results show that observations from our polysome profiling MPRA in HEK293T, as well as predictions from Optimus 5-Prime, generalize to HepG2 and T cells.biorxiv;2023.06.15.545194v1/FIGS2F6figs2Supplementary Figure 2.Optimus 5-Prime performance when retrained on cell type-specific pol
- For every cell line and replicate indicated in each row, Optimus 5-Prime was retrained from scratch on the training dataset after filtering for sequences with more than 200 reads.
- Then, MRL predictions on the test dataset were generated and compared with measurements from each cell line and replicate in each column.biorxiv;2023.06.15.545194v1/FIGS3F7figs3Supplementary Figure 3.Performance of a multi-output version of Optimus 5-Prime.(A) Model diagram.
- The architecture is the same as the original Optimus 5-Prime, but with a final dense layer with three outputs corresponding to each cell type.
- (B) Model performance when compared to MRL measurements in all cell type replicates, on a held-out test dataset containing 20,000 sequences with the highest minimum read coverage across all replicates.biorxiv;2023.06.15.545194v1/FIGS4F8figs4Supplementary Figure 4.Analysis of 3-mer with position mode
- Five models, one per cell line and replicate, were trained on z-normalized data using Ridge regression and a regularization coefficient of 1e-5.
- Regression weights and bias are represented by the 3,072-long vector W and the scalar b.
- Models were evaluated on the 20,000 sequences with highest read coverage on each cell line and replicate, which were held out from training.
- (C) Comparison of model parameters (3,072 weights + bias) across all five models.De novo designed 5’UTRs enable high gene editing efficiency from megaTAL-encoding mRNAs Next, we used Optimus 5-Prime to design de novo 5’UTRs, with the goal of maximizing megaTAL expression from mRNA vectors and theref
- Specifically, we used megaTALs designed to disrupt two genes whose knockout in engineered T cells enhance antitumor activity56,57.
- The first megaTAL targeted exon 6 of the TGFBR2 gene, which codes for the TGF-β receptor II, a receptor for the TGF-β cytokine with prominent roles in development, regeneration, immune cell differentiation, and cancer58,59.
- Our second megaTAL targeted exon 1 of the PDCD1 gene, which codes for the signaling receptor Programmed Cell Death Protein 1 (PD-1) which acts as an inhibitory checkpoint during T cell activation60.We designed 19 de novo 5’UTRs and selected 11 control sequences, incorporated them into megaTAL-encodi
- Our controls included eight sequences previously measured in our polysome profiling MPRA33, including four with low or medium measured MRLs as well as four selected from the top 0.02% by measured MRL (Supplementary Figure 5A).
- As additional controls, we included the 5’UTR sequences of the human VAT1 and LAMA5 genes which were identified in a prior gene editing screen as the best performing natural 5’UTRs.
- In previous MPRA measurements33 these UTRs showed high translation efficiencies similar to the commonly-used beta-globin UTR (top ∼20% among ∼17,000 short endogenous, Supplementary Figure 5B).
- We alsoincluded a minimal 5’UTR consisting of nothing more than a strong Kozak sequence61, which we had previously found to result in high editing efficiency.
- All UTRs were preceded only by the initial guanine triplet inserted by IVT.biorxiv;2023.06.15.545194v1/FIGS5F9figs5Supplementary Figure 5.Controls for the megaTAL gene editing assays.(A) Selection of controls from the fixed-end MPRA library.
- For the “high MRL” control set, starting from the HEK293T MPRA library we excluded sequences with a read count lower than 1,000 or if they contained uATGs or started with TG.
- For the “submaximal MRL” control set, we similarly filtered by read count and excluded sequences with TG at the start, and selected four sequences with MRLs close to 2, 3.5, 5, and 6.5.
- Bottom: Histogram of a high-coverage (# reads > 1,000) subset of the MPRA library, along with the MRLs of all eight selected sequences.
- (B) Selection of controls from a library of short (<=100bp) human 5’UTRs measured in our previous polysome profiling study33.
- Bottom: histogram of a subset (16,779 sequences with # reads > 10) of the human 5’UTR library, along with the MRLs of the two selected sequences (VAT1, LAMA5) and the hemoglobin beta (HBB) 5’UTR commonly used in mRNA therapeutics.
- The legend indicates the MRL percentile of these three 5’UTRs compared to the rest of the library.
- In the megaTAL experiments, human 5’UTR controls did not include the initial constant 25nt, but had a consensus Kozak sequence (GCCACC) appended at their 3’ end.
- See TABLE for full sequences.biorxiv;2023.06.15.545194v1/FIG2F2fig2Figure 2.Model-based design of 5’UTRs for gene-editing mRNA therapeutics.(A) Top: schematic of megaTAL mRNA vector.
- The 5’UTR has the same architecture as in our MPRA (Figure 1B).
- Bottom: the variable 5’UTR region is designed via a combination of two design algorithms (Fast SeqProp54 or Deep Exploration Networks (DENs)55) and two regularization strategies (no additional regularization or Variational AutoEncoders (VAEs)62).
- megaTAL mRNA with each 5’UTR was individually synthesized via IVT and transfected into K562 cells.
- After 72 hours, DNA sequencing of the genomic region targeted by the megaTAL was sequenced and the gene editing efficiency was calculated.
- (C) Editing efficiencies for mRNAs with a megaTAL targeting the TGFBR2 gene, for 30 different 5’UTR including designs and controls.
- Each group of four bars represents the editing efficiency of one 5’UTR sequence transfected at four mRNA doses (0.25, 0.5, 1, or 2 pmol mRNA).
- Two biological replicates were performed per 5’UTR and mRNA dosage, and are represented by individual markers.
- Editing efficiencies for the first High MRL MPRA control, the first No VAE Fast SeqProp design, the second No VAE DEN design, and the third Varying MRL DEN design were close to zero only at a dosage of 0.25 pmol mRNA, and were deemed to be the result of experimental error and excluded from subsequen
- (D) Absolute editing efficiency as a function of mRNA dosage for a few selected 5’UTRs, indicated with a vertical arrow in the bottom panel of (C).
- (E) Kozak-normalized editing efficiency of the TGFBR2 megaTAL vs.
- Optimus 5-Prime predicted MRL for all designed and MPRA control 5’UTRs.
- (F) Comparison of Kozak-normalized editing efficiencies when using a megaTAL targeting the TGFBR2 or the PDCD1 genes.
- (G) Comparison of Kozak-normalized editing efficiencies for the TGFBR2 megaTAL in K562 versus HepG2 cells.
- In (E), (F), and (G), each marker and error bar represent the mean and standard deviation of the Kozak-normalized editing efficiencies across all mRNA dosages for a particular 5’UTR.De novo 5’UTRs were designed using either Fast SeqProp54 or DENs55 (Figure 2A).
- To preserve Optimus 5-Prime prediction accuracy, 5’UTR architecture was kept identical to the MPRA library used for training: a constant 25nt-long initial region followed by a variable 50nt segment.
- In Fast SeqProp, a candidate sequence is iteratively refined by following the gradient of the Optimus 5-Prime-predicted MRL with respect to a continuous representation of the sequence.
- By following the gradient instead of scoring multiple random mutations at each step, Fast SeqProp can design high performing sequences hundreds of times faster than simulated annealing or genetic algorithms, though it may still get stuck in local optima or overfit the predictor54.
- To reduce the possibility of overfitting, we scored designed sequences using an independently trained linear k-mer model (Methods, Supplementary Figure 6).
- By following this procedure, we generated ten candidate sequences, from which we randomly selected four to be tested in our gene editing assays.biorxiv;2023.06.15.545194v1/FIGS6F10figs6Supplementary Figure 6.Using a linear k-mer model to validate fixed-end 50nt-long Fast SeqProp designs.(A) k-mer mo
- W is a 272-long weight vector, and b is a scalar bias.
- predicted MRL on a held-out set of 25,931 5’UTRs with no uAUG and greater than 250 reads.
- Pearson r = 0.5213 (C) Comparison of predicted MRL for the four sequences designed via Fast SeqProp and the four sequences designed via Fast SeqProp with VAE regularization, when using Optimus 5-Prime or the k-mer model from panel (A).
- K-mer model predictions from the designed sequences are within the top 1% compared to equivalent predictions on the entire test set shown in (B).To design sequences with DENs, we trained a generative neural network with the objective of maximizing Optimus 5-Prime-predicted MRL while minimizing the s
- By explicitly minimizing similarity, we force the generator to capture a large section of the sequence space, thereby reducing the possibility of overfitting or getting stuck in local optima55.
- We generated 1,024 5’UTRs and selected 5 from the top 20 by predicted MRL for gene editing experiments (Supplementary Figure 7C-E).
- In addition, to validate the accuracy of the design method and predictor, we trained a DEN in “inverse regression” mode, where the generator receives an additional input that specifies a target MRL (Supplementary Figure 8A-B), and designed four 5’UTRs with predicted MRLs of 2, 3.5, 5, and 6.5 for ex
- As the predictor, we used a “retrained” version of Optimus 5-Prime, initially trained on the fixed 50nt MPRA data and finetuned on sequences we previously designed to maximize MRL that ultimately underperformed33.
- Optimus 5-Prime is used to obtain an MRL prediction from a one hot-encoded sequence sampled from logit1.
- The training objective to minimize is the weighted sum of the following components: 1) a fitness component set to −MRL, 2) a similarity component calculated from both PWMs as follows max(0, CosineSimilarity(PWM1, PWM2)marginsimilarity), and 3) an entropy component set as the Shannon Entropy of PWM1 
- Weights for the fitness, similarity, and entropy components of the loss function were 0.1, 5, and 1.
- Margin values for the similarity and entropy terms were 0.3 and 1.8.
- Training was performed for 250 epochs.
- (C) Colormap representation of 50 5’UTR sequences randomly chosen from the 1,024 generated by the trained DEN.
- (D) Distribution of edit distances per nucleotide, for 500 random pairs chosen from the MPRA library (left) or the 1,024 sequences generated by the DEN.
- (E) Distribution of MRLs measured from the MPRA library (left), or predicted by Optimus 5-Prime on all 1,024 DEN-generated sequences (middle) and the four selected sequences from this set (right).biorxiv;2023.06.15.545194v1/FIGS8F12figs8Supplementary Figure 8.Design of 5’UTR sequences of varying MRL
- Compared to Supplementary Figure 7, this network has an additional input representing the target MRL of the 5’UTR to be generated.
- Compared to Supplementary Figure 7, we additionally sample target MRL values from a uniformly random distribution during training, and set the fitness loss to the squared difference between the target and predicted MRL.
- Weights for the fitness, similarity, and entropy components of the loss function were 0.2, 5, and 1.
- Margin values for the similarity and entropy terms were 0.3 and 1.8.
- Training was performed for 100 epochs.
- (C) After DEN training, 1,024 5’UTR sequences covering a range of target MRLs were generated and compared to the MRL predicted by Optimus 5-Prime.
- (D) Colormap representation of 50 5’UTR sequences randomly chosen from the 1,024 generated by the trained DEN, sorted by predicted MRL.
- (E) Distribution of edit distances per nucleotide, for 500 random pairs chosen from the MPRA library (left) or the 1,024 sequences generated by the DEN.
- (F) Distribution of MRLs measured from the MPRA library (left), or predicted by Optimus 5-Prime on all 1,024 DEN-generated sequences (middle) and the four selected sequences from this set (right).As design algorithms seek to maximize performance, they may drift into low-confidence sequence space reg
- To prevent this, we trained a Variational Auto Encoder (VAE)62, a neural network that learns the marginal distribution of the training data and estimates the likelihood of any new sequence with respect to this distribution.
- We then used the estimated likelihood as a regularization penalty to the cost function in both Fast SeqProp and DEN (Figure 2A, Supplementary Figure 9A-F, Methods).
- Specifically, we trained a VAE on a subset of 5,000 5’UTRs selected from our MPRA dataset for their high measured MRL and read depth (Supplementary Figure 9G).
- Finally, we trained a new DEN with VAE regularization, generated 1,024 sequences with high predicted MRL, and picked two from the top 10 for gene editing assays (Supplementary Figure 10).
- In summary, 19 de novo 5’UTRs were selected for gene editing assays, including 15 sequences designed for maximal MRL (4 with Fast SeqProp, 4 with Fast SeqProp + VAE, 5 with DEN, 2 with DEN + VAE), as well as 4 UTRs with low and medium target MRLs designed with a DEN.
- The sequences of all 5’UTRs tested in gene editing assays can be found in Supplementary Table 1.biorxiv;2023.06.15.545194v1/FIGS9F13figs9Supplementary Figure 9.Variational Autoencoder (VAE) to estimate the likelihood of 5’UTR sequences in the fixed-end 50nt MPRA.(A) Schematic of a VAE structure and 
- In the VAE framework, a sequence x originates from sampling a latent vector v from a continuous prior distribution p(v)∼N(0, 1), followed by sampling x from the likelihood p(x|v).
- Sequences in the dataset used for VAE training correspond to latent vectors close to 0 and therefore more likely under the prior.
- On one hand, an encoder accepts a one hot-encoded x and returns the mean μ and log variance log(σ2) of a normal distribution corresponding to p(v|x).
- Conceptually, the marginal probability of a sequence p(x) ≅ pVAE(x) is the expected cross-entropy (“distance”) between the x and the output PWM(v), when v is sampled from p(v) = N(0,1).
- In practice, it is more efficient to sample v from N(μ(x), σ2(x)) and use a correction factor to account for the different distribution (importance sampling).
- For implementation details, see55.
- (B) During VAE training, encoder and decoder weights are updated via gradient descent to minimize the KL-divergence between N(0,1) and N(μ(x), σ2(x)), as well as the cross-entropy between x and PWM(v), for all x in the training set.
- For a more comprehensive description of VAE training, see 55.
- For the 50nt VAE, a 54nt-long sequence is used where the last 4 bases are masked out with zeros.
- (G) Likelihood of different sequence sets under a VAE trained on high MRL 5’UTR sequences.
- Histograms were generated from 1,000 sequences randomly selected from the full MPRA library, the VAE training and testing sets, or randomly generated in silico.biorxiv;2023.06.15.545194v1/FIGS10F14figs10Supplementary Figure 10.50nt 5’UTR design using Optimus 5-Prime, a Deep Exploration Network (DEN)
- Compared to Supplementary Figure 7, we here used a VAE pretrained as shown in Supplementary Figure 9 to estimate the marginal pVAE(x) of a generated sequence x, and we add a VAE component to the loss function set to max(0, marginVAE – log(pVAE(x))).
- Weights for the fitness, similarity, entropy, and VAE components of the loss function were 0.1, 5, 1, and 0.5.
- Margin values for the similarity, entropy, and VAE terms were 0.3, 1.8, and -30.
- Training was performed for 100 epochs.
- (B) Colormap representation of 50 5’UTR sequences randomly chosen from the 1,024 generated by the trained DEN.
- (C) Distribution of edit distances per nucleotide, for 500 random pairs chosen from the MPRA library (left) or the 1,024 sequences generated by the DEN.
- (D) Distribution of MRLs measured from the MPRA library (left), or predicted by Optimus 5-Prime on all 1,024 DEN-generated sequences (middle) and the two selected sequences from this set (right).To evaluate the performance of our designs, we synthesized IVT mRNA containing candidate 5’UTRs followed 
- As expected, editing efficiency increased with mRNA dosage for all 5’UTRs, with several designs exceeding 40% for the TGFBR2 and 80% for the PDCD1 megaTALs at 2 pmol mRNA (Figure 2C top, Supplementary Figure 11A top, Figure 2D).
- Editing efficiencies normalized against the Strong Kozak control (hereafter Kozak-normalized efficiencies) were highly consistent across all dosage levels (Figure 2C bottom, Supplementary Figure 11A bottom).
- However, 50% of the Fast SeqProp-generated sequences showed lower editing efficiencies despite having high predicted MRL, regardless of VAE regularization.
- Kozak-normalized editing efficiencies were highly correlated with predicted MRL over all designed 5’UTRs (Figure 2E, Supplementary Figure 11B), although Fast SeqProp-derived sequences with low editing efficiency deviated from the linear trend the most.
- While we found these observations to hold for both TGFBR2 and PDCD1 megaTALs (Figure 2F), the specific 5’UTRs resulting in maximal editing differed: LAMA5 performed the best and VAT1 performed similarly to the Strong Kozak control with the TGFBR2 megaTAL, whereas the opposite was true for PDCD1 (Fig
- Finally, we repeated our assay in HepG2 cells and, while the general trends in Kozak-normalized efficiency were maintained (Figure 2G), absolute efficiency was lower and measurement variability was higher (Supplementary Figure 12).biorxiv;2023.06.15.545194v1/FIGS11F15figs11Supplementary Figure 11.Pe
- Analogous to Figure 2C but with the PDCD1 megaTAL instead of TGFBR2.
- Editing efficiencies for the first High MRL MPRA control, the first No VAE Fast SeqProp design, the second No VAE DEN design, and the third Varying MRL DEN design were close to zero only at a dosage of 0.25 pmol mRNA, and were deemed to be the result of experimental error and excluded from subsequen
- (B) Kozak-normalized editing efficiency of the PDCD1 megaTAL vs.
- Optimus 5-Prime predicted MRL for all designed and MPRA control 5’UTRs.
- Analogous to Figure 2E but with the PDCD1 megaTAL instead of TGFBR2.biorxiv;2023.06.15.545194v1/FIGS12F16figs12Supplementary Figure 12.Performance of 50nt 5’UTR designs on the TGFBR2 and PDCD1 megaTALs in HepG2.(A and C) Editing efficiencies for mRNAs with a megaTAL targeting the TGFBR2 (A) or PDCD1
- Analogous to Figure 2C and Supplementary Figure 11A but using HepG2 cells instead of K562.
- Only three mRNA dosage levels were evaluated for TGFBR2.
- (B and D) Kozak-normalized editing efficiencies of the TGFBR2 (B) and PDCD1 (D) megaTALs vs.
- Optimus 5-Prime predicted MRL for all designed and MPRA control 5’UTRs.
- Analogous to Figure 2E and Supplementary Figure 11B but using HepG2 cells instead of K562.Measuring translation efficiency of short, fully variable 5’UTRs5’UTR regulation may differ when sequence elements are placed close to the 5’ terminus.
- For example, various pyrimidine-rich motifs have been found to influence translation in response to stress when located within a few bases of the 5’ end42–45.
- Our previous 5’UTR MPRA was unable to interrogate this region, as a fixed 25nt segment was placed at the 5’ end to facilitate library preparation (Figure 1B).
- To overcome this limitation, and to enable design of shorter 5’UTRs, we performed polysome profiling MPRAs on two new “random-end” mRNA libraries, where the 5’UTR consisted only of a variable 25nt or 50nt region preceded only by the guanine triplet introduced by IVT (Figure 3A).
- As with our previous 50nt “fixed-end” library (Figure 1B), we transfected these random-end mRNA libraries into HEK293T cells and collected lysates 12h later.
- To compensate for a lack of a constant 5’ end for PCR-based incorporation of sequencing adapters, we used template switching (TS), wherein a reverse transcriptase derived from the Moloney murine leukemia virus appends three non-templated deoxycytosines after reaching the 5’ end of the template mRNA.
- Then, a template switching oligo with three riboguanines (rGrGrG) in its 3’ end binds to the non-templated overhang, thereby becoming the new reverse transcription (RT) template and providing a fixed cDNA sequence for subsequent adapter incorporation (Figure 3A, Methods).
- We then performed Illumina sequencing and data processing (Methods), and calculated MRLs from read counts as previously33.biorxiv;2023.06.15.545194v1/FIG3F3fig3Figure 3.Polysome profiling MPRA on fully randomized 5’UTR libraries.New libraries contain a 25nt- or 50nt-long randomized region in the 5’U
- (i) Reverse transcription (RT) proceeds from the EGFP CDS into the mRNA 5’end.
- (ii) The reverse transcriptase (RTase) adds three deoxycytosines (CCC) to the 3’ of the cDNA, to which a TS primer ending in three riboguanines (rGrGrG) binds.
- (iii) the RTase “switches” templates, thereby adding the reverse complement of the TS primer to the 3’ end of the cDNA.
- (B-C) Median MRL of all sequences containing a uAUG (B) or a 5nt-long oligopyrimidine (C or U) tract (C) at the indicated position from the start of the transcript, for the 25nt-(yellow) or 50nt-long (orange) randomized 5’UTR libraries, as well as our previous “fixed-end” 50nt library (green).
- (D) Architecture of Optimus 5-Prime(25), trained on data from the random-end 25nt MPRA library.
- (E) Performance of Optimus 5-Prime(25) on a set of 2,000 5’UTRs from the random-end 25nt library held out from training.We performed two biological replicates with the 25nt random-end library and obtained good-quality (sum of reads across replicates greater than 100) MRL measurements from 168,000 di
- Inter-replicate MRL correlation was good (r2 = 0.692 for the top 20,000 sequences by read coverage, Supplementary Figure 13C, D), although lower than our previous “fixed-end” 50nt library (r2 = 0.938, Supplementary Figure 1D).
- Similarly, we performed one replicate with the 50nt random-end library, and obtained MRL measurements from 149,000 sequences at the same quality level (Supplementary Figure 14).
- As with our previous fixed-end library, we found that 5’UTRs with uAUGs out of frame with respect to the intended AUG had significantly lower MRL compared to the median of the library and with sequences with in-frame uAUGs (Supplementary Figure 15A).
- A similar effect, although of much lower magnitude, was observed for upstream non-canonical start codons (Supplementary Figure 15B, C).
- Interestingly, MRL attenuation was noticeably lower when the uAUG was located near the 5’ end in the random-end libraries, suggesting distinct regulation at the very 5’ end compared to the rest of the 5’UTR that could not be captured in our previous fixed end library (Supplementary Figure 15A, Figur
- Marker indicates 168,297 sequences with at least 100 reads.
- (C) MRL correlation across replicates, for the top 20,000 sequences by read coverage.
- (D) r2 as a function of the number of sequences used.
- Then, the top x sequences (x axis) were used to calculate a corresponding r2 value (y axis).
- The large marker indicates the number of sequences and r2 in (C).biorxiv;2023.06.15.545194v1/FIGS14F18figs14Supplementary Figure 14.Read coverage as a function of the number of sequences retained in the random-end N50 MPRA.Marker indicates 57,165 sequences with at least 100 reads.biorxiv;2023.06.15.
- (A) is identical to Figure 3B but aligned to the EGFP start codon instead of the start of the transcript.Next, we evaluated the effect of short pyrimidine tracts (5 x C/U) at different locations within the 5’UTR on measured MRL, using data from both random-end and fixed-end library data (Figure 3C, 
- We found that pyrimidine tracts generally led to a small but statistically significant MRL increase compared to the library median (Supplementary Figure 16).
- For both libraries, we observed a noticeable decrease in effect size with increasing distance of the pyrimidine tract from the 5’ end (Figure 3C, Supplementary Figure 16).
- Therefore, our data is consistent with oligopyrimidine tracts at the start of the transcript resulting in slightly increased translation in HEK293 cells even in the absence of stressors.biorxiv;2023.06.15.545194v1/FIGS16F20figs16Supplementary Figure 16.Detailed analysis of the effects of 5’UTR polyp
- Identical to Figure 3C but with the interquartile range indicated.
- (B) Bonferroni-corrected p-values from a Mann Whitney U test of medians between the MRL of sequences that contain a 5nt-long polypyrimidine tract at the indicated position versus sequences that do not contain 5nt-long polypyrimidine tracts at all.
- Horizontal bar indicates p = 10-25.
- (C) MRL of library sequences containing a 5nt-long polypyrimidine tract (C or U) within the random region, starting at position 1 (red bars), 2 or after (blue bars), anywhere (purple bars), or none at all (gray bars).
- *: p < 10-20, **: p < 10-100.Predicting translation efficiency from short, fully variable 5’UTRsWe next sought to obtain a model that generates accurate predictions on 25nt-long 5’UTRs.
- We evaluated candidate models via their prediction accuracy on the top 2,000 sequences by read coverage from the random-end 25nt MPRA library, which showed good inter-replicate correlation (r2 = 0.844, Supplementary Figure 13D).
- We first tested Optimus 5-Prime, for which 25nt-long input sequences were one-hot encoded and zero padded on the left to reach the required input length.
- However, we found its accuracy to be relatively low (r2 = 0.564 for 50nt Optimus 5-Prime, Supplementary Figure 17!, r2 = 0.600 for 25-100nt Optimus 5-Prime, Supplementary Figure 17B).
- We hypothesized that these models, trained on data from 5’UTRs with a constant 5’ region, could not properly account for differential regulatory effects that sequence elements can have when located near the start of the transcript (Figure 3B and C).
- Thus, we developed Optimus 5-Prime(25), a new model trained directly on the random-end 25nt MRPA data.
- Inspired by the convolutional network VGG-1663, Optimus 5-Prime(25) contains two blocks with two convolutional layers and one pooling layer each, followed by two fully connected dense layers that ultimately compute the predicted MRL (Figure 3D, Methods).
- This model showed good performance on the same test set which was held out from training (r2 = 0.806, Figure 3E).biorxiv;2023.06.15.545194v1/FIGS17F21figs17Supplementary Figure 17.Performance of previously developed Optimus 5-Prime models on the random-end 25nt library.(A) Performance of the origina
- (B) Performance of Optimus 5-Prime - 10033, a model with the same architecture as the original Optimus 5-Prime but trained on a 5’UTR library with a fixed 25nt segment followed by a variable region between 25 and 100nt long.
- As in Figure 3E, these models were evaluated against a test dataset comprised of the 2,000 sequences with the highest read coverage in the random-end 25nt MPRA library.Designed short 5’UTRs enable high megaTAL-induced gene editing activityFinally, we used Optimus 5-Prime(25) to design 14 shorter 5’U
- As before, we used Fast SeqProp to design ten new 5’UTRs with maximal predicted MRL, validated these against an independent k-mer linear model (Supplementary Figure 18, Methods), and randomly selected four for gene editing assays.
- We then trained a DEN to generate 1,024 25nt-long 5’UTRs that maximize both sequence diversity and predicted MRL, and selected 5 from the top 25 by MRL (Supplementary Figure 19, Methods).
- To test the effect of VAE regularization, we trained a new VAE on 5,000 high-coverage, high MRL sequences from the 25nt random-end library (Supplementary Figure 20, Methods).
- We then used VAE estimated likelihood as a regularization term to design ten additional 5’UTRs using Fast SeqProp (Supplementary Figure 18), and randomly selected two for gene editing assays.
- Similarly, we trained a new DEN with VAE regularization to generate 1,024 5’UTRs with maximal predicted MRL, from which we selected two from the top 10 (Supplementary Figure 21).
- As controls specific to this shorter 5’UTR design, we included four 5’UTRs from the random-end 25nt library with MRLs within the top 0.25% of the library (Supplementary Figure 22).biorxiv;2023.06.15.545194v1/FIGS18F22figs18Supplementary Figure 18.Using a linear k-mer model to validate 25nt-long Fast
- predicted MRL on a held-out set of 11,349 sequences with no uAUG and greater than 200 reads.
- (B) Comparison of predicted MRL for the five sequences designed via Fast SeqProp and the two sequences designed via Fast SeqProp with VAE regularization, when using Optimus 5-Prime(25) or the k-mer predictors.
- Compared to k-mer model predictions on the entire test set shown in (A), most predictions on the designed sequences are within the top 1%.
- The exceptions are two sequences designed without VAE regularization, which are within the top 1.2% and 6.3%, and one VAE-regularized design, which is within the top 4.5%.biorxiv;2023.06.15.545194v1/FIGS19F23figs19Supplementary Figure 19.25nt 5’UTR design using Optimus 5-Prime(25) and Deep Explorati
- Training was performed as described in Supplementary Figure 7 but with Optimus 5-Prime(25) (Figure 3) as the predictor.
- Weights for the fitness, similarity, and entropy components of the loss function were 0.35, 5, and 1.
- Margin values for the similarity and entropy terms were 0.3 and 1.8.
- Training was performed for 100 epochs.
- (C) Colormap representation of 50 5’UTR sequences randomly chosen from the 1,024 generated by the trained DEN.
- (D) Distribution of edit distances per nucleotide, for 500 random pairs chosen from the 25nt random-end MPRA library (left) or the 1,024 sequences generated by the DEN.
- (E) Distribution of MRLs measured from the MPRA library (left), or predicted by Optimus 5-Prime(25) on all 1,024 DEN-generated sequences (middle) and the four selected sequences from this set (right).biorxiv;2023.06.15.545194v1/FIGS20F24figs20Supplementary Figure 20.Variational Autoencoder (VAE) to 
- (E) Likelihood of different sequence sets under a VAE trained on high MRL 5’UTR sequences.
- Histograms were generated from 1,000 sequences randomly selected from the full MPRA library, the VAE training and testing sets, or randomly generated in silico.biorxiv;2023.06.15.545194v1/FIGS21F25figs21Supplementary Figure 21.25nt-long 5’UTR design using Optimus 5-Prime(25), a Deep Exploration Netw
- Compared to Supplementary Figure 19, we use a VAE, pretrained as shown in Supplementary Figure 20, to estimate the marginal pVAE(x) of a generated sequence x, and we add a VAE component to the loss function set to max(0, marginVAE – log(pVAE(x))).
- Weights for the fitness, similarity, entropy, and VAE components of the loss function were 0.3, 5, 1, and 0.5.
- Margin values for the similarity, entropy, and VAE terms were 0.3, 1.8, and -30.
- Training was performed for 100 epochs.
- (B) Colormap representation of 50 5’UTR sequences randomly chosen from the 1,024 generated by the trained DEN.
- (C) Distribution of edit distances per nucleotide, for 500 random pairs chosen from the 25nt random-end MPRA library (left) or the 1,024 sequences generated by the DEN.
- (D) Distribution of MRLs measured from the MPRA library (left), or predicted by Optimus 5-Prime(25) on all 1,024 DEN-generated sequences (middle) and the two selected sequences from this set (right).biorxiv;2023.06.15.545194v1/FIGS22F26figs22Supplementary Figure 22.Random-end 25nt MPRA “high MRL” co
- The histogram shows the measured MRLs of all four control sequences, compared with a high-coverage (# reads > 1,000) subset of the MPRA library.We tested these new designs with our gene editing assay in K562 as described above (Figure 2B, Methods).
- As with our previous designs, editing efficiency increased with mRNA dosage (Figure 4A, Supplementary Figure 23 top).
- When normalizing against the Strong Kozak control, we found that most of our designed 5’UTRs performed comparably to the high performing controls at all mRNA dosages, with exception of one of the Fast SeqProp designs (Figure 4B, Supplementary Figure 23 bottom).
- Moreover, when targeting the TGFBR2 gene, one DEN-designed sequence outperformed all other UTRs at all mRNA dosages (absolute efficiency of 55.6% at 2 pmol mRNA), improving over the previous best performer LAMA5 by 18-33% (Figure 4C).
- When considering both defined-end and random-end designs, Kozak-normalized editing efficiency was highly correlated across the TGFBR2 and PDCD1 megaTALs (Figure 4D).
- However, the DEN-designed sequence that showed the highest efficiency with the TGFBR2 megaTAL performed only as well as the Strong Kozak control when combined with the PDCD1 megaTAL (absolute efficiency of 80.8% at 2 pmol mRNA), with the VAT1 control performing best in this context (absolute efficie
- Finally, we repeated these experiments in HepG2 cells and found high Kozak-normalized efficiencies for all new designs, although high replication noise prevented us from identifying a single best performing sequence (Figure 4E, Supplementary Figure 24).
- In conclusion, by using model-based design methods with Optimus 5-Prime(25), we successfully generated de novo 5’UTRs that supported high gene editing activity, including one that outperformed all others for the TGFBR2 megaTAL.biorxiv;2023.06.15.545194v1/FIGS23F27figs23Supplementary Figure 23.Perfor
- Analogous to Figure 4A and B but with the PDCD1 megaTAL instead of TGFBR2.biorxiv;2023.06.15.545194v1/FIGS24F28figs24Supplementary Figure 24.Performance of 25nt 5’UTR designs on TGFBR2 and PDCD1 megaTALs in HepG2.Editing efficiencies for mRNAs with a megaTAL targeting the TGFBR2 (A) or PDCD1 (B) gen
- Analogous to Figure 4A-B and Supplementary Figure 23 but using HepG2 instead of K562.biorxiv;2023.06.15.545194v1/FIG4F4fig4Figure 4.Model-based design of shorter 5’UTRs for gene editing mRNA therapeutics.(A) Top: schematic of mRNA vector, with a 25nt-long variable 5’UTR segment as in Figure 3.
- Bottom: Absolute editing efficiencies for mRNAs with a megaTAL targeting the TGFBR2 gene, for 21 different 5’UTR including designs and controls.
- Each group of four bars represents one 5’UTR sequence transfected at four mRNA doses (0.25, 0.5, 1, or 2 pmol mRNA).
- Two biological replicates were performed per 5’UTR and mRNA dosage, and are represented by individual markers.
- Editing efficiencies for the first No VAE Fast SeqProp design and the second +VAE DEN design were close to zero only at a dosage of 0.25 pmol mRNA, and were deemed to be the result of experimental error and excluded from subsequent analysis.
- (C) Absolute editing efficiency as a function of mRNA dosage for a few selected 5’UTRs indicated with a vertical arrow in (B).
- (D) Comparison of Kozak-normalized editing efficiencies when using a megaTAL targeting the TGFBR2 gene vs.
- (E) Comparison of Kozak-normalized editing efficiencies for the TGFBR2 megaTAL in K562 cells or HepG2.
- In (D) and (E), each marker and error bar represent the mean and standard deviation of the Kozak-normalized editing efficiencies across all mRNA dosages for a particular 5’UTR, and designs with the fixed-end 50nt architecture (Figure 2 and relevant Supplementary Figures) are also included.

## Figure Descriptions

### Figure 1.
Massively Parallel Reporter Assays (MPRAs) to measure cell type-specific 5’UTR regulation of translation.(A) A model-based design strategy for 5’UTRs in mRNA therapeutics applications, using neural network-based predictive models trained on MRPA data. (B) Summary of polysome profiling MPRA. A librar

### Supplementary Figure 1.
Comparison of polysome profiling MPRA data in HEK293, T cells, and HepG2.(A) Cell lines and number of biological replicates. (B) Comparison of number of reads for each 5’UTR sequence across all pairs of replicates. (C) MRL comparison for the 20,000 5’UTR sequences with the highest minimum read cover

### Supplementary Figure 2.
Optimus 5-Prime performance when retrained on cell type-specific polysome profiling data.The top 20,000 5’UTR sequences with the highest minimum read coverage across all cell type replicates were separated for testing, and the remaining sequences were used for training. For every cell line and repli

### Supplementary Figure 3.
Performance of a multi-output version of Optimus 5-Prime.(A) Model diagram. The architecture is the same as the original Optimus 5-Prime, but with a final dense layer with three outputs corresponding to each cell type. During training, we added an additional final layer containing learnable linear s

### Supplementary Figure 4.
Analysis of 3-mer with position models across all cell type replicates.(A) Model schematic. Five models, one per cell line and replicate, were trained on z-normalized data using Ridge regression and a regularization coefficient of 1e-5. Regression weights and bias are represented by the 3,072-long v

### Supplementary Figure 5.
Controls for the megaTAL gene editing assays.(A) Selection of controls from the fixed-end MPRA library. For the “high MRL” control set, starting from the HEK293T MPRA library we excluded sequences with a read count lower than 1,000 or if they contained uATGs or started with TG. The remaining sequenc

### Figure 2.
Model-based design of 5’UTRs for gene-editing mRNA therapeutics.(A) Top: schematic of megaTAL mRNA vector. The 5’UTR has the same architecture as in our MPRA (Figure 1B). Bottom: the variable 5’UTR region is designed via a combination of two design algorithms (Fast SeqProp54 or Deep Exploration Netw

### Supplementary Figure 6.
Using a linear k-mer model to validate fixed-end 50nt-long Fast SeqProp designs.(A) k-mer model architecture. W is a 272-long weight vector, and b is a scalar bias. See Methods for a description of the model and training procedure. (B) Observed vs. predicted MRL on a held-out set of 25,931 5’UTRs wi

### Supplementary Figure 7.
50nt 5’UTR design using Optimus 5-Prime and a Deep Exploration Network (DEN).(A) Architecture of the DEN generator network, which takes a continuous-valued 100-dimensional latent vector and returns a 50×4-dimesional continuous-valued logit representing a sequence. Convolutional and Transpose convolu

### Supplementary Figure 8.
Design of 5’UTR sequences of varying MRLs using Optimus 5-Prime and an “inverse regression”-type Deep Exploration Network (DEN).(A) Architecture of the DEN generator network. Compared to Supplementary Figure 7, this network has an additional input representing the target MRL of the 5’UTR to be gener

### Supplementary Figure 9.
Variational Autoencoder (VAE) to estimate the likelihood of 5’UTR sequences in the fixed-end 50nt MPRA.(A) Schematic of a VAE structure and function. In the VAE framework, a sequence x originates from sampling a latent vector v from a continuous prior distribution p(v)∼N(0, 1), followed by sampling 

### Supplementary Figure 10.
50nt 5’UTR design using Optimus 5-Prime, a Deep Exploration Network (DEN), and VAE regularization.(A) DEN training schematic. Compared to Supplementary Figure 7, we here used a VAE pretrained as shown in Supplementary Figure 9 to estimate the marginal pVAE(x) of a generated sequence x, and we add a 

### Supplementary Figure 11.
Performance of 50nt 5’UTR designs on the PDCD1 megaTAL.(A) Editing efficiencies for mRNAs with a megaTAL targeting the PDCD1 gene, for 30 different 5’UTR including designs and controls. Top: absolute editing efficiencies. Bottom: editing efficiencies normalized to the Strong Kozak control. Analogous

### Supplementary Figure 12.
Performance of 50nt 5’UTR designs on the TGFBR2 and PDCD1 megaTALs in HepG2.(A and C) Editing efficiencies for mRNAs with a megaTAL targeting the TGFBR2 (A) or PDCD1 (C) genes in HepG2 cells, for 30 different 5’UTR including designs and controls. Top: absolute editing efficiencies. Bottom: editing e

### Figure 3.
Polysome profiling MPRA on fully randomized 5’UTR libraries.New libraries contain a 25nt- or 50nt-long randomized region in the 5’UTR, preceded only by the G triplet appended by IVT. (A) Schematic of mRNA library preparation based on template switching (TS). (i) Reverse transcription (RT) proceeds f

### Supplementary Figure 13.
Basic analysis of random-end N25 MPRA library.(A) Sequencing read coverage for all sequences across two biological replicates. (B) Number of sequences resulting from a given cutoff on the total number of reads per sequence across both replicates. Marker indicates 168,297 sequences with at least 100 

### Supplementary Figure 14.
Read coverage as a function of the number of sequences retained in the random-end N50 MPRA.Marker indicates 57,165 sequences with at least 100 reads.

### Supplementary Figure 15.
Effects of upstream start codons on MRL in three MPRA libraries.Median MRL of all sequences containing a uAUG (A), uCUG (B), and uGUG (C) at the indicated position from the start of the EGFP ORF, for the 25nt-(yellow) or 50nt-long (orange) randomized 5’UTR libraries, as well as our previous “fixed-e

### Supplementary Figure 16.
Detailed analysis of the effects of 5’UTR polypyrimidine tracts on MRL in three MPRA libraries.(A) Median MRL (solid lines) and interquartile range (shaded regions) of all sequences containing 5nt-long polypyrimidine (C or U) tract at the indicated position from the start of the transcript. Identica

### Supplementary Figure 17.
Performance of previously developed Optimus 5-Prime models on the random-end 25nt library.(A) Performance of the original Optimus 5-Prime trained on the fixed-end 50nt 5’UTR library. (B) Performance of Optimus 5-Prime - 10033, a model with the same architecture as the original Optimus 5-Prime but tr

### Supplementary Figure 18.
Using a linear k-mer model to validate 25nt-long Fast SeqProp designs.See Methods for training and model details. (A) Observed vs. predicted MRL on a held-out set of 11,349 sequences with no uAUG and greater than 200 reads. Pearson r = 0.4094. (B) Comparison of predicted MRL for the five sequences d

### Supplementary Figure 19.
25nt 5’UTR design using Optimus 5-Prime(25) and Deep Exploration Networks.(A) Architecture of the DEN generator network, which takes a continuous-valued 100-dimensional latent vector and returns a 25×4-dimesional continuous-valued logit representing a sequence. Convolutional and Transpose convolutio

### Supplementary Figure 20.
Variational Autoencoder (VAE) to estimate the likelihood of 5’UTR sequences in the 25nt random-end MPRA.The general VAE architecture and training scheme is identical to those in Supplementary Figure 9A and B. (A-D) Architecture of the Encoder network (A), decoder network (B), and the residual blocks

### Supplementary Figure 21.
25nt-long 5’UTR design using Optimus 5-Prime(25), a Deep Exploration Network (DEN), and VAE regularization.(A) DEN training schematic. Compared to Supplementary Figure 19, we use a VAE, pretrained as shown in Supplementary Figure 20, to estimate the marginal pVAE(x) of a generated sequence x, and we

### Supplementary Figure 22.
Random-end 25nt MPRA “high MRL” controls for the megaTAL gene editing assays.(A) Starting from the random-end 25nt MPRA library data in HEK293T, we excluded sequences if their read count was lower than 1,000 or if they contained uATGs. The remaining sequences were sorted by MRL, and four from the to

### Supplementary Figure 23.
Performance of the 25nt 5’UTR designs on the PDCD1 megaTAL.Editing efficiencies for mRNAs with a megaTAL targeting the PDCD1 gene, for 21 different 5’UTRs including designs and controls. Top: absolute editing efficiencies. Bottom: editing efficiencies normalized to the Strong Kozak control. Analogou

### Supplementary Figure 24.
Performance of 25nt 5’UTR designs on TGFBR2 and PDCD1 megaTALs in HepG2.Editing efficiencies for mRNAs with a megaTAL targeting the TGFBR2 (A) or PDCD1 (B) genes in HepG2 cells, for 21 different 5’UTRs including designs and controls. Top: absolute editing efficiencies. Bottom: editing efficiencies n

### Figure 4.
Model-based design of shorter 5’UTRs for gene editing mRNA therapeutics.(A) Top: schematic of mRNA vector, with a 25nt-long variable 5’UTR segment as in Figure 3. Bottom: Absolute editing efficiencies for mRNAs with a megaTAL targeting the TGFBR2 gene, for 21 different 5’UTR including designs and co

### Supplementary Figure 25.
Half-life predictions for mRNAs containing all designed 5’UTRs versus editing efficiencies.Predictions were made using Saluki35, a model comprised of an ensemble of 50 hybrid convolutional/recurrent neural networks. Inputs to the predictor are a one-hot encoded mRNA sequence, a binary sequence indic

## References
Total references in published paper: 64

### Key References (from published paper)
- The challenge and prospect of mRNA therapeutics landscape (, 2020)
- mRNA vaccines manufacturing: Challenges and bottlenecks (, 2021)
- Genome Editing with mRNA Encoding ZFN, TALEN, and Cas9 (, 2019)
- The delivery challenge: fulfilling the promise of therapeutic genome editing (, 2020)
- Safety and Efficacy of the BNT162b2 mRNA Covid-19 Vaccine (, 2020)
- Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine (, 2021)
- mRNA-Based Protein Replacement Therapy for the Heart (, 2019)
- Delivery of mRNA Therapeutics for the Treatment of Hepatic Diseases (, 2019)
- Emergence of synthetic mRNA: In vitro synthesis of mRNA and its applications in regenerative medicin (, 2018)
- mRNA-Enhanced Cell Therapy and Cardiovascular Regeneration (, 2021)
- In Vitro-Transcribed mRNA Chimeric Antigen Receptor T Cell (IVT mRNA CAR T) Therapy in Hematologic a (, 2020)
- mRNA therapeutics in cancer immunotherapy (, 2021)
- Unlocking the promise of mRNA therapeutics (, 2022)
- mRNA and gene editing: Late breaking therapies in liver diseases (, 2022)
- Delivery technologies for genome editing (, 2017)
- megaTALs: a rare-cleaving nuclease architecture for therapeutic genome engineering (, 2014)
- Efficient modification of CCR5 in primary human hematopoietic cells using a megaTAL nuclease and AAV (, 2015)
- Efficient Modification of the CCR5 Locus in Primary Human T Cells With megaTAL Nuclease Establishes  (, 2016)
- A Phase 1/2 Study of bbT369, a Dual Targeting CAR T Cell Drug Product With a Gene Edit, in Relapsed  (, 2022)
- Lipid nanoparticles for mRNA delivery (, 2021)
- Incorporation of Pseudouridine Into mRNA Yields Superior Nonimmunogenic Vector With Increased Transl (, 2008)
- N1-methylpseudouridine-incorporated mRNA outperforms pseudouridine-incorporated mRNA by providing en (, 2015)
- Phosphorothioate cap analogs increase stability and translational efficiency of RNA vaccines in imma (, 2010)
- Codon bias and heterologous protein expression (, 2004)
- Optimization of mRNA untranslated regions for improved expression of therapeutic mRNA (, 2018)
- Improving mRNA-Based Therapeutic Gene Delivery by Expression-Augmenting 3ʹ UTRs Identified by Cellul (, 2019)
- Combining an optimized mRNA template with a double purification process allows strong expression of  (, 2021)
- Combinatorial optimization of mRNA structure, stability, and translation for RNA-based therapeutics (, 2022)
- Decoding mRNA translatability and stability from the 5ʹ UTR (, 2020)
- A census of human RNA-binding proteins (, 2014)

## Ground Truth Reference
- Figures: 29
- Tables: 0
- References: 64