# Agent working instructions for this repository

This repository packages a reusable Agent Skill for classroom exam construction.

When editing this repository:

1. Keep the canonical skill in `skills/exam-construction/`.
2. Keep `claude-plugin/skills/exam-construction/` synchronized by running:

   ```bash
   python scripts/sync_plugin.py
   ```

3. Validate the package before committing:

   ```bash
   python scripts/validate_repo.py
   ```

4. Keep `SKILL.md` concise and place longer guidance in `references/`.
5. Avoid adding scripts that access networks, credentials, personal files, or external services.
