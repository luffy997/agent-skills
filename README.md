<div align="center">

# Agent Skills

**Reusable skills that make AI agents measurably better at specific work.**

<p>
  <strong>English</strong> &nbsp;·&nbsp; <a href="README.zh-CN.md">简体中文</a>
</p>

<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-111111?style=flat-square"></a>
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent_Skills-compatible-111111?style=flat-square">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude_Code-supported-111111?style=flat-square">
  <img alt="Codex" src="https://img.shields.io/badge/Codex-supported-111111?style=flat-square">
</p>

</div>

---

## Why this repository

Agent Skills are folders of instructions, references, and assets that an AI agent loads on demand. Instead of repeating the same context in every conversation, a skill packages a repeatable way of working: the workflow, the judgment calls, and the quality bar.

Every skill here is self-contained, versioned in git, and usable across tools that support the [Agent Skills](https://agentskills.io) format — including Claude Code and Codex.

## Skills

| Skill | What it does | Contents |
| --- | --- | --- |
| [key-reporting](skills/key-reporting/) | Structures work reports for research and engineering teams: audience analysis, one-message outlines, review defense, and evidence gap detection. | `SKILL.md` · `references/` · `assets/` |

## Install

Clone the repository, then copy the skill you need into your agent's skills directory.

**Claude Code — personal**

```bash
mkdir -p ~/.claude/skills
cp -r skills/key-reporting ~/.claude/skills/
```

**Claude Code — project**

```bash
mkdir -p .claude/skills
cp -r skills/key-reporting .claude/skills/
```

**Codex — personal**

```bash
mkdir -p ~/.agents/skills
cp -r skills/key-reporting ~/.agents/skills/
```

**Codex — project**

```bash
mkdir -p .agents/skills
cp -r skills/key-reporting .agents/skills/
```

## Use

Once installed, invoke the skill explicitly or describe the task in natural language:

```text
/key-reporting Turn these notes into a 10-minute update for the engineering director.
```

```text
Use key-reporting to prepare the 8 hardest questions for tomorrow's design review.
```

In Codex, reference it as `$key-reporting` or simply describe the task.

## Repository layout

```text
agent-skills/
├── skills/
│   └── key-reporting/        # One folder per skill
│       ├── SKILL.md          # Required: frontmatter + instructions
│       ├── README.md         # Human-facing documentation
│       ├── references/       # Supporting material loaded as needed
│       └── assets/           # Examples and reusable outputs
├── template/
│   └── SKILL.md              # Starting point for a new skill
├── README.md                 # English
├── README.zh-CN.md           # 简体中文
└── LICENSE
```

A skill needs only a folder and a `SKILL.md`. The frontmatter has two required fields:

```yaml
---
name: my-skill
description: What the skill does and when the agent should use it.
---
```

Everything below the frontmatter is the instruction the agent follows. Keep `SKILL.md` focused; move long supporting material into `references/` and examples into `assets/`.

## Create a skill

1. Copy `template/` to `skills/<your-skill>/`.
2. Rename the `name` field and write a precise trigger-oriented `description`.
3. Add the workflow, decision rules, and output contract to `SKILL.md`.
4. Move bulky references and examples into `references/` and `assets/`.
5. Add the skill to the table above and test it in a real session.

## License

Released under the [MIT License](LICENSE).
