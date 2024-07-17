from upper_bound import Upper
import pytest


def test_empty():
    assert Upper.upper_bound([], 1) == 0


def test_single_element():
    assert Upper.upper_bound([1], 0) == 0


def test_upper_bound():
    assert Upper.upper_bound([1, 2, 3, 4, 5], 6) == 5
