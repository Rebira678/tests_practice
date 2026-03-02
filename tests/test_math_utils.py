import pytest 
from src.math_utils import average

def test_average():
    numbers=[2,4,6,8,10]
    assert average(numbers)==6

def test_empty():
    numbers=[]
    assert average(numbers)==0

def test_one():
    with pytest.raises(ValueError):
        numbers=[2]
        average(numbers)
