import pytest 
from src.number_utils import find_max

def test_find_max():
    numbers=[-1,-5,0,-5,10]
    assert find_max(numbers)==10

def test_empty_list():
    numbers=[]
    assert find_max(numbers)==None