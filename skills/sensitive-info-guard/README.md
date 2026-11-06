# Sensitive Info Guard

提交代码前的敏感信息审查技能，适用于支持 Agent Skills 的 Claude Code、Codex 等编码代理。

## 触发

在已加载该技能的代理中说：

- `提交代码`
- `帮我 commit`
- `检查一下这些修改有没有敏感信息，然后提交`

技能将先检查本次拟提交的 Git 文件，再判断能否继续提交。高风险内容会阻断提交；不确定内容要求确认；没有风险才提交。不会自动推送。

## 安装

将整个 `sensitive-info-guard` 文件夹复制到相应的技能目录：

```bash
# Claude Code（个人）
mkdir -p ~/.claude/skills
cp -r sensitive-info-guard ~/.claude/skills/

# Codex（个人）
mkdir -p ~/.agents/skills
cp -r sensitive-info-guard ~/.agents/skills/
```

也可以放在项目级 `.claude/skills/` 或 `.agents/skills/` 下。重启/重新加载代理以刷新技能发现。

## 限制

这是通过自然语言触发的 Agent Skill，不是 Git 原生 hook。它只在代理执行提交任务时生效，不能拦截终端里直接运行的 `git commit`。对于私有公司、人名与项目关键词，可在本机另建不入库的私有名单交给代理使用，切勿写入这个公开仓库。
