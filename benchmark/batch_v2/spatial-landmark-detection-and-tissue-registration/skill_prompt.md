Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Nature Methods

## Idea Summary

# Idea Summary

## Working title
Spatial Landmark Detection and Tissue Registration with Deep Learning

## Core question
Can an unsupervised deep learning method detect spatial landmarks and register tissue sections across diverse modalities, handling small datasets and nonlinear deformations typical of spatial omics and histological data?

## Motivation / gap
- Spatial landmarks are crucial for comparing histological features, tracking ROIs, and registering tissue to common coordinate frameworks
- Existing unsupervised landmark detection methods require large datasets (100,000+ images), cannot handle nonlinear elastic deformations, and fail for multimodal data
- Manual annotation is labor-intensive and creates a bottleneck for large-scale spatial omics experiments
- Multi-omics studies often have fewer than 10 samples, making deep learning overfitting a major concern
- No existing method simultaneously handles single-modality registration, 3D z-stack alignment, and multimodal data alignment

## Core contribution (bullet form)
- Introduced ELD (Effortless Landmark Detection) using neural-network-guided thin-plate splines (TPS), removing the generative network to reduce overfitting on small datasets
- Achieved superior consistency error and backward error on MAFL and AFLW face landmark benchmarks compared to two state-of-the-art models
- Demonstrated faster convergence: runtime scales linearly with number of genes/channels and landmarks, with 10 landmarks converging in minutes
- Outperformed manual annotation with Eggplant and STAlign for single-modality Visium, H&E, and ISS data registration
- Improved ATRE metric for mouse prostate 3D reconstruction compared to 8 competing registration models
- Successfully aligned multimodal data (gene expression + histology) using separate landmark detectors with latent space similarity optimization

## Method in brief
ELD uses a landmark detection neural network without a generative component, constrained to prevent overfitting on small datasets. The network identifies landmarks on tissue sections, and TPS (thin-plate splines) performs nonlinear registration based on detected landmarks. The cost function uses Multi-Scale Structural Similarity (MS-SSIM) for robustness to batch effects. Landmark drop-out (p=10%) prevents local minima where landmarks cluster. Cropping handles missing regions from data augmentation.

For 3D reconstruction, ELD produces anchor points rather than landmarks, using a combination of TPS and rigid transformation with a noise-augmented reference scheme. For multimodal alignment, separate landmark detectors are trained for each modality, and registration similarity is optimized in a latent tissue space. All experiments used an NVIDIA A100-SXM 81GB GPU with 12 AMD EPYC 7742 processors. The PIQA package computed MS-SSIM with default parameters and window size 5.

## Target venue
Nature Methods


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the ELD spatial landmark detection study.

---

## Method Configuration

| Parameter | Value |
|-----------|-------|
| Cost function | Multi-Scale Structural Similarity (MS-SSIM) |
| Registration method | Thin-plate splines (TPS) |
| Landmark drop-out probability | 10% |
| MS-SSIM window size | 5 |
| MS-SSIM package | PIQA (PyTorch Image Quality Assessment) |
| Hardware | NVIDIA A100-SXM 81GB; 12x AMD EPYC 7742 64-Core |
| Default landmarks | 14 (for benchmarks) |

---

## Experiment 1: Face Landmark Benchmarks (MAFL and AFLW)

| Metric | ELD | Competitor 1 | Competitor 2 |
|--------|-----|-------------|-------------|
| Mean consistency error (distribution) | Superior (lower) | Higher | Higher |
| Per-landmark consistency error | More uniform | Variable | Variable |
| Backward error (per image) | Superior (lower) | Higher | Higher |
| Forward error (per image) | Marginally worse | Better | Similar |

Fig. 1b: Distribution of mean consistency error per image across three models.
Fig. 1c: Consistency error per individual landmark.
Fig. 1d: Backward error distribution per image.
Fig. 1e: Forward error distribution per image.

---

## Experiment 2: Runtime Analysis

| Variable Tested | Fixed Parameter | Scaling Behavior |
|----------------|----------------|-----------------|
| Number of genes/channels (1-100+) | 10 landmarks | Linear scaling (minutes) |
| Number of landmarks (5-50) | 3 channels | Linear scaling (minutes) |

Fig. 1f: Runtime vs number of genes/channels with 10 landmarks.
Fig. 1g: Runtime vs number of landmarks with 3 channels.

---

## Experiment 3: Single-Modality Registration

### Visium Data

| Method | Correlation (Nrgn) | Correlation (Apoe) | Correlation (Omp) |
|--------|-------------------|--------------------|--------------------|
| ELD (14 landmarks) | Higher | Higher | Higher |
| Manual annotation | Moderate | Moderate | Moderate |
| Unregistered | Low | Low | Low |

### H&E Histology

| Method | Registration Quality |
|--------|---------------------|
| ELD | Good alignment |
| STAlign | Comparable |
| Manual Eggplant | Comparable but labor-intensive |

### ISS (In Situ Sequencing)

| Method | Registration Quality |
|--------|---------------------|
| ELD | Good alignment |
| Competitor methods | Variable |

Fig. 2a: Landmarks identified by ELD on various modalities with manual annotation comparison.
Fig. 2b: Violin plots of target gene correlations between registered samples and reference.

---

## Experiment 4: 3D Tissue Reconstruction (Mouse Prostate)

| Method | ATRE Metric |
|--------|-------------|
| ELD | Significantly improved |
| Model 1 (of 8 competitors) | Lower performance |
| Model 2 | Lower performance |
| Model 3 | Lower performance |
| Model 4 | Lower performance |
| Model 5 | Lower performance |
| Model 6 | Lower performance |
| Model 7 | Lower performance |
| Model 8 | Lower performance |

Fig. 3a: Illustration of 3D modeling process with reference selection, noise augmentation, landmark detection, and TPS+rigid transformation.

---

## Experiment 5: Multimodal Alignment

| Modality A | Modality B | Alignment Method | Result |
|-----------|-----------|-----------------|--------|
| Gene expression (Visium) | H&E histology | Separate landmark detectors + latent space | Successful alignment |
| Gene expression | Mass spectrometry imaging | Separate detectors + latent space | Demonstrated |

Fig. 4a: Multimodal registration overview with separate detectors and latent representations.
Fig. 4b: Detected landmarks for gene expression and histology modalities.

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Remove generative network | Reduces parameters; prevents overfitting on small datasets |
| Use TPS (not homography) | Handles elastic/nonlinear deformations in tissue |
| MS-SSIM cost function | Robust to batch effects; better than MSE |
| Landmark drop-out | Prevents landmark clustering in local minima |
| Separate detectors for multimodal | Each modality has distinct features requiring specialized detection |

---

## Datasets Used

| Dataset | Modality | Application |
|---------|----------|------------|
| MAFL | Face images | Benchmark evaluation |
| AFLW | Face images | Benchmark evaluation |
| Visium spatial transcriptomics | Gene expression + histology | Single-modality registration |
| H&E histology | Tissue images | Single-modality and multimodal |
| ISS | In situ sequencing | Single-modality registration |
| Mouse prostate z-stack | Serial sections | 3D reconstruction |
| Mass spectrometry imaging | Spatial metabolomics | Multimodal alignment |

---

## Error Metrics Definitions

| Metric | Description |
|--------|-------------|
| Consistency error | Deviation of landmarks after forward-backward registration cycle |
| Backward error | Error when mapping from target back to source |
| Forward error | Error when mapping from source to target |
| ATRE | Average tissue registration error for 3D reconstruction |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | ELD framework overview; superior consistency and backward error on face benchmarks; efficient runtime |
| Fig. 2 | Single-modality performance across Visium, H&E, ISS; outperforms manual annotation |
| Fig. 3 | 3D reconstruction with improved ATRE vs 8 competitors on mouse prostate |
| Fig. 4 | Multimodal alignment using separate detectors and latent space optimization |

---

## Reference Count
17 references cited.

