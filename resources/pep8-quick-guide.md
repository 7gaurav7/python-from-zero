# 🎨 PEP 8 Quick Guide

PEP 8 is Python's official style guide. This repository follows it, and
you should too — consistent style makes code easier for you (and others)
to read later. Here are the rules that matter most as a beginner.

## Naming
| Thing | Convention | Example |
|---|---|---|
| Variables | `snake_case` | `first_name`, `total_score` |
| Functions | `snake_case` | `calculate_total()` |
| Classes | `PascalCase` | `BankAccount`, `Student` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_ATTEMPTS = 3` |

## Indentation & Spacing
- Use **4 spaces** per indentation level. Never mix tabs and spaces.
- Put a single space around operators: `a + b`, not `a+b`.
- Put a space after commas: `func(a, b, c)`, not `func(a,b,c)`.
- No trailing whitespace at the end of lines.
- Two blank lines before top-level function/class definitions; one blank
  line between methods inside a class.

## Line Length
- Aim for lines under ~79–99 characters. If a line gets too long, break it
  across multiple lines using parentheses.

## Strings
- Prefer f-strings for building strings with variables:
  `f"{name} is {age}"`, not `name + " is " + str(age)`.
- Be consistent with quote style (`"` or `'`) within a project.

## Comments
- Use comments to explain **why**, not to restate **what** the code
  already shows.
- Keep comments up to date — an outdated comment is worse than none.
- A `#` comment should have a space after it: `# like this`, not `#like this`.

## Imports
- Put all `import` statements at the top of the file.
- One import per line: `import os` then `import sys`, not `import os, sys`.
- Avoid `from module import *` — it makes it unclear where a name came
  from.

## General Philosophy
PEP 8 itself says it best: **"Readability counts."** When in doubt, choose
whatever makes the code easiest for a human to understand later — including
future you.
