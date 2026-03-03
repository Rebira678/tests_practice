import pytest 
from src.numbers_utils import second_largest

def test_normal_list():
    assert second_largest([4,6,2,7,8,22,44,11,63,])==44
    assert second_largest([3,55,22,142,532,])==142

def test_with_duplicate():
    assert second_largest([33,33,33,45])==33

def test_the_same_numbers():
    assert second_largest([3,3,3,3,3,3,3,3,3])==None

def test_two_number():
    assert second_largest([4,6])==4

def test_negative_numbers():
    assert second_largest([-4,-6,-3])==-4

def test_single_number():
    assert second_largest([4])==None

def test_empty():
    assert second_largest([])==None

