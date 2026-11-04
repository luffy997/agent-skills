# key-reporting：关键汇报助手

面向研发及通用专业汇报场景的结构化表达技能，遵循“想清楚、说明白、接得住”的工作流，适用于 Claude Code、Codex 等兼容 Agent Skills 的工具。

## 功能

- 汇报前五问和核心主张提炼
- 周报、项目进度、技术评审、故障复盘、客户交流的结构化提纲
- 一页一个观点、病药效托、观点—论述—总结
- 模拟领导/评委追问及证据缺口识别
- 12分制质量检查与事实红线

## 安装

Claude Code（个人）：

```bash
mkdir -p ~/.claude/skills
cp -r key-reporting ~/.claude/skills/
```

Claude Code（项目）：

```bash
mkdir -p .claude/skills
cp -r key-reporting .claude/skills/
```

Codex（个人）：

```bash
mkdir -p ~/.agents/skills
cp -r key-reporting ~/.agents/skills/
```

Codex（项目）：

```bash
mkdir -p .agents/skills
cp -r key-reporting .agents/skills/
```

## 使用示例

- `/key-reporting 帮我把下面的研发周报改成面向研发负责人的汇报：……`（Claude Code）
- `使用 key-reporting，帮我给这次技术评审准备8个高风险追问。`
- `使用 key-reporting，把以下故障复盘改为5分钟口头汇报，不要新增事实：……`
- `使用 key-reporting，给我设计一个不超过8页的项目进展汇报提纲：……`

Codex 中可以使用 `$key-reporting` 显式引用，或直接用自然语言描述相应任务。

## 文件说明

- `SKILL.md`：核心行为规则和工作流
- `references/`：五问工作卡、场景手册、答辩手册、质量门禁
- `assets/example-report.md`：演示示例

本技能不依赖额外程序包，不会自动读取业务数据或生成未经要求的文件。
