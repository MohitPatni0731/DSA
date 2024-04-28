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


@pytest.fixture
def setup_tree_for_testing():
    # build root's subtree
    t = BinaryTree(1)
    left = t.insert_left(2)
    right = t.insert_right(3)

    # now build root's left child subtree
    left_subtree = left
    left_subtree.insert_left(4)
    left_subtree.insert_right(5)

    # now build root's right child subtree
    right_subtree = right
    right_subtree.insert_left(6)
    right_subtree.insert_right(7)

    return t  # notice that we have returned reference to root to refer to whole tree


def test_preorder(setup_tree_for_testing):
    assert setup_tree_for_testing.preorder() == [1, 2, 4, 5, 3, 6, 7]


def test_inorder(setup_tree_for_testing):
    assert setup_tree_for_testing.inorder() == [4, 2, 5, 1, 6, 3, 7]


def test_postorder(setup_tree_for_testing):
    assert setup_tree_for_testing.postorder() == [4, 5, 2, 6, 7, 3, 1]
