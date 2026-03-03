import pytest 
from src.stats_utils import median

def test_even_list():
    numbers=[4,1,6,7]
    assert median(numbers)==5

def test_even_fraction_list():
    numbers=[2,1,5,6]
    assert median(numbers)==3.5

def test_odd_list():
    numbers=[1,4,2,5,2,4,2,2,5]
    assert median(numbers)==2

def test_empty_list():
    numbers=[]
    assert median(numbers)==None

def test_single_element():
    numbers=[4]
    assert median(numbers)==4

def test_negative_number():
    numbers=[-1,-2,-7,6,-4]
    assert median(numbers)==-2
