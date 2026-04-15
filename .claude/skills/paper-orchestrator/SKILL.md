---
name: paper-orchestrator
description: >
  Orchestrates the multi-agent paper writing pipeline. This is the TOP-LEVEL
  skill that coordinates 5 sub-skills (outline-agent, literature-agent,
  plot-agent, writing-agent, refinement-agent) in sequence with validation
  gates between stages. Use this skill instead of paper-builder when you want
  the full multi-agent pipeline with proper stage isolation. Trigger on: "write
  my paper", "draft a manuscript", "generate a LaTeX paper", "orchestrate paper
  writing", "run the paper pipeline", or any request to produce a structured
  academic document. This skill manages the full pipeline: it invokes each
  sub-skill via the Skill tool, validates outputs between stages, and enforces
  quality gates before advancing.
---

# Paper Orchestrator

Coordinates a 5-stage multi-agent pipeline for academic paper writing. Each stage
is a **separate skill invocation** with validated handoffs.

## Architecture

```
User Inputs (idea + results + venue)
        │
        ▼
┌──────────────────────┐
│  Stage 0: INIT       │  → workspace/ directory + validated inputs
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Stage 1: OUTLINE    │  → workspace/outline.json
│  Skill: outline-agent│
└──────────┬───────────┘
           │  GATE: outline.json exists + valid schema
           ▼
┌──────────────────────┐
│  Stage 2: LITERATURE │  → workspace/references.bib + intro_relwork.tex
│  Skill: literature-  │
│         agent        │
└──────────┬───────────┘
           │  GATE: .bib has >= 10 entries, no orphan cites
           ▼
┌──────────────────────┐
│  Stage 2.5: PLOT     │  → workspace/figures/*.pdf + figures.tex
│  Skill: plot-agent   │
└──────────┬───────────┘
           │  GATE: figures.tex exists, >= 1 figure generated
           ▼
┌──────────────────────┐
│  Stage 3: WRITING    │  → workspace/main.tex (full manuscript)
│  Skill: writing-agent│
└──────────┬───────────┘
           │  GATE: main.tex compiles or is valid LaTeX
           ▼
┌──────────────────────┐
│  Stage 4: REFINEMENT │  → workspace/main.tex (improved) + scores
│  Skill: refinement-  │
│         agent        │
└──────────┬───────────┘
           ▼
        OUTPUT: final main.tex + references.bib + figures/
```

## Stage 0: Initialize Workspace

Before invoking any sub-skill, set up the workspace:

1. Create the workspace directory structure:
```
{output_dir}/
├── inputs/
│   ├── idea_summary.md       (copy from user's materials)
│   └── experimental_log.md   (copy from user's materials)
├── outline.json              (Stage 1 output)
├── references.bib            (Stage 2 output)
├── intro_relwork.tex         (Stage 2 output)
├── main.tex                  (Stage 3/4 output)
└── snapshots/                (refinement rollback)
    ├── round_0/
    ├── round_1/
    └── round_2/
```

2. Copy the user's input files into `inputs/`.

3. Validate that we have at minimum:
   - An idea summary or abstract describing what the paper is about
   - Experimental results (tables, metrics, numbers)
   - A target venue (default: single-column format if none specified)

If inputs are incomplete, ask the user before proceeding.

## Stage 1: Invoke Outline Agent

**Invoke the `outline-agent` skill** using the Skill tool:

```
Skill("outline-agent", args="workspace={output_dir}")
```

The outline agent will:
- Read `inputs/idea_summary.md` and `inputs/experimental_log.md`
- Produce `outline.json` with section plan, literature strategy, and table plan

### Gate Check (after outline-agent returns)
Verify that `{output_dir}/outline.json` exists and contains:
- [ ] `sections` array with at least 4 entries
- [ ] `literature_strategy` with search queries
- [ ] `table_plan` with at least 1 planned table

If the gate fails, re-invoke outline-agent with feedback about what's missing.

## Stage 2: Invoke Literature Agent

**Invoke the `literature-agent` skill** using the Skill tool:

```
Skill("literature-agent", args="workspace={output_dir}")
```

The literature agent will:
- Read `outline.json` for search strategy
- Use PubMed, bioRxiv, web search to find and verify citations
- Produce `references.bib` and `intro_relwork.tex`

### Gate Check (after literature-agent returns)
- [ ] `references.bib` exists and has >= 10 BibTeX entries
- [ ] Each BibTeX entry has title, author, year, and journal/booktitle
- [ ] No duplicate keys in the .bib file
- [ ] `intro_relwork.tex` exists (optional — writing agent can draft these if missing)

If the gate fails, re-invoke literature-agent with feedback.

## Stage 2.5: Invoke Plot Agent

**Invoke the `plot-agent` skill** using the Skill tool:

```
Skill("plot-agent", args="workspace={output_dir}")
```

The plot agent will:
- Read `outline.json` for table_plan and figure hints
- Read `inputs/experimental_log.md` for numerical data
- Generate matplotlib figures for data-grounded comparisons,
  schematic diagrams for structural descriptions, and placeholder
  figures for data not present in the extraction
- Write figures to `{output_dir}/figures/` as .pdf and .png
- Write LaTeX snippets to `{output_dir}/figures/figures.tex`

### Gate Check (after plot-agent returns)
- [ ] `figures/` directory exists
- [ ] At least 1 figure generated (.pdf file)
- [ ] `figures.tex` exists with `\includegraphics` snippets
- [ ] No fabricated numerical values (all plotted data traces to experimental log)

If the gate fails, re-invoke plot-agent with feedback.

## Stage 3: Invoke Writing Agent

**Invoke the `writing-agent` skill** using the Skill tool:

```
Skill("writing-agent", args="workspace={output_dir}")
```

The writing agent will:
- Read `outline.json`, `references.bib`, `intro_relwork.tex`, `figures/figures.tex`
- Read `inputs/idea_summary.md` and `inputs/experimental_log.md`
- Produce complete `main.tex` manuscript with embedded figures

### Gate Check (after writing-agent returns)
- [ ] `main.tex` exists and is > 100 lines
- [ ] All `\cite{}` keys have matching entries in `references.bib`
- [ ] All numerical claims trace back to the experimental log
- [ ] No author names, URLs, or details from memory (anti-leakage)

If the gate fails, provide specific feedback and re-invoke writing-agent.

## Stage 4: Invoke Refinement Agent

Before refinement, create a snapshot:
```bash
cp {output_dir}/main.tex {output_dir}/snapshots/round_0/main.tex
```

**Invoke the `refinement-agent` skill** using the Skill tool:

```
Skill("refinement-agent", args="workspace={output_dir}")
```

The refinement agent will:
- Read `main.tex` and score it on 7 axes (0-100)
- Apply revisions and re-score
- Up to 3 rounds with rollback if score decreases
- Write final improved `main.tex`

### Gate Check (after refinement-agent returns)
- [ ] Final `main.tex` exists
- [ ] Score report exists or was logged

## Stage 5: Finalize and Deliver

1. Copy `main.tex` and `references.bib` to the final output location
2. Report the pipeline summary:
   - Outline: number of sections planned
   - Literature: number of citations found and verified
   - Writing: manuscript length (lines)
   - Refinement: score progression across rounds
3. Present the output to the user

## Critical Rules

1. **Each stage MUST be a separate Skill invocation.** Do not combine stages.
2. **Validate outputs between stages.** Do not advance if a gate check fails.
3. **Anti-leakage**: All content comes from user inputs, not from memory.
4. **Data fidelity**: Numbers in the paper must match the experimental log exactly.
5. **No hallucinated citations**: Every \cite{} must have a verified .bib entry.

## Arguments

The orchestrator accepts these arguments:
- `workspace=<path>` — output directory for all artifacts
- `idea=<path>` — path to idea summary / extraction prompt
- `results=<path>` — path to experimental log / extracted JSON
- `venue=<name>` — target venue (default: Nature Communications style)
