#!/usr/bin/env bash
# compile_latex.sh — Full LaTeX build cycle with error reporting
#
# Usage:
#   bash compile_latex.sh /path/to/latex/dir [main_filename_without_ext]
#
# Runs pdflatex -> bibtex -> pdflatex -> pdflatex, reports errors, and
# checks for common issues.
#
# On Windows with TinyTeX, set TEXDIR or it auto-detects from APPDATA.

set -euo pipefail

LATEX_DIR="${1:-.}"
MAIN="${2:-main}"

cd "$LATEX_DIR"

# Auto-detect TinyTeX on Windows
if [ -n "${APPDATA:-}" ] && [ -d "$APPDATA/TinyTeX/bin/windows" ]; then
    export PATH="$APPDATA/TinyTeX/bin/windows:$PATH"
fi

# Verify tools exist
if ! command -v pdflatex &> /dev/null; then
    echo "ERROR: pdflatex not found. Install TinyTeX or TeX Live."
    echo "  TinyTeX: https://yihui.org/tinytex/"
    exit 1
fi

echo "=== Paper Builder: LaTeX Compilation ==="
echo "Directory: $(pwd)"
echo "Main file: ${MAIN}.tex"
echo "pdflatex: $(which pdflatex)"
echo ""

# Pass 1: Initial compile
echo "--- Pass 1: pdflatex ---"
if ! pdflatex -interaction=nonstopmode -halt-on-error "${MAIN}.tex" > /tmp/latex_pass1.log 2>&1; then
    echo "ERROR in pass 1. Key errors:"
    grep -A2 "^!" /tmp/latex_pass1.log || grep -i "error" /tmp/latex_pass1.log | head -20
    echo ""
    echo "Full log: /tmp/latex_pass1.log"
    exit 1
fi
echo "  Pass 1 OK"

# BibTeX pass
if [ -f "${MAIN}.aux" ]; then
    echo "--- BibTeX pass ---"
    if ! bibtex "${MAIN}" > /tmp/bibtex.log 2>&1; then
        echo "WARNING: BibTeX had issues:"
        grep -i "warning\|error" /tmp/bibtex.log | head -10
    else
        echo "  BibTeX OK"
    fi
fi

# Pass 2
echo "--- Pass 2: pdflatex ---"
pdflatex -interaction=nonstopmode "${MAIN}.tex" > /tmp/latex_pass2.log 2>&1
echo "  Pass 2 OK"

# Pass 3
echo "--- Pass 3: pdflatex ---"
pdflatex -interaction=nonstopmode "${MAIN}.tex" > /tmp/latex_pass3.log 2>&1
echo "  Pass 3 OK"

# Check results
echo ""
echo "=== Compilation Summary ==="
if [ -f "${MAIN}.pdf" ]; then
    PDF_SIZE=$(du -h "${MAIN}.pdf" | cut -f1)
    echo "PDF generated: ${MAIN}.pdf (${PDF_SIZE})"
else
    echo "ERROR: PDF not generated!"
    exit 1
fi

# Report remaining warnings
UNDEF_CITE=$(grep -c "Citation.*undefined" "${MAIN}.log" 2>/dev/null || echo "0")
UNDEF_REF=$(grep -c "Reference.*undefined" "${MAIN}.log" 2>/dev/null || echo "0")
OVERFULL=$(grep -c "Overfull" "${MAIN}.log" 2>/dev/null || echo "0")

if [ "$UNDEF_CITE" -gt 0 ] 2>/dev/null; then
    echo "WARNING: ${UNDEF_CITE} undefined citation(s)"
    grep "Citation.*undefined" "${MAIN}.log" | head -5
fi
if [ "$UNDEF_REF" -gt 0 ] 2>/dev/null; then
    echo "WARNING: ${UNDEF_REF} undefined reference(s)"
fi
if [ "$OVERFULL" -gt 0 ] 2>/dev/null; then
    echo "NOTE: ${OVERFULL} overfull box warning(s)"
fi

echo ""
echo "=== Done ==="
