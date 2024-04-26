import pytest
from Binary_tree import BinaryTree


def test_set_root_value():
    root = BinaryTree(5)
    root.set_root(10)
    assert root.get_root() == 10


def test_set_root_value_string():
    root = BinaryTree(5)
    root.set_root("test")
    assert root.get_root() == "test"


def test_get_root_value():
    root = BinaryTree(2)
    assert root.get_root() == 2


def test_get_left():
    root = BinaryTree(5)
    root.insert_left(3)
    assert root.get_left().data == 3


def test_get_left_not_exist():
    root = BinaryTree(5)
    assert root.get_right() is None


def test_get_right():
    root = BinaryTree(5)
    root.insert_right(5)
    assert root.get_right().data == 5


def test_get_right_not_exist():
    root = BinaryTree(5)
    assert root.get_right() is None
