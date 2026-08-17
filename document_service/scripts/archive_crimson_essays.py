"""Build a clean, printable HTML archive of the Crimson's 2020 essay collection."""

from __future__ import annotations

import argparse
import html
import json
import re
import urllib.request
from pathlib import Path


SLUGS = ("sarah", "lucien", "chaffee", "john", "winnie", "lessard", "danielle", "josh", "octav")
BASE_URL = "https://www.thecrimson.com/sponsored/article/successful-essays-2020-{slug}/"


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 document-archive/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def paragraphs(page: str) -> list[str]:
    match = re.search(r'"paragraphs":\{"type":"json","json":(\[.*?\])\},"authorDescript"', page)
    if not match:
        raise ValueError("could not find serialized article paragraphs")
    return json.loads(match.group(1))


def build(output: Path) -> None:
    sections: list[str] = []
    for slug in SLUGS:
        url = BASE_URL.format(slug=slug)
        body = "\n".join(p for p in paragraphs(fetch(url)) if "shortcode-" not in p)
        sections.append(
            f'<section><h2>{html.escape(slug.title())}</h2>'
            f'<p class="source">Source: <a href="{url}">{url}</a></p>{body}</section>'
        )
    output.write_text(
        """<!doctype html><html><head><meta charset="utf-8"><title>10 Successful Harvard Application Essays | 2020</title>
<style>
@page { size: letter; margin: 0.7in; }
body { color: #202020; font: 11pt/1.45 Georgia, serif; max-width: 7in; margin: auto; }
h1, h2 { color: #8b0000; line-height: 1.15; } h1 { font-size: 24pt; }
h2 { font-size: 18pt; margin-top: 0; } section { break-before: page; }
section:first-of-type { break-before: auto; } .source { color: #555; font: 8pt Arial, sans-serif; }
a { color: #555; overflow-wrap: anywhere; } strong { font-family: Arial, sans-serif; letter-spacing: .04em; }
</style></head><body>
<h1>10 Successful Harvard Application Essays | 2020</h1>
<p>Archived from The Harvard Crimson sponsored collection. The source page currently exposes nine named essay entries. Each entry includes the essay and the published review.</p>
<p class="source">Collection: https://www.thecrimson.com/topic/sponsored-successful-harvard-essays-2020/</p>
"""
        + "\n".join(sections)
        + "</body></html>",
        encoding="utf-8",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    build(parser.parse_args().output)
