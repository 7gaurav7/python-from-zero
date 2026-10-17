"""
Exercises for 18 - Real-World Python
Each section matches one lesson file in 18-real-world-python/.
Some are hands-on terminal tasks (write your commands/observations as
comments); the rest are ordinary Python to write below each comment.
"""

# --- 01: Virtual Environments ---
# 1. Create a new project folder and set up a virtual environment inside
#    it. Activate it and confirm with `which python` / `where python`.
#    (commands + observation as a comment)


# 2. Add a .gitignore file to that folder excluding venv/.


# --- 02: pip and requirements.txt ---
# 3. Install a small package of your choice inside an activated virtual
#    environment, then run `pip list` to confirm it installed.


# 4. Generate a requirements.txt with `pip freeze`, delete your virtual
#    environment, recreate it, and reinstall from requirements.txt.


# --- 03: Project Structure ---
# 5. Take a single-file script you've written and split it into a small
#    package: a __init__.py, one module with the logic, and a separate
#    main.py that imports and uses it.


# --- 04: Configuration and Environment Variables ---
# 6. Write a small settings-reading snippet below with at least two
#    settings read from os.environ, each with a sensible default.


# 7. Install python-dotenv, create a .env file (and .gitignore it
#    immediately), and load one value from it.


# Challenge: Add an EXPENSE_FILE environment variable (default
# "expenses.txt") to the 19-projects Expense Tracker.
import os  # noqa: E402  (used by exercise 6 below, if you complete it here)
