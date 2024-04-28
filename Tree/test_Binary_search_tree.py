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
