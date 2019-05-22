"""
Tests the buy_product function of the vending machine
"""
from vending_machine import buy_product


def test_buy_a_drink():
    """
    Given that "drink" is purchased with an exact balance,
    the balance returned should be 0.
    """
    assert buy_product('drink', 275) == 0
