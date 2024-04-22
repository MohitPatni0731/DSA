import pytest
from main import Graph


def test_add_edge():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert graph.adjacency_list == {1: [2], 2: [1, 3], 3: [2]}
