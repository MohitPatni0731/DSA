class Graph:
    def __init__(self) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        self.adjacency_list = {}

    def add_edge(self, node_1, node_2) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        if node_1 not in self.adjacency_list:
            self.adjacency_list[node_1] = []
        if node_2 not in self.adjacency_list:
            self.adjacency_list[node_2] = []
        self.adjacency_list[node_1].append(node_2)
        self.adjacency_list[node_2].append(node_1)

    def add_vertex(self, vertex) -> None:
        """
        Time -
        Space -
        """

    def is_empty(self) -> None:
        """
        Time -
        Space -
        """
        return len(self.adjacency_list) == 0

    def size_of_vertices(self) -> None:
        """
        Time -
        Space -
        """

    def size_of_edges(self) -> None:
        """
        Time -
        Space -
        """
        length = 0
        for edge in self.adjacency_list:
            length += len(self.adjacency_list[edge])
        print(length // 2)

    def remove_edge(self, node_1, node_2) -> None:
        """
        Time -
        Space -
        """
        if node_1 and node_2 in self.adjacency_list:
            self.adjacency_list[node_1].remove(node_2)
            self.adjacency_list[node_2].remove(node_1)

    def remove_vertex(self, vertex) -> None:
        """
        Time -
        Space -
        """

    def print_graph(self) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        for node in self.adjacency_list:
            print(node, " -> ", self.adjacency_list[node])


graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
graph.add_edge("D", "E")
graph.add_edge("E", "A")
graph.print_graph()
graph.size_of_edges()
graph.is_empty()
graph.remove_edge("A", "B")
graph.print_graph()
