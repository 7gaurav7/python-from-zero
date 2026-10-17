# Repository Basics

## Learning Objectives
By the end of this lesson you can:
- Turn a folder into a Git repository with `git init`
- Stage and commit changes with `git add` and `git commit`
- Check a repository's current state with `git status`
- View a repository's history with `git log`

## Concept Explanation

This lesson covers the five commands you'll use every single day:
`init`, `add`, `commit`, `status`, and `log`. Together they form the basic
loop of using Git: make changes, check what changed, stage what you want
to save, commit it with a message, repeat.

## Syntax

```
git init                       # turn the current folder into a Git repository
git status                     # show what's changed since the last commit
git add <filename>             # stage a specific file
git add .                       # stage everything changed in this folder
git commit -m "message"        # save a snapshot of staged changes
git log                         # view commit history
git log --oneline               # a condensed one-line-per-commit view
```

## Examples

**Example 1 — Starting a new repository**
```
$ mkdir my-project
$ cd my-project
$ git init
Initialized empty Git repository in /path/to/my-project/.git/
```

**Example 2 — Checking status, then staging and committing a file**
```
$ echo "print('Hello, Git!')" > hello.py
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

$ git add hello.py
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hello.py

$ git commit -m "Add hello.py"
[main (root-commit) a1b2c3d] Add hello.py
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
```

**Example 3 — Making another change and committing again**
```
$ echo "print('A second line!')" >> hello.py
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   hello.py

$ git add hello.py
$ git commit -m "Add a second print statement"
[main b2c3d4e] Add a second print statement
 1 file changed, 1 insertion(+)
```

**Example 4 — Viewing history**
```
$ git log --oneline
b2c3d4e (HEAD -> main) Add a second print statement
a1b2c3d Add hello.py
```

## Common Mistakes

- **Running `git init` inside an already-existing repository** (e.g.
  inside a subfolder of one) — usually a sign you're in the wrong
  directory; check with `pwd` (or `cd` to where you meant to be) first.
- **Forgetting `git add` before `git commit`** — Git only commits what's
  been staged; a modified-but-unstaged file won't be included even if it
  shows up in `git status`.
- **Writing a vague commit message** like `"stuff"` or `"fix"` — a good
  commit message describes *what* changed and *why*, so future-you (or a
  teammate) can understand the history without re-reading every line of
  code. `"Fix off-by-one error in the discount calculation"` beats `"fix"`.
- **Committing far too rarely** (one giant commit for a week of work) —
  small, focused commits make history much more useful; commit every time
  you finish one coherent piece of work.

## Practice

1. Create a new folder, run `git init`, and confirm the `.git` folder
   exists (`ls -a`).
2. Create a Python file with one `print()` statement, check `git status`,
   then `git add` and `git commit` it.
3. Modify the file, check `git status` again to see the difference, then
   commit the change with a clear message.
4. Run `git log --oneline` and confirm you see both commits.

## Challenge

Make three separate, small, well-described commits to a practice project
(e.g. one commit per function you add), then use `git log` (without
`--oneline`) to read the full details of each commit, including author and
date.

## Mini Project

Turn one of your completed `19-projects` folders into its own small Git
repository: run `git init` inside it, then make an initial commit with all
of its files, followed by one additional commit for a small improvement
you make to it.

## Summary

`git init` starts tracking a folder; `git status` shows what's changed;
`git add` stages specific changes; `git commit -m "..."` saves a permanent,
labeled snapshot; `git log` shows the full history. This add → commit loop
is the daily rhythm of using Git.

## Next Step

Continue to [`03-branching-and-merging.md`](03-branching-and-merging.md).
