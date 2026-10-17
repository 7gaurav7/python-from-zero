"""Helper module for exercise 4 in topic 12."""


def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
