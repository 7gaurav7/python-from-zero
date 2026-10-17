# Configuration Basics

## Learning Objectives
By the end of this lesson you can:
- Explain why settings shouldn't be hard-coded directly into your logic
- Store configuration in a dedicated Python module or a config file
- Load a simple JSON/INI-style configuration at startup

## Concept Explanation

Throughout this course, values like a filename (`FILENAME = "contacts.txt"`)
have been defined near the top of a script — that's already a small step
toward **configuration**: separating "settings that might change" from
"the logic that uses them."

Real projects push this further: a project might need different settings
per environment (a test database vs. a production database), or a
non-programmer might need to tweak a setting without touching code.
**Configuration** is the general practice of keeping these values in one
clear, separate place instead of scattered through your logic.

## Syntax

**Option 1 — a plain Python config module** (simplest, good for most small
projects):
```python
# config.py
DATA_FILENAME = "contacts.txt"
MAX_CONTACTS = 1000
DEBUG = True
```
```python
# main.py
import config

print(config.DATA_FILENAME)
```

**Option 2 — a JSON config file** (good when non-programmers might edit
settings, or the config needs to change without a code deployment):
```json
{
  "data_filename": "contacts.txt",
  "max_contacts": 1000,
  "debug": true
}
```
```python
import json

with open("config.json") as file:
    config = json.load(file)

print(config["data_filename"])
```

## Examples

**Example 1 — A plain Python config module**
```python
# config.py
APP_NAME = "Contact Book"
DATA_FILE = "contacts.txt"
MAX_RESULTS = 50
```
```python
# main.py
import config

print(f"Welcome to {config.APP_NAME}")
print(f"Loading from {config.DATA_FILE}")
```
Expected output:
```
Welcome to Contact Book
Loading from contacts.txt
```

**Example 2 — Loading configuration from JSON**
```python
import json

with open("config.json", "w") as file:
    json.dump({"app_name": "Contact Book", "max_results": 50}, file)

with open("config.json", "r") as file:
    config = json.load(file)

print(config["app_name"])
print(config["max_results"])
```
Expected output:
```
Contact Book
50
```

**Example 3 — Providing sensible defaults if a setting is missing**
```python
import json

settings = {"app_name": "Contact Book"}   # "max_results" was never set

max_results = settings.get("max_results", 100)   # falls back to 100
print(max_results)
```
Expected output:
```
100
```

**Example 4 — Different configuration per environment**
```python
# config.py
import os

ENVIRONMENT = os.environ.get("APP_ENV", "development")

if ENVIRONMENT == "production":
    DATA_FILE = "prod_contacts.txt"
    DEBUG = False
else:
    DATA_FILE = "dev_contacts.txt"
    DEBUG = True

print(f"Running in {ENVIRONMENT} mode, using {DATA_FILE}")
```
Sample output (when `APP_ENV` isn't set):
```
Running in development mode, using dev_contacts.txt
```
(This uses `os.environ`, covered fully in the next lesson.)

## Common Mistakes

- **Hard-coding values that should be configurable** deep inside unrelated
  functions — makes them hard to find and easy to forget when something
  needs to change.
- **Putting secrets (passwords, API keys) directly into a config file that
  gets committed to Git** — see the next lesson, environment variables, for
  the correct way to handle these.
- **Over-engineering configuration for a tiny script** — a two-line
  `config.py` (or even just constants at the top of `main.py`) is entirely
  sufficient for most small projects; don't build an elaborate
  configuration system you don't need yet.
- **Not providing sensible defaults** for optional settings — a missing
  config value should ideally fall back to something reasonable rather
  than crashing the whole program.

## Practice

1. Create a `config.py` with at least 3 settings for one of your
   `19-projects` projects (e.g. filename, max items, app name), and import
   it from the main script.
2. Rewrite that same configuration as a `config.json` file instead, and
   load it with `json.load()`.
3. Use `.get()` with a default value to handle a setting that might be
   missing from a JSON config.
4. Explain in a comment why the plain-Python approach and the JSON
   approach each have their place — when would you pick one over the
   other?

## Challenge

Add a `config.py` to the `19-projects` **Expense Tracker** project holding
its `FILENAME` constant and a new `CURRENCY_SYMBOL` setting, then update
the solution to display amounts with that configurable currency symbol
instead of a hard-coded `$`.

## Mini Project

No dedicated mini project — the Challenge above is this lesson's hands-on
application.

## Summary

Configuration means keeping "settings that might change" — filenames,
limits, feature flags — separate from your program's logic, whether as a
plain Python module or a JSON/INI file. This makes a project easier to
adjust, reuse, and understand at a glance. Secrets specifically need one
more layer of care, covered next.

## Next Step

Continue to [`06-environment-variables.md`](06-environment-variables.md).
