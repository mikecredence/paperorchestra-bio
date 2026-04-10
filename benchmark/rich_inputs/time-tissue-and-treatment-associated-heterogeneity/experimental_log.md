# Experimental Log: Time-, tissue- and treatment-associated heterogeneity in tumour-residing migratory DCs

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsmRegDC signatures are associated with improved survival in human cancersThe presence of mature LAMP+ DCs within lymphoid follicles has been associated with improved prognosis in NSCLC12, but the effect of tumour mRegDCs on prognosis in human cancers more broadly has not been examined.
- To address this, we analysed the transcriptomes of 4,045 human solid tumours from the cancer genome atlas (TCGA)23.
- 1A), all of which harbour CCR7+ mRegDCs (Extended Data Fig.
- Further analysis of 1,853 human breast tumours from METABRIC27 revealed cancer subtype-specific associations with survival (Extended Data Fig.
- These data suggest that mRegDCs contribute to anti-tumour responses across a range of human cancers.biorxiv;2023.07.03.547454v2/FIGS1F7figs1Extended Data Figure 1mRegDCs in human cancer.(A) Kaplan-Meier analysis of overall survival rate in skin cutaneous melanoma (SKCM, n = 473), colorectal adenocar
- Log-rank test was used.mRegDCs are transcriptionally heterogenous, and some remain within the tumour despite CCR7 expressionTo investigate the mechanisms by which mRegDCs promote anti-tumour immunity, we sought to characterise their spatio-temporal dynamics.
- The mRegDC programme is thought to be driven by acquisition of tumour antigen5, and we asked whether establishment of this programme inevitably leads to the trafficking of CCR7+ mRegDCs to the dLN, or whether some cells remain in the tumour.
- To address this, we established multiple syngeneic subcutaneous colorectal tumours (MC38, MC38-Ova, CT26) in a photoconvertible Kaede transgenic model that enables site-specific temporal labelling of cells within the tumour28.
- Tumours were transcutaneously photoconverted on day 13, converting all infiltrated cells in the tumour only from the default green fluorescence (Kaede-green) to a red fluorescent profile (Kaede-red)19.
- 24-72h following photoconversion, tumours were harvested, enabling the distinction of newly-infiltrating Kaede-green cells and Kaede-red cells retained in the tumour from the point of photo-labelling (Fig.
- To address the effect of ICB on mRegDCs, we administered anti-PD-L1 antibodies in this model (Extended Data Fig.
- 2A), selecting this target because mRegDCs in CRC showed the highest expression of PD-L1 among immune cells (Extended Data Fig.
- 1C).biorxiv;2023.07.03.547454v2/FIGS2F8figs2Extended Data Figure 2Single cell profiling of mouse subcutaneous tumours.(A) Tumour growth curves comparing anti-PD-L1 antibody-treated versus isotype control antibody treatment, administered on day 7, 10 and 13 in MC38-Ova tumours.
- 1) and includes 5 mice per condition.(B) Fluorescence-activated cell sorting (FACS) strategy for isolation of tumour immune cells for scRNA-seq.
- CD45+ cells were only sorted to CD11b+ or CD11b-/low fractions to ensure appropriate representation of various cell types in the scRNA-seq data, but both fractions were combined for scRNA-seq analysis and annotated based on their transcriptome.(C) Canonical marker gene expression in myeloid cell sub
- 1B.(D) Gene signature scores of publis hed transcriptomic signatures in DC clusters from Fig.
- Monocyte-derived DCs (moDC) signatures scored highly in cDC2 clusters, consistent with known challenges in distinction of cDC2 and moDC7.(E) Flow cytometry of surface PD-L1 expression in MC38-Ova tumours.(F) Representative flow cytometry gating strategy for tumour and LN DCs.
- mRegDCs were identified as Live, CD45+ lineage- (CD3, NK1.1, B220, Ly6G, F4/80) CD11c+MHC-II+ PD- L2+CCR7+ cells; (PD-L2 expression was more restricted to mRegDCs than PD-L1.) Where Kaede transgenic mice were used, Kaede+ cells were gated.(G) Flow cytometry of DC composition in MC38-Ova tumours.
- Points represent independent mice.(H) Kaede fluorescence by DC cluster in the scRNA-seq data.(I) Flow cytometry of Kaede fluorescence in DCs from MC38 and CT26 tumours; photoconversion time course.
- Paired t-test with FDR correction was used (G,H).(J) Representative microscopy of MC38 tumours 72h after tumour photoconversion.
- Insets highlight selected regions with Kaede-red CCR7+MHC-II+ DCs.(K-L) Zoomed-in representative microscopy of MC38 (K) and CT26 (L) tumours 72h after tumour photoconversion.
- Scale bar, 30μm; arrows, tumour-residing mRegDCs.biorxiv;2023.07.03.547454v2/FIG1F1fig1Figure 1Landscape and temporal dynamics of DCs in murine subcutaneous tumours.(A) Experiment design.
- Tumours from Kaede transgenic mice were harvested 5h, 24h, 48h, or 72h after photoconversion.(B) UMAP of myeloid cells from scRNA-seq of FACS-sorted CD45+TER119- Kaede- green+/Kaede-red+ cells 48h after photoconversion of subcutaneous MC38-Ova tumours.(C) UMAP of DCs from (B), and canonical marker g
- Data is representative of 3 independent experiments (12 independent mice).(G) Flow cytometry of Kaede fluorescence in DCs from MC38-Ova tumours.
- Paired t-test with FDR correction was used.(H) Representative confocal microscopy images of MC38 tumours 72h after photoconversion.
- Scale bar, 40μm; arrows, tumour-residing mRegDCs (Kaede- red+CCR7+MHC-II+, dendritic morphology).(I) Tumour DCs ordered by pseudotime, rooted in the cluster with highest proportion of Kaede-green DCs; and proposed pseudotime trajectory.(J) RNA velocity trajectory in tumour DCs.(K) Expression of Axl.
- 2B) generated 80,556 single cell transcriptomes, following rigorous quality control, including 32,191 myeloid cells (Fig.
- Unbiased clustering of DCs revealed 8 distinct clusters, including cycling DCs, cDC1, cDC2s, and mRegDCs, assigned based on expression of canonical marker genes and similarity to published transcriptomes (Fig.
- 2D), with mRegDC showing high expression of Ccr7, Cd274 and Pdcd1lg2.
- Indeed, mRegDCs expressed higher levels of surface PD-L1 than other immune cells (Extended Data Fig.
- 2E).CCR7+PD-L2+ mRegDC were a prominent tumour DC population (Fig.
- 1C), and this was confirmed by flow cytometry (Extended Data Fig.
- Surprisingly, tumour mRegDCs were predominantly Kaede-red indicating that they have resided in the tumour for over 48h (Fig.
- In contrast, cDC1 and cDC2 were mostly Kaede-green, consistent with the conclusion that these newly infiltrating cDCs differentiate into mRegDCs following uptake of tumour antigen5.
- The prevalence of tumour-retained Kaede-red mRegDCs was validated over a time-course in all tumour models, by flow cytometry, where CCR7+PD-L2+ mRegDCs were the major Kaede-red DC cell-type up to 72h post-photoconversion (Fig.
- Using immunofluorescence (IF) microscopy, we confirmed the presence of Kaede-red MHC-II+CCR7+ cells (Fig.
- 2J-L).To explore the relationship between tumour DC subsets, we performed pseudotime analysis rooted in the Kaede-green dominant cluster (cDC2_1).
- This revealed a trajectory terminating in mRegDC_2/3 that transitioned through an intermediate mRegDC_1 state (Fig.
- 3A), consistent with the Kaede-green/red ratio of clusters that marks tumour dwell in real-time.
- RNA velocity analysis confirmed the cell-state transition from cDC, through mRegDC_1, to mRegDC_2 or mRegDC_3, which were the endpoints of the velocity trajectory (Fig 1J, Extended Data Fig.
- 3B).biorxiv;2023.07.03.547454v2/FIGS3F9figs3Extended Data Figure 3Maturation trajectory in tumour DCs.(A) Partition-based graph abstraction (PAGA) of scRNA-seq of tumour DCs.(B) Terminal states (end points) of RNA velocity analysis.(C) Flow cytometry of mRegDC to cDC ratio in Kaede-green DCs; time c
- MC38 and CT26 tumours were used; points represent independent mice; one-way ANOVA with Šidák’s multiple comparisons test was used.(D) Flow cytometry of surface cDC1 (XCR1+) and cDC2 (CD11b+) marker expression on mRegDCs from MC38-Ova tumours.
- Paired t-test with FDR correction was used.(E) Expression of selected DC migration genes and Ciita in scRNA-seq data of cDC1 and cDC2.
- Arrows indicate relative expression in Kaede-red versus Kaede-green cells; Wilcoxon rank-sum test was used.(F) Principal component (PC) analysis of scRNA-seq of cDC2s, pseudo-bulked to 3 artificial replicates per condition.
- PC1; variance due to Kaede profile.
- PC2; variance due to treatment.
- (G-H) Gene ontology (GO) term enrichment test for the top 100 loading genes of PC1 (G) and PC2 (H).
- Fisher-exact test was used.(I) Differential gene expression between cDC2_2 and cDC2_3.
- Selected DEGs relating to DC maturation, antigen presentation, MHC-II and migration are highlighted in red (all P-adj < 0.01).(J) Expression of Axl in cDC2_2 and cDC2_3 combined.To further prove that tumour mRegDC arise from cDC precursors, we examined Kaede-green DCs 5h post-photoconversion, which 
- Indeed, at 5h post-photoconversion the Kaede-green mRegDC:cDC ratio was only 1/100, but this increased to 1/5 72h post-photoconversion (Extended Data Fig.
- cDC1 or cDC2-defining transcripts were not conserved upon acquisition of the mRegDC programme, for example, Clec9a or Clec10a expression was lost but Irf8 and Batf3 are upregulated ubiquitously (Fig 1D).
- However, retained cDC subset-specific surface marker expression indicated a mixed ontogeny of mRegDCs, with expression of XCR1 (cDC1 origin) and CD11b (cDC2 origin) detectable, and notably, XCR1+ mRegDCs were higher among the Kaede-red fraction (Extended Data Fig.
- These data support the conclusion that both cDC1 and cDC2 maturate to tumour-residing mRegDCs.Kaede-red+ cDC1 and cDC2 showed higher expression of migratory transcripts and Ciita, a master regulator of antigen presentation29, than Kaede-green+ counterparts, suggesting that cDCs mature with duration 
- Principal component (PC) analysis showed that Kaede status (green/red) accounted for most of the transcriptional variance in cDC2s (PC1, Extended Data Fig.
- Genes driving PC1 were enriched in pathways relating to antigen presentation and myeloid differentiation (Extended Data Fig.
- cDC2_3, the most mature cluster in the cDC2-to-mRegDC trajectory, upregulated Ciita, class-II MHC (MHC-II) transcripts, and Ccr7 (Extended Data Fig.
- The receptor tyrosine kinase Axl, which recognises apoptotic cells and induces the mRegDC programme5, was also upregulated as cDC2_1 transitioned to cDC2_3 (Figure 1K).
- Altogether, these data suggest time-associated maturation of cDCs in the TME towards an mRegDC state, and importantly, antigen-charged mRegDCs may reside in the tumour for several days despite the expression of genes involved in tumour egress, including CCR7.Migrated mRegDCs are phenotypically disti
- Kaede-red CCR7+PD-L2+ DCs, which were photo-labelled within the tumour and hence tumour emigrants, were readily detectable in the dLN, but not in the contralateral non-draining LN (ndLN, Fig.
- Indeed, among Kaede-red DCs in the dLN, essentially all were mRegDC, up to 72h post-photoconversion (Fig.
- scRNA-seq of Kaede-red CD45+ cells in tumour-dLNs (integrated with CD45+ cells from control LNs) included a prominent Ccr7+Cd274+ mRegDC cluster among myeloid cells (Fig.
- In this data, 94% of Kaede-red+ myeloid cells in the dLN were mRegDCs (Fig.
- Hence, mRegDC are the dominant myeloid cell tumour emigrants arriving in the dLN.biorxiv;2023.07.03.547454v2/FIGS4F10figs4Extended Data Figure 4Comparison of tumour-residing mRegDCs versus LN mRegDC emigrants.(A) Expression of mRegDC or myeloid cell canonical marker genes in scRNA-seq of LN myeloid 
- 2D).(B) Expression of selected genes in tumour DCs (isotype control-treated) and Kaede-red DC emigrants in tumour-dLNs.(C) GSEA of “GO:biological process (BP) lymphocyte co-stimulation (GO:0031294)”, comparing Kaede-red mRegDCs from the dLN versus tumour mRegDCs.(D) UMAP of myeloid cells from scRNA-
- Wilcoxon rank-sum test was used.(G) Expression of selected DEGs between in tumour and dLN mRegDCs from (D), indicated within the box.(H-I) Expression of CCR7 in DCs from MC38-Ova tumours in the scRNA-seq data (H) and by flow cytometry (I).
- Paired t-test with FDR correction was used (I).(J) Gene signature enrichment of pathways relating to DC movement and CCR7 signalling.biorxiv;2023.07.03.547454v2/FIG2F2fig2Figure 2mRegDCs that migrate to the dLN become phenotypically and transcriptionally distinct from tumour-residing populations.(A)
- MC38-Ova tumours were used (A- C); points represent independent mice; paired t-test with FDR correction was used (B-C).(D-E) UMAP of myeloid cells from scRNA-seq of FACS-sorted CD45+ Kaede-red cells from tumour-dLNs (MC38-Ova) and CD45+ cells from control LNs.(F) GSEA of Kaede-red mRegDCs in dLNs ve
- Signed P-adj indicate log10(adjusted P-value) with the direction of enrichment.(G) Expression of selected genes in tumour mRegDCs and Kaede-red mRegDCs in dLNs (isotype control-treated).
- Wilcoxon rank-sum test was used.(H) Flow cytometry of CD80/86 on mRegDCs from MC38-Ova tumours or dLNs 48h after photoconversion, with representative histograms.
- Specifically, CD80 and CD86 were higher in tumour- residing mRegDCs, confirmed at a protein level, while Icosl was significantly higher in migrated mRegDCs in the dLN (Fig.
- Of note, CD80/86 and ICOSL have differing effects on T cell activation, where signalling through CD28 but not ICOS induces IL-2 production to support the clonal expansion of T cells31.
- Il12b, which drives anti-tumour cytotoxic T cell activity32, was enriched in tumour mRegDCs, while Il15ra, associated with DC maturation33, was higher in mRegDC in the dLN.
- Notably, scRNA-seq of B16-F10 tumours and their dLNs34 demonstrated the same tissue-associated heterogeneity in mRegDCs (Extended Data Fig.
- 4D-G).We next asked whether the three transcriptionally distinct tumour mRegDC states contributed equally to the dLN emigrants.
- Strikingly, over 80% of Kaede- red DCs from the dLN mapped to the tumour mRegDC_1 cluster (Fig.
- Only 9% of DCs in the dLN resembled mRegDC_2/3, despite mRegDC_2/3 being the dominant Kaede-red+ tumour mRegDC states.
- Although CCR7 expression remained high in both tumour-residing or migrated mRegDCs, we observed a decrease in transcripts associated with DC chemotaxis and CCR7 signalling in mRegDC_2 and 3 (Extended Data Fig.
- Moreover, CD80 and CD86 expression was upregulated on Kaede- red versus Kaede-green tumour mRegDCs, with expression levels on tumour Kaede-green mRegDCs similar to migrated mRegDCs in matched dLNs (Fig 2H).
- Altogether, these data suggest that mRegDC_1, which have most recently acquired the mRegDC programme, are the main population to seed the dLN.
- Hence, we propose that mRegDC_2 and mRegDC_3 are terminal, tumour-residing mRegDC states, and DCs that have transitioned beyond the intermediate mRegDC_1 state become increasingly unlikely to egress.Tumour-retained mRegDCs progress towards an “exhausted”-like state but is attenuated by anti-PD-L1 tr
- During the progression from mRegDC_1 to mRegDC_3, there was a decrease in MHC-II expression, including class-II invariant chain Cd74 (Fig.
- Concomitantly, DC antigen presentation genes decreased as cells transitioned towards the tumour-retained mRegDC_2/3 states (Fig.
- This included downregulation of molecules involved in antigen processing (Ctsb, Ctsl, Ifi30, Lgmn, Psme2), transport (Tap1, Tap2), chaperones (Hsp1a1, Hspa2, Hspa8), MHC loading (H2-DMa, H2-Oa, Tapbp, Calr) and Ciita (Extended Data Fig.
- 5B-C).biorxiv;2023.07.03.547454v2/FIGS5F11figs5Extended Data Figure 5Transcriptional changes in mRegDCs with prolonged tumour residence.(A) Dot plot of class-I and class-II MHC gene expression (log-transformed, unscaled) in mRegDCs.(B) Differential gene expression between mRegDC_1 and mRegDC_3.
- Significant DEGs from “KEGG antigen processing and presentation” are highlighted in red (P-adj < 0.01).(C) Expression of Ciita.(D) Differential gene expression between mRegDC_1 and mRegDC_3.
- Significant DEGs from “GO: molecular function (MF) cytokine activity (GO:0005125)” are highlighted in red (P-adj < 0.01).(E) Tcf7 expression and regulon activity score.biorxiv;2023.07.03.547454v2/FIG3F3fig3Figure 3Tumour-residing mRegDCs undertake an “exhausted” state with duration in the tumour, at
- (B) Gene signature scores for “GO:BP dendritic cell antigen processing and presentation (GO:0002468)” across mRegDC clusters.
- (C) Gene signature scores (scaled) of individual cells for “GO:BP dendritic cell antigen processing and presentation (GO:0002468)” and mRegDC signature genes, coloured by pseudotime.
- (D) GSEA of mRegDC_3 versus mRegDC_1.
- Only significant pathways (P-adj < 0.05) shown.
- (E) Differential gene expression between mRegDC_1 and mRegDC_3.
- Significant DEGs from “Hallmark inflammatory response” are highlighted in red (P-adj < 0.01).
- Differentially abundant neighbourhoods at FDR < 0.05 are coloured.
- ‘Mixed’ refers to neighbourhoods where cells do not predominantly (>70%) belong to a single cluster.
- (G) Differential gene expression between mRegDC_2 and mRegDC_3.
- DEGs (P-adj < 0.01, log2Fold- change > 0.5) are coloured.
- (H) Flow cytometry of OX40L expression on mRegDC from MC38-Ova tumours and their dLN.
- Paired t- test was used.Moreover, genes involved in innate immune function and response to inflammatory stimuli, including ‘interferon gamma/alpha response’, ‘inflammatory response’, ‘cytokine-cytokine receptor interaction’ and ‘Toll-like receptor signalling’ pathways, significantly decreased as cel
- Specifically, mRegDC_3 showed reduced expression of several innate immune response genes (Nlrp3, Tlr1, Cd14), genes involved in DC activation and migration (Axl, Ccr7, Rgs1, Icam1), lymphocyte co-stimulation (Cd40, Tnfsf9, Pvr) and cytokines which may recruit and activate immune cells (Cxcl9, Il1b, 
- To identify transcription factors (TF) that accompany the tumour-retained mRegDC state, we performed TF regulon analysis, which revealed that Tcf7 expression and its activity were upregulated in terminal mRegDC states (Extended Data Fig.
- Altogether, these data suggest that mRegDCs retained in the tumour undergo a transition, acquiring the transcriptional hallmarks of “exhaustion”, as defined in T cells20, namely reduced expression of molecules enabling effector function (e.g.
- antigen presentation), sustained expression of inhibitory molecules (such as PD-L1/L2), and a transcriptional state distinct from that of functional effector cells (i.e.
- successful dLN emigrants).Next, we considered the effects of anti-PD-L1 treatment on tumour DCs, since PD-L1 expression by DCs is essential for effective responses to anti-PD-L1 antibodies16,17.
- In cDC2s from anti-PD-L1- treated tumours, genes involved in inflammation and adaptive immunity were upregulated and expression of Axl increased (Extended Data Fig.
- Across all mRegDC states, differential gene expression following anti-PD-L1 drove enrichment of similar pathways, including “interferon gamma response”, necessary for effective response to ICB32, and “TNFα signalling via NFκB” (Extended Data Fig.
- 6A-B).biorxiv;2023.07.03.547454v2/FIGS6F12figs6Extended Data Figure 6mRegDC activation following anti-PD-L1 treatment.(A) GSEA of mRegDCs in anti-PD-L1-treated versus isotype control-treated tumours; Hallmark (HM) and KEGG pathways.
- Only significant pathways (P-adj < 0.05) are shown.(B) Dot plot of selected leading-edge genes from GSEA analysis of “Hallmark interferon gamma response”, “Hallmark inflammatory response”, and “KEGG antigen processing and presentation” pathways from (A).(C) RNA velocity trajectory in tumour mRegDCs 
- Wilcoxon rank-sum test was used.(F) Representative flow cytometry of surface OX40L expression (using OX40L+/Human-CD4 reporter mice) on DCs from MC38-Ova tumours and dLNs.
- Wild-type DC (non-reporter) were used for OX40L+ gating.(G) Quantification of (F).
- Points represent independent mice, paired t-test with FDR correction was used.We then asked whether anti-PD-L1 treatment influenced tumour mRegDC heterogeneity.
- Assessment of differential abundance showed significant enrichment within mRegDC_2 neighbourhoods following anti-PD-L1 treatment, but relative depletion of mRegDC_3 (Fig.
- 3F), consistent with kernel density embeddings (Fig 1E).
- RNA velocity analysis suggested that this was driven by a preferential transition from mRegDC_1 to mRegDC_2 in anti-PD-L1-treated tumours (Extended Data Fig.
- Strikingly, the transcriptome of mRegDC_2 was highly activated compared to mRegDC_3, with increased expression of many genes involved in immune signalling, including Cd40, Il1b, Tnf, Nfkbia, etc.
- This was reflected in the pathway enrichment analysis, which showed multiple genesets relating to immune activation enriched in mRegDC_2 (Extended Data Fig.
- 6D), potentially augmenting their capacity to promote anti-tumour responses.Importantly, we identified several lymphocyte activation ligands32,35,36 that were significantly upregulated on mRegDC_2 versus other tumour mRegDC states and dLN mRegDCs, such as Il12b, Tnfsf4, Tnfsf9, Cd70 and Pvr (Extende
- These molecules were also preferentially expressed on tumour-residing mRegDCs in B16-F10 tumours (Extended Data Fig.
- Using OX40LHu-CD4 (Tnfsf4)-reporter mice, we confirmed that some tumour mRegDCs express OX40L, but it was not expressed by tumour cDCs or mRegDCs in the dLN (Fig.
- The absence of OX40L expression in the dLN suggests that it is only upregulated by tumour-retained CCR7+ DCs, and that OX40L+ mRegDC do not emigrate to the dLN, or at least rapidly downregulate it upon tumour exit.
- Altogether, these data underline that a subset of tumour-retained mRegDCs exhibit a specific, “activated” state, which is enriched following anti-PD-L1 treatment.mRegDCs interact with CD8+ T cells in human tumoursGiven that a substantial proportion of mRegDCs in the tumour failed to migrate to dLN, 
- We deconvolved 521 human CRC transcriptomes23 and found the highest correlation between mRegDC and CD8+ T cell transcripts (Fig.
- 4A), an observation replicated in melanoma, breast, and lung tumour biopsies (Fig.
- Furthermore, the CCR7+CD274+PDCD1LG2+ DC cluster (consistent with mRegDCs in human CRC26) (Extended Data Fig.
- 1B-C), had stronger predicted interactions with effector CD8+ T cells than other myeloid cells, including via CD28, CTLA-4 and PD-1 (PDCD1) engagement (Fig.
- 1D-G)24,25.biorxiv;2023.07.03.547454v2/FIG4F4fig4Figure 4mRegDCs interact with CD8+ T cells in human cancers.(A) Pearson correlation between cell proportions, from deconvolution of 521 bulk transcriptomes of colorectal adenocarcinoma biopsies (TCGA), and mRegDC signature genes.
- Box highlights high correlation between mRegDC and CD8+ T cells.
- Only significant correlations (p < 0.05) shown.
- (B) Pearson correlation between mRegDC signature genes and effector CD8+ T cell signature genes in colorectal cancer (COAD), breast cancer (BRCA), cutaneous melanoma (SKCM) and lung adenocarcinoma (LUAD) from TCGA.
- (C) CellPhoneDB cell-cell communication analysis between myeloid cells and effector CD8+ T cells in scRNA-seq of human CRC.
- Only significant interactions (p < 0.05) shown.
- (D-F) Spatial correlation (Pearson R-value) of mRegDC and effector CD8+ T cell signature scores in spatial transcriptomics (10X Genomics Visium) of independent human CRC tumour sections (D, n= 2), human melanoma section (E, n= 1), and independent human breast tumour sections (F, n= 2).
- (G) Expression of selected genes in myeloid-T cell doublets from PICseq of NSCLC tumours, grouped by the myeloid cell identity in each myeloid-T cell doublet.Effective engagement of cell-surface ligand-receptor pairs require co-localisation of mRegDCs and effector CD8+ T cells.
- Analysis of spatial transcriptomics data from human CRC tumours37 revealed hotspots with co-localised expression of mRegDC and effector CD8+ T cell genes (Fig.
- Spatial correlation of mRegDC and effector CD8+ T cell transcripts was also evident in human melanoma and breast tumours (Fig.
- 4E-F).biorxiv;2023.07.03.547454v2/FIGS7F13figs7Extended Data Figure 7mRegDC-CD8+ T cell engagement in human solid tumours.(A-B) Gene signature scores for mRegDCs and effector CD8+ T cells in spatial transcriptomics (10X Genomics Visium) of independent human CRC tumour sections associated with Fig.
- 4D (n= 2).(C) Sequencing of physically interacting cells (PICseq, myeloid-T cell doublets) from human NSCLC (n = 10 patients).
- Each dot represents one myeloid-T cell doublet.(D) Heatmap of frequency (values) of myeloid-T cell doublet combinations in PICseq of NSCLC.Finally, we analysed data from RNA-seq of physically-interacting cells (PICs), consisting of sorted myeloid-T cell doublets from NSCLC38.
- Of note, mRegDC-T cell PICs were more frequent in tumours than normal tissue38.
- We found that mRegDC-CD8+ T cell doublets were more frequent than other mRegDC-T cell combinations (Extended Data Fig.
- 7C-D), and PICs containing mRegDC (CCR7+FSCN1+CD274+) highly co-expressed CD8B, PRF1, GZMB and PDCD1 (Fig.
- 4G), confirming that in NSCLC, mRegDC and effector CD8+ T cells physically interact.
- Altogether, these data suggest that mRegDC-CD8+ T cell interaction is conserved across multiple human solid tumours.
- The prolonged tumour dwell-time of mRegDCs, which maintain high levels of PD-1 ligand expression, but downregulate expression of genes enabling effector function, suggests that these cellular interactions are potentially deleterious.
- Specifically, tumour-retained mRegDC may regulate the activation and expansion of anti-tumour cytotoxic T cells, but they could also be important targets of cancer immunotherapy.Anti-PD-L1 promotes immunogenic mRegDC-CD8+ T cell interactionsTo investigate the effects of anti-PD-L1 on mRegDC-CD8 T ce
- 8A-B), focussing on PD-1 (Pdcd1)-expressing CD8+ T cells which are the target of PD-L1–PD-1 checkpoint blockade.
- These include a major Prf1highGzmhighPdcd1+Havcr2+ cluster resembling “exhausted” T (TEX) cells and a Pdcd1+Tcf7+Slamf6+cluster resembling “stem-like” T cells39,40 (Fig.
- 8C-D), that were predominantly tumour-resident and expanded with anti-PD-L1 (Fig.
- Pdcd1+ cells were evident among the cycling_CD8T cluster (Extended Data Fig.
- 8F-G) and increased in proliferation following anti-PD-L1, potentially underpinning their increased number (Extended Data Fig.
- Of note, the TEX cluster showed the largest transcriptional response to anti-PD-L1 (Fig.
- 5C), including upregulation of genes involved in “TCR signalling” and “IL2-STAT5 signalling” with potential anti-tumour benefits (Extended Data Fig.
- Indeed, Kaede-red+PD-1+ CD8+ T cells showed a significant increase in Granzyme B and IFNγ protein expression following anti-PD-L1 treatment (Extended Data Fig.
- 8H,K-L).biorxiv;2023.07.03.547454v2/FIGS8F14figs8Extended Data Figure 8Single cell profiling of tumour CD8+ T cells following anti-PD- L1 treatment.(A) UMAP of TILs from scRNA-seq of FACS-sorted CD45+TER119- Kaede-green+/Kaede- red+ cells 48h after photoconversion of subcutaneous MC38-Ova tumours, a
- 5A.(D) Gene signature enrichment of published T cell exhaustion transcriptomic signatures in CD8+ T cell clusters.(E) Proportion of CD8+ T cells by Kaede fluorescence and treatment groups.(F) Regression of cell cycle genes from the cycling_CD8T cluster followed by re-integration, and label transfer.
- Majority of the cycling cluster embedded with the CD8+ TEX cell cluster.(G) Proportion of cycling CD8+ T cells belonging to each CD8+ T cell cluster, from (F).
- Chi- squared test for over-representation of TEX CD8+ T cells was used.(H) Representative flow cytometry of Ki-67+, GzmB+ and IFNγ+ expression in CD3+CD8+Kaede-red+PD-1+ TEX cells, following anti-PD-L1 treatment.(I) Flow cytometry of Kaede-red+PD-1+CD8+ T cells, showing increased frequency of cyclin
- Points represent independent mice, student’s t-test (I,K) or Mann-Whitney U test was used (L).biorxiv;2023.07.03.547454v2/FIG5F5fig5Figure 5anti-PD-L1 promotes activating mRegDC-cytotoxic CD8+ T cell interactions in the TME.(A) UMAP of scRNA-seq of CD8+ T cells, from FACS-sorted CD45+ Kaede-green/re
- DEGs calculated using Wilcoxon rank-sum test.(D) CellPhoneDB ligand-receptor analysis between tumour DCs and CD8+ TEX cells.
- Only significant interactions (p < 0.05) shown.(E) Representative confocal microscopy images of MC38 tumours, showing co-localisation of CCR7+MHC-II+ mRegDCs and CD3+CD8+4-1BB+Ki-67+ T cells.
- Scale bar, 20 μm.(F-K) In vitro and Ex vivo cultures.(F) Phenotype of BMDCs following culture with UV-irradiated MC38-Ova tumour cells.(G) Experiment set-up: DC-T cell co-culture.(H) Representative flow cytometry of OT-I activation and proliferation following co-culture with MC38-Ova-experienced mRe
- Values are plotted relative to cultures with isotype control antibodies and OX40L-expressing DCs (baseline), to facilitate comparisons across experiments.(J) Flow cytometry of mRegDCs from subcutaneously grown MC38-Ova tumours following 8h culture ex vivo with antibodies or recombinant IFNγ.(K) Flow
- Data is representative of two independent experiments, one-way ANOVA with Šidák’s multiple comparisons test was used (F-K).Given mRegDCs are a major source of PD-L1 in tumours, and the marked response of CD8+ TEX cells to anti-PD-L1 treatment, we sought to identify mRegDC-mediated interactions that 
- Cell-cell communication analysis showed several previously described interaction pairs, including Cxcl16 and Il15 from CCR7+ DCs, which may recruit and sustain cytotoxic T cells (Extended Data Fig.
- Importantly, we identified TNF-superfamily interactions, including TNFSF4–TNFRSF4 (OX40L–OX40), TNFSF9–TNFRSF9 (4-1BBL–4-1BB), CD70–CD27, and PVR-mediated interactions upregulated between mRegDC_2, which were enriched with anti-PD-L1 treatment, and CD8+ TEX cells (Fig 5D).
- These TNF-superfamily ligands are known to promote T cell survival, proliferation and activation35, and PVR engages the activating receptor CD226, or its competing inhibitory receptor TIGIT, to control CD8+ T cell effector function36.
- We observed similar predicted interactions between mRegDC_2 and other PD-1-expressing CD8+ T cells, including Tcf7+ stem-like cells (Extended Data Fig.
- Overall, mRegDC_3 had fewer predicted activating interactions with PD-1-expressing CD8+ T cells than mRegDC_1/2, supporting their status as an “exhausted” mRegDC state (Extended Data Fig.
- 9C), but all mRegDC states were a consistently high source of inhibitory PD-1 or CTLA-4 signals (Extended Data Fig.
- 9D).biorxiv;2023.07.03.547454v2/FIGS9F15figs9Extended Data Figure 9mRegDCs communicate with CD8+ T cells in murine tumours.(A) Expression of Cxcl16 and Il15.(B-D) CellPhoneDB cell-cell communication analysis between DCs and Pdcd1+ CD8+ T cells in scRNA-seq of MC38-Ova tumours.
- (B) Ligand-receptor predicted interactions between tumour DCs and activated or stem-like CD8+cells.
- (C) Interactions that are well-described in existing literature to influence CD8+ T cells function were identified and classified based on whether engagement of the cognate T cell receptor was activating (increase in effector function, proliferation, or survival) or inhibitory in nature.
- (D) PDCD1 or CTLA4-mediated inhibitory signals; edge width scaled to standardised interaction scores.
- Only significant interactions (p < 0.05) shown (B,D).(E) Representative confocal microscopy images of MC38 tumours, showing co-localisation of CCR7+MHC-II+ mRegDCs and CD3+CD8+ T cells (arrows).
- Scale bar, 80 μm.(F) Quantification of (E); spatial correlation (Pearson) between mRegDC and CD8+ T cell counts in 200 x 200 μm fields of MC38 tumour sections.
- 3 independent tumours were analysed.(G-H) Representative microscopy of independent MC38 tumours 48h after tumour photoconversion, showing interaction between Kaede-red CCR7+MHC-II+ mRegDCs and Kaede-red CD3+ T cells (arrows).
- Scale bar, 15 μm (G), 20 μm (H).(I) Representative microscopy of independent MC38 tumour, showing co-localisation of CCR7+MHC-II+ mRegDCs and CD3+CD8+4-1BB+Ki-67+ T cells.
- Scale bar, 15 μm.To visualise the cellular interactions predicted by our analysis, we used IF microscopy to confirm that mRegDCs and CD8+ T cells spatially co-localise (Extended Data Fig.
- There were frequent interactions between tumour-residing mRegDCs and Kaede-red+CD3+CD8+ T cells, often within a perivascular niche, including proliferating (Ki-67+)4-1BB+ cytotoxic cells (Fig.
- 9G-I), consistent with a role for mRegDCs in regulating anti-tumour cytolytic activity.To test the functional importance of these predicted mRegDC-CD8+ T cell interactions, we generated mRegDC-like cells from bone marrow-derived dendritic cells (BMDC) by culturing with apoptotic MC38-Ova cells, as p
- This led to a robust expression of mRegDC markers, including PD-L1, PD-L2 and CCR7 (Fig.
- Of note, the CCR7+PD- L2+ BMDCs (mReg-BMDC) generated by this system also expressed OX40L and PVR (Extended Data Fig.
- 10C), resembling the phenotype of tumour-retained mRegDC in vivo.biorxiv;2023.07.03.547454v2/FIGS10F16figs10Supplementary Figure 10In vitro DC OT-I CD8+ T cell co-culture.(A) Cell death following UV irradiation of MC38-Ova cell monolayer in vitro; for optimisation of tumour cell-line apoptosis.
- 30s UV exposure was chosen for subsequent experiments.
- (B) Representative flow cytometry of BMDC following 8h culture with UV-irradiated MC38-Ova cells.
- (C) Representative flow cytometry OX40L and PVR expression on BMDC.
- Culture with apoptotic MC38-Ova experienced FACS-sorted PD-L2+CCR7+ BMDC (mReg-BMDC), top left; positive control (BMDC + Ova + LPS), top right; negative controls, bottom left (no Ova antigen) and right (no DC).
- (E) Number of live CD8+ T cells in mReg-BMDC + OT-I co-culture set-up versus controls.
- (F) Representative flow cytometry of GzmB expression in OT-I cells; +/- anti-PD-L1 antibodies.
- (G) Flow cytometry of OT-I activation, and (H) CTV proliferation in OT-I cells and mean number of cell divisions, following culture with OX40L-expressing (+) or OX40L-deficient (-) mReg-BMDC.
- (I) Flow cytometry of mReg-BMDCs following 8h treatment with antibodies or recombinant IFNγ (before OT-I co-culture).
- (J) Flow cytometry of OT-I cells following co-culture with mReg-BMDC; DCs pre-treated with recombinant IFNγ (+) or PBS (-), OX40L-expressing (+) or OX40L-deficient (-) BMDCs.
- One-way ANOVA with Šidák’s multiple comparisons test was used (E-J).Co-culture of tumour-antigen (Ova)-experienced mReg-BMDC with naïve Ova-specific CD8+ T cells (OT-I) for 3 days (Fig.
- 5G) led to OT-I proliferation, which was not observed unless DCs were exposed to Ova (Extended Data Fig.
- Notably, the addition of anti-PD-L1 antibodies to the mReg- BMDC:OT-I co-culture resulted in an increase in activated (CD44+CD25+), clonally-expanded OT-I cells, and enhanced the production of granzyme B among activated cells (Fig.
- 10F).To assess the role of Tnfsf4 (OX40L), a ligand expressed by the activated mRegDC_2 state increased by anti-PD-L1 treatment, and enables interactions with CD8+ T cells via OX40 (Fig.
- 5D), we generated OX40L-deficient mReg-BMDC from CD11ccre Tnfsf4fl/fl mice.
- OT-I cells co-cultured with OX40L- deficient mReg-BMDC showed reduced activation and proliferation (Fig.
- 10G-H), suggesting that the OX40L:OX40 axis may be important for mRegDC function in vivo.Finally, we asked whether anti-PD-L1 treatment directly influences the tumour mRegDC state, or whether this is driven by DC-extrinsic factors.
- For example, immune checkpoint therapy increases interferon gamma (IFNγ) production by PD-1+CD8+ T cells that co-localise with mRegDCs in tumours (Extended Data Fig.
- 8K), which may activate tumour DCs32.
- Administration of anti-PD-L1 antibodies to isolated, tumour antigen-experienced BMDC in vitro did not alter their phenotype, but the addition of recombinant IFNγ upregulated expression of OX40L, PVR and CD40, consistent with the mRegDC_2 state (Extended Data Fig.
- This increased the activation and expansion of OT- I cells, but was reduced in cultures containing OX40L-deficient mReg-BMDC (Fig.
- Altogether, these data support the conclusion that tumour mRegDC states can be manipulated to promote antigen-specific CD8+ T cell responses.Conserved mRegDC heterogeneity and CD8+ T cell crosstalk in human cancersWe asked if the time, tissue, and treatment-associated heterogeneity in mRegDCs observ
- 1B), there was a gradient of MHC-II expression (Fig.
- Importantly, markers upregulated on tumour-residing MHC-IIlow mRegDCs in murine tumours were also preferentially expressed in the human MHC-IIlow mRegDCs, including IL15, PVR, TNFSF4, TNFSF9, and CD70.biorxiv;2023.07.03.547454v2/FIG6F6fig6Figure 6Conserved mRegDC heterogeneity and CD8+ T cell crosst
- Wilcoxon rank-sum test was used.(C) UMAP of myeloid cells from scRNA-seq of human metastatic urothelial carcinoma (mUC, HRA000212, n = 11 patients).(D) Cells associated with responders (complete responder, CR; partial responder, PR) or non- responders (stable disease, SD; progressive disease, PD) in
- Comparison between T cell clonotype expanders (responders, n = 9 patients) versus non-expanders (non-responders, n = 20 patients, EGAS00001004809).
- Wilcoxon rank-sum test was used.(G) PICseq (myeloid-T cell doublets) of human NSCLC; expression of mRegDC-T cell ligand-receptor pairs, grouped by myeloid cell identity in each myeloid-T cell doublet (GSE160903, n = 10 patients).(H) Gene signature scores for “GO:BP T cell mediated cytotoxicity (GO:0
- Wilcoxon rank-sum test was used.(I-J) Spatial correlation (Pearson R-value) of mRegDC signature scores and selected mRegDC-ligand receptors expressed by CD8+ T cells, in spatial transcriptomics (10X Genomics Visium) of independent human CRC tumour sections (n = 2).To assess tissue-associated differe
- Consistent with our findings, there was no difference in CCR7 expression, but CD80, CD86, TNFSF4, TNFSF9, CD70 and PVR were higher in tumour-residing mRegDCs versus dLN and normal tissue, while ICOSLG was enriched in the dLN (Fig.
- Therefore, the heterogeneity of mRegDCs in murine tumours are paralleled in human CRC.biorxiv;2023.07.03.547454v2/FIGS11F17figs11Extended Data Figure 11mRegDC heterogeneity and interaction with CD8+ T cells in human cancer.(A) UMAP of myeloid cells from scRNA-seq of human CRC (n = 63 patients) with 
- Molecules associated with tumour- residing mRegDCs in mice were also preferentially expressed in tumour mRegDCs in human CRC, but not the dLN.(F) Pearson correlation between mRegDC signature genes and effector CD8+ T cell signature genes in bulk RNA-seq of 208 mUC tumours treated with atezolizumab (
- Left, middle and right panel show all patients, clinical responders, and non-responders respectively.(G) UMAP of mRegDCs from human breast cancer (n = 29 patients).(H) GSEA of mRegDCs from T cell clonotype expanders (E, i.e.
- responders, n = 9 patients) versus non-expanders (NE, i.e.
- non-responders, n = 20 patients), in breast tumours treated with anti-PD-1.(I) Gene signature score for “Hallmark TNFa response via NFkB” in PICseq of NSCLC, grouped by the myeloid cell identity in each myeloid-T cell doublet.
- Atezolizumab (anti-PD-L1 antibody) is widely used in the treatment of metastatic urothelial carcinoma (mUC), but its efficacy is variable43.
- We analysed 208 bulk transcriptomes of tumour biopsies from the IMvigor210 trial for mUC44,45.
- In both responders and non- responders, mRegDC gene expression was positively correlated with effector CD8+ T cell transcripts, and was higher in responders (Extended Data Fig.
- To leverage the clinical response data from this cohort, we integrated the bulk transcriptomes with scRNA-seq of myeloid cells in mUC46 (Fig.
- 6C) using Scissor47, which enables identification of clinically relevant cell subpopulations and gene expression profiles.
- Indeed, myeloid cells associated with a favourable clinical response expressed transcripts associated with tumour-residing mRegDCs, including CCR7, CD274, IL15, PVR and CD70 (Fig.
- 6E).Moreover, in scRNA-seq of breast cancer (Extended Data Fig.
- 1D, 11G)24, mRegDCs from tumours that successfully underwent T cell clonotype expansion following treatment with anti-PD-1 antibodies were enriched in transcripts associated with our ICB-induced mRegDC_2 cluster, versus non- responders (Fig.
- Altogether, data from these treatment cohorts support the importance of an ICB-activated tumour-residing mRegDC state.Next, we asked if the molecular crosstalk between mRegDCs and CD8+ T cells in mice is conserved in humans.
- In PIC-seq data from NSCLC38, we found that doublets containing mRegDCs highly expressed ligands we identified in murine tumours (Fig.
- 5D), and their corresponding T cell receptors were highly expressed in the same mRegDC-T cell conjugates (Fig.
- Moreover, mRegDC-CD8+ T cell doublets were most enriched for T cell cytotoxicity genes and ‘TNFα response via NFκΒ’ compared to other myeloid-CD8+ T cell combinations (Fig.
- 11I-J).Finally, we re-examined hotspots of mRegDC and effector CD8+ T cell co-localisation in spatial transcriptomics of CRC, breast cancer and melanoma (Fig.
- Molecules involved in mRegDC- CD8+ T cell crosstalk were expressed in these voxels, with spatial correlation of mRegDC-CD8+ T cell ligand-receptor pairs in all 3 tumour types (Fig.
- Altogether, these data show that mRegDCs are critically positioned to regulate anti-tumour cytolytic activity, including via TNF-superfamily ligands such as OX40L, and PVR.biorxiv;2023.07.03.547454v2/FIGS12F18figs12Extended Data Figure 12Visium spatial transcriptomics of human cancer.(A) Expression 

## Figure Descriptions

### Extended Data Figure 1
mRegDCs in human cancer.(A) Kaplan-Meier analysis of overall survival rate in skin cutaneous melanoma (SKCM, n = 473), colorectal adenocarcinoma (COAD, n = 521), breast invasive carcinoma (BRCA, n = 1226), and lung adenocarcinoma (LUAD, n = 598) from TCGA, stratified by enrichment of mRegDC signatur

### Extended Data Figure 2
Single cell profiling of mouse subcutaneous tumours.(A) Tumour growth curves comparing anti-PD-L1 antibody-treated versus isotype control antibody treatment, administered on day 7, 10 and 13 in MC38-Ova tumours. Data shown is related to the scRNA-seq experiment (Fig. 1) and includes 5 mice per condi

### Figure 1
Landscape and temporal dynamics of DCs in murine subcutaneous tumours.(A) Experiment design. Tumours from Kaede transgenic mice were harvested 5h, 24h, 48h, or 72h after photoconversion.(B) UMAP of myeloid cells from scRNA-seq of FACS-sorted CD45+TER119- Kaede- green+/Kaede-red+ cells 48h after phot

### Extended Data Figure 3
Maturation trajectory in tumour DCs.(A) Partition-based graph abstraction (PAGA) of scRNA-seq of tumour DCs.(B) Terminal states (end points) of RNA velocity analysis.(C) Flow cytometry of mRegDC to cDC ratio in Kaede-green DCs; time course post- photoconversion. MC38 and CT26 tumours were used; poin

### Extended Data Figure 4
Comparison of tumour-residing mRegDCs versus LN mRegDC emigrants.(A) Expression of mRegDC or myeloid cell canonical marker genes in scRNA-seq of LN myeloid cells (Fig. 2D).(B) Expression of selected genes in tumour DCs (isotype control-treated) and Kaede-red DC emigrants in tumour-dLNs.(C) GSEA of “

### Figure 2
mRegDCs that migrate to the dLN become phenotypically and transcriptionally distinct from tumour-residing populations.(A) Representative flow cytometry of tumour-dLNs and contralateral ndLNs 48h after tumour photoconversion. DCs that originate from photo-flashed tumours carry the Kaede-red fluoresce

### Extended Data Figure 5
Transcriptional changes in mRegDCs with prolonged tumour residence.(A) Dot plot of class-I and class-II MHC gene expression (log-transformed, unscaled) in mRegDCs.(B) Differential gene expression between mRegDC_1 and mRegDC_3. Significant DEGs from “KEGG antigen processing and presentation” are high

### Figure 3
Tumour-residing mRegDCs undertake an “exhausted” state with duration in the tumour, attenuated in anti-PD-L1 treatment.(A) Expression of MHC-II transcripts and Cd74 over pseudotime in tumour DCs. Local regression (loess) was fit to scaled expression values. (B) Gene signature scores for “GO:BP dendr

### Extended Data Figure 6
mRegDC activation following anti-PD-L1 treatment.(A) GSEA of mRegDCs in anti-PD-L1-treated versus isotype control-treated tumours; Hallmark (HM) and KEGG pathways. Only significant pathways (P-adj < 0.05) are shown.(B) Dot plot of selected leading-edge genes from GSEA analysis of “Hallmark interfero

### Figure 4
mRegDCs interact with CD8+ T cells in human cancers.(A) Pearson correlation between cell proportions, from deconvolution of 521 bulk transcriptomes of colorectal adenocarcinoma biopsies (TCGA), and mRegDC signature genes. Box highlights high correlation between mRegDC and CD8+ T cells. Only signific

### Extended Data Figure 7
mRegDC-CD8+ T cell engagement in human solid tumours.(A-B) Gene signature scores for mRegDCs and effector CD8+ T cells in spatial transcriptomics (10X Genomics Visium) of independent human CRC tumour sections associated with Fig. 4D (n= 2).(C) Sequencing of physically interacting cells (PICseq, myel

### Extended Data Figure 8
Single cell profiling of tumour CD8+ T cells following anti-PD- L1 treatment.(A) UMAP of TILs from scRNA-seq of FACS-sorted CD45+TER119- Kaede-green+/Kaede- red+ cells 48h after photoconversion of subcutaneous MC38-Ova tumours, and canonical marker gene expression (B).(C) Canonical marker gene expre

### Figure 5
anti-PD-L1 promotes activating mRegDC-cytotoxic CD8+ T cell interactions in the TME.(A) UMAP of scRNA-seq of CD8+ T cells, from FACS-sorted CD45+ Kaede-green/red TILs 48h after photoconversion of subcutaneous MC38-Ova tumours.(B) Proportions of CD8+ TEX cells by Kaede profile and treatment.(C) Numbe

### Extended Data Figure 9
mRegDCs communicate with CD8+ T cells in murine tumours.(A) Expression of Cxcl16 and Il15.(B-D) CellPhoneDB cell-cell communication analysis between DCs and Pdcd1+ CD8+ T cells in scRNA-seq of MC38-Ova tumours. (B) Ligand-receptor predicted interactions between tumour DCs and activated or stem-like 

### Supplementary Figure 10
In vitro DC OT-I CD8+ T cell co-culture.(A) Cell death following UV irradiation of MC38-Ova cell monolayer in vitro; for optimisation of tumour cell-line apoptosis. 30s UV exposure was chosen for subsequent experiments. (B) Representative flow cytometry of BMDC following 8h culture with UV-irradiate

### Figure 6
Conserved mRegDC heterogeneity and CD8+ T cell crosstalk in human cancer.(A) UMAP of scRNA-seq of mRegDCs from human CRC (GSE178341, n = 62 patients).(B) Expression of selected ligands in mRegDCs between tumour (T), normal adjacent tissue(N) and tumour-dLN from independent scRNA-seq data of human CR

### Extended Data Figure 11
mRegDC heterogeneity and interaction with CD8+ T cells in human cancer.(A) UMAP of myeloid cells from scRNA-seq of human CRC (n = 63 patients) with paired tumour (T), normal adjacent tissue (N) and dLN samples, and expression of mRegDC signature genes (B).(C) UMAP of mRegDCs subset from (A), coloure

### Extended Data Figure 12
Visium spatial transcriptomics of human cancer.(A) Expression of selected receptors expressed by CD8+ T cells which facilitate interactions with tumour- residing mRegDCs in spatial transcriptomics (10X Genomics Visium) of independent human CRC tumour sections (n= 2).(B-C) Spatial correlation (Pearso

## References
Total references in published paper: 77

### Key References (from published paper)
- Dendritic cells in cancer immunology and immunotherapy (, 2019)
- Critical Role for CD103(+)/CD141(+) Dendritic Cells Bearing CCR7 for Tumor Antigen Trafficking and P (, 2016)
- Rapid and coordinated switch in chemokine receptor expression during dendritic cell maturation (, 1998)
- The Role of Type 1 Conventional Dendritic Cells in Cancer Immunity (, 2018)
- A conserved dendritic-cell regulatory program limits antitumour immunity (, 2020)
- Human dendritic cells in cancer (, 2022)
- Broad and Largely Concordant Molecular Changes Characterize Tolerogenic and Immunogenic Dendritic Ce (, 2016)
- Expanding dendritic cell nomenclature in the single- cell era (, 2022)
- Tumor-infiltrating dendritic cell states are conserved across solid human cancers (, 2021)
- A pan-cancer single-cell transcriptional atlas of tumor infiltrating myeloid cells (, 2021)
- Single-Cell Transcriptomics of Human and Mouse Lung Cancers Reveals Conserved Myeloid Populations ac (, 2019)
- Dendritic cells in tumor-associated tertiary lymphoid structures signal a th1 cytotoxic immune conte (, 2014)
- Selective Accumulation of Mature DC-Lamp+ Dendritic Cells in Tumor Sites Is Associated with Efficien (, 2004)
- TIM-3 Regulates CD103+ Dendritic Cell Function and Response to Chemotherapy in Breast Cancer (, 2018)
- Long-term survival for patients with non-small-cell lung cancer with intratumoral lymphoid structure (, 2008)
- PD-L1 on dendritic cells attenuates T cell activation and regulates response to immune checkpoint bl (, 2020)
- PD-L1 expression by dendritic cells is a key regulator of T-cell immunity in cancer (, 2020)
- Landscape and Dynamics of Single Immune Cells in Hepatocellular Carcinoma (, 2019)
- In vivo labeling reveals continuous trafficking of TCF-1+ T cells between tumor and lymphoid tissue (, 2022)
- T cell exhaustion (, 2011)
- Profound coordinated alterations of intratumoral NK cell phenotype and function in lung carcinoma (, 2011)
- Rapid establishment of a tumor-retained state curtails the contribution of conventional NK cells to  (, 2023)
- A single-cell map of intratumoral changes during anti-PD1 treatment of patients with breast cancer (, 2021)
- Dysfunctional CD8 T Cells Form a Proliferative, Dynamically Regulated Compartment within Human Melan (, 2019)
- Spatially organized multicellular immune hubs in human colorectal cancer (, 2021)
- The genomic and transcriptomic architecture of 2,000 breast tumours reveals novel subgroups (, 2012)
- Monitoring cellular movement in vivo with photoconvertible fluorescence protein ‘Kaede’ transgenic m (, 2008)
- Activation of class II MHC genes requires both the X ☐ region and the class II transactivator (CIITA (, 1995)
- Deciphering the transcriptional network of the DC lineage (, 2012)
- Modulation of TCR-induced transcriptional profiles by ligation of CD28, ICOS, and CTLA-4 receptors (, 2002)

## Ground Truth Reference
- Figures: 18
- Tables: 0
- References: 77