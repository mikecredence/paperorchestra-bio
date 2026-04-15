# Bio Paper Orchestra

A **multi-skill orchestrated pipeline** for automated biomedical research paper writing, implemented as a set of coordinated [Claude Code](https://claude.ai/claude-code) skills. Inspired by [PaperOrchestra](https://arxiv.org/abs/2604.05018), this project transforms unstructured pre-writing materials (idea summaries, experimental logs) into submission-ready LaTeX manuscripts with verified citations, data-grounded figures, and iterative refinement.

## What's Different: True Multi-Agent Orchestration

Unlike monolithic skills that load a single mega-prompt and generate a paper in one pass, this project implements **6 separate skills that communicate through a shared workspace**:

```
paper-orchestrator (top-level driver)
    |
    +-- outline-agent       Stage 1: workspace/outline.json
    +-- literature-agent    Stage 2: workspace/references.bib + intro_relwork.tex
    +-- plot-agent          Stage 2.5: workspace/figures/*.pdf + figures.tex
    +-- writing-agent       Stage 3: workspace/main.tex
    +-- refinement-agent    Stage 4: iterative review with score-tracked rollback
```

Each sub-skill is invoked separately via the Skill tool, with **validation gates between stages**. This forces stage isolation — the outline agent cannot bleed into literature decisions, the writing agent cannot fabricate citations that literature-agent did not verify, and refinement runs with its own isolated context.

## The Skill

**Primary skill: `paper-orchestrator`**

Invoke from Claude Code with:
- "Orchestrate paper writing on [my inputs]"
- "Run the paper pipeline"
- "Generate a LaTeX paper using the multi-agent pipeline"

Or invoke directly via the Skill tool with a workspace argument.

### Sub-skills (invoked only by the orchestrator)

| Skill | Stage | Produces | Key features |
|-------|-------|----------|-------------|
| `outline-agent` | 1 | `outline.json` | Section plan, table plan, literature strategy |
| `literature-agent` | 2 | `references.bib`, `intro_relwork.tex` | PubMed/bioRxiv/S2 verification, no hallucinated cites |
| `plot-agent` | 2.5 | `figures/*.pdf`, `figures.tex` | Data-grounded plots, schematics, placeholders |
| `writing-agent` | 3 | `main.tex` | Anti-leakage, data fidelity, citation audit |
| `refinement-agent` | 4 | revised `main.tex`, `worklog.json` | 0-100 scoring on 8 axes, rollback on score decrease |

## Pipeline Architecture

```
User Inputs (idea + results + venue)
        |
        v
  Stage 0: INIT ---------- workspace/ structure + validated inputs
        |
        v
  Stage 1: OUTLINE ------- workspace/outline.json
        |                     GATE: valid schema, >= 4 sections, >= 1 table planned
        v
  Stage 2: LITERATURE ---- workspace/references.bib + intro_relwork.tex
        |                     GATE: >= 10 verified entries, no orphan cites
        v
  Stage 2.5: PLOT -------- workspace/figures/*.pdf + figures.tex
        |                     GATE: >= 1 figure, all data traces to extraction
        v
  Stage 3: WRITING ------- workspace/main.tex
        |                     GATE: >100 lines, all cites in .bib, anti-leakage ok
        v
  Stage 4: REFINEMENT ---- workspace/main.tex (improved) + worklog.json
        |                     score-tracked loop with rollback on decrease
        v
    OUTPUT: main.tex + references.bib + figures/
```

### Key guarantees at each stage

- **Outline**: Every section content bullet traces to the input materials.
- **Literature**: Every BibTeX entry is verified against PubMed / bioRxiv / web. Unverified candidates are discarded.
- **Plot**: Every data point in a plot corresponds to a specific sentence in the experimental log. Schematic diagrams use only structural parameters from the extraction. Placeholder figures are explicitly labeled when data is absent.
- **Writing**: Every `\cite{}` key matches a verified `.bib` entry. Every numerical claim traces to the experimental log. Anti-leakage protocol prevents content from pre-training memory.
- **Refinement**: Revisions are scored on 8 axes before and after. Any revision that decreases the overall score is reverted from a filesystem snapshot.

## Features

- **Multi-channel literature discovery**: PubMed (37M+ articles), bioRxiv, ClinicalTrials.gov, web search
- **Citation verification**: Every reference validated via PubMed or Semantic Scholar with DOI extraction
- **Data-grounded figures**: matplotlib bar charts, line plots, and schematic diagrams generated only from values verbatim in the extraction. Placeholders used honestly for missing data.
- **Anti-leakage protocol**: Text is generated solely from user inputs, not from memory of known papers
- **Score-tracked refinement**: 0-100 scoring on 8 axes (clarity, rigor, completeness, writing, presentation, citations, correctness, figures) with rollback on score decrease
- **Stage-isolated execution**: Each sub-skill runs in its own context, communicating only through shared workspace files
- **BiomedWritingBench**: 143 test cases across 10 biomedical subfields

## Evaluation Results (n=1, prefrontal network model)

Initial validation on the prefrontal network model paper. The orchestrated multi-skill pipeline beats a single-agent baseline run with the same inputs on the same judge rubric:

| Axis | Single-agent baseline | **Orchestrated pipeline** | Delta |
|------|-----------------------|---------------------------|-------|
| Clarity | 82 | **90** | +8 |
| Rigor | 80 | **86** | +6 |
| Completeness | 76 | **88** | +12 |
| Writing | 83 | **90** | +7 |
| Presentation | 78 | **90** | +12 |
| Citations | 72 | **88** | +16 |
| Correctness | 88 | **95** | +7 |
| Figures | n/a | **87** | (new axis) |
| **Overall** | **79** | **89** | **+10** |

**Correctness check**: 32/32 numerical claims in the orchestrated output match the extraction exactly. Zero hallucinated values. 4 figures generated (2 data-grounded, 2 schematic), all data points traceable.

Scaled-up comparison on n=5 papers is in progress; results and methodology in `benchmark/README.md`.

## Quick Start

### Install

```bash
git clone https://github.com/mikecredence/paperorchestra-bio.git
cd paperorchestra-bio
uv sync
```

### Usage

In Claude Code, set up a workspace with your inputs:

```
benchmark/results/my-paper/skill_run/
  inputs/
    idea_summary.md          # core contribution, methodology
    experimental_log.md      # raw numbers, results
```

Then invoke the orchestrator:

```
Skill("paper-orchestrator", args="workspace=benchmark/results/my-paper/skill_run venue=eLife")
```

Or ask Claude Code directly:

> "Run the paper-orchestrator pipeline on benchmark/results/my-paper/skill_run, target venue eLife"

### What you get

```
workspace/
├── inputs/
│   ├── idea_summary.md
│   └── experimental_log.md
├── outline.json              # Stage 1 output
├── references.bib            # Stage 2 output (verified citations)
├── intro_relwork.tex         # Stage 2 output (drafted sections)
├── figures/                  # Stage 2.5 output
│   ├── make_figures.py
│   ├── fig_*.pdf / .png
│   └── figures.tex
├── main.tex                  # Stage 3/4 output (final manuscript)
├── snapshots/                # Stage 4 rollback snapshots
├── worklog.json              # Stage 4 refinement log
└── final_scores.json         # Stage 4 final scores
```

## Project Structure

```
.claude/skills/
  paper-orchestrator/SKILL.md         # Top-level driver skill
  outline-agent/SKILL.md              # Stage 1: structured JSON outline
  literature-agent/SKILL.md           # Stage 2: verified .bib + intro/related work
  plot-agent/SKILL.md                 # Stage 2.5: matplotlib figures + figures.tex
  writing-agent/SKILL.md              # Stage 3: full LaTeX manuscript
  refinement-agent/SKILL.md           # Stage 4: iterative review with rollback
  paper-builder/                      # Legacy monolithic skill (superseded)
    references/                       # Reference docs reused by sub-skills
    scripts/                          # Citation verification, LaTeX compilation

benchmark/
  README.md                           # BiomedWritingBench design + results
  extraction_prompts_v3/              # 100 papers with v3 two-phase extraction
    {paper-slug}.txt                  # Experimental log (from JATS XML)
    {paper-slug}.extracted.json       # Statistical sentences + methods
  results/
    {paper-slug}/
      skill_v3_orchestrated/          # Orchestrated pipeline output
      baseline_v3/                    # Single-agent baseline output
      llm_judge.json                  # 8-axis scoring
  scripts/                            # Benchmark analysis tools
  test-cases/                         # 143 test cases
  ground_truth/                       # Published paper metadata
```

## Benchmark: Skill vs Baseline

Our benchmark compares the orchestrated pipeline against a single-agent baseline:

- **Skill condition** (`skill_v3_orchestrated`): Full 5-stage multi-skill pipeline
- **Baseline condition** (`baseline_v3`): Single agent receives the same extraction inputs and writes the paper in one pass

Both conditions use identical v3 extraction inputs. The judge scores both on the same 8-axis rubric (including figures) without knowing which is which.

See `benchmark/README.md` for full methodology, scripts, and results.

## Comparison to PaperOrchestra

| Feature | PaperOrchestra | Bio Paper Orchestra |
|---------|---------------|---------------------|
| Architecture | Multi-agent skill pipeline | Multi-skill orchestrated pipeline (same pattern) |
| Number of skills | 6 sub-skills | 6 sub-skills (orchestrator + 5 agents) |
| Literature discovery | Semantic Scholar + web | PubMed + bioRxiv + ClinicalTrials + web + S2 |
| Citation verification | Semantic Scholar API | PubMed MCP + DOI/arXiv lookup + S2 fallback |
| Figure generation | Plotting agent | plot-agent with data traceability + schematic/placeholder fallback |
| Anti-leakage | Yes | Yes, enforced at writing + refinement stages |
| Refinement scoring | 6 axes | 8 axes (includes correctness + figures) |
| Target domain | AI / ML papers | Biomedical / life sciences |
| Benchmark corpus | PaperWritingBench (200 AI papers) | BiomedWritingBench (143 biomedical test cases) |

## References

- [PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://arxiv.org/abs/2604.05018) (Song et al., 2025)
- [PaperOrchestra Project Page](https://yiwen-song.github.io/paper_orchestra/)
- [Ar9av/PaperOrchestra skill pack](https://github.com/Ar9av/PaperOrchestra) (architectural inspiration)

## License

MIT
