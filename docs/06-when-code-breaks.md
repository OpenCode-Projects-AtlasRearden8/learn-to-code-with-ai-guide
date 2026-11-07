# Chapter 06: When Code Breaks

Let's set expectations honestly: your code will break. Often. Several times
per hour on real projects. If you expected broken code to mean you're failing
at this — breathe. Broken code is not the deviation from programming;
broken code *is* programming. The skill you build across a career isn't
"writing code that never breaks." It's **getting calm and getting curious**.

Professionals who seem relaxed about errors aren't brave — they've just
debugged enough to know errors are almost always small and local. That calm
is learnable, and this chapter is the manual.

## The mindset: errors are information, not judgment

Read the two ways of receiving an error:

- "I got an error. I'm bad at this."
- "I got an error. The computer is telling me something. Let's read it."

The second one is rote-learnable. An error message is the computer doing
something genuinely kind: it stops, it points at the problem, and it names it.
No human teacher interrupting you constantly, tagging the exact sentence you
got wrong, would be this efficient. Errors are the fastest feedback loop
you'll ever get. Beginners run from errors; experienced people run *toward*
them, because an error means you're seconds from progress.

## Anatomy of an error message

Here's a real one:

```text
Uncaught TypeError: Assignment to constant variable.
```

Parse it in three parts:

1. **Type** — `TypeError` (what *kind* of problem)
2. **Message** — "Assignment to constant variable." (what happened)
3. **Location** — browsers also show the file and line, like `chapter.js:12`

Half of debugging is just reading all three instead of panicking at the first
scary word. You will not understand every word at first. Read what you can,
and paste the rest into the AI with "explain this error to me."

## The four errors you'll see most

You can fix a startling percentage of beginner errors with just these four.

### 1. `SyntaxError: ...` — you mistyped something

> `SyntaxError: missing ) after argument list`
> `SyntaxError: Unexpected end of input`

Meaning: the sentence of code is malformed — the computer can't even *read*
it, so it never ran. Look for: missing or swapped brackets/parens/quotes, a
word typed wrong. Check line numbers near the reported line.

Quick self-check: every `(` a `)`? Every `{` a `}`? Every unclosed quote
closed? Unbalanced braces are the classic cause of "Unexpected end of input."

### 2. `ReferenceError: X is not defined` — spelling or timing

```js
cosole.log("Hi")
```

> `Uncaught ReferenceError: cosole is not defined`

Meaning: the name doesn't exist. 90% of the time, for beginners, it's a typo
(`cosole` vs `console`). The rest is using a variable before you made it, or
in a place it doesn't exist. Fix is usually one keystroke — which is also why
guessing randomly at a fix rarely works: you must spot the misspelled name,
not shuffle code.

### 3. `TypeError: X is not a function` / similar — wrong kind of thing

```js
const name = "Sam"
name()
```

> `Uncaught TypeError: name is not a function`

Meaning: you asked a value to do a job it can't do. A string can't be called
like a function; a constant can't be reassigned. The fix: check what's really
inside the box (`typeof` from Chapter 02 helps).

### 4. Logic error — code runs fine, and is wrong

The sneakiest. No error at all. The loop loops, the function returns — and
the answer is wrong, because a `<=` should be `<`, or the loop starts at 1
instead of 0. The computer did exactly what you said. You said something
slightly different from what you meant.

There's no error message to read for logic errors. The treatment is a tool,
and here is the tool:

## The debugger's best friend: console.log everywhere

`console.log` is a flashlight. When behavior surprises you, shine light on
each stage:

```js
function sumTo(n) {
  let total = 0
  for (let i = 1; i <= n; i++) {
    console.log(`pass ${i}: total was ${total}`)
    total = total + i
    console.log(`pass ${i}: total is now ${total}`)
  }
  return total
}

sumTo(4)
```

Watch the values. You will almost always spot the moment the values stop
being what you assumed. Programming is full of invisible states; logging
renders them visible. This habit alone fixes a large share of logic bugs:
you are running the same code while actually *looking* at what it is doing.

When the flashlights have found the general neighborhood, then invoke the AI.

## Case study 1: the typo

You run: `console.log("Hello")` — wait, you typed `cosole.log("Hello")`, and
got `ReferenceError: cosole is not defined`.

Asked your AI: "what does 'is not defined' usually mean for a beginner?" It
says: "usually a typo — check the spelling of the name." You compare letter
by letter. `cosole`. Fix: `console`. Sixty seconds if you stayed calm. If you
had flailed ("maybe I need a semicolon? let me move things around?"), you
could have spent ten minutes and learned less.

## Case study 2: the missing brace

You write:

```js
if (isRaining) {
  console.log("Bring an umbrella")
```

and get `SyntaxError: Unexpected end of input`.

Plain-English translation: "I ran out of code, and something was still open."
You look at your braces — they're unbalanced. Fix: add the closing `}`. Asking
the AI to explain the message, then *finding it yourself*, teaches you the
message — next time you won't need the AI for this one.

## Case study 3: the off-by-one

You write a loop to print 1 to 5:

```js
for (let i = 1; i < 5; i++) {
  console.log(i)
}
```

It prints `1 2 3 4`. No error. Wrong result. Can't read an error — so you add
a log: `console.log(\`i is ${i}, and 5 is the goal\`)` and watch. You see the
loop stops while the condition `i < 5` is still true at `i = 4`. Aha moment: you
need `i <= 5`. The bug was one character. Logic bugs are one
character with big opinions.

## The AI debugging conversation, done right

When you hit the AI, don't say "it doesn't work, fix it." That's
answer-machine mode (Chapter 05). The magic sentence:

> Here's my code. Here's what I expected. Here's what I got instead. Ask me
> questions to help me find the problem myself.

This does two things. First, composing those three sentences ("expected X, got
Y") is itself half the debugging solve — clear articulation catches bugs by
itself more often than you'd expect. Second, it keeps you the one building
the skill.

And when the AI finds it, ask the follow-up: "How could I have spotted that
myself?" The answer is usually a tool you get to keep.

## When you're frustrated: the permission slip

A real thing that helps, from one human evaluator to another:

Coding frustration is real, and it isn't weakness — it's your brain saying
"This has been hard for X minutes with no progress." The move is not more
pushing. The move:

1. **Two minutes of logging/predicting** (flashlights, above).
2. If still stuck, ask the AI for **one hint**, not a solution.
3. If still stuck: stop the session. Write in your learning log what you were
   trying and where it broke. Return tomorrow.

Real phenomenon: solutions that wouldn't come are *waiting* for you the next
morning. Sleep does processing we can't order on demand. Stopping is a
strategy — not giving up, deferring to a smarter version of you.

## Choose-your-own-debug checklist

When something breaks, in order:

1. Breathe. This is normal. (Really — this is a step; panic closes your eyes.)
2. Read the full error, all parts: type, message, location.
3. Re-read your own code near the reported line, out loud if you can.
4. `console.log` the values on each side of the break.
5. The AI: "explain this error to me" or "here's what I expected / got; ask
   me questions."
6. Ask: "How could I have caught this myself?"

Now with calm under your feet, go see the wide open country ahead:
[Chapter 07: Next Steps](07-next-steps.md).
