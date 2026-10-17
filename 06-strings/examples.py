"""
Topic 06 - Strings
Runnable examples matching the README.
"""

# Example 1: indexing and slicing
word = "Python"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[3:])
# Expected output:
# P
# n
# Pyt
# hon

# Example 2: common string methods
text = "  Hello, World  "
print(text.strip())
print(text.strip().upper())
print(text.strip().lower())
# Expected output:
# Hello, World
# HELLO, WORLD
# hello, world

# Example 3: splitting and joining
sentence = "Python is fun"
words = sentence.split(" ")
print(words)
print("-".join(words))
# Expected output:
# ['Python', 'is', 'fun']
# Python-is-fun

# Example 4: length and concatenation
first = "Ada"
last = "Lovelace"
full = first + " " + last
print(full)
print(len(full))
# Expected output:
# Ada Lovelace
# 12
