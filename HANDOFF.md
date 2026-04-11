# Session Handoff: BiomedWritingBench

## Repo: https://github.com/mikecredence/bio-paper-orchestra

## What Was Built This Session

### 1. Paper-Builder Skill (`.claude/skills/paper-builder/`)
Multi-agent pipeline for biomedical paper writing with 5 stages: Outline, Plot, Literature, Writing, Refinement. Integrates bioRxiv, PubMed, ClinicalTrials MCP tools. Anti-leakage protocol, score-tracked refinement with rollback, citation audit scripts.

### 2. BiomedWritingBench Dataset
- **143 test cases** across 10 biomedical subfields
- **100 papers with full-text JATS XML** extraction from bioRxiv
- **100 papers with v2 LLM-structured inputs** (PaperOrchestra-quality: 15-20 markdown tables each)
- Real ground truth reference lists from published papers

### 3. Evaluation Results (6 conditions, 120+ generated papers)
All results in `benchmark/results/{paper_id}/{condition}/`:

| Condition | Description | N papers | Avg Citations | Avg Tables |
|-----------|-------------|----------|---------------|------------|
| `baseline_paper` | Single agent + abstract inputs | 20 | 12.1 | 3.8 |
| `generated_paper` | Skill pipeline + abstract inputs | 20 | 22.5 | 4.0 |
| `baseline_rich_paper` | Single agent + XML full-text | 15 | 19.7 | 0.0 |
| `rich_paper` | Skill pipeline + XML full-text | 15 | 29.0 | 1.6 |
| `baseline_v2_paper` | Single agent + v2 LLM-structured | 20 | 8.3 | 0.1 |
| `skill_v2_paper` | Skill pipeline + v2 LLM-structured | 20 | 22.2 | 9.8 |

### 4. Key Findings So Far

**2x2 factorial (abstract conditions, n=15 paired):**
- Pipeline effect: +1.9 quality points
- Input richness effect: +2.1 quality points
- Interaction: +1.4 (synergistic — pipeline helps MORE with rich inputs)
- Overall quality: Baseline 80.2 → Skill+FullText 84.3

**V2 inputs (LLM-structured) produce dramatically more tables:**
- Skill+v2 has 9.8 tables/paper (vs 4.0 with abstract inputs)
- The structured markdown tables flow directly into LaTeX

## What Needs To Be Done Next

### Immediate (continue this run):

1. **Judge all 40 v2 papers** (skill_v2_paper + baseline_v2_paper)
   - Launch subagents to score each paper on 7 axes (0-100)
   - Same pattern as before: read main.tex, write llm_judge.json
   - 4 agents of 10 papers each should work

2. **Run the expanded factorial analysis**
   - Update `benchmark/scripts/final_analysis.py` to include v2 conditions
   - 3x2 design: Pipeline (baseline vs skill) × Input (abstract vs XML vs v2-LLM)
   - Compute Wilcoxon tests on all paired comparisons

3. **Compile all v2 papers** with TinyTeX
   - Run `benchmark/scripts/fix_and_compile.py` (update for v2 conditions)
   - Report compilation rates

### Medium-term:

4. **Rewrite the paper** with the 3x2 factorial design
   - Novel finding: extraction quality (v1 XML dump vs v2 LLM-structured) matters
   - Skill+v2 tables (9.8/paper) dramatically exceed other conditions
   - Paper draft exists at `benchmark/paper/build/latex/main.tex` (outdated, needs full rewrite)

5. **Improve the pipeline based on findings**
   - The baseline+v2 only gets 8.3 citations — why? The inputs have reference lists
   - The skill should be leveraging the v2 reference lists for citation discovery
   - Add a "reference list seeding" step to the Literature Agent

6. **Add AI Scientist v2 comparison** (optional but strengthens paper)
   - Clone from github.com/SakanaAI/AI-Scientist
   - Run on same 20 papers
   - Compare as third baseline

### Key Scripts

| Script | Purpose | Command |
|--------|---------|---------|
| `quick_metrics.py` | Structural metrics for all 6 conditions | `uv run python benchmark/scripts/quick_metrics.py` |
| `final_analysis.py` | Full factorial + Wilcoxon tests | `uv run python benchmark/scripts/final_analysis.py` |
| `fix_and_compile.py` | LaTeX compilation for all papers | `uv run python benchmark/scripts/fix_and_compile.py` |
| `compute_comparison.py` | Paired citation comparison | `uv run python benchmark/scripts/compute_comparison.py` |
| `ground_truth_comparison.py` | Generated vs published papers | `uv run python benchmark/scripts/ground_truth_comparison.py` |
| `llm_extract.py` | Generate extraction prompts for LLM | `uv run python benchmark/scripts/llm_extract.py --all` |
| `overnight_run.py` | Batch JATS XML extraction | `uv run python benchmark/scripts/overnight_run.py --all` |

### Key Data Files

| File | Content |
|------|---------|
| `benchmark/benchmark_run_20.json` | 20 papers used in original evaluation |
| `benchmark/benchmark_run_v2.json` | 20 papers used in v2 evaluation |
| `benchmark/fulltext_queue.json` | 135 candidates for future extraction |
| `benchmark/v2_extraction_batches.json` | Batch assignments for v2 extraction |
| `benchmark/results/factorial_analysis.json` | Previous 2x2 factorial results |
| `benchmark/results/comparison_results.json` | Structural comparison data |

### Judge Agent Pattern (for scoring papers)

```
For each paper, read main.tex, score on 7 axes (0-100):
clarity, rigor, completeness, writing, presentation, citations, overall

Write JSON: {
  "paper_id": "...",
  "condition": "skill_v2_paper",
  "scores": {"clarity": X, "rigor": X, ...},
  "brief_notes": "..."
}

To: benchmark/results/{paper_id}/{condition}/llm_judge.json
```

### Environment

- Python 3.12 via `uv`
- TinyTeX at `$APPDATA/TinyTeX/bin/windows/`
- GitHub CLI at `/tmp/gh/bin/gh.exe`
- GitHub: mikecredence/bio-paper-orchestra
- No Anthropic API key (use subagents for LLM tasks)
- No Semantic Scholar API key (use web search fallback)
