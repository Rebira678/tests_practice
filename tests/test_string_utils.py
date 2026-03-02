import pytest 
from src.string_utils import reverse_string

def test_reverse_string():

    assert reverse_string("word")=="drow"
    assert reverse_string("")==""
