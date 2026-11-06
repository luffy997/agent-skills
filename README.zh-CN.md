<div align="center">

# Agent 技能库

**可复用的 Agent Skills，让 AI 在特定任务上表现得更专业、更稳定。**

<p>
  <a href="README.md">English</a> &nbsp;·&nbsp; <strong>简体中文</strong>
</p>

<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-111111?style=flat-square"></a>
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent_Skills-compatible-111111?style=flat-square">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude_Code-supported-111111?style=flat-square">
  <img alt="Codex" src="https://img.shields.io/badge/Codex-supported-111111?style=flat-square">
</p>

</div>

---

## 为什么需要这个仓库

Agent Skill 是由指令、参考资料和资产组成的文件夹，AI 在需要时按需加载。它把一套可重复的工作方式沉淀下来——流程、判断标准和交付质量，而不是在每次对话里重复相同的背景说明。

这里的每个技能都独立成目录、纳入版本管理，并可在支持 [Agent Skills](https://agentskills.io) 规范的工具中复用，包括 Claude Code 与 Codex。

## 技能列表

| 技能 | 作用 | 内容 |
| --- | --- | --- |
| [key-reporting](skills/key-reporting/) | 面向研发与工程团队的工作汇报技能：听众分析、一句话主张、结构化提纲、答辩预演与证据缺口识别。 | `SKILL.md` · `references/` · `assets/` |
| [requirement-analysis](skills/requirement-analysis/) | 把模糊需求转化为可验收的研发规格：确认门禁、候选方案、决策台账与验收标准。 | `SKILL.md` · `references/` · `assets/` |
| [sensitive-info-guard](skills/sensitive-info-guard/) | 提交前扫描密码、密钥、IP、内网域名、公司/客户及人员信息等敏感内容，发现风险即阻止提交。 | `SKILL.md` · `references/` · `scripts/` · `examples/` |

## 安装

克隆仓库后，把需要的技能复制到对应 Agent 的技能目录。

**Claude Code — 个人**

```bash
mkdir -p ~/.claude/skills
cp -r skills/key-reporting ~/.claude/skills/
```

**Claude Code — 项目**

```bash
mkdir -p .claude/skills
cp -r skills/key-reporting .claude/skills/
```

**Codex — 个人**

```bash
mkdir -p ~/.agents/skills
cp -r skills/key-reporting ~/.agents/skills/
```

**Codex — 项目**

```bash
mkdir -p .agents/skills
cp -r skills/key-reporting .agents/skills/
```

## 使用

安装后可以显式调用技能，也可以直接用自然语言描述任务：

```text
/key-reporting 把这些笔记改成面向研发负责人的 10 分钟汇报。
```

```text
使用 key-reporting，为明天的技术评审准备 8 个最难的追问。
```

在 Codex 中可以使用 `$key-reporting` 显式引用，或直接描述任务。

## 目录结构

```text
agent-skills/
├── skills/
│   └── key-reporting/        # 每个技能一个目录
│       ├── SKILL.md          # 必需：frontmatter + 指令
│       ├── README.md         # 面向使用者的文档
│       ├── references/       # 按需加载的参考资料
│       └── assets/           # 示例与可复用产物
├── template/
│   └── SKILL.md              # 新技能模板
├── README.md                 # English
├── README.zh-CN.md           # 简体中文
└── LICENSE
```

一个技能只需要一个目录和一个 `SKILL.md`。Frontmatter 有两个必填字段：

```yaml
---
name: my-skill
description: 技能做什么，以及 Agent 应在什么场景下使用它。
---
```

Frontmatter 之下就是 Agent 会遵循的指令。保持 `SKILL.md` 聚焦，把较长的参考资料放进 `references/`，把示例放进 `assets/`。

## 新建技能

1. 将 `template/` 复制为 `skills/<your-skill>/`。
2. 修改 `name` 字段，并写出面向触发场景的精确 `description`。
3. 在 `SKILL.md` 中写明工作流、判断规则和输出约定。
4. 把体积较大的资料与示例分别放入 `references/` 和 `assets/`。
5. 在上方技能表中登记，并在真实会话中测试。

## 许可证

基于 [MIT License](LICENSE) 发布。
