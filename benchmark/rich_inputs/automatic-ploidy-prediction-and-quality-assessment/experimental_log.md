# Experimental Log: Automatic Ploidy Prediction and Quality Assessment of Human Blastocyst Using Time-Lapse Imaging

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- Two internal datasets from Weill Cornell Medicine’s Center for Reproductive Medicine (WCM) were employed: the first encompassed 1,998 Embryoscope® time-lapse sequences, and the second contained 841 sequences from the Embryoscope+®.
- These sequences typically constituted 360-420 distinct frames, captured at 0.3-hour intervals over five days of development.
- BS encompasses three sub-components: inner cell mass (ICM), trophectoderm (TE), and expansion score.14 This blastocyst score formulation has been shown to be predictive of implantation success, euploidy, and live-birth.14 For additional model validation, we utilized an external dataset from IVI Vale
- Comprehensive descriptions of these datasets are detailed in Table 1, Supplemental Table 10, and further expounded in the Methods section.biorxiv;2023.08.31.555741v1/TBL1T1tbl1Table 1.Characteristics of Datasets.The sample size, distribution of data across ploidy classes, and additional clinical fea
- First, BELA predicts the Blastocyst Score (BS) from processed day-5 time-lapse videos (96 -112 hpi), a timeframe chosen based on our ablation analyses comparing embryonic development timepoints and image versus video inputs (Supplemental Text 1).
- The input video undergoes processing and transformation into feature vectors via a pre-trained spatial feature extraction model (Figure 1, steps 1 - 4).
- In the second step, BELA uses the now ‘model-derived blastocyst score’ (MDBS) to predict the embryo’s ploidy status, employing a logistic regression that integrates maternal age as a continuous input feature, as illustrated in Figure 1.
- The first baseline is a day-5 video model which exclusively uses time-lapse input from 96 - 112 hpi to directly predict ploidy status using a BiLSTM architecture.
- The second baseline is an embryologist-annotated model which uses only the ground-truth BS to predict ploidy status using a logistic regression.biorxiv;2023.08.31.555741v1/FIG1F1fig1Figure 1.Overview of BELA development.Features are extracted from time-lapse image frames as shown in steps 1-4.
- 512-dimensional features are extracted for each time-lapse image using a pretrained VGG16 architecture.
- As depicted in Supplemental Figure 1, both the training and test sets from WCM-Embryoscope show a moderate correlation (Pearson correlation >0.7) between the model-derived blastocyst scores (MDBS) and the embryologist BS.
- This moderate correlation is also evident in the predicted and actual scores of other embryologist metrics (Supplemental Figure 2).
- The mean absolute error (MAE) between the MDBS and the ground truth Embryoscope BS scores is 1.855 ± 0.03.
- Using the WCM-Embryoscope test set, BELA, when trained to distinguish between EUP and ANU, attained an AUC of 0.66 ± 0.008, which rose to 0.76 ± 0.002 upon inclusion of maternal age.
- In the EUP versus CxA task, the AUC of the model was 0.708 ± 0.004 and increased to 0.826 ± 0.004 with the inclusion of maternal age.
- Comprehensive performance metrics of BELA are found in Supplemental Table 1.
- BELA’s performance (in orange), compared with a day-5 Video model and the embryologist-annotated blastocyst score model, is illustrated in Figure 2.
- In all tested scenarios (including or excluding age), test sets, and prediction tasks (EUP versus ANU and EUP versus CxA), BELA outperforms the day-5 video model (p < 0.05).
- Without including maternal age in ploidy prediction, the embryologist-annotated BS model surpasses BELA (p < 0.05) in all prediction tasks, barring EUP vs ANU on the WCM-Embryoscope test set (Figure 2a).
- However, with maternal age incorporated, BELA outperforms the embryologist-annotated blastocyst score model on the WCM-Embryoscope test set (p < 0.05).
- Still, it underperforms in comparison to the embryologist-annotated blastocyst score model on the WCM-Embryoscope+ dataset.biorxiv;2023.08.31.555741v1/FIG2F2fig2Figure 2.Comparison of BELA models with other models.Mean AUC scores and standard deviation for day-5 video, BELA, and embryologist-annotat
- (b) Performances of models with maternal age.The performance of the BELA was compared with a day-5 video model using an external dataset from Spain, consisting of 543 embryos (Figure 3, Supplemental Table 1).
- Notably, BELA significantly outperforms the day-5 video model in both scenarios – with and without the inclusion of maternal age (p < 0.05).
- Unlike the embryos from Weill Cornell Medicine (WCM-Embryoscope and WCM-Embryoscope+ datasets), those from the Spanish dataset were artificially hatched on day 3, which likely impacted later blastocyst morphology and morphokinetics.
- To quantitatively verify these differences, feature encodings were extracted using the pre-trained feature extractor for each frame (between 96 hpi and 112 hpi) of each embryo.
- The resulting feature encodings, categorized by dataset, can be viewed in Supplemental Figure 3.
- For example, in Spain, IVF is more affordable and accessible due to different healthcare insurance policies, whereas in the United States, the high cost of IVF can limit its accessibility to individuals with the necessary financial resources.15,16 This likely contributes to the different maternal ag
- Blue bars depict model performances of day-5 video models, whereas orange bars depict performances of BELA models.The performance of BELA was further assessed using an external dataset from IVF Florida, comprising 869 embryos.
- This decrease in performance could be attributed to the weak correlations between blastocyst score, maternal age, and ploidy within the Florida dataset (Supplemental Table 8).
- Moreover, the embryologist-derived blastocyst scores in the Florida dataset were predominantly centered around a score of 7, thereby reducing the granularity that made it a potent predictor of ploidy in other datasets.
- This lack of granularity within the Florida dataset might be a result of different scoring practices, as IVF Florida evaluates blastocysts at 115 and 144 hpi, in contrast with the methods employed at Weill Cornell, which also utilize earlier time points for determining blastocyst score.
- Interestingly, the model-derived blastocyst score (MDBS) from the first module of BELA shows a stronger correlation (−0.119) with ploidy status than the embryologist-derived blastocyst score (−0.101).
- In order to further validate this hypothesis, an embryologist at Weill Cornell re-graded the 50 embryos within the Florida dataset where the MDBS deviated most significantly from the provided Florida blastocyst scores.
- We observed a decrease in mean absolute error (MAE) between the MDBS versus the re-graded blastocyst score from Weill Cornell (4.16) and the MDBS versus the original Florida blastocyst score (5.02).
- This improved mapping could explain why BELA, with maternal age included, significantly outperforms the model trained on maternal age and embryologist-derived blastocyst score for the EUP vs ANU task (p < 0.05) (Figure 4).biorxiv;2023.08.31.555741v1/FIG4F4fig4Figure 4.Performances of BELA and tradit
- The required input for the prediction includes time-lapse images captured between 96 and 112 hpi, and the maternal age.
- This will help medical professionals make more informed decisions regarding embryo selection and ultimately improve IVF success rates.biorxiv;2023.08.31.555741v1/FIG5F5fig5Figure 5.STORK-V web interface.A clinical tool that utilizes automation to assist embryologists in determining both the embryo q

## Tables

### Table 1.
> Characteristics of Datasets.The sample size, distribution of data across ploidy classes, and additional clinical features for each dataset are shown.


## Figure Descriptions

### Figure 1.
Overview of BELA development.Features are extracted from time-lapse image frames as shown in steps 1-4. Time-lapse images are both temporally and spatially processed to decrease bias. Horizontal and rotational augmentation is performed on time-lapse sequences. 512-dimensional features are extracted 

### Figure 2.
Comparison of BELA models with other models.Mean AUC scores and standard deviation for day-5 video, BELA, and embryologist-annotated BS trained models are shown. Performances are shown on both the WCM-Embryoscope and WCM-Embryoscope+ dataset for both prediction tasks. (a) Performances of models with

### Figure 3.
Performances of day-5 video model and BELA on the Spain dataset.Average AUC with standard errors is shown for all EUP vs ANU prediction tasks on the Spain dataset for both the day-5 video model and BELA. Blue bars depict model performances of day-5 video models, whereas orange bars depict performanc

### Figure 4.
Performances of BELA and traditional machine learning models on the Florida dataset.Average AUC with standard errors is shown for EUP versus ANU and EUP versus CxA prediction tasks on the Florida dataset for BELA and logistic regression models trained only on embryologist-derived BS and/or maternal 

### Figure 5.
STORK-V web interface.A clinical tool that utilizes automation to assist embryologists in determining both the embryo quality score and ploidy status, providing a comprehensive assessment of the embryo.

## References
Total references in published paper: 24

### Key References (from published paper)
- Assisted Reproduction Technology and long-term Cardiometabolic Health in The offspring (, 2021)
- Human pre-implantation embryo development (, 2012)
- Forty years of IVF (, 2018)
- Preimplantation Genetic Testing: Where We Are Today (, 2020)
- The Pregnancy Outcome of Mosaic Embryo Transfer: A Prospective Multicenter Study and Meta-Analysis (, 2020)
- Deep learning enables robust assessment and selection of human blastocysts after in vitro fertilizat (, 2019)
- Embryo Ranking Intelligent Classification Algorithm (ERICA): artificial intelligence clinical assist (, 2020)
- A non-invasive artificial intelligence approach for the prediction of human blastocyst ploidy: a ret (, 2023)
- Data-Driven Prediction of Embryo Implantation Probability Using IVF Time-lapse Imaging (, 2020)
- End-to-end deep learning for recognition of ploidy status using time-lapse videos (, 2021)
- Assessment of human embryo development using morphological criteria in an era of time-lapse, algorit (, 2016)
- Modelling a risk classification of aneuploidy in human embryos using non-invasive morphokinetics (, 2013)
- No evidence of association between blastocyst aneuploidy and morphokinetic assessment in a selected  (, 2015)
- Blastocyst score, a blastocyst quality ranking tool, is a predictor of blastocyst ploidy and implant (, 2020)
- Female age and assisted Reproductive Technology (, 2018)
- Reproductive genetics laboratory may impact euploid blastocyst and live birth rates: a comparison of (, 2023)
- Preimplantation genetic testing for aneuploidy versus morphology as selection criteria for single fr (, 2019)
- A deep learning-based approach for inappropriate content detection and classification of YouTube vid (, 2022)
- Optimized NGS Approach for Detection of Aneuploidies and Mosaicism in PGT-A and Imbalances in PGT-SR (, 2020)
- Multitask Learning (, 1997)
- Correlation between aneuploidy, standard morphology evaluation and morphokinetic development in 1730 (, 2016)
- Previously reported and here added cases demonstrate euploid pregnancies followed by PGT-A as”mosaic (, 2023)
- On the reproductive capabilities of aneuploid human preimplantation embryos (, 2022)
- National mosaic embryo transfer practices: a survey (, 2018)

## Ground Truth Reference
- Figures: 5
- Tables: 1
- References: 24