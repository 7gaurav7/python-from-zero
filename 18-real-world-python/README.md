# 18 — Real-World Python

Every lesson so far has run inside one file with the standard library only.
Real projects need more: isolating dependencies per project, installing
third-party packages, organizing multiple files sensibly, and keeping
secrets (like API keys) out of your code. This topic covers the practical
setup skills that sit around your Python code once a project grows beyond
a single script.

**Prerequisite check:** `12-modules-and-packages` and `17-git-and-github`
(you'll want `.gitignore` again here).

## Lessons in This Topic

| # | Lesson | What You'll Learn |
|---|---|---|
| 1 | [Virtual Environments](01-virtual-environments.md) | Isolate each project's dependencies |
| 2 | [pip Basics](02-pip-basics.md) | Install, upgrade, and remove third-party packages |
| 3 | [requirements.txt](03-requirements-txt.md) | Record and share a project's exact dependencies |
| 4 | [Project Structure](04-project-structure.md) | Organize a multi-file Python project sensibly |
| 5 | [Configuration Basics](05-configuration-basics.md) | Keep settings out of your program logic |
| 6 | [Environment Variables](06-environment-variables.md) | Keep secrets out of your code entirely |

## Suggested Order

Follow the table top to bottom — `requirements.txt` only makes sense once
you understand virtual environments and `pip`, and configuration/env
variables assume you already know how a project's files are organized.

**Previous:** [`17-git-and-github`](../17-git-and-github/README.md) | **Next:** [`19-projects`](../19-projects/README.md)
