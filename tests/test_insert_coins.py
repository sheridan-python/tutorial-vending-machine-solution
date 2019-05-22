"""
Tests the insert_coin function
"""
from vending_machine import insert_coin


def test_insert_five():
    """
    Given 5 to an empty list of coins, 5 should be
    appended.
    """
    inserted_coins = []
    insert_coin(5, inserted_coins)

    assert inserted_coins == [5]
