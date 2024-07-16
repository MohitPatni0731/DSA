from insertion_sort import Insertion
import pytest


def test_insertion_sort_empty():
    assert Insertion.insertion_sort([]) == []


def test_insertion_sort_single_element():
    assert Insertion.insertion_sort([1]) == [1]


def test_insertion_sort():
    assert Insertion.insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
