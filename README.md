# CLCV115-Greece-Mythology

Author: Tony Wang

A repo for final project demonstration of *Mythology of Greece and Rome* (CLCV 115).

## 📖 文档站点 / Documentation

完整文档（剧本设计、图像画廊、课程资料）以 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建，部署在 GitHub Pages：

👉 **https://everloom-129.github.io/CLCV115-Greece-Mythology/**

> 首次启用：在仓库 **Settings → Pages → Build and deployment** 中，将 *Source* 设为 **Deploy from a branch**，**Branch** 选择 `gh-pages` / `(root)` 并保存。首次推送到 `main` 后，CI 会自动创建 `gh-pages` 分支。
>
> ⚠️ 注意：站点路径区分大小写，须与仓库名一致（`CLCV115-Greece-Mythology`）。

## 目录 / Category

- `Tartarus/` —— DALL·E 3 生成的冥界主题图像合集
- `Aeschylus.pptx` —— 埃斯库罗斯戏剧背景（围绕女神故事）
- `GreekMythology.pptx` —— 希腊神话总览演示文稿
- `GreecePlot.md` —— 剧本设计讨论记录
- `*.pdf` —— 《神谱》（Theogony）等阅读资料
- `docs/` —— 文档站点源文件
- `CLAUDE.md` —— 协作与文档维护约定

## 本地预览文档 / Local preview

```bash
pip install -r docs/requirements.txt
python scripts/build_gallery.py
mkdocs serve
```

## 文档维护规则

每次功能 / 内容更新都需**同步更新文档并推送到 `main`**，详见 [`CLAUDE.md`](CLAUDE.md)。
