# Writing a Good README

## Learning Objectives
By the end of this lesson you can:
- Explain why every project benefits from a README
- Write a README covering what a project is, how to run it, and how it
  works
- Use basic Markdown formatting (the format every README in this course
  is written in)

## Concept Explanation

A **README** is the first (often only) file people read to understand a
project — including future you, returning to old code months later.
GitHub automatically displays a repository's `README.md` on its main page,
which is why nearly every project has one.

You've been reading (and this course is built entirely from) `README.md`
files since `00-getting-started` — this lesson makes explicit what makes
one good, so you can write your own for the projects you build going
forward.

A solid README typically answers, in order:
1. **What is this?** — a one or two sentence description.
2. **How do I run it?** — setup/installation steps.
3. **How do I use it?** — basic usage instructions or examples.
4. **What does it require?** — dependencies, Python version, etc.
5. (Optional) **How can I contribute?** — for open projects.

## Syntax

READMEs are written in **Markdown** (`.md`), a lightweight text formatting
language. The basics:

```markdown
# Heading 1
## Heading 2
### Heading 3

**bold text**
*italic text*

- bullet point
- another bullet point

1. numbered item
2. another numbered item

`inline code`

​```python
# a fenced code block, with syntax highlighting
print("Hello!")
​```

[link text](https://example.com)

> a blockquote
```

## Examples

**Example 1 — A minimal but complete README**
```markdown
# Quiz Game

A command-line multiple-choice quiz game written in Python.

## How to Run

​```
python quiz_game.py
​```

## How to Play

Answer each question by typing the number of your chosen option. Your
score is shown at the end.

## Requirements

- Python 3.8 or later
```

**Example 2 — Adding a features list and usage example**
```markdown
## Features

- Multiple-choice questions with instant feedback
- Final score summary with performance-based messages
- No external dependencies

## Example Session

​```
What does CPU stand for?
  1. Central Process Unit
  2. Central Processing Unit
  3. Computer Personal Unit
Your answer (number): 2
Correct!
​```
```

**Example 3 — Documenting project structure**
```markdown
## Project Structure

​```
quiz-game/
├── quiz_game.py       # main program
├── questions.json      # question data
└── README.md
​```
```

**Example 4 — A badge-free, honest "Known Limitations" section**
```markdown
## Known Limitations

- Questions are hard-coded in `questions.json` — no editor UI yet.
- Doesn't currently save scores between runs.
```
(This last kind of section is a mark of a *mature* project — being upfront
about what something doesn't do yet builds trust.)

## Common Mistakes

- **A README with no "how to run it" section** — even a brilliant project
  is unusable to someone (including future you) who doesn't know the exact
  command to start it.
- **Letting the README go stale** — if you change how a project works,
  update the README in the same commit; a wrong README is often worse than
  no README.
- **Wall-of-text README with no headings** — use Markdown headings and
  bullet points; people skim READMEs, they rarely read them top to bottom.
- **Forgetting to specify the Python version / dependencies** — "it works
  on my machine" isn't good enough once someone else tries to run it.

## Practice

1. Write a README for one of your finished `19-projects` beginner
   projects, covering what it is, how to run it, and its requirements.
2. Add a "Features" section and an "Example Session" section (a copy-paste
   of real output) to that README.
3. Add a "Project Structure" section showing its files in a fenced code
   block.
4. Review this repository's own root [`README.md`](../README.md) and
   identify which of the sections above it already includes.

## Challenge

Write a complete README from scratch for a project idea of your own (it
doesn't need to exist yet) — as if you were about to start building it.
Writing the README *first* is a real technique some developers use to
clarify their own thinking before writing any code.

## Mini Project

Add or improve the README for every project you've completed in
`19-projects` so each one could stand alone if someone found only that
folder, without the rest of this course for context.

## Summary

A good README tells a stranger (or future you) what a project is, how to
run it, and how to use it — written in Markdown with clear headings,
code blocks for commands/examples, and kept up to date as the project
changes. It's the single highest-leverage piece of documentation any
project has.

## Next Step

You've completed `17-git-and-github`. Continue to
[`18-real-world-python`](../18-real-world-python/README.md).
