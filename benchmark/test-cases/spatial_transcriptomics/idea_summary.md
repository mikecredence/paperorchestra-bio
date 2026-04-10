## Working title

Systematic Benchmarking of High-Throughput Subcellular Spatial Transcriptomics Platforms

## Core question

How do the leading subcellular-resolution spatial transcriptomics platforms compare on key performance metrics when applied to the same clinical tissue samples?

## Motivation / gap

- Spatial transcriptomics technologies have rapidly improved in resolution and throughput, but no systematic head-to-head benchmarking exists using uniformly processed clinical samples.
- Researchers choosing between platforms lack standardized comparisons of sensitivity, specificity, diffusion control, and cell segmentation quality.
- Ground truth datasets (protein-level validation, matched scRNA-seq) are needed to properly evaluate platform performance but have not been generated alongside multi-platform spatial data.

## Core contribution

- Generate matched spatial transcriptomics data from serial sections of three cancer types (colon adenocarcinoma, hepatocellular carcinoma, ovarian cancer) across five platforms: Stereo-seq v1.3, Visium HD FFPE, Visium HD FF, CosMx 6K, Xenium 5K
- Establish ground truth with CODEX protein profiling and scRNA-seq on the same samples
- Perform manual cell segmentation and detailed annotations for rigorous evaluation
- Systematically assess capture sensitivity, specificity, diffusion control, and cell segmentation across all five platforms

## Method in brief

- Clinical samples from three cancer types, processed into serial tissue sections
- Spatial transcriptomics profiling on all five platforms using uniform sample preparation
- CODEX protein imaging on adjacent sections for all five platform comparisons
- scRNA-seq on matched samples for transcriptomic ground truth
- Manual cell segmentation and expert annotation
- Quantitative comparison across sensitivity, specificity, diffusion, and segmentation metrics

## Target venue

Nature Communications
