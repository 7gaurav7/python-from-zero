# 🤝 Contributing to Python From Zero

Thank you for considering a contribution! This repo exists to help absolute
beginners progress all the way to intermediate, project-ready Python, so
the bar for any contribution is: **does this make that path easier to
follow, without skipping a step or assuming knowledge the learner doesn't
have yet?**

## Ways to Contribute

- **Fix errors** — typos, broken code, incorrect explanations, wrong
  expected output, broken links between lessons.
- **Improve clarity** — if an explanation confused you as a learner, it
  will confuse others. Suggest a clearer wording.
- **Add practice problems** — more (good, appropriately-leveled) practice
  problems are always welcome in `exercises/`.
- **Add resources** — beginner-friendly articles, videos, or tools for
  `resources/`.
- **Add project ideas** — a new beginner/intermediate/final project
  proposal for `19-projects/` is welcome, as long as it follows the
  11-part structure described below.
- **Translate** — translations of lesson content into other languages are
  welcome as a `README.<lang-code>.md` (or `<lesson>.<lang-code>.md`)
  alongside the original.
- **Report confusing sections** — even opening an issue that says "I
  didn't understand X" is a valuable contribution.

## Ground Rules

1. **Match the level of the topic it's in.** Topics `00`–`13` assume
   *zero* prior programming knowledge — don't introduce advanced syntax,
   external libraries, or "clever" one-liners there, even if they're more
   "Pythonic." Topics `14`–`20` assume the fundamentals are already
   solid, but still shouldn't introduce a concept before it's been taught
   somewhere earlier in the course — if a new lesson needs something not
   yet covered, teach it inline or add a prerequisite note.
2. **Every code example must run.** Test it yourself (`python3 -m
   py_compile <file>.py` at minimum, and actually run it) before
   submitting. Any example with `input()` should be clearly marked as
   needing interactive use.
3. **Follow PEP 8** — 4-space indentation, `snake_case` names, sensible
   line lengths. A linter like `flake8` is helpful if you have it.
4. **Include expected output** in a comment for any example that prints
   something.
5. **Keep exercises and solutions separate, always.** Never put a
   solution inside a lesson file or inside `exercises/` — solutions only
   belong in `solutions/`, or in a project's own `solution/` subfolder.
   Exercise numbers in `exercises/NN_topic_exercises.py` must correspond
   to the same numbers in `solutions/NN_topic_solutions.py`.
6. **Never put a solution immediately after its exercise in the same
   lesson file.** The whole point of the separate `exercises/`/`solutions/`
   split is to make peeking a deliberate extra step, not an accident.
7. **Match the existing structure for the kind of content you're adding:**
   - A lesson in topics `00`–`13` follows: Beginner-friendly explanation →
     Important concepts → Syntax → Examples → Practice problems →
     Challenge problems → Common mistakes → Mini quiz → Practical
     exercise.
   - A lesson in topics `14`–`20` follows: Topic → Learning Objectives →
     Concept Explanation → Syntax → Examples → Common Mistakes → Practice
     → Challenge → Mini Project → Summary → Next Step. Each lesson file
     is one focused subtopic, with its own `-examples.py` file.
   - A project in `19-projects/` follows the 11-part structure: Problem
     Statement, Learning Objectives, Requirements, Features, Suggested
     Folder Structure, Step-by-Step Milestones, Starter Code, Test Cases,
     Expected Behavior, Extension Challenges, and a Solution kept in its
     own `solution/` subfolder. New projects need a real `tests/`
     folder with passing `unittest` tests, not just a description.
8. **Keep logic testable.** When a project involves both data/logic and
   user interaction, separate them (a class or pure function with no
   `input()`/`print()`, plus a thin CLI layer around it) — see any
   existing `19-projects/*/solution/solution.py` for the pattern. This
   makes it possible to write meaningful tests without simulating
   keyboard input.
9. **Update navigation when you add or remove a lesson.** If you add,
   rename, or remove a lesson file, update: that topic's `README.md`
   lesson table, the previous/next lesson's "Next Step" link, the root
   `ROADMAP.md`, and `CHECKLIST.md`.
10. **No duplicate lessons.** Before adding a new file, check whether the
    topic folder already covers the subtopic under a different name —
    rename/edit the existing one instead of creating a second version.

## How to Submit a Change

1. Fork this repository.
2. Create a branch: `git checkout -b fix/typo-in-loops-lesson` (see
   `17-git-and-github` if branching is new to you).
3. Make your changes.
4. Test any code you added or changed (`python3 -m py_compile`, run it,
   and run any related project's test suite with `python -m unittest`).
5. Commit with a clear message: `git commit -m "Fix off-by-one example in 05-loops"`.
6. Push and open a Pull Request describing **what** you changed and
   **why**.

## Style Guide (Quick Reference)

- Use `snake_case` for variables and functions: `student_name`, not
  `studentName`.
- Use 4 spaces per indentation level (never tabs).
- Add a blank line between logical blocks of code.
- Prefer f-strings for formatting: `f"Hello, {name}!"`.
- Comments should explain **why**, not restate **what** (the code already
  shows what).
- Keep lines under ~79–99 characters where reasonable.

## Code of Conduct

Be kind. Remember every learner using this repo once knew nothing about
programming — including you. Answer questions and review contributions
the way you'd want to have been treated on day one.
