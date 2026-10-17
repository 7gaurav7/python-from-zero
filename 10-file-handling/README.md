# 10 — File Handling

## 1. Beginner-Friendly Explanation

Until now, everything your programs stored disappeared the moment they
finished running. **Files** let you save data permanently on disk, and read
it back later — essential for anything from saving a high score to
processing a spreadsheet of data.

Python opens files using the `open()` function, which gives you a **file
object** you can read from or write to. It's best practice to use a `with`
block, which automatically closes the file for you when you're done — even
if an error happens.

## 2. Important Concepts

- **Opening a file** — `open(filename, mode)`.
- **Modes** — `"r"` (read, default), `"w"` (write — *overwrites* the file),
  `"a"` (append — adds to the end), `"r+"` (read and write).
- **`with` statement** — automatically closes the file when the block ends;
  always prefer this over manually calling `.close()`.
- **Reading** — `.read()` (whole file as one string), `.readline()` (one
  line), `.readlines()` (list of lines).
- **Writing** — `.write(text)` writes a string; you must add `"\n"` yourself
  for a new line.
- **File not found** — trying to read a file that doesn't exist raises a
  `FileNotFoundError` (handled properly in `11-exceptions`).

## 3. Syntax

```python
# Writing to a file (creates it if missing, overwrites if it exists)
with open("data.txt", "w") as file:
    file.write("Hello, file!\n")

# Appending to a file (adds to the end, doesn't erase existing content)
with open("data.txt", "a") as file:
    file.write("Another line.\n")

# Reading an entire file
with open("data.txt", "r") as file:
    content = file.read()

# Reading line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())   # .strip() removes the trailing newline
```

## 4. Simple Examples

**Example 1 — Writing to a file**
```python
with open("notes.txt", "w") as file:
    file.write("Buy milk\n")
    file.write("Walk the dog\n")
print("File written.")
```
Expected output:
```
File written.
```
(and `notes.txt` now contains two lines)

**Example 2 — Reading an entire file**
```python
with open("notes.txt", "r") as file:
    content = file.read()
print(content)
```
Expected output:
```
Buy milk
Walk the dog

```

**Example 3 — Reading line by line**
```python
with open("notes.txt", "r") as file:
    for line in file:
        print("Task:", line.strip())
```
Expected output:
```
Task: Buy milk
Task: Walk the dog
```

**Example 4 — Appending to a file**
```python
with open("notes.txt", "a") as file:
    file.write("Read a book\n")

with open("notes.txt", "r") as file:
    print(file.read())
```
Expected output:
```
Buy milk
Walk the dog
Read a book

```

## 5. Practice Problems

1. Write a program that saves 3 of your favorite movies to `movies.txt`,
   one per line.
2. Write a program that reads `movies.txt` and prints each movie with a
   number in front of it (e.g. "1. ...").
3. Write a program that appends a new movie to `movies.txt` without erasing
   the existing ones.
4. Write a program that counts how many lines are in a text file.
5. Write a program that reads a file and prints only the lines that contain
   a specific word.

## 6. Challenge Problems

1. Write a program that reads a text file and counts how many times each
   word appears (reusing ideas from `08-dictionaries`), then writes the
   results to a new file called `word_counts.txt`.
2. Write a simple "logging" function `log(message)` that appends a message
   with the current line number (count existing lines first) to `log.txt`
   every time it's called.

## 7. Common Mistakes

- **Using `"w"` mode when you meant to keep existing content** — `"w"`
  erases the file first. Use `"a"` to add to the end instead.
- **Forgetting `with`** and manually forgetting to `.close()` the file —
  this can leave the file locked or data not fully saved.
- **Forgetting `.strip()`** when reading lines — each line from a file
  includes a trailing `"\n"`, which shows up as extra blank lines if not
  removed.
- **Assuming a file exists** — always be prepared for `FileNotFoundError`
  (you'll learn to handle this properly next topic).
- **Using the wrong relative path** — `open("data.txt")` looks for the file
  in the folder you're running the script from, not necessarily the folder
  the script is saved in.

## 8. Mini Quiz

1. What mode do you use to add to the end of a file without erasing it?
2. What Python keyword automatically closes a file for you?
3. What method reads the whole file at once as a single string?
4. Why do you often need `.strip()` when reading lines from a file?
5. What error occurs if you try to read a file that doesn't exist?

*(Answers: 1. `"a"`  2. `with`  3. `.read()`  4. To remove the trailing newline character  5. `FileNotFoundError`)*

## 9. Practical Exercise

Create `diary.py` that asks the user to type a diary entry and appends it
(with a blank line separator) to `diary.txt` each time it's run. Then add a
second small script `read_diary.py` that prints the full contents of
`diary.txt`.

➡️ Matching files: [`exercises/10_file_handling_exercises.py`](../exercises/10_file_handling_exercises.py) ·
[`solutions/10_file_handling_solutions.py`](../solutions/10_file_handling_solutions.py)

**Previous:** [`09-functions`](../09-functions/README.md) | **Next:** [`11-exceptions`](../11-exceptions/README.md)
