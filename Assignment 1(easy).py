from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start):
        visited = [False] * self.vertices
        self._dfs_util(start, visited)

    def _dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            v = queue.popleft()
            print(v, end=' ')

            for neighbor in self.adj_list[v]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


# Creating a graph with 5 vertices
g = Graph(5)

# Adding edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

# Testing the DFS algorithm
print("DFS traversal starting from vertex 0:")
g.dfs(0)
print()

# Testing the BFS algorithm
print("BFS traversal starting from vertex 0:")
g.bfs(0)
print()
