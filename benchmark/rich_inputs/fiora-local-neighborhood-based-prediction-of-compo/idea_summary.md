# Idea Summary: Fiora: Local neighborhood-based prediction of compound mass spectra from single fragmentation events

## Working title
Fiora: Local neighborhood-based prediction of compound mass spectra from single fragmentation events

## Core question
ABSTRACTNon-targeted metabolomics holds great promise for advancing precision medicine and facilitating the discovery of novel biomarkers. However, the identification of compounds from tandem mass spectra remains a non-trivial task due to the incomplete nature of spectral reference libraries. Augmenting these libraries with simulated mass spectra can provide the necessary reference to resolve unmatched mass spectra, but remains a difficult undertaking to this day. In this study, we introduce Fio

## Motivation / gap


## Core contribution (bullet form)
Extracted from abstract:
ABSTRACTNon-targeted metabolomics holds great promise for advancing precision medicine and facilitating the discovery of novel biomarkers. However, the identification of compounds from tandem mass spectra remains a non-trivial task due to the incomplete nature of spectral reference libraries. Augmenting these libraries with simulated mass spectra can provide the necessary reference to resolve unmatched mass spectra, but remains a difficult undertaking to this day. In this study, we introduce Fiora, an innovative open-source algorithm using graph neural networks to simulate tandem mass spectra in silico. Our objective is to improve fragment intensity prediction with an intricate graph model architecture that facilitates edge prediction, thereby modeling fragment ions as the result of singular bond breaks and their local molecular neighborhood. We evaluate the performance on test data from NIST (2017) and the curated MS-Dial spectral library, as well as compounds from the 2016 and 2022 CASMI challenges. Fiora not only surpasses state-of-the-art fragmentation algorithms, ICEBERG and CFM-ID, in terms of prediction quality, but also predicts additional features, such as retention time and collision cross section. In addition, Fiora demonstrates significant speed improvements through the use of GPUs. This enables rapid (re)scoring of putative compound identifications in non-targeted experiments and facilitates large-scale expansion of spectral reference libraries with accurate spectral predictions.biorxiv;2024.04.22.590551v1/UFIG1F1ufig1

## Method in brief
METHODSFragmentation algorithmFiora is designed to take advantage of the unique power of graph neural networks to learn structural patterns and local neighborhoods around chemical bonds. Each molecular structure M is represented as a graph G with atoms for nodes and bonds for edges, which is common practise in computational chemistry. The molecular structure graphs are built from string representations, e.g., SMILES. Fiora operates on neutral molecular structures and only considers information about precursor charge ([M+H]+, [M-H]-) and other covariates at the very end. Fragment ions are modeled by the removal of edges in the graph, indicating singular bond cleavages.A key concept of our method is that we explicitly model ion rearrangements through hydrogen losses. This is important for direct assignment of peaks to fragment ions and allows end-to-end prediction from the molecular structure graph G to the fragment ion space 𝔽 (G). The latter is constructed as follows: Let E(G) denote the set of edges in G and G−e the pair of subgraphs (fragments) that arise from removing edge e ∈ E(G). The fragment ion space is the set of all subgraphs and fragment ionizations, accounting for up to 4 hydrogen losses, i.e.,



For each molecular graph G, Fiora predicts the precursor stability σ and the abundance values θf for all f ∈ 𝔽(G). Both are combined using a softmax function to compute fragment probabilities:



Predicting abundance values θf is conceptually related to the idea of break

## Target venue
Nature Communications
