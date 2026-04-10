# BiomedWritingBench

A benchmark corpus for evaluating automated biomedical research paper writing,
analogous to PaperOrchestra's [PaperWritingBench](https://arxiv.org/abs/2604.05018)
but focused on life sciences.

**Current status:** 63 test cases, 63/63 passing validation, across 10+ biomedical subfields.

## Corpus Overview

Each test case is reverse-engineered from a bioRxiv preprint that has been
published in a peer-reviewed journal. The inputs (idea summary + experimental
log) simulate what a researcher would hand over before writing — the published
paper serves as ground truth for evaluation.

```
benchmark/
  test-cases/
    {paper-slug}/
      idea_summary.md         # Core contribution, motivation, method sketch
      experimental_log.md     # Raw numbers, metrics, comparison tables
      metadata.json           # Ground truth reference, venue, category
  ground_truth/
    {paper-id}/
      ground_truth.json       # Extracted metadata: estimated figs/tables/refs,
                              #   key methods, key results, difficulty tags
```

### Current Distribution

| Subfield | Test Cases | Example Papers |
|----------|-----------|---------------|
| Genomics / Single-Cell | 10 | Spatial clustering benchmark, GPT-4 cell annotation |
| Bioinformatics | 10 | DNA foundation models, metagenomic classifiers |
| Drug Discovery | 4 | DeepTernary, ScopeDTI, proteomic disease prediction |
| Neuroscience (general) | 4 | Cortical development, osl-dynamics toolbox, brain SC-FC coupling |
| Neuroscience (biological neural nets) | 3 | Drosophila connectome (FlyWire), mouse MICrONS, C. elegans synapses |
| Immunology | 4 | Immune aging atlas, CAR-T humoral immunity |
| Cancer Biology | 2 | EMT stem cells, tumor-retained state |
| Structural Biology | 5 | Cryo-EM refinement, inflammasome inhibition |
| Cell Biology | 6 | RNA Pol II inhibitor, histone deubiquitinase |
| Epidemiology | 2 | Avian influenza migration, ectotherm life history |
| Clinical | 1 | Nanopore metagenomics mock communities |
| **Total** | **63** | |

### Venues Represented

Nature Communications, Nature Methods, Nature Biotechnology, Nature Neuroscience,
Nature Immunology, Nature (main), eLife, Genome Biology, Nucleic Acids Research,
PLOS Computational Biology, Bioinformatics, BMC Bioinformatics, Briefings in
Bioinformatics, Scientific Data, Cell Reports, Lancet Digital Health

## Pipeline Scripts

All scripts in `benchmark/scripts/`. Use `uv run python benchmark/scripts/<script>.py`.

| Script | Purpose |
|--------|---------|
| `config.py` | Shared paths, bioRxiv API helpers, rate limiter, venue mappings |
| `discover_candidates.py` | Find new candidates via bioRxiv `/pubs/` API |
| `extract_ground_truth.py` | Extract structured GT from abstracts (heuristic or Claude API) |
| `generate_test_case.py` | Reverse-engineer idea_summary + experimental_log |
| `validate_schema.py` | JSON Schema + structural validation for all test cases |
| `batch_runner.py` | Prepare prompts, collect metrics, show status |
| `aggregate_results.py` | Compute per-subfield stats, generate tables and figures |
| `citation_f1.py` | Citation precision / recall / F1 metric |
| `llm_judge.py` | LLM-as-judge evaluation (side-by-side or absolute mode) |

## Running the Benchmark

### 1. Validate the dataset

```bash
uv run python benchmark/scripts/validate_schema.py --report
```

### 2. Prepare evaluation prompts

```bash
uv run python benchmark/scripts/batch_runner.py prepare
```

This generates `benchmark/batch/{paper-id}/prompt.md` for each test case.

### 3. Run the paper-builder skill

Feed each prompt to the paper-builder skill in Claude Code:

```bash
# In Claude Code, for each test case:
# "Write a paper from benchmark/test-cases/{paper-id}/idea_summary.md
#  and experimental_log.md, target venue: {venue}"
```

Or run programmatically with the Anthropic API (requires `ANTHROPIC_API_KEY`).

### 4. Collect metrics

```bash
uv run python benchmark/scripts/batch_runner.py evaluate
```

### 5. Aggregate results

```bash
uv run python benchmark/scripts/aggregate_results.py --figures --markdown benchmark/results/summary.md
```

## Evaluation Metrics

### Citation F1

```bash
uv run python benchmark/scripts/citation_f1.py \
  --generated-bib results/paper/references.bib \
  --ground-truth benchmark/ground_truth/{paper-id}/ground_truth.json
```

Computes precision, recall, and F1 by fuzzy-matching generated citation titles
against ground truth expected citations.

### LLM-as-Judge (7 axes)

```bash
# Side-by-side mode (when ground truth text available):
uv run python benchmark/scripts/llm_judge.py \
  --generated output.tex --ground-truth gt.tex --batch

# Absolute mode (score a single paper, no comparison):
uv run python benchmark/scripts/llm_judge.py \
  --generated output.tex --absolute --batch --dry-run
```

Axes: clarity, rigor, completeness, writing, presentation, citations, overall.
Each scored 0-100 with rationale.

### Structural Metrics

Computed by `batch_runner.py evaluate`:
- Compilation success (did LaTeX produce a PDF?)
- Figure count delta vs ground truth
- Table count delta vs ground truth
- Citation count delta vs ground truth

## Extending the Corpus

### Add more papers from bioRxiv

```bash
# Discover 20 new candidates published in target journals
uv run python benchmark/scripts/discover_candidates.py --target-count 20

# Extract ground truth for new candidates
uv run python benchmark/scripts/extract_ground_truth.py

# Generate test case files
uv run python benchmark/scripts/generate_test_case.py

# Validate
uv run python benchmark/scripts/validate_schema.py --report
```

For higher quality test cases, set `ANTHROPIC_API_KEY` before running
`extract_ground_truth.py` and `generate_test_case.py` — this enables
Claude-assisted extraction instead of heuristic-only mode.

### Manual curation

The 3 highest-quality test cases (`dna-foundation-models`,
`spatial-transcriptomics`, `nanopore-variant-calling`) were manually curated
with rich experimental logs containing full results tables. These serve as
the gold standard. Auto-generated test cases from abstracts are tagged with
a `generation_confidence` field (high/medium/low) in their ground truth.

## Schema

See `schema.json` for the formal JSON Schema for `metadata.json`. Key fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier |
| `title` | string | Paper title |
| `biorxiv_doi` | string/null | bioRxiv DOI |
| `published_doi` | string | Published journal DOI |
| `published_venue` | string | Journal name |
| `category` | enum | Subfield (genomics, neuroscience, etc.) |
| `paper_type` | enum | benchmark, methods, clinical, research, etc. |
| `ground_truth_citation_count` | int/null | References in published paper |
| `ground_truth_figure_count` | int/null | Figures in published paper |
| `ground_truth_table_count` | int/null | Tables in published paper |
| `difficulty` | enum | easy, medium, hard |

## Comparison to PaperWritingBench

| Feature | PaperWritingBench | BiomedWritingBench |
|---------|------------------|-------------------|
| Domain | AI (CVPR/ICLR) | Biomedical (10+ subfields) |
| Corpus size | 200 | 63 (target 100) |
| Source | Reverse-engineered from published papers | bioRxiv preprints → published journals |
| Ground truth | Full paper text | Abstract + estimated metrics |
| Venues | CVPR, ICLR | Nature, eLife, Genome Biology, etc. |
| Evaluation | Human SxS + LLM judge + ScholarPeer | Citation F1 + LLM judge + structural |
| Automation | Manual reverse-engineering | Semi-automated pipeline |
| MCP integration | None | bioRxiv, ClinicalTrials, PubMed |

## References

- [PaperOrchestra](https://arxiv.org/abs/2604.05018) — Song et al., 2025
- [paper-orchestra skill pack](https://github.com/Ar9av/paper-orchestra) — Ar9av
