"""14 - Intermediate Python: Unpacking"""

point = (3, 4)
x, y = point
print(x, y)

a, b = 1, 2
a, b = b, a
print(a, b)

scores = [100, 90, 85, 70, 60]
highest, *others = scores
print(highest)
print(others)


def min_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = min_max([4, 8, 15, 16, 23, 42])
print(lowest, highest)
