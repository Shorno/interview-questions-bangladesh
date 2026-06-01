#!/usr/bin/env python3
"""Remove duplicate theory, generic talking points, and placeholder JS tabs."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPANIES = ROOT / "docs" / "companies"

GENERIC_TALKING = re.compile(
    r"\n*\*\*Interview talking points\*\*\s*\n+"
    r"- Relate the answer to the company stack \(Java, Spring, Node, React\) when you have project experience\.\s*\n"
    r"- Mention trade-offs \(time vs space, consistency vs availability\) (?:when they apply|if applicable)\.\s*\n*",
    re.I,
)

PLACEHOLDER_JS_MARKERS = (
    "Illustrative pattern — adapt naming",
    "Conceptual demo — not always required",
    "Use this tab to show you can express ideas in code",
)

JS_DETAILS = re.compile(
    r"<details><summary>Solution \(JavaScript\)</summary>.*?</details>",
    re.S,
)

THEORY_DETAILS = re.compile(
    r"(<details><summary>Theory and explanation</summary>\s*\n+)(.*?)(\n+</details>)",
    re.S,
)


def dedupe_paragraphs(body: str) -> str:
    paras = re.split(r"\n\n+", body.strip())
    out: list[str] = []
    prev_key: str | None = None
    for p in paras:
        p = p.strip()
        if not p:
            continue
        key = re.sub(r"\s+", " ", p).lower()
        if prev_key is not None and key == prev_key:
            continue
        out.append(p)
        prev_key = key
    return "\n\n".join(out)


def clean_theory_body(body: str) -> str:
    body = GENERIC_TALKING.sub("\n\n", body)
    body = dedupe_paragraphs(body)
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def maybe_remove_js(m: re.Match) -> str:
    block = m.group(0)
    if any(marker in block for marker in PLACEHOLDER_JS_MARKERS):
        return "\n"
    return block


def clean_text(text: str) -> str:
    text = JS_DETAILS.sub(maybe_remove_js, text)

    def fix_theory(m: re.Match) -> str:
        return m.group(1) + clean_theory_body(m.group(2)) + m.group(3)

    text = THEORY_DETAILS.sub(fix_theory, text)
    return text


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    before = text.count("Solution (JavaScript)")
    cleaned = clean_text(text)
    removed = before - cleaned.count("Solution (JavaScript)")
    if cleaned != text:
        path.write_text(cleaned, encoding="utf-8")
    return removed


def main():
    total = 0
    for path in sorted(COMPANIES.rglob("*.md")):
        if path.name == "README.md" or ".draft" in path.name:
            continue
        n = process_file(path)
        if n:
            print(f"{path.relative_to(ROOT)}: removed {n} placeholder JS tab(s)")
        total += n
    print(f"Total placeholder JS tabs removed: {total}")


if __name__ == "__main__":
    main()
