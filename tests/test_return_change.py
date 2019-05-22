from vending_machine import return_change


def test_call_with_zero():
    assert return_change(0) == []
