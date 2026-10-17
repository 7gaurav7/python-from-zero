"""
Topic 05 - Loops
Runnable examples matching the README.
"""

# Example 1: counting with for and range
for i in range(5):
    print(i)
# Expected output: 0 1 2 3 4 (each on its own line)

# Example 2: range with start, stop, step
for i in range(2, 10, 2):
    print(i)
# Expected output: 2 4 6 8 (each on its own line)

# Example 3: while loop
count = 0
while count < 3:
    print("Count is", count)
    count += 1
# Expected output:
# Count is 0
# Count is 1
# Count is 2

# Example 4: break and continue
for i in range(10):
    if i == 5:
        break          # stop the loop entirely
    if i % 2 == 0:
        continue       # skip even numbers, go to next i
    print(i)
# Expected output: 1 3 (each on its own line)
