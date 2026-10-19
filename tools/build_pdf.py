#!/usr/bin/env python3
# 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · MIT⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​​‌‌​‌‌​​​‌‌​​​​​‌‌​​​‌​​​‌‌​​‌​​​‌‌​‌​‌​​‌‌​​​‌​‌‌​​​​‌​‌‌​​‌‌​​​‌‌​​‌​​‌‌​​​‌​​‌‌​​​‌‌​​‌‌​​‌‌⁠
# ============================================================
# shingja 的工科生手册 · 官方源码
# Author     : shingja
# Source     : https://github.com/shingja/ustb-engineering-handbook-shingja
# License    : MIT
# File-ID    : 60b251af2bc37f1a
# ============================================================

"""构建 PDF 手册：VitePress 构建 → 本地服务 → Playwright 打印 → pypdf 合并。"""
from __future__ import annotations

import argparse
import functools
import http.server
import socket
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

import fitz
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "docs" / ".vitepress" / "dist"
OUT = ROOT / "release" / "ustb-engineering-handbook-shingja.pdf"
TITLE = "shingja 的工科生手册"
AUTHOR = "shingja"
PAYLOAD = "esh/pdf"

PAGES = [
    ("封面", "/"),
    ("这本手册怎么用", "/00-使用指南/这本手册怎么用"),
    ("30 分钟快速开始", "/00-使用指南/30分钟快速开始"),
    ("信息力", "/10-信息力/"),
    ("检索与来源验证", "/10-信息力/检索与来源验证"),
    ("文件系统与命名", "/10-信息力/文件系统与命名"),
    ("备份与同步", "/10-信息力/备份与同步"),
    ("编码、后缀与压缩包", "/10-信息力/编码后缀与压缩包"),
    ("终端与批量操作", "/10-信息力/终端与批量操作"),
    ("浏览器插件与脚本风险", "/10-信息力/浏览器插件与脚本风险"),
    ("磁盘空间与软件清理", "/10-信息力/磁盘空间与软件清理"),
    ("信息甄别", "/10-信息力/信息甄别"),
    ("文档力", "/20-文档力/"),
    ("Word 排版最小工作流", "/20-文档力/Word排版最小工作流"),
    ("Excel 数据表与图表", "/20-文档力/Excel数据表与图表"),
    ("PPT 答辩叙事", "/20-文档力/PPT答辩叙事"),
    ("Markdown 与编辑器", "/20-文档力/Markdown与编辑器"),
    ("Mermaid 与 draw.io 图示", "/20-文档力/Mermaid与drawio图示"),
    ("排版、打印与 PDF", "/20-文档力/排版打印与PDF"),
    ("文档协作与版本", "/20-文档力/文档协作与版本"),
    ("代码与数据力", "/30-代码与数据力/"),
    ("Git 第一次提交", "/30-代码与数据力/Git第一次提交"),
    ("Python 环境与依赖", "/30-代码与数据力/Python环境与依赖"),
    ("GitHub 私有仓库与协作", "/30-代码与数据力/GitHub私有仓库与协作"),
    ("数据清洗与可复现", "/30-代码与数据力/数据清洗与可复现"),
    ("可视化与出图", "/30-代码与数据力/可视化与出图"),
    ("VS Code 配置", "/30-代码与数据力/VSCode配置"),
    ("代码质量与测试", "/30-代码与数据力/代码质量与测试"),
    ("AI 辅助编程边界", "/30-代码与数据力/AI辅助编程边界"),
    ("项目推进力", "/40-项目推进力/"),
    ("竞赛值不值得参加", "/40-项目推进力/竞赛值不值得参加"),
    ("选题：从问题出发", "/40-项目推进力/选题从问题出发"),
    ("组队与分工", "/40-项目推进力/组队与分工"),
    ("读规则与评分表", "/40-项目推进力/读规则与评分表"),
    ("项目管理与周报", "/40-项目推进力/项目管理与周报"),
    ("申报书写作", "/40-项目推进力/申报书写作"),
    ("原型与实验", "/40-项目推进力/原型与实验"),
    ("答辩准备", "/40-项目推进力/答辩准备"),
    ("复盘方法", "/40-项目推进力/复盘方法"),
    ("学业平衡", "/40-项目推进力/学业平衡"),
    ("经验卷", "/60-经验卷/"),
    ("做对了什么，做错了什么", "/60-经验卷/做对了什么做错了什么"),
    ("团队协作与冲突", "/60-经验卷/团队协作与冲突"),
    ("时间管理与学业平衡", "/60-经验卷/时间管理与学业平衡"),
    ("失败复盘", "/60-经验卷/失败复盘"),
    ("给不同年级的建议", "/60-经验卷/给不同年级的建议"),
    ("工具箱", "/70-工具箱/"),
    ("模板索引", "/70-工具箱/模板索引"),
    ("竞赛名录", "/70-工具箱/竞赛名录"),
    ("软件清单", "/70-工具箱/软件清单"),
    ("网站清单", "/70-工具箱/网站清单"),
    ("术语表", "/70-工具箱/术语表"),
    ("FAQ", "/70-工具箱/FAQ"),
    ("附录", "/80-附录/"),
    ("许可与引用", "/80-附录/许可与引用"),
    ("版本与更新", "/80-附录/版本与更新"),
]


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class _CleanUrlsHandler(http.server.SimpleHTTPRequestHandler):
    """把 /foo 映射到 /foo.html，支持 VitePress cleanUrls。"""

    def translate_path(self, path: str) -> str:
        resolved = super().translate_path(path)
        if not Path(resolved).exists() and Path(resolved + ".html").exists():
            return resolved + ".html"
        if Path(resolved).is_dir() and Path(resolved, "index.html").exists():
            return str(Path(resolved, "index.html"))
        return resolved

    def log_message(self, *args) -> None:
        pass


def _serve(directory: Path, port: int) -> http.server.ThreadingHTTPServer:
    handler = functools.partial(_CleanUrlsHandler, directory=str(directory))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def build_site() -> None:
    subprocess.run(["npm", "run", "docs:build"], cwd=ROOT, check=True)


def print_pages(port: int, workdir: Path) -> list[Path]:
    pdfs = []
    base = f"http://127.0.0.1:{port}"
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        for index, (_title, route) in enumerate(PAGES):
            page.goto(base + route, wait_until="networkidle", timeout=60000)
            page.emulate_media(media="print")
            target = workdir / f"{index:02d}.pdf"
            options = {
                "path": str(target),
                "format": "A4",
                "print_background": True,
                "display_header_footer": False,
                "margin": {"top": "18mm", "bottom": "22mm", "left": "16mm", "right": "16mm"},
            }
            if index == 0:
                options["page_ranges"] = "1"
            page.pdf(**options)
            pdfs.append(target)
        browser.close()
    return pdfs


def merge(pdfs: list[Path]) -> None:
    doc = fitz.open()
    toc = []
    for pdf, (title, _route) in zip(pdfs, PAGES):
        start = doc.page_count + 1
        with fitz.open(pdf) as source:
            doc.insert_pdf(source)
        toc.append([1, title, start])
    total = doc.page_count
    fontfile = "C:/Windows/Fonts/simhei.ttf"
    for index, page in enumerate(doc):
        footer = (
            "shingja · github.com/shingja/ustb-engineering-handbook-shingja · "
            f"第 {index + 1} / {total} 页"
        )
        page.insert_text(
            (45, page.rect.height - 28),
            footer,
            fontsize=8,
            fontname="simhei",
            fontfile=fontfile,
            color=(0.4, 0.4, 0.4),
        )
    doc.set_metadata({
        "title": TITLE,
        "author": AUTHOR,
        "subject": f"工科生竞赛与项目手册 · USTB · {PAYLOAD}",
        "creator": AUTHOR,
        "producer": AUTHOR,
        "keywords": f"USTB, 工科, 竞赛, 项目, 手册, {PAYLOAD}",
    })
    doc.set_toc(toc)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT, garbage=4, deflate=True)
    doc.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-build", action="store_true")
    args = parser.parse_args()
    if not args.no_build:
        build_site()
    if not DIST.is_dir():
        print("缺少 VitePress 构建产物，先运行 npm run docs:build", file=sys.stderr)
        return 1
    port = _free_port()
    server = _serve(DIST, port)
    try:
        with tempfile.TemporaryDirectory() as tmp:
            pdfs = print_pages(port, Path(tmp))
            merge(pdfs)
    finally:
        server.shutdown()
    print(f"PDF 已生成：{OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
