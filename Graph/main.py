from typing import Any
from collections import defaultdict

"""
This is Bidirectional graph
"""


class Graph:
    def __init__(self) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        self.adjacency_list = defaultdict(list)

    def add_edge(self, node1: Any, node2: Any) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def is_empty(self) -> bool:
        """
        Time - O(1)
        Space - O(1)
        """
        return len(self.adjacency_list) == 0

    def size_of_vertices(self) -> int:
        """
        Time - O(1)
        Space - O(1)
        """
        return len(self.adjacency_list)

    def size_of_edges(self) -> int:
        """
        Time - O(N)
        Space - O(1)
        """
        length = 0
        for edge in self.adjacency_list:
            length += len(self.adjacency_list[edge])
        return length // 2

    def remove_edge(self, node1: Any, node2: Any) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].remove(node2)
            self.adjacency_list[node2].remove(node1)

    def remove_vertex(self, vertex: str) -> None:
        # Time - O(N*N)
        """
        Space - O(1)
        """
        if vertex not in self.adjacency_list:
            return None

        # First remove this vertex from all of its neighbour's adjacency list
        for neighbour in self.adjacency_list[vertex]:  # iterating of a list is O(N)
            self.adjacency_list[neighbour].remove(
                vertex
            )  # remove method on a list is O(N)
        # Overall time complexity of above snippet is O(N) * O (N) = O(N*N)

        # Remove this vertex now after its reference is removed from everywhere
        del self.adjacency_list[vertex]  #  O(1)

    def print_graph(self) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        graph_in_str = ""
        for node in self.adjacency_list:
            graph_in_str += node + " -> " + ", ".join(self.adjacency_list[node]) + "\n"
        return graph_in_str
