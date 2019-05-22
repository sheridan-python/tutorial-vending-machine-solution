"""
Tests return change
"""
from vending_machine import return_change


def test_call_with_zero():
    """
    When no balance exists, no coins should be returned.
    """
    assert return_change(0) == []


def test_call_with_25():
    """
    When the balance is 25, 25 should be returned in the list.
    """
    assert return_change(25) == [25]


def test_call_with_400():
    """
    When the balance is 400, two 200 coins should be returned.
    """
    assert return_change(400) == [200, 200]


def test_call_with_300():
    """
    When the balance is 300, a 200 and 100 coin should be returned.
    """
    assert return_change(300) == [200, 100]


def test_call_with_265():
    """
    When the balance is 265, a 200, two 25, a 10 and 5 coin
    should be returned.
    """
    assert return_change(265) == [200, 25, 25, 10, 5]


def test_call_with_7():
    """
    When the balance is 7, 5 should be returned. The vending
    machine's lowest denomination is 5 and will keep any extra
    balance.
    """
    assert return_change(7) == [5]


def test_call_with_negative():
    """
    When the balance is negative, no coins should be returned. The
    vending machine company won't make money by giving away money.
    """
    assert return_change(-9) == []
