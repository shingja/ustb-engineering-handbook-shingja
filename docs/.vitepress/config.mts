// 作者 shingja · https://github.com/shingja/ustb-engineering-handbook-shingja · CC BY-NC-SA 4.0

import { defineConfig } from 'vitepress'
import { sidebarFor, startSidebar } from './sidebar.mts'

const SITE = 'https://shingja.github.io/ustb-engineering-handbook-shingja/'

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
  sitemap: {
    hostname: 'https://shingja.github.io',
  },
  head: [
    ['meta', { name: 'author', content: 'shingja' }],
    ['meta', { name: 'robots', content: 'index,follow' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'shingja 的工科生手册' }],
    ['meta', { property: 'og:description', content: '竞赛、项目、工具，和一些踩过的坑。面向北京科技大学工科本科生。' }],
    ['meta', { property: 'og:image', content: `${SITE}og-cover.png` }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'shingja 的工科生手册' }],
    ['meta', { name: 'twitter:description', content: '竞赛、项目、工具，和一些踩过的坑。' }],
    ['meta', { name: 'twitter:image', content: `${SITE}og-cover.png` }],
  ],
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '开始', link: '/00-使用指南/30分钟快速开始' },
      { text: '手册', link: '/00-使用指南/这本手册怎么用' },
      { text: '竞赛名录', link: '/70-工具箱/竞赛名录' },
      { text: '经验', link: '/60-经验卷/' },
      { text: '关于', link: '/80-附录/' },
    ],
    sidebar: {
      '/00-使用指南/': startSidebar(),
      '/10-信息力/': sidebarFor('/10-信息力/'),
      '/20-文档力/': sidebarFor('/20-文档力/'),
      '/30-代码与数据力/': sidebarFor('/30-代码与数据力/'),
      '/40-项目推进力/': sidebarFor('/40-项目推进力/'),
      '/60-经验卷/': sidebarFor('/60-经验卷/'),
      '/70-工具箱/': sidebarFor('/70-工具箱/'),
      '/80-附录/': sidebarFor('/80-附录/'),
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
