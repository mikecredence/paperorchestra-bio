# Idea Summary

## Working title
Deciphering the Genetic Code of Neuronal Type Connectivity Through Bilinear Modeling

## Core question
Can a bilinear model inspired by recommendation systems link single-cell transcriptomic gene expression profiles of pre- and postsynaptic neurons to their anatomical connectivity, thereby revealing the genetic rules governing synaptic specificity?

## Motivation / gap
- The genetic mechanisms dictating specific connections between neuronal types remain poorly understood, especially in complex brain structures
- Single-cell transcriptomics and connectomics each provide rich data, but computational frameworks to systematically bridge gene expression to connectivity are lacking
- The spatial connectome model (SCM) is the main existing approach but uses a full rule matrix, limiting scalability and potentially missing interactions
- No existing method treats the gene-expression-to-connectivity mapping as a latent factor problem analogous to collaborative filtering in recommendation systems
- There is a need for interpretable models that not only reconstruct connectivity but also identify candidate genes and genetic interaction rules

## Core contribution (bullet form)
- Developed a bilinear model that factorizes the gene-expression-to-connectivity rule matrix into two lower-dimensional transformation matrices, achieving performance comparable to or slightly better than the SCM on C. elegans gap junction reconstruction (AUC comparison in ROC analysis)
- The model captures all innexin interactions found by the SCM and identifies additional putative interactions for experimental exploration
- Applied to mouse retinal data, the model reconstructs BC-to-RGC connectivity and reveals two distinct latent dimensions corresponding to recognized connectivity motifs (ON vs. OFF stratification patterns)
- Identified gene signatures (top 50 genes per latent dimension) enriched for cell-cell adhesion and synapse formation gene ontology terms, providing biologically interpretable insights
- Predicted BC partners for transcriptomically defined RGC types with unknown connectivity; predictions align with known functional descriptions of those cell types
- The approach generalizes from single-cell level (C. elegans, where each neuron is treated as a type) to neuronal-type level (mouse retina, where transcriptomic and connectomic data come from different sources)

## Method in brief
The bilinear model draws on collaborative filtering principles. Given presynaptic gene expression vectors x and postsynaptic gene expression vectors y, the connectivity z between a presynaptic neuron and postsynaptic neuron is modeled as z = x^T A^T B y, where A and B are learned transformation matrices that project gene expressions into a shared latent feature space. The optimization objective minimizes the weighted Frobenius norm of the difference between the predicted covariance matrix (constructed from transformed gene expressions) and the observed connectivity matrix, with L2 regularization on A and B. A weight matrix ensures neuronal types with different cell counts contribute equally.

In the practical scenario where transcriptomic and connectomic data come from different sources and are aligned at the neuronal-type level, cell-level gene expressions and connectivity are approximated by their type-level averages. PCA is applied to gene expression vectors before model fitting to address multicollinearity. Hyperparameters (regularization strength lambda, latent dimensionality) are selected via cross-validation.

For the C. elegans dataset, spatial constraints such as physical contact between neurons are incorporated into the weight matrix. For the mouse retinal dataset, the model is trained with BC and RGC transcriptomic data as pre- and postsynaptic inputs, and the BC-RGC connectivity matrix from connectomic studies as the target. The learned latent dimensions are then interpreted biologically through gene weight analysis and GO enrichment.

## Target venue
eLife
