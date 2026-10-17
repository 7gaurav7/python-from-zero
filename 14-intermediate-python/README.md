# 14 — Intermediate Python

You've built a solid foundation (`00`-`13`). This topic introduces idioms
experienced Python developers reach for constantly — code that reads
shorter and clearer once you know the patterns. Real-world Python code
(including any library you'll ever `import`) uses these patterns
everywhere, so you need to read them fluently even where you'd choose the
plainer version yourself.

**Prerequisite check:** functions (`09-functions`), loops (`05-loops`),
and the core data structures (`07-lists-tuples-sets`, `08-dictionaries`).

## Lessons in This Topic

| # | Lesson | What You'll Learn |
|---|---|---|
| 1 | [Comprehensions](01-comprehensions.md) | Build lists/dicts/sets in one readable line |
| 2 | [Lambda Functions](02-lambda-functions.md) | Small, unnamed functions for one-off use |
| 3 | [map() and filter()](03-map-and-filter.md) | Apply a function across a collection |
| 4 | [*args and **kwargs](04-args-and-kwargs.md) | Functions accepting a flexible number of arguments |
| 5 | [enumerate() and zip()](05-enumerate-and-zip.md) | Loop with indexes, and over multiple lists together |
| 6 | [Unpacking](06-unpacking.md) | Assign multiple variables from a sequence at once |
| 7 | [Iterators](07-iterators.md) | What actually powers every `for` loop |
| 8 | [Generators](08-generators.md) | Produce values lazily, one at a time |
| 9 | [Decorators](09-decorators.md) | Wrap a function to add behavior without changing its code |

## Suggested Order
Follow the table top to bottom — generators lean on iterators; decorators
lean on `*args`/`**kwargs`.

Exercises: [`exercises/14_intermediate_python_exercises.py`](../exercises/14_intermediate_python_exercises.py) ·
Solutions: [`solutions/14_intermediate_python_solutions.py`](../solutions/14_intermediate_python_solutions.py)

**Previous:** [`13-oop`](../13-oop/README.md) | **Next:** [`15-working-with-data`](../15-working-with-data/README.md)
