# Experimental Log: Disseminating cells in human oral tumours acquire an EMT cancer stem cell state that is predictive of metastasis

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- In combination with EpCAM, we stained tumour specimens for CD24 as a second marker of plastic EMT CSCs, and Vimentin as a mesenchymal marker to identify cells that have undergone EMT.
- Notably, CD44 cannot be used as an EMT marker in the context of intact tissue as it requires trypsin degradation in order to yield differential expression in EMT and epithelial populations (Biddle et al., 2013; Mack and Gires, 2008).
- Vimentin, on the other hand, accurately distinguishes EMT from epithelial tumour cells in immunofluorescent staining protocols (Biddle et al., 2016).
- By combining EpCAM as a tumour lineage and EMT CSC marker, Vimentin as a mesenchymal marker, and CD24 as a plastic EMT CSC marker, we aimed to identify tumour cells that have undergone EMT and disseminated into the surrounding stromal region.
- For this, we developed a protocol for automated 4-colour (3 markers + nuclear stain) immunofluorescent imaging and analysis of entire histopathological slide specimens, to test for co-localisation of the 3 markers in each individual cell across each specimen.To determine whether this marker combinat
- EpCAM+Vim+CD24+ cells were greatly enriched in the EMT-stem sub-line, comprising 41% of the population, compared to 2.1% in the CA1 line (Figure 1A, B, E).
- Cells with this staining profile were absent from normal keratinocyte culture and cancer associated fibroblast culture (Supplementary Figure S1).
- There was very little Pan-keratin+Vim+CD24+ staining, and no enrichment for Pan-keratin+Vim+CD24+ cells in the EMT-stem sub-line (Figure 1C, D, E).
- Therefore, whilst epithelial keratins are lost, EpCAM is retained in cells undergoing EMT and an EpCAM+Vim+CD24+ staining profile can be used as a marker for EMT CSCs in immunofluorescent staining protocols.biorxiv;2020.04.07.029009v2/FIG1F1fig1Figure 1Immunofluorescent co-staining for EpCAM, Viment
- A-D, Immunofluorescent staining for EpCAM, Vimentin and CD24 (A, B) and pan-keratin, Vimentin and CD24 (C, D) in the CA1 cell line (A, C) and the EMT-stem CA1 sub-line (B, D).
- E, Quantification of the percentage of EpCAM+Vim+CD24+ and pan-keratin+Vim+CD24+ cells in the CA1 cell line and EMT-stem sub-line.
- The graph shows mean +/-95% confidence interval.
- F, Detection of EpCAM+Vim+CD24+ cells in the stroma surrounding an oral cancer tumour specimen.
- The white arrow highlights an EpCAM+Vim+CD24+ cell in the stroma.
- The red arrow highlights an EpCAM+Vim+CD24- cell in the stroma.
- Scale bars = 100µm.Imaging the tumour body and adjacent stroma in sections of human OSCC specimens, we detected single cells co-expressing EpCAM, Vimentin and CD24 in the stromal region surrounding the tumour (Figure 1F), confirming that these cells can be detected in human tumour specimens.
- We next stratified 24 human primary OSCC specimens into 12 tumours that had evidence of lymph node metastasis or perineural spread, and 12 that remained metastasis free (Supplementary Figure S2), and stained them for EpCAM, Vimentin and CD24.
- Single cells co-expressing EpCAM, Vimentin and CD24 were abundant in the stroma surrounding metastatic tumours.
- This was not the case in non-metastatic tumours or normal epithelial regions (Figure 2, A-C).
- In contrast to EpCAM, pan-keratin staining did not identify cells in the stroma surrounding metastatic tumours (Figure 2D).biorxiv;2020.04.07.029009v2/FIG2F2fig2Figure 2Enrichment of EpCAM+Vim+CD24+ cells in the stroma surrounding metastatic tumours.
- A-C, Immunofluorescent four-colour staining of oral tumour specimens for EpCAM (yellow), Vimentin (red) and CD24 (green) with DAPI nuclear stain (blue).
- D, Staining of a metastatic tumour for pan-keratin, Vimentin and CD24.
- Grey level intensities for EpCAM, Vimentin and CD24 were obtained for every nucleated cell in each imaging field.
- F, Quantification of the percentage of EpCAM+Vim+CD24+, EpCAM+Vim+CD24- and pan-keratin+Vim+CD24+ cells in normal region (epithelium distant from the tumour), tumour body, and stromal region from metastatic and non-metastatic tumours in the first batch of specimens.
- A student t-test was performed comparing the mean percentage of EpCAM+Vim+CD24+ co-expressing cells in the metastatic stroma compared to the other fractions.
- The graph shows mean +/-95% confidence interval.
- White arrows highlight single EpCAM+Vim+CD24+ cells in the stroma.
- Scale bars = 100 µm.biorxiv;2020.04.07.029009v2/FIG3F3fig3Figure 3Predicting metastasis using EpCAM, Vimentin and CD24 immunofluorescent staining and a supervised machine learning approach.
- A, Pipeline for machine learning based on grey level intensities for the three markers in tumour batch 1.
- B, C, Performance of EpCAM, Vimentin and CD24 (B) and pan-keratin, Vimentin and CD24 (C) in the supervised learning task on tumour batch 1.
- The tables show the 10-fold cross-validation F1 scores of different machine learning classification algorithms.
- D, Performance of EpCAM, Vimentin and CD24 in the supervised learning task on tumour batch 2.
- An ANN classifier was trained and tested on batch 2, independently of tumour batch 1.
- Accuracy and loss scores are displayed for the training set (green and blue lines) and the validation set (red and yellow lines) drawn from within this batch, for 14 training epochs on the ANN classifier.We developed an image segmentation protocol that separated the tumour body from the adjacent str
- Expression of EpCAM, Vimentin and CD24 was then analysed for every nucleated cell in every imaging field that included both tumour and stroma (3500 manually curated imaging fields across the 24 tumours).
- This enabled the proportion of each cell type in each region to be quantified (Figure 2F).
- EpCAM+Vim+CD24+ cells were enriched in the stroma compared to the tumour body, and there was a much greater accumulation of EpCAM+Vim+CD24+ cells in the stroma of metastatic tumours compared to non-metastatic tumours.
- Interestingly, this was not the case for EpCAM+Vim+CD24- cells, which were also enriched in the stroma but showed no difference between metastatic and non-metastatic tumours.
- Pan-keratin+Vim+CD24+ cells were not detected.To extend this analysis, we stained and imaged a further 60 tumours, evenly stratified on the same criteria.
- These displayed the same evidence of individual disseminating cells co-expressing EpCAM, Vimentin and CD24 in metastatic tumours only (Figure 2G and Supplementary Figure S3F, G).
- For these tumours, using a variation on the previous image segmentation protocol (Supplementary Figure S3, A-D), the proportion of EpCAM+Vim+CD24+ and EpCAM+Vim+CD24- cells was quantified for each cell in over 9000 imaging fields at the tumour-stroma boundary (Supplementary Figure S3E).
- Consistent with the previous set of tumours, only EpCAM+Vim+CD24+ cells were specifically enriched in the stroma of metastatic tumours.To explore whether these EpCAM+Vim+CD24+ cells in the stroma may in fact be non-tumour cell types, we analysed a published scRNAseq dataset for human head and neck c
- Analysing this dataset for EpCAM, Vimentin and CD24 co-expression, we found that 12% of tumour cells (267/2215) were EpCAM+Vim+CD24+.
- In the non-tumour cells, only 0.8% (29/3687) were EpCAM+Vim+CD24+ (Supplementary Figure S4).
- Therefore, the observed EpCAM+Vim+CD24+ cells in our tumour specimens are highly likely to be a tumour cell population.
- EpCAM is a specific epithelial marker, that is not expressed in stromal or immune cells – it is expressed exclusively in epithelia and epithelial-derived tumours (Keller et al., 2019).These findings demonstrate that an EpCAM+Vim+CD24+ staining profile marks tumour cells disseminating into the surrou
- The presence of disseminating tumour cells that express EpCAM but not CD24 did not correlate with metastasis.
- This highlights a requirement for the plasticity marker CD24, when identifying disseminating metastatic CSCs.Identification of EpCAM+CD24+Vim+ CSCs enables clinical prediction using a machine learning approachOSCC are an important health burden and one of the top ten cancers worldwide, with over 300
- There is frequent metastatic spread to the lymph nodes of the neck; this is the single most important predictor of outcome and an important factor in treatment decisions (Sano and Myers, 2007).
- We sought to determine whether the EpCAM+CD24+Vim+ staining pattern could be predictive of metastasis.Starting with the EpCAM, Vimentin and CD24 immunofluorescence grey levels for each nucleated cell, we used a supervised machine learning approach to predict whether an imaging field comes from a met
- As a benchmark we used the pan-keratin, Vimentin and CD24 immunofluorescence grey levels, as we hypothesised that pan-keratin would provide an inferior predictive value than EpCAM given that there was no dissemination of pan-keratin expressing cells in the stroma.
- 3500 imaging fields containing 2,640,000 total nucleated cells from 24 tumour specimens were used in the machine learning task.
- We compared the performance accuracy (10-fold cross-validated F-score) of different machine learning classification algorithms.
- The best performing classifiers for EpCAM, Vimentin and CD24 were the artificial neural network (ANN) and support vector machine (SVM), with F1 accuracy scores of 91% and 87% respectfully (Figure 5B).
- For the ANN, the area under the curve (AUC) accuracy score was 87%, with 94% sensitivity and 82% specificity.
- Training with Pan-keratin, Vimentin and CD24 gave much worse prediction across all classifiers (Figure 5C).
- These findings demonstrate that, utilising a machine learning algorithm, staining for EpCAM, Vimentin and CD24 can predict metastatic status with high accuracy and may therefore have clinical utility.To extend this analysis of utility for metastasis prediction, we stained and imaged a further 60 tum
- Over 9000 imaging fields at the tumour-stroma boundary from 60 evenly stratified tumour specimens, containing over 8.5 million nucleated cells, were fed into an artificial neural network machine learning task.
- For this task, we recorded the predictive accuracy from the training and validation sets after each training epoch, which showed good alignment and an 89% accuracy score after 12 training epochs (Figure 5D).To our knowledge, this is the first time immunofluorescent staining of human tumour tissue sp
- Previous studies using cytokeratin immunohistochemistry, clinicopathological data and serum biomarkers for clinical prediction via machine learning have achieved AUCs of 75% in breast cancer (Tseng et al., 2019), 80% in OSCC (Bur et al., 2019), and 82% in colorectal cancer (Takamatsu et al., 2019).

## Figure Descriptions

### Figure 1
Immunofluorescent co-staining for EpCAM, Vimentin and CD24 identifies the EMT stem cell state. A-D, Immunofluorescent staining for EpCAM, Vimentin and CD24 (A, B) and pan-keratin, Vimentin and CD24 (C, D) in the CA1 cell line (A, C) and the EMT-stem CA1 sub-line (B, D). E, Quantification of the perc

### Figure 2
Enrichment of EpCAM+Vim+CD24+ cells in the stroma surrounding metastatic tumours. A-C, Immunofluorescent four-colour staining of oral tumour specimens for EpCAM (yellow), Vimentin (red) and CD24 (green) with DAPI nuclear stain (blue). Representative imaging fields from a normal epithelial region (A)

### Figure 3
Predicting metastasis using EpCAM, Vimentin and CD24 immunofluorescent staining and a supervised machine learning approach. A, Pipeline for machine learning based on grey level intensities for the three markers in tumour batch 1. The training tiles were classified as coming from a metastatic or non-

## References
Total references in published paper: 28

### Key References (from published paper)
- Multidimensional Binary Search Trees Used for Associative Searching (, 1975)
- CD44 staining of cancer stem-like cells is influenced by down-regulation of CD44 variant isoforms an (, 2013)
- Phenotypic Plasticity Determines Cancer Stem Cell Therapeutic Resistance in Oral Squamous Cell Carci (, 2016)
- Cancer stem cells in squamous cell carcinoma switch between two distinct phenotypes that are prefere (, 2011)
- The relevance of EMT in breast cancer metastasis: Correlation or causality? (, 2015)
- Cancer cell invasion and EMT marker expression: a three-dimensional study of the human cancer-host i (, 2014)
- Machine learning to predict occult nodal metastasis in early oral squamous cell carcinoma (, 2019)
- Fast Multi-Class Image Annotation with Random Subwindows and Multiple Output Randomized Trees (, 2009)
- Molecular profiling of tumour budding implicates TGFβ-mediated epithelial-mesenchymal transition as  (, 2015)
- Biology and clinical relevance of EpCAM (, 2019)
- Single-cell analysis reveals a stem-cell program in human metastatic breast cancer cells (, 2015)
- Probing the Fifty Shades of EMT in Metastasis (, 2016)
- Breast Cancer Stem Cells Transition between Epithelial and Mesenchymal States Reflective of their No (, 2014)
- CD44s and CD44v6 expression in head and neck epithelia (, 2008)
- Metastatic colonization requires the repression of the epithelial-mesenchymal transition inducer Prr (, 2012)
- Scikit-learn: Machine Learning in Python (, 2011)
- Single-Cell Transcriptomic Analysis of Primary and Metastatic Tumor Ecosystems in Head and Neck Canc (, 2017)
- Learning Representations by Back-Propagating Errors (, 1986)
- HDAC inhibition impedes epithelial-mesenchymal plasticity and suppresses metastatic, castration-resi (, 2016)
- Metastasis of squamous cell carcinoma of the oral tongue (, 2007)
- Immortalized N/TERT keratinocytes as an alternative cell source in 3D human epidermal models (, 2017)
- A tutorial on support vector regression (, 2004)
- Prediction of early colorectal cancer metastasis by machine learning using digital slide images (, 2019)
- Epithelial-mesenchymal transition spectrum quantification and its efficacy in deciphering survival a (, 2014)
- Spatiotemporal regulation of epithelial-mesenchymal transition is essential for squamous cell carcin (, 2012)
- Predicting breast cancer metastasis by using serum biomarkers and clinicopathological data with mach (, 2019)
- Controversies around epithelial-mesenchymal plasticity in cancer metastasis (, 2019)
- Exploring conditions for the optimality of Naive bayes (, 2005)

## Ground Truth Reference
- Figures: 3
- Tables: 0
- References: 28