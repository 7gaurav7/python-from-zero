# 20 — AI/ML Preparation

This topic is a **bridge**, not a machine learning course. Its only goal
is to make sure that when you do start learning AI/ML — with a dedicated
course, book, or bootcamp — the *Python* isn't what slows you down. Every
ML tutorial you'll ever follow assumes fluency with the libraries and
habits covered here.

**This topic deliberately does NOT teach machine learning concepts**
(no models, no training, no algorithms) — only the Python foundations that
sit underneath any ML work: array/table manipulation, plotting, and the
handful of math ideas that show up constantly once you get there.

**Prerequisite check:** `14-intermediate-python` (comprehensions, in
particular, show up everywhere in this style of code) and
`15-working-with-data` (this topic is a direct continuation of it, using
specialized libraries instead of the standard library alone).

## Lessons in This Topic

| # | Lesson | What You'll Learn |
|---|---|---|
| 1 | [NumPy Fundamentals](01-numpy-fundamentals.md) | Fast, array-based numerical computing |
| 2 | [Pandas Fundamentals](02-pandas-fundamentals.md) | Table-shaped data (like a spreadsheet, in code) |
| 3 | [Matplotlib Fundamentals](03-matplotlib-fundamentals.md) | Turning data into charts |
| 4 | [Jupyter Notebook Basics](04-jupyter-notebook-basics.md) | The interactive, cell-based environment most ML work happens in |
| 5 | [Math Foundations for ML](05-math-foundations-for-ml.md) | The handful of math ideas (vectors, mean/variance, linear equations) worth knowing before ML |
| 6 | [Python Habits That Matter for AI/ML](06-python-habits-for-ai-ml.md) | The parts of this course that get used constantly in ML code |

## Setup Note

NumPy, pandas, and Matplotlib are third-party packages — install them
inside a virtual environment (see `18-real-world-python`) with:
```
pip install numpy pandas matplotlib jupyter
```

## Suggested Order

Follow the table top to bottom. Lesson 6 is a deliberate look back at this
entire course, connecting what you already know to what's coming next.

**Previous:** [`19-projects`](../19-projects/README.md) — this topic is the
natural finishing point of this repository.
