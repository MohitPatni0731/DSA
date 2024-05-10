// Graph implementation using adjacency matrix
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

class Graph {
public:
    int vertices;
    vector<vector<int>> adjacency_matrix;

public:
    void add_edge(int node1, int node2) {       
        adjacency_matrix[node1][node2] = 1;
        adjacency_matrix[node2][node1] = 1;
    }
};

void test_add_edge() {
    Graph graph;
    graph.add_edge(0, 1);
    assert(graph.adjacency_matrix[0][1] == 1);
    assert(graph.adjacency_matrix[1][0] == 1);
    cout << "1: test_add_edge() passed!" << endl; 
}

int main() {
    test_add_edge();
}
