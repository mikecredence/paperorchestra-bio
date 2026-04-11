# Idea Summary: Automatic Ploidy Prediction and Quality Assessment of Human Blastocyst Using Time-Lapse Imaging

## Working title
Automatic Ploidy Prediction and Quality Assessment of Human Blastocyst Using Time-Lapse Imaging

## Core question
AbstractAssessing fertilized human embryos is crucial for in vitro-fertilization (IVF), a task being revolutionized by artificial intelligence and deep learning. Existing models used for embryo quality assessment and chromosomal abnormality (ploidy) detection could be significantly improved by effectively utilizing time-lapse imaging to identify critical developmental time points for maximizing prediction accuracy. Addressing this, we developed and compared various embryo ploidy status predictio

## Motivation / gap
- IntroductionSince the advent of in vitro fertilization (IVF) in 1978, it has served as a key solution for individuals unable to conceive naturally, accounting for over 8 million successful births glob
- A critical determinant of IVF success and minimizing risk of perilous multiple pregnancies lies in the selection of high-quality, single normal embryos, primarily influenced by their ploidy status.2,3
- Euploid embryos, characterized by normal chromosomal counts, typically lead to successful pregnancies, while aneuploid embryos—those with chromosomal aberrations—are associated with miscarriage, faile
- Embryo aneuploidy, which leads to increased miscarriage rates, correlates with advanced maternal age.Currently, preimplantation genetic testing for aneuploidy (PGT-A) is used to ascertain embryo ploid
- This procedure requires a biopsy of trophectoderm (TE) cells, whole genome amplification of their DNA, and testing for chromosomal copy number variations.

## Core contribution (bullet form)
Extracted from abstract:
AbstractAssessing fertilized human embryos is crucial for in vitro-fertilization (IVF), a task being revolutionized by artificial intelligence and deep learning. Existing models used for embryo quality assessment and chromosomal abnormality (ploidy) detection could be significantly improved by effectively utilizing time-lapse imaging to identify critical developmental time points for maximizing prediction accuracy. Addressing this, we developed and compared various embryo ploidy status prediction models across distinct embryo development stages. We present BELA (Blastocyst Evaluation Learning Algorithm), a state-of-the-art ploidy prediction model surpassing previous image- and video-based models, without necessitating subjective input from embryologists. BELA uses multitask learning to predict quality scores that are used downstream to predict ploidy status. By achieving an AUC of 0.76 for discriminating between euploidy and aneuploidy embryos on the Weill Cornell dataset, BELA matches the performance of models trained on embryologists’ manual scores. While not a replacement for preimplantation genetic testing for aneuploidy (PGT-A), BELA exemplifies how such models can streamline the embryo evaluation process, reducing time and effort required by embryologists.

## Method in brief
Materials & MethodsThe research utilized multiple datasets for training and validation of the machine learning models. The first dataset, known as the WCM-Embryoscope data, was collected from the Center for Reproductive Medicine at Weill Cornell Medicine between 2018 and 2019. It comprises time-lapse images and PGT-A results for 1,998 embryos, including 494 single aneuploid (SA), 588 complex aneuploid (CxA), and 916 euploid (EUP) embryos. A total of 498 patients were included in the WCM-Embryoscope data with an average of four biopsied embryos each. We treated each sample independently irrespective of parental origin. Accompanying the time-lapse sequences were clinical data such as embryologist-derived blastocyst score (BS), morphokinetic parameters, and maternal age at the time of oocyte retrieval. The blastocyst score is the sum of a set of scores converted from the expansion, inner cell mass (ICM), trophectoderm (TE) grades, and day of blastocyst formation.14 The blastocyst score ranges from 3 to 14, with a lower number indicating a higher-quality embryo. The images were captured using the Embryoscope® imaging instrument. To validate the models’ generalizability, we used a second dataset, referred to as the WCM-Embryoscope+ data, which was also collected from the Center for Reproductive Medicine. However, these were gathered between 2019 and 2020 and included a total of 841 embryos (170 SA, 261 CxA, and 410 EUP), using a newer Embryoscope+® instrument. Similar to the first

## Target venue
Nature Communications
