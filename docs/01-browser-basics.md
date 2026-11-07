# Chapter 01: Your Free Browser Workbench

You don't need to install anything. Every browser — Chrome, Firefox, Edge,
Safari — already contains a place where you can type and run code. It's called
the **console**, and it's where this whole guide takes place.

## Opening the console

1. Open your browser.
2. Open any web page (a blank "New Tab" page is fine).
3. Press **F12** (or right-click anywhere and choose **Inspect**, or press
   **Cmd+Option+I** on a Mac).
4. Find the **Console** tab and click it.

You'll see a blinking cursor after a `>` symbol. That's your prompt. The
console is asking: "What should I run?"

A word of reassurance: you cannot break the internet from here. The console
only affects the page you have open, and refreshing the page wipes anything
you typed. It's a whiteboard, not a bomb.

## Your first line of code

Type exactly this and press Enter:

```js
console.log("Hello, world!")
```

You should see `Hello, world!` printed back at you. Congratulations — despite
its size, that line is genuinely a program. It told the computer to *do*
something, and the computer did it.

Some things to notice:

- `console.log` is a **function** the browser gives you. You'll learn to write
  your own functions in Chapter 04. For now, treat it as "print this out".
- The **quotation marks** make `"Hello, world!"` a piece of *text* (called a
  string). Text goes in quotes so the computer knows it isn't code.
- The **parentheses** hold what you want printed. They're the "input slot" of
  a function.

Try a few more:

```js
console.log("My name is Sam")
console.log(2 + 2)
console.log("2 + 2")
```

See the difference? `2 + 2` prints `4` — no quotes means *do the math*.
`"2 + 2"` with quotes prints the text `2 + 2` — quotes means *say this
literally*. That distinction (do it vs. say it) is the seed of everything that
follows.

## The console as a calculator (and a playground)

Try these, one per line, and predict each answer *before* pressing Enter:

```js
console.log(10 * 3)
console.log(7 - 2)
console.log(10 / 4)
console.log(3 > 2)
```

The last one prints `true`. That's not a typo or a string — it's a *boolean*,
a value that means yes/no. You'll meet those properly in Chapter 02.

Making predictions first matters. Your brain learns from the moment of
"ah, I was almost right" far more than from reading an answer.

## Free alternatives (still no installs)

The console is great, but a couple of free websites give you a bigger workspace
where multiple lines of code live permanently:

- **CodePen** (codepen.io) — the HTML/CSS/JS editor box; JavaScript goes in the
  JS panel.
- **JSFiddle** (jsfiddle.net) — same idea.
- **OneCompiler** or similar free online JavaScript runners — plain code, big
  output area.

These are all free, need only a browser, and need no account to start.

## Safety habits, early

Three habits worth building from day one:

1. **Don't paste code into the console if you don't know what it does.** Some
   scams ask people to paste code that logs them out of or into accounts on
   the current page. If you can't explain a line, ask your AI what it does
   first. This habit is also the #1 learning habit anyway.
2. **Console experiments live on the current page.** Refresh and they're gone.
   When you build something you want to keep, save it as a `.js` text file
   using any plain-text editor, or keep it in a free editor site you're signed
   into.
3. **Free tools are enough for everything in this book.** You should never
   reach for your credit card to follow along.

## Exercise 1.1 — say hello, three ways

In the console, one line each:

1. Print a greeting to yourself by name.
2. Print the result of `25 + 75`.
3. Print the text `"25 + 75"` (with quotes). Notice how it differs.

## Exercise 1.2 — predict, then run

For each line below, write down your prediction, then run it:

```js
console.log(8 - 3)
console.log("8 - 3")
console.log(3 + 3 * 2)
console.log((3 + 3) * 2)
```

If any prediction surprised you, that's gold — put it in your learning log.

## Try asking your AI

- "I typed `console.log("Hello")` and nothing happened. What are the most
  common reasons a beginner's first console line fails? Ask me questions
  instead of giving me the whole answer."
- "Give me three console.log exercises for a day-one beginner, ranked from
  easiest to hardest. Check my answers when I type them."
- "What does the word 'string' mean in JavaScript? Explain it in one sentence
  and then give me one example."

## Check yourself

You're ready for Chapter 02 when you can answer:

- How do I open the console?
- Why does `2 + 2` and `"2 + 2"` in the console act differently?
- Why should I never paste code I don't understand?

Go to [Chapter 02: Variables](02-variables.md) when you're ready.
