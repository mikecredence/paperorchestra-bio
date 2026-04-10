#!/usr/bin/env python3
"""Compile all generated LaTeX papers and report success/failure."""
import os
import re
import json
import subprocess
import shutil
import tempfile
from pathlib import Path

results_dir = Path(__file__).parent.parent / "results"

# Find pdflatex
APPDATA = os.environ.get("APPDATA", "")
PDFLATEX = os.path.join(APPDATA, "TinyTeX", "bin", "windows", "pdflatex.exe")
BIBTEX = os.path.join(APPDATA, "TinyTeX", "bin", "windows", "bibtex.exe")

if not os.path.exists(PDFLATEX):
    # Try PATH
    PDFLATEX = shutil.which("pdflatex") or "pdflatex"
    BIBTEX = shutil.which("bibtex") or "bibtex"


def compile_paper(tex_path: Path, bib_path: Path | None) -> dict:
    """Compile a LaTeX paper. Returns compilation result dict."""
    result = {
        "tex_path": str(tex_path),
        "success": False,
        "pages": 0,
        "pdf_size": 0,
        "errors": [],
        "warnings": {"undefined_citations": 0, "undefined_refs": 0, "overfull": 0},
    }

    # Create temp dir for compilation (avoid polluting source)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        shutil.copy(tex_path, tmp / "main.tex")
        if bib_path and bib_path.exists():
            shutil.copy(bib_path, tmp / "references.bib")

        # Also copy any figures referenced
        tex_content = tex_path.read_text(errors="replace")
        for fig_match in re.findall(r"\\includegraphics(?:\[.*?\])?\{([^}]+)\}", tex_content):
            fig_src = tex_path.parent / fig_match
            if fig_src.exists():
                shutil.copy(fig_src, tmp / fig_match)

        try:
            # Pass 1
            r1 = subprocess.run(
                [PDFLATEX, "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                cwd=str(tmp), capture_output=True, text=True, timeout=30
            )

            if r1.returncode != 0:
                # Try without halt-on-error to get more info
                r1 = subprocess.run(
                    [PDFLATEX, "-interaction=nonstopmode", "main.tex"],
                    cwd=str(tmp), capture_output=True, text=True, timeout=30
                )

            # BibTeX (if bib exists)
            if (tmp / "main.aux").exists() and bib_path and bib_path.exists():
                subprocess.run(
                    [BIBTEX, "main"],
                    cwd=str(tmp), capture_output=True, text=True, timeout=15
                )

            # Pass 2+3
            for _ in range(2):
                subprocess.run(
                    [PDFLATEX, "-interaction=nonstopmode", "main.tex"],
                    cwd=str(tmp), capture_output=True, text=True, timeout=30
                )

            # Check result
            pdf_path = tmp / "main.pdf"
            if pdf_path.exists():
                result["success"] = True
                result["pdf_size"] = pdf_path.stat().st_size

                # Count pages from log
                log_path = tmp / "main.log"
                if log_path.exists():
                    log_content = log_path.read_text(errors="replace")
                    page_match = re.search(r"Output written on main\.pdf \((\d+) page", log_content)
                    if page_match:
                        result["pages"] = int(page_match.group(1))

                    result["warnings"]["undefined_citations"] = log_content.count("Citation") and len(re.findall(r"Citation.*undefined", log_content))
                    result["warnings"]["undefined_refs"] = len(re.findall(r"Reference.*undefined", log_content))
                    result["warnings"]["overfull"] = log_content.count("Overfull")

                # Copy PDF back to source dir
                dest_pdf = tex_path.parent / "main.pdf"
                shutil.copy(pdf_path, dest_pdf)
            else:
                result["errors"].append("No PDF produced")
                log_path = tmp / "main.log"
                if log_path.exists():
                    log = log_path.read_text(errors="replace")
                    for line in log.split("\n"):
                        if line.startswith("!"):
                            result["errors"].append(line[:200])

        except subprocess.TimeoutExpired:
            result["errors"].append("Compilation timed out")
        except FileNotFoundError:
            result["errors"].append(f"pdflatex not found at {PDFLATEX}")

    return result


# Compile all papers
all_results = {}
for condition in ["generated_paper", "baseline_paper"]:
    label = "SKILL" if condition == "generated_paper" else "BASELINE"
    compiled = 0
    failed = 0

    print(f"\n=== Compiling {label} papers ===")

    for d in sorted(results_dir.iterdir()):
        tex = d / condition / "main.tex"
        bib = d / condition / "references.bib"
        if not tex.exists():
            continue

        result = compile_paper(tex, bib)
        key = f"{d.name}/{condition}"
        all_results[key] = result

        if result["success"]:
            compiled += 1
            pages = result["pages"]
            kb = result["pdf_size"] // 1024
            undef = result["warnings"]["undefined_citations"]
            status = f"OK ({pages}p, {kb}KB" + (f", {undef} undef cites" if undef else "") + ")"
        else:
            failed += 1
            err = result["errors"][0][:60] if result["errors"] else "unknown"
            status = f"FAIL: {err}"

        print(f"  [{'+' if result['success'] else '!'}] {d.name[:45]:45s} {status}")

    total = compiled + failed
    print(f"\n  {label}: {compiled}/{total} compiled ({compiled/total*100:.0f}%)")

# Save results
with open(results_dir / "compilation_results.json", "w") as f:
    json.dump(all_results, f, indent=2)

# Summary
print(f"\n{'='*60}")
print("COMPILATION SUMMARY")
print(f"{'='*60}")
for condition, label in [("generated_paper", "Skill"), ("baseline_paper", "Baseline")]:
    papers = {k: v for k, v in all_results.items() if condition in k}
    success = sum(1 for v in papers.values() if v["success"])
    total = len(papers)
    avg_pages = sum(v["pages"] for v in papers.values() if v["success"]) / max(success, 1)
    print(f"{label:12s}: {success}/{total} compiled ({success/total*100:.0f}%), avg {avg_pages:.1f} pages")
