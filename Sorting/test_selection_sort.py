from selection_sort import Selection
import pytest


def test_selection_sort_empty():
    assert Selection.selection_sort([]) == []


def test_selection_sort_single_element():
    assert Selection.selection_sort([1]) == [1]


def test_selection_sort():
    assert Selection.selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
