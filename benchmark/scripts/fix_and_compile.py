#!/usr/bin/env python3
"""Fix common LaTeX issues and recompile all papers."""
import os
import re
import json
import subprocess
import shutil
import tempfile
from pathlib import Path

results_dir = Path(__file__).parent.parent / "results"
APPDATA = os.environ.get("APPDATA", "")
PDFLATEX = os.path.join(APPDATA, "TinyTeX", "bin", "windows", "pdflatex.exe")
BIBTEX = os.path.join(APPDATA, "TinyTeX", "bin", "windows", "bibtex.exe")

# Packages not available in TinyTeX minimal — remove or replace
UNAVAILABLE_PACKAGES = {
    "multirow", "authblk", "setspace", "lineno", "caption", "subcaption",
    "xcolor", "algorithm", "algorithmic", "textcomp", "float", "placeins",
    "enumitem", "adjustbox", "makecell", "siunitx", "cleveref", "tabularx",
}

# Packages we know TinyTeX has
SAFE_PACKAGES = {
    "inputenc", "fontenc", "amsmath", "amssymb", "amsfonts",
    "graphicx", "booktabs", "hyperref", "natbib", "geometry",
}


def fix_tex(content: str) -> str:
    """Remove unavailable packages and fix common issues."""
    lines = content.split("\n")
    fixed = []
    for line in lines:
        # Remove usepackage lines for unavailable packages
        match = re.match(r"\\usepackage(?:\[.*?\])?\{(.+?)\}", line.strip())
        if match:
            pkgs = [p.strip() for p in match.group(1).split(",")]
            available = [p for p in pkgs if p not in UNAVAILABLE_PACKAGES]
            if not available:
                fixed.append("% " + line.strip() + "  % removed: package unavailable")
                continue
            elif len(available) < len(pkgs):
                pkg_str = ",".join(available)
                opts_match = re.match(r"\\usepackage(\[.*?\])?", line.strip())
                opts = opts_match.group(1) or "" if opts_match else ""
                fixed.append(f"\\usepackage{opts}{{{pkg_str}}}")
                continue

        # Remove \multirow{} commands — replace with plain text
        line = re.sub(r"\\multirow\{(\d+)\}\{[^}]*\}\{([^}]*)\}", r"\2", line)

        # Remove \rowcolor commands
        line = re.sub(r"\\rowcolor\{[^}]*\}", "", line)

        # Remove \cellcolor commands
        line = re.sub(r"\\cellcolor\{[^}]*\}", "", line)

        # Remove \color commands
        line = re.sub(r"\\color\{[^}]*\}", "", line)

        # Remove \linenumbers
        line = line.replace("\\linenumbers", "")

        # Fix \affil command (from authblk)
        line = re.sub(r"\\affil\{([^}]*)\}", "", line)

        fixed.append(line)

    return "\n".join(fixed)


def compile_paper(tex_content: str, bib_path: Path | None) -> dict:
    """Compile fixed LaTeX content. Returns result dict."""
    result = {"success": False, "pages": 0, "pdf_size": 0, "errors": []}

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        (tmp / "main.tex").write_text(tex_content, encoding="utf-8")
        if bib_path and bib_path.exists():
            shutil.copy(bib_path, tmp / "references.bib")

        try:
            # 3-pass compilation
            subprocess.run([PDFLATEX, "-interaction=nonstopmode", "main.tex"],
                           cwd=str(tmp), capture_output=True, timeout=30)

            if (tmp / "main.aux").exists() and bib_path and bib_path.exists():
                subprocess.run([BIBTEX, "main"],
                               cwd=str(tmp), capture_output=True, timeout=15)

            for _ in range(2):
                subprocess.run([PDFLATEX, "-interaction=nonstopmode", "main.tex"],
                               cwd=str(tmp), capture_output=True, timeout=30)

            pdf = tmp / "main.pdf"
            if pdf.exists():
                result["success"] = True
                result["pdf_size"] = pdf.stat().st_size

                log = (tmp / "main.log").read_text(errors="replace") if (tmp / "main.log").exists() else ""
                m = re.search(r"Output written on main\.pdf \((\d+) page", log)
                if m:
                    result["pages"] = int(m.group(1))

                result["warnings"] = {
                    "undefined_citations": len(re.findall(r"Citation.*undefined", log)),
                    "undefined_refs": len(re.findall(r"Reference.*undefined", log)),
                    "overfull": log.count("Overfull"),
                }
            else:
                log = (tmp / "main.log").read_text(errors="replace") if (tmp / "main.log").exists() else ""
                for line in log.split("\n"):
                    if line.startswith("!"):
                        result["errors"].append(line[:150])
                        if len(result["errors"]) >= 3:
                            break
                if not result["errors"]:
                    result["errors"].append("No PDF produced (unknown error)")

        except subprocess.TimeoutExpired:
            result["errors"].append("Timeout")
        except FileNotFoundError:
            result["errors"].append(f"pdflatex not found")

    return result


# Main
all_results = {}
for condition in ["generated_paper", "baseline_paper"]:
    label = "SKILL" if condition == "generated_paper" else "BASELINE"
    compiled = 0
    total = 0

    print(f"\n=== {label} ===")

    for d in sorted(results_dir.iterdir()):
        tex = d / condition / "main.tex"
        bib = d / condition / "references.bib"
        if not tex.exists():
            continue

        total += 1
        content = tex.read_text(errors="replace")
        fixed = fix_tex(content)
        result = compile_paper(fixed, bib)

        key = f"{d.name}/{condition}"
        all_results[key] = result

        if result["success"]:
            compiled += 1
            undef = result.get("warnings", {}).get("undefined_citations", 0)
            info = f"OK ({result['pages']}p, {result['pdf_size']//1024}KB)"
            if undef:
                info += f", {undef} undef cites"
        else:
            err = result["errors"][0][:50] if result["errors"] else "unknown"
            info = f"FAIL: {err}"

        icon = "+" if result["success"] else "!"
        print(f"  [{icon}] {d.name[:45]:45s} {info}")

    rate = compiled / total * 100 if total else 0
    print(f"\n  {label}: {compiled}/{total} ({rate:.0f}%)")

# Summary
print(f"\n{'='*60}")
print("FINAL COMPILATION RATES")
print(f"{'='*60}")
for cond, label in [("generated_paper", "Skill"), ("baseline_paper", "Baseline")]:
    papers = {k: v for k, v in all_results.items() if cond in k}
    ok = sum(1 for v in papers.values() if v["success"])
    n = len(papers)
    avg_pages = sum(v["pages"] for v in papers.values() if v["success"]) / max(ok, 1)
    avg_undef = sum(v.get("warnings", {}).get("undefined_citations", 0)
                    for v in papers.values() if v["success"]) / max(ok, 1)
    print(f"  {label:12s}: {ok}/{n} ({ok/n*100:.0f}%), avg {avg_pages:.1f} pages, avg {avg_undef:.1f} undef cites")

with open(results_dir / "compilation_results.json", "w") as f:
    json.dump(all_results, f, indent=2)
print(f"\nSaved to {results_dir / 'compilation_results.json'}")
