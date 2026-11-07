# Chapter 07: Next Steps — What You Can Do From Here

Pause and take stock of what you can now do: create variables of every basic
type, loop a known or unknown number of times, write functions that take
input and hand back output, use AI as a tutor, and debug calmly with errors
and `console.log`.

That is not "the beginning of coding." That is the core of coding. Everything
else — including professional work — is combinations and extensions of what's
in your head now. Here's the honest map of what comes next, all free.

## Step 1: solidify with slightly bigger data

Your next tiny step is learning to store *several* values together:

```js
const groceries = ["eggs", "coffee", "oranges"]
console.log(groceries[0])
console.log(groceries.length)
```

An **array** is a numbered row of boxes, and you can loop over it — which is
the moment loops become truly everyday-useful. An **object** is a labeled
bunch of related boxes:

```js
const recipe = { name: "Pancakes", minutes: 25, servings: 4 }
console.log(`To make ${recipe.name} for ${recipe.servings} takes ${recipe.minutes} minutes.`)
```

You already possess every tool to make sense of these: they're still variables
(boxes), an array is just a row of them, and `[0]` and `.length` are simply
new built-in abilities of those boxes.

## Step 2: meet the page itself

So far your code has only talked to the console. Browsers also give you the
*page* your code lives in. This is called the DOM, and the practical first
version is: make a button, and make clicking it run your function.

```js
function makeButton() {
  const button = document.createElement("button")
  button.textContent = "Roll a die"
  button.addEventListener("click", () => {
    console.log(`You rolled a ${Math.ceil(Math.random() * 6)}`)
  })
  document.body.append(button)
}

makeButton()
```

Paste that into your browser console on any empty tab and watch a real button
appear — your own function, wired to a real event on a real page. That's not
"beginner stuff." It's the same doorway professional web developers use,
only smaller.

## Step 3: three free next-step resources

When you want structured continuation, these are all free and all good. Pick
the one whose vibe fits you, not the one that is "best":

- **MDN Web Docs** (developer.mozilla.org) — the reference for looking up
  what something does, patient and plain-English.
- **freeCodeCamp** (freecodecamp.org) — interactive exercises with instant
  feedback, entirely free.
- **The Odin Project** (theodinproject.com) — a full free curriculum from
  beginner to building real projects, with a friendly community.

## Step 4: your first tiny real projects

Nothing cements learning like building something *yours* — even if it's tiny
and ugly. Classic first projects, roughly in order of difficulty:

1. **Dice roller** — a button that rolls 1–6 (you've seen the core already)
2. **Unit converter** — type a number, see it converted (ml to oz, for example)
3. **Tip calculator** — inputs: bill and tip percent; output: total
4. **Tiny to-do list** — add items to an array, loop to display them
5. **Chess match tracker** — record wins/losses/draws with an object and a loop
6. **FFXIV loot counter** — enter dungeon runs, track gear drops until it
   drops the item you want

Build each *with the AI in tutor mode*, using prompts like:

> I want to build a tip calculator from scratch in the browser console. Guide
> me with hints, not code. Start by asking me what pieces the program needs.

Expect your first projects to take longer than you think — and to be roughly
ten times more satisfying than any tutorial.

## Step 5: version control (your future safety net)

After a few projects, you'll have broken-and-fixed enough code to appreciate
a time machine. That's **Git** — saving snapshots of your files so you can go
back to any earlier one. **GitHub** is the free website where those snapshots
can live, so they're safe even if your computer isn't. This guide doesn't
teach Git — that's a separate adventure — but files-as-snapshots is a habit
worth picking up early: even just saving dated copies of your project files
(`dice-roller-v1.js`, `dice-roller-v2.js`) builds the instinct.

## Step 6: keep the tutor habit

Whatever comes next, the habit pays for itself: use the AI for *explanations,
hints, quizzes, and error translations* — and keep the copy-paste checklist
from Chapter 05 standing between you and answer-machine mode. The syntax you
learned here will evolve; the ability to ask good questions and read errors
calmly never expires.

## A last word

Six months from now, you could be someone who opens a browser console to
automate a small chore, who reads an error message without flinching, and who
knows how to ask an AI to teach instead of just answer. None of that requires
talent, money, or a computer science degree. It requires short sessions,
honest questions, and the patience to understand instead of paste.

You've already done several of those in this book. Keep the streak.

---

*Learn to Code with AI — a free guide. If it helped, build something tiny
today.*
