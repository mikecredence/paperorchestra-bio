# Experimental Log: A supervised Bayesian factor model for the identification of multi-omics signatures

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- 3Results3.1SPEAR improves prediction of synthetic responses from simulated multi-omics dataWe first evaluated the ability of SPEAR to predict a Gaussian response on simulated data.
- In the simulation, five predetermined factor signals (U) were used to construct four multi-omics assays (X), each with 500 analytes (for a total of 2,000 simulated features), for 500 training and 2,000 test samples.
- This procedure was repeated across a gradient of signal-to-noise ratios (low signal, moderate signal, and high signal), with 10 independent iterations for each ratio (Supplementary Methods D).We trained SPEAR across a gradient of values for weight w to demonstrate the effect of w on SPEAR’s performa
- As a comparison, we also employed a two-step MOFA-based model that performs Lasso regression (Tibshirani, 1996) using factors derived from MOFA (denoted as MOFA in the following) as well as a vanilla Lasso regression model using concatenated features in lieu of factors (denoted as Lasso).
- 2c).biorxiv;2023.01.25.525545v2/FIG2F2fig2Figure 2.Gaussian simulation results.
- Color is applied to factor scores found to be correlated with true factors 1 (red) and 2 (blue) with true factors 3-5 designated as grey.
- Significant correlations are denoted with ‘*’ for p ≤ 0.001.In scenarios with moderate signal-to-noise, SPEAR with w = 1 significantly outperformed MOFA (Fig.
- Correlation analyses of the factor scores for one iteration (denoted by the red line in Figure 2a) confirmed that SPEAR with w = 1 correctly identified all five simulated factors, whereas MOFA only identified two of the uncorrelated factors (Factor 3 and Factor 5) likely due to the lack of supervisi
- 2c), which was confirmed across all 10 iterations (Supplementary Fig.
- As expected, SPEAR with w = 0 condensed all predictive signals into a single factor, as evidenced by its correlation with the first two simulated factors.
- Overall, SPEAR with higher weights achieved the best predictive performance due to better reconstruction of the multiple underlying simulated factors.Finally, we repeated the above protocol to test the ability of SPEAR for predicting various non-Gaussian responses (Supplementary Methods A1).
- 4C-D).biorxiv;2023.01.25.525545v2/FIG3F3fig3Figure 3.TCGA-BC Tumor Subtype and COVID-19 Severity Prediction Results.
- Error bars show the 95% confidence interval found via 2,000 stratified bootstrapping replicates.
- Significance testing is denoted as * (p ≤ .05), ** (p ≤ .005), and *** (p ≤ .0005).
- (D, H) Balanced misclassification errors of SPEAR, MOFA, DIABLO, and Lasso on test samples from the (D) TCGA (Breast Cancer) dataset and (H) COVID-19 dataset.biorxiv;2023.01.25.525545v2/FIG4F4fig4Figure 4.Downstream TCGA-BC Analysis.
- (A) Grouped violin plot of factors 1-3 scores (y-axis) and tumor subtype (x-axis), with group means marked with a line.
- (B) 3D scatter plot, embedding samples by factors 1, 2, and 3 scores.
- (C) Dotplot of GSEA results on mRNA features for factors 1-3.
- (D) GSEA plot for Estrogen Response (Early) Hallmark pathway for SPEAR Factor 1.
- mRNA genes are ranked by their assigned projection coefficient from SPEAR factor 1.
- (E) Heatmap showing normalized expressions for the top 24 mRNA genes involved in the Estrogen Response (Early) Hallmark pathway.
- mRNA genes were selected with a factor loading (projection coefficient) magnitude ≥ .02.
- Samples were ranked by Factor 1 score (x-axis) and genes were ranked by projection coefficient (y-axis).
- Also shown are corresponding true tumor subtypes (True) and SPEAR-predicted tumor subtypes (Pred).3.2SPEAR improves prediction of breast cancer tumor subtypes and COVID-19 severityTo test whether SPEAR could achieve competitive performance in real data, we applied SPEAR to two publicly available mul
- (Singh et al., 2019) with the goal of tumor subtype prediction, and a SARS-CoV-2 patient dataset of blood samples by Yapeng et al.
- (Su et al., 2020) with the goal of predicting disease severity.
- We refer to these datasets as TCGA-BC (The Cancer Genome Atlas (Cancer Genome Atlas Network, 2012) - Breast Cancer) and COVID-19, respectively.
- The TCGA-BC dataset is composed of 989 biopsy samples each associated with RNA-Seq, miRNA, and methylation probe data from primary solid breast cancer tumors that have been annotated according to the PAM50 subtype signature into one of four subtypes: Luminal A (LumA), Luminal B (LumB), HER2-enriched
- The COVID-19 dataset contains plasma protein and metabolite compositions for 254 SARS-CoV-2 positive patient samples and 124 matched healthy subject samples.
- Each subject is associated with a severity score based on the World Health Organization (WHO) ordinal severity score (Rubio-Rivas et al., 2022), binned into four ordinal classes (healthy, mild, moderate, and severe).We applied SPEAR, Lasso, MOFA, and DIABLO to predict the response from each multi-om
- AUROC significance was calculated via a bootstrapping procedure and compared via DeLong’s test (DeLong et al., 1988).The advantage of SPEAR was clear when looking at the multi-class AUROC, measuring a classifier’s ability to discriminate each class individually across a gradient of threshold values.
- 3c), and moderate SARS-CoV-2 severity from the COVID-19 dataset (Fig.
- 3g) compared to all other models via AUROC comparison testing (LumB – MOFA: p.adj=7.8e-09, Lasso: p.adj=2.1e-07, DIABLO: p.adj=1.9e-02; Moderate – MOFA: p.adj=1.4e-02, Lasso: p.adj=1.9e-04, DIABLO: p.adj=1.5e-05).
- The balanced misclassification errors of SPEAR (0.15, 0.21) were comparable to those of Lasso (0.15, 0.21), MOFA (0.16, 0.21), and DIABLO (0.16, 0.23) for the TCGA-BC dataset and COVID-19 dataset respectively (Fig.
- Overall, our results demonstrate that SPEAR outperforms current state-of-the-art methods for predicting a response using multi-omics data.biorxiv;2023.01.25.525545v2/FIG5F5fig5Figure 5.Downstream COVID-19 Dataset Analysis.
- (A) Grouped violin plot of factor 2 scores (y-axis) and simplified WHO score (x-axis), with group means marked with a line.
- (B) Grouped violin plot of factor 8 scores (y-axis) and simplified WHO score (x-axis), with group means marked with a line.
- (C) GSEA plot for IL6 JAK STAT3 Signaling Hallmark pathway for SPEAR Factor 2.
- Proteins are ranked by their assigned projection coefficient from SPEAR factor 2.
- (D) Embedding of samples by factor 8 (x-axis) and factor 2 (y-axis) scores.
- Samples are colored by WHO Ordinal Score, normalized IL6 expression, and normalized kynurenine expression.
- (E) Heatmap showing normalized expressions for proteins involved in the IL6 JAK STAT3 Signaling Hallmark pathway.
- Samples were ranked by Factor 2 score (x-axis) and proteins were ranked by projection coefficient (y-axis).
- (F) Alluvial plot showing correlation between the IL6 JAK STAT3 proteins and the top metabolite features contributing to SPEAR Factor 2.
- Also shown are normalized plasmalogen expressions of samples ranked by Factor 2 score (x-axis).It was notable that the balanced misclassification error of SPEAR was comparable with other methods even though SPEAR does not optimize purely for predictive performance.
- If we instead choose the w that minimizes the cross-validated error (denoted as SPEAR min), the balanced misclassification error is better than all other models on both the TCGA-BC and COVID-19 datasets (0.13, 0.19) (Supplementary Fig.
- The SPEAR min model showed only a slight improvement in classification accuracy but chose considerably lower w values (w = 0.5 for TCGA-BC and w = 0.01 for COVID-19) than the default SPEAR model (denoted as SPEAR sd when needed for clarity) (w = 2.0 for both datasets) (see Supplementary Fig.
- Although we recommend and used the default SPEAR model to enhance the downstream interpretation, SPEAR min can be used in cases where prediction is the key objective regardless of multi-omics assay influence in factor construction.3.3SPEAR identifies steroid response pathways associated with TCGA PA
- Factors 1-3 clearly distinguished one or more subtypes, which motivated us to investigate what biological pathways each factor was associated with (Fig.
- Factor 1 was strongly associated with the Basal subtype and moderately associated with the HER2e subtype (Fig.
- 4b), while the negative factor loadings were enriched for Estrogen Response (ER) (Early and Late) pathways of the Molecular Signatures Database (MSigDB) Hallmark collection (Liberzon et al., 2015) (Fig.
- 4d).The anti-correlation between the ER pathways and the Basal subtype, the highest scoring Factor 1 subtype, reflects that it is most strongly associated with a triple-negative profile for Estrogen, Progesterone, and the HER2e receptor (Prat et al., 2013).
- Whereas HER2e-classified samples were predominantly hormone receptor (HR) negative, a proportion is also HR positive (Bastien et al., 2012; Prat et al., 2015).
- LumA and LumB are hormone receptor positive (HR) and retain expression of ER, and the Progesterone receptor (PR) in the case of LumA, and in some proportion of LumB (Prat et al., 2015).
- Indeed, genes XBP1, AGR2, and CA12 which yielded high posterior selection probabilities as well as the strongest negative projection coefficients in Factor 1 (Fig.
- 4e, Supplemental Table 1) for the Estrogen Response (Late) pathway were all associated with a breast cancer Steroid Responsiveness (SR) module that indicates functional steroid response (Fredlund et al., 2012).
- Genes XBP1 and MYB were in the top 20% of the ER Early and Late pathway genes with respect to the SPEAR projection coefficient magnitude.
- MYB is a direct target of Estrogen signaling and is overexpressed in most ER+ cancers (Gonda et al., 2008), and both genes were also identified as part of a luminal expression signature (Cancer Genome Atlas Network, 2012).The positive association of Factor 1 with the MYC Targets V1 Hallmark pathway 
- Additionally, four of the miRNAs associated with Factor 1, hsa-mir-18a, hsamir-10a, hsa-mir135b, hsa-mir-577, were identified in a miRNA analysis of TCGA data to have diagnostic significance for triple-negative breast cancer (Fan and Liu, 2019).
- Hsa-mir-18a has been shown in independent datasets to downregulate ERα (Klinge, 2012) and is associated with worse overall survival (Luengo-Gil et al., 2019).
- Hypomethylation of MIA, a PAM50 gene, which has the second highest in magnitude SPEAR projection coefficient for Factor 1, has been associated with the Basal subtype in TCGA and independent data (Bardowell et al., 2013).Factor 1 distinguished Basal-like and HER2e subtypes from LumA/LumB, while Facto
- Pathways enriched in Factor 2 were associated with genes that are more highly expressed in LumA, whereas pathways in Factor 3 were associated with genes that are downregulated in LumA (Fig.
- The strongest signal in Factor 2 was in the Epithelial Mesenchymal Transition (EMT) Hallmark pathway, and in Factor 3 the G2M Checkpoint Hallmark pathway (Fig.
- It has been previously observed that LumB tumors are enriched in proliferation and cell-cycle associated genes in comparison to LumA (Prat et al., 2015), whereas the positive association of LumA with an EMT phenotype is somewhat surprising, as LumA tumors are generally considered to be associated wi
- The role of EMT has been primarily studied in non-luminal tumors28, and therefore the presence of this pathway distinguishing the subtypes warrants further investigation with respect to the underlying biology.
- Interestingly, the miRNAs with the top magnitude projection coefficients in Factor 2 and which have a positive association with the factor, hsa-mir199a/b, have been associated with EMT (Drago-García et al., 2017; Wang et al., 2019).
- Overall, the molecular signatures identified via SPEAR factorization of the TCGA-BC data provided both well-documented and novel associations with PAM50 breast cancer subtypes.3.4SPEAR identifies multi-omics factors and pathways associated with COVID-19 severityOn the COVID-19 dataset, SPEAR identif
- Investigation of the association of each factor with the COVID-19 severity revealed that the Factor 2 score showed a positive ordinal association (Fig.
- SPEAR also identified several factors that were heavily associated with identifying COVID-19 severities, including Factor 1 score for mild severity and Factor 8 for moderate severity (Fig.
- Embedding the samples by Factors 2 and 8 scores revealed a trajectory for SARS-CoV-2 severities (Fig.
- Calculation of the variance explained for these three factors revealed that Factor 2 had the largest influence from both assays (16% proteomics, 11% metabolomics) compared to Factor 1 (20% proteomics, 1% metabolomics) and Factor 8 (1% proteomics, 2% metabolomics) (Supplementary Fig.
- We opted to further investigate Factor 2 due to its larger multi-omics influences.Proteomic enrichment analysis of Factor 2 identified several significant pathways from the MSigDB Hallmark pathway database (Supplemental Table 2).
- One pathway enriched in Factor 2 was the Janus kinase Signal Transducer and Activator of Transcription (JAK-STAT) signaling pathway (Seif et al., 2017) (Fig.
- Pathway member Interleukin 6 (IL-6) was also found to be a key contributor to the Factor 2 score, with the second highest projection coefficient (Fig.
- IL-6 is a proinflammatory cytokine proposed as an inflammatory biomarker for COVID-19 severity (Azevedo et al., 2021) and is an activator of the JAK-STAT signaling pathway.
- The JAK-STAT signaling pathway is involved in immune regulation, lymphocyte growth and differentiation, and promotes oxidative stress, serving as an attractive therapeutic target for COVID-19 treatment (Luo et al., 2020).The Factor 2 metabolic signature, extracted via automatic feature selection of 
- Kynurenine, a key contributor to the Factor 2 score, is a known marker of severe/fatal COVID-19 trajectory (Danlos et al., 2021; Mangge et al., 2021).
- The tryptophan/kynurenine (Trp/Kyn) pathway is activated by inflammatory cytokines (Almulla et al., 2022), which is consistent with its positive correlation with the cytokines of Factor 2 such as IL-6 (Fig.
- 5f).Several plasmalogens, including phosphatidylcholines (PCs) and phosphatidylethanolamines (PEs) were also found to be inversely associated with the ordinal severity trend of Factor 2 (Fig.
- Plasmalogens are plasma-borne antioxidant phospholipids that provide endothelial protection during oxidative stress (Messias et al., 2018), which could account for the inverse association with the JAK-STAT signaling pathway proteins.
- Our multi-omics results further support the utility of plasmalogens as prognostic indicators of COVID-19 severity (Pike et al., 2022).

## Figure Descriptions

### Figure 1.
SPEAR workflow overview: (A) SPEAR takes multi-omics data (X) taken from the same N samples, as well as a response of interest (Y). SPEAR supports Gaussian, ordinal, and multinomial types of responses. From these inputs, the algorithm first automatically estimates the minimum number of factors to us

### Figure 2.
Gaussian simulation results. (A) Boxplots of mean-squared errors of the models on the testing data. MSE results for each simulated iteration are connected. Results are shown for varying signal-to-noise ratios, including low, moderate, and high signals. (B) Scatterplots of various factor scores (y-ax

### Figure 3.
TCGA-BC Tumor Subtype and COVID-19 Severity Prediction Results. (A, E) Test sample class predictions of the SPEAR model, colored by true class. (B, F) Multi-class AUROC statistics for each model for the LumB and Moderate classes. Error bars show the 95% confidence interval found via 2,000 stratified

### Figure 4.
Downstream TCGA-BC Analysis. (A) Grouped violin plot of factors 1-3 scores (y-axis) and tumor subtype (x-axis), with group means marked with a line. (B) 3D scatter plot, embedding samples by factors 1, 2, and 3 scores. Samples are colored by tumor subtype. (C) Dotplot of GSEA results on mRNA feature

### Figure 5.
Downstream COVID-19 Dataset Analysis. (A) Grouped violin plot of factor 2 scores (y-axis) and simplified WHO score (x-axis), with group means marked with a line. (B) Grouped violin plot of factor 8 scores (y-axis) and simplified WHO score (x-axis), with group means marked with a line. (C) GSEA plot 

## References
Total references in published paper: 53

### Key References (from published paper)
- The tryptophan catabolite or kynurenine pathway in COVID-19 and critical COVID-19: a systematic revi (, 2022)
- MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data (, 2020)
- Covid-19 and the cardiovascular system: a comprehensive review (, 2021)
- Mitochondria in innate immune signaling (, 2018)
- Differential methylation relative to breast cancer subtype and matched normal tissue reveals distinc (, 2013)
- PAM50 breast cancer subtyping by RT-qPCR and concordance with standard clinical molecular markers (, 2012)
- ImmPort: disseminating data to the public for the future of immunology (, 2014)
- Systematic comparison of published host gene expression signatures for bacterial/viral discriminatio (, 2022)
- Dynamic expression profiling of type I and type III interferon-stimulated hepatocytes reveals a stab (, 2014)
- Comprehensive molecular portraits of human breast tumours (, 2012)
- Benchmarking joint multi-omics dimensionality reduction approaches for the study of cancer (, 2021)
- Benchmarking transcriptional host response signatures for infection diagnosis (, 2022)
- Metabolomic analyses of COVID-19 patients unravel stage-dependent and prognostic biomarkers (, 2021)
- Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves: A Nonpara (, 1988)
- Network analysis of EMT and MET micro-RNA regulation in breast cancer (, 2017)
- Identification of dysregulated microRNAs associated with diagnosis and prognosis in triple-negative  (, 2019)
- EMT in Breast Carcinoma-A Review (, 2016)
- Pan-vaccine analysis reveals innate immune endotypes predictive of antibody responses to vaccination (, 2022)
- The gene expression landscape of breast cancer is shaped by tumor protein p53 status and epithelial- (, 2012)
- Personalizing the treatment of women with early breast cancer: highlights of the St Gallen Internati (, 2013)
- Estrogen and MYB in breast cancer: potential for new therapies (, 2008)
- Post model-fitting exploration via a “Next-Door” analysis (, 2020)
- Transcriptional atlas of the human immune response to 13 vaccines reveals a common predictor of vacc (, 2022)
- Generalized additive models for medical research (, 1995)
- miRNAs and estrogen action (, 2012)
- Shared and Distinct Functions of Type I and Type III Interferons (, 2019)
- Identifying multi-layer gene regulatory modules from multi-dimensional genomic data (, 2012)
- The Molecular Signatures Database (MSigDB) hallmark gene set collection (, 2015)
- Clinical and biological impact of miR-18a expression in breast cancer after neoadjuvant chemotherapy (, 2019)
- Targeting JAK-STAT Signaling to Control Cytokine Release Syndrome in COVID-19 (, 2020)

## Ground Truth Reference
- Figures: 5
- Tables: 0
- References: 53