// 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · CC BY-NC-SA 4.0⁠​‌‌‌​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​​‌​​​‌​‌‌​‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​‌‌​‌​‌‌​‌​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌​‌‌​​‌​‌‌​‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌‌​​‌‌​‌‌​‌​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌‌‌​‌‌​‌​‌​​‌‌​​​​‌​​‌​‌‌‌‌​‌‌​​‌​‌​​‌‌​​‌‌​‌‌​​‌​​​‌‌​​‌​​​​‌‌​​‌​​​‌‌​​‌​​​‌‌​​‌​​​‌‌​‌‌‌​‌‌​​‌​‌​​‌‌‌​​‌​​‌‌​​​‌​​‌‌​​​‌⁠
// ============================================================
// shingja 的工科生手册 · 官方源码
// Author     : shingja
// Source     : https://github.com/shingja/ustb-engineering-handbook-shingja
// License    : MIT
// File-ID    : e3dd2227e911b905
// ============================================================

import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: 'shingja 的工科生手册',
  description: '竞赛、项目、工具，和一些踩过的坑。面向北京科技大学工科本科生。',
  base: process.env.DOCS_BASE || '/',
  cleanUrls: false,
  lastUpdated: true,
  // templates/ 与 checklists/ 在 docs/ 之外，VitePress 无法解析；
  // 用 tools/check_links.py 做真实文件存在性检查。
  ignoreDeadLinks: true,
  head: [
    ['meta', { name: 'author', content: 'shingja' }],
    ['meta', { name: 'robots', content: 'index,follow' }],
  ],
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '手册', link: '/00-使用指南/这本手册怎么用' },
      { text: '模板', link: '/70-工具箱/模板索引' },
      { text: '经验', link: '/60-经验卷/' },
      { text: '关于', link: '/80-附录/' },
    ],
    sidebar: {
      '/': [
        {
          text: '开始',
          items: [
            { text: '这本手册怎么用', link: '/00-使用指南/这本手册怎么用' },
          ],
        },
        {
          text: '卷一 · 信息力',
          items: [
            { text: '卷首', link: '/10-信息力/' },
            { text: '检索与来源验证', link: '/10-信息力/检索与来源验证' },
            { text: '文件系统与命名', link: '/10-信息力/文件系统与命名' },
            { text: '备份与同步', link: '/10-信息力/备份与同步' },
            { text: '编码、后缀与压缩包', link: '/10-信息力/编码后缀与压缩包' },
            { text: '终端与批量操作', link: '/10-信息力/终端与批量操作' },
            { text: '浏览器插件与脚本风险', link: '/10-信息力/浏览器插件与脚本风险' },
            { text: '磁盘空间与软件清理', link: '/10-信息力/磁盘空间与软件清理' },
            { text: '信息甄别', link: '/10-信息力/信息甄别' },
          ],
        },
        {
          text: '卷二 · 文档力',
          items: [
            { text: '卷首', link: '/20-文档力/' },
            { text: 'Word 排版最小工作流', link: '/20-文档力/Word排版最小工作流' },
            { text: 'Excel 数据表与图表', link: '/20-文档力/Excel数据表与图表' },
            { text: 'PPT 答辩叙事', link: '/20-文档力/PPT答辩叙事' },
            { text: 'Markdown 与编辑器', link: '/20-文档力/Markdown与编辑器' },
            { text: 'Mermaid 与 draw.io 图示', link: '/20-文档力/Mermaid与drawio图示' },
            { text: '排版、打印与 PDF', link: '/20-文档力/排版打印与PDF' },
            { text: '文档协作与版本', link: '/20-文档力/文档协作与版本' },
          ],
        },
        {
          text: '卷三 · 代码与数据力',
          items: [
            { text: '卷首', link: '/30-代码与数据力/' },
            { text: 'Git 第一次提交', link: '/30-代码与数据力/Git第一次提交' },
            { text: 'Python 环境与依赖', link: '/30-代码与数据力/Python环境与依赖' },
            { text: 'GitHub 私有仓库与协作', link: '/30-代码与数据力/GitHub私有仓库与协作' },
            { text: '数据清洗与可复现', link: '/30-代码与数据力/数据清洗与可复现' },
            { text: '可视化与出图', link: '/30-代码与数据力/可视化与出图' },
            { text: 'VS Code 配置', link: '/30-代码与数据力/VSCode配置' },
            { text: '代码质量与测试', link: '/30-代码与数据力/代码质量与测试' },
            { text: 'AI 辅助编程边界', link: '/30-代码与数据力/AI辅助编程边界' },
          ],
        },
        {
          text: '卷四 · 项目推进力',
          items: [
            { text: '卷首', link: '/40-项目推进力/' },
            { text: '竞赛值不值得参加', link: '/40-项目推进力/竞赛值不值得参加' },
            { text: '选题：从问题出发', link: '/40-项目推进力/选题从问题出发' },
            { text: '组队与分工', link: '/40-项目推进力/组队与分工' },
            { text: '读规则与评分表', link: '/40-项目推进力/读规则与评分表' },
            { text: '项目管理与周报', link: '/40-项目推进力/项目管理与周报' },
            { text: '申报书写作', link: '/40-项目推进力/申报书写作' },
            { text: '原型与实验', link: '/40-项目推进力/原型与实验' },
            { text: '答辩准备', link: '/40-项目推进力/答辩准备' },
            { text: '复盘方法', link: '/40-项目推进力/复盘方法' },
            { text: '学业平衡', link: '/40-项目推进力/学业平衡' },
          ],
        },
        {
          text: '其他',
          items: [
            { text: '经验卷', link: '/60-经验卷/' },
            { text: '做对了什么，做错了什么', link: '/60-经验卷/做对了什么做错了什么' },
            { text: '团队协作与冲突', link: '/60-经验卷/团队协作与冲突' },
            { text: '时间管理与学业平衡', link: '/60-经验卷/时间管理与学业平衡' },
            { text: '失败复盘', link: '/60-经验卷/失败复盘' },
            { text: '给不同年级的建议', link: '/60-经验卷/给不同年级的建议' },
            { text: '工具箱', link: '/70-工具箱/' },
            { text: '模板索引', link: '/70-工具箱/模板索引' },
            { text: '竞赛名录', link: '/70-工具箱/竞赛名录' },
            { text: '软件清单', link: '/70-工具箱/软件清单' },
            { text: '网站清单', link: '/70-工具箱/网站清单' },
            { text: '术语表', link: '/70-工具箱/术语表' },
            { text: 'FAQ', link: '/70-工具箱/FAQ' },
            { text: '附录', link: '/80-附录/' },
            { text: '许可与引用', link: '/80-附录/许可与引用' },
          ],
        },
      ],
    },
    outline: { level: [2, 3], label: '本页目录' },
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/shingja/ustb-engineering-handbook-shingja' }],
    footer: {
      message: '内容 CC BY-NC-SA 4.0 · 代码与模板 MIT',
      copyright: 'Copyright © 2026 shingja · 唯一官方地址 github.com/shingja/ustb-engineering-handbook-shingja',
    },
    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdatedText: '最后更新',
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色',
    darkModeSwitchTitle: '切换到深色',
  },
})
