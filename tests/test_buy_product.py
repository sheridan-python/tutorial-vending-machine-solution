"""
Tests the buy_product function of the vending machine
"""
import pytest

from vending_machine import buy_product


def test_buy_a_drink():
    """
    Given that "drink" is purchased with an exact balance,
    the balance returned should be 0.
    """
    assert buy_product('drink', 275) == 0



def test_buy_banana():
    """
    Given that "banana" is purchased, a ValueError should be
    raised.
    """
    with pytest.raises(ValueError):
        buy_product('banana', 5)  # Random value of 5 balance
