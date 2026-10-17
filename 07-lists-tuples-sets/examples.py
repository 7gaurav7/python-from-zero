"""
Topic 07 - Lists, Tuples, and Sets
Runnable examples matching the README.
"""

# Example 1: lists - create, access, modify
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("date")
print(fruits)
fruits.remove("banana")
print(fruits)
# Expected output:
# apple
# ['apple', 'banana', 'cherry', 'date']
# ['apple', 'cherry', 'date']

# Example 2: looping over a list
scores = [85, 90, 78]
for score in scores:
    print(f"Score: {score}")
# Expected output:
# Score: 85
# Score: 90
# Score: 78

# Example 3: tuples are immutable
point = (3, 4)
print(point[0], point[1])
# point[0] = 10   # this would raise: TypeError
# Expected output: 3 4

# Example 4: sets remove duplicates
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)
print(4 in unique_numbers)
# Expected output:
# {1, 2, 3}
# False
