#!/usr/bin/env python3
"""Scan staged Git blobs without printing their sensitive contents."""
import ipaddress
import os
import re
import subprocess
import sys
from pathlib import Path

EMAIL = re.compile(r'(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])')
IPV4 = re.compile(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])')
HOME = re.compile(r'(?:(?:/home/|/Users/)[A-Za-z0-9_.-]+/|[A-Za-z]:\\Users\\[^\\\s]+\\)')
CRED = re.compile(r'''(?ix)(?:password|passwd|pwd|secret(?:_key)?|api[_-]?key|access[_-]?token|auth[_-]?token|数据库密码|登录密码)\s*[:=]\s*["']?([^\s"',;#}]+)''')
PRIVATE_KEY = re.compile(r'-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----')
BLOCKED_FILES = re.compile(r'(?i)(?:^|/)(?:\.env(?:\..+)?|id_rsa|id_ed25519|[^/]+\.(?:pem|p12|pfx|key))$')
SAFE_VALUES = {'', 'none', 'null', 'true', 'false', 'password', 'changeme', 'example', 'your_password', 'your_token', 'xxx', '***', 'test', 'dummy', 'placeholder'}
MAX_BLOB = 2 * 1024 * 1024


def git(*args):
    return subprocess.run(['git', *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout


def private_terms():
    path = Path(os.environ.get('SENSITIVE_GUARD_TERMS', str(Path.home() / '.config/sensitive-info-guard/terms.txt')))
    if not path.exists():
        return []
    terms = []
    for line in path.read_text(encoding='utf-8').splitlines():
        val = line.strip()
        if val and not val.startswith('#'):
            terms.append(val.casefold())
    return terms


def main():
    try:
        paths = [p.decode('utf-8', 'surrogateescape') for p in git('diff', '--cached', '--name-only', '-z', '--diff-filter=ACMR').split(b'\0') if p]
        terms = private_terms()
        findings = []
        for path in paths:
            if BLOCKED_FILES.search(path):
                findings.append((path, '-', '敏感文件名'))
            try:
                blob = git('show', ':' + path)
            except subprocess.CalledProcessError:
                continue
            if len(blob) > MAX_BLOB or b'\0' in blob[:8192]:
                continue
            content = blob.decode('utf-8', errors='replace')
            for i, line in enumerate(content.splitlines(), 1):
                kinds = set()
                if PRIVATE_KEY.search(line): kinds.add('私钥')
                if HOME.search(line): kinds.add('用户目录绝对路径')
                for match in CRED.finditer(line):
                    val = match.group(1).strip().lower()
                    if val not in SAFE_VALUES and not val.startswith(('$', '${', '{{', '<', 'os.getenv', 'environ', 'your_', 'example_')):
                        kinds.add('疑似明文凭据')
                for m in IPV4.finditer(line):
                    try:
                        ip = ipaddress.ip_address(m.group())
                        if ip.is_private and not ip.is_loopback and not ip.is_link_local and not ip.is_reserved:
                            kinds.add('非公网 IPv4 地址')
                    except ValueError:
                        pass
                for m in EMAIL.finditer(line):
                    if not m.group().lower().endswith(('@example.com', '@example.org', '@example.net')):
                        kinds.add('邮箱地址')
                if any(t in line.casefold() for t in terms):
                    kinds.add('命中本地私有词库')
                for kind in sorted(kinds):
                    findings.append((path, str(i), kind))
        if findings:
            print(f'\n[敏感信息防泄漏] 检测到 {len(findings)} 项风险，已阻止提交：', file=sys.stderr)
            for path, line, kind in findings[:80]:
                print(f'  {path}:{line}  {kind}', file=sys.stderr)
            if len(findings) > 80:
                print(f'  ... 其余 {len(findings)-80} 项未显示', file=sys.stderr)
            print('请修复后重新 git add；扫描结果不会输出实际敏感值。', file=sys.stderr)
            return 1
        print('[敏感信息防泄漏] 本地规则检查通过')
        return 0
    except (OSError, UnicodeError, subprocess.CalledProcessError) as exc:
        print(f'[敏感信息防泄漏] 检查无法完成，默认拒绝提交：{type(exc).__name__}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
