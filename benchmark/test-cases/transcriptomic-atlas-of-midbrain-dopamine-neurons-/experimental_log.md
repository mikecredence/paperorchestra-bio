# Experimental Log: Transcriptomic atlas of midbrain dopamine neurons uncovers differential vulnerability in a Parkinsonism lesion model

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsSingle nuclei RNA sequencing of the ventral midbrainPerhaps partly because of the challenges in dissociating and isolating whole mDA neurons, previous studies have only analyzed a relatively small fraction of all mDA neurons from each dissected brain (Dougalis et al., 2012; Hook et al., 2018;
- To overcome this limitation, we used single nuclei RNA sequencing (snRNA-seq) for mice expressing nuclear mCherry under the control of the Slc6a3 (DAT, dopamine transporter) promoter (Figure 1A-C)(Hupe et al., 2014).
- Nuclei isolated by fluorescent sorting were sequenced using the 10X Genomics Chromium platform (10Xv3).
- Using this strategy, more than 20% of all mDA neurons were consistently collected and sequenced from each brain, an improvement of over 50X from our previous study (Tiklova et al., 2019).biorxiv;2023.06.05.543445v2/FIG1F1fig1Figure 1.Generation of a snRNAseq dataset from the mouse midbrainA) Schemat
- C) Immunohistochemical staining of the mouse ventral midbrain coronal section, showing the overlap of TH and mCherry, scalebar 100 μm.
- Accordingly, mice (n=6) were unilaterally injected with 6-hydroxydopamine (6-OHDA, 0.7μg or 1.5μg) into the medial forebrain bundle, which leads to partial cell death of mDA neurons on one hemisphere of the brain (Figure 1A).
- To avoid omitting low red fluorescent protein (RFP)-expressing nuclei from analysis, a relatively relaxed gating in fluorescently activated nuclear sorting (FANS) was used, resulting in an approximately equal number of mCherry+ and mCherry- nuclei from each sample per brain (Figure 1–figure suppleme
- After snRNAseq and quality control, 36,051 nuclei from the intact and 32,863 from the lesioned hemisphere were retained for bioinformatic analysis (see Methods, Figure 1 - figure supplement 2).Sequencing data were subjected to normalization, variance stabilization, and dimensional reduction and then
- Louvain clustering was adopted, dividing all nuclei into 26 clusters (Methods, Figure 1–figure supplement 3).
- A hierarchical clustering dendrogram illustrating the relationship between clusters was also constructed, and cluster-specific markers were identified and used to annotate previously known cell types (Figure 1D, E; Figure 1–figure supplement 3, Supplementary file 1).
- Neuronal clusters were mainly comprised of different types of glutamatergic (GLU), gamma-aminobutyric acid (GABA), and dopamine neurons (Figure 1–figure supplement 3).
- This dataset is accessible via our lab homepage: https://perlmannlab.org/resources/.Dopamine neuron diversityPlotting known markers for mDA neurons in the UMAP revealed that a substantial number of all analyzed nuclei, clusters 1, 4, 7, and 10, were derived from mDA neurons (Figure 1–figure suppleme
- To focus the analysis on dopamine neurons, 33,052 nuclei expressing above threshold levels of either Th or Slc6a3 (Th+/DAT+) were selected for further computational analysis.
- Most of these filtered nuclei, visualized in a de novo UMAP, were positive for several genes known to be expressed in mDA neurons (Figure 2A, B).
- Included in this analysis are neurons that have been described before expressing Th mRNA but no protein (Morales and Margolis, 2017).
- In addition, we detected some mCherry- cells that contained only Th mRNA (Figure 2-figure supplement 1).
- As our analysis was based on mRNA and not protein expression, these cells were also included in our dopaminergic subset.biorxiv;2023.06.05.543445v2/FIG2F2fig2Figure 2.Midbrain DA dataset, cell types and compositionA) UMAP projection of the dopaminergic dataset, with numerical labels of the 71 cluste
- B) Typical dopaminergic markers plotted in UMAP separately, with the top 1 percentile of the normalized gene expression range clipped for better visualization.
- mODC = mature oligodendrocyte, HyDA = hypothalamic dopaminergic.K-means clustering, followed by hierarchical clustering, was used to divide Th+/DAT+ nuclei into 71 unique clusters whose relationship was also visualized in a dendrogram (Figure 2C).
- A few clusters remained unassigned (Figure 2A, C, Supplementary file 2).
- Almost all clusters expressing genes required for synthesis and handling DA (dopaminergic) also expressed mDA neuron markers, including En1, Nr4a2, and Pitx3, the latter at a lower abundance, except the ones that expressed hypothalamic dopaminergic markers, including, Satb2, Prlr, and Gad1 (Figure 2
- The mDA neuron clusters form a major separate branch in the dendrogram, while HyDA neurons constitute a more distant branch (Figure 2C).
- Two closely related clusters (#12 and #26) form a distinctly separate group, predominantly (∼95%) composed of nuclei from the lesioned hemisphere.
- However, the expression of Th and other dopaminergic markers in these two lesion-specific clusters is relatively low (Figure 2C).
- This classification subdivided mDA neurons into 7 territories and 16 neighborhoods (Figure 3A, C; Figure 3–figure supplement 1).
- The territories were named according to selected distinguishing genes (Sox6, Gad2, Fbn2, Pcsk6, Pdia5, Ebf1, and Otx2) and can be identified by additional markers as indicated in Figure 3 (see also Figure 3–figure supplement 1).
- It should be noted that these markers were typically not unique for a particular territory but, in combination, defined gene signatures that distinguished territories from each other.biorxiv;2023.06.05.543445v2/FIG3F3fig3Figure 3.Dopaminergic territories and neighborhoodsA) UMAP projection of the do
- B) Co-expression of Sox6 and Calb1 plotted in UMAP, roughly delineating SNc and VTA respectively.
- Dotplot showing territory (TER) and neighborhood (NH) specific markers.The transcription factor Sox6 is known to be expressed in mDA neurons of the SNc and in some neurons of the VTA (Luppi et al., 2021; Panman et al., 2014; Poulin et al., 2014).
- The Sox6-territory included approximately one-third of all sequenced mDA neuron nuclei (Figure 3A).
- This territory expressed other previously defined SNc markers, including Kcnj6 (Girk2) (Figure 3–figure supplement 1) and additional genes representing a gene signature that included Col25a1 and Tigar, as well as Nwd2, Pex5l, Cdh11, and Serpine2 (Figure 3C; Figure 3–figure supplement 1).
- In contrast, expression of Calb1, encoding the known VTA marker Calbindin 1, was either absent or was expressed at low levels in Sox6-territory nuclei (Figure 3C).
- This almost non-intersecting, mutually exclusive expression of Sox6 and Calb1 defined a striking major division among all analyzed mDA neuron nuclei, following the neuroanatomical division of mDA neurons into SNc and VTA (Figure 3B).The remaining six territories consisting of approximately 15,000 mD
- Indeed, these territories expressed additional VTA markers, including Otx2 (Figure 3C).
- Expression of mDA neuron markers such as Th, Ddc, and Slc6a3 was particularly weak in the Gad2-territory, which displayed typical features of GABAergic neurons, including Gad2 and Slc32a1.Our next focus was to describe mDA neuron diversity within territories by dividing them into more highly resolve
- Four neighborhoods were defined within the Sox6-territory, two of which expressed high levels of Aldh1a1, a previously recognized marker for some SNc neurons (NH1 and NH4).
- Sox6+ neighborhoods were also distinguished by, Vcan and Col11a (NH1 and NH2), Anxa1 and Fam19a4 (NH1 and NH4), Grin2c, Ndnf and Vill (NH3 and NH4), and Aldh1a7 (NH4), among other markers.The other six territories were each divided into two neighborhoods (Figure 3C, Figure 3-figure supplement 1).
- Gad2_NH1 expressed Chrm2 and Zfp536, whereas Gad2_NH2 expressed Megf11, Zeb2, and Met.
- Fbn2_NH1 was specified by Rxfp1 and Hs3st2 while Fbn2_NH2 by Col23a1, Dsg2 and Ism1.
- Pcsk6_NH1 was positive for Cald1, Pde11a and Cpne2.
- Pcsk6_NH2 contained Tacr3+ Aldh1a1- cells, which also expressed Igf1.
- There were also Tacr3+ Aldh1a1+cells, but they belonged to Otx2_NH1, which also expressed Grp, Eya1, and Plekhg1.
- Otx2_NH2, which was low for Slc6a3, was identified by Csf2rb2, Nfib, and Nfia.
- The Pdia5_NH1 expressed Jph1 Cpne5, and Pdia5_NH2 was positive for Npy1r, Postn, and Wnt7b.
- The Ebf1_NH1 expressed Col24a1, whereas Ebf1_NH2 was positive for Vip.Anatomical distribution of diverse mDA neuronsNext, we investigated the anatomical distribution of the seven mDA neuron territories and their neighborhoods in the adult mouse midbrain.
- We also used an in situ sequencing strategy that included 49 selected probes, hybridized simultaneously on seven sections across the entire midbrain (Figure 4B-E, Figure 4–figure supplements 1-3, Supplementary files 3 and 4)(Gyllborg et al., 2020; Krzywkowski et al., 2017; Qian et al., 2020).
- For the anatomical localization of territories and neighborhoods, we mainly followed Paxinos and colleagues (Fu et al., 2011) and the coronal reference atlas from Allen Mouse Brain Atlas.
- Together these analyses provided the basis of the schematic in Figure 4F, showing the distribution of different territories in rostrocaudal levels of the midbrain.biorxiv;2023.06.05.543445v2/FIG4F4fig4Figure 4.Mapping of mDA territories in the adult mouse midbrainA) A color-coded UMAP projection of 
- E) Fluorescent RNA in situ hybridization with Tacr3 probe combined with immunohistochemistry.
- Scalebars are 200 μm.Consistent with previously published results (Panman et al., 2014; Poulin et al., 2014), Sox6 territory neurons were confined to the SNc and its subdomains (Figure 4F, Figure 4– figure supplement 1, See also Supplementary Results).
- Cells of the Ebf1 territory were scattered within the periaqueductal grey (PAG), parabrachial pigmented nucleus (PBP), rostral linear nucleus (RLi), and para nigral nucleus (PN) (Figure 4F, Figure 4–figure supplement 2), consistent with previous single-cell studies identifying Vip-expressing mDA neu
- Cells of the Pdia5 territory were mapped to the dorsal VTA and the most lateral SN tip (Figure 4F, Figure 4–figure supplement 2).
- Consistent with previous analyses (Hook et al., 2018; Manno et al., 2016; Poulin et al., 2014; Saunders et al., 2018; Tiklova et al., 2019), Otx2 territory was localized in the ventral tier of VTA, including PBP, PN, and interfascicular nucleus (IF), but some cells were also found in RLi and caudal 
- 4F, Figure 4–figure supplement 2).
- Gad2 territory was primarily localized in the most medial VTA, especially to IF, RLi, and CLi (Figure 4A, F, Figure 4–figure supplement 3), supporting findings from previous studies (Garritsen et al., 2023; Poulin et al., 2020).
- A few scattered neurons matching the smallest territory, Fbn2, were detected in the anteromedial PBP (Figure 4A, F, Figure 4–figure supplement 3).
- Finally, neurons of the Pcsk6 territory were localized broadly in VTA, although being most numerous in PBP (Figure 4F, Figure 4–figure supplement 3).The analysis of the anatomical localization of neighborhoods, and how the diversity identified here relates to previous findings, is described in furth
- Animals with partial lesions were chosen for sampling and RNA sequencing of nuclei (Methods, Figure 5–figure supplement 1).
- The nuclei that expressed either Th or Slc6a3 (mDA nuclei dataset, in total 33,052 nuclei) were visualized by UMAP and split by condition to indicate their origin from either lesioned or intact hemispheres (Figure 5A, B).
- Unsurprisingly, fewer nuclei (8,243) were recovered from the lesioned compared to the intact hemisphere (24,809).
- Pearson’s Chi test of independence further supported this conclusion and showed a similar relative distribution among clusters and neighborhoods, per animal, regardless of the number of mDA neurons remaining (Figure 5–figure supplement 1 C).
- Co-staining for TH and RFP on coronal sections of lesioned brains also confirmed this notion (Figure 5–figure supplement 1 E).biorxiv;2023.06.05.543445v2/FIG5F5fig5Figure 5.Normalized cell loss across territories and neighborhoods in mDA datasetA, B) UMAP projection of the dopaminergic dataset nucle
- ns = not significant, * P ≤ 0.05, ** P ≤ 0.01, *** P ≤ 0.001, **** P ≤ 0.0001.
- For the Conover-Iman test; p-value = P(T ≥ |t|), and null hypothesis (H0) was rejected at p ≤ α/2, which is 0.025.
- Error bars show standard deviation (SD).Two conclusions were immediately apparent from the UMAP visualization: First, many nuclei from the lesioned hemisphere were distributed outside of the mDA neuron territories (Figure 5A-B, F, see Figures 2 and 3), and, as expected, the numbers of nuclei in thes
- Second, most mDA neuron nuclei remaining from the lesioned hemispheres were evenly dispersed together with nuclei from the non-lesioned hemispheres within mDA neuron territories and neighborhoods, indicating that surviving cells were relatively similar to non-lesioned cells at the gene expression le
- Next, normalized cell loss per territory and neighborhood was calculated based on the sub-clusters cellular composition per condition, accounting for the global FANS yield per condition and sub-cluster size (see methods, Supplementary file 5).
- The results demonstrated a pervasive loss in the Sox6 territory (Figure 5C), which is consistent with previous studies showing that Sox6-expressing cells of the SNc are more vulnerable to pathological stress in rodents and in PD (Luppi et al., 2021; Panman et al., 2014).
- Cell loss was also notably high in the Pcsk6 territory.
- The Ebf1 territory showed the lowest level of cell loss, while the other territories were affected at intermediate levels (Figure 5C, D).
- Within the Sox6 territory, a consistent and high level of cell loss was seen in all neighborhoods except Sox6_NH3, which showed a somewhat milder but still significant decrease (Fig.
- Notably, different levels of cell loss were often seen within individual territories e.g., Gad2_NH1, and Otx2_NH1 as compared to Gad2_NH2 and Otx2_NH2 (Figure 5E).
- As described above, the corresponding mDA neurons were mostly confined to regions within the VTA, demonstrating that high vulnerability to 6-OHDA was not exclusive to neurons distributed within the SNc.Identification of genes associated with vulnerability or resilienceNext, we set out to identify ge
- Accordingly, genes that are commonly and significantly enriched in intact nuclei from clusters with either >90% (vulnerability genes) or <50% (resilience genes) normalized cell loss were identified (Figure 6–figure supplement 1, Supplementary file 5).
- 39 genes fulfilled the stringent cutoff criteria for vulnerability genes.
- The selected genes were ranked based on average Log2 fold change, and vulnerability and resilience gene modules were constructed, consisting of 20 and 8 most significantly enriched genes, respectively (Figure 6F, G, Supplementary file 6).
- The composite average expression of the gene sets (modules) was visualized in violin plots for neighborhoods and territories (Figure 6A-D, Supplementary File 6).
- As expected, the vulnerability and resilience gene module expression in territories and neighborhoods corresponded to the distribution of the clusters used as input for identifying the gene modules (Figure 6–figure supplement 1).
- However, linear regression analysis also demonstrated a highly significant overall correlation between cell loss and the vulnerability module scores (p-value = 3.89e-10), even when the input clusters were excluded from analysis (Figure 6–figure supplement 1C).
- This suggests that the identified module genes may be functionally associated with either sensitivity to or protection against 6-OHDA-induced cell stress.
- One of the vulnerability genes, Slc6a3, encodes the dopamine transporter used to import 6-OHDA to the cytosol.
- Thus, it is unsurprising that neurons of the Gad2 and Ebf1 territories expressing low levels of Slc6a3 are less vulnerable.
- However, when regression analysis was repeated using a vulnerability gene module in which Slc6a3 had been excluded, correlation to cell loss remained highly significant (Figure 6–figure supplement 1D, p-value = 1.73e-09).
- Therefore, the other genes of the vulnerability module predict the sensitivity to toxic stress.biorxiv;2023.06.05.543445v2/FIG6F6fig6Figure 6.Vulnerability and resilience modules in territories, neighborhoods, and the ML clustersA-B) Violin plots of the vulnerability module across territories and ne
- F) Vulnerability module gene list, ranked by average Log2FC.
- G) Resilience module gene list, ranked by average Log2FC.
- See Methods for the statistical tests used.The Th+/DAT+ dataset of 33,052 nuclei was re-analyzed by the Seurat integration method treating nuclei from lesioned and intact hemispheres as two different experimental conditions (Stuart et al., 2019).
- Vulnerability and resilience modules were plotted across the integrated clusters and were color-coded by territory identities (Figure 6–figure supplement 2).
- Of note, the module scores corresponded well to the clusters, as integrated clusters with the Sox6 territory identity and most of the clusters with the Pcsk6 territory identity showed considerably high and low values of the vulnerability and resilience modules, respectively.Conversely, integrated cl
- In addition, most of the pairwise comparisons of module scores across the mDA-integrated clusters were significant (Figure 6–figure supplement 2, Supplementary file 7).
- Thus, a strong predictive correlation between the expression of vulnerability and resilience modules is apparent across the snRNA-seq data.Finally, we used recently developed tools for using WGCNA to calculate gene co-expression modules based on high-dimensional data sets (Morabito et al., 2023).
- This analysis along with an associated GO term analysis is presented in Figure 6-figure supplement 3, and Supplementary file 9.
- GO terms associated with glutamatergic and GABAergic neuronal functions characterized the co-expression module mostly similar to the resilience gene module, likely reflecting the resilience of atypical mDA neurons with potential for glutamaterigic and GABAergic neurotransmission.Long-lasting gene ex
- To distinguish them from territories harboring nuclei characteristic of the normal non-lesioned /intact hemisphere of the brain, they were named mostly lesion (ML) clusters (Figure 7A, B).
- Although expression of typical mDA neuron markers such as Th and Slc6a3 was low, the ML-clusters were part of the mDA neuron dendrogram branch and shared a parent node with Sox6-territory (Figure 3A, C).
- Using original territory labels, visualizing the integrated data by UMAP was consistent with data from non-integrated original analysis and demonstrated that the mDA neuron nuclei clustered together (Figure 7C, Figure 6-figure supplement 2).
- Next, the integrated data territories were annotated based on the cluster composition of inherited merged (original) territory identities and the enriched markers for the original territories (see Figure 3C).
- In addition to ML clusters being predominantly made up of lesioned nuclei, Sox6 expression level and abundance were also clearly higher than Calb1 (Figure 7D, E).
- Both visualizations of ML-clusters nuclei in the integrated UMAP and quantifications demonstrated that most (>80%) of all ML nuclei were confined to two territories, Sox6 and Pcsk6.
- Notably, these territories were also the most vulnerable when exposed to 6-OHDA (Figure 7F-H, also see Figure 6A, C).biorxiv;2023.06.05.543445v2/FIG7F7fig7Figure 7.Transcriptional kinship and enriched markers of ML clustersA) UMAP projection of the dopaminergic dataset nuclei from the intact (non-le
- D, E) Sox6 and Calb1 expression plotted in intact and lesioned nuclei respectively.
- More than 80% of ML nuclei cluster in Sox6 and Pcsk6 territories of the integrated data.
- Scalebar = 50 µm.Differential gene expression analysis by condition was performed in two different ways.
- Consistent with the similar distribution of most of the lesioned and intact nuclei in the UMAP, relatively few (242 in total) significantly differentially expressed genes were identified (Figure 7–figure supplement 1, Supplementary file 8).
- Consistent with a more dramatic and long-lasting influence from lesioning in the ML-clusters, 1577 genes were found to be differentially expressed in this comparison.
- Several of the most strongly upregulated genes, including Atf3, Creb5, Xirp2, Clic4, Sprr1a, and Mmp12, have in previous studies been associated with cellular stress, cell death, and cell signaling (Figure 7I, Figure 7-figure supplement 1, Supplementary file 8).
- In situ hybridization analysis combined with immunohistochemistry shows apparent upregulation of ML-enriched genes in the lesioned tissue compared to control (Figure 7J-M).
- A GO-enrichment analysis of the genes uniquely dysregulated in ML clusters identified genes associated with axon guidance, synaptic transmission and RAS signaling pathway, among other terms (Figure 7-figure supplement 1 D, E, Supplementary file 10).Although 6-OHDA was injected unilaterally, a potent
- Therefore, to assess whether the stereotactic injection had any effect on the transcriptional profile of the nuclei from the intact hemisphere, we created and analyzed a separate dataset including all Th+/DAT+ nuclei from the intact hemisphere of the brain, merged with a new dataset of 6,001 mCherry
- The dataset was annotated similar to the procedure above and all major cell types were also identifiable in it (Figure 7–figure supplement 2).
- Moreover, comparative differential gene expression analysis also supported the conclusion that any differences between the two groups were attributable to undefined technical parameters in experimental conditions rather than to the effects of the toxin (Figure 7–figure supplement 2, Supplementary fi
- We, therefore, integrated and reanalyzed our mouse data with human snRNAseq data from a recently published paper (Kamath et al., 2022).
- Canonical correlation analysis (CCA) was used to integrate 25,003 nuclei from human control and diseased (PD and Lewy body disease) donors with our lesioned and intact nuclei from the Th+/DAT+ dataset (see methods).
- Detection of mouse-specific UMAP regions is not surprising, given the comprehensiveness of the mDA-enriched mouse dataset.However, human specific UMAP regions were also observed (Figure 8).
- Next, we used the mouse intact nuclei from the mDA territories (see Figure 3) to build a reference UMAP structure onto which the human control nuclei (query dataset) were projected (see methods).
- The results demonstrated that almost 75% of the human control nuclei are mapped to mouse Sox6 territory (Figure 8-figure supplement 1A-D).
- Upon using the mouse intact nuclei, only from Sox6 territory as a reference, and the human control nuclei that were mapped to Sox6 territory in the previous step as query, most of this human query subset were mapped to Sox6-NH2, while almost no nuclei mapped to Sox6-NH4 (Figure 8-figure supplement 1
- The findings that most human nuclei bear the closest resemblance to mouse Sox6 territory nuclei were expected, as the human nuclei were derived from SNc.biorxiv;2023.06.05.543445v2/FIG8F8fig8Figure 8.Integration of human and mouse datasetsA, B) UMAP projections of the integrated dopaminergic human (
- This integrated dataset includes 25,003 human nuclei and 33,052 mouse nuclei.

## Figure Descriptions

### Figure 1.
Generation of a snRNAseq dataset from the mouse midbrainA) Schematic design of the study, unilateral injection of low doses of 6-OHDA (0.7, 1.5 µg/µl) in the medial forebrain bundle (MFB), followed by dissection, nuclei isolation and enrichment via FANS, before library preparation, sequencing, and d

### Figure 2.
Midbrain DA dataset, cell types and compositionA) UMAP projection of the dopaminergic dataset, with numerical labels of the 71 clusters and color-coded for the major cell types. B) Typical dopaminergic markers plotted in UMAP separately, with the top 1 percentile of the normalized gene expression ra

### Figure 3.
Dopaminergic territories and neighborhoodsA) UMAP projection of the dopaminergic dataset with territory color-coding and size. B) Co-expression of Sox6 and Calb1 plotted in UMAP, roughly delineating SNc and VTA respectively. C) Hierarchical dendrograms with labels and color-coded territories and the

### Figure 4.
Mapping of mDA territories in the adult mouse midbrainA) A color-coded UMAP projection of the seven mDA territories and of the mostly-lesion (ML) clusters, with individual enriched genes plotted on smaller UMAPs. B-D) Immunohistochemical staining with antibodies indicated in the ventral midbrain. E)

### Figure 5.
Normalized cell loss across territories and neighborhoods in mDA datasetA, B) UMAP projection of the dopaminergic dataset nuclei from the intact (un-lesioned) and the lesioned hemisphere, respectively. C) Calculated normalized cell loss for territories, visualized as percentages. D) Pairwise compari

### Figure 6.
Vulnerability and resilience modules in territories, neighborhoods, and the ML clustersA-B) Violin plots of the vulnerability module across territories and neighborhoods, with percentage of normalized cell loss shown at the bottom per territory and neighborhood, respectively. C-D) Violin plots of th

### Figure 7.
Transcriptional kinship and enriched markers of ML clustersA) UMAP projection of the dopaminergic dataset nuclei from the intact (non-lesioned) hemisphere. B) UMAP projection of the dopaminergic dataset nuclei from the lesioned hemisphere. ML clusters are marked with dashed circles in A and B. C) UM

### Figure 8.
Integration of human and mouse datasetsA, B) UMAP projections of the integrated dopaminergic human (control + diseased) and mouse (intact + lesioned) nuclei, split per condition. This integrated dataset includes 25,003 human nuclei and 33,052 mouse nuclei. C) UMAP projections of the human and mouse 

## References
Total references in published paper: 49

### Key References (from published paper)
- Single-nucleus and single-cell transcriptomes compared in matched cortical cell types (, 2018)
- Dopamine neuron systems in the brain: an update (, 2007)
- Parkinson’s disease: animal models and dopaminergic cell vulnerability (, 2014)
- Functional properties of dopamine neurons and co-expression of vasoactive intestinal polypeptide in  (, 2012)
- Progressive parkinsonism in mice with respiratory-chain-deficient dopamine neurons (, 2007)
- FLUORESCENCE OF CATECHOL AMINES AND RELATED COMPOUNDS CONDENSED WITH FORMALDEHYDE (, 1962)
- A cytoarchitectonic and chemoarchitectonic analysis of the dopamine cell groups in the substantia ni (, 2011)
- Development, wiring and function of dopamine neuron subtypes (, 2023)
- Hybridization-based in situ sequencing (HybISS) for spatially resolved transcriptomics in human and  (, 2020)
- Normalization and variance stabilization of single-cell RNA-seq data using regularized negative bino (, 2019)
- Integrated analysis of multimodal single-cell data (, 2021)
- Single-Cell RNA-Seq of Mouse Dopaminergic Neurons Informs Candidate Gene Selection for Sporadic Park (, 2018)
- Evaluation of TRAP-sequencing technology with a versatile conditional mouse model (, 2014)
- Activating Transcription Factor 3 Is Integral to the Eukaryotic Initiation Factor 2 Kinase Stress Re (, 2004)
- Single-cell genomic profiling of human dopamine neurons identifies a population that selectively deg (, 2022)
- The Longitudinal Transcriptomic Response of the Substantia Nigra to Intrastriatal 6-Hydroxydopamine  (, 2015)
- VGluT2 Expression in Dopamine Neurons Contributes to Postlesional Striatal Reinnervation (, 2020)
- A transcriptomic atlas of mouse cerebellar cortex comprehensively defines cell types (, 2021)
- Using single nuclei for RNA-seq to capture the transcriptome of postmortem neurons (, 2016)
- In Situ Single-Molecule RNA Genotyping Using Padlock Probes and Rolling Circle Amplification (, 2017)
- Enrichr: a comprehensive gene set enrichment analysis web server 2016 update (, 2016)
- WGCNA: an R package for weighted correlation network analysis (, 2008)
- Identification of candidate genes associated with clinical onset of Alzheimer’s disease (, 2022)
- K-ATP channels promote the differential degeneration of dopaminergic midbrain neurons (, 2005)
- Sox6 expression distinguishes dorsally and ventrally biased dopamine neurons in the substantia nigra (, 2021)
- Molecular Diversity of Midbrain Development in Mouse, Human, and Stem Cells (, 2016)
- Brain-derived growth factor and nerve growth factor concentrations are decreased in the substantia n (, 1999)
- Single-nucleus chromatin accessibility and transcriptomic characterization of Alzheimer’s disease (, 2020)
- hdWGCNA identifies co-expression networks in high-dimensional transcriptomics data (, 2023)
- Ventral tegmental area: cellular heterogeneity, connectivity and behaviour (, 2017)

## Ground Truth Reference
- Figures: 8
- Tables: 0
- References: 49