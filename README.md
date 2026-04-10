# Bio Paper Orchestra

A multi-agent pipeline for automated biomedical research paper writing, inspired by [PaperOrchestra](https://arxiv.org/abs/2604.05018). Implemented as a [Claude Code](https://claude.ai/claude-code) skill that transforms unstructured pre-writing materials (idea summaries, experimental logs) into submission-ready LaTeX manuscripts with verified citations, generated figures, and iterative refinement.

## Features

- **5-stage pipeline**: Outline, Plot, Literature, Writing, Refinement
- **MCP integrations**: bioRxiv, ClinicalTrials.gov, PubMed for biomedical literature discovery
- **Citation verification**: Semantic Scholar API with DOI/arXiv direct lookup, fuzzy title matching, deduplication, and cutoff date enforcement
- **Anti-leakage protocol**: Prevents content generation from pre-training memory
- **Score-tracked refinement**: 0-100 scoring on 6 axes with filesystem rollback
- **Citation audit**: Automated orphan detection and coverage enforcement (>=90% target)
- **BiomedWritingBench**: Benchmark of 60 test cases across 10 biomedical subfields with full 2x2 factorial evaluation

## Key Finding

A 2x2 factorial experiment (Pipeline x Input Richness, n=15 paired papers) reveals that **pipeline and input quality are synergistic**:

```
                    Abstract Input    Full-Text Input
Baseline:           80.2              80.9  (+0.7)
Skill Pipeline:     80.7  (+0.5)     84.3  (+3.4)
```

- The pipeline alone adds little with sparse inputs (+0.5)
- Rich inputs alone add little without the pipeline (+0.7)
- **Combined, they add +4.1 points** — the pipeline amplifies the value of rich inputs
- Skill+FullText wins 9/15 papers (60%) on overall quality
- Biggest gains in substance: rigor (+6.6), completeness (+4.2), citations (+4.4)

## Pipeline

```
User Inputs (idea + results + venue)
        |
        v
  0. WORKSPACE INIT ---- Validated inputs + directory structure
        |
        v
  1. OUTLINE AGENT ----- Structured JSON plan (sections, lit strategy, plot plan)
        |                    <- USER CHECKPOINT
       / \
      v   v
  2. PLOT  3. LITERATURE -- Figures + verified BibTeX + drafted Intro & Related Work
      \   /
       v v
  4. WRITING AGENT ----- Full LaTeX manuscript + anti-leakage checks + citation audit
        |
        v
  5. REFINEMENT AGENT -- Polished PDF (score-delta tracking + rollback)
```

## Quick Start

### Install as a Claude Code skill

```bash
# Clone the repo
git clone https://github.com/mikecredence/bio-paper-orchestra.git
cd bio-paper-orchestra

# The skill is already in .claude/skills/paper-builder/
# Start Claude Code in this directory and ask it to write a paper
```

### Usage

In Claude Code, trigger the skill with any of these prompts:

- "Write my paper from these results"
- "Draft a manuscript for Nature Communications"
- "Turn my experimental log into a research paper"
- "Help me write up my genomics benchmark"

The skill expects:
1. **Idea summary** - core contribution, methodology, motivation
2. **Experimental log** - raw numbers, metrics, comparison tables
3. **Target venue** - journal name (determines formatting)

### Dependencies

```bash
# Python environment (uses uv)
uv sync
uv add requests matplotlib numpy seaborn

# LaTeX (for PDF compilation)
# TinyTeX recommended: https://yihui.org/tinytex/
```

## Project Structure

```
.claude/skills/paper-builder/
  SKILL.md                          # Main skill definition
  references/
    outline-agent.md                # Outline generation prompt
    plot-agent.md                   # Figure generation guidelines
    literature-agent.md             # Citation pipeline (MCP + S2 API)
    writing-agent.md                # LaTeX writing + anti-leakage
    refinement-agent.md             # Score-tracked review + rollback
  scripts/
    verify_citation.py              # Semantic Scholar verification
    citation_audit.py               # Orphan detection + coverage
    init_workspace.py               # Workspace setup + validation
    compile_latex.sh                # pdflatex + bibtex build cycle
    academic_plots.py               # Publication-quality figure utilities

benchmark/
  README.md                         # BiomedWritingBench design
  schema.json                       # Entry schema (JSON Schema)
  corpus_candidates.json            # 25 candidates across 6 subfields
  scripts/
    citation_f1.py                  # Citation precision/recall/F1
    llm_judge.py                    # Claude API side-by-side evaluation
  test-cases/
    dna-foundation-models/          # Nature Comms benchmark paper
    spatial-transcriptomics/        # Nature Comms platform comparison
    nanopore-variant-calling/       # eLife variant calling benchmark
```

## BiomedWritingBench

A benchmark corpus for evaluating automated biomedical paper writing, analogous to PaperOrchestra's PaperWritingBench but focused on life sciences. Each test case contains reverse-engineered inputs from published bioRxiv preprints.

| Test Case | Venue | Subfield | Status |
|-----------|-------|----------|--------|
| DNA Foundation Models | Nature Comms | Computational biology | Full pipeline tested |
| Spatial Transcriptomics | Nature Comms | Spatial genomics | Inputs ready |
| Nanopore Variant Calling | eLife | Bioinformatics | Inputs ready |

### Evaluation metrics

- **Citation F1**: Precision/recall of generated vs ground truth citations
- **LLM-as-judge**: Side-by-side scoring via Claude API (6 axes, 0-100)
- **Citation audit**: Orphaned citations, coverage ratio, citation count

## Comparison to PaperOrchestra

| Feature | PaperOrchestra | Bio Paper Orchestra |
|---------|---------------|-------------------|
| Literature discovery | S2 + web search | S2 + web + bioRxiv + PubMed + ClinicalTrials |
| Citation verification | Semantic Scholar | S2 + DOI/arXiv lookup + web fallback |
| Anti-leakage | Yes | Yes |
| Refinement scoring | 0-100, 6 axes | 0-100, 6 axes with rollback |
| Citation audit | Orphan + coverage scripts | Orphan + coverage + dedup |
| Cutoff enforcement | Yes | Yes |
| Biomedical MCP tools | No | bioRxiv, ClinicalTrials, PubMed |
| Benchmark corpus | 200 AI papers (CVPR/ICLR) | 25 biomedical candidates (Nature, eLife, etc.) |

## References

- [PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://arxiv.org/abs/2604.05018) (Song et al., 2025)
- [PaperOrchestra Project Page](https://yiwen-song.github.io/paper_orchestra/)
- [paper-orchestra skill pack](https://github.com/Ar9av/paper-orchestra) (Ar9av)

## License

MIT
