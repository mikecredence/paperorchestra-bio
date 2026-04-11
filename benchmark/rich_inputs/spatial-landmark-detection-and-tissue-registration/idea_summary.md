# Idea Summary: Spatial landmark detection and tissue registration with deep learning

## Working title
Spatial landmark detection and tissue registration with deep learning

## Core question
AbstractSpatial landmarks are crucial in describing histological features between samples or sites, tracking regions of interest in microscopy, and registering tissue samples within a common coordinate framework. Although other studies have explored unsupervised landmark detection, existing methods are not well-suited for histological image data as they often require a large number of images to converge, are unable to handle non-linear deformations between tissue sections, and are ineffective fo

## Motivation / gap


## Core contribution (bullet form)
Extracted from abstract:
AbstractSpatial landmarks are crucial in describing histological features between samples or sites, tracking regions of interest in microscopy, and registering tissue samples within a common coordinate framework. Although other studies have explored unsupervised landmark detection, existing methods are not well-suited for histological image data as they often require a large number of images to converge, are unable to handle non-linear deformations between tissue sections, and are ineffective for z-stack alignment, other modalities beyond image data, or multimodal data. We address these challenges by introducing a new landmark detection and registration method, utilizing neural-network-guided thin-plate splines. Our proposed method is evaluated on a diverse range of datasets, demonstrating superior performance in both accuracy and stability compared to existing approaches.

## Method in brief
MethodsHardwareWe used an NVIDIA A100-SXM 81GB graphics card, and 12 AMD EPYC 7742 64-Core Processors for all model training.Cost function: Multiscale Structural Similarity (MS-SSIM)In all the experiments detailed in the subsequent sections, we utilize a cost function rooted in the Multi-Scale Structural Similarity (MS-SSIM) method. This approach allows for a comprehensive assessment of image quality by considering image details across a range of resolutions. This method extends the single-scale SSIM index, which compares luminance, contrast, and structure of two aligned signals, such as image patches19. MS-SSIM has been very useful in our experiments since we have due to the presence of significant batch effects, and MS-SSIM have demonstrated more robustness than for instance Mean Squared Error in our experiments.The MS-SSIM procedure involves an iterative process of applying a low-pass filter to the image and downsampling the filtered image. Each iteration defines a new scale, culminating in the highest scale. Contrast and structure comparisons are computed at every scale, while luminance comparison is reserved for the highest scale19.The overall quality assessment in MS-SSIM combines these measurements from all scales, using adjustable parameters for accounting for the relative importance of each component at every scale. The method yields a detailed image quality map, with the mean MS-SSIM index offering an overall evaluation of image quality. For a comprehensive understa

## Target venue
Nature Methods
