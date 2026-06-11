#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="$ROOT_DIR/skills/exam-construction"
PLUGIN_SRC="$ROOT_DIR/claude-plugin"

usage() {
  cat <<USAGE
Usage: bash install.sh <target>

Targets:
  codex          Install globally for Codex-compatible agents to ~/.agents/skills/exam-construction
  claude         Install as a personal Claude Code skill to ~/.claude/skills/exam-construction
  both           Install both codex and claude targets
  repo-codex     Install into the current repo at .agents/skills/exam-construction
  repo-claude    Install into the current repo at .claude/skills/exam-construction
  claude-plugin  Install Claude Code plugin wrapper to ~/.claude/skills/exam-construction-plugin

USAGE
}

copy_dir() {
  local src="$1"
  local dest="$2"
  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  cp -R "$src" "$dest"
  echo "Installed: $dest"
}

install_codex() {
  copy_dir "$SKILL_SRC" "$HOME/.agents/skills/exam-construction"
}

install_claude() {
  copy_dir "$SKILL_SRC" "$HOME/.claude/skills/exam-construction"
}

install_repo_codex() {
  copy_dir "$SKILL_SRC" "$(pwd)/.agents/skills/exam-construction"
}

install_repo_claude() {
  copy_dir "$SKILL_SRC" "$(pwd)/.claude/skills/exam-construction"
}

install_claude_plugin() {
  copy_dir "$PLUGIN_SRC" "$HOME/.claude/skills/exam-construction-plugin"
}

case "${1:-}" in
  codex) install_codex ;;
  claude) install_claude ;;
  both) install_codex; install_claude ;;
  repo-codex) install_repo_codex ;;
  repo-claude) install_repo_claude ;;
  claude-plugin) install_claude_plugin ;;
  -h|--help|help|"") usage ;;
  *) echo "Unknown target: $1" >&2; usage; exit 1 ;;
esac
