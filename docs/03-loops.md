# Chapter 03: Loops — Teaching the Computer to Repeat

Computers have exactly one superpower: doing the same small step over and
over, insanely fast, without getting bored. A **loop** is how you borrow that
superpower.

If you found yourself copy-pasting `console.log("line")` three times in a row
in Chapter 01, you already felt the problem a loop solves. Whenever you're
about to repeat yourself, a loop usually exists to say "do that N times" once.

## The for loop: repeat a known number of times

Type this in the console:

```js
for (let i = 1; i <= 5; i++) {
  console.log(i)
}
```

This prints `1` through `5`, one per line. The ingredients on the first line
are worth naming, because every `for` loop you'll ever write has them:

1. `let i = 1` — the **start**: make a counter box `i`, begin at 1.
2. `i <= 5` — the **keep-going test**: as long as this is true, keep looping.
3. `i++` — the **step**: after each pass, make `i` one bigger.
4. `{ ... }` — the **body**: the thing to do each pass.

The curly braces `{ }` are the loop's hands, wrapping around everything it
should repeat.

A very common beginner mix-up: writing `i` inside the body but not realizing
`i` *changes each pass*. Watch:

```js
for (let i = 1; i <= 3; i++) {
  console.log(`Pass number ${i}`)
}
```

Prints three lines with `1`, `2`, `3` inside. The body runs three separate
times, and `i` has a slightly different value each time.

## Loops over "things you can count"

Counting 1-to-5 is cute, but loops shine when the count comes from real life.
Eleven dishes to wash? A loop. 30 charts to review, one at a time? A loop.
(A loop would wash them, if dishes could be washed by code.)

```js
const daysUntilDayOff = 4
for (let day = 1; day <= daysUntilDayOff; day++) {
  console.log(`Day ${day}: still going.`)
}
console.log("Day off!")
```

Notice the "Day off!" line is *outside* the braces, so it runs once, after the
loop finishes. That in-and-out of the braces is a real skill — watch where
lines live and why.

## The while loop: repeat until something happens

A `for` loop is best when you know how many repetitions you want. A **while**
loop is better when you only know a *condition*:

```js
let cups = 0
while (cups < 2) {
  cups = cups + 1
  console.log(`Cup of coffee number ${cups} made.`)
}
console.log("Okay, now I can start the day.")
```

Read it in plain English: "while it's not yet 2 cups, keep making cups." The
variable `cups` *changes inside the loop*, which is what eventually makes the
condition false and lets you out.

## Infinite loops: the one scary thing, now disarmed

A `while` loop whose condition never becomes false runs forever. In a browser
console this just makes the tab sluggish, and you can close the tab. That's
the whole disaster possible here — annoying, not dangerous.

How to avoid it: make sure *something inside the loop moves toward making the
condition false*. In the coffee example, if you forgot `cups = cups + 1`, the
loop would never end: `cups` would stay 0, `0 < 2` stays true, forever.

A free trick: a loop that prints as it goes shows you immediately whether it
is making progress. Printing as you loop is like leaving a trail of breadcrumbs.

## Loop vocabulary in one glance

- **iterate** — to go around once. "The loop iterated five times."
- **counter** — the variable that counts the passes (`i` above).
- **off-by-one** — the classic mistake of looping one time too many or too
  few (`i <= 5` vs `i < 5`). Everyone makes this. Yours will not be special,
  and the fix is usually obvious once you print the values.

## Exercises

### Exercise 3.1 — countdown

Write a loop that prints 5, 4, 3, 2, 1, "Liftoff!". Hint: your start and step
can both change.

### Exercise 3.2 — every other number

Print the even numbers from 2 to 10. (Start at 2 and step how much?)

### Exercise 3.3 — the sum

Using a loop and a `let total = 0` box, add up the numbers 1 to 10 and print
the total at the end. If you're stumped: "total = total + i" is a pattern you
saw in Chapter 02, and the loop makes you get to do it ten times.

### Exercise 3.4 — a deliberate bug

Type this, watch it go bad, then fix it:

```js
let cups = 0
while (cups < 3) {
  console.log("Making cup of coffee.")
}
```

What's missing? (This is the infinite loop from this chapter, in miniature.
Notice how the printed lines repeat identically — no progress.)

## Try asking your AI

- "Explain the three parts of a for loop header — start, condition, step —
  using a treadmill metaphor."
- "Quiz me on loops: invent a for loop with a deliberate mistake (off-by-one
  or a missing step) and ask me to find it. Wait for my answer before telling
  me the bug."
- "I want to print the even numbers 2 to 10. Ask me questions to help me get
  there instead of writing it for me."

## Check yourself

- What are the three parts of a `for` loop header, and what does each do?
- When would you pick `while` over `for`?
- What causes an infinite loop, and how do you escape one in a browser?

Onward to [Chapter 04: Functions](04-functions.md).
