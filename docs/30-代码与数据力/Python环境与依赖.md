---
title: Python 环境与依赖
description: Python 版本、虚拟环境、conda/uv、依赖锁定与可复现。
---
<!-- 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · CC BY-NC-SA 4.0 -->⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​​‌‌​‌​​​‌‌​​​‌​​‌‌​​​​‌​​‌‌​​‌​​​‌‌​​​​​‌‌​​​​‌​​‌‌​‌‌‌​‌‌​​​​‌​‌‌​​​​‌​‌‌​​​‌​​‌‌​​​​‌​​‌‌​‌​​⁠

# Python 环境与依赖

## 适用场景

你换了电脑，项目跑不起来；同一个包在两个项目里版本冲突；队友说“我这里能跑”；`pip install` 装到一半报错。

## 最小做法

### 一个项目一个虚拟环境

不要把所有包装在全局 Python 里。

用 `venv`：

```powershell
cd D:\work\project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

macOS/Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

退出：

```powershell
deactivate
```

### 记录依赖

```powershell
pip freeze > requirements.txt
pip install -r requirements.txt
```

规则：

- 项目根目录放 `requirements.txt` 或 `pyproject.toml`。
- 锁定版本：`numpy==2.1.3`，不要只写 `numpy`。
- 开发依赖和运行依赖分开：`requirements-dev.txt`。
- 不要把 `.venv/` 提交到 Git。

### 选 Python 版本

- 新项目优先 3.11/3.12；库兼容性最好。
- 老项目按 `README` 指定版本，不要硬升。
- Windows 用官方安装包或 `winget`；不要装多个来路不明的 Python。
- 用 `py -0p` 查看已安装版本。

### 常见安装问题

- 公司/学校网络慢：换镜像源。
- 需要编译的包（如某些科学计算库）：优先用 `conda` 或预编译 wheel。
- 权限错误：不要用管理员全局安装，回到虚拟环境。
- 包冲突：新建干净环境重装，不要在一个环境里反复升降级。

## 进阶做法

- 用 `uv` 管理环境和依赖，速度快：

```powershell
uv venv
uv pip install -r requirements.txt
```

- 用 `conda` 管理需要 C/Fortran 依赖的科学计算环境：

```powershell
conda create -n project python=3.11
conda activate project
```

- 用 `pyproject.toml` 记录项目元数据和依赖。
- 用 `pip-tools` 生成锁定文件。
- 在 README 写清：Python 版本、安装命令、运行命令、已知问题。

## 常见坑

- 全局装包，项目之间互相污染。
- 只写 `pip install xxx`，不记录版本，半年后复现不了。
- 把 `.venv/` 提交进 Git，仓库巨大。
- 在系统 Python 里 `pip install`，把系统工具搞坏。
- 混用 conda 和 pip，依赖冲突难排查。
- 不写 README，队友不知道用哪个 Python。
- 安装失败就 `--force-reinstall`，越修越乱。

## 自检清单

- [ ] 每个项目有独立虚拟环境。
- [ ] `.venv/` 在 `.gitignore` 里。
- [ ] 依赖版本已锁定。
- [ ] README 写了 Python 版本和安装命令。
- [ ] 运行命令能一条命令复现。
- [ ] 新环境从零安装能成功。
- [ ] 没有把包全局安装到系统 Python。

## 版本与时效

本文基于 Python 3.11、pip 26、uv 0.8、conda 23。命令会变，但“一项目一环境 + 锁版本 + README 可复现”的原则不变。
