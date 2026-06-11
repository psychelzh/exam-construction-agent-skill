#!/usr/bin/env python3
"""Lightweight MCQ structural validator.

Input: a UTF-8 plain text or Markdown file containing MCQs with options A-D.
Output: heuristic warnings about item-writing risks.

This script does not judge substantive correctness. It only flags structural cues that
an instructor or agent should review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from statistics import mean

NEGATIVE_PATTERNS = ["不是", "不属于", "不正确", "错误的是", "except", "not "]
ALL_NONE_PATTERNS = ["以上都", "全部正确", "均正确", "均不正确", "all of the above", "none of the above"]
ABSOLUTE_PATTERNS = ["总是", "从不", "必然", "完全", "唯一", "绝对", "always", "never", "only", "must"]

OPTION_RE = re.compile(r"^\s*([A-DＡ-Ｄ])[\.．、)]\s*(.+?)\s*$", re.MULTILINE)
QUESTION_SPLIT_RE = re.compile(r"\n(?=\s*(?:\d+|[一二三四五六七八九十]+)[\.．、])")


def normalize_letter(letter: str) -> str:
    return {"Ａ": "A", "Ｂ": "B", "Ｃ": "C", "Ｄ": "D"}.get(letter, letter)


def validate_block(block: str, idx: int) -> list[str]:
    warnings: list[str] = []
    options = [(normalize_letter(m.group(1)), m.group(2).strip()) for m in OPTION_RE.finditer(block)]

    if len(options) not in (3, 4):
        warnings.append(f"Q{idx}: option count is {len(options)}; expected 3 or 4 plausible options.")

    lower_block = block.lower()
    for pat in NEGATIVE_PATTERNS:
        if pat in lower_block:
            warnings.append(f"Q{idx}: possible negative wording detected: {pat!r}.")
            break

    for pat in ALL_NONE_PATTERNS:
        if pat in lower_block:
            warnings.append(f"Q{idx}: all/none-of-the-above style option detected: {pat!r}.")
            break

    if options:
        lengths = [len(text) for _, text in options]
        avg_len = mean(lengths)
        if avg_len > 0 and max(lengths) / avg_len > 1.65:
            warnings.append(f"Q{idx}: one option is much longer than the others; check length cue.")
        if len(set(text for _, text in options)) < len(options):
            warnings.append(f"Q{idx}: duplicate or near-duplicate options may be present.")
        for letter, text in options:
            low = text.lower()
            if any(pat in low for pat in ABSOLUTE_PATTERNS):
                warnings.append(f"Q{idx}{letter}: absolute wording detected; verify it is not a cue.")

    return warnings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_mcq.py <questions.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    blocks = [b.strip() for b in QUESTION_SPLIT_RE.split(text) if b.strip()]
    all_warnings: list[str] = []
    for i, block in enumerate(blocks, 1):
        if OPTION_RE.search(block):
            all_warnings.extend(validate_block(block, i))

    if not all_warnings:
        print("No structural warnings found. Substantive expert review is still required.")
    else:
        print("Structural warnings:")
        for w in all_warnings:
            print(f"- {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
