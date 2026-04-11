#!/usr/bin/env python3
"""
Validate all BiomedWritingBench test cases against the schema.

Usage:
    python validate_schema.py
    python validate_schema.py --test-cases-dir benchmark/test-cases/
    python validate_schema.py --report
"""

import sys
import json
import re
import argparse
from pathlib import Path

from jsonschema import validate, ValidationError

sys.path.insert(0, str(Path(__file__).parent))
from config import BENCHMARK_DIR, TEST_CASES_DIR, SCHEMA_PATH, SUBFIELD_CATEGORIES


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_metadata(metadata_path: Path, schema: dict) -> list[str]:
    """Validate metadata.json against JSON Schema. Return list of errors."""
    errors = []
    try:
        data = json.loads(metadata_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        errors.append(f"Schema violation: {e.message} (at {'.'.join(str(p) for p in e.path)})")

    # Additional checks beyond schema
    if data.get("category") and data["category"] not in SUBFIELD_CATEGORIES:
        errors.append(f"Unknown category: {data['category']}")

    if data.get("published_year") and not (2020 <= data["published_year"] <= 2027):
        errors.append(f"Suspicious year: {data['published_year']}")

    return errors


def validate_idea_summary(path: Path) -> list[str]:
    """Check idea_summary.md has required sections."""
    errors = []
    if not path.exists():
        return ["Missing idea_summary.md"]

    text = path.read_text(encoding="utf-8", errors="replace")
    required_patterns = [
        (r"##\s*(Working\s+title|Title)", "Working title section"),
        (r"##\s*(Core\s+question|Research\s+question)", "Core question section"),
        (r"##\s*(Motivation|Gap)", "Motivation/gap section"),
        (r"##\s*(Core\s+contribution|Contribution|Key\s+innovation)", "Contributions section"),
        (r"##\s*(Method|Approach)", "Method section"),
        (r"##\s*(Target\s+venue|Venue)", "Target venue section"),
    ]

    for pattern, name in required_patterns:
        if not re.search(pattern, text, re.IGNORECASE):
            errors.append(f"Missing section: {name}")

    if len(text.strip()) < 200:
        errors.append(f"Idea summary too short ({len(text.strip())} chars, expected 200+)")

    return errors


def validate_experimental_log(path: Path) -> list[str]:
    """Check experimental_log.md has data tables and quantitative content."""
    errors = []
    if not path.exists():
        return ["Missing experimental_log.md"]

    text = path.read_text(encoding="utf-8", errors="replace")

    # Check for markdown tables (pipe-delimited) or rich quantitative content
    table_lines = [line for line in text.split("\n") if "|" in line and line.strip().startswith("|")]
    has_jats_marker = "Extracted from full-text JATS XML" in text
    if len(table_lines) < 3 and not has_jats_marker:
        errors.append("No data tables found (expected markdown tables with | delimiters)")

    # Check for numbers (quantitative content)
    numbers = re.findall(r'\d+\.?\d*', text)
    if len(numbers) < 10:
        errors.append(f"Low quantitative density ({len(numbers)} numbers, expected 10+)")

    if len(text.strip()) < 300:
        errors.append(f"Experimental log too short ({len(text.strip())} chars, expected 300+)")

    return errors


def validate_test_case(case_dir: Path, schema: dict) -> dict:
    """Validate a single test case directory. Return validation result."""
    result = {
        "id": case_dir.name,
        "path": str(case_dir),
        "valid": True,
        "errors": [],
        "warnings": [],
    }

    # Check required files exist
    metadata_path = case_dir / "metadata.json"
    idea_path = case_dir / "idea_summary.md"
    exp_path = case_dir / "experimental_log.md"

    if not metadata_path.exists():
        result["errors"].append("Missing metadata.json")
        result["valid"] = False
        return result

    # Validate metadata
    meta_errors = validate_metadata(metadata_path, schema)
    result["errors"].extend(meta_errors)

    # Validate idea summary
    idea_errors = validate_idea_summary(idea_path)
    result["errors"].extend(idea_errors)

    # Validate experimental log
    exp_errors = validate_experimental_log(exp_path)
    result["errors"].extend(exp_errors)

    # Check ground truth fields
    meta = json.loads(metadata_path.read_text(encoding="utf-8"))
    null_gt_fields = []
    for field in ["ground_truth_citation_count", "ground_truth_figure_count", "ground_truth_table_count"]:
        if meta.get(field) is None:
            null_gt_fields.append(field)
    if null_gt_fields:
        result["warnings"].append(f"Null ground truth fields: {', '.join(null_gt_fields)}")

    if result["errors"]:
        result["valid"] = False

    return result


def main():
    parser = argparse.ArgumentParser(description="Validate BiomedWritingBench test cases")
    parser.add_argument("--test-cases-dir", type=Path, default=TEST_CASES_DIR)
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH)
    parser.add_argument("--report", action="store_true", help="Print detailed report")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    case_dirs = sorted(d for d in args.test_cases_dir.iterdir() if d.is_dir())

    if not case_dirs:
        print(f"No test cases found in {args.test_cases_dir}")
        sys.exit(1)

    results = []
    for case_dir in case_dirs:
        result = validate_test_case(case_dir, schema)
        results.append(result)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    # Summary
    total = len(results)
    valid = sum(1 for r in results if r["valid"])
    with_warnings = sum(1 for r in results if r["warnings"])

    print(f"=== BiomedWritingBench Validation ===")
    print(f"Test cases: {total}")
    print(f"Valid: {valid}/{total}")
    print(f"With warnings: {with_warnings}/{total}")
    print()

    for r in results:
        status = "PASS" if r["valid"] else "FAIL"
        icon = "+" if r["valid"] else "!"
        print(f"  [{icon}] {r['id']}: {status}")
        if args.report:
            for err in r["errors"]:
                print(f"      ERROR: {err}")
            for warn in r["warnings"]:
                print(f"      WARN:  {warn}")

    # Subfield distribution
    if args.report:
        print(f"\n=== Subfield Distribution ===")
        subfield_counts = {}
        for case_dir in case_dirs:
            meta_path = case_dir / "metadata.json"
            if meta_path.exists():
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                cat = meta.get("category", "unknown")
                subfield_counts[cat] = subfield_counts.get(cat, 0) + 1
        for sf in sorted(subfield_counts.keys()):
            print(f"  {sf}: {subfield_counts[sf]}")

    sys.exit(0 if valid == total else 1)


if __name__ == "__main__":
    main()
