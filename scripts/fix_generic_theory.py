import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from enrich_phase13_14 import match_topic_theory, wrap_theory_body

GENERIC = re.compile(
    r"<details><summary>Theory and explanation</summary>\s*\n\nPrepare a structured verbal answer: definition, example, and trade-off\.\s*\n\n\*\*Interview talking points\*\*.*?</details>",
    re.S,
)


def fix_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    articles = list(re.finditer(r"<article>.*?</article>", text, re.S))
    replaced = 0
    for art in reversed(articles):
        block = art.group(0)
        if "Prepare a structured verbal answer" not in block:
            continue
        qm = re.match(r"<article>\s*(.*?)(?=\n<details>)", block, re.S)
        question = qm.group(1).strip() if qm else ""
        topic = match_topic_theory(question)
        if not topic:
            continue
        body = wrap_theory_body(topic, question)
        new_block = re.sub(
            GENERIC,
            "<details><summary>Theory and explanation</summary>\n\n" + body.strip() + "\n\n</details>",
            block,
            count=1,
        )
        if new_block != block:
            text = text[: art.start()] + new_block + text[art.end() :]
            replaced += 1
    path.write_text(text, encoding="utf-8")
    print(path.name, "fixed", replaced, "generic left", text.count("Prepare a structured verbal answer"))


if __name__ == "__main__":
    base = Path(__file__).resolve().parents[1] / "docs/companies"
    for name in ("exabyting.md", "bs23.md"):
        fix_file(base / name)
