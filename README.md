# Learn to Code with AI

A first coding manual for absolute beginners: **variables, loops, and
functions**, learned through tiny exercises built together with AI as a
patient tutor. Free tools only, browser-first, no installs — and a kind
troubleshooting chapter for when code breaks (because it will, and that's normal).

Written in plain English, step by step, never condescending — for
[Asdale Dynamics, LLC](https://dylanasdale.github.io), the beginner-friendly
AI education publisher of *The Massive AI Manual* by Dylan Asdale.

## Who this is for

Someone who has never written a line of code, has any computer with a browser,
and has access to any free AI chat (ChatGPT, Claude, Gemini, or a local model).
No installs, no paid tools, no prior experience assumed.

## What's inside

| File | Chapter |
|---|---|
| `docs/00-welcome.md` | Welcome: you can learn to code |
| `docs/01-browser-basics.md` | Your free browser workbench (the console) |
| `docs/02-variables.md` | Variables — teaching the computer to remember |
| `docs/03-loops.md` | Loops — teaching the computer to repeat |
| `docs/04-functions.md` | Functions — teaching the computer a new trick |
| `docs/05-ai-as-tutor.md` | Using AI as a tutor (not an answer machine) |
| `docs/06-when-code-breaks.md` | When code breaks — kind troubleshooting |
| `docs/07-next-steps.md` | Next steps: free resources and tiny projects |

The distinction in one line: this guide teaches **coding itself, with AI in the
tutor's seat**. It is not a manual for one specific AI coding tool, and it is
not a general "study with AI" guide — the AI is your tutor for learning
variables, loops, and functions, hands on the keyboard.

## How to use it

1. Open `docs/00-welcome.md` and read on. Every chapter stands alone, in order.
2. Work through chapters with a browser console open in one tab and a free AI
   chat in another.
3. Do the tiny exercises in each chapter. Type them by hand. Understanding
   over copy-paste, always.

## Reading the built site

A static HTML version of the guide lives in `site/`, generated from the
Markdown in `docs/`. Just open `site/index.html` in any browser — no server,
no installs, works offline from a plain file on disk. Style files: everything
is inline in every page to keep it portable.

## Building the site yourself

The static site is regenerated from `docs/` with a small dependency-free
Python script:

```sh
python3 build.py
```

This rebuilds every page in `site/` from its Markdown source and the landing
page (`site/index.html`) from the chapter list.

## Verifying everything works

```sh
./verify.sh
```

runs three checks:

- **build**: regenerates the site with `python3 build.py` and confirms it exits cleanly
- **exercises**: runs `tests/run-solutions.js`, which executes every solution
  in `solutions/` with Node and asserts each exercise's expected results
- **links**: `tests/check_links.py` confirms every internal `.md`/`.html` link
  in `docs/` and `site/` points at a file that exists

Expected output ends with a line like `ALL CHECKS PASSED`. Requires
`python3` (3.8+) and Node.js (v14+), both free.

## Repository layout

```sh
docs/          the guide, chapter by chapter, in Markdown (source of truth)
site/          the same guide, generated: pages each link to every other page
solutions/     runnable JavaScript solutions to each chapter's exercises
build.py       dependency-free Markdown-to-HTML static site generator
verify.sh      build + exercise tests + link check, in one command
tests/         the verification scripts mentioned above
```

## Design values

- **Free tools only.** Everything, including the browser console, is free.
- **Browser-first, no installs.** The reader needs a browser; the builder
  needs only the stock Python and Node both of us already have.
- **Understanding over copy-paste.** Every chapter includes reflection
  questions and AI-tutor prompts designed to keep learning on the reader's
  side of the table.
- **Kind troubleshooting.** Errors are treated as information, not judgment,
  and the "when code breaks" chapter is written to keep a nervous beginner calm.
- **Local-first, no secrets.** No accounts, no API keys, no network calls,
  no personal data anywhere in this project.

## License

MIT — see [LICENSE](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC
