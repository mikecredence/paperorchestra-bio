# Experimental Log: Spatial landmark detection and tissue registration with deep learning

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsBenchmarking ELD against existing methodsOne can design a deep neural network to better generalize for small datasets by adding constraints to the model, such as reducing the neuron count per layer, decreasing the number of layers, implementing dropout, or adding a regularizer to the loss fun
- In ELD, we constrain the solution space by removing the generative network while retaining the landmark-detecting network, as suggested by Sanchez et al.8.
- With the image landmarks identified, registration can be easily performed using landmark-based methods, such as homography11 or thin-plate spline (TPS)12.
- These methods offer several advantages, including having fewer unlearnable parameters (hard constraints) and being more computationally efficient than large deep neural networks.The process of aligning tissue slices to a common coordinate framework (CCF) can be outlined as follows (Figure 1a): To be
- As a final step, ELD projects all the aligned tissue regions onto a CCF, facilitating comparative studies across various slices.biorxiv;2023.08.24.554614v1/FIG1F1fig1Figure 1:Overview of ELD framework and performance assessment.(a) Proposed workflow of acquiring spatial landmarks and aligning sectio
- Figures show the time required for convergence in minutes as a function of the number of genes or color channels used when the number of landmarks is set to 10 (f) and as a function of the number of landmarks used when the number of channels is set to 3 (g).In this study, we employ standard error me
- These metrics include forward error, backward error, and consistency error8.
- To calculate the consistency error, one must: 1) detect the landmarks in the image, apply an affine transformation to the landmarks, 2) apply the same affine transformation to the image, and then detect the landmarks again but on the transformed image.
- ELD exhibits superior consistency compared to other methods (Figure 1b).
- Interestingly, a closer examination of the results reveals that the performance difference is largely attributed to the other methods’ tendency to identify landmarks that are sometimes significantly misaligned (Figure 1c).
- On the other hand, a model that has a low backward error but high forward error is likely to converge to a fixed set of points independent of the input image.ELD exhibits significantly better backward error than other methods (Figure 1d), which can be attributed to the inconsistent landmarks found b
- Although all models show better performance in forward error than backward error, ELD displays marginally worse performance in forward error (Figure 1e).
- This indicates that ELD sacrifices some generalization in favor of significantly improved consistency.We conducted two tests to evaluate ELD’s runtime requirements: one with varying numbers of genes or image channels (Figure 1f) and another with varying numbers of landmarks (Figure 1g).
- As detailed in the methods section, the convergence criterion is quite stringent; however, convergence is typically achieved more quickly in real-world applications.Performance Evaluation on Single-modality DataAn effective registration method for Visium data, Eggplant13, is currently openly availab
- Using Eggplant to transfer the gene expression of three target genes with distinct expression patterns (Nrgn, Apoe, and Omp) in the mouse olfactory bulb to a reference section using either manually or automatically detected landmarks, we find that the landmarks produced by ELD yield results that are
- For this experiment, we used 12 mouse olfactory bulb samples, the same reference as employed in Eggplant13.
- Our results are consistent whether landmarks were identified using histology or expression data from 3 or 100 genes.biorxiv;2023.08.24.554614v1/FIG2F2fig2Figure 2:Performance on single-modality data.(a) Landmarks identified by ELD when trained on various modalities, such as histology and Visium data
- The rightmost image, which includes 100 genes, is visualized using PCA; however, all genes were utilized during the training process.
- For all experiments, 14 landmarks were used.
- Salas et al.14 to demonstrate ELD’s compatibility with ISS data.
- In this experiment, we employ RGB images of the clustering on the ISS data (Figure 2e) and use TPS for the final registration.
- Comparing ELD to STAlign15, which has shown promising results for aligning data from ISS experiments, we find that ELD attains a higher accuracy in both replicates (Figure 2d).3D modelingTo make it possible to align a stack of multiple tissue sections, whose morphology may change drastically along t
- The general procedure is illustrated in Figure 3a.
- This forces the landmarks to act more like anchor points with fixed x-y coordinates instead of identifying common morphology, as demonstrated in Figure 3c.biorxiv;2023.08.24.554614v1/FIG3F3fig3Figure 3:3D tissue reconstruction with ELD(a) Illustration of the 3D modeling process.
- A total of 20 landmarks were used for the alignment.
- All results are normalized using the value obtained when aligning with manual landmarks (corresponding to a score of 1).
- (e) Absolute error between manual alignment and alignment using ELD across four sections in the z-stackTo assess ELD’s 3D alignment performance, we utilize a mouse prostate dataset containing 260 slices from K.
- Kartasalo et al.16 The dataset contains annotations from two different annotators of four corresponding landmarks in each pair of consecutive sections.
- The mean of TRE and ATRE is used, and it’s normalized by the score obtained when registering with manually annotated landmarks, as depicted in Figure 3d.
- The final 3D alignment is illustrated in Figure 3b.Performance Evaluation on Multimodal DataELD can detect landmarks and align tissue data from different modalities.
- During training, random samples from both modalities are selected, one sample is registered to the other, and their alignment is assessed in the latent space obtained from the landmark detector (Figure 4a).biorxiv;2023.08.24.554614v1/FIG4F4fig4Figure 4:Benchmarking ELD for multimodal alignment.(a) R
- The upper-left image shows MYH6, ELN, and MYH7 gene expression.
- In total, 16 landmarks were used for this experiment.
- d) PCA visualization of MSI and Visium data with their respective landmarks.We used the Human Developing Heart dataset13, which consists of four samples, to demonstrate ELD’s ability to align tissues from two different modalities.
- Histology images were used for the first two samples, while the genes MYH6, ELN, and MYH7 from Visium expression data were employed to construct an image for the other samples.
- The detected landmarks for the two modalities are displayed (Figure 4b).To benchmark ELD’s performance, we randomly selected one of the samples as reference.
- The programmatically detected landmarks perform comparably to manually annotated landmarks (Figure 4b-c).To further demonstrate the flexibility of ELD to model data of diverse modalities, we apply it to PCA embeddings of MSI and Visium data.
- We find the generated landmarks to be qualitatively consistent across sections and to mark out biologically relevant anatomical features (Figure 4d).

## Figure Descriptions

### Figure 1:
Overview of ELD framework and performance assessment.(a) Proposed workflow of acquiring spatial landmarks and aligning sections within a common coordinate framework. The process can be divided into the following steps: i) Obtain two different sections, A and B, for which we want to identify landmark

### Figure 2:
Performance on single-modality data.(a) Landmarks identified by ELD when trained on various modalities, such as histology and Visium data, alongside an image with manual annotation for comparison. The rightmost image, which includes 100 genes, is visualized using PCA; however, all genes were utilize

### Figure 3:
3D tissue reconstruction with ELD(a) Illustration of the 3D modeling process. First, i) randomly select a reference from the tissue stack, choose a tissue, and create a noisy counterpart to map to the reference. Next, detect landmarks ii) for the reference and both the source tissue and its noisy co

### Figure 4:
Benchmarking ELD for multimodal alignment.(a) Registration of multimodal data, overview. i) Each modality, A and B, is passed through its respective landmark detector, and a latent representation of modality A is saved. ii) Landmarks are extracted from the heatmaps, and the two modalities’ samples a

## References
Total references in published paper: 17

### Key References (from published paper)
- Spatial mapping of metals in tissue-sections using combination of mass-spectrometry and histology th (, 2017)
- Label-free 3D-CLEM Using Endogenous Tissue Landmarks (, 2018)
- Toward a Common Coordinate Framework for the Human Body (, 2019)
- Scalable tissue labeling and clearing of intact human organs (, 2022)
- Identifying biological landmarks using a novel cell measuring image analysis tool: Cell-o-Tape (, 2012)
- Learning Deep Representation for Face Alignment with Auxiliary Attributes (, 2016)
- Object landmark discovery through unsupervised adaptation (, 2019)
- Unsupervised learning of object landmarks through conditional image generation (, 2018)
- A Comparison of Regularization Techniques in Deep Neural Networks (, 2018)
- Thin plate spline interpolation (, 2019)
- A Landmark-based Common Coordinate Framework for Spatial Transcriptomics Data (, 2021)
- Optimizing Xenium In Situ data utility by quality assessment and best practice analysis workflows (, 2023)
- Alignment of spatial transcriptomics data using diffeomorphic metric mapping (, 2023)
- Comparative analysis of tissue reconstruction algorithms for 3D histology (, 2018)
- CODA: quantitative 3D reconstruction of large tissues at cellular resolution (, 2022)
- Spatial Multimodal Analysis of Transcriptomes and Metabolomes in Tissues (, 2023)
- Multiscale structural similarity for image quality assessment (, 2003)

## Ground Truth Reference
- Figures: 4
- Tables: 0
- References: 17