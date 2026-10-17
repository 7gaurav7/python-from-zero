# Virtual Environments

## Learning Objectives
By the end of this lesson you can:
- Explain why every Python project should use its own virtual environment
- Create, activate, and deactivate a virtual environment
- Recognize when a virtual environment is active
- Know which files/folders to exclude from Git in a project using one

## Concept Explanation

Every third-party package you install with `pip` (next lesson) normally
gets installed system-wide, shared by every Python project on your
computer. This causes real problems: Project A might need version 1.0 of
a library, while Project B needs version 2.0 — installed globally, only
one version can exist at a time.

A **virtual environment** is an isolated, self-contained copy of Python
and its packages, created for one specific project. Installing a package
inside a virtual environment only affects that environment — other
projects (and your system Python) are untouched.

**Rule of thumb: every project that uses third-party packages should have
its own virtual environment.**

## Syntax

```
python -m venv venv          # create a virtual environment named "venv"
                               # (the folder name "venv" is a strong convention)

# Activate it:
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate          # Windows (Command Prompt)
venv\Scripts\Activate.ps1      # Windows (PowerShell)

deactivate                     # turn off the virtual environment
```

While a virtual environment is active, your terminal prompt usually shows
its name in parentheses, e.g. `(venv) $`, and `python`/`pip` refer to the
versions inside that environment.

## Examples

**Example 1 — Creating and activating a virtual environment**
```
cd my-project
python -m venv venv
source venv/bin/activate
```
Sample output (prompt changes to show the environment is active):
```
(venv) $
```

**Example 2 — Confirming which Python you're using**
```
(venv) $ which python
/path/to/my-project/venv/bin/python
```
On Windows: `where python` shows the equivalent path inside `venv\Scripts\`.

**Example 3 — Deactivating**
```
(venv) $ deactivate
$
```
The prompt returns to normal, and `python`/`pip` refer to your system
installation again.

**Example 4 — A project's `.gitignore` entry for its virtual environment**
```
# .gitignore
venv/
__pycache__/
*.pyc
```
The `venv/` folder should **never** be committed to Git — it's large,
platform-specific, and entirely reconstructable from `requirements.txt`
(next lesson) on any machine.

## Common Mistakes

- **Committing the `venv/` folder to Git** — it can be hundreds of
  megabytes and won't even work correctly on a different operating system;
  always add it to `.gitignore`.
- **Forgetting to activate the environment** before installing packages —
  you'll end up installing into your system Python instead, defeating the
  whole purpose.
- **Installing packages system-wide out of habit** and wondering later why
  different projects conflict — this is exactly the problem virtual
  environments solve.
- **Naming the environment folder something unconventional** and
  forgetting to add *that* name to `.gitignore` — `venv` or `.venv` are the
  strong conventions for a reason: tools and teammates expect them.

## Practice

1. Create a new project folder and set up a virtual environment inside it.
2. Activate it, confirm with `which python` (or `where python` on Windows)
   that you're using the environment's Python, then deactivate it.
3. Add a `.gitignore` file to that folder excluding `venv/`.
4. Delete the virtual environment folder entirely, then recreate it from
   scratch — notice this is quick and safe, since nothing valuable lives
   inside it that isn't reproducible.

## Challenge

Create two separate project folders, each with its own virtual
environment. In one, install a specific version of a small package (the
next lesson covers `pip install package==version`); in the other, install
a different version. Confirm (`pip show package_name` in each) that the
two don't conflict.

## Mini Project

Set up a proper virtual environment for one of your `19-projects`
solutions that doesn't need one yet (they've all used the standard library
only) — this is good practice for the day you add your first third-party
dependency to a personal project.

## Summary

A virtual environment is an isolated Python installation and package set,
scoped to one project, preventing dependency conflicts between projects.
Create one with `python -m venv venv`, activate it before installing
anything, and always exclude the environment folder from Git.

## Next Step

Continue to [`02-pip-basics.md`](02-pip-basics.md).
