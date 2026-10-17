# pip and Installing Packages

## Learning Objectives
By the end of this lesson you can:
- Explain what `pip` is and where packages come from
- Install, list, upgrade, and uninstall packages
- Install a specific version of a package
- Understand what happens when you `import` a package you installed

## Concept Explanation

Everything you've built so far uses only Python's **standard library** —
the modules that ship with Python itself (`math`, `random`, `csv`,
`datetime`, and so on). But the Python community publishes hundreds of
thousands of additional **packages** on the **Python Package Index**
(PyPI, at pypi.org) — for everything from web frameworks to data science
to talking to specific web APIs.

`pip` is the tool that downloads and installs these packages. It comes
bundled with Python, so if you have Python you already have `pip`.

```
pip install requests
```
downloads the `requests` package (a very popular tool for making web
requests) from PyPI, and afterward you can `import requests` in your code
exactly like any standard-library module.

**Always activate your virtual environment (previous lesson) before
running `pip install`**, so the package installs into that project's
isolated environment, not system-wide.

## Syntax

```
pip install <package-name>              # install the latest version
pip install <package-name>==1.2.3       # install a specific version
pip install --upgrade <package-name>     # upgrade to the latest version
pip uninstall <package-name>             # remove a package
pip list                                  # list installed packages
pip show <package-name>                  # show details about one package
```

## Examples

**Example 1 — Installing a package**
```
(venv) $ pip install requests
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
...
Successfully installed requests-2.31.0
```

**Example 2 — Using an installed package**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```
Sample output:
```
200
```
(This requires an internet connection and the `requests` package actually
installed — this course otherwise avoids external dependencies, but this
is exactly what installing and using a real package looks like.)

**Example 3 — Installing a specific version**
```
(venv) $ pip install requests==2.28.0
(venv) $ pip show requests
Name: requests
Version: 2.28.0
...
```

**Example 4 — Listing and uninstalling**
```
(venv) $ pip list
Package         Version
--------------- -------
pip             24.0
requests        2.28.0

(venv) $ pip uninstall requests
Found existing installation: requests 2.28.0
Uninstalling requests-2.28.0:
  Would remove:
    ...
Proceed (Y/n)? y
  Successfully uninstalled requests-2.28.0
```

## Common Mistakes

- **Running `pip install` outside an activated virtual environment** by
  accident — the package installs system-wide instead of into your
  project's isolated environment.
- **Confusing the package name with the import name** — some packages
  install under one name but import under another (a common example
  outside this course: `pip install pillow` but `import PIL`). Always
  check a package's documentation for the exact import name.
- **Forgetting `pip` itself sometimes needs an upgrade**:
  `pip install --upgrade pip`. An outdated `pip` occasionally fails to
  install newer packages correctly.
- **Installing a package you don't actually need** "just in case" —
  every dependency is something that can break, go unmaintained, or
  introduce a security issue; install only what your project actually
  uses.

## Practice

1. Activate a virtual environment and install any one real package (e.g.
   `requests`).
2. Run `pip show <that-package>` and read its version and summary.
3. Upgrade the package with `pip install --upgrade <package-name>`.
4. Uninstall it, then confirm with `pip list` that it's gone.

## Challenge

Install a specific older version of a package on purpose (e.g.
`pip install requests==2.25.0`), confirm the version with `pip show`, then
upgrade to the latest and confirm the version changed.

## Mini Project

No dedicated mini project — the exercises above are hands-on enough for
this lesson; the next lesson (`requirements.txt`) is where you'll apply
this to a real project.

## Summary

`pip` installs third-party packages from PyPI into your (ideally virtual)
environment, letting you `import` them exactly like standard-library
modules. Always activate your project's virtual environment before running
`pip install`, and install only what you actually need.

## Next Step

Continue to [`03-requirements-txt.md`](03-requirements-txt.md).
