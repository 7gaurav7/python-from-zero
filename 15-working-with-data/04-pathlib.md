# pathlib

## Learning Objectives
- Explain why `pathlib` is preferred over manually building path strings
- Create and inspect a `Path` object
- Join paths, check existence, and list directory contents
- Read/write a file directly through a `Path` object

## Concept Explanation
In `10-file-handling` you opened files using plain string paths. As soon
as programs work with folders, nested paths, or need to run on both
Windows (`\`) and Mac/Linux (`/`), string concatenation gets error-prone.
`pathlib`'s `Path` class represents a path as an object with useful
methods, handling the correct separator automatically.
```python
from pathlib import Path
file_path = Path("data") / "students.csv"   # / joins paths!
```

## Syntax
```python
from pathlib import Path
Path("some/path"); Path.cwd()
path1 / "subfolder" / "file.txt"

path.exists(); path.is_file(); path.is_dir()
path.name; path.stem; path.suffix; path.parent

path.mkdir(exist_ok=True)
list(path.iterdir())
list(path.glob("*.txt"))

path.read_text()
path.write_text("content")
```

## Examples

**Example 1 - Creating and joining paths**
```python
from pathlib import Path
file_path = Path("data") / "students.csv"
print(file_path)
```
Expected output (Linux/Mac): `data/students.csv`
(On Windows: `data\students.csv` -- `pathlib` picks the right separator.)

**Example 2 - Inspecting a path's parts**
```python
file_path = Path("data/students.csv")
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.parent)
```
Expected output:
```
students.csv
students
.csv
data
```

**Example 3 - Reading and writing text directly**
```python
note_path = Path("note.txt")
note_path.write_text("Remember to practice Python today!")
print(note_path.read_text())
```
Expected output: `Remember to practice Python today!`

**Example 4 - Checking existence and listing files**
```python
folder = Path(".")
print(folder.exists())
print(len(list(folder.glob("*.py"))) >= 0)
```
Expected output:
```
True
True
```

## Common Mistakes
- Building paths with string concatenation instead of `/` -- breaks on
  Windows.
- Forgetting `Path` objects work almost everywhere a string path would
  (including `open()`), but occasionally you'll need `str(path)` explicitly.
- Sticking to old `os.path` functions out of habit -- still works, but
  `pathlib` is the modern standard for new code.
- Forgetting `mkdir(exist_ok=True)` -- without it, an existing directory
  raises `FileExistsError`.

## Practice
1. Create a `Path` joining a folder `"output"` and file `"report.txt"`.
2. Print a path's `.name`, `.stem`, and `.suffix`.
3. Save and reload a short note with `write_text()`/`read_text()`.
4. List all `.py` files in the current directory with `.glob("*.py")`.

## Challenge
Write `find_files_by_extension(folder, extension)` returning a list of
matching files in `folder` (not subfolders) using `Path.glob()`.

## Mini Project
Update the `19-projects` Contact Book to use a `Path` object for its
`FILENAME`, checking `.exists()` before loading.

## Summary
`pathlib`'s `Path` represents filesystem paths as objects -- joining with
`/`, inspecting parts, and reading/writing files directly, while handling
OS differences automatically. It's the modern, recommended approach.

## Next Step
Continue to [`05-basic-data-processing.md`](05-basic-data-processing.md).
