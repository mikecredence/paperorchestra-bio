# Idea Summary

## Working title
Disseminating Cells in Human Oral Tumours Acquire an EMT Cancer Stem Cell State That Is Predictive of Metastasis

## Core question
Can we identify tumour cells that have undergone EMT and are actively disseminating from human oral cancer specimens, and does the presence of these cells predict metastatic disease?

## Motivation / gap
- The EMT-driven metastatic dissemination model has been built from mouse and cell line studies; it has not been directly observed in human tumour specimens in vivo
- Cancer cells undergoing EMT downregulate epithelial markers and become indistinguishable from surrounding mesenchymal stromal cells, making them invisible to standard analysis once they leave the tumour body
- Previous attempts to use combined epithelial+mesenchymal markers in human tumours were limited to characterizing cells still attached to the tumour body (earliest stages of EMT)
- EpCAM and CD24 have been identified as markers retained by a subset of EMT cancer stem cells (CSCs) with enhanced plasticity (ability to undergo MET), but their combined use for detecting disseminating cells in tissue sections has not been tested
- No study has demonstrated a predictive link between single disseminating EMT CSCs in human tumour specimens and metastatic outcome
- Pan-keratin is lost during EMT whereas EpCAM is retained, making EpCAM uniquely suited as a tumour lineage tracer in the stromal compartment

## Core contribution (bullet form)
- Developed an automated 4-colour immunofluorescent imaging and analysis protocol for entire histopathological slides, examining over 12,000 imaging fields from 84 human oral cancer specimens
- Showed that EpCAM+Vimentin+CD24+ triple-positive cells identify EMT CSCs: enriched to 41% in EMT-stem sub-line vs. 2.1% in parental CA1 line, absent in normal keratinocytes and cancer-associated fibroblasts
- Found significant enrichment of single EpCAM+Vim+CD24+ cells disseminating beyond the tumour body in metastatic specimens compared to non-metastatic specimens
- Demonstrated that EpCAM+CD24-Vim+ cells in the stroma do NOT correlate with metastasis, highlighting the specific importance of the CD24+ plasticity marker
- Trained an artificial neural network that predicts metastasis with cross-validated accuracy of 87-89% using the three-marker staining profile
- Pan-keratin+Vim+CD24+ staining fails to identify disseminating EMT CSCs and shows no enrichment in EMT-stem sub-line, confirming EpCAM retention is a specific feature of this state

## Method in brief
Immunofluorescent 4-colour staining (EpCAM, Vimentin, CD24, plus DAPI nuclear stain) was applied to formalin-fixed paraffin-embedded oral squamous cell carcinoma specimens. An automated imaging system captured entire slides, and image segmentation was performed to identify individual cells and quantify marker co-expression. An EpCAM density map was generated to separate the tumour body from the surrounding stroma, enabling specific quantification of disseminating cells in the stromal compartment.

For validation, the protocol was first tested on the CA1 OSCC cell line and its EMT-stem derivative sub-line. A parallel staining with pan-keratin replacing EpCAM served as a negative control. Two batches of tumour specimens (84 total), stratified by metastatic status, were analysed. A supervised machine learning approach using an artificial neural network was trained on grey-level intensities of the three markers in imaging tiles from batch 1, with 10-fold cross-validation. The model was additionally validated on batch 2 as an independent test set.

## Target venue
eLife
