import pytest
from src.text_utils import  word_count

def test_word_count():
    text="Hello World"
    assert word_count(text)=={"hello":1,"world":1}

def test_case_sensative():
    text="hello Hello HelLO"
    assert word_count(text)=={"hello":3}

def test_multiple_space():
    text=" hello      world"
    assert word_count(text)=={"hello":1,"world":1}