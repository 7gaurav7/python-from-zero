# Changelog

This file documents how **Python From Zero** evolved from a `00`–`13`
beginner course into a full beginner-to-intermediate curriculum with
real-world practices, a project track, and an AI/ML preparation bridge.

---

## [2.0.0] — Curriculum Upgrade: Intermediate Python, Real-World Skills, and AI/ML Bridge

This release is a major upgrade of the existing repository. The original
`00-getting-started` through `13-oop` curriculum, and its exercises,
solutions, and resources, were **preserved and built upon** — nothing in
the foundational path was removed, and only a small number of things were
fixed for accuracy or consistency (see "Fixed," below).

### Added

**New topic: `14-intermediate-python/`**
Nine lessons bridging beginner and professional Python idioms:
comprehensions, lambda functions, `map()`/`filter()`, `*args`/`**kwargs`,
`enumerate()`/`zip()`, unpacking, iterators, generators, and decorators.
Each lesson follows the Topic → Learning Objectives → Concept Explanation
→ Syntax → Examples → Common Mistakes → Practice → Challenge → Mini
Project → Summary → Next Step structure, with a matching runnable
examples file. Added combined
`exercises/14_intermediate_python_exercises.py` and
`solutions/14_intermediate_python_solutions.py`.

**New topic: `15-working-with-data/`**
Five lessons on exchanging and processing data: JSON, CSV, `datetime`,
`pathlib`, and a capstone "basic data processing" lesson combining all
four. Same lesson structure and examples-file pattern as topic 14. Added
matching exercises/solutions files.

**New topic: `16-testing-and-debugging/`**
Five lessons: a systematic debugging process, reading tracebacks,
assertions, `unittest` basics, and an introduction to `pytest`. Added
matching exercises/solutions files.

**New topic: `17-git-and-github/`**
Five lessons covering what Git is, repository basics (`init`, `add`,
`commit`, `status`, `log`), branching and merging, the GitHub remote
workflow (`push`/`pull`/`clone`), and writing a good README. Exercises are
hands-on terminal tasks (kept as a `.py` file of commented instructions
for consistency with every other topic's exercises/solutions file
format), with matching solutions.

**New topic: `18-real-world-python/`**
Six lessons: virtual environments, `pip` basics, `requirements.txt`,
project structure, configuration basics, and environment variables. Added
matching exercises/solutions files, plus runnable examples for the two
code-heavy lessons (configuration basics, environment variables).

**New topic: `19-projects/`** (restructured from the original
`14-mini-projects/` and `15-final-projects/` — see "Changed," below)
A three-tier project track — `beginner-projects/`, `intermediate-projects/`,
`final-projects/` — with a new top-level `README.md` explaining the tiers
and how to use them. Every project now follows an 11-part structure:
problem statement, learning objectives, requirements, features, suggested
folder structure, step-by-step milestones, starter code, test cases,
expected behavior, extension challenges, and a solution kept in its own
`solution/` subfolder.

**New topic: `20-ai-ml-preparation/`**
Six lessons forming a deliberate *bridge* (not an ML course): NumPy
fundamentals, pandas fundamentals, Matplotlib fundamentals, Jupyter
Notebook basics, math foundations for ML (vectors, mean/variance, linear
equations), and the Python habits that matter most once you start reading
ML code. Added matching exercises/solutions files.

**New root file: `CHANGELOG.md`** (this file).

**Testing infrastructure for every project in `19-projects/`.** All 7
projects (2 beginner, 3 intermediate, 2 final) now ship with a real
`tests/` folder using Python's built-in `unittest`, covering their core
logic. All 38 tests pass.

**Expanded `resources/`:**
- `cheat-sheet.md` extended with quick-reference sections for topics
  `14`–`18` (comprehensions/lambda/map/filter, `*args`/`**kwargs`/
  enumerate/zip/unpacking, iterators/generators/decorators, JSON/CSV/
  datetime/pathlib, testing, Git, and real-world project setup).
- `glossary.md` extended with ~25 new terms introduced in topics `14`–`18`
  (Assertion, Branch, Comprehension, Decorator, Dependency, Environment
  variable, Generator, Iterator, JSON, Lambda, Merge, pip, Pull Request,
  Remote, Repository, requirements.txt, Unit test, Unpacking, Virtual
  environment, `*args`/`**kwargs`, and more).
- `debugging-tips.md` and `further-reading.md` updated with cross-references
  to the new dedicated topics (`16-testing-and-debugging`,
  `17-git-and-github`, `20-ai-ml-preparation`) so readers know where to go
  deeper.

### Changed

**Projects reorganized into `19-projects/`.** The original
`14-mini-projects/` (Number Guessing Game, Simple Calculator, To-Do List
App, Contact Book, Quiz Game) and `15-final-projects/` (Expense Tracker,
Student Management System) were moved into a tiered structure:
- `19-projects/beginner-projects/`: Number Guessing Game, Simple Calculator
- `19-projects/intermediate-projects/`: To-Do List App, Contact Book, Quiz
  Game
- `19-projects/final-projects/`: Expense Tracker, Student Management
  System

No project content was deleted — every original problem statement,
requirement, and milestone was preserved and then extended to the new
11-part structure.

**Every migrated project's solution was refactored to separate core logic
from `input()`/`print()` calls**, specifically so that logic could be unit
tested without simulating keyboard input. For example:
- Number Guessing Game: extracted a pure `check_guess(secret, guess)`
  function.
- Simple Calculator: `calculate(a, b, operator)` was already pure; left
  as-is and given tests.
- To-Do List App: introduced a `TaskManager` class holding all task logic.
- Contact Book: introduced a `ContactBook` class, including a
  `to_lines()`/`load_from_lines()` pair that lets the file format be
  tested without touching the filesystem.
- Quiz Game: extracted a pure `grade_answer(question_data, choice)`
  function.
- Expense Tracker and Student Management System already used a clean
  `Expense`/`ExpenseTracker` and `Student`/`Classroom` class design; these
  were left structurally as-is and given test suites.

**Root `README.md`, `ROADMAP.md`, and `CHECKLIST.md` rewritten** to cover
the full `00`–`20` curriculum: who the course is for, prerequisites, how
to use the repository, a complete curriculum roadmap with phases and
checkpoints, a progress checklist for every topic and project, recommended
learning order, project progression across the three tiers, contribution
guidelines, and an explicit statement that exercises should be attempted
before viewing solutions.

**`CONTRIBUTING.md` rewritten** to describe the three distinct content
structures now in the repository (the 9-section format for `00`–`13`, the
11-section lesson format for `14`–`20`, and the 11-part project format for
`19-projects/`), and to require new projects to ship with real tests and a
separate `solution/` subfolder.

**`SETUP.md` extended** with a note clarifying that Git installation
(`17-git-and-github`) and virtual environment / `pip` setup
(`18-real-world-python`) are taught as part of their own lessons, so
nothing extra needs to be installed before starting the course.

### Fixed

- **`14-intermediate-python/01-comprehensions.md`**: corrected an expected
  output value (`len("Carla")` is `5`, not `6`) in the dictionary
  comprehension example.
- **`14-intermediate-python/08-generators.md`**: added the missing
  `08-generators-examples.py` runnable example file (the lesson existed
  without its matching code file).
- **`17-git-and-github/`**: removed a duplicate, less-structured
  consolidated lesson file (`01-git-and-github.md`) that conflicted with
  the five properly chained per-topic lesson files; fixed the resulting
  "Next Step" link and a broken relative link to the root `README.md` in
  the README-basics lesson.
- **`17-git-and-github/` exercises and solutions**: removed duplicate
  `.md` versions of the exercises/solutions that conflicted with the
  `.py` versions, keeping one consistent file per topic.
- **`18-real-world-python/`**: resolved two competing lesson-numbering
  schemes left over from earlier drafts (a 4-lesson version and a
  6-lesson version covering the same material). Kept the 6-lesson version
  (matching the course's explicit subtopic list — virtual environments,
  pip, requirements.txt, project structure, configuration basics,
  environment variables — one lesson each) and removed the 3 conflicting
  duplicate files. Fixed a dangling "Next Step" link in
  `01-virtual-environments.md` and rewrote `README.md` to reference the
  correct 6-lesson structure.
- **`20-ai-ml-preparation/`**: removed two duplicate lesson files (an
  earlier draft of the math-for-ML lesson and the Python-habits lesson)
  that conflicted with the versions referenced in `README.md`.
- Removed assorted stray generated files that had been left in the
  repository from earlier test runs (`__pycache__/` directories, leftover
  `.json`/`.csv`/`.txt` sample output files, and a stray `config.json` at
  the repository root).

### Quality Control Performed

Before finalizing this upgrade, the following checks were run across the
entire repository:

1. **Markdown links** — a custom link-checking script scanned every `.md`
   file for relative links and confirmed each target exists (220 links
   checked; the only intentional exception was this file, created
   immediately after).
2. **Python syntax** — every `.py` file in the repository (lessons,
   exercises, solutions, and all 7 projects) was compiled with
   `python -m py_compile` with zero errors.
3. **Referenced files exist** — verified via the link-checking pass above,
   plus manual confirmation that every topic's `README.md` lesson table
   matches the lesson files actually present in that folder.
4. **Exercise/solution numbering matches** — confirmed all 20 topic
   exercise files in `exercises/` have an exact one-to-one matching
   solution file in `solutions/` (verified by diffing the base filenames).
5. **No duplicated lessons** — audited and resolved duplicate/conflicting
   files in `17-git-and-github/`, `18-real-world-python/`, and
   `20-ai-ml-preparation/` (see "Fixed," above); confirmed no other topic
   has duplicate lesson files.
6. **Difficulty increases logically** — confirmed topic ordering
   (`00`–`13` foundations → `14`–`18` intermediate/real-world skills →
   `19` projects → `20` optional AI/ML bridge) and that each lesson's
   stated prerequisites only reference earlier material.
7. **No lesson depends on an unexplained concept** — spot-checked that
   concepts used in examples (e.g. `*args`/`**kwargs` in the decorators
   lesson, iterators before generators) are taught in an earlier lesson
   within the same topic or an earlier topic.
8. **README navigation** — confirmed the root `README.md`'s structure
   diagram, curriculum roadmap, and "Start here" links all point to real,
   current paths.
9. **Project instructions** — ran every project's full test suite
   (`python -m unittest discover`) against its reference solution; all 7
   suites pass (38 tests total).
10. **This changelog** — produced as the final step, summarizing every
    change above.

---

### Final Verification Pass

A closing verification pass was run to confirm the upgrade actually lands
as documented above, independent of the work that produced it:

- Every `.py` file in the repository (lessons, exercises, solutions, and
  all 7 projects) recompiled cleanly with zero errors.
- A link-checking script re-scanned all 219 relative Markdown links
  repository-wide and found zero broken links.
- Every file in `exercises/` was confirmed to have an exact one-to-one
  matching file in `solutions/`, and vice versa.
- Every lesson file in `14`–`20` was confirmed to be referenced in its
  topic's own `README.md` lesson table, with no orphaned or duplicate
  files left in any topic folder.
- Every `*-examples.py` file was confirmed to have a matching lesson file,
  and vice versa, for topics `14`, `15`, `16`, `18`, and `20`.
- All 7 project test suites in `19-projects/` were re-run end-to-end
  against their reference solutions (38 tests total; all pass).
- The top-level folder structure was confirmed to match `README.md`'s
  documented tree exactly, `00` through `20`, with no gaps.
- Stray generated artifacts (`__pycache__/`, sample output files left by
  running examples) were swept from the repository one final time.

## [1.0.0] — Initial Release

- Initial beginner-to-OOP curriculum: `00-getting-started` through
  `13-oop`, each with the 9-part lesson structure (explanation, concepts,
  syntax, examples, practice problems, challenge problems, common
  mistakes, mini quiz, practical exercise).
- `exercises/` and `solutions/` folders with one matching pair per topic.
- `14-mini-projects/` (5 projects) and `15-final-projects/` (2 capstone
  projects), later reorganized into `19-projects/` in version 2.0.0.
- `resources/` folder: cheat sheet, glossary, further reading, PEP 8 quick
  guide, debugging tips.
- Root documentation: `README.md`, `ROADMAP.md`, `SETUP.md`,
  `CHECKLIST.md`, `CONTRIBUTING.md`, `LICENSE`.
