#!/usr/bin/env python3
"""Validate the repository layout for the exam-construction Agent Skill."""

from __future__ import annotations

import json
import py_compile
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "skills/exam-construction/SKILL.md",
    "skills/exam-construction/references/quality_checklists.md",
    "skills/exam-construction/references/measurement_assessment_additions.md",
    "skills/exam-construction/scripts/validate_mcq.py",
    "skills/exam-construction/scripts/analyze_items.py",
    "skills/exam-construction/agents/openai.yaml",
    "claude-plugin/.claude-plugin/plugin.json",
    "claude-plugin/skills/exam-construction/SKILL.md",
    "README.md",
    "install.sh",
    "install.ps1",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_required_files() -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        fail("SKILL.md must start with YAML frontmatter delimited by ---")
    lines = match.group(1).splitlines()
    fields: dict[str, str] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"')
            if value in {">", "|"}:
                collected = []
                i += 1
                while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                    collected.append(lines[i].strip())
                    i += 1
                fields[key] = " ".join(part for part in collected if part)
                continue
            fields[key] = value
        i += 1
    return fields


def check_skill_frontmatter() -> None:
    text = (ROOT / "skills/exam-construction/SKILL.md").read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    for key in ["name", "description"]:
        if key not in fields:
            fail(f"SKILL.md frontmatter missing required key: {key}")
    if fields["name"] != "exam-construction":
        fail("SKILL.md name must be exam-construction")
    if len(fields["description"]) < 40:
        fail("SKILL.md description is too short for reliable discovery")


def check_plugin_manifest() -> None:
    manifest_path = ROOT / "claude-plugin/.claude-plugin/plugin.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    for key in ["name", "description", "version"]:
        if not data.get(key):
            fail(f"plugin.json missing required key: {key}")


def check_plugin_synced() -> None:
    src = ROOT / "skills/exam-construction/SKILL.md"
    dest = ROOT / "claude-plugin/skills/exam-construction/SKILL.md"
    if src.read_text(encoding="utf-8") != dest.read_text(encoding="utf-8"):
        fail("Claude plugin skill copy is out of sync. Run: python scripts/sync_plugin.py")


def check_python_scripts() -> None:
    for script in (ROOT / "skills/exam-construction/scripts").glob("*.py"):
        py_compile.compile(str(script), doraise=True)
    for script in (ROOT / "scripts").glob("*.py"):
        if script.name != Path(__file__).name:
            py_compile.compile(str(script), doraise=True)


def main() -> None:
    check_required_files()
    check_skill_frontmatter()
    check_plugin_manifest()
    check_plugin_synced()
    check_python_scripts()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
