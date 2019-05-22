"""
Tests return change
"""
from vending_machine import return_change


def test_call_with_zero():
    assert return_change(0) == []


def test_call_with_25():
    assert return_change(25) == [25]


def test_call_with_400():
    assert return_change(400) == [200, 200]
