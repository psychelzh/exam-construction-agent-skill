# Security Policy

This repository is intentionally local-first and does not require network access.

Before installing any Agent Skill, review `SKILL.md`, `scripts/`, and plugin metadata. Skills are operational instructions for AI agents and may influence tool use. Do not install third-party skills blindly.

## Safety design choices

- No script in this repository sends data to external services.
- No script reads credentials or environment secrets.
- Installation scripts copy files only into local skill directories.
- The post-exam item-analysis script processes local CSV files only.

## Reporting issues

If you adapt this repository for public use, create GitHub Issues and Security Advisories for vulnerability reports.
