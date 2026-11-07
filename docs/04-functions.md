# Chapter 04: Functions — Teaching the Computer a New Trick

A **function** is a named recipe: a set of steps you write once, give a name,
and ask for by name whenever you need it. You've already been *using* them —
`console.log` is a function someone else wrote. This chapter you write your
own.

## Your first function

Type this in the console:

```js
function greet() {
  console.log("Hello there!")
}

greet()
greet()
```

Three things happened:

1. `function greet() { ... }` **defines** the recipe, but runs *nothing*.
   The computer just takes notes: "if anyone says `greet()`, here's the plan."
2. The lines inside the braces are the **body** — the steps of the recipe.
3. `greet()` **calls** the recipe. Each call runs the whole body. Call it
   twice, it runs twice.

Defining and calling are different events. This is the single biggest "wait,
what?" moment for beginners: writing the function does nothing visible;
*calling* it does the work. If your function seems to "not work," first
question: **did I call it?**

## Parameters: recipes with blanks to fill

`greet()` says the same thing every time. A **parameter** lets the recipe
have slots that the caller fills in:

```js
function greetPerson(name) {
  console.log(`Hello, ${name}!`)
}

greetPerson("Sam")
greetPerson("Dana")
```

Here `name` is a parameter — an empty labeled box inside the function. When
you call `greetPerson("Sam")`, the string `"Sam"` goes into that box (it's
called an **argument**, the value you pass in).

Functions can take more than one parameter, with commas:

```js
function introduce(name, job) {
  console.log(`${name} works as a ${job}.`)
}

introduce("Dana", "RN")
```

Order matters: the first argument goes into the first parameter, second into
second, like filling a form left to right.

## return: recipes that hand something back

So far our functions only *do* things (print). But the truly powerful kind
*hands back a value* you can keep using. That's what **return** does:

```js
function add(a, b) {
  return a + b
}

const totalCost = add(3.5, 8.25)
console.log(totalCost)
```

`add(3.5, 8.25)` is an *expression* — it computes to a value — so just like
`2 + 2`, you can store it in a variable, print it, or feed it into another
function.

`console.log` vs `return` confuses almost everyone once, so let's be real
clear:

- `console.log(...)` — show the human something. Nothing is handed back.
- `return ...` — hand the value back to whoever called. Nothing is shown.

A function with `return` is a fountain you can drink from. A function with
only `console.log` is a shower over a cactus: impressive, but nothing to catch.

## Why functions matter more than they seem

Even with this tiny vocabulary, functions buy you three big things:

1. **Reuse.** Write the steps once, call many times. Fix the recipe once, all
   the calls improve.
2. **Names as documentation.** `totalPriceWithTax(cart, taxRate)` reads like
   English. Good names let code explain itself.
3. **Small understandable pieces.** Big programs aren't harder than small
   ones because of some magic — they're just *more pieces you already
   understand*. Functions are how you build big things while only ever
   holding one small thing in your head.

## Building up: a function with a loop inside

Here's where the book's three ideas click together — a function that uses a
loop, taking a parameter:

```js
function countTo(n) {
  for (let i = 1; i <= n; i++) {
    console.log(i)
  }
}

countTo(3)
countTo(5)
```

The function is the recipe "print numbers 1 through n." The loop is one of
its steps. The parameter decides how far. Every real program you'll ever read
is layers of this: variables feeding loops inside functions.

## Exercises

### Exercise 4.1 — greet three people

Write `greetPerson(name)` and call it with three different names.

### Exercise 4.2 — double it

Write `double(number)` which **returns** the number times two. Call it and
store the result in a variable, then print that. Test it with 4 and with 0.

### Exercise 4.3 — is short name?

Write `isShortName(name)` that **returns** `true` if the name has 4 or fewer
letters and `false` otherwise. Hint from Chapter 02: strings have a `length`:
`"Sam".length` is `3`. Then call it with `"Sam"` and `"Dana"` and print the
results.

### Exercise 4.4 — a sinking feeling (finding the classic bug)

What's wrong with this? Predict, run, fix:

```js
function triple(x) {
  console.log(x * 3)
}

const nine = triple(3)
console.log(nine)
```

`nine` prints `undefined`. Because `triple` *returned nothing* — it showed the
answer on screen but never handed a value back. This is the #1 beginner
function bug. The fix is one word: change `console.log(x * 3)` to
`return x * 3` (and print the *caller's* side instead).

## Try asking your AI

- "Explain the difference between a parameter and an argument using a form
  and a filled-in form metaphor."
- "Give me three tiny function exercises in increasing difficulty, but don't
  show me the solutions until I've typed my attempt."
- "Here is a function I wrote. It prints the answer but the variable it was
  assigned to is undefined. Guide me to see why — ask me questions instead of
  telling me."

## Check yourself

- What's the difference between *defining* a function and *calling* one?
- What's the difference between a parameter and an argument?
- What does `return` do that `console.log` doesn't?

Now the two "glue" chapters that travel with you long after syntax:
[Chapter 05: Using AI as a Tutor](05-ai-as-tutor.md).
