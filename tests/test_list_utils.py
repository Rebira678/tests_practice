import pytest 
from  src.list_utils import remove_duplicates

def test_remove_duplicates():
    items=["a","b","a","aa","b","c"]
    assert remove_duplicates(items)==["a","b","aa","c"]