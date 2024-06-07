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
    Graph(int vertices) : vertices(vertices), adjacency_matrix(vertices, vector<int>(vertices, 0)) {}


    void add_edge(int node1, int node2) { 
        adjacency_matrix[node1][node2] = 1;
        adjacency_matrix[node2][node1] = 1;
    }

    bool is_empty() {
        if (vertices == 0) {
            return true;
        } else {
            return false;
        }
    }

    int size_of_vertices() {
        return vertices;
    }

    int size_of_edges() {
        int count = 0;
        for (int i = 0; i < vertices; ++i) {
            for (int j = i + 1; j < vertices; ++j) {
                if (adjacency_matrix[i][j] == 1) {
                    count++;
                }
            }
        }
        return count;
    }

    void remove_edge(int node1, int node2) {
        adjacency_matrix[node1][node2] = 0;
        adjacency_matrix[node2][node1] = 0;
    }

    void print_graph() {
        for (int i = 0; i < vertices; ++i) {
            for (int j = 0; j < vertices; ++j) {
                if (adjacency_matrix[i][j] == 1) {
                    cout << i << " -> " << j << endl;
                }
            }
        }
    }
};

void test_add_edge() {
    Graph graph(2);
    graph.add_edge(0, 1);
    assert(graph.adjacency_matrix[0][1] == 1);
    assert(graph.adjacency_matrix[1][0] == 1);
    cout << "1: test_add_edge() passed!" << endl; 
}

bool test_is_empty() {
    Graph graph(2);
    graph.add_edge(0, 1);
    assert(graph.is_empty()==false);
    cout << "2: test_is_empty() passed!" << endl;
    return true;
}

void test_size_of_edges() {
    Graph graph(3);
    graph.add_edge(0, 1);
    graph.add_edge(1, 2);
    assert(graph.size_of_edges() == 2);
    cout << "4: test_size_of_edges() passed!" << endl;
}

void test_remove_edge() {
    Graph graph(3);
    graph.add_edge(0, 1);
    graph.add_edge(1, 2);
    graph.remove_edge(0, 1);
    assert(graph.adjacency_matrix[0][1] == 0);
    assert(graph.adjacency_matrix[1][0] == 0);
    cout << "5: test_remove_edge() passed!" << endl;
}

void test_size_of_vertices() {
    Graph graph(2);
    graph.add_edge(0, 1);
    assert(graph.size_of_vertices()==2);
    cout << "3: test_size_of_vertices() passed!" << endl;
}

void test_empty_graph() {
    Graph graph2(0);
    assert(graph2.is_empty());
    cout << "4: test_empty_graph() passed!" << endl;
}

int main() {
    test_add_edge();
    test_is_empty();
    test_size_of_vertices();
    test_size_of_edges();
    test_remove_edge();
    test_empty_graph();
}
