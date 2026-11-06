#!/bin/sh
set -eu
ROOT=$(git rev-parse --show-toplevel)
if [ ! -f "$ROOT/scripts/check_sensitive.py" ]; then
  echo '请先将 scripts/ 目录复制到目标 Git 仓库根目录' >&2
  exit 1
fi
mkdir -p "$HOME/.config/sensitive-info-guard"
touch "$HOME/.config/sensitive-info-guard/terms.txt"
chmod 600 "$HOME/.config/sensitive-info-guard/terms.txt"
chmod +x "$ROOT/scripts/pre-commit"
git config --local core.hooksPath scripts
echo '已启用提交前钩子。请安装 gitleaks，并配置 ~/.config/sensitive-info-guard/terms.txt'
