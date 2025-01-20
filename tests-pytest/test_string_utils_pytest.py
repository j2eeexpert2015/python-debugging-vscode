# test_string_utils_pytest.py

import pytest
from testsample.string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""

def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("Racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOUaeiou") == 10
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
