#!/usr/bin/env python3
"""
Batch runner for BiomedWritingBench evaluation.

Modes:
  prepare  — Generate prompt files for each test case
  evaluate — Collect metrics from completed runs
  single   — Run metrics on a single test case
  status   — Show progress across all test cases

Usage:
    python batch_runner.py prepare
    python batch_runner.py evaluate --results-dir benchmark/results/
    python batch_runner.py single --test-case benchmark/test-cases/dna-foundation-models/
    python batch_runner.py status
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))
from config import (
    BENCHMARK_DIR, TEST_CASES_DIR, GROUND_TRUTH_DIR, RESULTS_DIR,
)


def prepare_prompts(test_cases_dir: Path, output_dir: Path, skip_existing: bool = True):
    """Generate prompt files for each test case."""
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for case_dir in sorted(test_cases_dir.iterdir()):
        if not case_dir.is_dir():
            continue

        idea_path = case_dir / "idea_summary.md"
        exp_path = case_dir / "experimental_log.md"
        meta_path = case_dir / "metadata.json"

        if not all(p.exists() for p in [idea_path, exp_path, meta_path]):
            continue

        prompt_dir = output_dir / case_dir.name
        prompt_file = prompt_dir / "prompt.md"

        if skip_existing and prompt_file.exists():
            continue

        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        idea = idea_path.read_text(encoding="utf-8", errors="replace")
        exp_log = exp_path.read_text(encoding="utf-8", errors="replace")
        venue = meta.get("published_venue", "Nature Communications") or "Nature Communications"

        prompt = f"""Please write a complete research paper based on the following materials.
Use the paper-builder skill to generate a submission-ready LaTeX manuscript.

## Target Venue
{venue}

## Idea Summary
{idea}

## Experimental Log
{exp_log}

Output the complete LaTeX paper (main.tex) and BibTeX references (references.bib).
"""

        prompt_dir.mkdir(parents=True, exist_ok=True)
        prompt_file.write_text(prompt, encoding="utf-8")
        count += 1

    return count


def collect_structural_metrics(case_dir: Path, results_dir: Path) -> dict:
    """Compute structural metrics for a completed run."""
    meta_path = case_dir / "metadata.json"
    if not meta_path.exists():
        return {"error": "No metadata.json"}

    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    # Look for generated LaTeX in results
    latex_dir = results_dir / "generated_paper"
    tex_files = list(latex_dir.glob("*.tex")) if latex_dir.exists() else []
    bib_files = list(latex_dir.glob("*.bib")) if latex_dir.exists() else []
    pdf_files = list(latex_dir.glob("*.pdf")) if latex_dir.exists() else []

    # Count figures/tables in generated tex
    gen_figures = 0
    gen_tables = 0
    gen_citations = 0
    if tex_files:
        tex_content = tex_files[0].read_text(encoding="utf-8", errors="replace")
        import re
        gen_figures = len(re.findall(r'\\begin\{figure', tex_content))
        gen_tables = len(re.findall(r'\\begin\{table', tex_content))
        gen_citations = len(set(re.findall(r'\\cite[tp]?\*?\{([^}]+)\}', tex_content)))

    # Count bib entries
    gen_bib_entries = 0
    if bib_files:
        bib_content = bib_files[0].read_text(encoding="utf-8", errors="replace")
        gen_bib_entries = len(re.findall(r'@\w+\{', bib_content))

    gt_citations = meta.get("ground_truth_citation_count")
    gt_figures = meta.get("ground_truth_figure_count")
    gt_tables = meta.get("ground_truth_table_count")

    return {
        "paper_id": case_dir.name,
        "compilation_success": len(pdf_files) > 0,
        "generated_figures": gen_figures,
        "generated_tables": gen_tables,
        "generated_citations_in_text": gen_citations,
        "generated_bib_entries": gen_bib_entries,
        "ground_truth_figures": gt_figures,
        "ground_truth_tables": gt_tables,
        "ground_truth_citations": gt_citations,
        "figure_delta": (gen_figures - gt_figures) if gt_figures else None,
        "table_delta": (gen_tables - gt_tables) if gt_tables else None,
        "citation_delta": (gen_bib_entries - gt_citations) if gt_citations else None,
    }


def run_citation_f1(results_dir: Path, gt_dir: Path) -> dict | None:
    """Run citation_f1.py on a completed result."""
    bib_file = None
    for f in (results_dir / "generated_paper").glob("*.bib"):
        bib_file = f
        break

    gt_file = gt_dir / "ground_truth.json"
    if not bib_file or not gt_file.exists():
        return None

    # Call citation_f1.py
    scripts_dir = Path(__file__).parent
    try:
        result = subprocess.run(
            [sys.executable, str(scripts_dir / "citation_f1.py"),
             "--generated-bib", str(bib_file),
             "--ground-truth", str(gt_file),
             "--json"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception as e:
        return {"error": str(e)}

    return None


def evaluate_single(case_dir: Path, results_dir: Path, gt_dir: Path) -> dict:
    """Evaluate a single test case."""
    paper_id = case_dir.name
    result = {
        "paper_id": paper_id,
        "timestamp": datetime.now().isoformat(),
        "structural_metrics": None,
        "citation_f1": None,
        "llm_judge": None,
    }

    paper_results_dir = results_dir / paper_id
    paper_gt_dir = gt_dir / paper_id

    # Structural metrics
    result["structural_metrics"] = collect_structural_metrics(case_dir, paper_results_dir)

    # Citation F1 (if generated bib exists)
    if paper_results_dir.exists():
        result["citation_f1"] = run_citation_f1(paper_results_dir, paper_gt_dir)

    # Save
    paper_results_dir.mkdir(parents=True, exist_ok=True)
    eval_file = paper_results_dir / "evaluation.json"
    eval_file.write_text(json.dumps(result, indent=2), encoding="utf-8")

    return result


def show_status(test_cases_dir: Path, results_dir: Path):
    """Show progress across all test cases."""
    total = 0
    with_prompts = 0
    with_results = 0
    with_eval = 0

    batch_dir = BENCHMARK_DIR / "batch"

    for case_dir in sorted(test_cases_dir.iterdir()):
        if not case_dir.is_dir():
            continue
        total += 1

        prompt_file = batch_dir / case_dir.name / "prompt.md"
        if prompt_file.exists():
            with_prompts += 1

        result_dir = results_dir / case_dir.name
        if result_dir.exists() and list(result_dir.glob("generated_paper/*.tex")):
            with_results += 1

        eval_file = result_dir / "evaluation.json" if result_dir.exists() else None
        if eval_file and eval_file.exists():
            with_eval += 1

    print(f"=== BiomedWritingBench Status ===")
    print(f"Test cases:     {total}")
    print(f"Prompts ready:  {with_prompts}/{total}")
    print(f"Papers generated: {with_results}/{total}")
    print(f"Evaluated:      {with_eval}/{total}")


def main():
    parser = argparse.ArgumentParser(description="BiomedWritingBench batch runner")
    parser.add_argument("mode", choices=["prepare", "evaluate", "single", "status"],
                        help="Operation mode")
    parser.add_argument("--test-cases-dir", type=Path, default=TEST_CASES_DIR)
    parser.add_argument("--results-dir", type=Path, default=RESULTS_DIR)
    parser.add_argument("--ground-truth-dir", type=Path, default=GROUND_TRUTH_DIR)
    parser.add_argument("--test-case", type=Path, help="Single test case dir (for 'single' mode)")
    parser.add_argument("--skip-existing", action="store_true", default=True)
    args = parser.parse_args()

    if args.mode == "prepare":
        batch_dir = BENCHMARK_DIR / "batch"
        count = prepare_prompts(args.test_cases_dir, batch_dir, args.skip_existing)
        print(f"Generated {count} prompt files in {batch_dir}", file=sys.stderr)

    elif args.mode == "evaluate":
        args.results_dir.mkdir(parents=True, exist_ok=True)
        results = []
        for case_dir in sorted(args.test_cases_dir.iterdir()):
            if not case_dir.is_dir():
                continue
            result = evaluate_single(case_dir, args.results_dir, args.ground_truth_dir)
            results.append(result)
            status = "OK" if result["structural_metrics"].get("compilation_success") else "no paper"
            print(f"  {case_dir.name}: {status}", file=sys.stderr)

        summary_path = args.results_dir / "batch_summary.json"
        summary_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"\nEvaluated {len(results)} test cases. Summary: {summary_path}", file=sys.stderr)

    elif args.mode == "single":
        if not args.test_case:
            print("--test-case required for 'single' mode", file=sys.stderr)
            sys.exit(1)
        result = evaluate_single(args.test_case, args.results_dir, args.ground_truth_dir)
        print(json.dumps(result, indent=2))

    elif args.mode == "status":
        show_status(args.test_cases_dir, args.results_dir)


if __name__ == "__main__":
    main()
