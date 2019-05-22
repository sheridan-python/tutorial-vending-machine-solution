"""
Tests the buy_product function of the vending machine
"""
import pytest

from vending_machine import InsufficientFunds, buy_product


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


def test_buy_chips():
    """
    Given that chips are purchased with a balance of 225,
    0 should be returned.
    """
    assert buy_product('chips', 225) == 0


def test_buy_candy():
    """
    Given that candy is purchased with a balance of 315,
    0 should be returned.
    """
    assert buy_product('candy', 315) == 0


def test_drink_with_a_274_should_raise_insufficient_funds():
    """
    Given that a drink is attempted to be purchased with a balance
    of 274, an InsufficientFunds exception should be raised.
    """
    with pytest.raises(InsufficientFunds):
        buy_product('drink', 274)
