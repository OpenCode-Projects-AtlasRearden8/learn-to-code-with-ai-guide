import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

URL_RE = re.compile(r'(?:href|src)="([^"]+)"')
MD_LINK_RE = re.compile(r"\]\(([^)]+)\)")

problems = []


def check_file(path, targets, kind):
    text = path.read_text(encoding="utf-8")
    matches = URL_RE.findall(text) if kind == "html" else MD_LINK_RE.findall(text)
    for link in matches:
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = link.split("#")[0].split("?")[0]
        if not clean:
            continue
        if not (path.parent / clean).exists():
            problems.append(f"{path.relative_to(ROOT)} -> missing {link}")


for md in sorted(DOCS.glob("*.md")):
    check_file(md, None, "md")

for page in sorted(SITE.glob("*.html")):
    check_file(page, None, "html")

if problems:
    print("\n".join(problems))
    print(f"{len(problems)} broken link(s)")
    sys.exit(1)

print("ALL LINKS OK")
