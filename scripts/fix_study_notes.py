import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from enrich_phase13_14 import match_topic_theory, wrap_theory_body

GENERIC = re.compile(
    r"<details><summary>Theory and explanation</summary>\s*\n\*\*Study note:\*\* Original prompt was incomplete.*?</details>",
    re.S,
)


def fix_study_notes(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    def repl(m):
        block = m.group(0)
        pm = re.search(r"\*\*Prompt:\*\*\s*(.+?)(?=\n\n\*\*Interview)", block, re.S)
        prompt = pm.group(1).strip() if pm else ""
        topic = match_topic_theory(prompt)
        if topic:
            body = wrap_theory_body(topic, prompt)
        else:
            body = wrap_theory_body(
                "Prepare a structured verbal answer: definition, example, and trade-off.",
                prompt,
            )
        return "<details><summary>Theory and explanation</summary>\n\n" + body.strip() + "\n\n</details>"

    new, n = GENERIC.subn(repl, text)
    path.write_text(new, encoding="utf-8")
    print(path.name, "replaced", n, "remaining", new.count("Study note:"))


if __name__ == "__main__":
    base = Path(__file__).resolve().parents[1] / "docs/companies"
    for name in ("exabyting.md", "bs23.md"):
        fix_study_notes(base / name)
