import pytest
from programs.factorial import fact

def test_fact_zero():
    assert fact(0) == 1

def test_fact_float():
    assert fact(0.0) == 1.0

def test_fact_num():
    assert fact(5) == 120