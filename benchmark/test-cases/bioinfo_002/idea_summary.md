## Working title

DREAM Challenge: Optimizing sequence-based deep learning models of gene regulation

## Core question

How do different neural network architectures and training strategies impact the ability to predict gene expression from regulatory DNA sequences, and can we identify optimal approaches through community competition?

## Motivation / gap

- Neural networks have shown great promise for predicting functional genomic regions and gene regulatory logic
- A systematic evaluation of how model architecture choices and training strategies affect performance on gene regulation tasks is lacking
- No community-wide effort has compared approaches on a large, experimentally determined dataset of promoter sequence-expression relationships

## Core contribution

- Organize a DREAM Challenge where competitors train models on millions of random promoter DNA sequences with experimentally measured expression levels in yeast
- Design a comprehensive suite of benchmarks encompassing various sequence types for robust evaluation
- Show that all top-performing models use neural networks but diverge in architectures and employ novel training strategies tailored to genomics data
- Find that some benchmarks produce similar results across top models while others differ substantially, revealing complementary strengths

## Method in brief

- Training data: millions of random yeast promoter sequences with experimentally measured expression (MPRA/STARR-seq style)
- Participants submit trained models; organizers evaluate on held-out and designed test sets
- Benchmark suite: random held-out sequences, natural yeast promoters, motif-insertion sequences, expression-matched pairs
- Compare architectures: CNN, transformer, hybrid, with various training strategies (data augmentation, curriculum learning, multi-task)

## Target venue

Nature Biotechnology
