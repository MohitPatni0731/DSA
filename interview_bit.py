from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer

    def adjacency_list(self, A, B):
        graph = defaultdict(list)
        for x, y in B:
            graph[x].append(y)
        return graph

    def solve(self, A, B, C):
        graph = self.adjacency_list(A, B)
        print(graph)
        visited = set()
        path_count = 0
        path_count = self.DFS(1, A, C, graph, visited, 0, path_count)
        return path_count

    def DFS(self, node, A, C, graph, visited, good_node, path_count):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                path_count = self.DFS(
                    neighbour,
                    A,
                    C,
                    graph,
                    visited,
                    good_node + 1 if A[node - 1] == 1 else good_node,
                    path_count,
                )

        if len(graph[node]) == 0 and good_node <= C:
            path_count += 1
        print(path_count, node, good_node, graph[node])
        return path_count


A = [0, 1, 0, 1, 1, 1]
B = [[1, 2], [1, 5], [1, 6], [2, 3], [2, 4]]
C = 1
a = Solution()
a.solve(A, B, C)



#interview bit solution
maxn = 100009
cnt = 0
ans = 0
adj = []
def ini():
    global maxn, adj, cnt, ans
    ans = 0
    cnt = 0
    adj = [[] for i in range(maxn)]
def dfs(u,p,A,C,):
    global adj, cnt, ans
    if A[u - 1]:
        cnt += 1
    isLeaf = 1
    for node in adj[u]:
        if node == p:
            continue
        isLeaf = 0
        dfs(node, u, A, C)
    if isLeaf and cnt <= C:
        ans += 1
    if A[u - 1]:
        cnt -= 1
    return
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self,A,B,C,):
        global maxn, adj, cnt, ans
        ini()
        for edge in B:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        dfs(1, 0, A, C)
        return ans
