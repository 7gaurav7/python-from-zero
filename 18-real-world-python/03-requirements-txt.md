# requirements.txt

## Learning Objectives
By the end of this lesson you can:
- Explain why a project needs to record its dependencies
- Generate a `requirements.txt` file from an active environment
- Install every dependency listed in a `requirements.txt` file at once
- Pin exact versions for reproducibility

## Concept Explanation

If you send a project to someone else (or clone your own project onto a
new computer), they need to know exactly which packages to install before
it will run. Re-explaining this by hand ("oh, you also need to `pip
install requests` and `pip install pillow`...") doesn't scale.

A **`requirements.txt`** file lists every package (and usually exact
version) a project depends on, in plain text, one per line. Anyone with
this file can recreate your exact environment with a single command.

```
requests==2.31.0
pillow==10.0.0
```

## Syntax

```
pip freeze > requirements.txt        # save all currently installed packages to a file
pip install -r requirements.txt      # install everything listed in the file
```

A `requirements.txt` line can pin an exact version (`package==1.2.3`), a
minimum version (`package>=1.2.3`), or just the name with no version
(`package`) — pinning exact versions is recommended for reproducibility,
so everyone (and your future self) installs the exact same thing.

## Examples

**Example 1 — Generating a requirements.txt from your environment**
```
(venv) $ pip install requests pillow
(venv) $ pip freeze > requirements.txt
(venv) $ cat requirements.txt
pillow==10.0.0
requests==2.31.0
```

**Example 2 — Installing from a requirements.txt on a new machine**
```
$ git clone https://github.com/your-username/my-project.git
$ cd my-project
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
Collecting requests==2.31.0
...
Collecting pillow==10.0.0
...
Successfully installed pillow-10.0.0 requests-2.31.0
```

**Example 3 — A requirements.txt with a comment (documenting why a
package is needed)**
```
# requirements.txt
requests==2.31.0   # for calling the weather API
pillow==10.0.0      # for resizing profile pictures
```
(Lines starting with `#` are ignored by `pip install -r`, exactly like
Python comments.)

**Example 4 — Updating requirements.txt after adding a new dependency**
```
(venv) $ pip install python-dotenv
(venv) $ pip freeze > requirements.txt
(venv) $ cat requirements.txt
pillow==10.0.0
python-dotenv==1.0.0
requests==2.31.0
```

## Common Mistakes

- **Forgetting to regenerate `requirements.txt`** after installing a new
  package — anyone else setting up the project will be missing it.
- **Committing the `venv/` folder instead of (or as well as)
  `requirements.txt`** — commit only `requirements.txt`; the `venv/`
  folder is meant to be regenerated locally by each person, not shared.
- **Not pinning versions** (`requests` instead of `requests==2.31.0`) —
  this can install a newer, possibly incompatible version months later,
  breaking reproducibility.
- **Running `pip freeze` outside the project's virtual environment** —
  this captures your *global* packages (potentially hundreds, from every
  other project you've ever worked on), not just the ones this project
  actually needs.

## Practice

1. In an activated virtual environment, install any one package and
   generate a `requirements.txt` with `pip freeze`.
2. Deactivate, delete the `venv` folder entirely, then recreate a fresh
   virtual environment and reinstall everything using
   `pip install -r requirements.txt`.
3. Add a `#` comment above one line in your `requirements.txt` explaining
   why that package is needed.
4. Add a second package, regenerate `requirements.txt`, and confirm (with
   `cat` or by opening the file) that both packages are listed.

## Challenge

Simulate the "new team member" experience: in a completely fresh folder,
`git clone` a repository that has a `requirements.txt` (or copy one of
your own practice projects into a new location), create a new virtual
environment, and get it running using only the `requirements.txt` file —
no memory of what you installed originally.

## Mini Project

Add a `requirements.txt` to project structure lesson's example project
(next lesson) — even if it currently has zero external dependencies, an
empty or comment-only `requirements.txt` documents that intentionally.

## Summary

`requirements.txt` records a project's exact dependencies in plain text,
generated with `pip freeze > requirements.txt` and restored with
`pip install -r requirements.txt`. This is what lets anyone (including
future you, on a new computer) recreate your exact working environment
with one command.

## Next Step

Continue to [`04-project-structure.md`](04-project-structure.md).
