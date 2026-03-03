import pytest 
from src.strings_utils import is_palindrome

def test_is_palindrome():
    assert is_palindrome("BABY")==False
    assert is_palindrome("NUMber")==False
    assert is_palindrome('abnba')==True

def test_empty():
    assert is_palindrome("")==True

def test_one():
    assert is_palindrome("a")==True

def test_number_string():
    assert is_palindrome("1234")==False
    assert is_palindrome("12321")==True

def test_with_space():
    assert is_palindrome("2 3 32")==True
