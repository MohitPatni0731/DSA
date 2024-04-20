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

    def remove_edge(self, edge) -> None:
        """
        Time -
        Space -
        """

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
