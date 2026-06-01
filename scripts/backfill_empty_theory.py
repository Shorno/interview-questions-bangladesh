#!/usr/bin/env python3
"""Restore theory when only Further reading remains after cleanup."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from enrich_phase13_14 import match_topic_theory, dedupe_paragraphs, further_reading_links

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "docs/companies/bs23.md", ROOT / "docs/companies/exabyting.md"]


def extract_question(article: str) -> str:
    m = re.match(r"<article>\s*(.*?)(?=\n<details>)", article, re.S)
    return m.group(1).strip() if m else ""


def theory_is_empty(body: str) -> bool:
    stripped = re.sub(r"#### Further reading.*", "", body, flags=re.S).strip()
    return len(stripped) < 20


def process(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    fixed = 0
    articles = list(re.finditer(r"<article>.*?</article>", text, re.S))
    for art in reversed(articles):
        block = art.group(0)
        m = re.search(
            r"<details><summary>Theory and explanation</summary>\s*\n+(.*?)\n+</details>",
            block,
            re.S,
        )
        if not m or not theory_is_empty(m.group(1)):
            continue
        q = extract_question(block)
        topic = match_topic_theory(q) or (
            "**Answer framework:** State the direct answer first, then explain with one "
            "example and one trade-off.\n\n"
            f"**Question:** {q[:500]}"
        )
        new_body = dedupe_paragraphs(topic)
        if "#### Further reading" not in new_body:
            new_body += "\n\n" + further_reading_links(q)
        new_block = block[: m.start(1)] + new_body + block[m.end(1) :]
        text = text[: art.start()] + new_block + text[art.end() :]
        fixed += 1
    if fixed:
        path.write_text(text, encoding="utf-8")
    print(f"{path.name}: backfilled {fixed}")
    return fixed


if __name__ == "__main__":
    for f in FILES:
        process(f)
