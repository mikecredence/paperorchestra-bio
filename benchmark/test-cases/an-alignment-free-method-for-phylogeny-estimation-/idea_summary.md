# Idea Summary: An Alignment-free Method for Phylogeny Estimation using Maximum Likelihood

## Working title
An Alignment-free Method for Phylogeny Estimation using Maximum Likelihood

## Core question
AbstractWhile alignment has traditionally been the primary approach for establishing homology prior to phylogenetic inference, alignment-free methods offer a simplified alternative, particularly beneficial when handling genome-wide data involving long sequences and complex events such as rearrangements. Moreover, alignment-free methods become crucial for data types like genome skims, where assembly is impractical. However, despite these benefits, alignment-free techniques have not gained widespr

## Motivation / gap
- 1.IntroductionA phylogenetic tree depicts the evolutionary history of a given set of species.
- Efficient and accurate construction of phylogenies from genome data is one of the most important problems in biology and is a major research focus in bioinformatics and systematics.
- Phylogeny construction methods can be broadly classified into two groups: distance based and character based.
- Distance based methods compute the distances from the genomic sequences of each pair of species to construct a distance matrix.
- Tree construction algorithms are then applied to this matrix to estimate the tree topology.

## Core contribution (bullet form)
Extracted from abstract:
AbstractWhile alignment has traditionally been the primary approach for establishing homology prior to phylogenetic inference, alignment-free methods offer a simplified alternative, particularly beneficial when handling genome-wide data involving long sequences and complex events such as rearrangements. Moreover, alignment-free methods become crucial for data types like genome skims, where assembly is impractical. However, despite these benefits, alignment-free techniques have not gained widespread acceptance since they lack the accuracy of alignment-based techniques, primarily due to their reliance on simplified models of pairwise distance calculation. Here, we present a likelihood based alignment-free technique for phylogenetic tree construction. We encode the presence or absence of k-mers in genome sequences in a binary matrix, and estimate phylogenetic trees using a maximum likelihood approach. We analyze the performance of our method on seven real datasets and compare the results with the state of the art alignment-free methods. Results suggest that our method is competitive with existing alignment-free tools. This indicates that maximum likelihood based alignment-free methods may in the future be refined to outperform alignment-free methods relying on distance calculation as has been the case in the alignment-based setting. A likelihood based alignment-free method for phylogeny estimation is implemented for the first time in a software named Peafowl, which is available at: https://github.com/hasin-abrar/Peafowlrepo.

## Method in brief
2.MethodsAn overview of phylogenetic tree estimation using Peafowl is shown in Figure 1. The method consists of four major steps. First, the set of k-mers present in each input sequence is generated. Second, a binary matrix is constructed, which encapsulates the presence or absence of the k-mers within the sequences. Third, a suitable value of k is chosen based on entropy values. Finally, a phylogenetic tree is constructed using maximum likelihood estimation. A sketch of the steps is presented in Algorithm 1 and described in more detail in the following sections.biorxiv;2019.12.13.875526v2/FIG1F1fig1Figure 1:Overview of phylogenetic tree estimation using Peafowl.At the beginning, k-mers of various sizes are listed from the input sequences. Then separate binary matrices are produced using these k-mers. From the binary matrices of different k-mer sizes, an appropriate k-mer length (kentropy) is chosen based on cumulative entropy values. Lastly, the binary matrix corresponding to kentropy is provided as input to RAxML for the estimation of the phylogenetic tree.biorxiv;2019.12.13.875526v2/FIG2F2fig2Figure 2:Choosing k-mer lengths.Existence of k-mers depends on the length. In this figure, the k-mer AT of length 2 is found in all 3 taxa. However, the k-mer ATAGCGC of length 7 is found only in the source taxon (T1).2.1.Generating k-mersThe first step in Peafowl is to generate the lists of k-mers present in the input sequences. k-mers are generated from the input DNA sequences using

## Target venue
BMC Bioinformatics
