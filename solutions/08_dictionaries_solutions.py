"""
Solutions for 08 - Dictionaries
Try the exercises yourself first! (exercises/08_dictionaries_exercises.py)
"""

# 1. book dictionary
book = {"title": "Dune", "author": "Frank Herbert", "year": 1965}
print(book["title"], book["author"], book["year"])

# 2. add and update
book["pages"] = 412
book["year"] = 1965  # (unchanged here, but this is how you'd update)
print(book)

# 3. loop through student scores
scores = {"Alice": 90, "Bob": 78, "Carla": 85}
for student, score in scores.items():
    print(f"{student}: {score}")

# 4. safe access with .get()
person = {"name": "Sam"}
print(person.get("age", "N/A"))

# 5. word frequency counter
sentence = "the quick brown fox jumps over the lazy fox"
word_counts = {}
for word in sentence.split(" "):
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

# Challenge 1: simple phone book
phone_book = {}
phone_book["Alice"] = "555-1234"
print(phone_book)
print(phone_book.get("Alice"))
del phone_book["Alice"]
print(phone_book)

# Challenge 2: average score per student (dict of lists)
grades = {"Alice": [90, 85, 92], "Bob": [70, 75, 80]}
for student, grade_list in grades.items():
    average = sum(grade_list) / len(grade_list)
    print(f"{student}: {average:.1f}")
