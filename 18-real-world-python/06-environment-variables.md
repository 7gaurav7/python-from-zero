# Environment Variables

## Learning Objectives
By the end of this lesson you can:
- Explain what an environment variable is and why secrets belong there,
  not in your code
- Read an environment variable from Python with `os.environ`
- Provide a safe default when a variable isn't set
- Understand the role of a `.env` file and why it's excluded from Git

## Concept Explanation

Some configuration values are **secrets** — API keys, passwords, database
credentials — that must never be hard-coded into a file that gets
committed to Git (remember: anything pushed to a public GitHub repository
should be treated as permanently public, even after later deletion).

**Environment variables** are values stored outside your code, at the
operating-system level, that your program can read at runtime. They're
the standard way to supply secrets and per-environment settings (like "am
I running in development or production?") without ever writing them into
a file that gets committed.

```python
import os

api_key = os.environ.get("MY_API_KEY")
```

## Syntax

Setting an environment variable in your terminal (temporary, current
session only):
```
export MY_API_KEY=abc123          # macOS/Linux
set MY_API_KEY=abc123               # Windows (cmd)
$env:MY_API_KEY = "abc123"          # Windows (PowerShell)
```

Reading it in Python:
```python
import os

os.environ.get("MY_API_KEY")                  # None if not set
os.environ.get("MY_API_KEY", "default_value")  # a fallback if not set
os.environ["MY_API_KEY"]                        # raises KeyError if not set
```

A `.env` file (used with the third-party `python-dotenv` package — install
with `pip install python-dotenv`) lets you define variables in a file for
local development, without setting them manually every session:
```
# .env  (never commit this file -- add it to .gitignore!)
MY_API_KEY=abc123
DEBUG=True
```
```python
from dotenv import load_dotenv
import os

load_dotenv()   # reads .env and loads it into os.environ
api_key = os.environ.get("MY_API_KEY")
```

## Examples

**Example 1 — Reading an environment variable with a default**
```python
import os

debug_mode = os.environ.get("DEBUG", "False")
print(f"Debug mode: {debug_mode}")
```
Sample output (if `DEBUG` isn't set in your terminal):
```
Debug mode: False
```

**Example 2 — Setting a variable, then reading it (same terminal session)**
```
$ export FAVORITE_LANGUAGE=Python
$ python3 -c "import os; print(os.environ.get('FAVORITE_LANGUAGE'))"
Python
```

**Example 3 — Using an environment variable to choose behavior**
```python
import os

environment = os.environ.get("APP_ENV", "development")

if environment == "production":
    print("Running with production settings.")
else:
    print("Running with development settings.")
```
Sample output (when `APP_ENV` is unset):
```
Running with development settings.
```

**Example 4 — A `.env` file with `python-dotenv` (requires
`pip install python-dotenv`)**
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("SECRET_API_KEY", "not set")
print(f"API key loaded: {api_key != 'not set'}")
```
Sample output (with a `.env` file containing `SECRET_API_KEY=xyz`):
```
API key loaded: True
```

## Common Mistakes

- **Hard-coding a secret directly in a `.py` file** and committing it —
  even a "quick test," since Git remembers it in history forever, even if
  you delete the line later. If this happens, the correct fix is to
  rotate/regenerate the secret, not just remove the line.
- **Forgetting to add `.env` to `.gitignore`** — defeats the entire
  purpose; double-check it's listed before your first commit involving
  secrets.
- **Using `os.environ["KEY"]` (raises `KeyError` if missing) when you meant
  `os.environ.get("KEY", default)`** — decide deliberately whether a
  missing variable should crash your program (because it's required) or
  fall back to a sensible default (because it's optional).
- **Committing a `.env.example` with real secrets instead of placeholders**
  — a template file showing *which* variables are needed (with fake
  placeholder values) is fine and often helpful to commit; the actual
  `.env` with real values never should be.

## Practice

1. Set an environment variable in your terminal and read it from a Python
   script using `os.environ.get()`.
2. Read a variable that you know isn't set, using `.get()` with a default
   value, and confirm the default is returned.
3. Create a `.env` file (add it to `.gitignore` first!), install
   `python-dotenv`, and load a value from it with `load_dotenv()`.
4. Write a `.env.example` file with placeholder values (e.g.
   `API_KEY=your-api-key-here`) suitable for committing to Git, alongside
   a real `.env` (not committed) with actual values.

## Challenge

Update the `19-projects` **Expense Tracker**'s configuration (from the
previous lesson's Challenge) so the data filename can be overridden by an
`EXPENSE_TRACKER_FILE` environment variable, falling back to the original
default filename when that variable isn't set.

## Mini Project

No dedicated mini project — the Challenge above is this lesson's hands-on
application, and completes the practical setup skills in this topic.

## Summary

Environment variables store configuration (especially secrets) outside
your code, read at runtime with `os.environ.get()`. A `.env` file (loaded
with `python-dotenv`) makes this convenient for local development but must
always be excluded from Git via `.gitignore` — never commit real secrets,
and if one is ever accidentally committed, rotate it rather than just
deleting the line.

## Next Step

You've completed `18-real-world-python` — and with it, every non-project
topic in this course. Continue to
[`19-projects`](../19-projects/README.md) to apply everything, or to
[`20-ai-ml-preparation`](../20-ai-ml-preparation/README.md) if you're
ready to look toward data science and machine learning next.
