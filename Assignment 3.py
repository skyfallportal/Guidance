from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def prim_mst(self):
        visited = [False] * self.V
        min_heap = PriorityQueue()
        min_heap.put((0, 0))
        cost = 0
        
        while not min_heap.empty():
            u, w = min_heap.get()
            
            if visited[u]:
                continue
            
            visited[u] = True
            cost += w
            
            for v, weight in self.graph[u]:
                if not visited[v]:
                    min_heap.put((v, weight))
        
        return cost


# Example usage
g = Graph(4)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 4)
mst_cost = g.prim_mst()
print("Minimum Spanning Tree Cost:", mst_cost)

'''
This code implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a weighted undirected graph. Prim's algorithm starts with an initial vertex and greedily adds the minimum weight edges to expand the tree until all vertices are included. Here's how the code works:

1. The `Graph` class is defined to represent a graph. The constructor takes the number of vertices as input and initializes an empty adjacency list `graph` with `vertices` number of lists.

2. The `add_edge` method is used to add an edge between vertices `u` and `v` with weight `w`. It adds the edge in both directions since the graph is undirected.

3. The `prim_mst` method implements Prim's algorithm to find the MST of the graph. It returns the total cost of the MST.

4. Inside the `prim_mst` method, a boolean list `visited` is created to keep track of visited vertices. Initially, all vertices are marked as unvisited.

5. A `PriorityQueue` named `min_heap` is created to store the edges with their weights. The priority is determined by the weight, so the edges with the minimum weight are always at the front of the queue.

6. The source vertex is initialized as vertex 0 (can be any vertex), and its weight is set to 0. The tuple `(0, 0)` is inserted into the `min_heap`.

7. A variable `cost` is initialized to 0 to keep track of the total cost of the MST.

8. The main loop runs until the `min_heap` is empty. In each iteration, the edge with the minimum weight is extracted from the `min_heap`.

9. If the vertex `u` of the extracted edge is already visited, it means that the edge leads to a vertex that has been included in the MST. In this case, the iteration continues to the next edge.

10. If the vertex `u` is not visited, it is marked as visited, and the weight `w` of the edge is added to the `cost`.

11. Next, the loop iterates over the adjacent vertices of `u`. If a vertex `v` is not visited, the edge `(v, weight)` is added to the `min_heap` to be considered for further expansion.

12. After the main loop ends, the `cost` variable holds the total cost of the MST, and it is returned.

13. In the example usage section, a graph with 4 vertices is created, and edges with their weights are added using the `add_edge` method.

14. The `prim_mst` method is called on the graph to find the MST cost, which is stored in the `mst_cost` variable.

15. Finally, the code prints the MST cost on the console.

The code demonstrates how to use the `Graph` class and the `prim_mst` method to find the MST of a graph using Prim's algorithm.
'''