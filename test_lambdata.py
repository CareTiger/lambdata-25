"""Basic tests"""

from random import randint
import pytest
import lambdata as ld


def test_increment_int():
    """Making sure increment works for Integers"""
    x = 0
    y = ld.increment(x)
    assert y == 1

def test_increment_float():
    """Making sure increment works for Floats"""
    x = 10.4
    y = ld.increment(x)
    assert y == 11.4