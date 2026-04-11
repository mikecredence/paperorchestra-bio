# Idea Summary: PEPerMINT: Peptide Abundance Imputation in Mass Spectrometry-based Proteomics using Graph Neural Networks

## Working title
PEPerMINT: Peptide Abundance Imputation in Mass Spectrometry-based Proteomics using Graph Neural Networks

## Core question
AbstractMotivationAccurate quantitative information about the protein abundance is crucial for understanding a biological system and its dynamics. Protein abundance is commonly estimated using label-free, bottom-up mass spectrometry protocols. Here, proteins are digested into peptides before quantification via mass spectrometry. However, missing peptide abundance values, which can make up more than 50% of all abundance values, are a common issue. They result in missing protein abundance values, 

## Motivation / gap
- IntroductionProteins are the main acting molecules in cells.
- The characterization of their quantity in different biological contexts plays a fundamental role in understanding cellular function and regulation in disease [1, 2].
- Methods based on label-free mass spectrometry (MS) are commonly used for high throughput quantification of protein abundance in biological samples [3].
- In MS-based bottom-up proteomics, proteins are enzymatically digested into peptides before subjecting them to a mass spectrometer.
- Individual peptides are then commonly identified by matching their spectra to corresponding databases [4].

## Core contribution (bullet form)
Extracted from abstract:
AbstractMotivationAccurate quantitative information about the protein abundance is crucial for understanding a biological system and its dynamics. Protein abundance is commonly estimated using label-free, bottom-up mass spectrometry protocols. Here, proteins are digested into peptides before quantification via mass spectrometry. However, missing peptide abundance values, which can make up more than 50% of all abundance values, are a common issue. They result in missing protein abundance values, which then hinder accurate and reliable downstream analyses.ResultsTo impute missing abundance values, we propose PEPerMINT, a graph neural network model working directly on the peptide level that flexibly takes both peptide-to-protein relationships in a graph format as well as amino acid sequence information into account. We benchmark our method against eleven common imputation methods on six diverse datasets, including cell lines, tissue, and plasma samples. We observe that PEPerMINT consistently outperforms other imputation methods. Its prediction performance remains high for varying degrees of missingness, different evaluation approaches and differential expression prediction. As an additional novel feature, PEPerMINT provides meaningful uncertainty estimates and allows for tailoring imputation to the user’s needs based on the reliability of imputed values.Availability and implementationThe code is available at https://github.com/DILiS-lab/pepermint.

## Method in brief
MethodsWe introduce PEPerMINT (PEPtide Mass spectrometry Imputation NeTwork), a method combining abundance values and information from amino acid sequences and protein-peptide relations to impute missing values on the peptide level. For its implementation and systematic benchmarking, we use our novel open-source PyProteoNet framework (see Supplement).PEPerMINT imputationFor our PEPerMINT imputation model, we propose a neural network architecture combining a learnable transformation of abundance values, a GNN operating on the peptide graph, as well as amino acid sequence embeddings derived from a transformer-based language model (see Fig. 1A for a visual overview).Input featuresWe assume a proteomics dataset with abundance values for n (potentially non-unique) peptides measured across s samples given as n × s matrix A where the elements of A either represent logarithmized (natural logarithm) and standardized (zero mean, unit variance) abundance values or missing values. Missing values are ignored for logarithmization and standardization. We address the problem of predicting abundance values for the missing values. PEPerMINT takes two inputs: the abundance matrix A and an n × 1024 sequence embedding matrix S. S is precomputed from the peptide amino acid sequences using the ProtT5 language model, which has previously shown good performance generating protein embeddings from sequence strings for tasks like predicting protein secondary structure [21]. This allows PEPerMINT to acco

## Target venue
Bioinformatics
