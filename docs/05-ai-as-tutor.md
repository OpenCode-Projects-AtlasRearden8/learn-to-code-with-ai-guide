# Chapter 05: Using AI as a Tutor (Not an Answer Machine)

Everything so far assumed you have an AI alongside you. This chapter is about
*how* to use it — because the same tool can be a gym that makes you stronger,
or an elevator that takes you nowhere slowly.

Two modes of using AI exist:

- **Answer machine mode**: "write me a program that does X." You paste, it
  runs, you shrug, nothing sticks.
- **Tutor mode**: the AI explains concepts, gives hints, asks *you* questions,
  and checks *your* work. You get stuck, wrestle, and figure it out — which is
  the entire mechanism by which learning happens.

This book asks you to live in tutor mode. Here's the vocabulary to make that
practical.

## The core principle: keep the cognitive load on your side

There is a real phenomenon in learning science: when someone hands you a
finished answer, your brain skims it, feels recognition ("yeah, I get it"),
and moves on. Recognition feels like knowing. It isn't. The feeling of real
learning is *effortful recall* — you reaching into your own head for the step.

So the tutor-level prompts are all designed around one move: **make the AI
give you less, make it ask you more.**

## Prompt recipes that work

Each recipe is copy-pasteable — and unlike code, prompts are safe to paste.
They're habits, though; you're meant to adapt them.

### "Explain like I'm twelve, then check me"

> Explain what a `for` loop is in JavaScript like I'm 12, with an everyday
> metaphor. Then ask me two questions to check I actually understood.

The "ask me two questions" tail is the key. It converts a lecture into a
conversation. If you can't answer the questions, ask for a *different* metaphor,
not a longer explanation. Metaphors either click in one sentence or don't;
stacking more words on a broken metaphor helps nothing.

### "Hint, not answer"

> I'm trying to make a loop that prints 1 to 5 but mine prints 1 to 6. Ask me
> what I wrote and gently guide me to the bug with questions. Don't fix it
> for me unless I ask.

One sentence — "don't fix it unless I ask" — changes the AI's entire posture.
Beginners underestimate how often they *would* have figured it out with one
question's worth of friction removed.

### "Explain this error to me"

> I got this error: `SyntaxError: missing ) after argument list`. Explain
> what it means in plain English, show one tiny example of code that causes
> it, and one line of how the fix usually looks.

This is the single most valuable habit in this whole book. When code breaks
(and it will, hourly), pointing the error message at the AI and asking for
plain-English translation turns every error into a private lesson.

### "Quiz me"

> Quiz me on JavaScript variables and loops. One question at a time, wait for
> my answer, tell me if I'm right, and adjust difficulty to my level. Start easy.

Your AI becomes a flashcard deck that adapts. Ten minutes of this beats an
hour of rereading.

### "Explain it back"

> I'm going to explain what `return` does in my own words. Tell me where my
> explanation is wrong or fuzzy. [your explanation here]

This is the "explain it back" technique, and it's brutal in the best way.
Explaining something out loud exposes every gap that skimming hid. The AI's
job is to poke exactly where you're fuzzy.

### "Three versions"

> Give me three *different* metaphors for what a variable is, one sentence
> each. I'll pick the one that clicks.

AIs are tireless at generating alternatives. When one explanation isn't
landing, three fresh phrasings usually beats one long one.

## The copy-paste checklist

Sometimes you *will* take code from the AI — that's normal for real snippets
and fine. Before you keep it, run it through this checklist. If any answer is
no, you're in answer-machine mode, back up:

1. ______ Can I say out loud what this code does, line by line?
2. ______ Could I rewrite it myself from a blank console, with the AI closed?
3. ______ Did I try at least one variation myself (change a name, a number,
   the order)?
4. ______ Do I know what would happen if one specific line were deleted?

Line 4 is a favorite. Ask the AI: "What would break if line 3 weren't here?"
Understanding a line's *absence* teaches its *purpose*.

## A rule for when you're stuck

Stuck for more than ~10 minutes without progress? Change strategies:

- wrong move: reading the next tutorial chapter hoping it will clarify the
  last one
- right move: tell the AI exactly what you tried and *where* you're stuck:
  "I expected X, I got Y, here's my code" and let it interview you.

"I tried A, expected X, got Y" is the magic sentence of debugging — you'll
meet it again next chapter.

## What "done with help" looks like

A useful benchmark: you should be able to close the AI and, unaided, write:

- a variable of each type, and print a template-literal sentence
- a `for` loop printing 1 to 10
- a function that takes a parameter and returns a value

If you can do those cold, Chapters 02–04 aren't just in your history —
they're in your head. Sprinkle these three checks into any AI quiz session.

On to [Chapter 06: When Code Breaks](06-when-code-breaks.md) — the chapter
that makes everything before it survivable.
