# 🛠 Setup Guide

Follow this once before starting `00-getting-started`. Total time: ~15 minutes.

## 1. Install Python 3

### Windows
1. Go to https://www.python.org/downloads/
2. Download the latest **Python 3** installer.
3. Run it. **Check the box "Add Python to PATH" before clicking Install** —
   this step is the #1 source of beginner setup problems, so don't miss it.
4. Open **Command Prompt** and type:
   ```
   python --version
   ```
   You should see something like `Python 3.12.4`.

### macOS
1. Go to https://www.python.org/downloads/ and download the macOS installer,
   **or**, if you have [Homebrew](https://brew.sh/), run:
   ```
   brew install python
   ```
2. Open **Terminal** and type:
   ```
   python3 --version
   ```

### Linux
Most distributions already include Python 3. Check with:
```
python3 --version
```
If missing, install via your package manager, e.g. (Debian/Ubuntu):
```
sudo apt update && sudo apt install python3
```

## 2. Install a Code Editor

We recommend **[VS Code](https://code.visualstudio.com/)** (free):

1. Download and install it.
2. Open VS Code → Extensions (left sidebar) → search **"Python"** (by
   Microsoft) → Install.
3. That's it — VS Code will now understand `.py` files, give you error
   highlighting, and let you run code with a single click.

Any editor works (PyCharm, Sublime, even Notepad), but VS Code has the
gentlest learning curve for beginners.

## 3. Running Your First Program

1. Create a new folder somewhere for your practice code, e.g. `python-practice`.
2. Open that folder in VS Code (`File → Open Folder`).
3. Create a new file called `hello.py`.
4. Type:
   ```python
   print("Hello, World!")
   ```
5. Run it:
   - **In VS Code:** click the ▶ "Run" button in the top-right, or right-click
     the file → "Run Python File in Terminal".
   - **From a terminal:** navigate to the folder and run:
     ```
     python hello.py        # Windows
     python3 hello.py       # macOS/Linux
     ```
6. You should see:
   ```
   Hello, World!
   ```

If you see that, your setup works. 🎉

## 4. Getting This Repository

If you have `git` installed:
```
git clone https://github.com/your-username/python-from-zero.git
cd python-from-zero
```

If you don't have `git` yet, that's fine — you can also just download this
repository as a `.zip` file (GitHub → "Code" → "Download ZIP") and extract it.
(You'll pick up `git` naturally later; it isn't required for this course.)

## 5. Common Setup Problems

| Problem | Fix |
|---|---|
| `'python' is not recognized...` (Windows) | Python wasn't added to PATH. Reinstall and check that box, or search "edit environment variables" and add Python's install folder manually. |
| `python: command not found` (Mac/Linux) | Use `python3` instead of `python`. |
| VS Code doesn't recognize Python | Install the Python extension, then reload the window (`Ctrl+Shift+P` → "Reload Window"). |
| `pip` not recognized | Use `python -m pip` (Windows) or `python3 -m pip` (Mac/Linux) instead of bare `pip`. |

You're ready. Head to [`00-getting-started/README.md`](00-getting-started/README.md).

## 6. Setup for Later Topics (nothing to do yet)

This guide covers everything you need for topics `00`–`16`. Two topics
later in the course teach additional setup *as part of the lesson itself*
— you don't need to prepare for these now:

- **`17-git-and-github`** teaches installing and configuring Git.
- **`18-real-world-python`** teaches virtual environments and `pip`, which
  you'll want before `20-ai-ml-preparation`'s third-party libraries
  (`numpy`, `pandas`, `matplotlib`) — install instructions are given right
  there, inside a virtual environment, when you reach it.

No need to install Git, set up a virtual environment, or install any
third-party package before then.
