# 16 — Testing and Debugging

You've already been informally testing your code by running it and
looking at the output. This topic makes that process systematic:
understanding what actually happens when something goes wrong, and writing
automated tests so you (or anyone else) can verify your code keeps working
as you change it. In fact, you've already seen this in action — every
project in `19-projects` ships with a `tests/` folder using exactly the
tools this topic teaches.

**Prerequisite check:** `09-functions`, `11-exceptions`, and ideally
you've glanced at a `tests/test_*.py` file in `19-projects` already.

## Lessons in This Topic

| # | Lesson | What You'll Learn |
|---|---|---|
| 1 | [Debugging Fundamentals](01-debugging-fundamentals.md) | A systematic process for finding bugs |
| 2 | [Reading Tracebacks](02-reading-tracebacks.md) | Decode Python's error output confidently |
| 3 | [Assertions](03-assertions.md) | Check assumptions in your code with `assert` |
| 4 | [unittest Basics](04-unittest-basics.md) | Write automated tests with Python's built-in framework |
| 5 | [Introduction to pytest](05-pytest-introduction.md) | A simpler, widely-used third-party testing tool |

## Suggested Order

Follow the table top to bottom — `unittest` and `pytest` both build on the
mental model from debugging/tracebacks/assertions.

**Previous:** [`15-working-with-data`](../15-working-with-data/README.md) | **Next:** [`17-git-and-github`](../17-git-and-github/README.md)
