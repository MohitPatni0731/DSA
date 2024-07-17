from lower_bound import Lower
import pytest


def test_empty():
    assert Lower.lower_bound([], 1) == 0


def test_single_element():
    assert Lower.lower_bound([1], 0) == 0


def test_lower_bound():
    assert Lower.lower_bound([1, 2, 3, 4, 5], 6) == 5
