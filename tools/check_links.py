#!/usr/bin/env python3
# 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · MIT⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​​‌‌​‌‌​​​‌‌​‌​​​​‌‌‌​​​​​‌‌​‌‌​​‌‌​​‌​‌​‌‌​​‌‌​​​‌‌​​‌‌​​‌‌‌​​‌​​‌‌​‌​​​​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​​⁠
# ============================================================
# shingja 的工科生手册 · 官方源码
# Author     : shingja
# Source     : https://github.com/shingja/ustb-engineering-handbook-shingja
# License    : MIT
# File-ID    : 6486ef3947201f2a
# ============================================================

"""Markdown 内部链接检查。"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")


def check_file(path: Path, root: Path = ROOT) -> list[str]:
    problems = []
    text = path.read_text(encoding="utf-8")
    # 忽略 fenced code block 里的示例链接
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for target in LINK_RE.findall(text):
        if target.startswith(SKIP_PREFIXES):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        if clean.startswith("/"):
            resolved = (root / "docs" / "public" / clean.lstrip("/")).resolve()
        else:
            resolved = (path.parent / clean).resolve()
        if not resolved.exists():
            problems.append(f"{path.relative_to(root).as_posix()}: 链接不存在 {target}")
    return problems


def iter_markdown(root: Path) -> list[Path]:
    return [
        path for path in sorted(root.rglob("*.md"))
        if not any(
            part in {".git", "node_modules", "docs/.vitepress/cache", "docs/.vitepress/dist"}
            for part in path.parts
        )
        and "docs/internal/" not in path.as_posix()
        and "docs/superpowers/" not in path.as_posix()
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        parser.error("需要 --check")
    problems = []
    for path in iter_markdown(ROOT):
        problems.extend(check_file(path))
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    print(f"链接检查通过：{len(iter_markdown(ROOT))} 个 Markdown 文件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
