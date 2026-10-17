"""14 - Intermediate Python: Lambda Functions"""

add = lambda a, b: a + b
print(add(3, 4))  # 7

students = [("Alice", 85), ("Bob", 92), ("Carla", 78)]
students.sort(key=lambda student: student[1])
print(students)  # [('Carla', 78), ('Alice', 85), ('Bob', 92)]

words = ["banana", "kiwi", "apple", "fig"]
words.sort(key=lambda word: len(word))
print(words)  # ['kiwi', 'fig', 'apple', 'banana']

greet = lambda name="friend": f"Hello, {name}!"
print(greet())
print(greet("Sam"))
