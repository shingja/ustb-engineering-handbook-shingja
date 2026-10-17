---
title: Git 第一次提交
description: 从 git init 到远程私有仓库：配置、提交、忽略、推送与常见坑。
---
<!-- 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · CC BY-NC-SA 4.0 -->⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​​‌‌​​​‌​​‌‌​‌‌‌​‌‌​​‌‌​​​‌‌​‌​​​​‌‌​​‌‌​‌‌​​‌‌​​​‌‌​​​​​​‌‌​‌​‌​​‌‌​​​​​​‌‌​‌​​​‌‌​​​​‌​​‌‌​​‌‌⁠

# Git 第一次提交

## 适用场景

你开始写代码、写文档，或者要跟队友协作。你担心改坏了回不去，或者想把版本传到 GitHub 私有仓库。

## 最小做法

### 第一步：配置身份

```bash
git config --global user.name "你的名字或 ID"
git config --global user.email "你的邮箱"
git config --global init.defaultBranch main
```

如果要把仓库公开，建议用 GitHub 提供的 noreply 邮箱，避免私人邮箱进入提交历史。

### 第二步：初始化仓库

```bash
mkdir my-project
cd my-project
git init
```

### 第三步：看状态、加文件、提交

```bash
git status
git add README.md
git commit -m "docs: add README"
git log --oneline
```

一次提交只做一件事。提交信息写“做了什么”，不要写“update”。

### 第四步：写 `.gitignore`

至少忽略：

```text
node_modules/
__pycache__/
*.pyc
.env
.venv/
venv/
*.log
.DS_Store
Thumbs.db
```

密钥、密码、数据库文件、大模型权重、几十 MB 的安装包，都不要进 Git。

### 第五步：连到远程私有仓库

在 GitHub 新建私有仓库，不要勾选自动生成 README（避免和本地冲突），然后：

```bash
git remote add origin https://github.com/<user>/<repo>.git
git branch -M main
git push -u origin main
```

之后每次：

```bash
git add <文件>
git commit -m "feat: ..."
git push
```

### 第六步：回退

- 还没提交的修改：`git restore <文件>`
- 已提交但想撤销提交、保留修改：`git reset --soft HEAD~1`
- 想看某次提交改了什么：`git show <commit>`

不要用 `git reset --hard` 除非你确定不要那些修改。

## 进阶做法

- 用分支做实验：`git switch -c experiment`，失败就删分支。
- 用 `.gitattributes` 统一换行，避免 Windows/macOS 协作时整文件 diff。
- 大文件用 Git LFS，不要直接提交。
- 提交前跑测试，CI 通过再合并。
- 用 `git log --graph --oneline --all` 看分支结构。

## 常见坑

- 把 `.env`、密钥、token 提交进去。即使后来删除，历史里仍然存在。
- 在 OneDrive 同步目录里建 Git 仓库，两个系统同时改文件，容易冲突。
- 直接删 `.git` 目录“重置”，历史全部丢失。
- 把 `node_modules/`、`venv/`、数据集提交进去，仓库变成几个 GB。
- 提交信息只写“update”“修改”，三个月后自己都看不懂。
- 多人同时改同一个文件，不会处理冲突，直接覆盖队友的版本。

## 自检清单

- [ ] `git config user.name` 和 `user.email` 正确。
- [ ] `.gitignore` 覆盖了依赖、环境、密钥、日志。
- [ ] 第一次提交只包含必要文件。
- [ ] 远程仓库是私有的（公开前）。
- [ ] 提交信息能看懂“做了什么”。
- [ ] 我知道怎么回退一次提交。

## 版本与时效

本文基于 Git 2.55。Git 命令长期稳定，GitHub 界面会变，但仓库、提交、分支、推送的概念不变。
