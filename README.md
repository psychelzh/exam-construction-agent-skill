# Exam Construction Agent Skill

A reusable Agent Skill for classroom and higher-education exam construction. It helps an AI agent design, generate, review, revise, assemble, and analyze exams as measurement instruments.

## Install

Install directly from GitHub with npm:

```bash
npm install -g github:psychelzh/exam-construction-agent-skill
exam-construction-agent-skill codex
```

Or run it once without a global install:

```bash
npx github:psychelzh/exam-construction-agent-skill claude
```

Supported targets are: `codex`, `claude`, `both`, `repo-codex`, `repo-claude`, and `claude-plugin`.

## Use

```text
Use the exam-construction skill. 根据这份课程大纲，为《发展心理学》期末闭卷考试设计双向细目表，100分，90分钟。
```

```text
/exam-construction 请审查以下10道选择题，重点检查干扰项质量、答案唯一性和认知层级。
```

```text
$exam-construction Build an item bank from the attached lecture notes. Include item metadata, answer key, and difficulty estimates.
```

## Maintenance

Validate the repository:

```bash
python scripts/validate_repo.py
```

Synchronize the Claude plugin copy from the canonical skill folder:

```bash
python scripts/sync_plugin.py
```

## Limits

This skill is for classroom and higher-education assessment. It should not be used as the sole basis for high-stakes licensing, admissions, employment selection, clinical diagnosis, or official psychometric instrument development.
