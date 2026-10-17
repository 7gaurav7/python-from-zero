"""
Solutions for 17 - Git and GitHub
Try the exercises yourself first!
(exercises/17_git_and_github_exercises.py)

These are the terminal commands you'd run for each exercise -- there is
no Python to execute here, since this topic is about the Git tool itself.
"""

# 1. Initialize a repository and make a first commit
#   mkdir git-practice && cd git-practice
#   git init
#   echo "print('Hello, Git!')" > hello.py
#   git add hello.py
#   git commit -m "Add hello.py"

# 2. A second, separate commit
#   echo "print('A second line')" >> hello.py
#   git add hello.py
#   git commit -m "Add a second print statement"
#   git log --oneline
#   # Expect to see two lines, one per commit, newest first.

# 3. Branch, commit, merge
#   git checkout -b add-farewell
#   echo "print('Goodbye!')" >> hello.py
#   git add hello.py
#   git commit -m "Add farewell message"
#   git checkout main
#   git merge add-farewell
#   # hello.py on main now includes the farewell message too.

# 4. A .gitignore file
#   printf "__pycache__/\n*.pyc\n" > .gitignore
#   git add .gitignore
#   git commit -m "Add .gitignore"
#   # After this, running your Python files (which creates __pycache__)
#   # and then `git status` should show .gitignore is respected --
#   # __pycache__/ no longer appears as an untracked file.

# Challenge: push a 19-projects solution to GitHub
#   cd 19-projects/beginner-projects/01-number-guessing-game
#   git init
#   git add .
#   git commit -m "Initial commit: Number Guessing Game"
#   # Create an empty repository on github.com first, then:
#   git remote add origin https://github.com/your-username/number-guessing-game.git
#   git branch -M main
#   git push -u origin main
