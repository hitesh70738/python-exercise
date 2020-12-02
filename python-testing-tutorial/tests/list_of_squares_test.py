import pytest
from programs.list_of_squares import list_of_squares

def test_list_of_squares():
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}