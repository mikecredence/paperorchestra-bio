---
name: paper-builder
description: >
  Automated AI research paper writing using a multi-agent pipeline inspired by
  PaperOrchestra. Use this skill whenever a user wants to write, draft, or generate
  an academic research paper, conference manuscript, or scientific publication from
  their idea summaries, experimental results, or lab notes. Also trigger when users
  say things like "write my paper", "draft a manuscript", "turn my results into a
  paper", "generate a LaTeX paper", "help me write up my research", "create a
  conference submission", or any request to produce a structured academic document
  (with abstract, related work, methods, experiments, conclusion). This skill
  handles the full pipeline: outlining, literature review with verified citations,
  figure generation, LaTeX writing, and iterative refinement. It produces a
  submission-ready PDF. Even partial requests like "write the related work section"
  or "help with my literature review for a paper" should trigger this skill.
---

# Paper Builder

A multi-agent pipeline for automated AI research paper writing, inspired by
[PaperOrchestra](https://arxiv.org/abs/2604.05018). Transforms unstructured
pre-writing materials (idea summaries, experimental logs) into submission-ready
LaTeX manuscripts with verified citations, generated figures, and iterative
refinement.

## When to Use

This skill is for turning research materials into a complete academic paper. The
user typically has some combination of:

- An **idea summary** (what the method does, why it matters)
- **Experimental results** (tables, metrics, comparisons)
- A **target venue** (e.g., CVPR, ICLR, NeurIPS, AAAI, a journal)
- Optionally: a LaTeX template, style file, or formatting guidelines

The output is a compiled PDF manuscript with proper LaTeX formatting, BibTeX
citations, generated figures/tables, and polished academic prose.

---

## Pipeline Overview

The pipeline has **5 sequential stages**, with stages 2 and 3 running in parallel
(but executed sequentially here since we lack true parallelism). Each stage builds
on the outputs of prior stages.

```
User Inputs (idea + results + venue)
        │
        ▼
┌─────────────────┐
│  1. OUTLINE      │  → Structured JSON plan
│     AGENT        │    (sections, lit strategy, plot plan)
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────────┐
│2. PLOT │ │3. LITERATURE│  → Figures + verified BibTeX
│  AGENT │ │   AGENT     │    + drafted Intro & Related Work
└───┬────┘ └─────┬──────┘
    └────┬───────┘
         ▼
┌─────────────────┐
│  4. WRITING      │  → Full LaTeX manuscript
│     AGENT        │
└────────┬────────┘
         ▼
┌─────────────────┐
│  5. REFINEMENT   │  → Polished, submission-ready PDF
│     AGENT        │
└─────────────────┘
```

---

## Step 0: Gather and Validate Inputs

Before starting the pipeline, collect and organize the user's materials.

### Required inputs
1. **Idea Summary**: The core contribution, methodology, and motivation. Can be
   sparse (high-level description) or dense (with equations, formal definitions).
2. **Experimental Log**: Results tables, metrics, ablation data, comparisons
   against baselines. Raw numbers are ideal.
3. **Target Venue / Format**: Conference name or journal, which determines the
   LaTeX template and style (single-column vs double-column, page limits, etc.).

### Optional inputs
- LaTeX template / `.cls` / `.sty` files
- Existing figures or diagrams the user wants included
- A list of must-cite references
- Specific section structure requests

If the user provides incomplete inputs, ask for what's missing. At minimum you need
an idea summary and some results. If no venue is specified, default to a clean
single-column format (e.g., NeurIPS-style).

### Working directory setup

```bash
mkdir -p /home/claude/paper-build/{outline,literature,figures,latex,output}
```

Copy any user-uploaded files from `/mnt/user-data/uploads/` into
`/home/claude/paper-build/`.

---

## Step 1: Outline Agent

**Goal**: Produce a structured JSON outline that guides all downstream agents.

Read `references/outline-agent.md` for the full prompt template and output schema.

The outline must contain:
1. **Paper metadata**: title, authors placeholder, abstract sketch
2. **Section plan**: ordered list of sections, each with a brief description of
   what it should cover and approximate length
3. **Visualization plan**: what figures/tables to create (type, data source,
   caption sketch)
4. **Literature search strategy**: macro-level queries (broad context for intro)
   and micro-level queries (specific method clusters for related work)
5. **Citation hints**: datasets, methods, metrics, and baselines mentioned in the
   user's materials that need citations

Write the outline to `/home/claude/paper-build/outline/outline.json`.

Review the outline with the user before proceeding. This is the most important
checkpoint — the structure drives everything downstream.

---

## Step 2: Plot Agent

**Goal**: Generate publication-quality figures from the experimental data.

Read `references/plot-agent.md` for detailed instructions.

For each entry in the visualization plan:
1. Parse the relevant data from the experimental log
2. Generate the figure using matplotlib/seaborn with academic styling
3. Save as both `.pdf` and `.png` to `/home/claude/paper-build/figures/`
4. Generate a LaTeX `\includegraphics` snippet and caption

### Academic figure standards
- Use a consistent color palette (colorblind-friendly: blue/orange/green)
- Font size ≥ 8pt in all labels, matching the paper body font
- Vector formats (PDF) for plots, PNG for raster images
- White backgrounds, minimal chartjunk
- Bold the best result in tables

Run `scripts/generate_figures.py` or write figure code inline — see the reference
file for the template.

---

## Step 3: Literature Agent

**Goal**: Discover, verify, and organize citations; draft Introduction and Related
Work sections.

Read `references/literature-agent.md` for the full process.

This is the most critical differentiation point. The process is:

### Phase 1: Discovery
Use web search to find relevant papers for each query in the literature search
strategy. For each macro query (intro context) and micro query (related work
cluster), search with queries like:
- `"{method name}" site:arxiv.org`
- `"{task name} survey" recent`
- `"{baseline name}" paper`

Collect candidate paper titles, authors, years, and venues.

### Phase 2: Verification
For every candidate citation, verify it actually exists. Use **two methods**:

**Primary (always available):** Use web search to verify each paper. Search for
the exact title in quotes. A paper is verified if you can find it on arxiv.org,
a conference proceedings page, or a publisher's site (ACM, IEEE, Springer, etc.)
with matching title, authors, and year.

**Secondary (when network allows):** Use the Semantic Scholar API script:
```python
python3 scripts/verify_citation.py "Paper Title Here"
```
This searches the API, fuzzy-matches titles, and returns structured metadata.
Note: this requires network access to `api.semanticscholar.org`. If the API is
unreachable (network restrictions), fall back to web search verification only.

**Discard any citation that cannot be verified by at least one method.** This
prevents hallucinated references — the single most damaging failure mode in
automated paper writing.

### Phase 3: BibTeX Generation
Compile all verified citations into a `.bib` file at
`/home/claude/paper-build/literature/references.bib`.

### Phase 4: Section Drafting
Using the verified citations and the outline, draft:
- **Introduction**: Broad context → gap → contribution → outline of paper
- **Related Work**: Organized by the micro-level clusters from the outline,
  positioning the user's method against prior art

Target: cite at least 25-50 references. Ensure ≥ 90% of gathered citations are
actively used in the text.

---

## Step 4: Writing Agent

**Goal**: Author the complete LaTeX manuscript.

Read `references/writing-agent.md` for section-by-section guidance.

Using the outline, verified citations, generated figures, and the user's
experimental data, write:

1. **Abstract** (~150-250 words): problem → approach → key results → impact
2. **Introduction** (from literature agent, refined to fit)
3. **Related Work** (from literature agent, refined to fit)
4. **Method / Approach**: Formal description of the proposed method with equations,
   algorithms, and architecture details drawn from the idea summary
5. **Experiments**: Setup (datasets, metrics, baselines, implementation details) →
   Main results (tables from experimental log) → Ablation studies → Analysis
6. **Conclusion**: Summary of contributions, limitations, future work

### LaTeX compilation

```bash
cd /home/claude/paper-build/latex/
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Run this cycle and fix any compilation errors. Common issues:
- Missing packages → add `\usepackage{...}`
- Undefined citations → check `.bib` keys match `\cite{...}` commands
- Figure paths → ensure paths are relative to the `.tex` file
- Overfull hboxes → adjust table column widths or figure sizes

---

## Step 5: Refinement Agent

**Goal**: Iteratively improve the manuscript through simulated self-review.

Read `references/refinement-agent.md` for the review criteria and process.

Perform **up to 3 refinement rounds**:

### Each round:
1. **Review**: Read the compiled PDF and evaluate against these axes:
   - Clarity and logical flow
   - Technical rigor and correctness
   - Completeness (are all claims supported by evidence?)
   - Writing quality (grammar, conciseness, academic tone)
   - Formatting and presentation
   - Citation adequacy

2. **Critique**: Produce specific, actionable feedback (not vague suggestions).
   Example: "Section 4.2 claims 'significant improvement' but Table 2 shows only
   0.3% gain — either temper the language or add statistical significance tests."

3. **Revise**: Apply the feedback to the LaTeX source.

4. **Recompile** and verify the changes improved quality.

### Stopping criteria
- Stop after 3 rounds, or
- Stop if a round produces no substantive changes

### Important constraints
- Never fabricate results or add data not present in the experimental log
- If a reviewer comment asks for experiments that don't exist, note this as a
  limitation rather than inventing data
- Preserve the user's core claims and methodology — refinement adjusts prose
  and presentation, not the science

---

## Step 6: Deliver

1. Copy the final PDF to `/mnt/user-data/outputs/`
2. Also copy the LaTeX source folder so the user can make further edits
3. Present the files to the user with a brief summary of what was produced

```bash
cp /home/claude/paper-build/latex/main.pdf /mnt/user-data/outputs/paper.pdf
cp -r /home/claude/paper-build/latex/ /mnt/user-data/outputs/paper-source/
```

---

## Key Principles

1. **Never hallucinate citations.** Every `\cite{}` must correspond to a verified
   entry in the `.bib` file. Use Semantic Scholar verification for every reference.

2. **Data fidelity.** Numbers in tables and claims in text must come directly from
   the user's experimental log. Never invent results.

3. **User checkpoint at outline stage.** The outline determines everything
   downstream. Get user approval before proceeding.

4. **Academic tone.** Write in third person, present tense for general claims,
   past tense for specific experiments. Avoid first person except in the
   introduction's contribution list ("We propose...").

5. **Iterative compilation.** Compile LaTeX after every major change. Fix errors
   immediately rather than accumulating them.

6. **Progressive disclosure.** Read the reference files for each agent only when
   you reach that stage — don't load everything at once.

---

## Reference Files

Read these as you reach each stage:

| Stage | File | When to read |
|-------|------|-------------|
| Outline | `references/outline-agent.md` | Step 1 |
| Figures | `references/plot-agent.md` | Step 2 |
| Literature | `references/literature-agent.md` | Step 3 |
| Writing | `references/writing-agent.md` | Step 4 |
| Refinement | `references/refinement-agent.md` | Step 5 |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/verify_citation.py` | Verify citations via Semantic Scholar API |
| `scripts/compile_latex.sh` | Full LaTeX build cycle (pdflatex + bibtex) |
| `scripts/academic_plots.py` | Reusable academic figure styling utilities |
