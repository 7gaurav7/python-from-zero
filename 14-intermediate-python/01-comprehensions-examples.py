"""14 - Intermediate Python: Comprehensions"""

squares = [n ** 2 for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

names = ["Alice", "Bob", "Carla"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Carla': 5}

words = ["Hi", "hi", "HELLO", "hello"]
unique_lower = {word.lower() for word in words}
print(unique_lower)  # {'hi', 'hello'}
