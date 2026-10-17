"""
Solutions for 07 - Lists, Tuples, and Sets
Try the exercises yourself first! (exercises/07_lists_tuples_sets_exercises.py)
"""

# 1. list of 5 favorite foods
foods = ["pizza", "sushi", "tacos", "pasta", "salad"]
print(foods)
print(foods[0], foods[-1])

# 2. add two, remove one
foods.append("ice cream")
foods.append("bread")
foods.remove("salad")
print(foods)

# 3. total and average of a list of numbers
numbers = [10, 20, 30, 40]
total = 0
for n in numbers:
    total += n
average = total / len(numbers)
print(total, average)

# 4. tuple for coordinates
location = (40.7128, -74.0060)
print(location[0], location[1])

# 5. unique values using a set
values = [1, 2, 2, 3, 3, 3, 4]
unique_values = set(values)
print(unique_values)
print(len(unique_values))

# Challenge 1: largest/smallest without max()/min()
numbers = [5, 12, 3, 9, 27, 1]
largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print(largest, smallest)

# Challenge 2: common values between two lists using sets
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)
print(common)
