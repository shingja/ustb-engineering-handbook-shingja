---
title: GitHub 私有仓库与协作
description: 私有仓库、分支、Issue、PR、Release、Actions 与团队协作边界。
---
<!-- 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · CC BY-NC-SA 4.0 -->⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​​‌‌​‌​​​​‌‌​​‌​​​‌‌​‌​​​​‌‌​​​​​‌‌​​‌​​​​‌‌​​‌​​‌‌​​‌​​​​‌‌‌​​​​‌‌​​‌​​​​‌‌​​​​​‌‌​​​​‌​‌‌​​‌‌​⁠

# GitHub 私有仓库与协作

## 适用场景

你要把项目代码/文档放到 GitHub，暂时不想公开；队友要一起改；你要留版本、发提交包、做自动化检查。

## 最小做法

### 建私有仓库

1. GitHub → New repository。
2. 选 **Private**。
3. 不要勾“Add a README”，避免和本地冲突。
4. 本地：

```powershell
git init
git add .
git commit -m "chore: initial commit"
git branch -M main
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```

### 分支

- `main` 保持可交付。
- 每个功能/修复开一个分支：`feat/login`、`fix/typo`。
- 改完提 PR，合并后删分支。

```powershell
git switch -c feat/export
git add .
git commit -m "feat: add pdf export"
git push -u origin feat/export
```

### Issue

- 一个 issue 只做一件事。
- 写清：背景、期望结果、验收标准。
- 用 label 区分 `bug`、`docs`、`enhancement`。
- 关闭 issue 时写一句“怎么验证的”。

### PR

- 标题写“做了什么”。
- 描述写：改了什么、为什么、怎么验证。
- 小步提交，一次 PR 不要改 50 个文件。
- 合并前至少自己跑一遍测试/构建。

### Release

- 打 tag：`v1.0.0`。
- Release 附：变更说明、安装包/PDF、`SHA256SUMS`。
- 提交包和源码分开，不要把大文件塞进 Git。

### Actions 入门

最小 CI：

```yaml
name: CI
on: [push, pull_request]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: python -m unittest discover -s tests
```

## 进阶做法

- 用 `CODEOWNERS` 指定审查人。
- 用分支保护：禁止 force push、要求 PR、要求 CI 通过。
- 用 Dependabot 自动更新依赖。
- 用 Issue 模板/PR 模板统一格式。
- 用 `git tag -s` 签名发布。
- 用 `gh` CLI 少点网页。

## 常见坑

- 私有仓库里放密钥、密码、个人信息，转公开后全泄露。
- 把数据集、模型权重、安装包提交进 Git，仓库几个 GB。
- 直接在 `main` 上改，出错无法回退。
- PR 太大，队友没法 review。
- CI 权限过大，PR 能改工作流/读 secrets。
- Release 没有校验文件，下载后不知道是否完整。
- 仓库公开前没清理 Git 历史。

## 自检清单

- [ ] 仓库是 Private（公开前）。
- [ ] `.gitignore` 排除依赖、数据、密钥。
- [ ] `main` 可交付，功能在分支上开发。
- [ ] PR 描述写清“改了什么/为什么/怎么验证”。
- [ ] CI 只读权限，action 固定版本。
- [ ] Release 附变更说明和 SHA256SUMS。
- [ ] 公开前扫描 Git 历史中的敏感信息。

## 版本与时效

本文基于 Git 2.55、GitHub 2026 界面、GitHub Actions。界面会变，但“分支 + PR + CI + Release”的协作模型不变。
