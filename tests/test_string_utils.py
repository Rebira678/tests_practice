import pytest 
from src.string_utils import reverse_string

def test_single_character():
    assert reverse_string("a") == "a"

def test_palindrome():
    assert reverse_string("madam") == "madam"

def test_with_spaces():
    assert reverse_string("a b") == "b a"

def test_numbers():
    assert reverse_string("123") == "321"