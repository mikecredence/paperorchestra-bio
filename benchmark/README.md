# BiomedWritingBench

A benchmark corpus for evaluating automated biomedical research paper writing,
analogous to PaperOrchestra's [PaperWritingBench](https://arxiv.org/abs/2604.05018)
but focused on life sciences.

**Current status:** 143 test cases across 10 biomedical subfields. 110+ generated papers across 6 conditions. Full 3x2 factorial evaluation complete.

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
| Bioinformatics | 15+ | DNA foundation models, metagenomic classifiers, sRNAfrag |
| Neuroscience | 15+ | Hippocampus-accumbens coding, synaptic event detection, speech decoding |
| Genomics / Single-Cell | 10+ | Spatial clustering benchmark, GPT-4 cell annotation |
| Immunology | 6+ | Immune aging atlas, inflammasome assembly, CAR-T |
| Structural Biology | 5+ | Cryo-EM refinement, CryoTEN density maps |
| Cell Biology | 6+ | RNA Pol II inhibitor, SUMO E3 ligase, lncRNA |
| Cancer Biology | 4+ | EMT stem cells, disseminating cells, tumor heterogeneity |
| Drug Discovery | 4+ | DeepTernary, ScopeDTI |
| Epidemiology | 4+ | Population structure, avian influenza, life history |
| Clinical | 1+ | Nanopore metagenomics mock communities |
| **Total** | **143** | |

### Venues Represented

Nature Communications, Nature Methods, Nature Biotechnology, Nature Neuroscience,
Nature Immunology, Nature (main), eLife, Genome Biology, Nucleic Acids Research,
PLOS Computational Biology, Bioinformatics, BMC Bioinformatics, Briefings in
Bioinformatics, Scientific Data, Cell Reports, Lancet Digital Health

## Evaluation Results (3x2 Factorial)

### Design

- **Pipeline** (2 levels): Single agent baseline vs multi-agent skill pipeline
- **Input type** (3 levels): Abstract-only, XML full-text (JATS), v2 LLM-structured (markdown tables)

### Conditions and Generated Papers

| Condition | Pipeline | Input | N papers |
|-----------|----------|-------|----------|
| `baseline_paper` | Single agent | Abstract | 20 |
| `generated_paper` | Skill pipeline | Abstract | 20 |
| `baseline_rich_paper` | Single agent | XML full-text | 15 |
| `rich_paper` | Skill pipeline | XML full-text | 15 |
| `baseline_v2_paper` | Single agent | v2 LLM-structured | 20 |
| `skill_v2_paper` | Skill pipeline | v2 LLM-structured | 20 |

### LLM-as-Judge Overall Quality (0-100)

| Input Type | Baseline | Skill | Delta | p-value | Skill Wins |
|------------|----------|-------|-------|---------|------------|
| Abstract (n=20) | 80.2 | 81.5 | +1.2 | n.s. | 11/20 |
| XML full-text (n=15) | 80.9 | 84.3 | +3.3 | 0.002** | 12/15 |
| v2 LLM-structured (n=20) | 70.5 | 81.0 | +10.5 | <0.001*** | 20/20 |

### Interaction Analysis

```
2x2: Abstract vs v2 LLM-Structured x Baseline vs Skill (n=15)
  Abstract+Baseline:    80.2
  Abstract+Skill:       80.7
  v2-LLM+Baseline:      70.7
  v2-LLM+Skill:         81.5
  Pipeline effect:      +5.7
  Input effect:         -4.4
  Interaction:         +10.3 (synergistic)
```

The pipeline's advantage is largest with structured inputs: the baseline cannot handle
markdown tables (presentation: 55.0), while the skill pipeline converts them into
LaTeX tables effectively (presentation: 76.8, tables/paper: 9.8 vs 0.1).

### Compilation Rates

| Condition | Rate | Avg Pages |
|-----------|------|-----------|
| Baseline (abstract) | 100% | 6.5 |
| Skill (abstract) | 90% | 8.2 |
| Baseline (XML) | 100% | 5.9 |
| Skill (XML) | 100% | 6.6 |
| Baseline (v2-LLM) | 100% | 4.5 |
| Skill (v2-LLM) | 100% | 8.8 |

## Pipeline Scripts

All scripts in `benchmark/scripts/`. Use `uv run python benchmark/scripts/<script>.py`.

| Script | Purpose |
|--------|---------|
| `final_analysis.py` | **3x2 factorial analysis** with Wilcoxon tests across all conditions |
| `fix_and_compile.py` | LaTeX compilation for all 6 conditions with TinyTeX |
| `quick_metrics.py` | Structural metrics for all conditions |
| `compute_comparison.py` | Paired citation comparison |
| `ground_truth_comparison.py` | Generated vs published papers |
| `llm_extract.py` | Generate v2 LLM extraction prompts |
| `overnight_run.py` | Batch JATS XML extraction from bioRxiv |
| `config.py` | Shared paths, bioRxiv API helpers, rate limiter, venue mappings |
| `discover_candidates.py` | Find new candidates via bioRxiv `/pubs/` API |
| `extract_ground_truth.py` | Extract structured GT from abstracts |
| `generate_test_case.py` | Reverse-engineer idea_summary + experimental_log |
| `validate_schema.py` | JSON Schema + structural validation for all test cases |
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
| Corpus size | 200 | 143 |
| Source | Reverse-engineered from published papers | bioRxiv preprints → published journals |
| Ground truth | Full paper text | Abstract + estimated metrics |
| Venues | CVPR, ICLR | Nature, eLife, Genome Biology, etc. |
| Generated papers | N/A | 110+ across 6 conditions |
| Evaluation | Human SxS + LLM judge + ScholarPeer | Citation F1 + LLM judge + structural + Wilcoxon |
| Automation | Manual reverse-engineering | Semi-automated pipeline |
| MCP integration | None | bioRxiv, ClinicalTrials, PubMed |

## References

- [PaperOrchestra](https://arxiv.org/abs/2604.05018) — Song et al., 2025
- [paper-orchestra skill pack](https://github.com/Ar9av/paper-orchestra) — Ar9av
