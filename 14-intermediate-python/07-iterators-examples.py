"""14 - Intermediate Python: Iterators"""

numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))

numbers = [1, 2]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print("No more items!")

iterator = iter("abc")
print(next(iterator))
print(next(iterator))
print(next(iterator))


def manual_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        print(item)


manual_for_loop([100, 200, 300])
