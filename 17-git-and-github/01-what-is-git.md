# What Git Is

## Learning Objectives
By the end of this lesson you can:
- Explain the problem Git solves
- Define "version control," "repository," and "commit" in plain language
- Explain the difference between Git and GitHub

## Concept Explanation

Imagine editing an essay and, every time you make a big change, saving a
new copy: `essay.docx`, `essay_v2.docx`, `essay_v2_final.docx`,
`essay_v2_final_REALLY.docx`. This is what programmers did before version
control — and it gets unmanageable fast, especially with more than one
person editing the same project.

**Git** is a **version control system**: a tool that tracks every change
to a set of files over time, lets you see exactly what changed and when,
and lets you go back to any earlier point if something breaks. Instead of
duplicate files, Git keeps one project folder (a **repository**, or
"repo") with a complete history built from **commits** — labeled snapshots
you create on purpose, each with a message describing what changed.

**Git vs. GitHub** — this trips up almost every beginner:
- **Git** is the tool itself: software that runs on your computer and
  tracks history locally. It works completely offline.
- **GitHub** is a website that *hosts* Git repositories online, adding
  collaboration features (pull requests, issues, project pages). You could
  use Git your entire life without ever using GitHub — but GitHub (and
  competitors like GitLab/Bitbucket) is how most teams share and
  collaborate on Git repositories in practice.

## Syntax

No commands yet — this lesson is conceptual. Check that Git is installed:
```
git --version
```
If that fails, install Git from https://git-scm.com/downloads.

One-time setup (tells Git who you are, for commit history):
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Examples

There's no runnable Python here — but here's the mental model in a
diagram:

```
Your project folder (working directory)
        │
        │  git add       (stage changes you want to include)
        ▼
   Staging area
        │
        │  git commit    (save a permanent snapshot with a message)
        ▼
  Repository history  ──── git push ────▶  GitHub (remote repository)
   (on your computer)  ◀─── git pull ─────
```

Every `python-from-zero` example you've run in this course lives inside a
Git repository (if you cloned it from GitHub) exactly like this — the
`.git` hidden folder at the project root is where all of this history is
actually stored.

## Common Mistakes

- **Thinking Git and GitHub are the same thing.** Git is the tool; GitHub
  is one (very popular) place to host Git repositories online.
- **Believing you need the internet to use Git.** All of the core
  commands in the next lesson (`init`, `add`, `commit`, `log`) work
  completely offline — you only need a connection for `push`/`pull`/
  `clone` with a remote like GitHub.
- **Skipping the one-time `user.name`/`user.email` setup** — Git will
  refuse to commit (or attribute commits to a generic placeholder) without
  it.

## Practice

1. Run `git --version` in your terminal and confirm Git is installed.
2. Run the one-time `git config --global user.name`/`user.email` setup
   with your own details.
3. In your own words (a short paragraph is fine), explain the difference
   between Git and GitHub to someone who has never coded.

## Challenge

Look up (search online) one real-world story of a team avoiding a serious
mistake because of Git's version history (e.g. reverting a bad change).
Summarize it in 2-3 sentences.

## Mini Project

No dedicated mini project — this lesson is the conceptual foundation for
the hands-on commands in the next lesson.

## Summary

Git is a version control system that tracks a project's history through
commits, letting you see what changed, when, and roll back if needed.
GitHub is a website that hosts Git repositories online and adds
collaboration tools — Git works entirely offline; GitHub is optional but
extremely common in practice.

## Next Step

Continue to [`02-repository-basics.md`](02-repository-basics.md).
