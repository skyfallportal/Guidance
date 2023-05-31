## PRACTICAL NO: 03
## Implementing greedy search algorithm to find Kueuskal's MST:

from collections import defaultdict
class Graph:

	def __init__(self, vertices):
		self.V = vertices 
		self.graph = [] 
	
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])	

	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)
		
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	
	def KruskalMST(self):

		result = [] 		
		i = 0
		e = 0
		self.graph = sorted(self.graph,
					key=lambda item: item[2])

		parent = []
		rank = []		
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		
		while e < self.V - 1:
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)


		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree" , minimumCost)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()


'''
This code implements the Kruskal's algorithm for finding the Minimum Spanning Tree (MST) of a graph using a greedy approach. Here's a step-by-step explanation:

1. The `Graph` class represents a graph and has attributes such as the number of vertices (`V`) and the `graph` list to store the edges.

2. The `addEdge` method is used to add edges to the graph. It takes the source vertex (`u`), destination vertex (`v`), and weight (`w`) of the edge as parameters.

3. The `find` method implements the "find" operation of the disjoint set data structure. It is used to find the parent of a vertex in the set.

4. The `union` method implements the "union" operation of the disjoint set data structure. It is used to merge two sets by attaching the smaller rank tree to the root of the larger rank tree.

5. The `KruskalMST` method is the main function that implements Kruskal's algorithm to find the MST of the graph.

6. It initializes an empty list called `result` to store the edges of the MST.

7. The `graph` list is sorted in non-decreasing order based on the edge weights using a lambda function as the key for sorting.

8. Two additional lists, `parent` and `rank`, are initialized to keep track of the parent of each vertex and the rank of each vertex in the disjoint set data structure.

9. A loop is executed until `e` (the number of edges in the MST) is less than `V-1` (the number of vertices in the MST).

10. In each iteration, the smallest weight edge is selected from the sorted `graph` list.

11. The `find` method is used to find the parent of the source vertex (`u`) and the destination vertex (`v`).

12. If the parent of the source vertex and the destination vertex are different, it means adding this edge to the MST will not create a cycle.

13. The edge is added to the `result` list, and the `union` method is called to merge the sets of the source and destination vertices.

14. The total cost of the MST is calculated by summing the weights of all the edges in the `result` list.

15. Finally, the edges of the constructed MST and the minimum spanning tree cost are printed.

16. In the last section, an instance of the `Graph` class is created with `4` vertices.

17. Edges are added to the graph using the `addEdge` method.

18. The `KruskalMST` method is called to find the MST of the graph.

19. The edges of the MST and the minimum spanning tree cost are printed.

The code demonstrates the implementation of Kruskal's algorithm, which is a greedy algorithm for finding the minimum spanning tree of a graph. The algorithm starts with an empty set of edges and adds the edges in increasing order of their weights, while ensuring that no cycles are formed in the process. The resulting set of edges forms a minimum spanning tree of the graph.
'''