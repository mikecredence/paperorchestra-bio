{
  "statistical_sentences": [
    "Chavez-Badiola et al. employed the deep learning model ERICA to analyze 1,231 embryo images to predict ploidy status, achieving a 70% accuracy, with an area under the receiver operating characteristic curve (AUC) of 74%, and a sensitivity and specificity of 54% and 86% respectively.",
    "Notably, ERICA predicted a euploid embryo in the top rank in 79% of cases.",
    "The mean absolute error (MAE) between the MDBS and the ground truth Embryoscope BS scores is 1.855 \u00b1 0.03.",
    "Using the WCM-Embryoscope test set, BELA, when trained to distinguish between EUP and ANU, attained an AUC of 0.66 \u00b1 0.008, which rose to 0.76 \u00b1 0.002 upon inclusion of maternal age.",
    "In the EUP versus CxA task, the AUC of the model was 0.708 \u00b1 0.004 and increased to 0.826 \u00b1 0.004 with the inclusion of maternal age.",
    "In all tested scenarios (including or excluding age), test sets, and prediction tasks (EUP versus ANU and EUP versus CxA), BELA outperforms the day-5 video model (p < 0.05).",
    "Without including maternal age in ploidy prediction, the embryologist-annotated BS model surpasses BELA (p < 0.05) in all prediction tasks, barring EUP vs ANU on the WCM-Embryoscope test set (Figure 2a).",
    "However, with maternal age incorporated, BELA outperforms the embryologist-annotated blastocyst score model on the WCM-Embryoscope test set (p < 0.05).",
    "Notably, BELA significantly outperforms the day-5 video model in both scenarios \u2013 with and without the inclusion of maternal age (p < 0.05).",
    "This improved mapping could explain why BELA, with maternal age included, significantly outperforms the model trained on maternal age and embryologist-derived blastocyst score for the EUP vs ANU task (p < 0.05) (Figure 4).biorxiv;2023.08.31.555741v1/FIG4F4fig4Figure 4.Performances of BELA and traditional machine learning models on the Florida dataset.Average AUC with standard errors is shown for EUP versus ANU and EUP versus CxA prediction tasks on the Florida dataset for BELA and logistic regression models trained only on embryologist-derived BS and/or maternal age.In order to make the model available for clinical use, a web-based application named STORK-V for BELA was developed (Figure 5, Supplemental Figure 4).",
    "For example, a model trained on day-2 embryo development would use these parameters, start hr = 24.0 hpi, end hr = 48.0 hpi, and interval = 2 hrs.",
    "While attention mechanisms and multiple bidirectional LSTM layers were explored, they failed to enhance performance significantly (p > 0.05) across all tasks.",
    "Multitask BELA demonstrated a lower MAE (1.855 \u00b1 0.03) compared with a non-multitask BELA (1.877 \u00b1 0.027) on the WCM-Embryoscope test, supporting the use of multitasking.",
    "Logistic regression models demonstrated an average training time of 2.5 \u00b1 1.2 seconds, whereas BiLSTM models required 30.3 \u00b1 11 minutes.",
    "Inference for a single embryo on the STORK-V platform took 30 \u00b1 5 seconds."
  ],
  "methods_sentences": [
    "We resized each frame from 800 \u00d7 800 to 224 \u00d7 224."
  ],
  "table_count": 0
}