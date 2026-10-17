"""
Solutions for 06 - Strings
Try the exercises yourself first! (exercises/06_strings_exercises.py)
"""

# 1. first and last characters
word = "Python"
print(word[0], word[-1])

# 2. split full name into first and last
full_name = "Ada Lovelace"
first, last = full_name.split(" ")
print(first, last)

# 3. count words in a sentence
sentence = "Python is a fun language to learn"
word_count = len(sentence.split(" "))
print(word_count)

# 4. reverse a string
text = "hello"
print(text[::-1])

# 5. clean up messy input
messy = "  JOHN@Email.com  "
clean = messy.strip().lower()
print(clean)

# Challenge 1: palindrome check
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("Was it a car or a cat I saw"))

# Challenge 2: capitalize each word manually
sentence = "python is fun"
words = sentence.split(" ")
capitalized_words = [word[0].upper() + word[1:] for word in words]
manual_title = " ".join(capitalized_words)
print(manual_title)
print(sentence.title())
