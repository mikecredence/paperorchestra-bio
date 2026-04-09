#!/usr/bin/env python3
"""
Initialize and validate the paper-build workspace.

Usage:
    python init_workspace.py [--base-dir /path/to/paper-build]
    python init_workspace.py --validate --base-dir /path/to/paper-build

Creates the workspace directory structure and validates that required
inputs are present before the pipeline begins.
"""

import sys
import os
import json
import argparse
from pathlib import Path


REQUIRED_DIRS = [
    "outline",
    "literature",
    "figures",
    "latex",
    "output",
    "snapshots",  # For refinement rollback
]


def init_workspace(base_dir: str) -> dict:
    """Create the workspace directory structure."""
    base = Path(base_dir)
    created = []

    for dirname in REQUIRED_DIRS:
        dirpath = base / dirname
        dirpath.mkdir(parents=True, exist_ok=True)
        created.append(str(dirpath))

    # Initialize worklog
    worklog_path = base / "worklog.json"
    if not worklog_path.exists():
        worklog_path.write_text(json.dumps({
            "pipeline_start": None,
            "stages": [],
            "refinement_rounds": [],
        }, indent=2))

    return {
        "status": "initialized",
        "base_dir": str(base),
        "directories_created": created,
        "worklog": str(worklog_path),
    }


def validate_inputs(base_dir: str) -> dict:
    """Validate that required inputs exist."""
    base = Path(base_dir)
    issues = []
    warnings = []

    # Check workspace structure
    for dirname in REQUIRED_DIRS:
        if not (base / dirname).is_dir():
            issues.append(f"Missing directory: {dirname}/")

    # Check for idea summary (could be in various forms)
    idea_patterns = ["idea_summary.*", "idea.*", "summary.*"]
    has_idea = False
    for pattern in idea_patterns:
        if list(base.glob(pattern)):
            has_idea = True
            break
    if not has_idea:
        issues.append("No idea summary found. Expected: idea_summary.md or similar")

    # Check for experimental log
    exp_patterns = ["experimental_log.*", "experiment.*", "results.*", "data.*"]
    has_exp = False
    for pattern in exp_patterns:
        if list(base.glob(pattern)):
            has_exp = True
            break
    if not has_exp:
        issues.append("No experimental log found. Expected: experimental_log.md or similar")

    # Check for venue template (optional but recommended)
    template_patterns = ["*.cls", "*.sty", "template.*"]
    has_template = False
    for pattern in template_patterns:
        if list(base.glob(pattern)) or list((base / "latex").glob(pattern)):
            has_template = True
            break
    if not has_template:
        warnings.append("No LaTeX template found. Will use default NeurIPS-style format.")

    # Check for outline (needed after Stage 1)
    outline_path = base / "outline" / "outline.json"
    has_outline = outline_path.exists()

    return {
        "status": "valid" if not issues else "invalid",
        "base_dir": str(base),
        "has_idea_summary": has_idea,
        "has_experimental_log": has_exp,
        "has_template": has_template,
        "has_outline": has_outline,
        "issues": issues,
        "warnings": warnings,
    }


def main():
    parser = argparse.ArgumentParser(description="Initialize paper-build workspace")
    parser.add_argument("--base-dir", default="./paper-build",
                        help="Base directory for workspace (default: ./paper-build)")
    parser.add_argument("--validate", action="store_true",
                        help="Validate existing workspace instead of creating")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON")
    args = parser.parse_args()

    if args.validate:
        result = validate_inputs(args.base_dir)
    else:
        result = init_workspace(args.base_dir)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if args.validate:
            print(f"Workspace: {result['base_dir']}")
            print(f"Status: {result['status']}")
            print(f"  Idea summary: {'YES' if result['has_idea_summary'] else 'MISSING'}")
            print(f"  Experimental log: {'YES' if result['has_experimental_log'] else 'MISSING'}")
            print(f"  LaTeX template: {'YES' if result['has_template'] else 'not found (optional)'}")
            print(f"  Outline: {'YES' if result['has_outline'] else 'not yet generated'}")
            if result["issues"]:
                print(f"\nIssues:")
                for issue in result["issues"]:
                    print(f"  - {issue}")
            if result["warnings"]:
                print(f"\nWarnings:")
                for w in result["warnings"]:
                    print(f"  - {w}")
        else:
            print(f"Workspace initialized at: {result['base_dir']}")
            for d in result["directories_created"]:
                print(f"  Created: {d}")


if __name__ == "__main__":
    main()
