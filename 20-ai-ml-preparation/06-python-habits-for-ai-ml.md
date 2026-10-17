# Python Habits That Matter for AI/ML

## Learning Objectives
By the end of this lesson you can:
- Identify which parts of this entire course show up constantly in
  real-world ML code
- Explain why comprehensions, unpacking, and `*args`/`**kwargs` are
  especially common in ML libraries
- Feel confident that you are genuinely ready to begin a dedicated AI/ML
  course

## Concept Explanation

This final lesson doesn't introduce anything new — it's a deliberate look
back at this repository, connecting the dots between what you've already
learned and what you'll see constantly once you start an ML-focused
course or tutorial. If you've worked through this repository from
`00-getting-started` onward, **you are ready**. This lesson is here to
make that visible.

**From `14-intermediate-python`:**
- **Comprehensions** appear everywhere in data preparation code:
  `[row for row in data if row["valid"]]` is a completely ordinary sight.
- **Unpacking** shows up whenever a library function returns multiple
  values, e.g. `train_data, test_data = split_dataset(data)` — a pattern
  you'll meet in literally the first hour of any ML course, for splitting
  data into a portion to train a model and a portion to check it against.
- **`*args`/`**kwargs`** are how flexible library functions (model
  constructors, plotting functions) accept dozens of optional settings
  without forcing you to specify all of them.
- **Lambda + `map`/`filter`**, and especially **`key=` sorting**, appear
  constantly when ranking or filtering results (e.g. sorting model
  predictions by confidence score).

**From `13-oop`:**
- Every ML model you'll use (in scikit-learn, PyTorch, or elsewhere) is an
  **object** you create, configure via `__init__`, then call methods on
  (commonly `.fit()` to train it, `.predict()` to use it) — exactly the
  class/object pattern from `13-oop`, just with different method names.

**From `11-exceptions` and `16-testing-and-debugging`:**
- Real data is messy. Missing values, malformed rows, and unexpected types
  are the norm, not the exception — the defensive habits from
  `11-exceptions` (and reading tracebacks from `16-testing-and-debugging`)
  are used constantly while cleaning data.

**From `15-working-with-data` and this topic:**
- Loading, cleaning, grouping, and summarizing data (CSV/JSON, pandas) is
  often the majority of the actual work in any real ML project — the
  "modeling" part you'll learn later is frequently a smaller piece than
  people expect.

## Syntax

No new syntax — this is a review. If any of the snippets below don't feel
immediately familiar, that's a good signal for exactly which earlier
lesson is worth a quick revisit before moving on.

```python
# Unpacking a function's multiple return values (14-intermediate-python)
train_data, test_data = split_dataset(data)

# A comprehension filtering rows (14-intermediate-python)
valid_rows = [row for row in data if row["value"] is not None]

# The object/method pattern every ML model follows (13-oop)
model = SomeModel(setting_one=10, setting_two="auto")
model.fit(training_data)
predictions = model.predict(new_data)

# Defensive handling of messy real-world data (11-exceptions)
try:
    value = float(raw_value)
except ValueError:
    value = None   # a common way to mark "couldn't parse this one"
```

## Examples

**Example 1 — A believable "before you learn ML" data-cleaning snippet**
```python
raw_rows = [
    {"age": "25", "score": "90"},
    {"age": "N/A", "score": "78"},
    {"age": "31", "score": "not recorded"},
]

def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None

cleaned = [
    {"age": safe_float(row["age"]), "score": safe_float(row["score"])}
    for row in raw_rows
]
print(cleaned)
```
Expected output:
```
[{'age': 25.0, 'score': 90.0}, {'age': None, 'score': 78.0}, {'age': 31.0, 'score': None}]
```
This one snippet uses a comprehension, a `try`/`except`, and a
function — three separate lessons from this course, combined naturally.

**Example 2 — Splitting data, using unpacking (the shape of every ML tutorial's first step)**
```python
def split_dataset(data, train_ratio=0.8):
    split_point = int(len(data) * train_ratio)
    return data[:split_point], data[split_point:]

all_data = list(range(10))
train_data, test_data = split_dataset(all_data)
print(train_data)
print(test_data)
```
Expected output:
```
[0, 1, 2, 3, 4, 5, 6, 7]
[8, 9]
```

**Example 3 — The object/method pattern, using a class you could write
yourself right now**
```python
class SimpleAverager:
    def __init__(self):
        self.values = []

    def fit(self, data):
        self.values = data

    def predict(self):
        return sum(self.values) / len(self.values)

model = SimpleAverager()
model.fit([10, 20, 30])
print(model.predict())
```
Expected output:
```
20.0
```
This is a deliberately simplified stand-in — but the *shape* (create an
object, `.fit()` it to data, then call it to get a result) is exactly the
shape of `model = LinearRegression(); model.fit(X, y);
model.predict(new_X)` in a real ML library you'll meet soon.

**Example 4 — Ranking results with `key=`, as you'll do with model output**
```python
predictions = [
    {"label": "cat", "confidence": 0.72},
    {"label": "dog", "confidence": 0.95},
    {"label": "bird", "confidence": 0.41},
]

ranked = sorted(predictions, key=lambda p: p["confidence"], reverse=True)
for prediction in ranked:
    print(prediction["label"], prediction["confidence"])
```
Expected output:
```
dog 0.95
cat 0.72
bird 0.41
```

## Common Mistakes

- **Believing you need to "master" NumPy/pandas before starting ML** —
  fluency builds naturally through use; what actually matters is not being
  blocked by unfamiliar *Python* syntax while you're trying to focus on
  new ML *concepts*. This course has already covered that syntax.
- **Skipping the fundamentals to rush toward ML** — every mistake pattern
  called out across `00`–`19` (off-by-one errors, mutable default
  arguments, un-handled exceptions) shows up just as often in ML code as
  anywhere else; the fundamentals don't become optional.
- **Assuming ML is mostly about complex math** — as noted in the previous
  lesson, a large fraction of real ML work is the data loading/cleaning
  skills from `15-working-with-data` and this topic.

## Practice

1. Rewrite Example 1's `cleaned` comprehension as a plain `for` loop, then
   compare which version you find more readable — both are correct.
2. Write your own `split_dataset()`-style function for a different ratio
   (e.g. 70/30) and confirm it via unpacking, as in Example 2.
3. Write a second tiny class following the `.fit()`/`.predict()` shape
   from Example 3 — e.g. a `SimpleMaxFinder` that "predicts" the maximum
   value it was fit on.
4. Extend Example 4 to also filter out any prediction below a confidence
   threshold of 0.5 before ranking (combine `filter()`/a comprehension
   with the `sorted()` call).

## Challenge

Combine everything from this lesson into one realistic script: take the
raw, messy list of dictionaries from Example 1, clean it, split it 80/20
using Example 2's function, and print both resulting parts — a compact
rehearsal of the exact first few steps of almost any ML tutorial you're
about to encounter.

## Mini Project

Write a short personal note to yourself (a `NEXT_STEPS.md` file, if you'd
like) listing: which lessons in this repository you feel most confident
in, which you'd want to revisit before an ML course, and which ML topic
you're most excited to learn next. This isn't Python practice — it's the
honest self-assessment that makes the transition into a dedicated ML
course far more effective.

## Summary

Nothing in AI/ML is going to ask you to abandon what you've learned in
this course — comprehensions, unpacking, `*args`/`**kwargs`, OOP,
exception handling, and data processing are used constantly, just applied
to new libraries and new problems. You've built the right foundation.
Where you go from here — scikit-learn, PyTorch, TensorFlow, or a
structured ML course — is a choice about *which* ML tools to learn next,
not whether you're ready to learn them.

## Next Step

This is the final lesson in **Python From Zero**. Revisit
[`19-projects`](../19-projects/README.md) if you haven't completed every
tier yet, or the main [`README.md`](../README.md) for the full roadmap and
what to explore next.
