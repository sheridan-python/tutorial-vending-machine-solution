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


def test_insert_ten():
    """
    Given 10 to an empty list of coins, 10 should be
    appended.
    """
    inserted_coins = []
    insert_coin(10, inserted_coins)

    assert inserted_coins == [10]


def test_insert_twenty_five():
    """
    Given 25 to an empty list of coins, 25 should be
    appended.
    """
    inserted_coins = []
    insert_coin(25, inserted_coins)

    assert inserted_coins == [25]


def test_insert_100():
    """
    Given 100 to an empty list of coins, 100 should be
    appended.
    """
    inserted_coins = []
    insert_coin(100, inserted_coins)

    assert inserted_coins == [100]


def test_insert_200():
    """
    Given 200 to an empty list of coins, 200 should be
    appended.
    """
    inserted_coins = []
    insert_coin(200, inserted_coins)

    assert inserted_coins == [200]


def test_insert_fifty():
    """
    Given 50, a ValueError should be raised.
    """
    inserted_coins = []
    with pytest.raises(ValueError):
        insert_coin(50, inserted_coins)
