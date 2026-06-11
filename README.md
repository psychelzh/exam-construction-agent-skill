# Exam Construction Agent Skill

A reusable Agent Skill for higher-education and classroom exam construction. It helps an AI agent design, generate, review, revise, assemble, and analyze exams as measurement instruments rather than loose collections of questions.

The skill is designed for tasks such as:

- creating a test blueprint / 双向细目表;
- generating MCQs, short-answer items, essays, and case-analysis tasks;
- reviewing distractors, answer uniqueness, difficulty, coverage, and fairness;
- writing answer keys and analytic scoring rubrics;
- building A/B parallel papers;
- conducting simple post-exam objective-item analysis from CSV files.

## Repository layout

```text
exam-construction-agent-skill/
├── skills/
│   └── exam-construction/          # Canonical Agent Skill folder
│       ├── SKILL.md                # Main skill instructions
│       ├── agents/openai.yaml      # Optional Codex metadata
│       ├── references/             # Longer measurement and exam-design references
│       └── scripts/                # Local helper scripts
├── claude-plugin/                  # Claude Code plugin wrapper
│   ├── .claude-plugin/plugin.json
│   └── skills/exam-construction/
├── examples/                       # Sample prompts and item-analysis CSVs
├── scripts/                        # Repo maintenance scripts
├── install.sh                      # macOS/Linux installer
├── install.ps1                     # Windows PowerShell installer
└── AGENTS.md                       # Repo-specific agent guidance
```

## Quick install

### Codex / open Agent Skills location

Install globally for Codex-compatible agents:

```bash
bash install.sh codex
```

This copies the skill to:

```text
$HOME/.agents/skills/exam-construction/
```

For a single project, run this from the target project root:

```bash
bash install.sh repo-codex
```

This copies the skill to:

```text
.agents/skills/exam-construction/
```

### Claude Code personal skill

Install as a personal Claude Code skill:

```bash
bash install.sh claude
```

This copies the skill to:

```text
$HOME/.claude/skills/exam-construction/
```

Then invoke it directly in Claude Code:

```text
/exam-construction
```

### Claude Code plugin wrapper

Install as a local Claude Code plugin-style skill bundle:

```bash
bash install.sh claude-plugin
```

This copies the plugin wrapper to:

```text
$HOME/.claude/skills/exam-construction-plugin/
```

After installation, restart Claude Code or run `/reload-plugins` if the session is already open.

### Windows PowerShell

```powershell
./install.ps1 codex
./install.ps1 claude
./install.ps1 claude-plugin
```

## Manual installation

Copy `skills/exam-construction/` into one of these locations:

```text
# Codex-compatible user scope
$HOME/.agents/skills/exam-construction/

# Codex-compatible repo scope
<repo>/.agents/skills/exam-construction/

# Claude Code personal scope
$HOME/.claude/skills/exam-construction/

# Claude Code project scope
<repo>/.claude/skills/exam-construction/
```

## Use examples

```text
Use the exam-construction skill. 根据这份课程大纲，为《发展心理学》期末闭卷考试设计双向细目表，100分，90分钟。
```

```text
/exam-construction 请审查以下10道选择题，重点检查干扰项质量、答案唯一性和认知层级。
```

```text
$exam-construction Build an item bank from the attached lecture notes. Include item metadata, answer key, and difficulty estimates.
```

## Item-analysis helper

For objective items, prepare a response CSV and answer-key CSV.

`responses.csv`:

```csv
respondent_id,Q1,Q2,Q3
S001,A,B,C
S002,A,C,C
```

`answer_key.csv`:

```csv
item_id,key
Q1,A
Q2,B
Q3,C
```

Run:

```bash
python skills/exam-construction/scripts/analyze_items.py --responses examples/item-analysis/responses.csv --key examples/item-analysis/answer_key.csv --out item_analysis.csv
```

## Development

Synchronize the Claude plugin copy from the canonical skill folder:

```bash
python scripts/sync_plugin.py
```

Validate repository structure:

```bash
python scripts/validate_repo.py
```

Create a distributable zip:

```bash
make package
```

## Important limits

This skill is for classroom and higher-education course assessment. It should not be used as the sole basis for high-stakes licensing, admissions, employment selection, clinical diagnosis, or official psychometric instrument development. Formal or summative exams require human instructor review before administration.
