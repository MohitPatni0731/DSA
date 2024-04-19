class Graph:
    def __init__(self, Nodes) -> None:
        """
        Time - O(1)
        Space - O(1)
        """
        self.nodes = Nodes
        self.adjacency_list = {}

    def print_graph(self) -> None:
        """
        Time - O(N)
        Space - O(1)
        """
        for node in self.nodes:
            print(node, " -> ", self.adjacency_list.get(node))


nodes = ["A", "B"]
graph = Graph(nodes)
graph.print_graph()
