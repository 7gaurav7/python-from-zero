"""
Solutions for 18 - Real-World Python
Try the exercises yourself first!
(exercises/18_real_world_python_exercises.py)

Exercises 1, 2, 3, 4, 5, and 7 are hands-on terminal/file-system tasks;
their "solutions" are shown as commands in comments. Exercises 6 and the
challenge are runnable Python, shown below.
"""
import os

# --- 01: Virtual Environments ---
#   mkdir env-practice && cd env-practice
#   python -m venv venv
#   source venv/bin/activate      # (Windows: venv\Scripts\activate)
#   which python                   # should point inside env-practice/venv/

#   printf "venv/\n__pycache__/\n*.pyc\n" > .gitignore

# --- 02: pip and requirements.txt ---
#   pip install requests
#   pip list                        # confirm "requests" is listed
#   pip freeze > requirements.txt
#   deactivate
#   rm -rf venv
#   python -m venv venv
#   source venv/bin/activate
#   pip install -r requirements.txt
#   pip list                        # should match the earlier list

# --- 03: Project Structure ---
#   mkdir -p my_tool/my_tool
#   touch my_tool/my_tool/__init__.py
#   # my_tool/my_tool/logic.py:
#   #     def greet(name):
#   #         return f"Hello, {name}!"
#   # my_tool/main.py:
#   #     from my_tool.logic import greet
#   #     print(greet("World"))

# --- 04: Configuration and Environment Variables ---
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", "3"))
APP_NAME = os.environ.get("APP_NAME", "Python From Zero Demo")
print(MAX_RETRIES, APP_NAME)

#   pip install python-dotenv
#   printf "API_KEY=demo-value\n" > .env
#   printf ".env\n" >> .gitignore
#   # then in Python:
#   #     from dotenv import load_dotenv
#   #     load_dotenv()
#   #     print(os.environ.get("API_KEY"))

# --- Challenge ---
EXPENSE_FILE = os.environ.get("EXPENSE_FILE", "expenses.txt")
print(f"Expenses will be saved to: {EXPENSE_FILE}")
