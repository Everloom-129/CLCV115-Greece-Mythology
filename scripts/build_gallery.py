#!/usr/bin/env python3
"""Generate docs/gallery.md from the images in Tartarus/.

Images are referenced via GitHub raw URLs (URL-encoded) so that filenames with
spaces, periods and non-ASCII characters render correctly both on the deployed
GitHub Pages site and when browsing the repo locally.

Run this whenever images are added/removed from Tartarus/:

    python scripts/build_gallery.py
"""
from __future__ import annotations

import pathlib
from urllib.parse import quote

REPO = "everloom-129/clcv115-greece-mythology"
BRANCH = "main"
SOURCE_DIR = "Tartarus"
OUTPUT = pathlib.Path("docs/gallery.md")
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

ROOT = pathlib.Path(__file__).resolve().parent.parent


def description(name: str) -> str:
    """Derive the full description from a DALL·E-style filename."""
    stem = pathlib.Path(name).stem
    # DALL·E exports look like: "DALL·E <date> <time> - <description>"
    if " - " in stem:
        stem = stem.split(" - ", 1)[1]
    return stem.strip().rstrip(".")


def title(desc: str, limit: int = 60) -> str:
    """A short heading: first sentence, truncated to `limit` chars."""
    head = desc.split(". ", 1)[0]
    if len(head) > limit:
        head = head[:limit].rsplit(" ", 1)[0] + "…"
    return head


def raw_url(name: str) -> str:
    encoded = quote(f"{SOURCE_DIR}/{name}")
    return f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{encoded}"


def main() -> None:
    source = ROOT / SOURCE_DIR
    images = sorted(
        p.name for p in source.iterdir() if p.suffix.lower() in IMAGE_EXTS
    )

    lines = [
        "# 图像画廊",
        "",
        "> 冥界塔尔塔罗斯（Tartarus）主题图像，由 DALL·E 3 生成。",
        ">",
        "> 本页由 `scripts/build_gallery.py` 自动生成，请勿手动编辑。",
        "",
        f"共 {len(images)} 张图像。",
        "",
    ]

    for name in images:
        desc = description(name)
        url = raw_url(name)
        lines.append(f"## {title(desc)}")
        lines.append("")
        lines.append(f"![{desc}]({url})")
        lines.append("")
        lines.append(f"*{desc}*")
        lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT} with {len(images)} images.")


if __name__ == "__main__":
    main()
