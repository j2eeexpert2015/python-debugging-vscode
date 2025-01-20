# string_utils.py

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)
