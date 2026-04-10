## Working title

Multi-modal deep learning for drug response prediction and biomarker discovery in cancer pharmacogenomics

## Core question

Can multi-modal deep learning that integrates genomics, proteomics, and other molecular profiling data improve drug response prediction in cancer cell lines and identify actionable biomarkers?

## Motivation / gap

- Patients with similar demographics and tumour types respond differently to the same drug regimens due to molecular variability
- Large-scale drug screening datasets (across molecularly profiled cancer cell lines) exist but current DRP methods have limited accuracy
- Deep learning outperforms traditional methods but still faces challenges in integrating multiple data modalities
- Biomarker discovery from DRP models is underexplored -- most work focuses on prediction accuracy alone

## Core contribution

- A multi-modal deep learning framework for drug response prediction (DRP) that integrates genomics, proteomics, and related molecular data
- Improved prediction performance over existing methods on large-scale drug screening datasets
- Systematic biomarker discovery pipeline leveraging learned model representations
- Demonstration that multi-modal integration captures complementary molecular signals missed by single-modality approaches

## Method in brief

- Integrate multi-modal molecular profiles (genomics, proteomics) of cancer cell lines with drug features
- Train deep learning architectures to predict drug response (e.g., IC50, AUC) for untested drug/cell-line combinations
- Benchmark against existing DRP methods on consortium screening datasets
- Extract and validate biomarkers from learned representations

## Target venue

Bioinformatics Advances
