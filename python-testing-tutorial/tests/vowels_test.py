import pytest
from programs import vowels

def test_vowels():
    assert vowels.vowels("abolition") == 5

def test_vowels_uppercase():
    assert vowels.vowels("Onomatopoeia") == 8