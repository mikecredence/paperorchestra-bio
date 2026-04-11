## Working title
BELA: A Multitask Deep Learning Model for Automated Embryo Ploidy Prediction from Time-Lapse Imaging

## Core question
Can a fully automated deep learning pipeline predict embryo ploidy status (euploid vs. aneuploid) from time-lapse imaging sequences without requiring subjective embryologist annotations, and how does it compare to models trained on manual scores?

## Motivation / gap
- IVF success depends heavily on selecting euploid embryos, but current gold standard (PGT-A) is costly, invasive, and time-consuming
- PGT-A accuracy can be compromised by embryonic mosaicism, leading to false results
- Existing deep learning models (ERICA: AUC 0.74; others at ~0.61-0.70) rely on single images or subjective embryologist input
- No prior model effectively leveraged time-lapse video to identify optimal developmental time points for maximizing ploidy prediction
- Prior work did not systematically compare image vs. video inputs across different embryo development stages
- Need for a model that provides explainability through intermediate morphological scores while remaining fully automated

## Core contribution (bullet form)
- Developed BELA (Blastocyst Evaluation Learning Algorithm) achieving AUC of 0.76 for euploid vs. aneuploid discrimination on the Weill Cornell dataset, matching models trained on embryologist manual scores
- BELA uses multitask learning (predicting ICM, TE, expansion, and blastocyst scores simultaneously) as a proxy for ploidy classification, requiring only day-5 video (96-112 hpi) and maternal age
- Systematic ablation analysis comparing image vs. video inputs across development stages identified day-5 video as optimal
- Validated on four datasets: WCM-Embryoscope (1,998 embryos), WCM-Embryoscope+ (841), Spain-IVI Valencia (543), and Florida-IVF Florida (869)
- Single aneuploid embryos were predicted roughly evenly as euploid or complex aneuploid by the EUP vs. CxA model, suggesting they morphologically resemble both categories
- Deployed as STORK-V clinical web interface for embryologist workflow integration

## Method in brief
BELA operates in two stages. First, time-lapse video frames from day 5 (96-112 hours post-insemination) are processed through a pretrained VGG16 architecture to extract 512-dimensional feature vectors for each frame. These features are fed into a multitask BiLSTM (bidirectional long short-term memory) network that simultaneously predicts blastocyst score components: inner cell mass (ICM) grade, trophectoderm (TE) grade, expansion score, and overall blastocyst score. Temporal and spatial processing, along with horizontal and rotational augmentation, are applied to reduce bias.

In the second stage, the model-derived blastocyst score (MDBS) from stage one is combined with maternal age as continuous input features in a logistic regression classifier to predict ploidy status (euploid vs. aneuploid, or euploid vs. complex aneuploid). The blastocyst score ranges from 3 to 14, with lower values indicating higher-quality embryos. Performance is evaluated using mean absolute error for score prediction and AUC for ploidy classification, compared against day-5 video-only models and models trained on embryologist-annotated blastocyst scores.

## Target venue
Nature Communications
