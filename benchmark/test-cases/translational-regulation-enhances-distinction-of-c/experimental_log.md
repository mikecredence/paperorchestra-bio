# Experimental Log: Translational regulation enhances distinction of cell types in the nervous system

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsComparative transcriptome-translatome analyses reveal translational suppression of selective groups of proteins in the fly headsTo gain an overview of the translation status, we first applied conventional Ribo-seq in the whole fly head, and successfully monitored footprint distribution at a s
- The majority (96.2%) of ribosome footprints was mapped onto the annotated coding sequences (CDS), and its distribution displayed a clear 3-nt periodicity, reflecting the codon-wise movement (Figure 1B).biorxiv;2023.06.15.545207v4/FIG1F1fig1Figure 1.Comparative transcriptome-translatome analyses in t
- (B) Meta-genome ribosome distribution (estimated P-sites of the 21-nt fragments), relative to the annotated start and stop codons.
- The squared Pearson’s correlation coefficient (R2) is indicated.
- The bin size is 0.2 in the unit of log 2.
- Total 9,611 genes with at least one read in both Ribo-seq and RNA-seq are plotted.
- (H) Kyoto Encyclopedia of Genes and Genomes (KEGG) pathways enrichment analysis, visualized by iPAGE (Goodarzi et al., 2009), based on TE.
- The 9,611 genes are ranked and binned according to TE (left to right: low to high), and over- and under-representation is tested.
- The presented KEGG pathways show P values smaller than 0.0005.
- ns: P > 0.05; ***: P < 0.001; in the Dunn’s multiple comparisons test, compared to the “all” group.To compare transcriptome and translatome, we also performed RNA-seq from the same lysate (Figure 1A).
- As previously reported, the transcript level and the number of ribosome footprints did not always match, suggesting substantial posttranscriptional regulations (R2 = 0.664; Figure 1C).
- For instance, while Shaker (Sh) and Trehalase (Treh), which encode a voltage-gated K+ channel and an enzyme that hydrolyzes trehalose, respectively, were similar regarding transcript levels, far more ribosome footprints were detected on Treh (Figure 1D-E).
- TE was much higher for Treh than Sh (Figure 1F), and we found a striking genome-wide variability with more than 20-fold TE difference between the 5 and 95 percentiles (Figure 1G).
- Kyoto Encyclopedia of Genes and Genome (KEGG) pathway enrichment analysis revealed that transcripts involved in fatty acid metabolism and proteasome are actively translated (Figure 1H).
- In contrast, ribosome proteins, as previously reported (Chen and Dickman, 2017; Cho et al., 2015), and proteins mediating neuronal ligand-receptor interactions were significantly enriched in the transcripts with low TE, suggesting translational suppression (Figure 1H).
- Indeed, many transcripts encoding ligand- or voltage-gated ion channels, G-protein coupled receptors (GPCR) showed remarkably low TE (Figure 1C and 1I).
- By expressing epitope-tagged RpL3 (uL3 in universal nomenclature) (Chen and Dickman, 2017) under the control of UAS using the nSyb- or the repo-GAL4 drivers, we immunopurified the tagged ribosomes and associated mRNAs separately from neurons and glia, and performed Ribo-seq (Figure 2A).
- By immunohistochemistry, we confirmed that UAS-RpL3::FLAG on the third chromosome exhibited minimum leakage expression in the brain and did not display any apparent morphological defects upon expression using either driver, compared to other insertions or constructs (Chen and Dickman, 2017; Huang et
- The exogenously expressed RpL3::FLAG was highly concentrated in cell bodies but also detectable in neurites, consistent with the subcellular localization of the endogenous ribosome (Figure 2 – figure supplement 1C-D).biorxiv;2023.06.15.545207v4/FIG2F2fig2Figure 2.Cell-type specific Ribo-seq and RNA-
- FLAG-tagged ribosome protein L3 (RpL3::FLAG) is expressed in neurons (nSyb-GAL4) or in glial cells (repo-GAL4).
- Whole brain images of the exogenously expressed RpL3::FLAG are shown.
- Each gene is plotted according to the fold change (x-axis) and the average (y-axis) in the unit of log2.
- Genes with TPM > 1 in the RNA-seq dataset are plotted.
- *: P < 0.05, **: P < 0.01, ***: P < 0.001, the Dunn’s multiple comparisons test.
- All genes with at least one read in both cell types (total 9,732 genes) are ranked and binned according to the neuron-to-glia ratio (left to right: high to low), and over- and under-representation is tested.
- The presented KEGG pathways show P values smaller than 0.0005.
- The squared Pearson’s correlation coefficient (R2) is indicated.
- ***: P < 0.001, Kruskal-Wallis test.
- All the 7,933 genes showing TPM > 1 in RNA-seq are analyzed.
- **: P < 0.01, ***: P < 0.001, Dunn’s multiple comparisons test.
- ns: P > 0.05, **: P < 0.01, ***: P < 0.001, Dunn’s multiple comparisons test.Through the purification of FLAG-tagged ribosomes, we successfully profiled translatome from neurons and glial cells in the fly heads: Footprints were found on 10,821 (78.4 % of all the annotated genes) and 10,994 (79.7 %) 
- The FLAG-tagged RpL3 in the corresponding cells far exceeded the endogenous RpL3, as RpL3 reads were 7.8 and 42.7 times higher in neurons and glia, respectively, compared to the wild-type whole-head samples (Figure 2 – figure supplement 2B).
- The known marker genes were strongly enriched while non-target markers were depleted (Figures 2B and Figure 2 – figure supplement 2C-D) (Croset et al., 2018; Davie et al., 2018; Li et al., 2022), and the KEGG enrichment analysis showed significant enrichment of footprints on genes associated with th
- Interestingly, the KEGG analysis also revealed that neurons exhibit a greater extent of protein synthesis related to oxidative phosphorylation and mitochondrial ribosome proteins, while glial cells show higher expression of proteins associated with glycolysis (Figure 2 – figure supplement 2E-F).
- These findings support the glia-neuron lactate shuttle hypothesis, a recently proposed concept of metabolic specialization (Mason, 2017; Volkenhoff et al., 2015).
- Furthermore, apart from the annotated CDS, we detected clustered ribosome footprints on Hsr-μ, previously annotated as a long non-coding RNA, strongly suggesting the synthesis of hitherto undescribed polypeptides (Figure 2 – figure supplement 2G) (Singh, 2022).
- Altogether, the combination of genetic labelling of ribosomes in selective cell types and Ribo-seq revealed the differential translatome profiles in the fly heads.To further examine translational regulation by calculating TE, we performed RNA-seq from the same immunoprecipitated complexes, similar t
- Because this approach relies on the 80S-ribosome-mRNA complex, we may miss mRNA with little or no translation.
- Nevertheless, our transcriptome was similar to the sn-transcriptome data (Li et al., 2022) (Figure 2 – figure supplement 3C).
- We identified groups of genes undergoing neuron- or glia-specific translational regulations compared to the whole heads (Figure 2 – figure supplement 4A).
- Genes mediating fatty acid metabolism and degradation, for example, were actively translated in the whole head, but showed lower TE in neurons or in glia (Figures 1H and 2C).
- Because many of these genes are highly expressed in the fat bodies (Dobson et al., 2018), these results suggest selective translational enhancement in the fat body.
- Strikingly, TE of genes involved in neuroactive ligand-receptor interaction was significantly higher in neurons but lower in glia (Figure 2C-D), suggesting cell-type specific translational regulation of these genes.This differential translational regulation was highlighted in the weak TE correlation
- We found a genome-wide tendency that genes transcribed less in glia are further suppressed at translation (Figure 2F).
- Specifically, many functionally-characterized neuronal genes, such as voltage- or ligand-gated ion channels, G-protein coupled receptors, neuropeptides and proteins for visual perception, showed particularly lower TE in glia (Figures 2E, 2G-H and Figure 2 – figure supplement 4C).
- For these genes, the distinction between neuronal and glial cells was much exaggerated at the level of translation than at transcription (Figure 2H).
- Consistently on the genome-wide scale, the inter-cell type correlation became weaker in Ribo-seq data compared to in RNA-seq (R2 = 0.59 vs.
- 0.81, Figure 2 – figure supplement 3B).
- Fat-body related genes showed lower TE in neurons compared to the whole head (Figure 2C).
- Among these genes, we found a remarkable ribosomal accumulation on the start codon specifically in neurons (Figure 3 – figure supplement 1A-B), as if the first round of the elongation cycle was arrested in neurons.
- Through the reanalysis of the published RNA-seq data (Dobson et al., 2018), we found that mRNAs showing strong ribosomal accumulation on the start codons are highly abundant in the fat bodies (Figure 3 – figure supplement 1C).
- On the other hand, DTTs suppressed in glial cells compared to neurons (defined as genes with more than 10 times higher TE in neurons than in glia, n = 161), we noticed that glial ribosome footprints were remarkably biased towards 5′ leaders (Figure 3A-B).
- Notably, this pattern was not obvious on the genome-wide scale (Figure 3A-B).
- The high 5′ leader/CDS ratio of ribosome footprints in glia was commonly observed on many transcripts with known neuronal functions, such as Rab3, Syt4, Arr1 and Syn (Figure 3D-E).
- Conversely, we observed accumulated ribosome footprints on the 5′ leaders of several glial marker genes specifically in neurons (Figure 3 – figure supplement 2).
- Altogether, these results suggest that the translation of 5’ leaders in selective mRNAs differentiates protein synthesis among cell types.biorxiv;2023.06.15.545207v4/FIG3F3fig3Figure 3.Ribosome stalling on the 5′ leaders of DTTs in glia.(A) Ribosome distribution (estimated P-sites) on the 161 DTTs a
- These DTTs are defined as transcripts showing more than 10 times higher TE in neurons compared to glia.
- All the transcripts showing TPM > 1 in RNA-seq both in neurons and glia are considered (7,933 genes in total), and the height is normalized by the total reads on this region.
- (B) Ratio of ribosome density on 5′ leader (TPM) to CDS (TPM) of the 161 DTTs or of all transcripts in neurons (green) or in glia (blue).
- ***: P < 0.001, Mann-Whitney test of ranks.
- Note that Syn-RD harbors a stop codon in the CDS but a fraction of ribosomes skip it, generating two annotated ORFs (CDS1 and CDS2) (Klagges et al., 1996).
- (D) Ratio of ribosome density on 5′ leader to CDS (mean ± standard error of mean of the biological replicates).
- (E) Ratio of ribosome density on 5′ leader to CDS on transcripts in the indicated GO terms in glia.
- *: P < 0.05, ***: P < 0.001, Dunn’s multiple comparisons test compared to the “all” group.We reasoned translational downregulation via upstream open reading frames (uORFs) in the 5′ leaders in glia, as the translation of uORFs was reported to suppress that of the downstream main ORF (Ferreira et al.
- Consistent with this idea, metagene plot around the AUG codons on 5′ leaders revealed strong accumulation of footprints on the upstream AUG codons, similar to those observed on the initiation codon of CDSs (Figures 4A-B).
- We calculated the footprint accumulation score on each codon (defined as the ratio of footprints on each codon with surrounding −50/+50 nt), and found that upstream AUG and the near cognate codons (NUG or AUN) showed relatively high accumulation (Figure 4C).
- On the other hand, inside the annotated CDS, none of the codons exhibited such significant accumulation (Figures 4D).
- Consistently, we found that transcripts related to neuronal functions typically contain long 5′ leaders and many upstream AUG (Figure 4 – figure supplement 1).
- We thus propose that glial cells suppress the translation of neuronal transcripts by stalling ribosomes on 5′ leader via uORF.biorxiv;2023.06.15.545207v4/FIG4F4fig4Figure 4.Footprint accumulation on upstream AUG in glia.(A) Meta-genome ribosome distribution (estimated P-sites of the 32-nt fragments)
- (B) Meta-genome ribosome distribution (estimated P-sites of the 32-nt fragments) around the annotated start codons in glia.
- (C) Footprint accumulation on 5′ leader in glia, defined as the number of ribosome footprints (estimated P-sites) on each codon normalized by the average on the surrounding (−50 to +50) regions.
- AU: arbitrary unit.uORFs in Rh1 confer translational suppression in gliaWe next asked if the 5′ leader sequences of neuronal genes cause cell-type differences in translation.
- To this end, we focused on Rh1 (Rhodopsin 1, also known as ninaE), which encodes an opsin, also detecting stimuli of other sensory modalities (Leung et al., 2020; O’Tousa et al., 1985; Shen et al., 2011; Zuker et al., 1985).
- Consistently, active translation of Rh1 was almost exclusively observed in neurons (Figure 5A).
- Similar to other neuronal genes shown in Figure 3C, the distribution of ribosome footprints was distinct among neuronal and glial cells: they were heavily biased to 5′ leader in glia, with the striking accumulation on the putative uORFs composed only of the start and stop codons (Figure 5B-C).biorxi
- (B) Ribosome distribution (estimated P-sites) on Rh1-RA in neurons (green) and in glia (blue), with 0 on the x-axis indicating the start codon of the CDS.
- 6-base upstream ORFs, consisting of consecutive start (or the near-cognate) and stop codons, are highlighted.
- (C) Ratio of ribosome density on 5′ leader (TPM) to CDS (TPM) in neurons (green) or in glia (blue).
- (D) Schematics of the control (UASz-GFP) or the Rh1 (UASz-Rh1-Venus) reporter.
- For the Rh1 reporter, 5′ leader and 3′ UTR sequences of Rh1-RA are fused to CDS of the Venus fluorescent protein.
- For the control reporter, synthetic 5′ leader sequences (syn21) and viral p10 terminator are fused to GFP (DeLuca and Spradling, 2018).
- Note that both reporters contain the same promoter (UASz) (DeLuca and Spradling, 2018) and are inserted onto the identical genomic locus (attP40).
- (E) Expression of the Rh1- or the control reporters driven by Tubulin-GAL4.
- **: P < 0.01, Mann-Whitney test of ranks.
- (G) Schematics of the mutated Rh1 reporter (m-Rh1).
- (H) The expression of the Rh1- or m-Rh1- reporters, driven by the nSyb- or the repo- GAL4.
- N = 8 (nSub > Rh1), 8 (nSyb > m-Rh1), 16 (repo > Rh1), 13 (repo > m-Rh1).
- ns: P > 0.05, *: P < 0.05, Mann-Whitney test of ranks.To address the function of these sequences on differential traslation, we constructed a transgenic reporter strain using the Rh1 UTR sequences under the control of UAS (Figure 5D), and directed gene expression ubiquitously using Tub-GAL4.
- While the reporter mRNA was detected both in neuronal and glial cells, the protein levels were much more heterogeneous and strikingly weak in glia (Figure 5E; Figure 5 – figure supplement 1A).
- The control reporter strain (DeLuca and Spradling, 2018), on the other hand, exhibited more ubiquitous expression, with significantly higher fluorescent intensity in glia (Figure 5E-F).
- Driving the reporter expression using the nSyb- or repo-GAL4 further corroborated cell-type specific suppression in glia (Figure 5 – figure supplement 1B-C).
- Strikingly, when the 6-base putative uORFs were mutated, the in-vivo protein-to-mRNA ratio of the reporter was significantly increased in glia but not in neurons (Figure 5G-H).

## Tables

### 

## Figure Descriptions

### Figure 1.
Comparative transcriptome-translatome analyses in the Drosophila head.(A) Schematics. Fly head lysate is digested with RNase I for Ribo-seq, while not for RNA-seq. Resultant short fragments or the whole mRNA are reverse-transcribed and sequenced. (B) Meta-genome ribosome distribution (estimated P-si

### Figure 2.
Cell-type specific Ribo-seq and RNA-seq reveal differential translational regulations.(A) Schematics. FLAG-tagged ribosome protein L3 (RpL3::FLAG) is expressed in neurons (nSyb-GAL4) or in glial cells (repo-GAL4). RNA-seq and Ribo-seq are performed following immunoprecipitation. Whole brain images o

### Figure 3.
Ribosome stalling on the 5′ leaders of DTTs in glia.(A) Ribosome distribution (estimated P-sites) on the 161 DTTs around the start codons (solid lines; start +/- 50 nt). These DTTs are defined as transcripts showing more than 10 times higher TE in neurons compared to glia. The dotted lines in the bo

### Figure 4.
Footprint accumulation on upstream AUG in glia.(A) Meta-genome ribosome distribution (estimated P-sites of the 32-nt fragments) around the upstream AUG codons in glia. (B) Meta-genome ribosome distribution (estimated P-sites of the 32-nt fragments) around the annotated start codons in glia. (C) Foot

### Figure 5.
The transgenic Rh1-Venus reporter reveals differential translation in neuronal and glial cells.(A) Reads on CDS of Rh1-RA in Ribo-seq. (B) Ribosome distribution (estimated P-sites) on Rh1-RA in neurons (green) and in glia (blue), with 0 on the x-axis indicating the start codon of the CDS. 6-base ups

## References
Total references in published paper: 76

### Key References (from published paper)
- Dynamics of ribosome scanning and recycling revealed by translation complex profiling (, 2016)
- Quantifying post-transcriptional regulation in the development of Drosophila melanogaster (, 2018)
- Selective 40S Footprinting Reveals Cap-Tethered Ribosome Scanning in Human Cells (, 2020)
- The developmental proteome of Drosophila melanogaster (, 2017)
- Widespread posttranscriptional regulation of cotransmission (, 2023)
- . fastp: an ultra-fast all-in-one FASTQ preprocessor (, 2018)
- Development of a tissue-specific ribosome profiling approach in Drosophila enables genome-wide evalu (, 2017)
- Multiple repressive mechanisms in the hippocampus during memory formation (, 2015)
- Cellular diversity in the Drosophila midbrain revealed by single-cell transcriptomics (, 2018)
- A Single-Cell Transcriptome Atlas of the Aging Drosophila Brain (, 2018)
- Efficient Expression of Genes in the Drosophila Germline Using a UAS Promoter Free of Interference b (, 2018)
- DAVID: Database for Annotation, Visualization, and Integrated Discovery (, 2003)
- STAR: ultrafast universal RNA-seq aligner (, 2013)
- Tissue-specific transcriptome profiling of Drosophila reveals roles for GATA transcription factors i (, 2018)
- Ribosome profiling reveals pervasive and regulated stop codon readthrough in Drosophila melanogaster (, 2013)
- Tuning gene expression with synthetic upstream open reading frames (, 2013)
- Memory in mice as affected by intracerebral puromycin (, 1963)
- Pervasive translational regulation of the cell signalling circuitry underlies mammalian development (, 2017)
- The translatome of neuronal cell bodies, dendrites, and axons (, 2021)
- Revealing Global Regulatory Perturbations across Human Cancers (, 2009)
- An Integrated Stress Response Regulates Amino Acid Metabolism and Resistance to Oxidative Stress (, 2003)
- A critical period of translational control during brain development at codon resolution (, 2022)
- Morphological diversity and development of glia in Drosophila (, 2011)
- A Translational Profiling Approach for the Molecular Characterization of CNS Cell Types (, 2008)
- Glial cells missing: A binary switch between neuronal and glial determination in drosophila (, 1995)
- RiboTag translatomic profiling of Drosophila oenocytes under aging and induced oxidative stress (, 2019)
- Tissue-specific dynamic codon redefinition in Drosophila (, 2021)
- Genome-wide analysis in vivo of translation with nucleotide resolution using ribosome profiling (, 2009)
- Ribosome Profiling of Mouse Embryonic Stem Cells Reveals the Complexity and Dynamics of Mammalian Pr (, 2011)
- Systematic Analysis of Neural Projections Reveals Clonal Composition of the Drosophila Brain (, 2013)

## Ground Truth Reference
- Figures: 5
- Tables: 1
- References: 76