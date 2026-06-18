# CLAUDE.md

本文件为 Claude Code（以及任何协作者）提供本仓库的工作约定。

## 项目简介

CLCV 115（Mythology of Greece and Rome）课程期末项目，内容包括：

- **戏剧剧本设计** —— 候选剧目、难度分析、投票与最终选定剧本。
- **AI 图像画廊** —— `Tartarus/` 目录下由 DALL·E 3 生成的冥界主题图像。
- **课程资料** —— `.pptx` 演示文稿与 `.pdf` 阅读材料。

## 文档站点

- 文档源文件位于 `docs/`，使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建。
- 站点配置见根目录 `mkdocs.yml`。
- 图像画廊页 `docs/gallery.md` 由 `scripts/build_gallery.py` **自动生成**，不要手动编辑。
- 通过 `.github/workflows/deploy-docs.yml`，每次推送到 `main` 时自动部署到 GitHub Pages。

### 本地预览

```bash
pip install -r docs/requirements.txt
python scripts/build_gallery.py   # 重新生成图像画廊
mkdocs serve                      # http://127.0.0.1:8000
```

## ⚠️ 文档同步规则（重要）

**每一次功能 / 内容更新，都必须同步更新文档，并推送到 `main` 分支。** 具体要求：

1. **同步写文档**：任何改动（新增剧本、补充资料、新增图像、修改流程等）完成后，必须在同一次提交 / PR 中更新 `docs/` 下对应的页面。功能代码与文档不可分离提交。
2. **更新画廊**：若改动了 `Tartarus/` 中的图像，运行 `python scripts/build_gallery.py` 重新生成 `docs/gallery.md`。
3. **记录更新日志**：在 `docs/changelog.md` 顶部新增一条对应记录（日期 + 简述）。
4. **推送到 `main`**：将变更推送到 `main` 分支；CI 会自动重新构建并发布 GitHub Pages 站点。
5. **新增页面同步更新导航**：如新增文档页面，记得在 `mkdocs.yml` 的 `nav` 中登记。

> 一句话：**功能改了，文档就得改，并 push 到 `main`。** 文档落后于功能视为未完成。

## 提交约定

- 提交信息使用清晰、描述性的语言，说明改动内容。
- 文档相关改动建议在信息中体现，例如：`docs: 更新剧本设计页面`。
