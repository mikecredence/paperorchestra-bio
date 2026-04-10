# Idea Summary: Competitive interactions shape brain dynamics and computation across species

## Working title
Competitive interactions shape brain dynamics and computation across species

## Core question
AbstractAdaptive cognition relies on cooperation across anatomically distributed brain circuits. However, specialised neural systems are also in constant competition for limited processing resources. How does the brain’s network architecture enable it to balance these cooperative and competitive tendencies? Here we use computational whole-brain modelling to examine the dynamical and computational relevance of cooperative and competitive interactions in the mammalian connectome. Across human, mac

## Motivation / gap
- IntroductionA central goal of neuroscience is to understand how the architecture of the brain governs information processing.
- To support cognition, the brain must orchestrate the constant competition between specialised functional circuits, each arising from the cooperation of anatomically distributed regions 1–4.
- Spontaneous haemodynamics and electrodynamics provide evidence for both cooperative and antagonistic processes in the mammalian brain, exhibiting systematic and recurrent patterns of coordinated and a
- Although the behavioural and physiological relevance of functional anticorrelations is well establsihed, their mechanistic origin remains unclear 6.
- How does the brain orchestrate its cooperative and antagonistic tendencies?Interactions between brain regions unfold dynamically over a complex network of anatomical connections: the structural connec

## Core contribution (bullet form)
Extracted from abstract:
AbstractAdaptive cognition relies on cooperation across anatomically distributed brain circuits. However, specialised neural systems are also in constant competition for limited processing resources. How does the brain’s network architecture enable it to balance these cooperative and competitive tendencies? Here we use computational whole-brain modelling to examine the dynamical and computational relevance of cooperative and competitive interactions in the mammalian connectome. Across human, macaque, and mouse we show that the architecture of the models that most faithfully reproduce brain activity, consistently combines modular cooperative interactions with diffuse, long-range competitive interactions. The model with competitive interactions consistently outperforms the cooperative-only model, with excellent fit to both spatial and dynamical properties of the living brain, which were not explicitly optimised but rather emerge spontaneously. Competitive interactions in the effective connectivity produce greater levels of synergistic information and local-global hierarchy, and lead to superior computational capacity when used for neuromorphic computing. Altogether, this work provides a mechanistic link between network architecture, dynamical properties, and computation in the mammalian brain.

## Method in brief
Materials and MethodsHuman FMRI dataThe dataset of functional and structural neuroimaging data used in this work came from the Human Connectome Project (HCP, http://www.humanconnectome.org/), Release Q3 81,153. Per HCP protocol, all subjects gave written informed consent to the HCP consortium. These data contained fMRI and diffusion weighted imaging (DWI) acquisitions from 100 unrelated subjects of the HCP 900 data release81,153. All HCP scanning protocols were approved by the local Institutional Review Board at Washington University in St. Louis. Detailed information about the acquisition and imaging is provided in the dedicated HCP publications. Briefly: anatomical (T1-weighted) images were acquired in axial orientation, with FOV = 224 × 224 mm, voxel size 0.7 mm3 (isotropic), TR 2,400ms, TE 2.14ms, flip angle 8°. Functional MRI data (1200 volumes) were acquired with EPI sequence, 2 mm isotropic voxel size, TR 720ms, TE 33.1ms, flip angle 52°, 72 slices.Functional MRI preprocessing and denoisingWe used the minimally preprocessed fMRI data from the HCP, which includes bias field correction, functional realignment, motion correction, and spatial normalisation to Montreal Neurological Institute (MNI-152) standard space with 2mm isotropic resampling resolution. We also removed the first 10 volumes, to allow magnetisation to reach steady state. Additional denoising steps were performed using the CONN toolbox (http://www.nitrc.org/projects/conn), version 17f 154.To reduce noise d

## Target venue
Nature Neuroscience
