# Bio Paper Orchestra

A multi-agent pipeline for automated biomedical research paper writing, inspired by [PaperOrchestra](https://arxiv.org/abs/2604.05018). Implemented as a [Claude Code](https://claude.ai/claude-code) skill that transforms unstructured pre-writing materials (idea summaries, experimental logs) into submission-ready LaTeX manuscripts with verified citations, generated figures, and iterative refinement.

## Features

- **5-stage pipeline**: Outline, Plot, Literature, Writing, Refinement
- **MCP integrations**: bioRxiv, ClinicalTrials.gov, PubMed for biomedical literature discovery
- **Citation verification**: Semantic Scholar API with DOI/arXiv direct lookup, fuzzy title matching, deduplication, and cutoff date enforcement
- **Anti-leakage protocol**: Prevents content generation from pre-training memory
- **Score-tracked refinement**: 0-100 scoring on 6 axes with filesystem rollback
- **Citation audit**: Automated orphan detection and coverage enforcement (>=90% target)
- **BiomedWritingBench**: 143 test cases across 10 biomedical subfields with full 3x2 factorial evaluation (110 generated papers, 6 conditions)

## Key Findings

A 3x2 factorial experiment (Pipeline x Input Type, 110 papers across 6 conditions) reveals:

### Overall Quality (LLM-as-Judge, 0-100)

| Condition | Baseline | Skill Pipeline | Delta | p-value |
|-----------|----------|---------------|-------|---------|
| Abstract inputs (n=20) | 80.2 | 81.5 | +1.2 | n.s. |
| XML full-text (n=15) | 80.9 | 84.3 | +3.3 | p=0.002** |
| v2 LLM-structured (n=20) | 70.5 | 81.0 | +10.5 | p<0.001*** |

### Structural Metrics

| Condition | Skill Citations | Skill Tables | Baseline Citations | Baseline Tables |
|-----------|----------------|-------------|-------------------|----------------|
| Abstract | 22.5 | 4.0 | 12.1 | 3.8 |
| XML full-text | 29.0 | 1.6 | 19.7 | 0.0 |
| v2 LLM-structured | 22.2 | 9.8 | 8.3 | 0.1 |

### Key insights

- **Pipeline + structured inputs are synergistic**: +10.3 interaction effect for v2 inputs
- The skill pipeline wins **20/20 papers** with v2 structured inputs (p<0.001 on every axis)
- The baseline collapses with v2 inputs (presentation: 55.0) while the skill thrives (76.8)
- The skill pipeline normalizes quality: 81-84 overall regardless of input type
- Compilation rate: 98.4% across all 6 conditions (123/125 papers)

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
  README.md                         # BiomedWritingBench design + results
  schema.json                       # Entry schema (JSON Schema)
  benchmark_run_20.json             # 20 papers for original evaluation
  benchmark_run_v2.json             # 20 papers for v2 evaluation
  scripts/
    final_analysis.py               # 3x2 factorial analysis + Wilcoxon tests
    fix_and_compile.py              # LaTeX compilation across all conditions
    quick_metrics.py                # Structural metrics summary
    citation_f1.py                  # Citation precision/recall/F1
    llm_judge.py                    # Claude API side-by-side evaluation
  test-cases/                       # 143 test cases across 10 subfields
  results/                          # 110+ generated papers across 6 conditions
  ground_truth/                     # Published paper metadata for comparison
```

## BiomedWritingBench

A benchmark for evaluating automated biomedical paper writing (143 test cases, 10 subfields, 110+ generated papers). See [`benchmark/README.md`](benchmark/README.md) for full details.

### 3x2 Factorial Design

- **Pipeline** (2 levels): Single agent baseline vs multi-agent skill pipeline
- **Input type** (3 levels): Abstract-only, XML full-text, v2 LLM-structured

### Evaluation

- **LLM-as-Judge**: 7 axes (clarity, rigor, completeness, writing, presentation, citations, overall), scored 0-100
- **Structural metrics**: Citation count, table count, word count, paper size
- **Wilcoxon signed-rank tests**: Paired comparisons within each input type
- **LaTeX compilation**: 98.4% success rate across all conditions

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
| Benchmark corpus | 200 AI papers (CVPR/ICLR) | 143 biomedical test cases (Nature, eLife, etc.) |

## References

- [PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://arxiv.org/abs/2604.05018) (Song et al., 2025)
- [PaperOrchestra Project Page](https://yiwen-song.github.io/paper_orchestra/)
- [paper-orchestra skill pack](https://github.com/Ar9av/paper-orchestra) (Ar9av)

## License

MIT
