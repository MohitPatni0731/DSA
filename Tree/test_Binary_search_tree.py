import pytest
from Binary_search_tree import BST


@pytest.fixture
def setup_tree_for_testing():
    t = BST(1)
    t.insert(2)
    t.insert(3)
    t.insert(6)
    t.insert(5)
    t.insert(7)
    return t


def test_preorder(setup_tree_for_testing):
    assert setup_tree_for_testing.preorder() == [1, 2, 3, 6, 5, 7]


def test_inorder(setup_tree_for_testing):
    assert setup_tree_for_testing.inorder() == [1, 2, 3, 5, 6, 7]


def test_postorder(setup_tree_for_testing):
    assert setup_tree_for_testing.postorder() == [5, 7, 6, 3, 2, 1]


def test_insert_duplicate():
    tree = BST(5)
    tree.insert(5)
    assert tree.preorder() == [5, 5]
    assert tree.inorder() == [5, 5]
    assert tree.postorder() == [5, 5]


def test_insert_left():
    tree = BST(5)
    tree.insert(3)
    assert tree.preorder() == [5, 3]
    assert tree.inorder() == [3, 5]
    assert tree.postorder() == [3, 5]


def test_insert_right():
    tree = BST(5)
    tree.insert(7)
    assert tree.preorder() == [5, 7]
    assert tree.inorder() == [5, 7]
    assert tree.postorder() == [7, 5]


def test_insert_left_and_right():
    tree = BST(5)
    tree.insert(3)
    tree.insert(7)
    assert tree.preorder() == [5, 3, 7]
    assert tree.inorder() == [3, 5, 7]
    assert tree.postorder() == [3, 7, 5]
