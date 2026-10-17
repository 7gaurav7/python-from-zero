# Matplotlib Fundamentals

## Learning Objectives
By the end of this lesson you can:
- Explain what Matplotlib is used for
- Create a basic line plot and bar chart
- Add titles and axis labels to a chart
- Save a chart to an image file

## Concept Explanation

**Matplotlib** is Python's foundational plotting library — turning
numbers (often from a NumPy array or a pandas DataFrame) into a visual
chart. Every other Python plotting library you'll encounter later either
builds on Matplotlib or was designed as an alternative to it, so it's the
right place to start.

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])
plt.show()
```

`plt.show()` opens a window displaying the chart when run as a normal
script; inside a Jupyter Notebook (next lesson), charts typically display
automatically inline instead.

## Syntax

```python
import matplotlib.pyplot as plt      # "plt" is the near-universal convention

plt.plot(x_values, y_values)          # line plot
plt.bar(categories, values)            # bar chart
plt.scatter(x_values, y_values)        # scatter plot

plt.title("Chart Title")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.legend()                            # shows labels set via label= in plot calls

plt.show()                              # display the chart (interactive window)
plt.savefig("chart.png")                # save the chart to an image file instead
```

## Examples

**Example 1 — A basic line plot**
```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperatures = [15, 17, 16, 19, 21]

plt.plot(days, temperatures)
plt.title("Temperature Over 5 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.savefig("temperature_line.png")
print("Chart saved.")
```
Expected output:
```
Chart saved.
```
(and a file `temperature_line.png` is created showing an upward-trending
line)

**Example 2 — A bar chart**
```python
import matplotlib.pyplot as plt

categories = ["Food", "Transport", "Entertainment"]
amounts = [150, 60, 40]

plt.bar(categories, amounts)
plt.title("Spending by Category")
plt.ylabel("Amount ($)")
plt.savefig("spending_bar.png")
print("Chart saved.")
```
Expected output:
```
Chart saved.
```

**Example 3 — Multiple lines with a legend**
```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
city_a = [15, 17, 16, 19, 21]
city_b = [10, 11, 14, 13, 12]

plt.plot(days, city_a, label="City A")
plt.plot(days, city_b, label="City B")
plt.title("Temperature Comparison")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.legend()
plt.savefig("comparison_line.png")
print("Chart saved.")
```
Expected output:
```
Chart saved.
```

**Example 4 — Plotting directly from a pandas DataFrame**
```python
import pandas as pd
import matplotlib.pyplot as plt

data = {"category": ["Food", "Transport", "Fun"], "amount": [150, 60, 40]}
df = pd.DataFrame(data)

plt.bar(df["category"], df["amount"])
plt.title("Spending by Category (from a DataFrame)")
plt.savefig("df_spending_bar.png")
print("Chart saved.")
```
Expected output:
```
Chart saved.
```

## Common Mistakes

- **Forgetting `plt.show()` (or `plt.savefig()`)** — building a plot with
  `plt.plot()`/`plt.bar()` alone doesn't display or save anything by
  itself; you need one of these two calls at the end.
- **Building multiple unrelated charts without clearing between them** —
  by default, Matplotlib keeps adding to the same figure; call
  `plt.figure()` (or `plt.clf()`) before starting a new, separate chart if
  you don't want them combined.
- **Choosing the wrong chart type for the data** — a line plot implies a
  continuous, ordered relationship (like time); a bar chart suits discrete
  categories. Using a line plot for unrelated categories can visually
  imply a trend that doesn't actually exist.
- **Forgetting axis labels and a title** — a chart without them may be
  unreadable to anyone (including future you) without the original code
  in front of them.

## Practice

1. Create a line plot of 7 days' worth of made-up step counts, with a
   title and axis labels, saved to a file.
2. Create a bar chart comparing 4 categories of your choice.
3. Plot two lines on the same chart with a legend distinguishing them.
4. Load `15-working-with-data/sales.csv` with pandas and create a bar
   chart of total amount per category (combine this lesson with
   `02-pandas-fundamentals`'s `.groupby()`).

## Challenge

Using the `19-projects` **Expense Tracker**'s category totals (from
`total_by_category()`), create a bar chart showing spending by category,
saved as `expense_report.png` — connecting a project you already built to
a new visualization skill.

## Mini Project

Build a tiny "weekly report" script: given a week of daily values (steps,
sales, temperature — your choice), compute the average with plain Python
or NumPy, then produce and save both a line chart (the daily trend) and a
short printed summary sentence.

## Summary

Matplotlib turns numeric data (often from NumPy arrays or pandas
DataFrames) into line plots, bar charts, and more, with `plt.title()`,
`plt.xlabel()`/`plt.ylabel()`, and `plt.legend()` for readability, and
`plt.show()`/`plt.savefig()` to display or save the result.

## Next Step

Continue to [`04-jupyter-notebook-basics.md`](04-jupyter-notebook-basics.md).
