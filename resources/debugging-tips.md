# 🐛 Debugging Tips for Beginners

Every programmer, no matter how experienced, spends a lot of time fixing
bugs. Getting comfortable reading error messages is one of the most
valuable early skills you can build.

## How to Read a Python Error (Traceback)

```
Traceback (most recent call last):
  File "hello.py", line 3, in <module>
    print(age + 1)
NameError: name 'age' is not defined
```

Read it **bottom to top**:
1. The **last line** tells you the type of error and what went wrong:
   `NameError: name 'age' is not defined`.
2. The lines above it show **where** it happened — the file and line
   number (`hello.py`, line 3).
3. Ignore the middle noise if the traceback is long; the top of the error
   message and the bottom line are what matter most as a beginner.

## Common Errors and What They Mean

| Error | Usual Cause |
|---|---|
| `SyntaxError` | Something violates Python's grammar rules — missing `:`, mismatched parentheses/quotes, etc. |
| `IndentationError` | Inconsistent spacing at the start of lines. |
| `NameError` | Using a variable or function that hasn't been defined (often a typo). |
| `TypeError` | Using an operation on the wrong type, e.g. adding a `str` and an `int`. |
| `ValueError` | The right type, but an invalid value, e.g. `int("abc")`. |
| `IndexError` | Trying to access a list index that doesn't exist. |
| `KeyError` | Trying to access a dictionary key that doesn't exist. |
| `ZeroDivisionError` | Dividing by zero. |
| `FileNotFoundError` | Trying to open a file that doesn't exist at that path. |
| `AttributeError` | Calling a method/attribute that doesn't exist on that object. |

## Debugging Strategies

1. **Read the error message fully** before assuming you know what's wrong.
2. **Add `print()` statements** at key points to see what values variables
   actually hold at that moment — this is the single most useful beginner
   debugging technique.
3. **Isolate the problem** — comment out or temporarily remove code until
   you narrow down exactly which line causes the issue.
4. **Check your indentation** — a huge fraction of early bugs come from
   inconsistent spacing.
5. **Re-read your own code out loud** — explaining it to yourself (or
   literally to a rubber duck — this is a real, named technique called
   "rubber duck debugging") often reveals the mistake.
6. **Search the exact error message** online — chances are someone else
   hit the same error; just make sure you understand *why* a fix works
   before copying it.
7. **Take a short break** if you're stuck and frustrated — a fresh look
   after 10 minutes away often reveals what you were missing.

## A Golden Rule

Bugs are not a sign you're bad at programming — they're the normal, daily
experience of every programmer, including senior engineers with decades of
experience. The skill that improves with practice isn't "not making
mistakes" — it's getting faster at finding and fixing them.

## Want More?

This page covers the essentials you'll want from day one. For a full
lesson on a systematic debugging process, reading tracebacks in depth, and
writing automated tests (`assert`, `unittest`, `pytest`) so bugs get
caught before they reach you, see
[`16-testing-and-debugging`](../16-testing-and-debugging/README.md).
