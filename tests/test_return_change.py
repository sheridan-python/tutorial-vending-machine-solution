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


def test_call_with_300():
    assert return_change(300) == [200, 100]


def test_call_with_265():
    assert return_change(265) == [200, 25, 25, 10, 5]
