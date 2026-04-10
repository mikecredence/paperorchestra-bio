# Idea Summary: Benchmarking DNA Foundation Models for Genomic and Genetic Tasks

## Working title
Benchmarking DNA Foundation Models for Genomic and Genetic Tasks

## Core question
AbstractThe rapid evolution of DNA foundation models promises to revolutionize genomics, yet comprehensive evaluations are lacking. Here, we present a comprehensive, unbiased benchmark of five models (DNABERT-2, Nucleotide Transformer V2, HyenaDNA, Caduceus-Ph, and GROVER) across diverse genomic and genetic tasks including sequence classification, gene expression prediction, variant effect quantification, and topologically associating domain (TAD) region recognition, using zero-shot embeddings. 

## Motivation / gap
- IntroductionLed by the advances in Natural Language Processing (NLP) in recent years, foundation language models through self-supervised pre-training have been the paradigm of decoding information in 
- By representing sequences as numerical embeddings, foundation language models can outperform previous methods in many downstream tasks such as sequence classification and sequence generation.
- As natural language-based foundation models like GPT-4 [1], Llama 3 [2], and Qwen3 [3] have been proven successful, similar ideas have been extended to other domains by interpreting domain-specific la
- With the long-lasting interests in decoding DNA sequences to understand the epigenetic patterns, transcriptional regulations, and disease associations [8,9], DNA foundation language models have also e
- These models are pre-trained on large genomic datasets such as the human reference genome [15], human whole-genome sequencing datasets like 1000 Genomes project datasets [16], and multi-species genome

## Core contribution (bullet form)
Extracted from abstract:
AbstractThe rapid evolution of DNA foundation models promises to revolutionize genomics, yet comprehensive evaluations are lacking. Here, we present a comprehensive, unbiased benchmark of five models (DNABERT-2, Nucleotide Transformer V2, HyenaDNA, Caduceus-Ph, and GROVER) across diverse genomic and genetic tasks including sequence classification, gene expression prediction, variant effect quantification, and topologically associating domain (TAD) region recognition, using zero-shot embeddings. Our analysis reveals that mean token embedding consistently and significantly improves sequence classification performance, outperforming other pooling strategies. Model performance varies among tasks and datasets; while general purpose DNA foundation models showed competitive performance in pathogenic variant identification, they were less effective in predicting gene expression and identifying putative causal QTLs compared to specialized models. Our findings offer a framework for model selection, highlighting the impact of architecture, pre-training data, and embedding strategies on performance in genomic and genetic tasks.

## Method in brief
MethodsDNA foundation language modelsTo evaluate DNA foundation language models comprehensively, we identified the three most recent state-of-the-art DNA foundation language models, including DNABERT-2 [10], Nucleotide Transformer version-2 [11], HyenaDNA [12], Caduceus [13], and GROVER [14]. These foundation models take DNA sequence as input, tokenize into sequence of tokens, and generate embeddings of fixed dimension for each token after passing multiple layers. In the following, we will briefly describe these three models.DNABERT-2 [10] has the network architecture similar to Bidirectional Encoder Representations from Transformers (BERT) [25], which usually contains a positional embedding layer added to input embeddings, and a series of encoders each consisting of a multi-head self-attention layer and a feedforward network. It is pre-trained using the masked language modelling approach on genomes from 135 species, including the human reference genome. DNABERT-2 tokenizes DNA sequences by the Byte Pair Encoding (BPE) method, which is an iterative algorithm that searches for nucleotides combinations and builds the vocabulary at the same time; it makes no assumption on fixed words and grammars, so each input sequence is independently tokenized merely based on its pattern. It is worth noting that the number of tokens in the tokenized sequence is not fixed in DNABERT-2. DNABERT-2 modifies the architecture of BERT by using Attention with Linear Biases (ALiBi) instead of position

## Target venue
Nature Communications
