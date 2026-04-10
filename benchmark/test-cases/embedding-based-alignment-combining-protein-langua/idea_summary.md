## Working title

EBA: Embedding-based protein sequence alignment using protein language models for structural similarity detection in the twilight zone

## Core question

Can protein language model embeddings be used to generate sequence alignments that capture structural similarities even in the twilight zone of sequence identity, outperforming both classical sequence methods and other pLM-based approaches?

## Motivation / gap

- Detecting remote homology (structural similarity at very low sequence identity, the "twilight zone") remains a fundamental challenge in bioinformatics
- Protein language models (pLMs) generate rich per-residue embeddings that encode structural and functional semantics, but these have not been fully exploited for alignment
- Classical sequence-based methods (BLAST, HHblits) fail in the twilight zone
- Other pLM-based methods for homology detection exist but do not generate actual alignments or underperform on structural similarity benchmarks

## Core contribution

- EBA (Embedding-Based Alignment): a new method that generates protein sequence alignments from pLM per-residue embeddings
- Captures structural similarities even in the twilight zone
- Outperforms both classical sequence-based scores and other pLM-based approaches
- Requires no training or parameter optimization -- excellent accuracy out of the box

## Method in brief

- Extract per-residue embeddings from a protein language model for each sequence
- Compute pairwise residue similarity scores from embedding space
- Generate optimal alignment using dynamic programming on the embedding-derived score matrix
- Benchmark against classical sequence alignment tools and other pLM-based methods on structural similarity datasets

## Target venue

Bioinformatics
