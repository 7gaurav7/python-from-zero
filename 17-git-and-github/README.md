# 17 — Git and GitHub

This lesson is a little different from the others: it's not about the
Python language, but about **version control** — the tool that lets you
save snapshots of your code over time, undo mistakes, and collaborate with
others (including your future self). If you downloaded this course from
GitHub, you've been using a Git repository this entire time — now you'll
learn what's actually happening, and how to use it for your own projects.

**Prerequisite check:** none of this depends on Python knowledge — you
could technically read this lesson on day one. It's placed here because by
now you have your own code (from `19-projects`) that's actually worth
putting under version control.

## Lessons in This Topic

| # | Lesson | What You'll Learn |
|---|---|---|
| 1 | [What Git Is](01-what-is-git.md) | The problem version control solves, and Git vs. GitHub |
| 2 | [Repository Basics](02-repository-basics.md) | `init`, `add`, `commit`, `status`, `log` |
| 3 | [Branching and Merging](03-branching-and-merging.md) | `branch`, `switch`/`checkout`, `merge`, conflicts |
| 4 | [GitHub and Remote Workflow](04-github-workflow.md) | `push`, `pull`, `clone`, remotes, pull requests |
| 5 | [Writing a Good README](05-readme-basics.md) | Markdown basics and what every README should cover |

## Suggested Order

Follow the table top to bottom — each lesson assumes the commands from the
one before it.

## How to Practice This Topic

Unlike the Python topics, the best way to practice Git is on an actual
folder of files, since every command's effect is easiest to understand
when you can see it happen. As you go through each lesson:

1. Create (or reuse) a small practice folder.
2. Run every command the lesson shows, in order, on that folder.
3. Use `git status` and `git log` liberally — they never change anything,
   so running them often to "check your understanding" is always safe.

**Previous:** [`16-testing-and-debugging`](../16-testing-and-debugging/README.md) | **Next:** [`18-real-world-python`](../18-real-world-python/README.md)
