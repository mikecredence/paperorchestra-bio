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
