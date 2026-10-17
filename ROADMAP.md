# 🗺 Learning Roadmap

This roadmap gives you a realistic schedule and explains **why** the topics
are ordered the way they are. Everything here assumes zero prior programming
knowledge.

## How long will this take?

That depends entirely on your pace — there is no deadline. As a rough guide,
studying **45–90 minutes a day**:

| Phase | Topics | Estimated Time |
|---|---|---|
| Phase 1: Foundations | 00 – 04 | 1.5 – 2 weeks |
| Phase 2: Control Flow & Data | 05 – 08 | 2 – 3 weeks |
| Phase 3: Structuring Code | 09 – 12 | 2 – 3 weeks |
| Phase 4: Object-Oriented Programming | 13 | 1 – 1.5 weeks |
| Phase 5: Intermediate Python & Idioms | 14 | 1 – 2 weeks |
| Phase 6: Working with Data | 15 | 1 week |
| Phase 7: Testing, Debugging & Git | 16 – 17 | 1.5 – 2 weeks |
| Phase 8: Real-World Project Setup | 18 | 1 week |
| Phase 9: Projects | 19 | 2 – 4 weeks |
| Phase 10: AI/ML Preparation (optional) | 20 | 1 – 2 weeks |
| **Total (through Phase 9)** | | **~13–19 weeks** |
| **Total (with optional Phase 10)** | | **~14–21 weeks** |

Go slower if something doesn't click — that is completely normal. Programming
rewards patience, not speed.

---

## Phase 1 — Foundations (00 – 04)

**Goal:** Understand what code even is, and be able to store data and make
simple decisions.

- `00-getting-started` — What is programming? Installing Python. Running your
  first program. The Python interpreter vs. a script file.
- `01-variables-and-data-types` — Storing data in memory. `int`, `float`,
  `str`, `bool`.
- `02-input-output` — Talking to the user with `print()` and `input()`.
- `03-operators` — Arithmetic, comparison, logical, and assignment operators.
- `04-conditions` — `if` / `elif` / `else`. Making decisions in code.

**Checkpoint:** You should be able to write a program that takes input from
a user, does some math or comparison on it, and prints a different message
depending on the result.

---

## Phase 2 — Control Flow & Core Data Structures (05 – 08)

**Goal:** Repeat actions automatically and organize larger amounts of data.

- `05-loops` — `while` and `for` loops, `break`, `continue`, `range()`.
- `06-strings` — Slicing, formatting, common string methods.
- `07-lists-tuples-sets` — Ordered collections, mutability, uniqueness.
- `08-dictionaries` — Key-value data, the workhorse of real Python programs.

**Checkpoint:** You should be able to process a list of data (e.g. student
scores) using loops and produce a summary, without writing the same code
twice.

---

## Phase 3 — Structuring Code Like a Real Programmer (09 – 12)

**Goal:** Stop writing one giant script. Organize logic into reusable,
testable, safe pieces.

- `09-functions` — Defining and calling functions, parameters, return values,
  scope.
- `10-file-handling` — Reading and writing `.txt` and `.csv` files.
- `11-exceptions` — `try`/`except`, handling errors instead of crashing.
- `12-modules-and-packages` — Splitting code across files, using the standard
  library (`math`, `random`, `datetime`).

**Checkpoint:** You should be able to write a program spread across
functions (and even a second file) that reads data from a file and doesn't
crash when given bad input.

---

## Phase 4 — Object-Oriented Programming (13)

**Goal:** Model real-world things as objects — the paradigm behind almost all
serious Python software.

- `13-oop` — Classes, objects, attributes, methods, `__init__`, basic
  inheritance.

**Checkpoint:** You should be able to design a simple class (e.g. `BankAccount`
or `Student`) with attributes and methods, and create multiple objects from it.

---

## Phase 5 — Intermediate Python & Idioms (14)

**Goal:** Read and write the patterns that real-world Python code (and
every library you'll ever `import`) uses constantly.

- `14-intermediate-python` — comprehensions, lambda functions, `map()`/
  `filter()`, `*args`/`**kwargs`, `enumerate()`/`zip()`, unpacking,
  iterators, generators, decorators.

**Checkpoint:** You can read a comprehension, a decorator, or a generator
function in someone else's code and explain what it does — and choose when
writing one yourself actually improves readability over a plain loop.

---

## Phase 6 — Working with Data (15)

**Goal:** Exchange data with the outside world in the formats real
programs actually use.

- `15-working-with-data` — JSON, CSV, `datetime`, `pathlib`, and a "load →
  process → report" data-processing pattern.

**Checkpoint:** You can load a CSV or JSON file, compute a summary from
it, and save the result back out — using proper path handling instead of
fragile string concatenation.

---

## Phase 7 — Testing, Debugging & Version Control (16 – 17)

**Goal:** Work the way professional developers actually work: verify your
code systematically, and track its history properly.

- `16-testing-and-debugging` — a repeatable debugging process, reading
  tracebacks, assertions, `unittest`, and an introduction to `pytest`.
- `17-git-and-github` — `init`, `add`, `commit`, `status`, `log`,
  branching, merging, `push`/`pull`, and writing a good README.

**Checkpoint:** You can write a failing test, fix the code to make it
pass, and commit that fix to a Git repository with a clear message.

---

## Phase 8 — Real-World Project Setup (18)

**Goal:** Set up a Python project the way it's done outside of a single
tutorial script.

- `18-real-world-python` — virtual environments, `pip`, `requirements.txt`,
  project structure, configuration basics, and environment variables.

**Checkpoint:** You can start a brand-new project from scratch with an
isolated virtual environment, a `requirements.txt`, a sensible folder
layout, and secrets kept out of your code.

---

## Phase 9 — Projects (19)

**Goal:** Combine everything into projects you could show someone,
complete with automated tests.

- `19-projects/beginner-projects` — 2 small projects reinforcing `00`–`05`.
- `19-projects/intermediate-projects` — 3 projects reinforcing `06`–`11`.
- `19-projects/final-projects` — 2 capstone projects reinforcing
  everything through `13-oop`.

**Checkpoint:** You have working, tested, runnable projects in your own
GitHub account that you built and verified yourself, one milestone at a
time.

---

## Phase 10 — AI/ML Preparation (20, optional)

**Goal:** If AI/ML is where you're headed next, arrive already fluent in
the tools and vocabulary, so a future course can focus entirely on the
ideas.

- `20-ai-ml-preparation` — NumPy, pandas, matplotlib, Jupyter Notebook
  basics, the handful of math concepts that show up constantly in ML
  material, and the Python habits (vectorized thinking, `.fit()`/
  `.predict()`-style classes) that matter most.

**Checkpoint:** You can load tabular data with pandas, plot it with
matplotlib, and read an unfamiliar function call in ML-flavored code by
recognizing its parts, without needing new Python syntax to do so.

---

## After This Repo — Where To Go Next

Once you finish, you're ready to branch into any of:

- **AI / Machine Learning** — you're already prepared by `20-ai-ml-preparation`;
  a dedicated ML or deep learning course is the natural next step.
- **Web development** — Flask or Django.
- **Data science / analysis** — go deeper with pandas, NumPy, and Jupyter
  than this bridge topic covers.
- **Automation / scripting** — automating spreadsheets, files, the web.
- **Advanced testing** — deeper `pytest` (fixtures, mocking), continuous
  integration.
- **Advanced Git** — rebasing, pull request workflows, GitHub Actions.

There is no single "correct" next step — pick based on what excites you.
