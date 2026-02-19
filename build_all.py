#!/usr/bin/env python3
"""
build_all.py — Single command to build and validate all outputs.

Usage:  python3 build_all.py

Steps:
  1. Build Excel workbook  (build_workbook.py)
  2. Build PowerPoint deck (build_presentation.py)
  3. Validate consistency  (validate.py)

If validation fails, the script exits with a non-zero code and prints
every specific error. Fix the flagged value in the appropriate source
file, then re-run.
"""

import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

steps = [
    ("Excel Workbook",        ["python3", "build_workbook.py"]),
    ("PowerPoint Deck",       ["python3", "build_presentation.py"]),
    ("Consistency Validator", ["python3", "validate.py"]),
]

all_passed = True

for label, cmd in steps:
    print(f"\n{'─'*60}")
    print(f"  ▶  {label}")
    print(f"{'─'*60}")
    result = subprocess.run(cmd, cwd=BASE_DIR)
    if result.returncode != 0:
        print(f"\n  ✗  {label} FAILED (exit code {result.returncode})")
        all_passed = False
        break  # stop pipeline on first failure

if all_passed:
    print(f"\n{'═'*60}")
    print("  ✓  BUILD COMPLETE — all files consistent and verified.")
    print(f"{'═'*60}\n")
    sys.exit(0)
else:
    print(f"\n{'═'*60}")
    print("  ✗  BUILD FAILED — see errors above. Do not deliver until resolved.")
    print(f"{'═'*60}\n")
    sys.exit(1)
