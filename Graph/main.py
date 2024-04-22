from typing import Any
from collections import defaultdict


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

    def size_of_edges(self) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        length = 0
        for edge in self.adjacency_list:
            length += len(self.adjacency_list[edge])
        print(length // 2)

    def remove_edge(self, node1: Any, node2: Any) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].remove(node2)
            self.adjacency_list[node2].remove(node1)

    def remove_vertex(self, vertex: str) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]

    def print_graph(self) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        for node in self.adjacency_list:
            print(node, " -> ")
            print(", ".join(self.adjacency_list[node]))
