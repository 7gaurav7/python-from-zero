# Jupyter Notebook Basics

## Learning Objectives
By the end of this lesson you can:
- Explain what a Jupyter Notebook is and how it differs from a `.py` script
- Install and launch Jupyter
- Understand cells, execution order, and the kernel
- Know when a notebook is (and isn't) the right tool

## Concept Explanation

Every lesson in this course has run as a `.py` script: write code, run the
whole file, read the output. A **Jupyter Notebook** (`.ipynb` file) works
differently — it's a document made of **cells**, each one independently
runnable, mixing code, its output, and formatted text (explanations,
headers, even images) in one place.

This interactive, "run one small piece, see the result immediately, run
the next piece" style is why almost all data science and ML work — the
world you're now bridging into — happens in notebooks rather than plain
scripts: you're constantly inspecting data, tweaking one step, and
re-running just that step, not the entire program from scratch.

## Syntax

```
pip install jupyter          # install (inside a virtual environment)
jupyter notebook               # launch the classic interface in your browser
jupyter lab                    # launch the newer "JupyterLab" interface
```

Inside a notebook:
- A **code cell** runs Python — press `Shift+Enter` to run it and move to
  the next cell.
- A **Markdown cell** holds formatted text (headers, lists, links) instead
  of code — this course's own `.md` lesson files use exactly the same
  Markdown syntax.
- The **kernel** is the running Python process behind the notebook — it
  holds all the variables you've defined so far, across cells.

## Examples

**Example 1 — A notebook's first few cells (shown as they'd appear)**

Cell 1 (code):
```python
x = 10
y = 20
```
Cell 2 (code, run after Cell 1):
```python
print(x + y)
```
Output shown directly beneath Cell 2:
```
30
```

**Example 2 — Cells share state (this is the key notebook behavior)**
```python
# Cell 1
numbers = [1, 2, 3, 4, 5]
```
```python
# Cell 2 (run later -- still sees `numbers` from Cell 1)
print(sum(numbers))
```
Output:
```
15
```

**Example 3 — Mixing Markdown and code**

A Markdown cell:
```markdown
## Step 1: Load the data
```
Followed by a code cell:
```python
import pandas as pd
df = pd.DataFrame({"score": [90, 85, 78]})
df
```
In a notebook, simply writing `df` as the last line of a cell (no
`print()` needed) displays it as a nicely formatted table — a
notebook-specific convenience you won't see in a plain script.

**Example 4 — Why execution order matters**
```python
# Cell 1
total = 100
```
```python
# Cell 2
print(total)
```
```python
# Cell 3 (imagine you go back and re-run Cell 1 with a new value)
total = 999
```
If you only re-run Cell 3 and not Cell 2, Cell 2's *displayed* output
still shows the old value until you re-run Cell 2 too — the notebook
shows whatever was true the last time each cell ran, not necessarily the
current state. This is the single most common source of notebook
confusion.

## Common Mistakes

- **Running cells out of order and getting confused by stale output** —
  as shown in Example 4; when in doubt, use the "Restart Kernel and Run
  All" option to confirm your notebook works correctly top-to-bottom.
- **Writing a huge, sprawling notebook instead of extracting reusable
  logic into a proper module** (see `18-real-world-python`'s project
  structure lesson) — notebooks are excellent for exploration, but code
  meant to be reused or tested usually belongs in a `.py` file that the
  notebook then imports.
- **Forgetting the kernel keeps old variables around** even after you
  delete or change the cell that created them — restarting the kernel
  clears everything, which is often the fastest fix for "why is this
  behaving strangely?"
- **Committing a notebook with large outputs (like embedded images) to
  Git** without realizing it — this can make repositories unexpectedly
  large; "Clear All Outputs" before committing is a common habit.

## Practice

1. Install Jupyter and launch it, creating a new, empty notebook.
2. Create three cells: one that defines a list, one that computes its sum,
   and a Markdown cell explaining what the code does — run them in order.
3. Deliberately create the "stale output" confusion from Example 4, then
   fix it with "Restart Kernel and Run All."
4. Load `15-working-with-data/sales.csv` into a pandas DataFrame inside a
   notebook cell, and display it by writing the DataFrame's variable name
   alone as the cell's last line (no `print()`).

## Challenge

Recreate one of the `20-ai-ml-preparation` Matplotlib examples inside a
notebook instead of a script, and observe that the chart displays inline
automatically (no `plt.savefig()` needed, though it still works if you
want a saved file too).

## Mini Project

Turn the `15-working-with-data` **Basic Data Processing** mini project
(the Sales Report Generator) into a notebook: one Markdown cell per step
(load data, compute totals, group by category, visualize), interleaved
with the corresponding code cells — a realistic small taste of how
exploratory data analysis is actually done.

## Summary

Jupyter Notebooks organize code into independently runnable cells that
share state through a persistent kernel, mixed with Markdown text —
ideal for the exploratory, iterative style of data science and ML work.
Execution order (not just the order cells appear on the page) determines
what a notebook actually does, which is the most important habit to get
right early.

## Next Step

Continue to [`05-math-foundations-for-ml.md`](05-math-foundations-for-ml.md).
