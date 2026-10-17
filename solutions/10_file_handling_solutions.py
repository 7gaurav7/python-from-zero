"""
Solutions for 10 - File Handling
Try the exercises yourself first! (exercises/10_file_handling_exercises.py)
Running this script creates/modifies files in the current folder.
"""

# 1. save favorite movies
with open("movies.txt", "w") as file:
    file.write("The Matrix\n")
    file.write("Inception\n")
    file.write("Interstellar\n")

# 2. read and number each movie
with open("movies.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")

# 3. append a new movie
with open("movies.txt", "a") as file:
    file.write("The Prestige\n")

# 4. count lines in a file
with open("movies.txt", "r") as file:
    line_count = len(file.readlines())
print("Line count:", line_count)

# 5. print lines containing a specific word
search_word = "Inter"
with open("movies.txt", "r") as file:
    for line in file:
        if search_word in line:
            print(line.strip())

# Challenge 1: word frequency to a new file
with open("movies.txt", "r") as file:
    text = file.read()
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
with open("word_counts.txt", "w") as file:
    for word, count in word_counts.items():
        file.write(f"{word}: {count}\n")

# Challenge 2: a simple logger
def log(message):
    try:
        with open("log.txt", "r") as file:
            line_number = len(file.readlines()) + 1
    except FileNotFoundError:
        line_number = 1
    with open("log.txt", "a") as file:
        file.write(f"{line_number}: {message}\n")

log("Program started")
log("Program finished")
