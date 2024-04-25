import pytest
from main import Graph


def test_add_edge():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert graph.adjacency_list == {1: [2], 2: [1, 3], 3: [2]}


def test_add_edge_same_value():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 2)
    assert graph.adjacency_list == {1: [2, 2], 2: [1, 1]}


def test_add_edge_empty_edge():
    graph = Graph()
    assert graph.add_edge(None, None) is None


def test_is_empty():
    graph = Graph()
    assert graph.is_empty() == True


def test_is_empty_not():
    graph = Graph()
    graph.add_edge(1, 2)
    assert graph.is_empty() == False


def test_size_of_vertices():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert graph.size_of_vertices() == 3


def test_size_of_vertices_empty_graph():
    graph = Graph()
    assert graph.size_of_vertices() == 0


def test_size_of_edges():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert graph.size_of_edges() == 2


def test_size_of_edges_empty_graph():
    graph = Graph()
    assert graph.size_of_edges() == 0


def test_remove_edge():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.remove_edge(1, 2)
    assert graph.adjacency_list == {1: [], 2: [3], 3: [2, 4], 4: [3]}


def test_remove_edge_non_existing():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert graph.remove_edge(4, 5) == None


def test_remove_edge_empty_graph():
    graph = Graph()
    assert graph.remove_edge(1, 2) == None


def test_print():
    graph = Graph()
    graph.add_edge("A", "B")
    assert graph.print_graph() == "A -> B\nB -> A\n"


def test_print_empty_graph():
    graph = Graph()
    assert graph.print_graph() == ""


def test_remove_vertex():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.remove_vertex("A")
    assert graph.adjacency_list == {"B": []}


def test_remove_vertex_from_empty_graph():
    graph = Graph()
    assert graph.remove_vertex("A") is None


def test_remove_vertex_non_existing_vertex():
    graph = Graph()
    graph.add_edge("A", "B")
    assert graph.remove_vertex("C") is None


def test_remove_vertex_duplicate_vertex():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("B", "A")
    graph.remove_vertex("B")
    assert graph.adjacency_list == {"A": []}
