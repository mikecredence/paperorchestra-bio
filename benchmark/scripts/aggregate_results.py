#!/usr/bin/env python3
"""
Aggregate BiomedWritingBench evaluation results across all test cases.

Usage:
    python aggregate_results.py
    python aggregate_results.py --results-dir benchmark/results/ --figures
"""

import sys
import json
import argparse
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from config import RESULTS_DIR, TEST_CASES_DIR


def load_all_results(results_dir: Path) -> list[dict]:
    """Load all per-paper evaluation.json files."""
    results = []
    for eval_file in sorted(results_dir.glob("*/evaluation.json")):
        data = json.loads(eval_file.read_text(encoding="utf-8"))
        results.append(data)
    return results


def compute_statistics(values: list[float]) -> dict:
    """Compute mean, median, std, min, max for a list of values."""
    if not values:
        return {"mean": None, "median": None, "std": None, "min": None, "max": None, "n": 0}

    import math
    n = len(values)
    mean = sum(values) / n
    sorted_vals = sorted(values)
    median = sorted_vals[n // 2] if n % 2 else (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2
    variance = sum((x - mean)**2 for x in values) / n if n > 1 else 0
    std = math.sqrt(variance)

    return {
        "mean": round(mean, 2),
        "median": round(median, 2),
        "std": round(std, 2),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "n": n,
    }


def aggregate(results: list[dict], test_cases_dir: Path) -> dict:
    """Aggregate metrics across all evaluated test cases."""
    # Load metadata for subfield grouping
    subfield_map = {}
    for case_dir in test_cases_dir.iterdir():
        if not case_dir.is_dir():
            continue
        meta_path = case_dir / "metadata.json"
        if meta_path.exists():
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            subfield_map[case_dir.name] = meta.get("category", "unknown")

    # Collect metrics by subfield
    by_subfield = defaultdict(lambda: {
        "citation_f1": [], "citation_precision": [], "citation_recall": [],
        "figure_delta": [], "table_delta": [], "citation_delta": [],
        "compilation_success": [],
        "judge_scores": defaultdict(list),
    })

    overall = {
        "citation_f1": [], "citation_precision": [], "citation_recall": [],
        "figure_delta": [], "table_delta": [], "citation_delta": [],
        "compilation_success": [],
        "judge_scores": defaultdict(list),
    }

    for result in results:
        paper_id = result.get("paper_id", "unknown")
        subfield = subfield_map.get(paper_id, "unknown")
        buckets = [by_subfield[subfield], overall]

        # Structural metrics
        sm = result.get("structural_metrics", {})
        if sm:
            for bucket in buckets:
                if sm.get("compilation_success") is not None:
                    bucket["compilation_success"].append(1 if sm["compilation_success"] else 0)
                if sm.get("figure_delta") is not None:
                    bucket["figure_delta"].append(abs(sm["figure_delta"]))
                if sm.get("table_delta") is not None:
                    bucket["table_delta"].append(abs(sm["table_delta"]))
                if sm.get("citation_delta") is not None:
                    bucket["citation_delta"].append(abs(sm["citation_delta"]))

        # Citation F1
        cf1 = result.get("citation_f1", {})
        if cf1 and "f1" in cf1:
            for bucket in buckets:
                bucket["citation_f1"].append(cf1["f1"])
                bucket["citation_precision"].append(cf1.get("precision", 0))
                bucket["citation_recall"].append(cf1.get("recall", 0))

        # LLM judge scores
        judge = result.get("llm_judge", {})
        if judge:
            evals = judge.get("evaluations", [])
            for ev in evals:
                axis = ev.get("axis", "unknown")
                score = ev.get("score") or ev.get("score_a")
                if score is not None:
                    for bucket in buckets:
                        bucket["judge_scores"][axis].append(score)

    # Build summary
    def summarize_bucket(bucket):
        summary = {
            "compilation_rate": round(sum(bucket["compilation_success"]) / len(bucket["compilation_success"]) * 100, 1) if bucket["compilation_success"] else None,
            "citation_f1": compute_statistics(bucket["citation_f1"]),
            "citation_precision": compute_statistics(bucket["citation_precision"]),
            "citation_recall": compute_statistics(bucket["citation_recall"]),
            "figure_delta_abs": compute_statistics(bucket["figure_delta"]),
            "table_delta_abs": compute_statistics(bucket["table_delta"]),
            "citation_delta_abs": compute_statistics(bucket["citation_delta"]),
            "judge_scores": {
                axis: compute_statistics(scores)
                for axis, scores in bucket["judge_scores"].items()
            },
        }
        return summary

    return {
        "total_evaluated": len(results),
        "overall": summarize_bucket(overall),
        "by_subfield": {
            sf: summarize_bucket(bucket) for sf, bucket in sorted(by_subfield.items())
        },
    }


def generate_markdown_table(summary: dict) -> str:
    """Generate a markdown summary table."""
    lines = ["## BiomedWritingBench Results Summary\n"]

    overall = summary["overall"]
    lines.append(f"**Total evaluated:** {summary['total_evaluated']}\n")

    # Citation metrics
    if overall["citation_f1"]["n"] > 0:
        lines.append("### Citation Quality\n")
        lines.append("| Metric | Mean | Median | Std | N |")
        lines.append("|--------|------|--------|-----|---|")
        for metric in ["citation_f1", "citation_precision", "citation_recall"]:
            s = overall[metric]
            lines.append(f"| {metric} | {s['mean']} | {s['median']} | {s['std']} | {s['n']} |")
        lines.append("")

    # Judge scores
    if overall["judge_scores"]:
        lines.append("### LLM Judge Scores (0-100)\n")
        lines.append("| Axis | Mean | Median | Std | N |")
        lines.append("|------|------|--------|-----|---|")
        for axis in ["clarity", "rigor", "completeness", "writing", "presentation", "citations", "overall"]:
            if axis in overall["judge_scores"]:
                s = overall["judge_scores"][axis]
                lines.append(f"| {axis} | {s['mean']} | {s['median']} | {s['std']} | {s['n']} |")
        lines.append("")

    # Per-subfield
    if summary["by_subfield"]:
        lines.append("### By Subfield\n")
        lines.append("| Subfield | N | Citation F1 | Compile% |")
        lines.append("|----------|---|-------------|----------|")
        for sf, data in sorted(summary["by_subfield"].items()):
            n = data["citation_f1"]["n"] or "—"
            f1 = f"{data['citation_f1']['mean']}" if data["citation_f1"]["mean"] else "—"
            comp = f"{data['compilation_rate']}%" if data["compilation_rate"] is not None else "—"
            lines.append(f"| {sf} | {n} | {f1} | {comp} |")

    return "\n".join(lines)


def generate_figures(summary: dict, output_dir: Path):
    """Generate visualization plots."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("matplotlib not available, skipping figures", file=sys.stderr)
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    # Judge scores radar chart
    judge = summary["overall"].get("judge_scores", {})
    if judge:
        axes = ["clarity", "rigor", "completeness", "writing", "presentation", "citations"]
        scores = [judge.get(a, {}).get("mean", 0) or 0 for a in axes]

        angles = np.linspace(0, 2 * np.pi, len(axes), endpoint=False).tolist()
        scores_plot = scores + [scores[0]]
        angles_plot = angles + [angles[0]]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles_plot, scores_plot, alpha=0.25, color="#0072B2")
        ax.plot(angles_plot, scores_plot, color="#0072B2", linewidth=2)
        ax.set_xticks(angles)
        ax.set_xticklabels([a.title() for a in axes])
        ax.set_ylim(0, 100)
        ax.set_title("LLM Judge Scores (Mean)", pad=20)
        plt.tight_layout()
        plt.savefig(output_dir / "judge_radar.png", dpi=200)
        plt.close()
        print(f"  Saved judge_radar.png", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Aggregate BiomedWritingBench results")
    parser.add_argument("--results-dir", type=Path, default=RESULTS_DIR)
    parser.add_argument("--test-cases-dir", type=Path, default=TEST_CASES_DIR)
    parser.add_argument("--figures", action="store_true", help="Generate visualization figures")
    parser.add_argument("--markdown", type=Path, help="Output markdown summary to file")
    args = parser.parse_args()

    results = load_all_results(args.results_dir)
    if not results:
        print(f"No evaluation results found in {args.results_dir}", file=sys.stderr)
        print("Run 'batch_runner.py evaluate' first.", file=sys.stderr)
        sys.exit(1)

    summary = aggregate(results, args.test_cases_dir)

    # Print JSON summary
    summary_path = args.results_dir / "aggregate_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Summary saved to {summary_path}", file=sys.stderr)

    # Markdown table
    md = generate_markdown_table(summary)
    if args.markdown:
        args.markdown.write_text(md, encoding="utf-8")
        print(f"Markdown saved to {args.markdown}", file=sys.stderr)
    else:
        print(md)

    # Figures
    if args.figures:
        generate_figures(summary, args.results_dir / "figures")


if __name__ == "__main__":
    main()
