#!/usr/bin/env python3
"""Validate Phase 0-D JSON outputs against their schemas.

Usage:
    validate.py <output_base_dir>          # validate every JSON file under output_base_dir
    validate.py <path_to_json>             # validate one file (schema chosen by filename)
    validate.py --phase 0 <output_base_dir>  # validate just what Phase 0 produces

Exit code 0 if all valid, non-zero if any file fails. Prints one line per file:
    OK    <path>
    FAIL  <path>: <reason>
"""
import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write("This script needs the `jsonschema` package.\n  pip install jsonschema\n")
    sys.exit(2)

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schemas"

# Filename pattern -> schema file. Order matters for stage<N>_branch_trace.
FILENAME_TO_SCHEMA = [
    ("_hydration.json",                 "hydration.schema.json"),
    ("_orchestrator_runs_index.json",   "orchestrator_runs_index.schema.json"),
    ("_branch_triage.json",             "branch_triage.schema.json"),
    ("_capture_index.json",             "capture_index.schema.json"),
    ("run_capture.json",                "run_capture.schema.json"),
]

# Phase membership for --phase filter.
PHASE_FILES = {
    "0": ["_hydration.json"],
    "B": ["_orchestrator_runs_index.json", "_branch_triage.json"],
    "C": ["run_capture.json"],
    "D": ["_capture_index.json"],
}


def schema_for(path: Path) -> Path | None:
    name = path.name
    for suffix, schema in FILENAME_TO_SCHEMA:
        if name == suffix:
            return SCHEMA_DIR / schema
    # stage<N>_branch_trace.json
    if name.startswith("stage") and name.endswith("_branch_trace.json"):
        return SCHEMA_DIR / "stage_branch_trace.schema.json"
    return None


def validate(path: Path) -> tuple[bool, str]:
    schema_path = schema_for(path)
    if schema_path is None:
        return True, "no-schema (skipped)"
    if not schema_path.exists():
        return False, f"schema missing: {schema_path}"
    try:
        schema = json.loads(schema_path.read_text())
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        return False, f"invalid JSON: {e}"
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if not errors:
        return True, "ok"
    first = errors[0]
    loc = "/".join(str(p) for p in first.absolute_path) or "<root>"
    return False, f"{loc}: {first.message}"


def walk_outputs(base: Path) -> list[Path]:
    files = []
    # Phase 0/B/D files at base
    for suffix, _ in FILENAME_TO_SCHEMA:
        for p in base.glob(f"**/{suffix}"):
            files.append(p)
    # stage<N>_branch_trace.json anywhere under base
    for p in base.glob("**/stage*_branch_trace.json"):
        files.append(p)
    return sorted(set(files))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Output base dir, or a single JSON file")
    ap.add_argument("--phase", choices=["0", "B", "C", "D"], help="Only validate files for the named phase")
    args = ap.parse_args()
    target = Path(args.path).expanduser()
    if not target.exists():
        sys.stderr.write(f"Not found: {target}\n")
        return 2

    if target.is_file():
        files = [target]
    else:
        files = walk_outputs(target)
        if args.phase:
            wanted = set(PHASE_FILES[args.phase])
            if args.phase == "C":
                files = [f for f in files if f.name == "run_capture.json" or (f.name.startswith("stage") and f.name.endswith("_branch_trace.json"))]
            else:
                files = [f for f in files if f.name in wanted]

    if not files:
        print("no files to validate")
        return 0

    any_fail = False
    for f in files:
        ok, msg = validate(f)
        mark = "OK  " if ok else "FAIL"
        print(f"{mark}  {f}  -  {msg}")
        if not ok:
            any_fail = True
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
