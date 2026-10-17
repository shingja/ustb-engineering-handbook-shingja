<!-- 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · MIT -->⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌​‌‌​​​‌‌​‌​​​‌‌​​‌‌​​​‌‌‌​​‌​‌‌​​‌​‌​​‌‌​​‌‌​​‌‌​‌​​​​‌‌​‌‌​​​‌‌‌​​​​‌‌​​​‌‌⁠
# Python 项目骨架

最小可运行结构：

```text
python-project/
├─ pyproject.toml
├─ README.md
├─ src/
│  └─ main.py
└─ tests/
   └─ test_main.py
```

## 使用

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -e .
python -m unittest discover -s tests -v
```

## 约定

- 源码放 `src/`，测试放 `tests/`。
- 依赖写进 `pyproject.toml`，不要靠口头记忆。
- 提交前跑测试。
- 不提交 `.venv/`、`__pycache__/`、`.env`。

## 许可

MIT。模板来源：shingja 的工科生手册。
