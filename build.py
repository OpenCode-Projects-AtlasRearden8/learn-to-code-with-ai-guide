import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

CHAPTER_ORDER = [
    "00-welcome.md",
    "01-browser-basics.md",
    "02-variables.md",
    "03-loops.md",
    "04-functions.md",
    "05-ai-as-tutor.md",
    "06-when-code-breaks.md",
    "07-next-steps.md",
]


def slugify(text):
    slug = re.sub(r"[^a-z0-9\s-]", "", text.lower())
    return re.sub(r"[\s]+", "-", slug.strip()).strip("-") or "section"


def esc(text):
    return html.escape(text, quote=False)


def inline(text):
    parts = []
    backticks = text.split("`")
    for i, chunk in enumerate(backticks):
        if i % 2 == 1:
            parts.append('<code class="code-inline">%s</code>' % esc(chunk))
        else:
            t = esc(chunk)
            t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
            t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
            t = re.sub(
                r"\[([^\]]+)\]\(([^)\s]+)\)",
                lambda m: '<a href="%s">%s</a>' % (rewrite_link(m.group(2)), m.group(1)),
                t,
            )
            t = re.sub(r"(<a href=\"[^\"]*)\.md([^\"]*\")", r"\1.html\2", t)
            parts.append(t)
    return "".join(parts)


def rewrite_link(url):
    return html.escape(url, quote=True)


def blocks(md):
    lines = md.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            lang = line[3:].strip()
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append(("code", lang, "\n".join(code)))
            continue

        if line.startswith("### "):
            text = inline(line[4:].strip())
            out.append(("h3", text))
            i += 1
            continue
        if line.startswith("## "):
            text = inline(line[3:].strip())
            out.append(("h2", text))
            i += 1
            continue
        if line.startswith("# "):
            text = inline(line[2:].strip())
            out.append(("h1", text))
            i += 1
            continue

        if line.strip() == "---":
            out.append(("hr",))
            i += 1
            continue

        if line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i].lstrip(">").strip())
                i += 1
            out.append(("quote", inline(" ".join(quote))))
            continue

        if re.match(r"^- ", line):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(inline(lines[i][2:].strip()))
                i += 1
            out.append(("ul", items))
            continue

        if re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(inline(re.sub(r"^\d+\. ", "", lines[i]).strip()))
                i += 1
            out.append(("ol", items))
            continue

        if line.strip():
            para = [line.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(
                ("#", "```", ">", "- ", "  ")
            ) and lines[i].strip() != "---" and not re.match(r"^\d+\. ", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(("p", inline(" ".join(para))))
            continue

        i += 1

    return out


def render_blocks(block_list):
    tags = []
    for b in block_list:
        kind = b[0]
        if kind == "h1":
            tags.append('<h1 id="%s">%s</h1>' % (slugify(re.sub(r"<[^>]+>", "", b[1])), b[1]))
        elif kind == "h2":
            tags.append('<h2 id="%s">%s</h2>' % (slugify(re.sub(r"<[^>]+>", "", b[1])), b[1]))
        elif kind == "h3":
            tags.append("<h3>%s</h3>" % b[1])
        elif kind == "p":
            tags.append("<p>%s</p>" % b[1])
        elif kind == "ul":
            tags.append("<ul>%s</ul>" % "".join("<li>%s</li>" % t for t in b[1]))
        elif kind == "ol":
            tags.append("<ol>%s</ol>" % "".join("<li>%s</li>" % t for t in b[1]))
        elif kind == "quote":
            tags.append("<blockquote><p>%s</p></blockquote>" % b[1])
        elif kind == "hr":
            tags.append("<hr>")
        elif kind == "code":
            cls = " class=\"lang-%s\"" % b[1] if b[1] else ""
            tags.append("<pre><code%s>%s</code></pre>" % (cls, esc(b[2])))
    return "\n".join(tags)


def markdown_to_html(md):
    return render_blocks(blocks(md))


def chapter_title(md):
    for line in md.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}} — Learn to Code with AI</title>
<style>
  :root { color-scheme: light dark; }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: ui-sans-serif, system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.65;
    background: #faf7f2;
    color: #2b2b2b;
  }
  .wrap { max-width: 740px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; }
  header.site { background: #2f4858; color: #fdfbf7; }
  header.site .wrap { padding-top: 1.6rem; padding-bottom: 1.1rem; }
  header.site a { color: #fdfbf7; text-decoration: none; font-weight: 600; letter-spacing: 0.01em; }
  header.site a:hover { text-decoration: underline; }
  header.site .tagline { opacity: 0.85; font-size: 0.95rem; margin-top: 0.25rem; }
  h1, h2, h3 { line-height: 1.25; color: #1f344d; }
  h1 { font-size: 2rem; margin-top: 1.5rem; }
  h2 { font-size: 1.4rem; margin-top: 2.2rem; border-bottom: 1px solid #e5ded2; padding-bottom: 0.3rem; }
  h3 { font-size: 1.12rem; margin-top: 1.8rem; }
  p { margin: 1rem 0; }
  ul, ol { padding-left: 1.5rem; }
  li { margin: 0.35rem 0; }
  code, pre {
    font-family: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  }
  .code-inline { background: #efe9df; border-radius: 4px; padding: 0.1em 0.35em; font-size: 0.92em; }
  pre {
    background: #2b2b33;
    color: #e8e6e3;
    padding: 1rem 1.15rem;
    border-radius: 10px;
    overflow-x: auto;
    font-size: 0.92rem;
    line-height: 1.55;
  }
  pre code { background: none; color: inherit; padding: 0; }
  blockquote {
    margin: 1.2rem 0; padding: 0.85rem 1.2rem;
    border-left: 4px solid #6b8e9c; background: #f1ede4;
    border-radius: 0 8px 8px 0;
  }
  blockquote p { margin: 0.2rem 0; }
  a { color: #2f5d75; }
  hr { border: none; border-top: 1px solid #e5ded2; margin: 2.5rem 0; }
  footer.pagenav {
    margin-top: 3rem; padding-top: 1.2rem; border-top: 2px solid #e5ded2;
    display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap;
  }
  footer.pagenav a { font-weight: 600; }
  .meta { color: #7a7367; font-size: 0.9rem; margin-top: 3rem; }
  .chapter-card {
    border: 1px solid #e5ded2; border-radius: 10px; padding: 1rem 1.25rem;
    margin: 0.9rem 0; background: #fffdf9; display: block; text-decoration: none; color: inherit;
  }
  .chapter-card:hover { border-color: #6b8e9c; }
  .chapter-card .num { color: #6b8e9c; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.06em; }
  .chapter-card h3 { margin: 0.2rem 0 0.3rem; font-size: 1.1rem; }
  .chapter-card p { margin: 0; color: #575046; font-size: 0.95rem; }
  .hero { padding: 1rem 0 0.5rem; }
  .hero h1 { margin-top: 0.5rem; font-size: 2.3rem; }
  .lead { font-size: 1.1rem; }
  @media (prefers-color-scheme: dark) {
    body { background: #1c1b19; color: #e6e2da; }
    h2 { border-bottom-color: #3a372f; }
    .code-inline, blockquote { background: #262420; }
    blockquote { border-left-color: #6b8e9c; }
    hr { border-top-color: #3a372f; }
    .chapter-card, pre { background: #242220; border-color: #3a372f; }
    .chapter-card { color: #e6e2da; }
    .chapter-card p { color: #b6b0a6; }
    a { color: #9cc3d8; }
    footer.pagenav { border-top-color: #3a372f; }
    .meta { color: #8f887c; }
  }
</style>
</head>
<body>
<header class="site">
  <div class="wrap">
    <a href="index.html">Learn to Code with AI</a>
    <div class="tagline">Variables, loops &amp; functions — for absolute beginners, with AI as a patient tutor</div>
  </div>
</header>
<main class="wrap">
{{BODY}}
<footer class="pagenav">
  <div>{{PREV}}</div>
  <div>{{NEXT}}</div>
</footer>
</main>
<footer class="wrap">
  <div class="meta">Generated from <code>docs/</code> by <code>build.py</code> ·
  <a href="https://dylanasdale.github.io">Asdale Dynamics, LLC</a> · MIT License</div>
</footer>
</body>
</html>
"""


def page(title, body, prev_html="", next_html=""):
    text = TEMPLATE.replace("{{TITLE}}", html.escape(title, quote=True))
    text = text.replace("{{BODY}}", body)
    text = text.replace("{{PREV}}", prev_html)
    text = text.replace("{{NEXT}}", next_html)
    return text


def slug_of_entry(entry):
    return entry[:-3]  # strip .md


CHAPTER_TAGS = {
    "00-welcome.md": "Start here", "01-browser-basics.md": "Setup", "02-variables.md": "Core idea",
    "03-loops.md": "Core idea", "04-functions.md": "Core idea", "05-ai-as-tutor.md": "Working with AI",
    "06-when-code-breaks.md": "Troubleshooting", "07-next-steps.md": "Where next",
}

CHAPTER_BLURBS = {
    "00-welcome.md": "How this guide works, why understanding beats copy-paste, and the one habit to start today.",
    "01-browser-basics.md": "Open the console and print Hello, world — your first program in any browser, no installs.",
    "02-variables.md": "Labeled boxes for strings, numbers, and booleans. let, const, and what = really means.",
    "03-loops.md": "for and while loops, counting, and why the computer's superpower is not getting bored.",
    "04-functions.md": "Named recipes: parameters, return values, and why defining is not calling.",
    "05-ai-as-tutor.md": "Prompt recipes that make the AI teach you — hints, quizzes, and error translations.",
    "06-when-code-breaks.md": "Reading errors calmly, the four most common messages, and console.log as a flashlight.",
    "07-next-steps.md": "Arrays, objects, first tiny projects, and free resources for the road ahead.",
}


def build_index(chapters):
    cards = []
    for fname in CHAPTER_ORDER:
        md = chapters[fname]
        title = chapter_title(md)
        num, _, _ = fname[:-3].partition("-")
        cards.append(
            '<a class="chapter-card" href="%s.html">'
            '<div class="num">%s · %s</div>'
            "<h3>%s</h3>"
            "<p>%s</p></a>" % (
                html.escape(slug_of_entry(fname), quote=True),
                html.escape(num, quote=True), html.escape(CHAPTER_TAGS[fname]),
                esc(title),
                esc(CHAPTER_BLURBS[fname]),
            )
        )

    body = """
<section class="hero">
  <h1>Learn to Code with AI</h1>
  <p class="lead">A free first coding manual for absolute beginners. Three ideas —
  <strong>variables</strong>, <strong>loops</strong>, and <strong>functions</strong> —
  learned through tiny exercises with an AI in the tutor's seat. Everything runs in
  the browser. No installs, no paid tools, no prior experience.</p>
</section>
<blockquote><p>The one rule: <strong>never keep a line of code you can't explain out
loud.</strong> Understanding over copy-paste.</p></blockquote>
%s
""" % "\n".join(cards)

    return page("Home", body, "", "")


def main():
    chapters = {}
    for fname in CHAPTER_ORDER:
        path = DOCS / fname
        md = path.read_text(encoding="utf-8")
        chapters[fname] = md

    SITE.mkdir(exist_ok=True)
    for idx, fname in enumerate(CHAPTER_ORDER):
        md = chapters[fname]
        body = markdown_to_html(md)
        slug = slug_of_entry(fname)

        prev_html = ""
        next_html = ""
        if idx > 0:
            prev_slug = slug_of_entry(CHAPTER_ORDER[idx - 1])
            prev_title = chapter_title(chapters[CHAPTER_ORDER[idx - 1]])
            prev_html = '&larr; <a href="%s.html">%s</a>' % (prev_slug, esc(prev_title))
        if idx < len(CHAPTER_ORDER) - 1:
            next_slug = slug_of_entry(CHAPTER_ORDER[idx + 1])
            next_title = chapter_title(chapters[CHAPTER_ORDER[idx + 1]])
            next_html = '<a href="%s.html">%s</a> &rarr;' % (next_slug, esc(next_title))

        (SITE / ("%s.html" % slug)).write_text(
            page(chapter_title(md), body, prev_html, next_html), encoding="utf-8"
        )

    (SITE / "index.html").write_text(build_index(chapters), encoding="utf-8")

    pages = sorted(p.name for p in SITE.glob("*.html"))
    print("Built %d pages:" % len(pages))
    for name in pages:
        print("  site/%s" % name)


if __name__ == "__main__":
    main()
