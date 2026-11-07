# Chapter 02: Variables — Teaching the Computer to Remember

A **variable** is a labeled box in the computer's memory. You put something in
it, give the box a name, and from then on you use the name whenever you want
that something.

Without variables a program is like doing math in your head all the way
through. With variables, the program can remember.

## Creating a variable

Type this in the console:

```js
let name = "Sam"
console.log(name)
```

Line one creates a box, labels it `name`, and puts the text `"Sam"` inside.
Line two says "print the *contents* of the box named `name`" — no quotes
around `name` here, because we want the value, not the word.

What's inside can change:

```js
name = "Dana"
console.log(name)
```

Now the same box says `Dana`. The old content is gone. That's why it's called
a *variable* — its value can vary.

## let and const

JavaScript has two everyday keywords for making boxes:

- `let` — a box you're allowed to replace later ("let it change").
- `const` — short for *constant*: a box that never changes. Try to replace it
  and you'll get an error.

```js
let score = 0
score = 10
console.log(score)

const daysInWeek = 7
console.log(daysInWeek)
```

Now try this — and read the error carefully when it comes:

```js
daysInWeek = 8
```

You'll see something like `TypeError: Assignment to constant variable.` This
is not the computer being mean. It's the computer saying: "You promised that
box would never change, and you tried to change it." Errors are information —
Chapter 06 is all about reading them kindly.

Rule of thumb: **use `const` by default**, and switch to `let` when you know
you'll replace the value. It documents your intentions for free.

## The kinds of things a box can hold (data types)

Three types cover almost everything a beginner needs:

**String** — text, always in quotes:

```js
const greeting = "Good morning"
```

**Number** — no quotes, works with math:

```js
const price = 4.5
```

**Boolean** — only `true` or `false`. This is a box holding a yes/no answer:

```js
const isRaining = false
```

How can you check what type is in a box? There's a built-in helper:

```js
console.log(typeof greeting)
console.log(typeof price)
console.log(typeof isRaining)
```

## Combining strings: template literals

You'll constantly want to build one sentence out of pieces. The clean way
uses backticks (`` ` `` — the key above Tab) with `${...}` to drop variables
into text:

```js
const name = "Dana"
const cupsOfCoffee = 2
console.log(`${name} has had ${cupsOfCoffee} cups of coffee today.`)
```

This prints `Dana has had 2 cups of coffee today.` Weeks from now, when you're
building bigger things, you'll reach for this pattern every few minutes.

## Naming: boxes have names for humans, not computers

The computer doesn't care if your variable is called `x` or
`cupsOfCoffeeToday`. But *you* — in ten minutes — definitely care. Names should
say what's inside.

- Good: `userName`, `totalPrice`, `isNurse`
- Not good: `x`, `thing1`, `stuff`

The letter case convention in JavaScript is called **camelCase**: first word
lowercase, later words capitalized, no spaces. `totalPrice`, not
`total price`, `TotalPrice`, or `total_price`.

## = is assignment, not equals

One mental shift to make early: a single `=` does not mean "these are equal."
It means "take the value on the right, and put it in the box on the left."

```js
let total = 5
total = total + 2
```

Line two looks like nonsense in math class, but in code it's perfectly
sensible: "make `total` be its old value plus 2." Read `=` as **"becomes"**
and a lot of early confusion evaporates. `total` is now `7`.

## Exercises — tiny, on purpose

### Exercise 2.1 — introduce yourself

Make three variables and print one sentence using template literals:

- a string with your first name
- a number for how many years you've been at your current job (an estimate is fine)
- a boolean for whether you drank coffee today

Print: "Hi, I'm NAME, I've been at my job NUMBER years, and COFFEE mentions coffee."

Hint: booleans print as `true` or `false` — that's fine for now; making it
print "yes/no" is a question for your AI tutor.

### Exercise 2.2 — the running total

Make a `const` for a starting amount (say, `0`) — wait, you can't, you'll be
changing it. Make it a `let`. Add 3 to it, then add 12.25 to it, then print
the total. Then make a second line that prints how much it would be with a 2
dollar tip.

### Exercise 2.3 — predict, then run

```js
const a = "5"
console.log(a + 1)
```

Before running: does that print `6` or `51`? Why? If the answer surprises you,
ask your AI: "Why does "5" + 1 give 51? What is type coercion, explained to a
beginner?" Surprises are your syllabus.

## Try asking your AI

- "What's the difference between let and const in JavaScript? Explain it with
  a metaphor, then quiz me with two questions."
- "Give me one tiny variable exercise where the mistake happens *before*
  running — a naming or type problem I have to spot by reading."
- "Here's a line of my code: `total = total + 2`. Explain why the computer
  doesn't get confused doing that."

## Check yourself

You're ready for Chapter 03 when you can answer:

- What's the difference between `let` and `const`?
- What are the three data types from this chapter, and how do you write each?
- What does `=` actually do?
- Why does `"5" + 1` not give `6`?

Onward to [Chapter 03: Loops](03-loops.md).
