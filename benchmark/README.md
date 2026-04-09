# BiomedWritingBench

A benchmark corpus for evaluating automated biomedical research paper writing,
analogous to PaperOrchestra's PaperWritingBench but focused on life sciences.

## Design

### Corpus Structure
Each benchmark entry consists of reverse-engineered raw materials from a
bioRxiv preprint that has been published in a peer-reviewed journal:

```
benchmark/
  test-cases/
    {paper-slug}/
      idea_summary.md         # Core contribution, motivation, method sketch
      experimental_log.md     # Raw numbers, metrics, comparisons
      metadata.json           # Ground truth reference, venue, category
```

### Schema (metadata.json)

```json
{
  "id": "dna-foundation-models",
  "title": "Ground truth paper title",
  "biorxiv_doi": "10.1101/...",
  "published_doi": "10.1038/...",
  "published_venue": "Nature Communications",
  "published_year": 2025,
  "authors": ["Author1", "Author2"],
  "category": "genomics",
  "subcategory": "computational_biology",
  "paper_type": "benchmark",
  "format": "single-column",
  "ground_truth_citation_count": 59,
  "ground_truth_figure_count": 6,
  "ground_truth_table_count": 2,
  "difficulty": "medium",
  "notes": "Benchmarking paper with systematic comparison matrix"
}
```

### Target Categories (10 per category = 100 total for v1)

| Category | Examples | MCP Tools Used |
|----------|----------|---------------|
| Genomics / Bioinformatics | DNA models, variant calling, RNA-seq | bioRxiv |
| Drug Discovery / Pharmacology | Target identification, ADMET, compound screening | bioRxiv |
| Clinical / Trials | Intervention studies, diagnostic accuracy | bioRxiv + ClinicalTrials |
| Neuroscience | Brain imaging, neural circuits, behavior | bioRxiv |
| Immunology / Infectious Disease | Vaccine design, immune profiling | bioRxiv |
| Cancer Biology | Tumor profiling, treatment response | bioRxiv + ClinicalTrials |
| Structural Biology | Protein structure, cryo-EM, molecular dynamics | bioRxiv |
| Cell Biology / -omics | Single-cell, spatial transcriptomics, proteomics | bioRxiv |
| Epidemiology / Public Health | Disease modeling, surveillance | bioRxiv |
| Methods / Technology | New assays, platforms, computational tools | bioRxiv |

### Selection Criteria for Corpus Papers
1. Must have a bioRxiv preprint AND a published journal version
2. Must have clear quantitative experimental results (tables, metrics)
3. Must span diverse venues (Nature, Cell, PLOS, BMC, eLife, etc.)
4. Prefer papers with 30-80 citations in the published version
5. Mix of paper types: benchmarks, methods, clinical studies, discovery

### Evaluation Metrics (aligned with PaperOrchestra)

**Automated metrics:**
- Citation F1: precision and recall of generated citations vs ground truth
- Citation coverage: % of verified pool actually cited
- Section completeness: presence and approximate length of all expected sections
- LaTeX compilation: clean compilation with no errors

**LLM-as-judge (side-by-side):**
- Literature review quality (generated vs ground truth)
- Overall manuscript quality (generated vs ground truth)

**Simulated peer review:**
- 6-axis scoring (clarity, rigor, completeness, writing, presentation, citations)
- Each axis 0-100, computed by the refinement agent

## Running the Benchmark

```bash
# For a single test case:
# 1. Feed idea_summary.md + experimental_log.md to the paper-builder skill
# 2. Compare output against ground truth (published paper)
# 3. Compute metrics

# For the full corpus:
# TBD - automation script for batch evaluation
```

## Current Test Cases

| ID | Paper | Category | Venue | Status |
|----|-------|----------|-------|--------|
| bioinfo_001 | Benchmarking DNA Foundation Models | Bioinformatics | Nature Comms | **Ready** |
| spatial-transcriptomics | Spatial Transcriptomics Platform Benchmark | Cell Biology | Nature Comms | Identified |
| nanopore-variant-calling | Nanopore Variant Calling Benchmark | Bioinformatics | eLife | Identified |

## Corpus Candidates (25 identified, target 100)

See `corpus_candidates.json` for the full list. Candidates span 6 subfields:

| Subfield | Candidates | Key Journals |
|----------|-----------|-------------|
| Genomics / Single-Cell | 5 | Nature Methods (x4), Genome Biology |
| Bioinformatics / Comp. Genomics | 4 | Nature Biotechnology, Genome Biology, NAR, PLOS Comp Bio |
| Drug Discovery | 3 | Nature Communications (x2), Lancet Digital Health |
| Neuroscience | 2 | eLife, Nature Methods |
| Immunology | 2 | Nature Immunology, Nature Communications |
| Clinical / Epidemiology | 1 | Scientific Data |

## Schema

See `schema.json` for the formal JSON Schema. Key differences from PaperWritingBench:
- **Structured idea_summary**: explicit `research_question`, `background_motivation`,
  `key_innovations` fields (biomedical papers need hypothesis framing)
- **Dataset provenance**: `source` field with repository accessions (GEO, dbGaP, TCGA)
- **Statistical tests**: explicit field since biomedical papers require statistical rigor
- **Article type**: journals distinguish Research Articles, Brief Communications, etc.
