---
title: VS Code 配置
description: 工作区、插件最小集、Python/LaTeX/Markdown、远程开发与设置同步。
---
<!-- 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · CC BY-NC-SA 4.0 -->⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌​​‌​‌​​‌‌​​​​​​‌‌​‌​‌​‌‌​​‌‌​​‌‌​​​​‌​‌‌​​​‌​​​‌‌​‌​​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌​​‌​‌​​‌‌​​​​​​‌‌​​​​⁠

# VS Code 配置

## 适用场景

你刚装 VS Code，插件一堆但不知道用哪个；打开项目全是红波浪线；想连服务器/另一台电脑写代码。

## 最小做法

### 先打开“文件夹”，不要只开单文件

- 文件 → 打开文件夹，选项目根目录。
- 项目根目录放 `.vscode/settings.json`，团队共用配置。
- 个人偏好放用户设置，不要提交到仓库。

### 插件最小集

按需安装，不要一次装 50 个：

- Python + Pylance：Python 补全/调试。
- C/C++：C++ 补全/调试。
- GitLens：看提交历史。
- Markdown All in One：目录、快捷键。
- markdownlint：Markdown 格式检查。
- Mermaid Preview：预览 Mermaid。
- Draw.io Integration：在 VS Code 里画图。

前端/嵌入式/LaTeX 再按项目加。

### 工作区配置

`.vscode/settings.json`：

```json
{
  "files.encoding": "utf8",
  "files.eol": "\n",
  "editor.formatOnSave": true,
  "editor.rulers": [88],
  "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true,
  "markdown.preview.breaks": true
}
```

### Python 解释器

1. `Ctrl+Shift+P` → Python: Select Interpreter。
2. 选项目 `.venv` 里的 Python。
3. 终端激活环境后再装包。
4. 左下角确认解释器路径。

### 远程开发

- 装 Remote - SSH 插件。
- `Ctrl+Shift+P` → Remote-SSH: Connect to Host。
- 在服务器上装 Python/扩展（部分扩展需远程安装）。
- 远程终端里跑命令，文件在服务器上。

## 进阶做法

- 用 Profiles 区分“Python”“嵌入式”“写作”三套配置。
- 用 Settings Sync 同步个人设置，但不要把密钥同步上去。
- 用 `.editorconfig` 统一缩进/换行。
- 用任务（tasks.json）一键构建/测试。
- 用调试配置（launch.json）复现运行环境。
- 用 Dev Container 固定开发环境。

## 常见坑

- 只打开单文件，Python 导入路径全错。
- 解释器选到全局 Python，包装错地方。
- 插件太多，启动慢、冲突多。
- 把 `.vscode/` 里的本机绝对路径提交到仓库。
- 远程开发时扩展装在本地，服务器上用不了。
- 自动格式化把整个文件重排，diff 爆炸。
- 设置同步把 token/密钥传到云端。

## 自检清单

- [ ] 打开的是项目文件夹，不是单文件。
- [ ] 解释器指向项目 `.venv`。
- [ ] `.vscode/settings.json` 不含本机绝对路径/密钥。
- [ ] 插件按需安装，没有明显冲突。
- [ ] 保存时格式化不会重排整个文件。
- [ ] 远程开发扩展装在远程端。
- [ ] 设置同步没有包含敏感信息。

## 版本与时效

本文基于 VS Code 1.141。插件名称和行为会变，但“工作区 + 解释器 + 最小插件集”的原则不变。
