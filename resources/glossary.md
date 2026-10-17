# 📖 Glossary

Plain-language definitions of every term used in this course, in
alphabetical order.

- **Argument** — an actual value passed into a function when calling it
  (as opposed to a *parameter*, which is the placeholder name).
- **Assertion** — a statement (`assert condition`) that checks an
  assumption in your code and raises an `AssertionError` if it's false.
- **Attribute** — a piece of data stored on an object (e.g. `dog.name`).
- **Boolean (`bool`)** — a value that is either `True` or `False`.
- **Branch (Git)** — an independent line of development, letting you work
  on changes without affecting the main codebase until you're ready.
- **Class** — a blueprint for creating objects, defining their attributes
  and methods.
- **Clone (Git)** — downloading a full copy of a remote repository
  (history included) onto your own computer.
- **Comment** — text in code starting with `#`, ignored by Python, meant
  for human readers.
- **Commit (Git)** — a saved snapshot of your project's files at a point
  in time, with a message describing the change.
- **Comprehension** — a compact expression that builds a list, dictionary,
  or set from an iterable in one line, e.g. `[n * 2 for n in numbers]`.
- **Concatenation** — joining strings together, usually with `+`.
- **CSV** — "Comma-Separated Values"; a plain-text format for
  spreadsheet-style tabular data.
- **Decorator** — a function that wraps another function to add behavior
  around it, applied with `@decorator_name` syntax.
- **Dependency** — a third-party package your project needs in order to
  run, typically installed with `pip` and recorded in `requirements.txt`.
- **Dictionary (`dict`)** — a collection of key-value pairs.
- **Environment variable** — a named value stored outside your code (at
  the operating-system level), commonly used for configuration and
  secrets like API keys.
- **Exception** — an error that occurs while a program is running.
- **f-string** — a string prefixed with `f` that lets you embed variables
  directly inside it, e.g. `f"Hello, {name}"`.
- **Float (`float`)** — a number with a decimal point, e.g. `3.14`.
- **Function** — a named, reusable block of code that performs a task.
- **Generator** — a function that produces values one at a time using
  `yield`, instead of building and returning a full collection at once.
- **Immutable** — cannot be changed after creation (e.g. strings, tuples).
- **Indentation** — spaces at the start of a line that tell Python which
  lines belong to the same block of code.
- **Index** — the position of an item in an ordered collection, starting
  at `0`.
- **Inheritance** — when a class is based on another class, reusing and
  extending its behavior.
- **Instance** — a specific object created from a class (also called an
  "object").
- **Integer (`int`)** — a whole number, e.g. `5` or `-3`.
- **Interpreter** — the program that reads and runs your Python code.
- **Iterable** — anything you can loop over (lists, strings, dictionaries,
  files, and more).
- **Iteration** — one pass through a loop.
- **Iterator** — the object that actually produces values one at a time
  (via `next()`) when you loop over an iterable.
- **JSON** — "JavaScript Object Notation"; a plain-text data format that
  maps closely onto Python dictionaries and lists, commonly used by web
  APIs and configuration files.
- **Key** — the label used to look up a value in a dictionary.
- **Lambda** — a small, unnamed function written in a single expression,
  e.g. `lambda n: n * 2`.
- **List** — an ordered, changeable collection of values.
- **Loop** — a block of code that repeats.
- **Merge (Git)** — combining the changes from one branch into another.
- **Method** — a function that belongs to an object (defined inside a
  class).
- **Module** — a `.py` file whose code can be reused elsewhere via
  `import`.
- **Mutable** — can be changed after creation (e.g. lists, dictionaries,
  sets).
- **Object** — see "instance".
- **Operator** — a symbol that performs an action on values, e.g. `+`.
- **Package** — a folder containing related modules (also used loosely to
  mean a third-party library installed with `pip`).
- **Parameter** — a placeholder name in a function's definition.
- **PEP 8** — Python's official style guide, describing naming and
  formatting conventions.
- **pip** — Python's package installer, used to add third-party libraries
  to a project.
- **Pull Request (GitHub)** — a request to merge changes from one branch
  (often on a fork) into another, usually reviewed before merging.
- **Remote (Git)** — a copy of a repository hosted elsewhere (almost
  always GitHub in practice) that you can push to and pull from.
- **REPL** — "Read-Eval-Print Loop"; Python's interactive mode.
- **Repository (Git)** — a project folder tracked by Git, containing the
  full history of its changes.
- **requirements.txt** — a text file listing a project's dependencies
  (and usually their versions) so they can be installed all at once.
- **Return value** — the result a function sends back using `return`.
- **Scope** — where in a program a variable can be accessed (e.g. "local"
  to a function, or "global").
- **Set** — an unordered collection of unique values.
- **Slicing** — extracting a portion of a string, list, or tuple using
  `[start:stop]`.
- **String (`str`)** — text, always written in quotes.
- **Syntax** — the grammar rules of a programming language.
- **Traceback** — the block of text Python prints when an unhandled
  exception occurs, showing where and why it happened.
- **Truthy / Falsy** — a value that behaves like `True` or `False` in a
  condition, even if it isn't literally `True`/`False` (e.g. `0` is
  falsy, `1` is truthy).
- **Tuple** — an ordered, unchangeable collection of values.
- **Type** — the kind of value a variable holds (`int`, `str`, `bool`,
  etc.).
- **Unit test** — a small, automated test that checks one specific piece
  of behavior in isolation, typically written with `unittest` or `pytest`.
- **Unpacking** — assigning the elements of a sequence to multiple
  variables in one statement, e.g. `a, b = (1, 2)`.
- **Value** — the actual data stored, whether in a variable or a
  dictionary entry.
- **Variable** — a named reference to a stored value.
- **Virtual environment** — an isolated installation of Python and its
  packages for one specific project, so different projects' dependencies
  don't conflict with each other.
- **`*args`** — a parameter that collects any extra positional arguments
  into a tuple.
- **`**kwargs`** — a parameter that collects any extra keyword arguments
  into a dictionary.
