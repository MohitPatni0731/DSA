from bubble_sort import Bubble
import pytest


def test_bubble_sort_empty():
    assert Bubble.bubble_sort([]) == []


def test_bubble_sort_single_element():
    assert Bubble.bubble_sort([1]) == [1]


def test_bubble_sort():
    assert Bubble.bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
