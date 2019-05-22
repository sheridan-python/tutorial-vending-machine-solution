"""
Tests the insert_coin function
"""
import pytest
from vending_machine import insert_coin


def test_insert_five():
    """
    Given 5 to an empty list of coins, 5 should be
    appended.
    """
    inserted_coins = []
    insert_coin(5, inserted_coins)

    assert inserted_coins == [5]


def test_insert_fifty():
    """
    Given 50, a ValueError should be raised.
    """
    inserted_coins = []
    with pytest.raises(ValueError):
        insert_coin(50, inserted_coins)
