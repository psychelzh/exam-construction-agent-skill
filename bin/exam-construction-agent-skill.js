#!/usr/bin/env node

import { cp, mkdir } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const packageRoot = dirname(__dirname);
const skillSource = join(packageRoot, 'skills', 'exam-construction');
const pluginSource = join(packageRoot, 'claude-plugin');

const homeDirectory = process.env.HOME || process.env.USERPROFILE || '';
const targets = {
  codex: join(homeDirectory, '.agents', 'skills', 'exam-construction'),
  claude: join(homeDirectory, '.claude', 'skills', 'exam-construction'),
  'repo-codex': join(process.cwd(), '.agents', 'skills', 'exam-construction'),
  'repo-claude': join(process.cwd(), '.claude', 'skills', 'exam-construction'),
  'claude-plugin': join(homeDirectory, '.claude', 'skills', 'exam-construction-plugin')
};

function usage() {
  console.log(`Usage: exam-construction-agent-skill <target>\n\nTargets:\n  codex          Install globally for Codex-compatible agents\n  claude         Install as a personal Claude Code skill\n  both           Install both codex and claude targets\n  repo-codex     Install into the current repo at .agents/skills/exam-construction\n  repo-claude    Install into the current repo at .claude/skills/exam-construction\n  claude-plugin  Install Claude Code plugin wrapper\n`);
}

async function copyDir(source, destination) {
  await mkdir(dirname(destination), { recursive: true });
  await cp(source, destination, { recursive: true, force: true });
  console.log(`Installed: ${destination}`);
}

async function main() {
  const target = process.argv[2];
  if (!target || target === '-h' || target === '--help' || target === 'help') {
    usage();
    return;
  }

  if (target === 'both') {
    await copyDir(skillSource, targets.codex);
    await copyDir(skillSource, targets.claude);
    return;
  }

  if (target === 'claude-plugin') {
    await copyDir(pluginSource, targets['claude-plugin']);
    return;
  }

  const destination = targets[target];
  if (!destination) {
    console.error(`Unknown target: ${target}`);
    usage();
    process.exitCode = 1;
    return;
  }

  await copyDir(skillSource, destination);
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exitCode = 1;
});
