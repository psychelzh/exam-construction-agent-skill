#!/usr/bin/env python3
"""Simple objective-item analysis for classroom tests.

Expected response CSV:
    respondent_id,Q1,Q2,Q3,...
    S001,A,B,C,...

Expected answer-key CSV:
    item_id,key
    Q1,A
    Q2,B

Outputs item difficulty, corrected item-total correlation, high-low discrimination,
blank rate, and option frequencies. This is a small-class diagnostic tool, not a
full psychometric validation pipeline.
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
from pathlib import Path
from statistics import mean, pstdev


def read_key(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not {"item_id", "key"}.issubset(reader.fieldnames or []):
            raise ValueError("Key CSV must contain columns: item_id,key")
        return {row["item_id"].strip(): row["key"].strip() for row in reader if row.get("item_id")}


def read_responses(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)
    return fields, rows


def corr(x: list[float], y: list[float]) -> float | None:
    if len(x) < 3 or len(y) < 3:
        return None
    mx, my = mean(x), mean(y)
    sx, sy = pstdev(x), pstdev(y)
    if sx == 0 or sy == 0:
        return None
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (len(x) * sx * sy)


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze objective classroom-test items.")
    parser.add_argument("--responses", required=True, type=Path, help="Wide CSV of student responses")
    parser.add_argument("--key", required=True, type=Path, help="CSV with columns item_id,key")
    parser.add_argument("--out", type=Path, help="Output CSV path; defaults to stdout")
    parser.add_argument("--id-column", default="respondent_id", help="Respondent ID column to ignore")
    args = parser.parse_args()

    key = read_key(args.key)
    fields, rows = read_responses(args.responses)
    items = [f for f in fields if f != args.id_column and f in key]
    if not items:
        raise ValueError("No response columns match item IDs in the key file.")

    score_by_item: dict[str, list[int]] = {}
    for item in items:
        score_by_item[item] = [1 if (row.get(item, "").strip() == key[item]) else 0 for row in rows]

    total_scores = [sum(score_by_item[item][i] for item in items) for i in range(len(rows))]
    n = len(rows)
    sorted_idx = sorted(range(n), key=lambda i: total_scores[i])
    group_n = max(1, math.ceil(n * 0.27)) if n else 0
    low_idx = set(sorted_idx[:group_n])
    high_idx = set(sorted_idx[-group_n:])

    output_rows: list[dict[str, str]] = []
    for item in items:
        scores = score_by_item[item]
        p_value = mean(scores) if scores else float("nan")
        corrected_total = [total_scores[i] - scores[i] for i in range(n)]
        rit = corr([float(s) for s in scores], [float(t) for t in corrected_total])
        high_p = mean([scores[i] for i in high_idx]) if high_idx else float("nan")
        low_p = mean([scores[i] for i in low_idx]) if low_idx else float("nan")
        responses = [row.get(item, "").strip() for row in rows]
        blanks = sum(1 for r in responses if not r)
        freqs = Counter(r if r else "<blank>" for r in responses)
        output_rows.append({
            "item_id": item,
            "n": str(n),
            "key": key[item],
            "p_value": f"{p_value:.3f}",
            "corrected_item_total_r": "" if rit is None else f"{rit:.3f}",
            "high_low_discrimination": f"{(high_p - low_p):.3f}",
            "blank_rate": f"{(blanks / n if n else float('nan')):.3f}",
            "option_frequencies": "; ".join(f"{k}:{v}" for k, v in sorted(freqs.items())),
        })

    fieldnames = ["item_id", "n", "key", "p_value", "corrected_item_total_r", "high_low_discrimination", "blank_rate", "option_frequencies"]
    if args.out:
        with args.out.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_rows)
    else:
        writer = csv.DictWriter(__import__("sys").stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
