import pytest
from Binary_tree import BinaryTree


def test_set_root_value():
    root = BinaryTree(5)
    root.setRootVal(10)
    assert root.getRootVal() == 10


def test_set_root_value_string():
    root = BinaryTree(5)
    root.setRootVal("test")
    assert root.getRootVal() == "test"


def test_get_root_value():
    root = BinaryTree(2)
    assert root.getRootVal() == 2


def test_get_leftChild():
    root = BinaryTree(5)
    root.insert_leftChild(3)
    assert root.getLeftChild().data == 3


def test_get_leftChild_not_exist():
    root = BinaryTree(5)
    assert root.getLeftChild() is None


def test_get_rightChild():
    root = BinaryTree(5)
    root.insert_rightChild(5)
    assert root.getRightChild().data == 5


def test_get_rightChild_not_exist():
    root = BinaryTree(5)
    assert root.getRightChild() is None
