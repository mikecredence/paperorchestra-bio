---
name: paper-builder
description: >
  Automated research paper writing using a multi-agent pipeline inspired by
  PaperOrchestra (arXiv:2604.05018). Use this skill whenever a user wants to
  write, draft, or generate an academic research paper, conference manuscript,
  or scientific publication from their idea summaries, experimental results, or
  lab notes. Also trigger when users say things like "write my paper", "draft a
  manuscript", "turn my results into a paper", "generate a LaTeX paper", "help
  me write up my research", "create a conference submission", or any request to
  produce a structured academic document (with abstract, related work, methods,
  experiments, conclusion). This skill handles the full pipeline: outlining,
  literature review with verified citations, figure generation, LaTeX writing,
  and iterative refinement. It produces a submission-ready PDF. Even partial
  requests like "write the related work section" or "help with my literature
  review for a paper" should trigger this skill. Supports biomedical papers with
  bioRxiv/ClinicalTrials MCP integration.
---

# Paper Builder

A multi-agent pipeline for automated research paper writing, inspired by
[PaperOrchestra](https://arxiv.org/abs/2604.05018). Transforms unstructured
pre-writing materials (idea summaries, experimental logs) into submission-ready
LaTeX manuscripts with verified citations, generated figures, and iterative
refinement.

## When to Use

This skill is for turning research materials into a complete academic paper. The
user typically has some combination of:

- An **idea summary** (what the method does, why it matters)
- **Experimental results** (tables, metrics, comparisons)
- A **target venue** (e.g., CVPR, ICLR, NeurIPS, AAAI, Nature Methods, PLOS ONE)
- Optionally: a LaTeX template, style file, or formatting guidelines

The output is a compiled PDF manuscript with proper LaTeX formatting, BibTeX
citations, generated figures/tables, and polished academic prose.

---

## Available MCP Tools

This skill integrates with the following MCP tools for enhanced literature
discovery and citation verification:

### bioRxiv MCP (biological/medical preprints)
- `search_preprints` — Search bioRxiv/medRxiv by keyword, author, date range
- `get_preprint` — Full preprint details by DOI
- `search_published_preprints` — Check if preprints have peer-reviewed journal versions
- `get_categories` — List bioRxiv subject categories

### ClinicalTrials MCP (clinical/medical papers)
- `search_trials` — Find trials by condition, intervention, status
- `get_trial_details` — Protocol details, endpoints, enrollment
- `search_by_sponsor` — Pipeline analysis by company/institution
- `analyze_endpoints` — Compare outcome measures across trials
- `search_investigators` — Find PIs and research sites

### PubMed MCP (peer-reviewed biomedical literature — 37M+ articles)
- `search_articles` — Search by keyword, author, MeSH terms, publication type, date
- `get_article_metadata` — Full metadata for specific PMIDs
- `find_related_articles` — Discover similar articles (citation graph expansion)
- `get_full_text_article` — Full text from PubMed Central (~6M articles)
- `convert_article_ids` — Convert between PMID, PMCID, and DOI
- `lookup_article_by_citation` — Match partial citations to PMIDs

### Semantic Scholar API (citation verification)
- Used via `scripts/verify_citation.py` for all citation verification
- Supports API key via `SEMANTIC_SCHOLAR_API_KEY` env variable
- DOI and arXiv ID direct lookup for higher accuracy
- Cutoff date enforcement for venue submission deadlines

---

## Pipeline Overview

The pipeline has **5 sequential stages** with validation gates between them.

```
User Inputs (idea + results + venue)
        │
        ▼
┌─────────────────────┐
│  0. WORKSPACE INIT   │  → Validated inputs + directory structure
└────────┬────────────┘
         │
         ▼
┌─────────────────┐
│  1. OUTLINE      │  → Structured JSON plan
│     AGENT        │    (sections, lit strategy, plot plan)
└────────┬────────┘
         │  ← USER CHECKPOINT
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────────┐
│2. PLOT │ │3. LITERATURE│  → Figures + verified BibTeX
│  AGENT │ │   AGENT     │    + drafted Intro & Related Work
└───┬────┘ └─────┬──────┘   (bioRxiv + ClinicalTrials + S2 API)
    └────┬───────┘
         ▼
┌─────────────────┐
│  4. WRITING      │  → Full LaTeX manuscript
│     AGENT        │    + anti-leakage checks
│                  │    + citation audit gates
└────────┬────────┘
         ▼
┌─────────────────┐
│  5. REFINEMENT   │  → Polished, submission-ready PDF
│     AGENT        │    (score-delta tracking + rollback)
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
- Submission deadline (for citation cutoff date enforcement)

If the user provides incomplete inputs, ask for what's missing. At minimum you need
an idea summary and some results. If no venue is specified, default to a clean
single-column format (e.g., NeurIPS-style).

### Working directory setup

```bash
python3 scripts/init_workspace.py --base-dir /home/claude/paper-build
```

This creates the full workspace structure including `snapshots/` for refinement
rollback and initializes the `worklog.json`.

Then validate inputs:
```bash
python3 scripts/init_workspace.py --validate --base-dir /home/claude/paper-build
```

Copy any user-uploaded files into `/home/claude/paper-build/`.

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
- Font size >= 8pt in all labels, matching the paper body font
- Vector formats (PDF) for plots, PNG for raster images
- White backgrounds, minimal chartjunk
- Bold the best result in tables

---

## Step 3: Literature Agent

**Goal**: Discover, verify, and organize citations; draft Introduction and Related
Work sections.

Read `references/literature-agent.md` for the full process.

### Multi-channel discovery
Use **all available channels** in parallel for maximum coverage:

1. **Web search** — broadest coverage, always available
2. **PubMed MCP** — `search_articles` for 37M+ peer-reviewed biomedical papers.
   Use `find_related_articles` for citation graph expansion. Gold standard for
   biomedical literature.
3. **bioRxiv MCP** — `search_preprints` for biomedical preprints not yet indexed
   elsewhere. Always check `search_published_preprints` for journal versions.
4. **ClinicalTrials MCP** — `search_trials` for clinical trial citations,
   `analyze_endpoints` for protocol comparisons
5. **Citation graph expansion** — follow references of the most relevant papers
   using PubMed `find_related_articles` + Semantic Scholar

### Verification (mandatory for ALL citations)
**Primary**: Semantic Scholar API via `scripts/verify_citation.py`
- Supports DOI and arXiv ID direct lookup
- API key support for higher throughput
- Cutoff date enforcement
- Built-in deduplication

**Fallback**: bioRxiv MCP → web search → manual verification

**Discard any citation that cannot be verified.** This prevents hallucinated
references — the single most damaging failure mode.

### Citation targets
- Collect **60-80 candidates**, verify down to **45-50 unique citations**
- Ensure >= 90% of verified pool is actively cited in text
- Run `scripts/citation_audit.py` to enforce programmatically

---

## Step 4: Writing Agent

**Goal**: Author the complete LaTeX manuscript with anti-leakage safeguards.

Read `references/writing-agent.md` for section-by-section guidance.

### Anti-leakage protocol
All content must be generated **solely from user-provided inputs**. Do not
reproduce text from pre-training memory. See the writing agent reference for
the full protocol.

### Post-compilation validation gates
After LaTeX compilation, run these mandatory checks:

1. **Citation audit**: `scripts/citation_audit.py --tex main.tex --bib references.bib`
2. **Anti-leakage verification**: Review for author names, URLs, or details not in inputs
3. **LaTeX syntax**: Zero errors, zero undefined references

---

## Step 5: Refinement Agent

**Goal**: Iteratively improve the manuscript with score-tracked review and rollback.

Read `references/refinement-agent.md` for the review criteria and process.

### Key improvements over basic refinement:
- **0-100 scoring** (not 1-5) on 6 axes for finer-grained tracking
- **Score-delta ACCEPT/REVERT** decision after each round
- **Filesystem snapshots** for rollback if a revision makes things worse
- **Append-only worklog** tracking all changes across iterations
- **Anti-gaming safeguards** preventing artificial score inflation
- **bioRxiv preprint upgrade** — checks if cited preprints now have journal versions
- **ClinicalTrials validation** — verifies trial details against registry

### Stopping criteria
- 3 rounds completed, OR
- All axes >= 80 with no critical issues, OR
- Score delta < 1.0 for two consecutive rounds, OR
- Overall score decreased (after rollback)

---

## Step 6: Deliver

1. Copy the final PDF to the output directory
2. Also copy the LaTeX source folder so the user can make further edits
3. Present the worklog summary showing score progression across refinement rounds
4. Report final citation statistics (count, coverage, verification rate)

---

## Key Principles

1. **Never hallucinate citations.** Every `\cite{}` must correspond to a verified
   entry in the `.bib` file. Use Semantic Scholar as primary verification.

2. **Data fidelity.** Numbers in tables and claims in text must come directly from
   the user's experimental log. Never invent results.

3. **Anti-leakage.** All text must be generated from provided inputs, not from
   memory of known papers. This prevents plagiarism and information leakage.

4. **User checkpoint at outline stage.** The outline determines everything
   downstream. Get user approval before proceeding.

5. **Academic tone.** Write in third person, present tense for general claims,
   past tense for specific experiments. Avoid first person except in the
   introduction's contribution list ("We propose...").

6. **Iterative compilation.** Compile LaTeX after every major change. Fix errors
   immediately rather than accumulating them.

7. **Progressive disclosure.** Read the reference files for each agent only when
   you reach that stage — don't load everything at once.

8. **Score-tracked refinement.** Use quantitative scoring with rollback to ensure
   each revision actually improves the manuscript.

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
| `scripts/init_workspace.py` | Initialize workspace + validate inputs |
| `scripts/verify_citation.py` | Verify citations via Semantic Scholar API (with DOI/arXiv lookup, dedup, cutoff) |
| `scripts/citation_audit.py` | Orphaned citation detection + coverage enforcement |
| `scripts/compile_latex.sh` | Full LaTeX build cycle (pdflatex + bibtex) |
| `scripts/academic_plots.py` | Reusable academic figure styling utilities |
