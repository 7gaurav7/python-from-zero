# Pandas Fundamentals

## Learning Objectives
By the end of this lesson you can:
- Explain what a pandas DataFrame is and how it relates to a spreadsheet
- Create a DataFrame from a dictionary or load one from a CSV file
- Select columns, filter rows, and compute summary statistics
- Group and aggregate data with `.groupby()`

## Concept Explanation

**pandas** is the standard library for working with tabular data in
Python — think of it as "a spreadsheet, but in code," built on top of
NumPy. Its core object is the **DataFrame**: rows and named columns, very
similar in spirit to the CSV files from `15-working-with-data`, but with
far more built-in power for filtering, transforming, and summarizing.

If you completed `15-working-with-data`'s `05-basic-data-processing`
lesson, you've already written, by hand, exactly what pandas automates:
loading rows, grouping by a field, and computing totals.

```python
import pandas as pd

data = {"name": ["Alice", "Bob"], "score": [90, 75]}
df = pd.DataFrame(data)
```

## Syntax

```python
import pandas as pd                  # "pd" is the near-universal convention

pd.DataFrame(dict_of_lists)           # build a DataFrame from a dictionary
pd.read_csv("file.csv")                # load a DataFrame directly from CSV

df.head()                              # first 5 rows
df["column_name"]                       # select one column (a Series)
df[["col1", "col2"]]                    # select multiple columns

df[df["column_name"] > value]           # filter rows by a condition

df["column_name"].sum()                 # sum a column
df["column_name"].mean()                # average a column
df.describe()                            # quick summary statistics for every numeric column

df.groupby("column_name")["other_column"].sum()   # group and aggregate
```

## Examples

**Example 1 — Creating a DataFrame**
```python
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Carla"],
    "score": [90, 75, 88],
}
df = pd.DataFrame(data)
print(df)
```
Expected output:
```
    name  score
0  Alice     90
1    Bob     75
2  Carla     88
```

**Example 2 — Selecting and filtering**
```python
print(df["name"])
print(df[df["score"] >= 85])
```
Expected output:
```
0    Alice
1      Bob
2    Carla
Name: name, dtype: object
    name  score
0  Alice     90
2  Carla     88
```
(Depending on your installed pandas version, the last line of the first
result may instead read `dtype: str` — pandas changed how it labels text
columns starting with version 3.0. Either way, the actual values shown are
identical.)

**Example 3 — Summary statistics**
```python
print(df["score"].mean())
print(df["score"].max())
print(df.describe())
```
Expected output:
```
84.33333333333333
90
           score
count   3.000000
mean   84.333333
std     8.144528
min    75.000000
25%    81.500000
50%    88.000000
75%    89.000000
max    90.000000
```
(`std` is the standard deviation — a measure of spread covered in
`05-math-foundations-for-ml`.)

**Example 4 — Grouping and aggregating**
```python
data = {
    "category": ["Food", "Food", "Transport", "Transport"],
    "amount": [20, 15, 50, 10],
}
expenses = pd.DataFrame(data)
totals = expenses.groupby("category")["amount"].sum()
print(totals)
```
Expected output:
```
category
Food         35
Transport    60
Name: amount, dtype: int64
```

## Common Mistakes

- **Confusing a DataFrame (2D, many columns) with a Series (1D, one
  column)** — `df["score"]` is a Series; `df[["score"]]` (double brackets)
  is a one-column DataFrame. They behave slightly differently.
- **Forgetting `pd.read_csv()` already handles what you built by hand in
  `15-working-with-data`** — column typing, header detection, and more —
  so there's usually no need to write your own CSV parsing once pandas is
  available.
- **Trying to filter with plain Python `and`/`or`** inside a DataFrame
  condition — pandas requires `&`/`|` (with parentheses around each
  condition) for combining filters:
  `df[(df["score"] > 50) & (df["age"] < 30)]`.
- **Not checking `.head()` or `.describe()` first** on unfamiliar data —
  a huge amount of real-world data work is simply understanding what
  you're looking at before doing anything else with it.

## Practice

1. Build a DataFrame of 4 students with `name` and `score` columns, then
   print only the students who scored above 80.
2. Load `15-working-with-data/sales.csv` with `pd.read_csv()` and print
   its `.describe()`.
3. Using that same sales data, group by `category` and print the total
   `amount` per category with `.groupby()`.
4. Add a new column to a DataFrame (e.g. a `passed` column computed from
   an existing `score` column being `>= 60`).

## Challenge

Load `15-working-with-data/sales.csv` with pandas and reproduce every
result from that topic's `05-basic-data-processing` lesson (total sales,
totals by category, and the top sale) using pandas methods instead of
manual loops — then compare how much shorter the code is.

## Mini Project

Build a small "class performance" analysis: create a DataFrame from the
`19-projects` **Student Management System**'s saved `students.txt` data
(you'll need to parse it into a dictionary of lists first, or export it as
CSV/JSON using ideas from `15-working-with-data`), then use pandas to
compute the class average and identify the top 3 students.

## Summary

pandas' DataFrame represents tabular data — rows and named columns — with
powerful, concise operations for selecting, filtering, summarizing
(`.describe()`), and grouping (`.groupby()`) data. Much of what you
practiced manually in `15-working-with-data` is exactly what pandas
automates at scale.

## Next Step

Continue to [`03-matplotlib-fundamentals.md`](03-matplotlib-fundamentals.md).
