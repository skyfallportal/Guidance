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


'''
Certainly! This code demonstrates the Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms for traversing a graph. Here's a step-by-step explanation:

1. The `Graph` class is defined, representing an undirected graph. It has an adjacency list to store the graph's edges.

2. The `add_edge` method adds an edge between two vertices by appending each vertex to the other's adjacency list.

3. The `dfs` method performs a Depth-First Search traversal starting from a given vertex. It initializes a `visited` list to keep track of visited vertices and calls the `_dfs_util` method to perform the actual DFS traversal.

4. The `_dfs_util` method is a recursive helper function that takes a vertex `v` and the `visited` list as parameters. It marks the current vertex as visited, prints its value, and recursively calls itself for all unvisited neighbors of the current vertex.

5. The `bfs` method performs a Breadth-First Search traversal starting from a given vertex. It initializes a `visited` list and a `queue` data structure using the `deque` class from the `collections` module. The starting vertex is enqueued, marked as visited, and then the following steps are repeated until the queue becomes empty:
   - Dequeue a vertex `v` from the front of the queue.
   - Print the value of the dequeued vertex.
   - Enqueue all unvisited neighbors of the dequeued vertex and mark them as visited.

6. An instance of the `Graph` class is created with 5 vertices.

7. Edges are added to the graph using the `add_edge` method.

8. The DFS algorithm is tested by calling the `dfs` method with a starting vertex of 0. The DFS traversal starting from vertex 0 is printed.

9. The BFS algorithm is tested by calling the `bfs` method with a starting vertex of 0. The BFS traversal starting from vertex 0 is printed.

In the example graph, the following edges are added:
- Edge between vertex 0 and 1
- Edge between vertex 0 and 2
- Edge between vertex 1 and 3
- Edge between vertex 1 and 4

The output will be:
```
DFS traversal starting from vertex 0:
0 1 3 4 2

BFS traversal starting from vertex 0:
0 1 2 3 4
```

The DFS traversal visits vertices in depth-first order, exploring as far as possible along each branch before backtracking. The BFS traversal visits vertices in breadth-first order, exploring all the neighbors of a vertex before moving to the next level.
'''