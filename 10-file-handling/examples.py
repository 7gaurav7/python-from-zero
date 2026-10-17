"""
Topic 10 - File Handling
Runnable examples matching the README.
Running this script will create/modify a 'notes.txt' file
in the same folder.
"""

# Example 1: writing to a file
with open("notes.txt", "w") as file:
    file.write("Buy milk\n")
    file.write("Walk the dog\n")
print("File written.")
# Expected output: File written.

# Example 2: reading an entire file
with open("notes.txt", "r") as file:
    content = file.read()
print(content)
# Expected output:
# Buy milk
# Walk the dog
# (plus a trailing blank line)

# Example 3: reading line by line
with open("notes.txt", "r") as file:
    for line in file:
        print("Task:", line.strip())
# Expected output:
# Task: Buy milk
# Task: Walk the dog

# Example 4: appending to a file
with open("notes.txt", "a") as file:
    file.write("Read a book\n")

with open("notes.txt", "r") as file:
    print(file.read())
# Expected output:
# Buy milk
# Walk the dog
# Read a book
# (plus a trailing blank line)
