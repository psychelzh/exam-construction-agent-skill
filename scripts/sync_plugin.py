#!/usr/bin/env python3
"""Synchronize Claude plugin skill copy from the canonical skill folder."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "skills" / "exam-construction"
DEST = ROOT / "claude-plugin" / "skills" / "exam-construction"

if not SRC.exists():
    raise SystemExit(f"Missing canonical skill folder: {SRC}")

if DEST.exists():
    shutil.rmtree(DEST)
shutil.copytree(SRC, DEST)
print(f"Synced {SRC.relative_to(ROOT)} -> {DEST.relative_to(ROOT)}")
