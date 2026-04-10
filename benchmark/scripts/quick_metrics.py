#!/usr/bin/env python3
"""Quick structural metrics for all generated papers."""
import re
from pathlib import Path

results_dir = Path(__file__).parent.parent / "results"

for condition in ["generated_paper", "baseline_paper", "rich_paper"]:
    count = 0
    total_secs = total_tabs = total_figs = total_cites = total_bib = total_kb = 0
    papers = []

    for d in sorted(results_dir.iterdir()):
        tex = d / condition / "main.tex"
        bib = d / condition / "references.bib"
        if not tex.exists():
            continue

        content = tex.read_text(errors="replace")
        bib_content = bib.read_text(errors="replace") if bib.exists() else ""

        sections = content.count(r"\section{")
        tables = content.count(r"\begin{table")
        figures = content.count(r"\begin{figure")

        cite_keys = set()
        for match in re.findall(r"\\cite[tp]?\*?\{([^}]+)\}", content):
            for key in match.split(","):
                cite_keys.add(key.strip())
        cites = len(cite_keys)
        bib_entries = len(re.findall(r"@\w+\{", bib_content))
        kb = len(content) / 1024

        count += 1
        total_secs += sections
        total_tabs += tables
        total_figs += figures
        total_cites += cites
        total_bib += bib_entries
        total_kb += kb
        papers.append({
            "name": d.name[:45],
            "sections": sections,
            "tables": tables,
            "figures": figures,
            "cites": cites,
            "bib": bib_entries,
            "kb": round(kb, 1),
        })

    label = {"generated_paper": "SKILL (ABSTRACT INPUT)", "baseline_paper": "SINGLE-AGENT BASELINE", "rich_paper": "SKILL (FULL-TEXT INPUT)"}[condition]
    if count == 0:
        print(f"\n=== {label}: no papers yet ===")
        continue

    print(f"\n=== {label} ({count} papers) ===")
    print(f"{'Paper':<47s} {'Secs':>5s} {'Tabs':>5s} {'Figs':>5s} {'Cites':>6s} {'Bib':>5s} {'KB':>6s}")
    print("-" * 82)
    for p in papers:
        print(f"{p['name']:<47s} {p['sections']:5d} {p['tables']:5d} {p['figures']:5d} {p['cites']:6d} {p['bib']:5d} {p['kb']:6.1f}")
    print("-" * 82)
    print(f"{'AVERAGE':<47s} {total_secs/count:5.1f} {total_tabs/count:5.1f} {total_figs/count:5.1f} {total_cites/count:6.1f} {total_bib/count:5.1f} {total_kb/count:6.1f}")
    print(f"{'TOTAL':<47s} {total_secs:5d} {total_tabs:5d} {total_figs:5d} {total_cites:6d} {total_bib:5d} {total_kb:6.1f}")
