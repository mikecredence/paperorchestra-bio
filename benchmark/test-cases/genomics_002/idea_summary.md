## Working title

Assessing GPT-4 for Cell Type Annotation in Single-Cell RNA-seq Analysis

## Core question

Can GPT-4, a general-purpose large language model, accurately annotate cell types from marker gene lists produced by standard scRNA-seq pipelines, and how does its performance compare to manual expert annotation?

## Motivation / gap

- Cell type annotation is essential but labor-intensive, requiring domain expertise and curation of canonical marker genes
- Automated annotation tools typically need high-quality reference datasets and custom pipelines
- LLMs like GPT-4 have broad biological knowledge but have not been systematically evaluated for this task across diverse tissues and cell types

## Core contribution

- Systematic evaluation of GPT-4 for cell type annotation across hundreds of tissue and cell types
- Demonstration of strong concordance between GPT-4 annotations and manual expert annotations
- Release of GPTCelltype, an open-source R package that wraps GPT-4 for easy integration into scRNA-seq workflows
- Evidence that LLM-based annotation can substantially reduce the effort and expertise barrier for cell type annotation

## Method in brief

We will run standard scRNA-seq analysis pipelines (Seurat/Scanpy) to identify clusters and compute marker genes (e.g., via Wilcoxon or MAST). Marker gene lists per cluster will be fed as prompts to GPT-4 with tissue context. GPT-4 annotations will be compared against manual annotations using concordance metrics across a diverse panel of datasets spanning hundreds of tissue types and cell types. We will package the workflow as GPTCelltype (R package).

## Target venue

Nature Methods
