# STATUS — Learn to Code with AI

Last updated: 2026-11-07

## What was built

A complete first coding manual for absolute beginners — "Learn to Code with
AI" — aimed at variables, loops, and functions, built around the idea of AI as
a patient tutor rather than an answer machine. Free tools only; the reader
needs nothing but a browser tab.

- **`docs/`** — the guide itself, 8 Markdown chapters:
  - `00-welcome.md` — how the guide works, the "understanding over
    copy-paste" rule, learning-log habit
  - `01-browser-basics.md` — opening the browser console, first `console.log`,
    free alternatives (CodePen/JSFiddle/OneCompiler), early safety habits
  - `02-variables.md` — let/const, strings/numbers/booleans, template
    literals, what `=` really means
  - `03-loops.md` — for/while anatomy, counting, infinite loops disarmed
  - `04-functions.md` — parameters, arguments, `return` vs `console.log`,
    the classic `undefined` bug
  - `05-ai-as-tutor.md` — copy-pasteable prompt recipes (hints not answers,
    quizzes, explain-it-back) plus a copy-paste checklist
  - `06-when-code-breaks.md` — kind troubleshooting: error anatomy, the four
    most common errors, three case studies, debugging checklist, and a
    frustration permission slip
  - `07-next-steps.md` — arrays/objects preview, DOM button, free resources
    (MDN, freeCodeCamp, The Odin Project), six tiny first projects
- **`site/`** — the same guide as a static HTML site (9 pages: landing page
  with chapter cards + 8 chapter pages), warm styling, light/dark support,
  prev/next chapter navigation. Opens straight from disk in any browser — no
  server, no JS, no network needed.
- **`build.py`** — dependency-free (stdlib-only) Markdown-to-HTML static site
  generator that produces `site/` from `docs/`.
- **`solutions/`** — runnable JavaScript solutions for each chapter's
  exercises, each file self-checking with explicit pass/fail assertions.
- **`tests/`** — `run-solutions.js` (runs every solution under Node and
  asserts results) and `check_links.py` (verifies every internal link in
  `docs/` and `site/` resolves).
- **`verify.sh`** — one command that rebuilds the site, runs all exercise
  solutions, and checks all links.
- **`LICENSE`** — MIT, `Copyright (c) 2026 Asdale Dynamics, LLC`.
- **`README.md`** — project overview, run/verify instructions, credited to
  Asdale Dynamics, LLC.

Distinct positioning: this teaches coding itself (variables, loops,
functions) with AI in the tutor's seat — not a manual for a specific AI
coding tool, and not a general study-with-AI guide.

## How to run it

- **Read the site**: open `site/index.html` in any browser. Works offline
  from the file on disk.
- **Rebuild the site** (needs Python 3 only, stdlib): `python3 build.py`
- **Verify everything** (needs Python 3 and Node.js): `./verify.sh`
- **Run one chapter's solution**: `node solutions/02-variables.js`
- **Read as plain Markdown**: start at `docs/00-welcome.md`.

## Verification results

`./verify.sh` — all three stages pass:

```
=== 1/3: build the static site ===
Built 9 pages
=== 2/3: run the chapter exercise solutions ===
PASS solutions/01-browser.js
PASS solutions/02-variables.js
PASS solutions/03-loops.js
PASS solutions/04-functions.js
ALL EXERCISE SOLUTIONS PASSED
=== 3/3: check internal links in docs/ and site/ ===
ALL LINKS OK
ALL CHECKS PASSED
```

Notes on what the checks actually cover:

- The site build is verified by running it (it regenerated all 9 pages
  cleanly from source).
- The four solution files each verify the chapter's exercises with explicit
  assertions (types, computed values, loop output order, return-value
  behavior, including the `TypeError` on reassigning `const` and the
  `"5" + 1` coercion surprise) — exercised under Node v20.
- The link checker walks `href`/`src` attributes in `site/*.html` and
  Markdown link syntax in `docs/*.md`, confirming each internal target
  exists (this caught and fixed 7 stale `.md` links in the generated HTML
  during development).

## Known gaps

- No JavaScript syntax highlighting in code blocks (static generator keeps
  it dependency-free; blocks are copyable as-is).
- `build.py`'s Markdown converter covers the constructs this guide uses
  (headings, paragraphs, lists, fenced code, blockquotes, hr, inline
  emphasis/code/links) — not a general-purpose GFM renderer, so tables,
  images, and nesting aren't supported.
- Chapter links from chapter pages to a rendered LICENSE page don't exist;
  license is linked from the footer text and from the README only.
- Solutions cover chapters 01–04 (variables/loops/functions are the core
  scope); chapters 05–07 are prompts/resources rather than exercise sets.
