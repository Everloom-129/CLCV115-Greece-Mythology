# 更新日志

记录项目内容与文档的每一次更新。新增条目请置于最上方。

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/) 的精神，日期采用 `YYYY-MM-DD`。

## [未发布]

### 新增（古希腊风格美化）
- 全站换用古希腊视觉主题：大理石 / 羊皮纸底色、爱琴海蓝 + 赤陶红 + 黄金配色，Cinzel + EB Garamond + Noto Serif SC 字体。
- 新增黄金回纹（Greek key / meander）装饰：标题下缀、导航栏分隔、`.greek-divider` 分隔线。
- 首页新增英雄横幅（hero），课程资料 / 表格 / 卡片 / 提示框等统一为石碑式样。
- 图像画廊改为带画框的响应式网格（`scripts/build_gallery.py` 生成 `<figure>` 卡片）。
- 自定义样式位于 `docs/stylesheets/extra.css`，`mkdocs.yml` 启用 `navigation.tabs` 顶部标签导航。

### 修复
- 修正仓库名大小写：图像画廊的 raw 链接、站点 URL 与文档内链接统一为 `Everloom-129/CLCV115-Greece-Mythology`，避免大小写导致的图片加载失败 / 404。
- `mkdocs.yml` 新增 `site_url`。

### 新增
- 搭建 MkDocs Material 文档站点，并通过 GitHub Actions 自动部署到 GitHub Pages。
- 新增首页、剧本设计、图像画廊、课程资料、更新日志等文档页面。
- 新增 `CLAUDE.md` 文档维护规则：每次功能 / 内容更新都需同步更新文档并推送到 `main`。
