"""14 - Intermediate Python: enumerate() and zip()"""

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")

names = ["Alice", "Bob", "Carla"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

keys = ["name", "age", "city"]
values = ["Alice", 25, "Paris"]
print(dict(zip(keys, values)))
